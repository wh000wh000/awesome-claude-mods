#!/usr/bin/env python3
"""
awesome-claude-mods :: build_assets.py

Builds the repository's visual layer, following the beautify-github-readme
method: deterministic SVG carries the layout and the typography, a generated
raster supplies the project-specific subject, and the two are composed into the
published asset.

Published artifacts
  assets/readme/hero.png         composed hero (the only thing the README loads)

Editable sources kept alongside, never loaded by the README
  assets/readme/sources/hero.subject.png   raw generated subject, no text in it
  assets/readme/sources/hero.layout.svg    layout + typography over the subject
  assets/readme/sources/hero.prompt.txt    the exact prompt used

Why the split: keeping the raster in a separate file rather than base64 inside
the SVG keeps the editable source reviewable in a diff, and exact copy stays out
of the stochastic generated layer where text rendering is unreliable.

Regenerating (needs the image router credentials; the prompt is committed):
  python3 scripts/build_assets.py --generate
Rendering only (raster already present, no credentials needed):
  python3 scripts/build_assets.py
"""

from __future__ import annotations

import argparse
import base64
import html
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "readme"
SOURCES = ASSETS / "sources"

# --------------------------------------------------------------------------
# art direction, frozen
# --------------------------------------------------------------------------
PALETTE = {
    "bg": "#0B0F14",
    "fg": "#E6EDF3",
    "muted": "#8B98A5",
    "primary": "#14B8A6",
    "primary_dim": "#0D9488",
    "accent": "#F0A93B",
    "line": "#1F2A36",
}
FONT_STACK = "'Helvetica Neue', Helvetica, Arial, 'Segoe UI', sans-serif"
MONO_STACK = "'SF Mono', Menlo, Consolas, 'DejaVu Sans Mono', monospace"

W, H = 2400, 520          # banner strip, not a poster: ~4.6:1
SUBJECT_X = 1120          # the generated subject occupies the right window

HERO_PROMPT = """An abstract, cinematic technical illustration for a software repository banner.
STRICT: absolutely no text, no letters, no numbers, no words, no captions, no logos, no watermarks, no UI chrome, no people, no faces.

Subject: a decision gate. From the left edge, a wide field of many faint teal light rays converges inward toward a narrow vertical aperture slightly right of centre. On the far right the rays re-emerge as a small set of distinct, evenly spaced horizontal bars of varying length, teal and warm amber, reading like a probability distribution.

Style: deep near-black background (#0B0F14) with an extremely subtle fine grid. Thin precise lines, volumetric glow, soft bloom, high contrast, restrained and editorial, scientific instrument aesthetic. Flat vector-like rendering, crisp edges, not photorealistic, no heavy shadows, no neon clutter.

Composition: leave the left third visually calm and dark so typography can be overlaid there. Wide cinematic aspect ratio."""


# --------------------------------------------------------------------------
def esc(t: str) -> str:
    return html.escape(t, quote=True)


def render_svg_to_png(svg_path: Path, out_path: Path, width: int) -> bool:
    """Rasterise with rsvg-convert, which resolves relative <image> hrefs."""
    exe = shutil.which("rsvg-convert")
    if not exe:
        print("  !! rsvg-convert not found; cannot rasterise", file=sys.stderr)
        return False
    out_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = [exe, "-w", str(width), "-o", str(out_path), str(svg_path)]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  !! rsvg-convert failed: {res.stderr.strip()[:400]}", file=sys.stderr)
        return False
    return True


# --------------------------------------------------------------------------
def generate_subject() -> bool:
    """Ask the image router for a fresh textless subject image."""
    SOURCES.mkdir(parents=True, exist_ok=True)
    (SOURCES / "hero.prompt.txt").write_text(HERO_PROMPT + "\n")

    helper = Path.home() / ".codex/skills/guildos-imagegen-router/scripts/guildos_image_generate.py"
    if not helper.exists():
        helper = Path.home() / ".agents/skills/guildos-imagegen-router/scripts/guildos_image_generate.py"
    if not helper.exists():
        print(f"  !! image router helper not found at {helper}", file=sys.stderr)
        return False

    out = SOURCES / "hero.subject.png"
    print("   generating hero subject via image router ...")
    res = subprocess.run(
        [sys.executable, str(helper),
         "--prompt-file", str(SOURCES / "hero.prompt.txt"),
         "--out", str(out),
         "--size", "1536x1024", "--quality", "high",
         "--output-format", "png", "--timeout", "300"],
        capture_output=True, text=True,
    )
    if res.returncode != 0:
        print(f"  !! generation failed: {(res.stderr or res.stdout).strip()[:400]}",
              file=sys.stderr)
        return False
    print(f"   {res.stdout.strip()[:120]}")
    return True


# --------------------------------------------------------------------------
def build_hero_svg() -> Path:
    """
    Compose the banner strip.

    Form factor is deliberate. A README's first screen should reach content
    quickly, so this is a wide, shallow strip (~4.6:1) rather than a poster —
    the convention for project banners on GitHub, where it renders about
    900 x 195. Typography sits left, the generated subject occupies a hard-edged
    window on the right, and a gradient fade removes the seam between them.
    """
    subject = "hero.subject.png"
    p = PALETTE
    sub_w = W - SUBJECT_X

    parts: list[str] = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
    )
    parts.append(f'''<defs>
  <linearGradient id="seam" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="{p['bg']}" stop-opacity="1"/>
    <stop offset="55%"  stop-color="{p['bg']}" stop-opacity="0.72"/>
    <stop offset="100%" stop-color="{p['bg']}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="{p['primary']}" stop-opacity="0.95"/>
    <stop offset="100%" stop-color="{p['primary']}" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="glow" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="{p['primary']}" stop-opacity="0.10"/>
    <stop offset="100%" stop-color="{p['primary']}" stop-opacity="0"/>
  </linearGradient>
</defs>''')

    # canvas + the same faint grid used by every other asset in the set
    parts.append(f'<rect width="{W}" height="{H}" fill="{p["bg"]}"/>')
    for gx in range(0, W, 60):
        parts.append(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" '
                     f'stroke="{p["line"]}" stroke-width="1" opacity="0.30"/>')
    for gy in range(0, H, 60):
        parts.append(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}" '
                     f'stroke="{p["line"]}" stroke-width="1" opacity="0.30"/>')

    # the generated subject, cropped to the window
    # Drawn narrower than the window so the longest probability bar keeps air on
    # its right instead of being clipped by the canvas edge.
    draw_w = int(sub_w * 0.86)
    parts.append(f'<clipPath id="subj"><rect x="{SUBJECT_X}" y="0" '
                 f'width="{sub_w}" height="{H}"/></clipPath>')
    parts.append(
        f'<g clip-path="url(#subj)"><image x="{SUBJECT_X}" y="0" '
        f'width="{draw_w}" height="{H}" xlink:href="{esc(subject)}" '
        f'preserveAspectRatio="xMidYMid slice"/></g>'
    )
    # fade the subject into the background instead of cutting it
    parts.append(
        f'<rect x="{SUBJECT_X - 340}" y="0" width="680" height="{H}" fill="url(#seam)"/>'
    )
    parts.append(
        f'<rect x="{SUBJECT_X}" y="0" width="{sub_w}" height="{H}" fill="url(#glow)"/>'
    )

    x = 140

    # eyebrow + rule
    parts.append(
        f'<text x="{x}" y="126" font-family="{FONT_STACK}" font-size="23" '
        f'font-weight="600" letter-spacing="5.5" fill="{p["primary"]}">'
        f'EVIDENCE-GRADED INDEX &#183; REBUILT EVERY TWO HOURS</text>'
    )
    parts.append(f'<rect x="{x}" y="148" width="430" height="3" fill="url(#rule)"/>')

    # title
    parts.append(
        f'<text x="{x}" y="248" font-family="{FONT_STACK}" font-size="86" '
        f'font-weight="700" letter-spacing="-2.5" fill="#FFFFFF">Awesome Jev Live</text>'
    )

    # tagline
    parts.append(
        f'<text x="{x}" y="303" font-family="{FONT_STACK}" font-size="27" '
        f'fill="{p["muted"]}">'
        f'The Jev / System One ecosystem, filtered twice an hour.</text>'
    )

    # the product shape stated as a schema rather than a slogan
    chip_x, chip_y, chip_w, chip_h = x, 336, 880, 58
    parts.append(
        f'<rect x="{chip_x}" y="{chip_y}" width="{chip_w}" height="{chip_h}" rx="10" '
        f'fill="#0E141B" fill-opacity="0.9" stroke="{p["line"]}" stroke-width="1.6"/>'
    )
    parts.append(
        f'<text x="{chip_x + 24}" y="{chip_y + 38}" font-family="{MONO_STACK}" '
        f'font-size="23" fill="{p["fg"]}">'
        f'state + typed questions &#8594; decisions + probabilities</text>'
    )

    # evidence legend on the first screen, because it is the differentiator
    legend = [
        ("official", p["primary"]),
        ("observed", "#7DD3FC"),
        ("inferred", p["accent"]),
        ("unverified", p["muted"]),
    ]
    lx = x
    for label, colour in legend:
        parts.append(f'<circle cx="{lx + 8}" cy="446" r="8" fill="{colour}"/>')
        parts.append(
            f'<text x="{lx + 26}" y="455" font-family="{FONT_STACK}" '
            f'font-size="24" font-weight="500" fill="{p["muted"]}">{esc(label)}</text>'
        )
        lx += 34 + len(label) * 14
    parts.append('</svg>')

    SOURCES.mkdir(parents=True, exist_ok=True)
    path = SOURCES / "hero.layout.svg"
    path.write_text("\n".join(parts) + "\n")
    return path


# --------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--generate", action="store_true",
                    help="regenerate the raster subject via the image router")
    ap.add_argument("--width", type=int, default=2400,
                    help="published hero width in pixels")
    args = ap.parse_args()

    SOURCES.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)

    subject = SOURCES / "hero.subject.png"
    if args.generate or not subject.exists():
        if not generate_subject() and not subject.exists():
            print("  !! no subject image available; hero cannot be composed",
                  file=sys.stderr)
            return 1
    else:
        print(f"   reusing existing subject ({subject.stat().st_size / 1e6:.2f} MB)")

    if not (SOURCES / "hero.prompt.txt").exists():
        (SOURCES / "hero.prompt.txt").write_text(HERO_PROMPT + "\n")

    layout = build_hero_svg()
    print(f"   wrote {layout.relative_to(ROOT)}")

    hero = ASSETS / "hero.png"
    if render_svg_to_png(layout, hero, args.width):
        print(f"   wrote {hero.relative_to(ROOT)} "
              f"({hero.stat().st_size / 1e6:.2f} MB, {args.width}px wide)")
    else:
        return 1

    print(f"   wrote {pipe.relative_to(ROOT)} ({pipe.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())