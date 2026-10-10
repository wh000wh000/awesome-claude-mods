#!/usr/bin/env python3
"""
awesome-claude-mods :: curate.py

Stage 2: turn raw candidates into the published index.

This stage is deliberately DETERMINISTIC and LLM-FREE. The list is rebuilt every
two hours from CI, so a model in the loop would make the output drift between
ticks and make any diff unreadable. Every decision here is a rule you can audit.

What it does
  1. Normalize each raw candidate into one entry record.
  2. Reject name collisions -- repos that merely contain the letters "jev"
     (JeVois machine vision, JEvents, Jevil/Deltarune, jEveAssets, JEval, ...).
     Competitor lists include several of these; excluding them is the point.
  3. Assign exactly one category (direct Jev application domain).
  4. Assign a tier (official / community) and an evidence grade
     (official / observed / inferred / unverified) in the 巡检 four-level scheme.
  5. Preserve first_seen across ticks, track star history, merge human overrides.
  6. Append new entries to data/CHANGELOG.md (append-only, never rewritten).

Inputs   data/raw/*.json, data/entries.json (previous), data/overrides.json
Outputs  data/entries.json, data/stats.json, data/CHANGELOG.md
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
DATA = ROOT / "data"
CST = timezone(timedelta(hours=8))
NOW = datetime.now(CST)
STAMP = NOW.isoformat(timespec="seconds")

OFFICIAL_OWNERS = {"anthropics", "anthropic"}

# Belonging to the official organisation is not by itself evidence of being a
# Jev artifact. The org also carries unrelated repositories that predate the
# product (LLaDA, vllm, pulumi-clickhouse, Overwatch, daggerverse), so the
# official tier is still gated by relevance -- with an allowlist for the
# official pages that carry no description of their own.
OFFICIAL_ALLOWLIST = {
    "anthropics/claude-code",
    "anthropics/claude-code-action",
    "anthropics/claude-code-sdk-python",
    "anthropics/claude-code-sdk-typescript",
    "anthropics/claude-code-security-review",
    "anthropics/claude-agent-sdk-python",
    "anthropics/claude-agent-sdk-typescript",
}

# Curated, not exhaustive: below this a repository only stays if the author
# declared Jev in the repository name or in an explicit topic tag.
MIN_STARS = 3

# Retention. The published page has a hard ceiling of roughly 512 KB, so the
# list has to choose what to keep instead of compacting everything until no card
# can show anything. An entry is dropped when it offers a reader nothing to act
# on: no traction, no independent evidence that it is used, and no description
# explaining what it is. A name and a URL is not an entry.
#
# Deliberately not age-based. Every zero-star repository in this ecosystem was
# created within three days, so a "stale" rule would bite nothing -- the honest
# statement is not that these are old, it is that they are empty.
RETENTION_MIN_STARS = 5
RETENTION_MIN_DESCRIPTION = 40

# Discussion noise floor. A 1-point link submission is not an ecosystem signal,
# and HN comment bodies are chatter rather than evidence.
MIN_HN_POINTS = 2

# --------------------------------------------------------------------------
# 1. Name-collision blocklist
# --------------------------------------------------------------------------
# These repositories contain the substring "jev" but have nothing to do with
# TypeSafe's Jev. Every pattern below was verified by hand against the live
# repository. Keeping this list explicit (rather than a clever heuristic) is
# what makes the exclusion auditable.
# Our own repository. It matches every relevance rule by construction -- its
# name contains "jev" and its scripts contain the API endpoints -- and listing
# yourself in your own index is both useless and the source of a real media bug:
# the entry harvested another project's recording out of our own README.
SELF_REPOS = {"wh000wh000/awesome-claude-mods"}

COLLISION_REPOS = {
    "jevois/jevois", "jevois/jevoisbase", "jevois/jevois-sdk",
    "jevois/jevois-tutorials", "jevois/jevois-inventor",
    "jevois/jevois-core", "jevois/jevois-core-sdk",
    "patrickpoirier51/JeVois--Python-Tracking",
    "JEvents/JEvents",
    "KRLW890/jevil-simulator", "jeviljester/Verity",
    "GoldenGnu/jeveassets",
    "jevajs/Jeva",
    "QAInsights/JEval",
    "jlop007/jevelin", "AlexandruStanica/Jevelin",
    "ur001/Jevix",
    "simonc/jeveuxapprendreruby.fr",
    "MohawkMEDIC/jeverest",
    "jevinskie/jevmachopp", "jevinskie/jevxpctrace",
    "jeroenvermeulen/JeVe_EasyOTA",
    "grakic/jevrc",
    "tmptrash/jevo",
    "gnlow/Jevi",
    "OpenJEVis/JEVis",
}

# Competitor aggregators are NOT collisions: they are real Jev ecosystem
# artifacts and a reader benefits from seeing them. They are listed under
# "文章、讨论与视频" with an explicit note so the list stays honest about
# the fact that it is not the only one of its kind.
COMPETITOR_LISTS = {
    "Anil-matcha/awesome-jev-by-typesafe",
    "AbdelStark/awesome-typesafe",
    "yibie/awesome-jev",
    "cobanov/awesome-jev",
    "AnotiaWang/awesome-jev",
    "hellogumbo/awesome-jev",
    "OmniJev/awesome-jev",
    "aliaihub/awesome-jev-usecases",
}

# Substring patterns that disqualify a record outright.
# Substring patterns that disqualify a record outright.
#
# This list is the whole defence against the central risk of this project. "mod"
# is one of the most overloaded tokens in software, and a naive search for it
# returns, in rough order of volume: game mods, moderation bots, modulo, and
# Apache's mod_* namespace. Each family below was a real hit during collection.
#
# Deliberately NOT here: module, model, modern, modify. `\bmods?\b` cannot match
# them -- the word boundary requires a non-word character after "mod" -- and
# listing them would drop legitimate mods that happen to discuss a module.
COLLISION_PATTERNS = [
    # --- game modding
    r"minecraft", r"neoforge", r"curseforge", r"modrinth", r"\bmoddb\b",
    r"garrys?mod", r"\bgmod\b", r"\bskyrim\b", r"\bfallout\b",
    r"factorio", r"rimworld", r"terraria", r"stardew", r"\bbukkit\b",
    r"\bspigot\b", r"papermc", r"\bbedrock\b", r"game\s?mod",
    r"steam\s?workshop", r"modpack", r"modding",
    # --- moderation, which is the single largest false-positive family
    r"moderat", r"automod", r"auto[\s\-_]?mod\b", r"mod[\s\-_]?bot",
    r"discord.*\bmod\b", r"reddit.*\bmod\b", r"twitch.*\bmod\b",
    r"\bmods?\b.*\b(ban|mute|warn|kick)\b", r"chat\s?filter",
    # --- arithmetic
    r"\bmodulo\b", r"\bmodulus\b", r"modular\s+arithmetic",
    r"\bmodpow\b", r"\bmodinv\b", r"mod\s?pow\b", r"\bmod\s*%",
    # --- Apache and friends: legitimate uses of the word-boundary token
    r"mod_python", r"mod_wsgi", r"mod_php", r"mod_perl", r"mod_jk",
    r"mod_rewrite", r"mod_security", r"mod_ssl", r"mod_proxy",
    r"apache\s+mod", r"nginx.*\bmod\b",
    # --- a bare "mod" repository with no Claude anywhere is not ours; this is
    #     handled by the pairing rule, not here
]

# --------------------------------------------------------------------------
# 2. Relevance rules
# --------------------------------------------------------------------------
# Precision is this list's entire value proposition, so relevance is decided by
# a two-signal rule rather than a keyword soup. The naive approach fails badly:
#
#   "typesafe" is generic software vocabulary  -> middleapi/orpc
#                                                 ("Typesafe APIs Made Simple")
#                                                 TanStack/router, http4k
#   "RLCD" is also Reflective LCD hardware     -> waveshareteam/ESP32-S3-RLCD-4.2
#   "noul" is also a programming language      -> betaveros/noulith
#   "jev" as a substring is a surname/initial  -> jevinskie/*, Jevanleeuwen/*
#
# So: an unambiguous signal accepts on its own. An ambiguous one must be paired
# with a domain word before the repository is treated as part of the ecosystem.

# Unambiguous: a single hit is sufficient. These name the mod surface itself.
STRONG_PATTERNS = [
    # The mod surface itself: the hook a mod draws through, the primitives it
    # draws with, the agents it may spawn, and the built-in mod's own name.
    r"ui\.render", r"ui\.fault", r"\$\.ui\.selection", r"\$\.agent\.list",
    r"agent\.spawn",
    r"cc[\s\-_]plugin[\s\-_]you[\s\-_]should[\s\-_]know",
    r"\bclaude[\s\-_]code[\s\-_]mods?\b",
    r"\bclaude[\s\-_]mods?\b",
    r"\bmods?\b[\s\-_]?(api|sdk|surface|interface)\b",
]

# "Claude Code plugin" is deliberately NOT strong. It was, and it admitted 783
# repositories: the plugin ecosystem is large and predates mods by months. This
# list is about the layer that came after -- mods, and the deeper behaviour they
# may change -- so a plain plugin qualifies only when it also touches the mod
# surface.
PLUGIN_PLATFORM = [r"\bcordis\b", r"\bdsh\b", r"\bclaude\b",
                   r"claude[\s\-_]code", r"cc[\s\-_]plugin"]

# Ambiguous: needs at least one DOMAIN word alongside it.
#
#   mod      game mods, moderation, modulo, mod_python
#   plugin   WordPress, Vim, Figma, a hundred other hosts
#   skill    "skills" is generic resume/HR vocabulary
#   hook     React hooks, git hooks, webhooks
#   claude   also a French given name, and Claude Monet
#   dsh      also a shell and several other acronyms
#   cordis   also a medical device company
MEDIUM_PATTERNS = [
    r"\bmods?\b",
    r"\bplugins?\b",
    r"\bskills?\b",
    r"\bhooks?\b",
    r"\bclaude\b",
    r"\banthropic\b",
    r"\bcordis\b",
    r"\bdsh\b",
    r"claude[\s\-_]code",
]

# --------------------------------------------------------------------------
# The mod surface: what this list is actually about
# --------------------------------------------------------------------------
# The criterion is not "is it a Claude Code extension" but "does it use the
# capability Claude Code gained in 2.1.287". Measured against the candidate set:
# of 909 entries that passed the earlier, looser rule, only 391 name any part of
# the mod surface in their own text -- and 406 of the 409 in the plugin category
# named none of it. Those were plugins, which is a different and much older
# thing.
#
# Every pattern below is something the author had to have read the mod
# documentation to write. A repository that merely says "a Claude Code plugin"
# is not evidence of anything.
MOD_SURFACE_PATTERNS = [
    # the hook a mod draws through, and the guarantee that it fails alone
    r"ui\.render", r"ui\.fault",
    # what it reads and spawns
    r"\$\.ui\.selection", r"\$\.agent\.list", r"agent\.spawn",
    r"\bteammates?\b",
    # what it draws with
    r"\bpanes?\b", r"\bbands?\b", r"\bcards?\b", r"\bbuttons?\b",
    r"\bmods?\b[\s\-_]?(api|surface|interface|hook)",
    r"client[\s\-_]?(region|area)",
    # the built-in mod, by name
    r"cc-plugin-you-should-know",
    # the one-line interface a mod owns outright
    r"\bstatus\s?lines?\b",
    # self-description. The user of this list accepts "the repository says it is
    # a mod" as evidence, and it is the signal most of the real ones carry.
    r"\bmods?\b",
]

# Words that can only mean this list's host. Mod-surface evidence counts only
# beside one of these, because "a pane in a terminal" is not a Claude Code mod.
PLATFORM_PATTERNS = [
    r"\bclaude\b", r"claude[\s\-_]code", r"\banthropic\b",
    r"cc[\s\-_]plugin", r"\bcordis\b", r"\bdsh\b",
]

# An explicit repository topic is the author's own classification. Topics
# corroborate an entry; they never admit one on their own, because topic-stuffing
# is common on high-star link lists.
TOPIC_TOKENS = {
    "claude", "claude-code", "claude-ai", "claude-code-plugin",
    "claude-code-plugins", "claude-code-mod", "claude-mods",
    "claude-code-hooks", "claude-code-marketplace", "claude-plugins",
    "claude-skills", "claude-code-skills", "claude-code-subagents",
    "claude-code-statusline", "anthropic", "anthropic-claude",
    "cordis", "cordis-plugin", "dsh", "dsh-plugin",
}

# Domain words that prove an ambiguous mention was meant in the Claude Code
# sense. Generic words (ai, llm, agent, tool, dev, code) are deliberately
# absent: they co-occur with everything.
DOMAIN_PATTERNS = [
    r"\bclaude\b", r"claude[\s\-_]code", r"\banthropic\b",
    r"cc[\s\-_]plugin", r"\bcordis\b", r"\bdsh\b",
    r"marketplace", r"statusline", r"subagent", r"teammate",
    r"\bslash[\s\-_]?command", r"\bprompt\b", r"\bsession\b",
    r"\bterminal\b", r"\bfullscreen\b", r"\bpane\b", r"\bband\b",
    r"\bcard\b", r"\bbutton\b",
]

# A name that literally contains the token "jev" (split on separators and
# camelCase) is accepted even without a description -- NanoJev, jev-router,
# jev-review -- because the author named the project after the product.
def medium_signal(haystack: str) -> bool:
    """
    True when the entry provides evidence that it uses the mod surface.

    Two things must both hold: the text names this host, and the text names
    something only a mod would name. A plain "Claude Code plugin" satisfies
    neither half of the second condition, which is the point -- the plugin
    ecosystem predates mods and is an order of magnitude larger.

    This replaced a looser rule that admitted any mechanism word beside any
    platform word. It read plausibly and, measured, kept 909 entries of which
    518 named no part of the mod surface at all.
    """
    if not any_match(PLATFORM_PATTERNS, haystack):
        return False
    # On DSH and Cordis the plugin *is* the mod mechanism -- those hosts have no
    # deeper layer to reach into -- so a plugin there is evidence by itself.
    if re.search(r"\bcordis\b|\bdsh\b", haystack, re.I) and \
            re.search(r"\bplugins?\b|\bmods?\b|\bhooks?\b", haystack, re.I):
        return True
    return any_match(MOD_SURFACE_PATTERNS, haystack)


# A name that itself names the platform, which is the author classifying the
# project for us -- claude-statusline, cordis-mods, cc-plugin-foo.
#
# Only distinctive words qualify. The Jev list could use its own name as a token
# because nothing else is called "jev"; here, "plugin", "mod", "skill" and
# "hook" are among the most common words in software, and treating them as a
# pass admitted `vim-plugin`, `figma-plugin` and `webpack-plugin` on the name
# alone. The test suite caught it.
NAME_TOKENS = {"claude", "anthropic", "cordis"}
NAME_PATTERNS = [
    r"cc[\s\-_]?(plugin|mod)",
    r"claude[\s\-_]?code",
    r"\bclaude[\s\-_]?mods?\b",
]


def name_has_domain_token(repo_name: str) -> bool:
    if any_match(NAME_PATTERNS, repo_name or ""):
        return True
    parts: list[str] = []
    for chunk in re.split(r"[-_.\s]+", repo_name or ""):
        parts.extend(re.findall(r"[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[A-Z]+|\d+", chunk) or [chunk])
    return any(p.lower() in NAME_TOKENS for p in parts if p)


# Only categories that are populated. The earlier rule admitted the whole
# Claude Code plugin ecosystem and needed eight headings to hold it; once the
# criterion became evidence of mod-surface use, five of those headings were
# empty, and a heading with nothing under it is worse than no heading.
CATEGORIES = [
    ("official", "官方：Anthropic 的 Claude Code 仓库与发布说明", [
        r"^anthropics/", r"\bofficial\b",
    ]),
    ("mods", "Mods：真正使用 mod 能力做出来的东西", [
        r"\bmods?\b", r"ui\.render", r"ui\.fault", r"\$\.ui\.selection",
        r"agent\.spawn", r"\bstatus\s?lines?\b", r"\bpanes?\b",
        r"\bbands?\b", r"\bcards?\b", r"\bbuttons?\b", r"\bteammates?\b",
    ]),
    ("dsh-cordis", "DSH 与 Cordis 的插件生态", [
        r"\bdsh\b", r"deepseek harness", r"\bcordis\b",
    ]),
    # Explicit rather than a silent fallback. A list should say what belongs
    # here, not accept whatever matched nothing above.
    ("other", "其他项目", []),
    ("writing", "文章、讨论与视频", [
        r"awesome", r"curated", r"catalogue", r"catalog", r"directory",
        r"blog", r"article", r"write.?up", r"discussion", r"newsletter",
        r"reading", r"interview", r"podcast", r"tutorial", r"guide",
        r"handbook", r"cheatsheet", r"show hn",
    ]),
]

DEFAULT_CATEGORY = ("other", "其他项目")

CATEGORY_ORDER = ["official", "mods", "dsh-cordis", "writing", "other"]

CATEGORY_TITLES = {key: title for key, title, _patterns in CATEGORIES}
CATEGORY_TITLES[DEFAULT_CATEGORY[0]] = DEFAULT_CATEGORY[1]

# A language-complete index is a listed requirement, so record the
# implementation language of every code entry even when it is not the primary
# organising axis.
LANG_ALIASES = {
    "jupyter notebook": "Jupyter",
    "c++": "C++",
    "c#": "C#",
    "objective-c": "Objective-C",
}


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def any_match(patterns: list[str], text: str) -> bool:
    return any(re.search(p, text, re.I) for p in patterns)


def load_raw(name: str) -> list[dict]:
    path = RAW / f"{name}.json"
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text()).get("items", [])
    except Exception:  # noqa: BLE001
        return []


def norm_lang(value: str | None) -> str:
    if not value:
        return ""
    return LANG_ALIASES.get(value.strip().lower(), value.strip())


def is_collision(full_name: str, haystack: str) -> bool:
    if full_name in COLLISION_REPOS:
        return True
    return any(re.search(p, haystack, re.I) for p in COLLISION_PATTERNS)


def categorize(text: str, full_name: str) -> str:
    if not text and not full_name:
        return DEFAULT_CATEGORY[0]
    for key, _title, patterns in CATEGORIES:
        if any_match(patterns, text):
            return key
    return DEFAULT_CATEGORY[0]


# Entries removed by the retention policy, collected for the audit trail.
DROPPED: list[dict] = []


def is_substantive(e: dict) -> bool:
    """
    Whether a repository gives a reader anything to act on.

    Any single signal is enough: the vendor published it, someone was found
    using it, it has traction, or its author explained what it does. What fails
    is the entry that is only a name.
    """
    if e.get("tier") == "official":
        return True
    if e.get("evidence") == "observed":
        return True
    if e.get("in_code_search"):
        return True
    if int(e.get("stars") or 0) >= RETENTION_MIN_STARS:
        return True
    if len((e.get("summary") or "").strip()) >= RETENTION_MIN_DESCRIPTION:
        return True
    return False


def evidence_grade(tier: str, in_code: bool, strong: bool, explicit: bool) -> str:
    """
    巡检 four-level scheme, applied to a repository.

    The grades only earn their place if they discriminate, so each one is tied
    to a different kind of proof:

      official    published by TypeSafe itself
      observed    proof of real use -- the project turned up in a code search for
                  a Jev-specific API token, or its own text cites typesafe.ai
      inferred    the author declared Jev in the repository name or an explicit
                  topic tag, but no code-level evidence was seen
      unverified  matched only on an ambiguous term plus domain vocabulary
    """
    if tier == "official":
        return "official"
    if in_code or strong:
        return "observed"
    if explicit:
        return "inferred"
    return "unverified"


# --------------------------------------------------------------------------
# repo candidates
# --------------------------------------------------------------------------
def build_repo_entries(repos: list[dict], code_repos: set[str]) -> list[dict]:
    out: list[dict] = []
    rejected: list[tuple[str, str]] = []

    for r in repos:
        full = r.get("full_name") or ""
        if not full:
            continue
        owner = full.split("/")[0].lower()
        repo_name = full.split("/")[-1]
        desc = r.get("description") or ""
        topics = " ".join(r.get("topics") or [])
        # The owner is deliberately excluded from the relevance haystack. If the
        # full name is searched, every repository under `typesafe-ai/` matches
        # the official-org pattern -- which is how LLaDA, vllm, Overwatch and
        # pulumi-clickhouse, all unrelated leftovers, were being graded strong.
        haystack = f"{repo_name} {desc} {topics}"
        full_haystack = f"{full} {desc} {topics}"

        if is_collision(full, full_haystack) or full in SELF_REPOS:
            rejected.append((full, "self" if full in SELF_REPOS else "name collision"))
            continue

        strong = any_match(STRONG_PATTERNS, haystack)
        medium = medium_signal(haystack)
        domain = any_match(DOMAIN_PATTERNS, haystack)
        topics_l = {(t or "").strip().lower() for t in (r.get("topics") or [])}
        topic_hit = bool(topics_l & TOPIC_TOKENS)
        name_hit = name_has_domain_token(repo_name)
        in_code = full in code_repos

        # Admission rule. Code search is a CORROBORATOR, never sufficient on its
        # own: a large repository can contain the string "jev" by accident.
        # Topic tags corroborate too, but do not admit: anything_about_game, a
        # 4.1k-star game-dev link list, carries a `jev` topic it has no use for.
        allowlisted = full in OFFICIAL_ALLOWLIST
        # A human explicitly added this repository to data/seed.json. That
        # bypasses the automated filters but not the evidence grading, because
        # a human saying "include this" is not the same as verifying what it does.
        seeded = bool(r.get("seeded"))
        # A name is not evidence of use. `name_hit` stays in the grading below,
        # where "the author named it after the mod surface" is a fair
        # corroborator, but it no longer admits: hundreds of repositories are
        # called claude-something and extend the client in no way at all.
        accepted = (strong or (medium and domain) or allowlisted or seeded)
        if not accepted:
            why = ("official but off-topic" if owner in OFFICIAL_OWNERS
                   else "no mod-surface evidence")
            rejected.append((full, why))
            continue

        stars = int(r.get("stars") or 0)
        official = owner in OFFICIAL_OWNERS

        # Quality bar. This is a curated list, not an exhaustive dump: a
        # repository that matched only on weak vocabulary and has no traction is
        # noise rather than signal.
        if not (stars >= MIN_STARS or official or strong or name_hit or seeded
                or full in COMPETITOR_LISTS):
            rejected.append((full, "below quality bar"))
            continue

        tier = "official" if official else "community"
        if official:
            # Anything published by TypeSafe belongs in the start-here section,
            # regardless of what its description happens to mention.
            category = "official"
        elif full in COMPETITOR_LISTS:
            category = "writing"
        else:
            category = categorize(haystack, full)

        out.append({
            "id": f"gh:{full}",
            "kind": "repo",
            "name": full,
            "url": r.get("url") or f"https://github.com/{full}",
            "owner": full.split("/")[0],
            "repo": full.split("/")[-1],
            "summary": desc,
            "category": category,
            "tier": tier,
            "evidence": evidence_grade(
                tier, in_code, strong, name_hit or topic_hit or allowlisted),
            "language": norm_lang(r.get("language")),
            "license": r.get("license") or "",
            "stars": stars,
            "forks": int(r.get("forks") or 0),
            "open_issues": int(r.get("open_issues") or 0),
            "created_at": r.get("created_at") or "",
            "pushed_at": r.get("pushed_at") or "",
            "archived": bool(r.get("archived")),
            "is_fork": bool(r.get("is_fork")),
            "homepage": r.get("homepage") or "",
            "topics": r.get("topics") or [],
            "in_code_search": in_code,
            "is_sibling_list": full in COMPETITOR_LISTS,
            "matched_queries": r.get("matched_queries") or [],
        })

    kept: list[dict] = []
    for e in out:
        if is_substantive(e):
            kept.append(e)
        else:
            DROPPED.append({
                "at": STAMP, "id": e["id"], "name": e["name"], "url": e["url"],
                "stars": e.get("stars", 0), "evidence": e.get("evidence"),
                "description_chars": len((e.get("summary") or "").strip()),
                "reason": "no traction, no independent evidence, no description",
            })
    if DROPPED:
        print(f"   retention: dropped {len(DROPPED)} entries with no traction, "
              f"no independent evidence and no description")
    out = kept

    reasons: dict[str, int] = {}
    for _f, why in rejected:
        reasons[why] = reasons.get(why, 0) + 1
    print(f"   relevance: rejected {len(rejected)} ({reasons})")
    return out


def build_submission_entries(subs: list[dict]) -> list[dict]:
    """
    Turn hand-curated submissions into entries.

    These exist because repository search is structurally blind to work that
    shows up first, or only ever, as a post with a screen recording. They are
    graded like anything else: a human choosing to include something is not the
    same as verifying it, so a submission still lands at `inferred` unless the
    person who added it actually watched the artifact, which is recorded by the
    evidence field they set.
    """
    out: list[dict] = []
    for s in subs:
        sid = s.get("id")
        if not sid or not s.get("url"):
            continue
        # Sibling lists and submissions share the category vocabulary, so an
        # unknown category is a mistake worth surfacing rather than silently
        # dumping into the fallback bucket.
        category = s.get("category") or DEFAULT_CATEGORY[0]
        if category not in CATEGORY_ORDER:
            print(f"  !! submission {sid}: unknown category {category!r}")
            category = DEFAULT_CATEGORY[0]

        summary_map = s.get("summary") or {}
        title_map = s.get("title") or {}
        notes_map = s.get("notes") or {}
        posted = s.get("posted_at") or ""

        out.append({
            "id": sid,
            "kind": "post",
            "name": title_map.get("en") or summary_map.get("en", "")[:60] or sid,
            "title_i18n": title_map,
            "url": s["url"],
            "owner": s.get("author_handle") or s.get("author") or "",
            "author": s.get("author") or "",
            "author_handle": s.get("author_handle") or "",
            "author_url": s.get("author_url") or "",
            "posted_at": posted,
            "summary": summary_map.get("en", ""),
            "summary_i18n": summary_map,
            "notes_i18n": notes_map,
            "notes": notes_map.get("en", ""),
            "category": category,
            "tier": s.get("tier", "community"),
            "evidence": s.get("evidence", "inferred"),
            "language": s.get("language") or "",
            "license": "",
            "stars": 0,
            "forks": 0,
            "created_at": posted,
            "pushed_at": posted,
            "topics": ["submission", s.get("platform") or ""],
            "metrics": s.get("metrics") or {},
            "project_url": s.get("project_url") or "",
            "project_label": s.get("project_label") or {},
            "replies_url": s.get("replies_url") or "",
            "declared_media": s.get("media") or {},
            "is_submission": True,
            "source_note": s.get("source_note") or "",
        })
    return out


def build_knowledge_entries(items: list[dict], taken: set[str]) -> list[dict]:
    """
    Turn our own collection log into entries.

    These are the half of the ecosystem a repository search cannot see: the
    official pages that were read and verified, the independent production
    tests, the write-ups, the disputes. The log already grades its evidence in
    the same four levels this list uses, so nothing is re-judged here.

    A URL already present from another source is skipped: the same page should
    not appear twice under two headings.
    """
    out: list[dict] = []
    for it in items:
        url = (it.get("url") or "").strip()
        title = (it.get("title") or "").strip()
        if not url or not title or url in taken:
            continue
        taken.add(url)
        point = (it.get("point") or "").strip() or title
        out.append({
            "id": "note:" + hashlib.sha1(url.encode()).hexdigest()[:16],
            "kind": "note",
            "name": title,
            "url": url,
            "owner": "",
            "summary": point,
            "notes": (it.get("impact") or "").strip(),
            "category": "writing",
            "tier": "community",
            "evidence": it.get("evidence") or "inferred",
            "language": "",
            "license": "",
            "stars": 0,
            "forks": 0,
            "created_at": it.get("date") or "",
            "pushed_at": it.get("date") or "",
            # No topics: the log's own labels are internal evidence notation.
            "topics": [],
            # The collection log is written in Chinese, so its records are a
            # non-English source. Every edition -- English included -- needs a
            # translation lookup for them.
            "source_lang": "zh",
            "source_note": it.get("source_note") or "",
            "seen_days": it.get("seen_days", 1),
        })
    return out


def build_changelog_entries(lines: list[dict]) -> list[dict]:
    """
    The official changelog, as entries.

    This field is days old and almost undocumented: the changelog is the only
    place that states what a mod is and what it may touch. That makes it the
    highest-grade content in the whole list, and it is graded `official` because
    the vendor wrote it -- not because we verified it.

    One entry per version rather than per line: fifteen separate cards all
    reading "Fixed a mod's ..." would be noise, while one card per release that
    lists what that release settled about the mod surface is exactly what a
    reader building a mod needs.
    """
    by_version: dict[str, list[dict]] = {}
    for ln in lines:
        v = (ln.get("version") or "").strip()
        if not v:
            continue
        by_version.setdefault(v, []).append(ln)

    out: list[dict] = []
    for version, items in by_version.items():
        texts = [i.get("text", "").strip() for i in items if i.get("text")]
        if not texts:
            continue
        # The changelog's own order: the release that introduced mods first,
        # then its fixes. Kept verbatim because this is a primary source and
        # paraphrasing it would be the one place a mistake could hide.
        summary = " ".join(texts)[:600]
        out.append({
            "id": f"cc:{version}",
            "kind": "release",
            "name": f"Claude Code {version} — the mod surface",
            "url": ("https://github.com/anthropics/claude-code/blob/main/"
                    "CHANGELOG.md"),
            "owner": "anthropics",
            "summary": summary,
            "notes": "",
            "category": "official",
            "tier": "official",
            "evidence": "official",
            "language": "",
            "license": "",
            "stars": 0,
            "forks": 0,
            "created_at": "",
            "pushed_at": "",
            "topics": [],
            "release_version": version,
            "release_lines": texts,
            "is_release_note": True,
        })
    return out


def build_model_entries(models: list[dict]) -> list[dict]:
    out = []
    for m in models:
        mid = m.get("id") or ""
        tags = " ".join(m.get("tags") or [])
        haystack = f"{mid} {tags} {m.get('pipeline_tag') or ''}"
        if not any_match(STRONG_PATTERNS, haystack):
            continue
        out.append({
            "id": f"hf:{mid}",
            "kind": "model",
            "name": mid,
            "url": m.get("url"),
            "owner": mid.split("/")[0],
            "summary": "",
            "category": "research-models",
            "tier": "community",
            "evidence": "observed",
            "language": "",
            "license": "",
            "stars": 0,
            "forks": 0,
            "downloads": int(m.get("downloads") or 0),
            "likes": int(m.get("likes") or 0),
            "pushed_at": m.get("last_modified") or "",
            "created_at": "",
            "topics": m.get("tags") or [],
        })
    return out


def build_discussion_entries(hits: list[dict]) -> list[dict]:
    """
    Hacker News items, filtered for signal.

    Comment bodies are dropped: 306 raw hits produced 47 comment records whose
    only qualification was that the word "jev" appeared somewhere in the thread,
    which is noise in a curated index. Stories must clear the points floor and
    match in the TITLE, because the title is what a reader can act on.
    """
    out = []
    for h in hits:
        if (h.get("kind") or "story") != "story":
            continue
        points = int(h.get("points") or 0)
        if points < MIN_HN_POINTS:
            continue
        title = h.get("title") or ""
        # A story belongs here when its title names the mod surface. The filter
        # still carried the previous project's keywords, so every mod-related
        # submission was being read as unrelated and dropped.
        if not (any_match(MOD_SURFACE_PATTERNS, title)
                and any_match(PLATFORM_PATTERNS, title)):
            continue
        if is_collision("", title):
            continue
        oid = h.get("id")
        out.append({
            "id": f"hn:{oid}",
            "kind": "story",
            "name": title,
            "url": h.get("url"),
            "owner": h.get("author") or "",
            "summary": re.sub(r"<[^>]+>", " ", h.get("text") or "")[:280].strip(),
            "category": "writing",
            "tier": "community",
            "evidence": "observed",
            "stars": points,
            "forks": int(h.get("num_comments") or 0),
            "created_at": h.get("created_at") or "",
            "pushed_at": h.get("created_at") or "",
            "language": "",
            "license": "",
            "topics": [],
            "hn_points": points,
        })
    return out


# --------------------------------------------------------------------------
# merge with previous state
# --------------------------------------------------------------------------
def merge(previous: dict[str, dict], fresh: list[dict]) -> tuple[list[dict], list[dict]]:
    """Keep first_seen, track star history, report genuinely new entries."""
    merged: list[dict] = []
    new_entries: list[dict] = []
    seen: set[str] = set()

    for e in fresh:
        eid = e["id"]
        seen.add(eid)
        old = previous.get(eid)
        if old:
            e["first_seen"] = old.get("first_seen", STAMP)
            e["last_seen"] = STAMP
            hist = list(old.get("history") or [])
            stars = e.get("stars", 0)
            if not hist or hist[-1].get("stars") != stars:
                hist.append({"t": STAMP, "stars": stars})
            e["history"] = hist[-30:]
            e["stars_delta"] = stars - (old.get("stars") or stars)
            e["is_new"] = False
        else:
            e["first_seen"] = STAMP
            e["last_seen"] = STAMP
            e["history"] = [{"t": STAMP, "stars": e.get("stars", 0)}]
            e["stars_delta"] = 0
            e["is_new"] = True
            new_entries.append(e)
        e["seen_count"] = (old or {}).get("seen_count", 0) + 1
        merged.append(e)
    return merged, new_entries


def apply_overrides(entries: list[dict], overrides: dict) -> list[dict]:
    """
    Human/agent layer. Overrides win, but can never delete an entry that the
    collector keeps finding; they can only refine it or force-exclude it by id.
    """
    blocked = set(overrides.get("exclude") or [])
    by_id = overrides.get("entries") or {}
    out = []
    for e in entries:
        if e["id"] in blocked:
            continue
        ov = by_id.get(e["id"]) or {}
        for key in ("summary", "category", "tier", "evidence", "featured",
                    "media", "title", "notes"):
            if key in ov:
                e[key] = ov[key]
        out.append(e)
    return out


# --------------------------------------------------------------------------
# ranking inside a category
# --------------------------------------------------------------------------
def rank_key(e: dict):
    ev_rank = {"official": 0, "observed": 1, "inferred": 2, "unverified": 3}
    return (
        0 if e.get("featured") else 1,
        ev_rank.get(e.get("evidence", "unverified"), 4),
        -int(e.get("stars") or 0),
        e.get("name", "").lower(),
    )


def main() -> int:
    print(f"== awesome-claude-mods :: curate @ {STAMP} ==")

    repos = load_raw("github_repos")
    code = load_raw("github_code")
    models = load_raw("huggingface")
    hits = load_raw("hackernews")
    changelog = load_raw("changelog")
    print(f"   raw: repos={len(repos)} code={len(code)} changelog={len(changelog)} hn={len(hits)}")

    code_repos = {c.get("full_name") for c in code if c.get("full_name")}
    code_paths = {c.get("full_name"): c.get("paths") or [] for c in code}

    submissions = []
    sub_path = DATA / "submissions.json"
    if sub_path.exists():
        try:
            submissions = json.loads(sub_path.read_text()).get("submissions", [])
        except Exception as exc:  # noqa: BLE001
            print(f"  !! could not read submissions.json: {exc}", file=sys.stderr)
    print(f"   submissions: {len(submissions)}")

    knowledge = []
    kpath = DATA / "knowledge.json"
    if kpath.exists():
        try:
            knowledge = json.loads(kpath.read_text()).get("entries", [])
        except Exception as exc:  # noqa: BLE001
            print(f"  !! could not read knowledge.json: {exc}", file=sys.stderr)
    print(f"   collection log: {len(knowledge)} entries")

    fresh = (
        build_changelog_entries(changelog)
        + build_repo_entries(repos, code_repos)
        + build_model_entries(models)
        + build_discussion_entries(hits)
        + build_submission_entries(submissions)
    )
    # De-duplicate against everything already found, so a page our own log
    # recorded does not appear twice.
    taken = {e["url"] for e in fresh}
    fresh += build_knowledge_entries(knowledge, taken)
    print(f"   relevant candidates: {len(fresh)}")

    prev_path = DATA / "entries.json"
    previous: dict[str, dict] = {}
    if prev_path.exists():
        try:
            doc = json.loads(prev_path.read_text())
            previous = {e["id"]: e for e in doc.get("entries", [])}
        except Exception as exc:  # noqa: BLE001
            print(f"  !! could not read previous entries.json: {exc}", file=sys.stderr)

    overrides = {}
    ov_path = DATA / "overrides.json"
    if ov_path.exists():
        try:
            overrides = json.loads(ov_path.read_text())
        except Exception as exc:  # noqa: BLE001
            print(f"  !! could not read overrides.json: {exc}", file=sys.stderr)

    merged, new_entries = merge(previous, fresh)
    merged = apply_overrides(merged, overrides)

    # attach code-search evidence paths, which prove real integration
    for e in merged:
        if e["kind"] == "repo" and e["name"] in code_paths:
            paths = code_paths[e["name"]][:6]
            e["code_paths"] = paths
            if e.get("evidence") == "inferred":
                e["evidence"] = "observed"

    merged.sort(key=lambda e: (CATEGORY_ORDER.index(e["category"])
                               if e["category"] in CATEGORY_ORDER else 99,
                               rank_key(e)))

    dropped = previous.keys() - {e["id"] for e in merged}
    if dropped:
        print(f"   note: {len(dropped)} previously listed entries no longer match")

    if DROPPED:
        dpath = DATA / "dropped.json"
        old_dropped = []
        if dpath.exists():
            try:
                old_dropped = json.loads(dpath.read_text()).get("entries", [])
            except Exception:  # noqa: BLE001
                old_dropped = []
        # Keep the first time an entry was dropped, and refresh its signals, so
        # the decision can be reviewed and reversed without re-deriving it.
        seen = {d["id"]: d for d in old_dropped}
        for d in DROPPED:
            if d["id"] in seen:
                seen[d["id"]]["last_seen_dropped"] = STAMP
                seen[d["id"]]["stars"] = d["stars"]
                seen[d["id"]]["description_chars"] = d["description_chars"]
            else:
                d["first_dropped"] = STAMP
                seen[d["id"]] = d
        dpath.write_text(json.dumps(
            {"updated_at": STAMP, "count": len(seen),
             "policy": {"min_stars": RETENTION_MIN_STARS,
                        "min_description_chars": RETENTION_MIN_DESCRIPTION},
             "entries": sorted(seen.values(), key=lambda x: x["name"])},
            ensure_ascii=False, indent=1) + "\n")

    payload = {
        "generated_at": STAMP,
        "count": len(merged),
        "categories": CATEGORY_ORDER,
        "category_titles": CATEGORY_TITLES,
        "entries": merged,
    }
    prev_path.write_text(json.dumps(payload, ensure_ascii=False, indent=1) + "\n")

    # ------------------------------------------------------------------
    # stats
    # ------------------------------------------------------------------
    by_cat: dict[str, int] = {}
    by_ev: dict[str, int] = {}
    by_lang: dict[str, int] = {}
    by_tier: dict[str, int] = {}
    for e in merged:
        by_cat[e["category"]] = by_cat.get(e["category"], 0) + 1
        by_ev[e.get("evidence", "unverified")] = by_ev.get(e.get("evidence", "unverified"), 0) + 1
        by_tier[e.get("tier", "community")] = by_tier.get(e.get("tier", "community"), 0) + 1
        lang = e.get("language") or ""
        if lang:
            by_lang[lang] = by_lang.get(lang, 0) + 1

    stats = {
        "generated_at": STAMP,
        "total": len(merged),
        "new_this_tick": len(new_entries),
        "by_category": by_cat,
        "by_evidence": by_ev,
        "by_tier": by_tier,
        "by_language": dict(sorted(by_lang.items(), key=lambda kv: -kv[1])),
        "repos": sum(1 for e in merged if e["kind"] == "repo"),
        "models": sum(1 for e in merged if e["kind"] == "model"),
        "discussions": sum(1 for e in merged if e["kind"] in ("story", "comment")),
        "total_stars": sum(int(e.get("stars") or 0) for e in merged),
    }
    (DATA / "stats.json").write_text(json.dumps(stats, ensure_ascii=False, indent=1) + "\n")

    # ------------------------------------------------------------------
    # append-only changelog
    # ------------------------------------------------------------------
    log_path = DATA / "CHANGELOG.md"
    if not log_path.exists():
        log_path.write_text(
            "# CHANGELOG — awesome-claude-mods\n\n"
            "> Append-only record of what changed, and when.\n"
            "> Historical lines are never rewritten; corrections are added as new lines.\n\n"
        )
    # only record a run that actually changed something
    if new_entries or not prev_path.exists():
        lines = [f"\n## {STAMP}\n"]
        lines.append(f"- 收录总数 **{len(merged)}**；本次更新新增 **{len(new_entries)}**\n")
        for e in sorted(new_entries, key=lambda x: -int(x.get("stars") or 0))[:25]:
            lines.append(
                f"- `+` [{e['name']}]({e['url']}) — {e.get('evidence')} / "
                f"{e.get('category')} — ⭐{e.get('stars', 0)}\n"
            )
        if len(new_entries) > 25:
            lines.append(f"- …另有 {len(new_entries) - 25} 条新增\n")
        with log_path.open("a") as fh:
            fh.writelines(lines)

    print(f"   entries: {len(merged)}  new: {len(new_entries)}")
    print(f"   by category: {by_cat}")
    print(f"   by evidence: {by_ev}")
    print(f"   languages: {len(by_lang)} -> {list(by_lang)[:8]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())