#!/usr/bin/env python3
"""
awesome-claude-mods :: build_site.py

Builds the GitHub Pages site into docs/.

Why a site
----------
A repository is discovered through its name, description, topics and star count.
None of those show what makes this list different: that every entry carries an
evidence grade, that it is rebuilt every two hours, or that it publishes in
twenty languages. A page can show all three at once, and it is a URL that can be
linked, indexed and shared independently of GitHub's ranking.

The site is generated exactly like the READMEs: one template, data from
data/entries.json. It is English with links to the twenty editions, rather than
twenty generated sites, because a reader searching for "Jev projects" is
overwhelmingly searching in English.

Outputs
  docs/index.html   the page (self-contained: no CDN, no build step, no JS deps)
  docs/site.json    the data it reads
"""

from __future__ import annotations

import html
import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
CST = timezone(timedelta(hours=8))
NOW = datetime.now(CST)
STAMP = NOW.isoformat(timespec="seconds")

REPO_URL = "https://github.com/wh000wh000/awesome-claude-mods"
SITE_URL = "https://wh000wh000.github.io/awesome-claude-mods/"

CATEGORY_EMOJI = {
    "official": "🏛️", "mods": "🧩", "plugins": "🔌", "hooks-automation": "🪝",
    "marketplaces": "🏪", "dev-tooling": "🛠️", "writing": "📰", "other": "📦",
}
EVIDENCE_EMOJI = {"official": "✅", "observed": "👁️",
                  "inferred": "🔎", "unverified": "❓"}
EVIDENCE_ORDER = ["official", "observed", "inferred", "unverified"]
LANGS = [("en", "English"), ("zh-CN", "简体中文"), ("zh-TW", "繁體中文"),
         ("ja", "日本語"), ("ko", "한국어"), ("es", "Español"),
         ("fr", "Français"), ("de", "Deutsch"), ("pt-BR", "Português"),
         ("ru", "Русский"), ("it", "Italiano"), ("ar", "العربية"),
         ("hi", "हिन्दी"), ("tr", "Türkçe"), ("vi", "Tiếng Việt"),
         ("th", "ไทย"), ("id", "Bahasa Indonesia"), ("pl", "Polski"),
         ("nl", "Nederlands"), ("uk", "Українська")]


def esc(t) -> str:
    return html.escape(str(t or ""), quote=True)


def strip_md(t: str) -> str:
    """The site renders plain text; the source carries markdown emphasis."""
    t = re.sub(r"`([^`]*)`", r"\1", str(t or ""))
    t = re.sub(r"\*\*([^*]*)\*\*", r"\1", t)
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def build_payload(entries: list[dict], stats: dict, media: dict) -> dict:
    out = []
    for e in entries:
        m = media.get(e["id"]) or {}
        out.append({
            "n": e.get("name", ""),
            "u": e.get("url", ""),
            "c": e.get("category", ""),
            "e": e.get("evidence", "unverified"),
            "t": e.get("tier", "community"),
            "s": int(e.get("stars") or 0),
            "l": e.get("language") or "",
            "d": strip_md(e.get("summary") or "")[:300],
            "k": e.get("kind", "repo"),
            "g": (e.get("topics") or [])[:6],
            "i": bool(m.get("image")),
            "f": str(e.get("first_seen") or "")[:10],
            "p": str(e.get("pushed_at") or "")[:10],
        })
    return {
        "generated_at": STAMP,
        "total": stats.get("total", len(out)),
        "new_this_tick": stats.get("new_this_tick", 0),
        "by_category": stats.get("by_category", {}),
        "by_evidence": stats.get("by_evidence", {}),
        "by_language": stats.get("by_language", {}),
        "categories": CATEGORY_EMOJI,
        "evidence_order": EVIDENCE_ORDER,
        "entries": out,
    }


PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Awesome Claude Mods — an evidence-graded index, rebuilt every 2 hours</title>
<meta name="description" content="A live index of the Jev / TypeSafe System One ecosystem: __TOTAL__ entries across SDKs, MCP tooling, agent guardrails, evaluations and open models. Every entry carries an evidence grade. Rebuilt every two hours.">
<meta property="og:title" content="Awesome Claude Mods — evidence-graded, rebuilt every 2 hours">
<meta property="og:description" content="__TOTAL__ Claude Code mods, plugins and hooks, graded by how much was actually verified. 20 language editions.">
<meta property="og:image" content="https://raw.githubusercontent.com/wh000wh000/awesome-claude-mods/main/assets/readme/hero.png">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><text y='24' font-size='24'>🔥</text></svg>">
<style>
  :root{
    --bg:#0b0f14; --panel:#0e141b; --line:#1f2a36; --fg:#e6edf3;
    --muted:#8b98a5; --primary:#14b8a6; --accent:#f0a93b; --blue:#7dd3fc;
    --violet:#c4b5fd; --red:#f87171; --green:#4ade80;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--fg);
    font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
    -webkit-font-smoothing:antialiased}
  a{color:var(--primary);text-decoration:none}
  a:hover{text-decoration:underline}
  .wrap{max-width:1080px;margin:0 auto;padding:0 20px}
  header{border-bottom:1px solid var(--line);background:linear-gradient(180deg,#0e141b,var(--bg))}
  .hero{width:100%;display:block;border-radius:0 0 12px 12px}
  h1{font-size:clamp(28px,5vw,44px);margin:22px 0 6px;letter-spacing:-.02em}
  .tag{color:var(--muted);margin:0 0 18px;font-size:clamp(15px,2.2vw,18px)}
  .bar{display:flex;flex-wrap:wrap;gap:18px;padding:14px 0;border-top:1px solid var(--line);
    border-bottom:1px solid var(--line);color:var(--muted);font-size:14px}
  .bar b{color:var(--fg)}
  .pulse{display:inline-block;width:8px;height:8px;border-radius:50%;
    background:var(--green);margin-right:7px;box-shadow:0 0 0 0 rgba(74,222,128,.7);
    animation:p 2s infinite}
  @keyframes p{0%{box-shadow:0 0 0 0 rgba(74,222,128,.6)}70%{box-shadow:0 0 0 9px rgba(74,222,128,0)}100%{box-shadow:0 0 0 0 rgba(74,222,128,0)}}
  .controls{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 8px}
  input[type=search]{flex:1 1 260px;background:var(--panel);border:1px solid var(--line);
    color:var(--fg);border-radius:10px;padding:11px 14px;font-size:15px;outline:none}
  input[type=search]:focus{border-color:var(--primary)}
  .chips{display:flex;flex-wrap:wrap;gap:7px;margin:10px 0}
  .chip{background:var(--panel);border:1px solid var(--line);color:var(--muted);
    border-radius:999px;padding:5px 12px;font-size:13px;cursor:pointer;user-select:none}
  .chip:hover{border-color:#2c3b4d;color:var(--fg)}
  .chip[aria-pressed=true]{border-color:var(--primary);color:var(--fg);
    background:rgba(20,184,166,.10)}
  main{padding:8px 0 60px}
  .count{color:var(--muted);font-size:14px;margin:16px 0 6px}
  ul{list-style:none;padding:0;margin:0}
  li.item{border:1px solid var(--line);border-radius:12px;background:var(--panel);
    padding:14px 16px;margin:10px 0}
  li.item:hover{border-color:#2c3b4d}
  .row1{display:flex;flex-wrap:wrap;gap:10px;align-items:baseline}
  .name{font-weight:600;font-size:16px;word-break:break-word}
  .meta{color:var(--muted);font-size:13px;margin-left:auto;white-space:nowrap}
  .desc{color:#b9c4d0;font-size:14px;margin:7px 0 0}
  .tags{margin-top:8px;display:flex;flex-wrap:wrap;gap:6px}
  .tag2{font-size:11px;color:var(--muted);background:#131b24;border:1px solid var(--line);
    border-radius:6px;padding:2px 7px}
  .ev{border-radius:6px;padding:2px 8px;font-size:12px;border:1px solid}
  .ev.official{color:var(--green);border-color:rgba(74,222,128,.35)}
  .ev.observed{color:var(--blue);border-color:rgba(125,211,252,.35)}
  .ev.inferred{color:var(--accent);border-color:rgba(240,169,59,.35)}
  .ev.unverified{color:var(--muted);border-color:var(--line)}
  .langs{display:flex;flex-wrap:wrap;gap:8px;font-size:13px;padding:14px 0 0}
  footer{border-top:1px solid var(--line);color:var(--muted);font-size:13px;padding:22px 0 50px}
  .legend{display:flex;flex-wrap:wrap;gap:14px;margin:12px 0 0;font-size:13px;color:var(--muted)}
  code{background:#131b24;border:1px solid var(--line);border-radius:5px;padding:1px 5px;font-size:13px}
  @media(prefers-color-scheme:light){
    :root{--bg:#fbfcfd;--panel:#fff;--line:#e3e8ee;--fg:#1b2430;--muted:#5b6675}
    .desc{color:#3d4856}
    .tag2{background:#f2f5f8}
    code{background:#f2f5f8}
  }
</style>
</head>
<body>
<header>
  <div class="wrap">
    <img class="hero" src="hero.png" alt="Awesome Jev Live">
    <h1>Awesome Claude Mods</h1>
    <p class="tag">Claude Code mods, graded by how much was actually verified. Rebuilt every two hours.</p>
    <div class="bar">
      <span><span class="pulse"></span>Last sync <b id="sync">__STAMP__</b></span>
      <span>Entries <b id="total">__TOTAL__</b></span>
      <span>Added in the latest update <b id="new">__NEW__</b></span>
      <span>Editions <b>20</b></span>
    </div>
  </div>
</header>
<main class="wrap">
  <div class="controls">
    <input type="search" id="q" placeholder="Search name, description, topic…" autocomplete="off">
  </div>
  <div class="chips" id="cats"></div>
  <div class="chips" id="evs"></div>
  <div class="legend" id="legend"></div>
  <p class="count" id="count"></p>
  <ul id="list">__ITEMS__</ul>
  <div class="langs">
    Read it in:
    __LANGS__
  </div>
</main>
<footer class="wrap">
  <p><strong>Evidence grades.</strong> <code>official</code> published by Anthropic,
  or read from the official changelog · <code>observed</code> its own text names part
  of the mod surface, such as <code>ui.render</code>, <code>ui.fault</code> or
  <code>agent.spawn</code> · <code>inferred</code> calls itself a mod, plugin or hook
  without naming that surface · <code>unverified</code> matched on vocabulary alone.
  A grade describes the evidence, not the quality of a project.</p>
  <p>Independent community project. Not affiliated with, endorsed by or reviewed by
  Anthropic. Claude and Claude Code are trademarks of Anthropic. Product behaviour
  changes without notice; verify anything load-bearing against the official
  documentation.</p>
  <p><a href="https://github.com/wh000wh000/awesome-claude-mods">Repository</a> ·
  <a href="https://github.com/wh000wh000/awesome-claude-mods/blob/main/CONTRIBUTING.md">Contributing</a> ·
  <a href="https://github.com/wh000wh000/awesome-claude-mods/blob/main/data/CHANGELOG.md">Change ledger</a> ·
  <a href="https://github.com/wh000wh000/awesome-claude-mods/blob/main/LICENSE">MIT</a></p>
</footer>
<script>
// Every entry is already in the HTML above. This script only filters: it hides
// and shows what is there, and never builds a result from data. A crawler or an
// agent that does not run JavaScript -- or runs it before the fetch resolves --
// still sees the full list, which is the whole point of publishing a page.
const EV = {official:"✅", observed:"👁️", inferred:"🔎", unverified:"❓"};
let data = null, cat = "all", ev = "all";

fetch("site.json").then(r => r.json()).then(d => {
  data = d;
  document.getElementById("sync").textContent = d.generated_at.replace("T", " ");
  document.getElementById("total").textContent = d.total;
  document.getElementById("new").textContent = d.new_this_tick;
  buildChips();
  render();
}).catch(() => { buildChipsFromDom(); });

function buildChips() {
  const cats = document.getElementById("cats");
  for (const [key, n] of Object.entries(data.by_category)) {
    cats.appendChild(chip(`${data.categories[key] || ""} ${key} (${n})`.trim(), key, "cat"));
  }
  const evs = document.getElementById("evs");
  for (const key of data.evidence_order) {
    evs.appendChild(chip(`${EV[key]} ${key} (${data.by_evidence[key] || 0})`, key, "ev"));
  }
}

function chip(label, value, kind) {
  const b = document.createElement("button");
  b.className = "chip";
  b.textContent = label;
  b.setAttribute("aria-pressed", (kind === "cat" ? cat : ev) === value);
  b.onclick = () => {
    if (kind === "cat") cat = (cat === value ? "all" : value);
    else ev = (ev === value ? "all" : value);
    document.querySelectorAll(kind === "cat" ? "#cats .chip" : "#evs .chip")
      .forEach(c => c.setAttribute("aria-pressed", "false"));
    if ((kind === "cat" ? cat : ev) !== "all") b.setAttribute("aria-pressed", "true");
    render();
  };
  return b;
}

function render() {
  const q = document.getElementById("q").value.trim().toLowerCase();
  const items = document.querySelectorAll("#list li.item");
  let shown = 0;
  items.forEach(li => {
    const ok = (cat === "all" || li.dataset.c === cat) &&
               (ev === "all" || li.dataset.e === ev) &&
               (!q || (li.dataset.hay || "").includes(q));
    li.hidden = !ok;
    if (ok) shown++;
  });
  document.getElementById("count").textContent =
    `${shown} of ${items.length} entries` + (q ? ` matching “${q}”` : "");
}

function buildChipsFromDom() {
  const counts = {}, evs = {};
  document.querySelectorAll("#list li.item").forEach(li => {
    counts[li.dataset.c] = (counts[li.dataset.c] || 0) + 1;
    evs[li.dataset.e] = (evs[li.dataset.e] || 0) + 1;
  });
  data = {by_category: counts, by_evidence: evs,
          categories: {}, evidence_order: Object.keys(EV),
          total: document.querySelectorAll("#list li.item").length,
          generated_at: "", new_this_tick: ""};
  buildChips();
}
function esc(s) {
  return String(s == null ? "" : s).replace(/[&<>"']/g,
    c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
}
document.getElementById("q").addEventListener("input", render);
</script>
<script type="application/ld+json">__JSONLD__</script>
</body>
</html>
"""


def main() -> int:
    doc = json.loads((DATA / "entries.json").read_text())
    stats = json.loads((DATA / "stats.json").read_text())
    # The media stage is allowed to fail, so its output may simply not exist.
    # The site degrades to no thumbnails rather than refusing to build.
    media_path = DATA / "media.json"
    media = {}
    if media_path.exists():
        try:
            doc_m = json.loads(media_path.read_text())
            media = doc_m.get("entries", {}) if isinstance(doc_m, dict) else {}
        except Exception:  # noqa: BLE001
            media = {}

    DOCS.mkdir(parents=True, exist_ok=True)

    # Pages serves /docs as the site root, so anything referenced with ../ is
    # outside the site and 404s. The hero is copied in rather than hot-linked:
    # a self-contained site keeps working if the raw host is unreachable.
    hero_src = ROOT / "assets/readme/hero.png"
    if hero_src.exists():
        (DOCS / "hero.png").write_bytes(hero_src.read_bytes())

    payload = build_payload(doc["entries"], stats, media)
    (DOCS / "site.json").write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n")

    langs = " · ".join(
        f'<a href="README.{code}.md">{esc(label)}</a>' if code != "en"
        else "<b>English</b>" for code, label in LANGS)

    items = []
    for e in payload["entries"]:
        bits = []
        if e["s"]:
            bits.append(f"★ {e['s']}")
        if e["l"]:
            bits.append(esc(e["l"]))
        if e["p"]:
            bits.append(f"pushed {esc(e['p'])}")
        hay = esc((e["n"] + " " + e["d"] + " " + " ".join(e["g"]) + " " + e["l"]).lower())
        items.append(
            f'<li class="item" data-c="{esc(e["c"])}" data-e="{esc(e["e"])}"'
            f' data-hay="{hay}">'
            f'<div class="row1"><span class="name">'
            f'<a href="{esc(e["u"])}">{esc(e["n"])}</a></span>'
            f'<span class="ev {esc(e["e"])}">{EVIDENCE_EMOJI.get(e["e"], "")} '
            f'{esc(e["e"])}</span>'
            f'<span class="meta">{esc(" · ".join(bits))}</span></div>'
            + (f'<p class="desc">{esc(e["d"])}</p>' if e["d"] else "")
            + (f'<div class="tags">' + "".join(
                f'<span class="tag2">{esc(t)}</span>' for t in e["g"]) + "</div>"
               if e["g"] else "")
            + "</li>")

    jsonld = json.dumps({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Awesome Jev",
        "description": "An evidence-graded index of the Jev / TypeSafe System One "
                       "ecosystem, rebuilt every two hours.",
        "url": SITE_URL,
        "numberOfItems": payload["total"],
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": e["n"], "url": e["u"]}
            for i, e in enumerate(payload["entries"][:500])
        ],
    }, ensure_ascii=False)

    page = (PAGE
            .replace("__ITEMS__", "\n".join(items))
            .replace("__JSONLD__", jsonld)
            .replace("__TOTAL__", str(payload["total"]))
            .replace("__NEW__", str(payload["new_this_tick"]))
            .replace("__STAMP__", esc(payload["generated_at"][:16].replace("T", " ")))
            .replace("__LANGS__", langs))
    (DOCS / "index.html").write_text(page)

    # Pages needs a marker to disable Jekyll processing of the generated files.
    (DOCS / ".nojekyll").write_text("")
    (DOCS / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n"
        f"Sitemap: {SITE_URL}sitemap.xml\n")
    (DOCS / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'  <url><loc>{SITE_URL}</loc><lastmod>{STAMP[:10]}</lastmod>'
        '<changefreq>hourly</changefreq><priority>1.0</priority></url>\n'
        '</urlset>\n')

    # llms.txt, the emerging convention for AI crawlers. Generated from the same
    # data as everything else, so it cannot drift.
    top = {k: v for k, v in sorted(stats.get("by_category", {}).items(),
                                    key=lambda kv: -kv[1])}
    lines = [
        "# Awesome Jev",
        "",
        "> An evidence-graded, continuously rebuilt index of the Jev / TypeSafe",
        "> System One ecosystem: SDKs, MCP tooling, agent guardrails, evaluations,",
        "> open models, applications and writing. Every entry carries an evidence",
        "> grade saying how much was actually verified. Rebuilt every two hours in",
        "> twenty languages.",
        "",
        f"Last generated: {STAMP}",
        f"Entries: {stats.get('total')}",
        "",
        "## What a Claude Code mod is",
        "",
        "Claude Code gained mods in 2.1.287: extensions that may change deeper",
        "behaviour than a plugin could, and draw their own interface. A mod can",
        "hook ui.render to paint a row, band, pane or card around the prompt,",
        "read the text you last selected with $.ui.selection(), spawn teammates",
        "with agent.spawn, and own a Client region. ui.fault keeps one broken mod",
        "from taking down the session.",
        "",
        "## Evidence grades",
        "",
        "- official: published by Anthropic, or read from the official changelog",
        "- observed: its own text names part of the mod surface",
        "- inferred: calls itself a mod, plugin or hook, without naming that surface",
        "- unverified: matched on vocabulary alone",
        "",
        "The grade describes how much was verified, not how good a project is.",
        "",
        "## Sections",
        "",
    ]
    for key, n in top.items():
        lines.append(f"- {key}: {n} entries")
    lines += [
        "",
        "## Pages",
        "",
        f"- [Index]({SITE_URL}): searchable, filterable list of every entry",
        f"- [Repository]({REPO_URL}): the generated README, contributing guide and change ledger",
        f"- [English README]({REPO_URL}/blob/main/README.md)",
        f"- [Chinese README]({REPO_URL}/blob/main/docs/README.zh-CN.md)",
        f"- [Data]({REPO_URL}/blob/main/data/entries.json): the underlying entries as JSON",
        "",
        "## Disclosure",
        "",
        "Independent community project, not affiliated with or endorsed by Anthropic.",
        "Claude and Claude Code are trademarks of Anthropic. Product behaviour changes",
        "without notice.",
        "",
    ]
    (ROOT / "llms.txt").write_text("\n".join(lines))

    print(f"   site: docs/index.html ({len(page) / 1024:.0f} KB), "
          f"docs/site.json ({len(json.dumps(payload)) / 1024:.0f} KB), "
          f"{len(payload['entries'])} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())