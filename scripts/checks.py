#!/usr/bin/env python3
"""
awesome-claude-mods :: checks.py

Regression checks for pull requests. Two properties are asserted, and both are
properties that have actually broken during development of this pipeline.

  --determinism
      curate.py must produce the same list, in the same order, with the same
      grades, from the same inputs. If it does not, the two-hourly diff stops
      being reviewable and nobody can tell a real change from noise.

  --i18n
      Every language file must carry exactly the English key set. A missing key
      is not a cosmetic problem: render.py indexes these keys directly, so one
      absent string takes down all twenty editions.

  --readmes
      The committed READMEs must match what render.py produces from data/.

Exit code 0 means the branch is safe to merge.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
I18N = ROOT / "i18n"
SCRIPTS = ROOT / "scripts"

LANGS = [
    "en", "zh-CN", "zh-TW", "ja", "ko", "es", "fr", "de", "pt-BR", "ru",
    "it", "ar", "hi", "tr", "vi", "th", "id", "pl", "nl", "uk",
]

failures: list[str] = []


def keys_of(obj, prefix: str = "") -> set[str]:
    out: set[str] = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            out |= keys_of(v, f"{prefix}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out |= keys_of(v, f"{prefix}[{i}]")
    else:
        out.add(prefix)
    return out


def signature(doc: dict) -> list[tuple]:
    """The part of the output that must be stable between runs."""
    return [(e["id"], e["category"], e["evidence"], e.get("tier"), e.get("language"))
            for e in doc.get("entries", [])]


def check_determinism() -> None:
    before_path = DATA / "entries.json"
    if not before_path.exists():
        failures.append("data/entries.json is missing; cannot check determinism")
        return
    before = json.loads(before_path.read_text())
    sig_a = signature(before)

    res = subprocess.run([sys.executable, str(SCRIPTS / "curate.py")],
                         capture_output=True, text=True, cwd=str(ROOT))
    if res.returncode != 0:
        failures.append(f"second curate.py run failed:\n{res.stderr[-800:]}")
        return

    after = json.loads(before_path.read_text())
    sig_b = signature(after)

    if sig_a != sig_b:
        failures.append("curate.py is not deterministic: identical input produced "
                        "a different list, ordering or grading")
        for a, b in zip(sig_a, sig_b):
            if a != b:
                print(f"   first difference:\n     {a}\n  -> {b}")
                break
        if len(sig_a) != len(sig_b):
            print(f"   list length changed: {len(sig_a)} -> {len(sig_b)}")
        return
    print(f"   determinism: OK ({len(sig_a)} entries, identical ordering and grades)")


def check_i18n() -> None:
    en_path = I18N / "en.json"
    if not en_path.exists():
        failures.append("i18n/en.json is missing")
        return
    base = keys_of(json.loads(en_path.read_text()))
    bad = 0
    for code in LANGS:
        path = I18N / f"{code}.json"
        if not path.exists():
            failures.append(f"i18n/{code}.json is missing")
            bad += 1
            continue
        try:
            doc = json.loads(path.read_text())
        except Exception as exc:  # noqa: BLE001
            failures.append(f"i18n/{code}.json is not valid JSON: {exc}")
            bad += 1
            continue
        got = keys_of(doc)
        if got != base:
            missing = sorted(base - got)[:6]
            extra = sorted(got - base)[:6]
            failures.append(
                f"i18n/{code}.json key mismatch: missing={missing} extra={extra}")
            bad += 1
        if doc.get("lang") != code:
            failures.append(f"i18n/{code}.json declares lang={doc.get('lang')!r}")
            bad += 1
        if not doc.get("native_name"):
            failures.append(f"i18n/{code}.json has no native_name")
            bad += 1
    print(f"   i18n: {len(LANGS) - bad}/{len(LANGS)} language files OK "
          f"({len(base)} keys each)")


def check_readmes_in_sync() -> None:
    """Regenerate into a temp dir and compare against what is committed."""
    def edition(code: str) -> Path:
        return ROOT / "README.md" if code == "en" else ROOT / "docs" / f"README.{code}.md"

    before = {}
    for code in LANGS:
        p = edition(code)
        if p.exists():
            before[str(p.relative_to(ROOT))] = p.read_text()

    res = subprocess.run([sys.executable, str(SCRIPTS / "render.py")],
                         capture_output=True, text=True, cwd=str(ROOT))
    if res.returncode != 0:
        failures.append(f"render.py failed:\n{res.stderr[-800:]}")
        return

    drifted = []
    for name, old in before.items():
        new = (ROOT / name).read_text()
        if new != old:
            drifted.append(name)

    if drifted:
        failures.append(
            "committed READMEs are stale for: " + ", ".join(drifted[:8])
            + " — run scripts/render.py and commit the result")
        return
    print(f"   readmes: OK ({len(before)} editions in sync with data/)")


def main(argv: list[str]) -> int:
    wanted = set(a for a in argv if a.startswith("--")) or {
        "--determinism", "--i18n", "--readmes"}
    print(f"== awesome-claude-mods :: checks ({', '.join(sorted(wanted))}) ==")
    if "--determinism" in wanted:
        check_determinism()
    if "--i18n" in wanted:
        check_i18n()
    if "--readmes" in wanted:
        check_readmes_in_sync()

    if failures:
        print(f"\n   FAILED with {len(failures)} problem(s):")
        for f in failures:
            print(f"     - {f}")
        return 1
    print("\n   PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))