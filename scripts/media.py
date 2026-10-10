#!/usr/bin/env python3
"""
awesome-claude-mods :: media.py

Stage 3: gather each project's image and video so every entry can render as a
self-contained card ("豆腐块": title / facts / data / summary / image | video).

Three rules govern this stage, and they are the reason it is a separate module
rather than a few lines inside the renderer.

1. LICENCE-AWARE BUNDLING
   Copying a third party's screenshots and videos into our repository is
   redistribution. We only do that when the project declares a licence that
   permits it. Otherwise we record the upstream URL and hot-link it instead, so
   the reader still sees the asset but we never re-host it.

2. CONTENT-ADDRESSED CACHE
   Media is stored under a SHA-256 of its own bytes. A file that has not changed
   is never downloaded twice, never re-written, and never shows up in the diff.
   That is what keeps a 2-hourly job from bloating git history.

3. GRACEFUL DEGRADATION
   GitHub plays a real <video> file inline. It cannot play YouTube, Bilibili or
   any iframe embed. So a card's video column has three honest states:
     file     -> local .mp4/.webm, plays inline
     animated -> local .gif, rendered as an animated image
     external -> poster image plus a link, because inline playback is impossible
"""

from __future__ import annotations

import hashlib
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
MEDIA = ROOT / "media"
CST = timezone(timedelta(hours=8))
NOW = datetime.now(CST)
STAMP = NOW.isoformat(timespec="seconds")

TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
if not TOKEN:
    try:
        import subprocess

        TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True,
                               text=True, timeout=10).stdout.strip() or None
    except Exception:  # noqa: BLE001
        TOKEN = None

UA = "awesome-claude-mods/1.0 (+https://github.com/wh000wh000/awesome-claude-mods)"

# Limits. GitHub warns above 50 MB per file and rejects above 100 MB, so these
# are deliberately far below that: a README asset should never be large.
MAX_IMAGE_BYTES = 3_500_000
MAX_VIDEO_BYTES = 12_000_000
MAX_ANIM_BYTES = 8_000_000
# Keep at most this much bundled media in the repository. Beyond it we stop
# bundling and fall back to hot-linking, which keeps clones reasonable.
MEDIA_BUDGET_BYTES = 700_000_000
# Per-entry cap so one media-rich project cannot dominate the repository.
MAX_ASSETS_PER_ENTRY = 3

PERMISSIVE = {
    "MIT", "Apache-2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC", "MPL-2.0",
    "CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0", "Unlicense", "0BSD", "Zlib",
    "PostgreSQL", "Python-2.0", "WTFPL", "AGPL-3.0", "GPL-2.0", "GPL-3.0",
    "LGPL-2.1", "LGPL-3.0", "BSL-1.0", "Artistic-2.0",
}

IMG_EXT = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".svg"}
VID_EXT = {".mp4", ".webm", ".mov", ".m4v"}
ANIM_EXT = {".gif"}

MAGIC = {
    b"\x89PNG\r\n\x1a\n": ("png", "image"),
    b"\xff\xd8\xff": ("jpg", "image"),
    b"GIF87a": ("gif", "image"),
    b"GIF89a": ("gif", "image"),
    b"RIFF": ("webp", "image"),          # refined below for WEBP/AVI
    b"\x1aE\xdf\xa3": ("webm", "video"),  # EBML -> webm/mkv
    b"\x00\x00\x00\x18ftyp": ("mp4", "video"),
    b"\x00\x00\x00\x1cftyp": ("mp4", "video"),
    b"\x00\x00\x00\x20ftyp": ("mp4", "video"),
}

# Anything matching these is chrome, not content.
BADGE_PATTERNS = [
    r"shields\.io", r"badge\.fury", r"badgen\.net", r"codecov\.io",
    r"travis-ci", r"appveyor", r"circleci", r"coveralls", r"david-dm",
    r"awesome\.re/badge", r"github\.com/.*/actions/workflows",
    r"img\.shields", r"api\.codacy", r"snyk\.io", r"bundlephobia",
    r"contrib\.rocks", r"isitmaintained", r"opencollective", r"buymeacoffee",
    r"ko-fi", r"paypal", r"twitter\.com/intent", r"badge\.svg\?",
    r"star-history", r"visitor-badge", r"hits\.se", r"profile-views",
    r"komarev", r"readme-typing-svg", r"capsule-render",
]

# Names that usually mean "this is the project's real screenshot".
GOOD_HINTS = [
    r"screenshot", r"demo", r"preview", r"hero", r"showcase", r"example",
    r"result", r"output", r"dashboard", r"ui\b", r"screen", r"cover",
    r"banner", r"shot", r"thumb", r"feature", r"architect", r"diagram",
    r"flow", r"compare", r"bench", r"chart", r"plot", r"graph",
]

EXTERNAL_VIDEO_HOSTS = [
    r"youtube\.com", r"youtu\.be", r"bilibili\.com", r"vimeo\.com",
    r"loom\.com", r"streamable\.com", r"asciinema\.org",
]


# --------------------------------------------------------------------------
def http_get(url: str, *, limit: int, head_only: bool = False, tries: int = 3):
    """Return (bytes, content_type, final_url) or (None, None, None)."""
    headers = {"User-Agent": UA, "Accept": "*/*"}
    if TOKEN and "api.github.com" in url:
        headers["Authorization"] = f"Bearer {TOKEN}"
        headers["Accept"] = "application/vnd.github+json"
    req = urllib.request.Request(url, headers=headers, method="HEAD" if head_only else "GET")
    delay = 1.5
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                ctype = (resp.headers.get("Content-Type") or "").split(";")[0].strip()
                length = resp.headers.get("Content-Length")
                if length and int(length) > limit:
                    return None, ctype, resp.geturl()
                if head_only:
                    return b"", ctype, resp.geturl()
                data = resp.read(limit + 1)
                if len(data) > limit:
                    return None, ctype, resp.geturl()
                return data, ctype, resp.geturl()
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 403, 500, 502, 503) and attempt < tries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            return None, None, None
        except Exception:  # noqa: BLE001
            if attempt < tries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            return None, None, None
    return None, None, None


def sniff(data: bytes) -> tuple[str, str]:
    """Return (ext, kind) from magic bytes; ('', 'unknown') when unrecognised."""
    for magic, (ext, kind) in MAGIC.items():
        if data.startswith(magic):
            if magic == b"RIFF":
                if data[8:12] == b"WEBP":
                    return "webp", "image"
                if data[8:12] == b"AVI ":
                    return "avi", "video"
                return "webp", "image"
            return ext, kind
    # mp4 variants put the ftyp box a few bytes in
    if b"ftyp" in data[:16]:
        return "mp4", "video"
    if b"<svg" in data[:400].lower():
        return "svg", "image"
    return "", "unknown"


# --------------------------------------------------------------------------
# video -> GIF, because GitHub will not play a video file
# --------------------------------------------------------------------------
# GitHub's HTML sanitiser removes <video> and <source> from user content, and
# raw.githubusercontent.com serves MP4 as application/octet-stream with
# nosniff. Both were verified against the published page. The only moving image
# GitHub will render is an animated GIF (or WebP) delivered as <img>.
#
# So a project's recording is transcoded here. Three passes, each cheaper than
# the last, because a 2 MB MP4 can easily become a 30 MB GIF without a palette,
# a frame-rate cap and a duration cap.
GIF_PASSES = [
    {"t": 8, "fps": 12, "w": 520},
    {"t": 6, "fps": 10, "w": 420},
    {"t": 5, "fps": 8, "w": 320},
]
MAX_GIF_BYTES = 4_000_000
# An animated image a browser must fetch even while the card is collapsed, so a
# project's own oversized GIF is re-encoded rather than trusted.
GIF_SOFT_CAP = 2_500_000


def transcode_to_gif(data: bytes, ext: str) -> tuple[bytes | None, str]:
    """
    Return (gif_bytes, note). gif_bytes is None when ffmpeg is unavailable or
    every pass exceeded the cap, in which case the caller falls back to a poster
    plus a link rather than emitting a tag GitHub would delete.
    """
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        return None, "ffmpeg unavailable"

    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / f"in.{ext}"
        src.write_bytes(data)
        for i, p in enumerate(GIF_PASSES):
            out = Path(tmp) / f"out{i}.gif"
            # palettegen/paletteuse is what keeps a GIF from looking like 1997
            vf = (f"fps={p['fps']},scale={p['w']}:-1:flags=lanczos,split[a][b];"
                  f"[a]palettegen=max_colors=128[p];[b][p]paletteuse=dither=bayer")
            cmd = [ffmpeg, "-y", "-v", "error", "-i", str(src),
                   "-t", str(p["t"]), "-vf", vf, "-loop", "0", str(out)]
            try:
                res = subprocess.run(cmd, capture_output=True, timeout=180)
            except subprocess.TimeoutExpired:
                continue
            if res.returncode != 0 or not out.exists():
                continue
            blob = out.read_bytes()
            if 0 < len(blob) <= MAX_GIF_BYTES:
                return blob, f"gif pass {i + 1} ({len(blob) / 1e6:.1f} MB)"
        return None, "all gif passes exceeded the cap"


def store(data: bytes, ext: str, slot: str) -> tuple[str, bool]:
    """Content-address the bytes. Returns (relative path, was_new)."""
    h = hashlib.sha256(data).hexdigest()[:16]
    d = MEDIA / slot
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"{h}.{ext}"
    if path.exists() and path.stat().st_size == len(data):
        return str(path.relative_to(ROOT)), False
    path.write_bytes(data)
    return str(path.relative_to(ROOT)), True


# --------------------------------------------------------------------------
# README harvesting
# --------------------------------------------------------------------------
def fetch_readme(full_name: str) -> tuple[str, str]:
    """Return (markdown, default_branch). Empty markdown when unavailable."""
    if not TOKEN:
        return "", "main"
    meta, _ct, _u = http_get(f"https://api.github.com/repos/{full_name}", limit=2_000_000)
    branch = "main"
    if meta:
        try:
            branch = json.loads(meta).get("default_branch") or "main"
        except Exception:  # noqa: BLE001
            pass
    url = f"https://api.github.com/repos/{full_name}/readme"
    data, _ct, _u = http_get(url, limit=1_500_000)
    if not data:
        return "", branch
    try:
        doc = json.loads(data)
        if doc.get("encoding") == "base64" and doc.get("content"):
            import base64

            raw = base64.b64decode(doc["content"]).decode("utf-8", "replace")
            return raw, branch
        if doc.get("download_url"):
            raw, _c, _u = http_get(doc["download_url"], limit=1_500_000)
            if raw:
                return raw.decode("utf-8", "replace"), branch
    except Exception:  # noqa: BLE001
        pass
    return "", branch


def absolutize(src: str, base: str) -> str:
    src = src.strip().strip("<>").strip()
    src = src.split(" ")[0] if " " in src and not src.startswith("http") else src
    src = src.strip("\"'")
    if not src:
        return ""
    if src.startswith(("http://", "https://")):
        return src
    if src.startswith("//"):
        return "https:" + src
    if src.startswith("data:"):
        return ""
    url = urllib.parse.urljoin(base, src.lstrip("./"))
    return url


def is_bad(src: str) -> bool:
    return any(re.search(p, src, re.I) for p in BADGE_PATTERNS)


# A repository that is itself a collection of links does not own the media in
# its README; it republished other projects' screenshots and recordings into its
# own tree. The ownership check cannot see that, because the copy really is
# served from the aggregator's namespace -- `thevibeworks/awesome-typesafe-jev`
# publishes `docs/media/sightmap__turbo.gif`, which is `sightmap/jev-turbo`'s
# recording. So a link list donates no media at all. A logo is a cheap thing to
# lose; attributing someone's work to the wrong author is not.
LINK_LIST_NAME = re.compile(r"^awesome[-_]", re.I)
LINK_LIST_TEXT = re.compile(
    r"\b(?:curated|awesome)\b[^.]{0,40}\b(?:list|collection|directory|resources)\b"
    r"|\b(?:link|resource|community)\s+(?:list|directory)\b"
    r"|\bkeep updating\b|\bshowcases\b", re.I)


def is_link_list(entry: dict) -> bool:
    repo = (entry.get("name") or "").split("/")[-1]
    text = entry.get("summary") or ""
    return bool(LINK_LIST_NAME.match(repo) or LINK_LIST_TEXT.search(text))


def owned_by(url: str, full: str) -> bool:
    """
    True when an asset URL may belong to this repository.

    A file served from raw.githubusercontent.com or github.com carries the
    owning `<owner>/<repo>` in its path. The owner must match the entry's owner:
    a project may keep assets in its own Pages repository, but it may not
    present another account's repository contents as its own.

    URLs on other hosts pass: a project's own uploads land on
    user-images.githubusercontent.com, and embedded CDN media has no owner to
    compare against.
    """
    owner = full.split("/")[0].lower()
    if re.match(r"https?://github\.com/(user-attachments|user-images|"
                r"private-user-images|objects)/", url, re.I):
        return True                       # GitHub's own asset CDN, not a repo
    m = re.match(r"https?://(?:raw\.githubusercontent\.com|githubusercontent\.com)"
                 r"/([^/]+)/([^/]+)/", url, re.I)
    if not m:
        m = re.match(r"https?://github\.com/([^/]+)/([^/]+)/"
                     r"(?:raw|blob|releases|tree)/", url, re.I)
    if m:
        return m.group(1).lower() == owner
    return True


def harvest(readme: str, base: str, full: str) -> dict:
    """
    Extract ranked image and video candidates from a README.

    Every candidate is checked against the owning repository before it is
    accepted. Without that check an aggregator list -- a README that links to
    other projects' screenshots -- donates those projects' media to itself, so
    `thevibeworks/awesome-typesafe-jev` was published showing
    `sightmap/jev-turbo`'s recording. A wrong asset is worse than no asset:
    it attributes someone's work to the wrong author.
    """
    images: list[str] = []
    videos: list[str] = []
    external: list[str] = []

    # markdown images ![alt](src) and html <img src=...>
    for m in re.finditer(r"!\[[^\]]*\]\(\s*([^)\s]+)", readme):
        images.append(absolutize(m.group(1), base))
    for m in re.finditer(r"<img[^>]+src=[\"']([^\"']+)[\"']", readme, re.I):
        images.append(absolutize(m.group(1), base))

    # video tags and <source>
    for m in re.finditer(r"<(?:video|source)[^>]+src=[\"']([^\"']+)[\"']", readme, re.I):
        videos.append(absolutize(m.group(1), base))

    # bare links to media files
    for m in re.finditer(r"\]\(\s*([^)\s]+\.(?:mp4|webm|mov|m4v|gif))", readme, re.I):
        u = absolutize(m.group(1), base)
        (videos if not u.lower().endswith(".gif") else images).append(u)

    # external video embeds -> not playable inline, but the link is valuable
    for m in re.finditer(r"\]\(\s*(https?://[^)\s]+)", readme):
        u = m.group(1)
        if any(re.search(host, u, re.I) for host in EXTERNAL_VIDEO_HOSTS):
            external.append(u)

    def clean(seq: list[str]) -> list[str]:
        seen, out = set(), []
        for u in seq:
            if not u or u in seen or is_bad(u):
                continue
            if not owned_by(u, full):
                continue          # belongs to a different repository
            seen.add(u)
            out.append(u)
        return out

    def score(u: str) -> tuple:
        low = u.lower()
        hinted = any(re.search(h, low) for h in GOOD_HINTS)
        ext = Path(urllib.parse.urlparse(low).path).suffix
        return (
            0 if hinted else 1,
            0 if ext in (".png", ".webp", ".jpg", ".jpeg") else 1,
            len(u),
        )

    images = sorted(clean(images), key=score)
    videos = clean(videos)
    external = clean(external)
    return {"images": images, "videos": videos, "external": external}


# --------------------------------------------------------------------------
def handle_entry(entry: dict, budget: dict) -> dict:
    """
    Build the media record for one entry.

    {
      "bundled": true/false,
      "license_ok": true/false,
      "image": "media/... or https://...",
      "image_remote": "...",
      "video": {"state": "file|animated|external|none", "src": "...", "poster": "..."}
    }
    """
    full = entry["name"]
    lic = (entry.get("license") or "").strip()
    license_ok = lic in PERMISSIVE

    if is_link_list(entry):
        return {"bundled": False, "license_ok": license_ok, "image": "",
                "image_source": "", "video": {"state": "none", "src": "", "poster": ""},
                "source": "link-list (no own media)"}

    readme, branch = fetch_readme(full)
    if not readme:
        return {"bundled": False, "license_ok": license_ok, "image": "",
                "video": {"state": "none", "src": "", "poster": ""}, "source": "no-readme"}

    base = f"https://raw.githubusercontent.com/{full}/{branch}/"
    found = harvest(readme, base, full)
    slot = full.replace("/", "--").lower()

    rec: dict = {
        "bundled": False,
        "license_ok": license_ok,
        "license": lic or "unknown",
        "image": "",
        "image_alt": "",
        "image_source": "",
        "video": {"state": "none", "src": "", "poster": ""},
        "source": "readme",
        "candidates": {"images": len(found["images"]), "videos": len(found["videos"]),
                       "external": len(found["external"])},
    }

    # ---- image -------------------------------------------------------
    for url in found["images"][:6]:
        if budget["bytes"] > MEDIA_BUDGET_BYTES:
            rec["image"] = url          # budget exhausted -> hot-link
            rec["source"] = "readme+hotlink"
            break
        data, ctype, _final = http_get(url, limit=MAX_IMAGE_BYTES)
        if not data:
            continue
        ext, kind = sniff(data)
        if kind != "image" or ext == "svg":
            continue                        # SVG screenshots are rare and unsafe to rehost
        if not license_ok:
            rec["image"] = url              # never re-host a restricted asset
            rec["image_source"] = url
            rec["source"] = "readme+hotlink(license)"
            break
        # A GIF in the image slot is an animated asset, and it is fetched even
        # while the card is collapsed. Re-encode anything oversized.
        if ext == "gif" and len(data) > GIF_SOFT_CAP:
            gif, gnote = transcode_to_gif(data, "gif")
            if gif and len(gif) < len(data):
                data, ext = gif, "gif"
                rec["image_reencoded"] = gnote
        rel, is_new = store(data, ext, slot)
        budget["bytes"] += len(data) if is_new else 0
        budget["files"] += 1 if is_new else 0
        rec["image"] = rel
        rec["image_source"] = url
        rec["bundled"] = True
        rec["image_alt"] = f"{full} screenshot"
        break

    # ---- video -------------------------------------------------------
    # A README <video>/<source>, or a file linked from the README.
    #
    # The goal here is not to store a video; it is to end up with something that
    # MOVES on the published page. A stored MP4 would be invisible, because
    # GitHub deletes <video>. So a real video file is transcoded to GIF, and the
    # original URL is kept as the full-quality link.
    if found["videos"]:
        url = found["videos"][0]
        ext = Path(urllib.parse.urlparse(url.lower()).path).suffix
        cap = MAX_ANIM_BYTES if ext in ANIM_EXT else MAX_VIDEO_BYTES
        data, _ct, _final = http_get(url, limit=cap)
        if data:
            sext, kind = sniff(data)
            if sext == "gif" or kind == "video":
                asset, aext, state = data, sext, ("animated" if sext == "gif" else "file")
                full_quality = "" if sext in ANIM_EXT else url
                note = ""
                if kind == "video":
                    gif, note = transcode_to_gif(data, sext)
                    if gif:
                        asset, aext, state = gif, "gif", "animated"
                elif aext == "gif" and len(asset) > GIF_SOFT_CAP:
                    # The project shipped a heavy GIF. Re-encode it: this file is
                    # fetched by every visitor even before the card is opened.
                    gif, note = transcode_to_gif(asset, "gif")
                    if gif and len(gif) < len(asset):
                        asset = gif
                        full_quality = url
                if license_ok and budget["bytes"] <= MEDIA_BUDGET_BYTES and state == "animated":
                    rel, is_new = store(asset, aext, slot)
                    budget["bytes"] += len(asset) if is_new else 0
                    budget["files"] += 1 if is_new else 0
                    rec["video"] = {
                        "state": state,
                        "src": rel,
                        "poster": rec["image"] if rec["image"].startswith("media/") else "",
                        "full_quality": full_quality,
                        "source_url": url,
                        "note": note,
                    }
                    rec["bundled"] = True
                else:
                    # Not redistributable, or no GIF could be produced within the
                    # cap: link the upstream file and let the card show a poster.
                    rec["video"] = {
                        "state": "file",
                        "src": url,
                        "poster": "",
                        "full_quality": url,
                        "source_url": url,
                        "hotlink": True,
                        "note": note,
                    }

    # an animated image anywhere in the readme still makes a good "video" column
    if rec["video"]["state"] == "none":
        for url in found["images"]:
            if not url.lower().endswith(".gif"):
                continue
            data, _c, _u = http_get(url, limit=MAX_ANIM_BYTES)
            if not data:
                continue
            sext, kind = sniff(data)
            if sext != "gif":
                continue
            if license_ok and budget["bytes"] <= MEDIA_BUDGET_BYTES:
                rel, is_new = store(data, "gif", slot)
                budget["bytes"] += len(data) if is_new else 0
                budget["files"] += 1 if is_new else 0
                rec["video"] = {"state": "animated", "src": rel, "poster": "",
                                "source_url": url}
                rec["bundled"] = True
            else:
                rec["video"] = {"state": "animated", "src": url, "poster": "",
                                "source_url": url, "hotlink": True}
            break

    # external embed (YouTube / Bilibili / Vimeo ...): never playable on GitHub
    if rec["video"]["state"] == "none" and found["external"]:
        rec["video"] = {
            "state": "external",
            "src": found["external"][0],
            "poster": rec["image"] if rec["image"].startswith("media/") else "",
        }

    return rec


def collect_referenced(records: dict) -> set[str]:
    """Every media path the current media.json actually points at."""
    ref: set[str] = set()
    for rec in records.values():
        for key in (rec.get("image"), (rec.get("video") or {}).get("src"),
                    (rec.get("video") or {}).get("poster")):
            if key and not key.startswith(("http://", "https://")):
                ref.add(str(Path(key)))
    return ref


def garbage_collect(records: dict) -> tuple[int, int]:
    """
    Delete bundled assets nothing references any more.

    Media is content-addressed, so changing how an asset is derived leaves the
    previous blob behind. Without this, every re-encode, every improved
    heuristic and every removed entry silently accumulates as dead weight in the
    repository forever. Measured on the first run of this pipeline: 63 orphaned
    files holding 39 of 59 MB.
    """
    ref = collect_referenced(records)
    removed = freed = 0
    if not MEDIA.exists():
        return 0, 0
    for path in MEDIA.rglob("*"):
        if not path.is_file():
            continue
        rel = str(path.relative_to(ROOT))
        if rel in ref:
            continue
        freed += path.stat().st_size
        path.unlink()
        removed += 1
    # drop directories that became empty
    for d in sorted((p for p in MEDIA.rglob("*") if p.is_dir()),
                    key=lambda p: -len(p.parts)):
        try:
            d.rmdir()
        except OSError:
            pass
    return removed, freed


# --------------------------------------------------------------------------
# submissions: media declared by the curator rather than scraped from a README
# --------------------------------------------------------------------------
def pick_variant(urls: list[str], max_width: int) -> str:
    """
    Choose the largest declared video variant that stays within max_width.

    Platform video URLs embed the resolution in the path
    (/vid/avc1/620x360/...), so the choice is made from the URL rather than by
    downloading every variant. Falls back to the first URL when nothing parses.
    """
    best, best_w = "", -1
    for u in urls:
        m = re.search(r"/(\d{2,4})x(\d{2,4})/", u)
        if not m:
            continue
        w = int(m.group(1))
        if w <= max_width and w > best_w:
            best, best_w = u, w
    return best or (urls[0] if urls else "")


def handle_post_entry(entry: dict, budget: dict) -> dict:
    """
    Media for a submission (a post, not a repository).

    The curator declares the poster and the candidate video variants in
    data/submissions.json; this function resolves them the same way a README
    would be resolved: download, transcode the recording to GIF, store
    content-addressed, keep the original as the full-quality link.

    Redistribution: a post has no licence to read, so the include/exclude
    decision is the curator's, which is why these arrive through a reviewed file
    rather than through pattern matching. The provenance is recorded on the card.
    """
    declared = entry.get("declared_media") or {}
    slot = entry["id"].replace(":", "--").replace("/", "--").lower()

    rec: dict = {
        "bundled": False,
        "license_ok": True,
        "license": "post media, supplied by the submitter",
        "image": "",
        "image_alt": "",
        "video": {"state": "none", "src": "", "poster": ""},
        "source": "submission",
    }

    poster_url = declared.get("poster") or ""
    if poster_url:
        data, _ct, _final = http_get(poster_url, limit=MAX_IMAGE_BYTES)
        if data:
            ext, kind = sniff(data)
            if kind == "image" and ext != "svg":
                rel, is_new = store(data, ext, slot)
                budget["bytes"] += len(data) if is_new else 0
                budget["files"] += 1 if is_new else 0
                rec["image"] = rel
                rec["image_alt"] = f"{entry.get('name', '')} still"
                rec["bundled"] = True

    video_url = pick_variant(declared.get("video") or [],
                             int(declared.get("max_width") or 1242))
    if video_url:
        data, _ct, _final = http_get(video_url, limit=MAX_VIDEO_BYTES)
        if data:
            sext, kind = sniff(data)
            if sext == "gif" or kind == "video":
                asset, aext, state = data, sext, ("animated" if sext == "gif" else "file")
                note = ""
                if kind == "video":
                    gif, note = transcode_to_gif(data, sext)
                    if gif:
                        asset, aext, state = gif, "gif", "animated"
                if state == "animated" and budget["bytes"] <= MEDIA_BUDGET_BYTES:
                    rel, is_new = store(asset, aext, slot)
                    budget["bytes"] += len(asset) if is_new else 0
                    budget["files"] += 1 if is_new else 0
                    rec["video"] = {
                        "state": "animated",
                        "src": rel,
                        "poster": rec["image"] if rec["image"].startswith("media/") else "",
                        "full_quality": video_url,
                        "source_url": video_url,
                        "note": note,
                    }
                    rec["bundled"] = True
                else:
                    rec["video"] = {
                        "state": "file",
                        "src": video_url,
                        "poster": "",
                        "full_quality": video_url,
                        "source_url": video_url,
                        "note": note,
                    }
    return rec


def main() -> int:
    print(f"== awesome-claude-mods :: media @ {STAMP} ==")
    entries_path = DATA / "entries.json"
    if not entries_path.exists():
        print("   !! data/entries.json missing; run curate.py first", file=sys.stderr)
        return 1

    doc = json.loads(entries_path.read_text())
    entries = doc.get("entries", [])

    media_path = DATA / "media.json"
    prior: dict = {}
    if media_path.exists():
        try:
            prior = json.loads(media_path.read_text()).get("entries", {})
        except Exception:  # noqa: BLE001
            prior = {}

    budget = {"bytes": sum(1 for _ in MEDIA.rglob("*")), "files": 0}
    budget["bytes"] = sum(f.stat().st_size for f in MEDIA.rglob("*") if f.is_file())
    print(f"   existing media: {budget['bytes'] / 1e6:.1f} MB")

    only = set(os.environ.get("MEDIA_ONLY", "").split(",")) - {""}
    max_n = int(os.environ.get("MEDIA_MAX", "0")) or len(entries)
    # Bypass the per-repo cache. Used when the extraction logic itself changed,
    # because then the cached record is stale even though the repo has not moved.
    force = os.environ.get("MEDIA_FORCE", "") not in ("", "0", "false")

    results = dict(prior)
    processed = 0
    errors = 0
    for e in entries:
        if e["kind"] not in ("repo", "post"):
            continue
        if only and e["id"] not in only and e["name"] not in only:
            continue
        if processed >= max_n:
            break
        # reuse a cached record only when the repo did not move
        cached = prior.get(e["id"])
        # Cached on pushed_at alone. Requiring a found image here would mean the
        # ~300 projects that publish no media get their README refetched on every
        # tick, which is both slow and pointless: an unpushed repository cannot
        # have gained an asset.
        if not force and cached and cached.get("pushed_at") == e.get("pushed_at"):
            results[e["id"]] = cached
            continue
        try:
            # Submissions declare their media; repositories have theirs scraped.
            rec = (handle_post_entry(e, budget) if e["kind"] == "post"
                   else handle_entry(e, budget))
        except Exception as exc:  # noqa: BLE001 - one bad repo must not stop the run
            print(f"   !! {e['name']}: {type(exc).__name__}: {exc}", file=sys.stderr)
            errors += 1
            continue
        rec["pushed_at"] = e.get("pushed_at")
        results[e["id"]] = rec
        processed += 1
        if processed % 10 == 0:
            print(f"   .. {processed} processed, {budget['bytes'] / 1e6:.1f} MB bundled")
        time.sleep(0.25)

    # Drop records whose entry is no longer listed. Files were already collected
    # against the current records, but the records themselves accumulated: 792 of
    # them for 497 entries, all retained forever.
    live_ids = {e["id"] for e in entries}
    stale = [k for k in results if k not in live_ids]
    for k in stale:
        results.pop(k, None)
    if stale:
        print(f"   pruned {len(stale)} media records for entries no longer listed")

    removed, freed = garbage_collect(results)
    # Report what is actually on disk. The running tally cannot be authoritative
    # once files have been pruned, and an inflated number is worse than none.
    on_disk = sum(f.stat().st_size for f in MEDIA.rglob("*") if f.is_file())
    budget["bytes"] = on_disk

    out = {"generated_at": STAMP, "entries": results,
           "bundled_bytes": on_disk,
           "bundled_files": sum(1 for f in MEDIA.rglob("*") if f.is_file())}
    if removed:
        print(f"   gc: removed {removed} unreferenced assets ({freed / 1e6:.1f} MB)")

    media_path.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")

    with_img = sum(1 for v in results.values() if v.get("image"))
    with_vid = sum(1 for v in results.values() if (v.get("video") or {}).get("state") not in (None, "", "none"))
    bundled = sum(1 for v in results.values() if v.get("bundled"))
    print(f"   media records: {len(results)}  image={with_img} video={with_vid} "
          f"bundled={bundled} errors={errors}")
    print(f"   bundled size: {budget['bytes'] / 1e6:.2f} MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())