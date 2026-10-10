#!/usr/bin/env python3
"""
awesome-claude-mods :: knowledge.py

Turns our own collection log into entries.

The repository search sees what is on GitHub today. It is structurally blind to
the other half of this ecosystem: the official documentation that was read and
verified, the independent production tests, the write-ups, and the disputes.
Those live in the Jev 巡检 collection on the maintainer's machine, which has been
recording them every two hours since the model launched.

What is published, and what is not
----------------------------------
Of roughly 190 records in that log, only the ones carrying a URL are ecosystem
entries. The rest are process notes -- search hygiene, self-audits, tool
repairs -- which are valuable internally and meaningless to a reader of an
awesome list. Those are deliberately excluded rather than published as filler.

The log already grades its evidence in the same four levels this list uses, so
the mapping is a translation rather than a judgement call.

The source directory is optional. On a machine without it the stage writes
nothing and the list simply does not gain these entries.
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CST = timezone(timedelta(hours=8))
STAMP = datetime.now(CST).isoformat(timespec="seconds")

# Overridable so the stage degrades to a no-op anywhere the log does not exist.
PATROL = Path(os.environ.get(
    "JEV_PATROL_DIR", str(Path.home() / "Desktop/知识库/Jev-巡检")))

HEAD = re.compile(r"^- \*\*\[(?P<kind>[^\]]+)\]\*\*\s*(?P<title>.+?)\s*$")
FIELD = re.compile(r"^\s+-\s*(?P<key>日期|来源|要点|影响|备注)\s*[：:]\s*(?P<value>.*)$")
URL = re.compile(r"https?://[^\s)\]<>，,；;]+")

# Process records, not ecosystem entries. Everything else is publishable when it
# carries a URL.
INTERNAL = re.compile(
    r"纪律|自查|修复|工具|方法|模式|本库|搜索卫生|质量|标注|精确化|政策",
)

GRADE = [
    (re.compile(r"未证实|未核实"), "unverified"),
    (re.compile(r"官方|政策"), "official"),
    (re.compile(r"观测|实测|审计|第三方|评测|验证"), "observed"),
    (re.compile(r"推断|推测"), "inferred"),
]


def grade_of(kind: str) -> str:
    for pattern, grade in GRADE:
        if pattern.search(kind):
            return grade
    return "inferred"


def clean_title(title: str) -> str:
    """
    The log marks importance with stars and emphasis inside its own headings.
    Those belong to the log's typography, not to a link caption in a published
    list, so they are stripped here rather than carried into the page.
    """
    t = re.sub(r"[⭐★☆⚠️\s]+", " ", title)
    t = t.replace("**", "").replace("__", "")
    t = re.sub(r"^[\s\-—·|]+", "", t)
    t = re.sub(r"\s{2,}", " ", t).strip(" 　—-·|")
    if len(t) > 150:
        t = t[:147].rsplit(" ", 1)[0] + "…"
    return t


def norm_url(raw: str) -> str:
    url = raw.strip().strip("。.,，；;")
    if not url.startswith("http"):
        url = "https://" + url
    return url


def parse_day(path: Path) -> list[dict]:
    """Pull the structured records out of one daily file."""
    out: list[dict] = []
    cur: dict | None = None
    for line in path.read_text(errors="replace").splitlines():
        head = HEAD.match(line)
        if head:
            if cur:
                out.append(cur)
            kind = head.group("kind").strip()
            title = head.group("title").strip()
            urls = URL.findall(title)
            title = URL.sub("", title).strip(" —-–·|")
            cur = {
                "kind_label": kind,
                "title": clean_title(title),
                "url": norm_url(urls[0]) if urls else "",
                "date": "",
                "source": "",
                "point": "",
                "impact": "",
                "file": path.name,
            }
            continue
        if cur is None:
            continue
        field = FIELD.match(line)
        if not field:
            if line.strip() and not line.startswith(" "):
                out.append(cur)
                cur = None
            continue
        key, value = field.group("key"), field.group("value").strip()
        if key == "日期":
            cur["date"] = value
            m = re.search(r"(\d{4}-\d{2}-\d{2})", value)
            if m:
                cur["date"] = m.group(1)
        elif key == "来源":
            cur["source"] = value
        elif key == "要点":
            cur["point"] = value
        elif key == "影响":
            cur["impact"] = value
    if cur:
        out.append(cur)
    return out


def main() -> int:
    print(f"== knowledge :: {PATROL} ==")
    if not PATROL.exists():
        print("   collection log not present; nothing to ingest")
        (DATA / "knowledge.json").write_text(json.dumps(
            {"generated_at": STAMP, "source": str(PATROL), "available": False,
             "count": 0, "entries": []}, ensure_ascii=False, indent=1) + "\n")
        return 0

    files = sorted(PATROL.glob("daily/*.md"))
    records: list[dict] = []
    for path in files:
        records.extend(parse_day(path))
    print(f"   parsed {len(records)} records from {len(files)} daily files")

    # Only records that point at something a reader can open.
    with_url = [r for r in records if r["url"]]
    internal = [r for r in with_url if INTERNAL.search(r["kind_label"])]
    publishable = [r for r in with_url if not INTERNAL.search(r["kind_label"])]
    print(f"   with a URL: {len(with_url)}  "
          f"(dropped {len(internal)} internal process records, "
          f"{len(records) - len(with_url)} without a URL)")

    # The same URL is often recorded on several days as it develops. Keep the
    # most recent record, which carries the fullest picture.
    by_url: dict[str, dict] = {}
    for r in sorted(publishable, key=lambda x: (x["date"], x["file"])):
        prev = by_url.get(r["url"])
        if prev:
            r["first_seen"] = prev.get("first_seen") or prev["date"]
            r["seen_days"] = (prev.get("seen_days") or 1) + 1
        else:
            r["first_seen"] = r["date"]
            r["seen_days"] = 1
        by_url[r["url"]] = r

    entries = sorted(by_url.values(), key=lambda x: x["date"], reverse=True)
    missing_point = [e for e in entries if not e["point"]]
    if missing_point:
        print(f"   note: {len(missing_point)} entries carry no 要点 text")

    payload = {
        "generated_at": STAMP,
        "source": str(PATROL),
        "available": True,
        "count": len(entries),
        "grades": {g: sum(1 for e in entries if grade_of(e["kind_label"]) == g)
                   for g in ("official", "observed", "inferred", "unverified")},
        "entries": [{
            "url": e["url"],
            "title": e["title"],
            "kind_label": e["kind_label"],
            "evidence": grade_of(e["kind_label"]),
            "date": e["date"],
            "first_seen": e.get("first_seen", e["date"]),
            "seen_days": e.get("seen_days", 1),
            "point": e["point"],
            "impact": e["impact"],
            "source_note": e["source"],
        } for e in entries],
    }
    (DATA / "knowledge.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1) + "\n")
    print(f"   wrote {len(entries)} entries: {payload['grades']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())