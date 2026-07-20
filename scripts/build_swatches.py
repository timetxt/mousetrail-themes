#!/usr/bin/env python3
"""Build assets/swatches/<file-stem>.svg for every themes/**/*.json in this repo.

Pure Python stdlib only (json, pathlib, sys, colorsys) -- no third-party
imports, so this script runs anywhere python3 runs. Paths are resolved from
this script's own location, so it works regardless of the caller's current
working directory.

Usage:
    python3 scripts/build_swatches.py

Output: assets/swatches/*.svg -- one SVG "trail demo" card per theme file,
named after the file's stem (themes/official/neon/aurora.json ->
assets/swatches/aurora.svg), showing a smooth S-curve trail stroked with the
theme's gradient (tail = location 0 on the left, head = location 1 on the
right, mirroring how the app paints a trail), a glow underlay, and a bright
mouse-cursor glyph at the head over a soft halo in the final stop's color.

IMPORTANT: assets/swatches/ is a GENERATED directory. This script is its SOLE
producer -- every file in it is written or pruned here and none should ever
be hand-edited or hand-added. Re-running this script is the only supported
way to add, update, or remove a swatch; it also deletes any orphan SVG whose
theme file no longer exists, so assets/swatches/ always mirrors themes/.

The script is deterministic: fixed path geometry, stable float formatting,
and sorted iteration order mean re-running it with unchanged theme files
reproduces byte-identical output (idempotent).
"""

import colorsys
import json
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
THEMES_DIR = REPO_ROOT / "themes"
SWATCHES_DIR = REPO_ROOT / "assets" / "swatches"

RAINBOW_STOP_COUNT = 6

# Canvas geometry. Chosen so the trail path (including its widest glow pass)
# stays well inside the rounded card at every point.
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 140
CARD_RADIUS = 12
CARD_FILL = "#17181d"

# Fixed, hand-tuned S-curve from tail (left) to head (right). Shared by every
# swatch -- only the stroke gradient and head-dot color vary per theme.
TAIL_X, TAIL_Y = 56, 102
HEAD_X, HEAD_Y = 584, 62
PATH_D = (
    f"M{TAIL_X} {TAIL_Y} "
    f"C168 102 168 34 302 34 "
    f"S436 102 {HEAD_X} {HEAD_Y}"
)

MAIN_STROKE_WIDTH = 8.0
GLOW_STROKE_WIDTH = MAIN_STROKE_WIDTH * 2.2
GLOW_OPACITY = 0.35
GLOW_BLUR_STDDEV = 6

HEAD_GLOW_RADIUS = 16
HEAD_GLOW_OPACITY = 0.35

# Classic arrow-cursor glyph drawn at the head (the trail follows the mouse
# pointer, so the head is the pointer). Path is in a ~14x20 local box with the
# hotspot (arrow tip) at 0,0; translated so the tip sits exactly on the path's
# head point. White fill with a dark outline so it reads on any theme color.
CURSOR_PATH_D = "M0 0 L0 17 L4.6 12.7 L7.6 19.7 L10.4 18.5 L7.4 11.6 L13.6 11.6 Z"
CURSOR_FILL = "#ffffff"
CURSOR_OUTLINE = "#1b1c21"
CURSOR_OUTLINE_WIDTH = 1.5
CURSOR_SCALE = 1.1


def _fmt(value):
    """Stable, deterministic float formatting for SVG attributes: rounds to
    4 decimal places and strips trailing zeros/dot so e.g. 0.3333333333333333
    -> "0.3333" and 1.0 -> "1" on every run, regardless of float repr
    differences.
    """
    rounded = round(float(value), 4)
    text = f"{rounded:.4f}".rstrip("0").rstrip(".")
    return text if text else "0"


def _to_hex_component(value):
    clamped = max(0.0, min(1.0, float(value)))
    return f"{round(clamped * 255):02X}"


def _stop_hex(stop):
    return (
        f"#{_to_hex_component(stop.get('red', 0))}"
        f"{_to_hex_component(stop.get('green', 0))}"
        f"{_to_hex_component(stop.get('blue', 0))}"
    )


def _rainbow_stops(count: int = RAINBOW_STOP_COUNT):
    """A representative rainbow stop list: `count` hues evenly spaced around
    the color wheel at full saturation/value, with evenly spaced `location`s
    0..1 -- mirrors scripts/build_index.py's gallery-swatch treatment of
    rainbow mode (a display-only sample; the app itself animates hue
    continuously as the mouse moves).
    """
    stops = []
    for i in range(count):
        hue = i / count
        location = i / (count - 1)
        red, green, blue = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        stops.append(
            {"red": red, "green": green, "blue": blue, "alpha": 1.0, "location": location}
        )
    return stops


def _resolve_stops(color_mode):
    """Resolves any of the three colorMode shapes to a location-sorted stop
    list for drawing the gradient:
      - gradient -> its own stops, as authored (sorted by location).
      - fixed    -> two identical stops (a flat single-color "gradient").
      - rainbow  -> a representative 6-hue rainbow stop list.
    Returns [] for an unrecognized/malformed colorMode so a bad theme file
    degrades to a skip instead of crashing the build.
    """
    if not isinstance(color_mode, dict):
        return []

    if "gradient" in color_mode:
        gradient = color_mode["gradient"]
        stops = gradient.get("stops") if isinstance(gradient, dict) else None
        if isinstance(stops, list) and stops:
            return sorted(stops, key=lambda s: s.get("location", 0))
        return []

    if "fixed" in color_mode:
        fixed = color_mode["fixed"]
        if not isinstance(fixed, dict):
            return []
        base = {
            "red": fixed.get("red", 0),
            "green": fixed.get("green", 0),
            "blue": fixed.get("blue", 0),
            "alpha": fixed.get("alpha", 1),
        }
        return [{**base, "location": 0.0}, {**base, "location": 1.0}]

    if "rainbow" in color_mode:
        return _rainbow_stops()

    return []


def _first_theme(doc):
    themes = doc.get("themes")
    if not isinstance(themes, list):
        return None
    for theme in themes:
        if isinstance(theme, dict) and isinstance(theme.get("style"), dict):
            return theme
    return None


def _render_svg(gradient_id, stops):
    stop_els = "\n".join(
        f'      <stop offset="{_fmt(s.get("location", 0))}" stop-color="{_stop_hex(s)}"/>'
        for s in stops
    )
    head_hex = _stop_hex(stops[-1])

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}" viewBox="0 0 {CANVAS_WIDTH} {CANVAS_HEIGHT}" role="img">
  <defs>
    <linearGradient id="{gradient_id}" gradientUnits="userSpaceOnUse" x1="{TAIL_X}" y1="0" x2="{HEAD_X}" y2="0">
{stop_els}
    </linearGradient>
    <filter id="{gradient_id}-blur" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="{GLOW_BLUR_STDDEV}"/>
    </filter>
  </defs>
  <rect x="0" y="0" width="{CANVAS_WIDTH}" height="{CANVAS_HEIGHT}" rx="{CARD_RADIUS}" fill="{CARD_FILL}"/>
  <path d="{PATH_D}" fill="none" stroke="url(#{gradient_id})" stroke-width="{_fmt(GLOW_STROKE_WIDTH)}" stroke-linecap="round" opacity="{_fmt(GLOW_OPACITY)}" filter="url(#{gradient_id}-blur)"/>
  <path d="{PATH_D}" fill="none" stroke="url(#{gradient_id})" stroke-width="{_fmt(MAIN_STROKE_WIDTH)}" stroke-linecap="round"/>
  <circle cx="{HEAD_X}" cy="{HEAD_Y}" r="{HEAD_GLOW_RADIUS}" fill="{head_hex}" opacity="{_fmt(HEAD_GLOW_OPACITY)}" filter="url(#{gradient_id}-blur)"/>
  <g transform="translate({HEAD_X} {HEAD_Y}) scale({_fmt(CURSOR_SCALE)})">
    <path d="{CURSOR_PATH_D}" fill="{CURSOR_FILL}" stroke="{CURSOR_OUTLINE}" stroke-width="{_fmt(CURSOR_OUTLINE_WIDTH)}" stroke-linejoin="round"/>
  </g>
</svg>
"""


def build_swatches(themes_dir: pathlib.Path, swatches_dir: pathlib.Path, repo_root: pathlib.Path):
    """Walks themes_dir for *.json files (sorted for deterministic output),
    writes assets/swatches/<stem>.svg for each, and returns
    (written_stems, skipped_labels).
    """
    written_stems = {}
    skipped = []

    for file_path in sorted(themes_dir.rglob("*.json")):
        label = str(file_path.relative_to(repo_root))
        stem = file_path.stem

        try:
            doc = json.loads(file_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"skipping {label}: {exc}", file=sys.stderr)
            skipped.append(label)
            continue

        theme = _first_theme(doc) if isinstance(doc, dict) else None
        if theme is None:
            print(f"skipping {label}: no usable 'themes' entry", file=sys.stderr)
            skipped.append(label)
            continue

        color_mode = theme["style"].get("colorMode", {})
        stops = _resolve_stops(color_mode)
        if not stops:
            print(f"skipping {label}: no usable colorMode stops", file=sys.stderr)
            skipped.append(label)
            continue

        if stem in written_stems:
            print(
                f"error: filename stem {stem!r} used by both "
                f"{written_stems[stem]!r} and {label!r} -- swatch names must "
                "be unique across all collections",
                file=sys.stderr,
            )
            sys.exit(1)

        svg = _render_svg(f"{stem}-grad", stops)
        swatches_dir.mkdir(parents=True, exist_ok=True)
        (swatches_dir / f"{stem}.svg").write_text(svg, encoding="utf-8")
        written_stems[stem] = label

    return written_stems, skipped


def prune_orphans(swatches_dir: pathlib.Path, keep_stems):
    if not swatches_dir.is_dir():
        return []

    removed = []
    for svg_path in sorted(swatches_dir.glob("*.svg")):
        if svg_path.stem not in keep_stems:
            svg_path.unlink()
            removed.append(svg_path.name)
    return removed


def main():
    written_stems, skipped = build_swatches(THEMES_DIR, SWATCHES_DIR, REPO_ROOT)
    removed = prune_orphans(SWATCHES_DIR, set(written_stems))

    print(f"Wrote {len(written_stems)} swatch(es) to {SWATCHES_DIR.relative_to(REPO_ROOT)}")
    if removed:
        print(f"Pruned {len(removed)} orphan swatch(es): {', '.join(removed)}")
    if skipped:
        print(f"Skipped {len(skipped)} theme file(s) (see warnings above)", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
