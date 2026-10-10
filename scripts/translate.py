#!/usr/bin/env python3
"""
awesome-claude-mods :: translate.py

Fills the summary translation cache.

Why this is separate from the pipeline
--------------------------------------
`curate.py` is deterministic and model-free, because it runs every two hours and
a model in that loop makes every diff unreviewable. Translation is a different
kind of work: additive, cached, and safely degradable. So it lives here, writes
a committed cache, and the renderer simply reads it. If this stage never runs,
or fails, every edition still renders with the English source.

What it protects, and why
-------------------------
The first attempt at multilingual output produced "MIT" rendered as
麻省理工学院 -- the Massachusetts Institute of Technology -- in a table of
software licences. That is the failure mode this stage exists to prevent.

Every identifier is replaced with a placeholder before the text is sent and
restored afterwards: code spans, URLs, licence SPDX ids, language and product
names, and acronyms like LLM, MCP and SDK. A translation that loses, duplicates
or invents a placeholder is rejected and the English original is kept. A reader
seeing English is a smaller failure than a reader seeing a wrong fact.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CACHE = DATA / "summaries"
CST = timezone(timedelta(hours=8))
STAMP = datetime.now(CST).isoformat(timespec="seconds")

LANGS = [
    # English is included because the collection log is a Chinese source: the
    # English edition needs a translation of it too.
    "en",
    "zh-CN", "zh-TW", "ja", "ko", "es", "fr", "de", "pt-BR", "ru",
    "it", "ar", "hi", "tr", "vi", "th", "id", "pl", "nl", "uk",
]
LANG_NAME = {
    "zh-CN": "Simplified Chinese", "zh-TW": "Traditional Chinese", "ja": "Japanese",
    "ko": "Korean", "es": "Spanish", "fr": "French", "de": "German",
    "pt-BR": "Brazilian Portuguese", "ru": "Russian", "it": "Italian",
    "ar": "Arabic", "hi": "Hindi", "tr": "Turkish", "vi": "Vietnamese",
    "th": "Thai", "id": "Indonesian", "pl": "Polish", "nl": "Dutch",
    "uk": "Ukrainian",
}

# Only the entries a reader is most likely to open, highest first. The cache
# converges on the visible head before it reaches the one-line tail.
TRANSLATE_TOP = int(os.environ.get("TRANSLATE_TOP", "250"))
BATCH = int(os.environ.get("TRANSLATE_BATCH", "40"))
# A tick must not spend half an hour translating. The cache is committed, so a
# bounded run simply continues where the last one stopped.
MAX_CALLS = int(os.environ.get("TRANSLATE_MAX_CALLS", "0"))
LANGS_PER_RUN = os.environ.get("TRANSLATE_LANGS", "").split(",")
LANGS_PER_RUN = [x for x in LANGS_PER_RUN if x] or LANGS

# Tokens that must survive verbatim. Anything here appearing in a translation
# under a different form is treated as a broken translation.
PROTECT_WORDS = [
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "MPL-2.0",
    "CC0-1.0", "CC-BY-4.0", "Unlicense", "AGPL-3.0", "GPL-2.0", "GPL-3.0",
    "LLM", "LLMs", "MCP", "SDK", "SDKs", "API", "APIs", "CLI", "JSON", "YAML",
    "HTTP", "HTTPS", "RLCD", "Noul", "Choice", "Score", "Jev", "jev-latest",
    "TypeSafe", "TypeSafe AI", "System One", "System One Model", "GitHub",
    "Hacker News", "Hugging Face", "HuggingFace", "OpenAI", "Anthropic",
    "Claude", "Codex", "Cursor", "Cline", "Kiro", "Gemini", "GPT",
    "Python", "TypeScript", "JavaScript", "Rust", "Golang", "Go", "Java",
    "Kotlin", "Swift", "Ruby", "PHP", "Elixir", "Zig", "Lua", "Julia",
    "Scala", "Clojure", "Haskell", "OCaml", "Erlang", "Dart", "Perl", "Nim",
    "Crystal", "Bun", "Deno", "Node.js", "React", "Vue", "Svelte", "Docker",
    "Kubernetes", "AWS", "Postgres", "PostgreSQL", "SQLite", "Redis",
    "MongoDB", "Neo4j", "MLX", "vLLM", "SGLang", "LoRA", "RAG", "OCR",
    "Chrome", "Firefox", "Safari", "macOS", "Linux", "Windows", "iPhone",
    "Android", "Unity", "Phaser", "Three.js", "Emacs", "Vim", "Neovim",
    "VS Code", "Zsh", "Fish", "Deltarune", "Doom", "Snake", "Tetris",
]
PROTECT_WORDS.sort(key=len, reverse=True)

CODE_SPAN = re.compile(r"`[^`]+`")
URL = re.compile(r"https?://[^\s)\]<>]+")
WORD = re.compile(r"\b(" + "|".join(re.escape(w) for w in PROTECT_WORDS) + r")\b")


CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]")


def needs_translation(text: str, lang: str) -> bool:
    """
    Whether `text` still has to be translated for `lang`.

    Without this, adding English as a target queued every English summary in the
    repository for translation into English: 491 identity calls whose only
    effect was to push the thirty Chinese collection-log records to the back of
    the queue, where they never ran.
    """
    chinese = bool(CJK.search(text))
    if lang == "en":
        return chinese                  # English text is already English
    if lang == "zh-CN":
        return not chinese              # Chinese text is already Simplified
    return True                         # zh-TW converts script; the rest translate


def key(text: str) -> str:
    return hashlib.sha1(text.strip().encode("utf-8")).hexdigest()[:16]


class Protector:
    """Replaces identifiers with placeholders and restores them afterwards."""

    def __init__(self) -> None:
        self.slots: list[str] = []

    def _slot(self, value: str) -> str:
        marker = "{{%d}}" % len(self.slots)
        self.slots.append(value)
        return marker

    def mask(self, text: str) -> str:
        self.slots = []
        text = CODE_SPAN.sub(lambda m: self._slot(m.group(0)), text)
        text = URL.sub(lambda m: self._slot(m.group(0)), text)
        text = WORD.sub(lambda m: self._slot(m.group(0)), text)
        return text

    def restore(self, text: str) -> str | None:
        """None when the translation does not preserve every placeholder."""
        for i, value in enumerate(self.slots):
            marker = "{{%d}}" % i
            if text.count(marker) != 1:
                return None
            text = text.replace(marker, value)
        if "{{" in text and "}}" in text:
            return None                     # invented a placeholder
        return text


def load_key() -> str | None:
    for var in ("TRANSLATE_API_KEY", "GUILDOS_IMAGE_API_KEY"):
        if os.environ.get(var):
            return os.environ[var]
    for candidate in (
        Path.home() / ".codex/skills/guildos-imagegen-router/.secrets.env",
        Path.home() / ".agents/skills/guildos-imagegen-router/.secrets.env",
    ):
        if candidate.exists():
            for line in candidate.read_text().splitlines():
                if line.startswith("GUILDOS_IMAGE_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def post(base: str, api_key: str, model: str, system: str, user: str) -> str | None:
    payload = {
        "model": model,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "temperature": 0,
    }
    req = urllib.request.Request(
        base.rstrip("/") + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": "Bearer " + api_key,
                 "Content-Type": "application/json"},
        method="POST",
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                doc = json.loads(resp.read().decode("utf-8", "replace"))
            return ((doc.get("choices") or [{}])[0].get("message") or {}).get("content")
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")[:200]
            print(f"    !! HTTP {exc.code}: {body}", file=sys.stderr)
            # 401 and 403 were transient on this router: 57 batches were
            # discarded as permanently unauthorised while the same key
            # authenticated fine minutes later. Retrying costs one call.
            if exc.code in (401, 403, 408, 425, 429, 500, 502, 503, 504):
                time.sleep(5 * (attempt + 1))
                continue
            return None
        except Exception as exc:  # noqa: BLE001
            print(f"    !! {type(exc).__name__}: {exc}", file=sys.stderr)
            time.sleep(3)
    return None


SYSTEM = (
    "You translate short software-project descriptions into {lang} for a "
    "curated index. Rules, in order of importance:\n"
    "1. The text contains placeholders of the form {{{{0}}}}, {{{{1}}}} and so "
    "on. Reproduce every placeholder exactly once, unchanged. Never translate, "
    "renumber, reorder or drop one.\n"
    "2. Translate the prose. Do not translate anything a placeholder stands for.\n"
    "3. Keep identifiers that are not placeholders as they are: product names, "
    "language names, acronyms, version numbers, licence ids (MIT, Apache-2.0). "
    "For example 'MIT' is a software licence and must never become the name of "
    "a university.\n"
    "4. Do not add, explain, summarise or omit information. No notes, no quotes, "
    "no markdown formatting that was not in the source.\n"
    "5. Reply with JSON only: an object mapping the input key to the translated "
    "string. Nothing else, no code fences."
)


def translate_batch(items: list[tuple[str, str]], lang: str, base: str,
                    api_key: str, model: str) -> dict[str, str]:
    """items: [(key, masked_text)] -> {key: translated_text}"""
    payload = {k: v for k, v in items}
    prompt = ("Translate each value into {}. Return JSON only.\n\n{}"
              .format(LANG_NAME.get(lang, lang),
                      json.dumps(payload, ensure_ascii=False)))
    raw = post(base, api_key, model, SYSTEM.format(lang=LANG_NAME.get(lang, lang)), prompt)
    if not raw:
        return {}
    raw = raw.strip()
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-z]*\n?|```$", "", raw).strip()
    try:
        doc = json.loads(raw)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", raw, re.S)
        if not m:
            return {}
        try:
            doc = json.loads(m.group(0))
        except json.JSONDecodeError:
            return {}
    if not isinstance(doc, dict):
        return {}
    return {str(k): str(v) for k, v in doc.items() if isinstance(v, str)}


def ask(chunk: list[tuple[str, str]], lang: str, base: str, api_key: str,
        model: str) -> dict[str, str]:
    """
    Translate a batch, splitting it when the batch as a whole fails.

    A malformed response from the model loses the whole batch, which is how the
    German edition ended up exactly one batch short of complete: 60 strings
    rejected together, silently. Halving a failed batch narrows a parse problem
    to the one or two strings that cause it instead of discarding the rest.
    """
    guards = [Protector() for _ in chunk]
    masked = [(k, g.mask(v)) for (k, v), g in zip(chunk, guards)]
    out = translate_batch(masked, lang, base, api_key, model)
    if out:
        return out
    if len(chunk) <= 4:
        print(f"    !! {lang}: giving up on {len(chunk)} string(s)", file=sys.stderr)
        return {}
    half = len(chunk) // 2
    print(f"    .. {lang}: batch of {len(chunk)} failed, splitting", file=sys.stderr)
    merged = ask(chunk[:half], lang, base, api_key, model)
    merged.update(ask(chunk[half:], lang, base, api_key, model))
    return merged


def acquire_lock():
    """
    One translator at a time.

    Running two instances is not merely wasteful: each loads the whole cache,
    adds its own strings and writes the file back, so the second writer silently
    discards the first one's work. That is exactly what happened when two rounds
    of groups were launched and overlapped -- coverage came out uneven across
    languages with nothing in the log to explain it.

    Returns a release callable, or None when another instance holds the lock.
    """
    import os
    import shutil
    import time as _time
    lockfile = CACHE.parent / ".translate.lockdir"
    try:
        os.mkdir(lockfile)
    except FileExistsError:
        # A run killed mid-flight leaves the directory behind. Treat a lock
        # older than the longest a run can plausibly take as stale, or one
        # killed process stops translation for good.
        age = _time.time() - lockfile.stat().st_mtime
        if age < 3600:
            return None
        print("   clearing a stale translate lock")
        shutil.rmtree(lockfile, ignore_errors=True)
        try:
            os.mkdir(lockfile)
        except OSError:
            return None
    return lambda: shutil.rmtree(lockfile, ignore_errors=True)


def main() -> int:
    release = acquire_lock()
    if release is None:
        print("   another translate run holds the lock; exiting")
        return 0
    try:
        return _main()
    finally:
        release()


def _main() -> int:
    api_key = load_key()
    if not api_key:
        print("   no translation credentials; skipping (editions keep English)")
        return 0
    base = os.environ.get("GUILDOS_IMAGE_BASE_URL", "https://router.guildos.ai/v1")
    model = os.environ.get("GUILDOS_IMAGE_MODEL", "gpt-5.5")

    doc = json.loads((DATA / "entries.json").read_text())
    entries = sorted(doc.get("entries", []),
                     key=lambda e: -int(e.get("stars") or 0))[:TRANSLATE_TOP]

    # Every distinct string that needs translating: the summary and the note.
    # Two sets: everything currently referenced (for pruning) and the head we
    # are willing to spend calls on (for adding).
    referenced: set[str] = set()
    for e in doc.get("entries", []):
        # `name` counts for a record authored in another language, because its
        # title is translated too. Leaving it out made every title translation
        # look unreferenced: it was pruned as stale and re-translated on the
        # next run, for ever, one wasted call every tick.
        fields = ["summary", "notes"]
        if (e.get("source_lang") or "en") != "en":
            fields.append("name")
        for field in fields:
            text = (e.get(field) or "").strip()
            if len(text) >= 8:
                referenced.add(key(text))

    wanted: dict[str, str] = {}
    for e in entries:
        # A record authored in another language needs its title translated as
        # well as its prose, or the English edition leads with a Chinese
        # heading and only the body underneath it is in English.
        fields = ["summary", "notes"]
        if (e.get("source_lang") or "en") != "en":
            fields.append("name")
        for field in fields:
            text = (e.get(field) or "").strip()
            if len(text) < 8 or (e.get(f"{field}_i18n") or {}):
                continue
            # Already in the target language? Nothing to do; the renderer skips
            # the lookup for a matching source language anyway.
            wanted.setdefault(key(text), text)

    CACHE.mkdir(parents=True, exist_ok=True)
    print(f"== translate :: {len(wanted)} distinct strings, "
          f"{len(LANGS_PER_RUN)} languages ==")

    # Round-robin across languages rather than completing one at a time. A
    # reader opening any edition sees progress; finishing Chinese while Japanese
    # still shows English looks like the feature is broken, not in progress.
    caches: dict[str, dict[str, str]] = {}
    todo: dict[str, list[tuple[str, str]]] = {}
    for lang in LANGS_PER_RUN:
        path = CACHE / f"{lang}.json"
        cache: dict[str, str] = {}
        if path.exists():
            try:
                cache = json.loads(path.read_text())
            except Exception:  # noqa: BLE001
                cache = {}
        # Content-addressed keys accumulate as upstream text changes. Without
        # this the cache only ever grows, and it is committed on every tick.
        stale = [k for k in cache if k not in referenced]
        for k in stale:
            cache.pop(k, None)
        if stale:
            print(f"   {lang:<6} pruned {len(stale)} stale strings")
        caches[lang] = cache
        todo[lang] = [(k, v) for k, v in wanted.items()
                      if k not in cache and needs_translation(v, lang)]

    total_added = 0
    calls = 0
    round_no = 0
    while any(todo[lang] for lang in LANGS_PER_RUN):
        if MAX_CALLS and calls >= MAX_CALLS:
            print(f"   stopping after {calls} calls this run")
            break
        round_no += 1
        for lang in LANGS_PER_RUN:
            pending = todo[lang]
            if not pending:
                continue
            if MAX_CALLS and calls >= MAX_CALLS:
                break
            chunk = pending[:BATCH]
            calls += 1
            out = ask(chunk, lang, base, api_key, model)
            guards = [Protector() for _ in chunk]
            added = rejected = 0
            for (k, v), g in zip(chunk, guards):
                g.mask(v)                 # populate the slots for restore()
                raw = out.get(k)
                if not raw:
                    rejected += 1
                    continue
                restored = g.restore(raw)
                if restored is None or not restored.strip():
                    rejected += 1
                    continue
                caches[lang][k] = restored.strip()
                added += 1
            todo[lang] = pending[len(chunk):]
            (CACHE / f"{lang}.json").write_text(
                json.dumps(caches[lang], ensure_ascii=False, indent=1,
                           sort_keys=True) + "\n")
            total_added += added
            print(f"   round {round_no:<3} {lang:<6} "
                  f"+{added} (rejected {rejected}), "
                  f"{len(caches[lang])} cached, {len(todo[lang])} pending")

    print(f"   translated {total_added} strings this run")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())