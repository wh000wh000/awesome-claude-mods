#!/usr/bin/env python3
"""
awesome-claude-mods :: summary.py

Writes a human-readable run summary. Consumed by the GitHub Actions job summary
(`$GITHUB_STEP_SUMMARY`) and useful locally when running the pipeline by hand.
Read-only: it never writes into the repository.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def load(name, default):
    try:
        return json.loads((DATA / name).read_text())
    except Exception:  # noqa: BLE001
        return default


def main() -> int:
    stats = load("stats.json", {})
    media = load("media.json", {})
    entries_doc = load("entries.json", {})

    if not stats:
        print("## awesome-claude-mods\n\nNo stats produced by this run.")
        return 0

    out: list[str] = []
    out.append("## awesome-claude-mods sync")
    out.append("")
    out.append(f"**Generated:** `{stats['generated_at']}` (UTC+8)")
    out.append("")
    out.append("| Metric | Value |")
    out.append("| --- | --- |")
    out.append(f"| Entries | **{stats['total']}** |")
    out.append(f"| Added in the latest update | {stats['new_this_tick']} |")
    out.append(f"| Repositories | {stats.get('repos', 0)} |")
    out.append(f"| Open models | {stats.get('models', 0)} |")
    out.append(f"| Discussions | {stats.get('discussions', 0)} |")
    out.append(f"| Implementation languages | {len(stats.get('by_language', {}))} |")
    out.append(f"| Combined stars | {stats.get('total_stars', 0)} |")
    out.append("")

    ev = stats.get("by_evidence", {})
    if ev:
        out.append("**Evidence grades** — " + " · ".join(
            f"`{k}` {v}" for k, v in ev.items()))
        out.append("")

    cats = stats.get("by_category", {})
    if cats:
        out.append("**Categories**")
        out.append("")
        for k, v in sorted(cats.items(), key=lambda kv: -kv[1]):
            out.append(f"- `{k}` — {v}")
        out.append("")

    langs = stats.get("by_language", {})
    if langs:
        top = list(langs.items())[:14]
        out.append("**Languages** — " + " · ".join(f"{k} {v}" for k, v in top))
        out.append("")

    records = media.get("entries", {})
    if records:
        with_img = sum(1 for v in records.values() if v.get("image"))
        with_vid = sum(1 for v in records.values()
                       if (v.get("video") or {}).get("state") not in (None, "", "none"))
        bundled = sum(1 for v in records.values() if v.get("bundled"))
        out.append("**Media**")
        out.append("")
        out.append(f"- cards with an image: {with_img}")
        out.append(f"- cards with a video or animation: {with_vid}")
        out.append(f"- assets bundled locally: {bundled}")
        out.append(f"- bundled size: {media.get('bundled_bytes', 0) / 1e6:.1f} MB")
        out.append("")

    entries = entries_doc.get("entries", [])
    fresh = [e for e in entries if e.get("is_new")]
    if fresh:
        out.append("**Added in the latest update**")
        out.append("")
        for e in sorted(fresh, key=lambda x: -int(x.get("stars") or 0))[:15]:
            out.append(f"- [{e['name']}]({e['url']}) — ⭐{e.get('stars', 0)} "
                       f"· `{e.get('evidence')}` · `{e.get('category')}`")
        out.append("")

    print("\n".join(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())