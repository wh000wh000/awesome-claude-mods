#!/usr/bin/env python3
"""
awesome-claude-mods :: collect.py

Stage 1 of the update pipeline: gather raw candidates from public sources.

Design rules (inherited from the Jev 巡检 layer):
  * stdlib only -- no pip install, so GitHub Actions stays fast and reproducible
  * append-only evidence -- every candidate keeps the URL that produced it
  * SHA-256 change detection -- a source whose payload is unchanged contributes
    nothing, so an unchanged 2-hour tick produces an empty diff (no commit spam)
  * external content is DATA, never instructions

Sources:
  github_repos  -- GitHub Search API across a query matrix
  github_code   -- GitHub Code Search for the mod API surface (corroborator only)
  hackernews    -- HN Algolia (stories + comments)
  changelog     -- the official Claude Code CHANGELOG, the hardest fact available
                   in a field that is days old

On the word "mod": it is one of the most overloaded tokens in software -- game
mods, modulo, moderators, and as a substring of module/model/modern/modify. The
queries below are deliberately phrase-heavy rather than relying on the bare word,
and curate.py carries the exclusion rules plus a test suite for them.

Output:
  data/raw/<source>.json     normalized candidate batches
  data/state/<key>.hash      change-detection baseline
"""

from __future__ import annotations

import hashlib
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
STATE = ROOT / "data" / "state"
RAW.mkdir(parents=True, exist_ok=True)
STATE.mkdir(parents=True, exist_ok=True)

CST = timezone(timedelta(hours=8))
NOW = datetime.now(CST)
STAMP = NOW.isoformat(timespec="seconds")

def _read_gh_token() -> str | None:
    """Fall back to the local gh CLI token when running on a workstation."""
    try:
        import subprocess

        out = subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, timeout=10
        )
        return out.stdout.strip() or None
    except Exception:
        return None


TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or _read_gh_token()

UA = "awesome-claude-mods/1.0 (+https://github.com/wh000wh000/awesome-claude-mods)"


# --------------------------------------------------------------------------
# http
# --------------------------------------------------------------------------
def http_json(url: str, *, headers: dict | None = None, tries: int = 4):
    """GET a JSON document with bounded retries and 403/429 backoff."""
    hdrs = {"User-Agent": UA, "Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    delay = 2.0
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as exc:
            if exc.code in (403, 429, 502, 503) and attempt < tries - 1:
                wait = delay + random.uniform(0, 1.5)
                if exc.headers.get("X-RateLimit-Remaining") == "0":
                    reset = exc.headers.get("X-RateLimit-Reset")
                    if reset and reset.isdigit():
                        wait = max(wait, min(int(reset) - time.time() + 2, 70))
                        wait = max(wait, 1)
                print(f"    .. HTTP {exc.code}, retry in {wait:.1f}s", file=sys.stderr)
                time.sleep(wait)
                delay = min(delay * 2, 30)
                continue
            print(f"    !! HTTP {exc.code} {url}", file=sys.stderr)
            return None
        except Exception as exc:  # noqa: BLE001 - network noise must never abort a tick
            if attempt < tries - 1:
                time.sleep(delay)
                delay = min(delay * 2, 30)
                continue
            print(f"    !! {type(exc).__name__}: {exc}", file=sys.stderr)
            return None
    return None


# --------------------------------------------------------------------------
# change detection
# --------------------------------------------------------------------------
def digest(obj) -> str:
    payload = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def changed(key: str, obj) -> bool:
    """True when `obj` differs from the stored baseline (and store the new one)."""
    safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in key)
    path = STATE / f"{safe}.hash"
    new = digest(obj)
    old = path.read_text().strip() if path.exists() else None
    if old == new:
        return False
    path.write_text(new + "\n")
    return True


# --------------------------------------------------------------------------
# source: GitHub repositories
# --------------------------------------------------------------------------
REPO_QUERIES = [
    # Phrase queries first. The bare word "mod" is never used on its own: it
    # returns Minecraft, modulo and moderation at a ratio of hundreds to one.
    "claude code mod",
    "claude code mods",
    "claude mods",
    "claude-code mod",
    "claude code plugin",
    "claude-code plugin",
    "cc-plugin",
    "claude code hooks",
    "claude code marketplace",
    "claude code skill",
    "claude code subagent",
    "claude code statusline",
    "anthropic claude code",
    "cordis plugin",
    "dsh plugin",
    "topic:claude-code",
    "topic:claude-code-plugin",
    "topic:claude-code-plugins",
    "topic:claude-code-hooks",
    "topic:claude-code-marketplace",
    "topic:claude-code-mod",
    "topic:claude-mods",
    "topic:claude-skills",
    "topic:anthropic",
    "topic:cordis",
    "topic:dsh",
]

# The queries above are sorted by recency, which surfaces new work but has a
# blind spot: a canonical, high-star repository that has not been pushed lately
# never reaches the first page of 100 results. These are sorted by stars, which
# is the complementary view.
REPO_QUERIES_BY_STARS = [
    "claude code",
    "claude code plugin",
    "claude code mods",
    "claude-code",
    "awesome claude code",
    "claude code hooks",
    "anthropic",
]


def collect_github_repos() -> list[dict]:
    if not TOKEN:
        print("  !! no GITHUB_TOKEN -- skipping GitHub repository search", file=sys.stderr)
        return []

    found: dict[str, dict] = {}
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    for q, sort in ([(q, "updated") for q in REPO_QUERIES]
                    + [(q, "stars") for q in REPO_QUERIES_BY_STARS]):
        url = (
            "https://api.github.com/search/repositories?q="
            + urllib.parse.quote(q)
            + f"&sort={sort}&order=desc&per_page=100"
        )
        data = http_json(url, headers=headers)
        if not data:
            continue
        items = data.get("items") or []
        print(f"    github_repos[{q}/{sort}] -> {len(items)}")
        for it in items:
            full = it.get("full_name")
            if not full:
                continue
            # keep the richest record if the same repo matches several queries
            existing = found.get(full)
            rec = {
                "source": "github",
                "full_name": full,
                "url": it.get("html_url"),
                "description": (it.get("description") or "").strip(),
                "topics": it.get("topics") or [],
                "language": it.get("language"),
                "stars": it.get("stargazers_count", 0),
                "forks": it.get("forks_count", 0),
                "open_issues": it.get("open_issues_count", 0),
                "created_at": it.get("created_at"),
                "pushed_at": it.get("pushed_at"),
                "archived": bool(it.get("archived")),
                "is_fork": bool(it.get("fork")),
                "homepage": it.get("homepage") or "",
                "license": ((it.get("license") or {}) or {}).get("spdx_id"),
                "matched_queries": [q],
            }
            if existing:
                existing["matched_queries"] = sorted(
                    set(existing["matched_queries"]) | {q}
                )
                if rec["stars"] > existing["stars"]:
                    rec["matched_queries"] = existing["matched_queries"]
                    found[full] = rec
            else:
                found[full] = rec
        time.sleep(2.2)  # stay well inside the 30 req/min search limit

    return list(found.values())


# --------------------------------------------------------------------------
# source: the official organisation (seeded explicitly)
# --------------------------------------------------------------------------
# Repository search ranks by recency, so the vendor's own repositories are easily
# buried under the thousands of community ones that merely mention Claude Code.
# They are the most important entries in the list, so they are fetched from the
# org endpoint instead of being left to chance.
#
# The org is swept but not trusted wholesale: Anthropic publishes SDKs, cookbooks
# and unrelated tools under the same account, and the first sweep of the Jev list
# pulled in a vLLM fork and a Pulumi provider. Only names that belong to Claude
# Code itself are kept.
OFFICIAL_ORGS = ["anthropics"]
OFFICIAL_NAME_ALLOW = re.compile(r"claude", re.I)


def collect_official_org() -> list[dict]:
    if not TOKEN:
        return []
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    found: dict[str, dict] = {}
    for org in OFFICIAL_ORGS:
        for page in (1, 2):
            url = (f"https://api.github.com/orgs/{org}/repos"
                   f"?per_page=100&page={page}&sort=updated")
            data = http_json(url, headers=headers)
            if not isinstance(data, list) or not data:
                break
            print(f"    official_org[{org} p{page}] -> {len(data)}")
            for it in data:
                full = it.get("full_name")
                if not full:
                    continue
                found[full] = {
                    "source": "github",
                    "full_name": full,
                    "url": it.get("html_url"),
                    "description": (it.get("description") or "").strip(),
                    "topics": it.get("topics") or [],
                    "language": it.get("language"),
                    "stars": it.get("stargazers_count", 0),
                    "forks": it.get("forks_count", 0),
                    "open_issues": it.get("open_issues_count", 0),
                    "created_at": it.get("created_at"),
                    "pushed_at": it.get("pushed_at"),
                    "archived": bool(it.get("archived")),
                    "is_fork": bool(it.get("fork")),
                    "homepage": it.get("homepage") or "",
                    "license": ((it.get("license") or {}) or {}).get("spdx_id"),
                    "matched_queries": [f"org:{org}"],
                    "official": True,
                }
            time.sleep(1.0)
    return list(found.values())


# --------------------------------------------------------------------------
# source: GitHub code search (finds real integration snippets)
# --------------------------------------------------------------------------
# The tokens a mod actually uses. These are corroborators, never a grade on
# their own: `ui.render` and `agent.spawn` are generic enough to appear in
# unrelated code, so curate.py requires a second signal before it will call a
# repository observed.
CODE_QUERIES = [
    "cc-plugin-you-should-know",
    "ui.fault",
    "$.ui.selection",
    "$.agent.list",
    "ui.render claude",
    "claude code mod.json",
    "claude-mods",
]

def collect_github_code() -> list[dict]:
    if not TOKEN:
        return []
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.text-match+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    out: dict[str, dict] = {}
    for q in CODE_QUERIES:
        url = (
            "https://api.github.com/search/code?q="
            + urllib.parse.quote(q)
            + "&per_page=50"
        )
        data = http_json(url, headers=headers, tries=3)
        if not data:
            continue
        items = data.get("items") or []
        print(f"    github_code[{q}] -> {len(items)}")
        for it in items:
            repo = (it.get("repository") or {}).get("full_name")
            if not repo:
                continue
            rec = out.setdefault(
                repo,
                {
                    "source": "github_code",
                    "full_name": repo,
                    "url": f"https://github.com/{repo}",
                    "paths": [],
                    "matched_queries": [],
                },
            )
            p = it.get("path")
            if p and p not in rec["paths"]:
                rec["paths"].append(p)
            if q not in rec["matched_queries"]:
                rec["matched_queries"].append(q)
        time.sleep(2.2)
    return list(out.values())


# --------------------------------------------------------------------------
# source: curated seed list
# --------------------------------------------------------------------------
# The documented contribution path. A newcomer who knows about a project the
# automated rules miss adds its `owner/repo` here, and the next tick picks it
# up. This exists because no relevance filter is perfect: a project can be
# genuinely part of the ecosystem while describing itself in words the rules do
# not know.
SEED_PATH = ROOT / "data" / "seed.json"


def collect_seeded() -> list[dict]:
    if not TOKEN or not SEED_PATH.exists():
        return []
    try:
        seed = json.loads(SEED_PATH.read_text())
        wanted = [s for s in (seed.get("repositories") or []) if "/" in s]
    except Exception as exc:  # noqa: BLE001
        print(f"  !! could not read data/seed.json: {exc}", file=sys.stderr)
        return []

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    out: list[dict] = []
    for full in wanted:
        it = http_json(f"https://api.github.com/repos/{full}", headers=headers, tries=2)
        if not isinstance(it, dict) or not it.get("full_name"):
            print(f"    seeded[{full}] -> not found")
            continue
        print(f"    seeded[{full}] -> ok")
        out.append({
            "source": "seed",
            "full_name": it["full_name"],
            "url": it.get("html_url"),
            "description": (it.get("description") or "").strip(),
            "topics": it.get("topics") or [],
            "language": it.get("language"),
            "stars": it.get("stargazers_count", 0),
            "forks": it.get("forks_count", 0),
            "open_issues": it.get("open_issues_count", 0),
            "created_at": it.get("created_at"),
            "pushed_at": it.get("pushed_at"),
            "archived": bool(it.get("archived")),
            "is_fork": bool(it.get("fork")),
            "homepage": it.get("homepage") or "",
            "license": ((it.get("license") or {}) or {}).get("spdx_id"),
            "matched_queries": ["seed"],
            "seeded": True,
        })
        time.sleep(0.4)
    return out


# --------------------------------------------------------------------------
# source: Hacker News
# --------------------------------------------------------------------------
HN_QUERIES = ["Claude Code mods", "Claude Code plugins", "Claude Code mod",
              "Claude Code", "Claude Mods"]


def collect_hackernews() -> list[dict]:
    out: dict[str, dict] = {}
    for q in HN_QUERIES:
        for kind in ("story", "comment"):
            url = (
                "https://hn.algolia.com/api/v1/search_by_date?query="
                + urllib.parse.quote(q)
                + f"&tags={kind}&hitsPerPage=40"
            )
            data = http_json(url, headers={"Accept": "application/json"}, tries=3)
            if not data:
                continue
            hits = data.get("hits") or []
            print(f"    hackernews[{q}/{kind}] -> {len(hits)}")
            for h in hits:
                oid = str(h.get("objectID") or "")
                if not oid:
                    continue
                title = (h.get("title") or h.get("story_title") or "").strip()
                body = (h.get("comment_text") or h.get("story_text") or "") or ""
                body = body[:400]
                rec = {
                    "source": "hackernews",
                    "id": oid,
                    "url": f"https://news.ycombinator.com/item?id={oid}",
                    "kind": kind,
                    "title": title,
                    "text": body,
                    "points": h.get("points") or 0,
                    "num_comments": h.get("num_comments") or 0,
                    "author": h.get("author"),
                    "created_at": h.get("created_at"),
                    "matched_query": q,
                }
                out[oid] = rec
            time.sleep(0.6)
    return list(out.values())


# --------------------------------------------------------------------------
# source: HuggingFace
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# source: the official CHANGELOG
# --------------------------------------------------------------------------
# The field is days old and mostly undocumented. The vendor's own changelog is
# the only place that states what a mod is and what it can touch, so it is a
# source in its own right rather than background reading.
CHANGELOG_URL = (
    "https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md"
)
# Lines that concern the mod surface. Kept narrow on purpose: the changelog is
# mostly unrelated fixes, and a loose match would fill the list with them.
MOD_LINE = re.compile(
    r"\bmods?\b|cc-plugin-|ui\.render|ui\.fault|agent\.spawn|"
    r"\$\.ui\.selection|\$\.agent\.list",
    re.I,
)
# Measured, not guessed: this pattern selects 15 lines out of the whole file
# where a looser one that also matched the bare word "plugin" selected 528. The
# 15 are the mod API surface itself -- ui.render, pane/band/card/button,
# agent.spawn, $.ui.selection, the Client region, ui.fault. The 528 were
# unrelated plugin fixes.


def collect_changelog() -> list[dict]:
    """Mod-related entries from the official Claude Code CHANGELOG."""
    req = urllib.request.Request(CHANGELOG_URL, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            text = resp.read().decode("utf-8", "replace")
    except Exception as exc:  # noqa: BLE001
        print(f"    !! changelog: {type(exc).__name__}: {exc}", file=sys.stderr)
        return []

    # The file is a flat list of versions, newest first, each heading followed by
    # its bullet points.
    version = ""
    out: list[dict] = []
    for line in text.splitlines():
        head = re.match(r"^##\s*(.+?)\s*$", line)
        if head:
            version = head.group(1).strip()
            continue
        if not line.strip().startswith(("-", "*")):
            continue
        body = line.strip().lstrip("-*").strip()
        if len(body) < 15 or not MOD_LINE.search(body):
            continue
        out.append({
            "source": "changelog",
            "version": version,
            "text": body,
            "url": f"https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md",
        })
    print(f"    changelog -> {len(out)} mod-related lines")
    return out


def write_raw(name: str, items: list[dict]) -> bool:
    """Persist a batch and report whether it actually changed."""
    blob = {"collected_at": STAMP, "count": len(items), "items": items}
    is_new = changed(f"raw_{name}", items)
    path = RAW / f"{name}.json"
    if is_new or not path.exists():
        path.write_text(json.dumps(blob, ensure_ascii=False, indent=1) + "\n")
    return is_new


def collect_repos_with_official() -> list[dict]:
    """Repo search, the official org sweep and the curated seed list, merged."""
    found = {r["full_name"]: r for r in collect_github_repos() if r.get("full_name")}
    for r in collect_official_org() + collect_seeded():
        full = r["full_name"]
        if full in found:
            found[full].update({k: v for k, v in r.items() if k != "matched_queries"})
            found[full]["matched_queries"] = sorted(
                set(found[full].get("matched_queries") or [])
                | set(r.get("matched_queries") or []))
        else:
            found[full] = r
    return list(found.values())


def main() -> int:
    only = set()
    for i, a in enumerate(sys.argv):
        if a == "--only" and i + 1 < len(sys.argv):
            only = set(sys.argv[i + 1].split(","))

    print(f"== awesome-claude-mods :: collect @ {STAMP} ==")
    print(f"   token: {'yes' if TOKEN else 'NO (github sources will be skipped)'}"
          + (f"  sources: {','.join(sorted(only))}" if only else ""))

    def repos_seeded_only() -> list[dict]:
        """Merge just the seed list into the existing repo batch."""
        existing = {}
        path = RAW / "github_repos.json"
        if path.exists():
            try:
                existing = {r["full_name"]: r
                            for r in json.loads(path.read_text()).get("items", [])
                            if r.get("full_name")}
            except Exception:  # noqa: BLE001
                existing = {}
        for r in collect_official_org() + collect_seeded():
            existing[r["full_name"]] = r
        return list(existing.values())

    collectors = [
        ("github_repos", repos_seeded_only if "seed" in only else collect_repos_with_official),
        ("github_code", collect_github_code),
        ("hackernews", collect_hackernews),
        ("changelog", collect_changelog),
    ]
    if only - {"seed"}:
        collectors = [c for c in collectors if c[0] in only]
    elif only:
        collectors = [c for c in collectors if c[0] == "github_repos"]

    batches: dict[str, list[dict]] = {}
    total = 0
    touched = []
    # Each source is written the moment it finishes, so a slow or failing later
    # source can never discard the work of an earlier one.
    for name, fn in collectors:
        try:
            items = fn()
        except Exception as exc:  # noqa: BLE001 - one bad source must not abort the tick
            print(f"  !! {name} failed: {type(exc).__name__}: {exc}", file=sys.stderr)
            items = []
        batches[name] = items
        if not items:
            touched.append(f"{name}=0")
            continue
        total += len(items)
        dirty = write_raw(name, items)
        touched.append(f"{name}={len(items)}{'*' if dirty else ''}")
        print(f"   -> wrote data/raw/{name}.json")

    print(f"   candidates: {total}  ({', '.join(touched)})")
    print("   (* = source payload changed this tick)")

    manifest = {
        "collected_at": STAMP,
        "counts": {k: len(v) for k, v in batches.items()},
        "total": total,
    }
    (RAW / "_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=1) + "\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())