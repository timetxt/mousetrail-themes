#!/usr/bin/env python3
"""Build docs/themes.json from every themes/**/*.json in this repo.

Pure Python stdlib only (json, pathlib, sys, colorsys) -- no third-party
imports, so this script runs anywhere python3 runs. Paths are resolved from
this script's own location, so it works regardless of the caller's current
working directory.

Usage:
    python3 scripts/build_index.py

Output: docs/themes.json -- a flat, deterministically ordered index of every
theme in the repo, consumed by the docs/ gallery (docs/app.js). Ordering is
by collection (designer, neon, community), then by filename, so the output
diffs cleanly between runs.

IMPORTANT: docs/themes.json is a GENERATED file. It is produced only by this
script and must never be hand-edited -- JSON itself has no comment syntax to
carry that warning, so it is recorded here and in this script's own output.
"""

import colorsys
import json
import pathlib
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
THEMES_DIR = REPO_ROOT / "themes"
OUTPUT_PATH = REPO_ROOT / "docs" / "themes.json"

# Path segment (relative to themes/) -> collection label, matching the repo
# layout: themes/official/designer, themes/official/neon, themes/community.
COLLECTION_BY_SEGMENT = {
    "designer": "designer",
    "neon": "neon",
    "community": "community",
}

COLLECTION_ORDER = {"designer": 0, "neon": 1, "community": 2}

RAINBOW_STOP_COUNT = 6


def _stable_id(rel_path: str) -> str:
    """A deterministic, path-derived identifier suitable for UI state."""
    stem = rel_path.removesuffix(".json").replace("/", "-").replace("_", "-")
    return "theme-" + stem.lower()


def _collection_for(file_path: pathlib.Path) -> str:
    """Derives the collection ('designer'/'neon'/'community') from the file's
    path segments relative to themes/, e.g. themes/official/neon/aurora.json
    -> 'neon', themes/community/foo.json -> 'community'.
    """
    rel_parts = file_path.relative_to(THEMES_DIR).parts
    for part in rel_parts:
        if part in COLLECTION_BY_SEGMENT:
            return COLLECTION_BY_SEGMENT[part]
    return "community"


def _rainbow_stops(count: int = RAINBOW_STOP_COUNT):
    """A representative rainbow stop list: `count` hues evenly spaced around
    the color wheel at full saturation/value, evenly spaced `location`s
    0..1. This is a display-only representative sample -- the real rainbow
    mode animates hue continuously as the mouse moves; the gallery just needs
    something to draw a swatch with, hence the "rainbow": true flag alongside
    it so the site can label it distinctly from an actual authored gradient.
    """
    stops = []
    for i in range(count):
        hue = i / count  # 0..1, one full trip around the color wheel
        location = i / (count - 1)
        red, green, blue = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        stops.append(
            {
                "red": red,
                "green": green,
                "blue": blue,
                "alpha": 1.0,
                "location": location,
            }
        )
    return stops


def _resolve_stops(color_mode: dict):
    """Resolves any of the three colorMode shapes to a (stops, is_rainbow)
    pair the gallery can render as a gradient swatch:
      - gradient -> its own stops, as authored.
      - fixed    -> a synthetic 2-stop list of the same color (a flat
                    "gradient" of one color, head to tail).
      - rainbow  -> a representative 6-hue rainbow stop list, flagged so the
                    site can label it as animated rather than a fixed
                    gradient.
    Returns ([], False) for an unrecognized/malformed colorMode so a bad
    theme file degrades to an empty swatch instead of crashing the build.
    """
    if not isinstance(color_mode, dict):
        return [], False

    if "gradient" in color_mode:
        gradient = color_mode["gradient"]
        stops = gradient.get("stops") if isinstance(gradient, dict) else None
        if isinstance(stops, list):
            return stops, False
        return [], False

    if "fixed" in color_mode:
        fixed = color_mode["fixed"]
        if not isinstance(fixed, dict):
            return [], False
        base = {
            "red": fixed.get("red", 0),
            "green": fixed.get("green", 0),
            "blue": fixed.get("blue", 0),
            "alpha": fixed.get("alpha", 1),
        }
        return [
            {**base, "location": 0.0},
            {**base, "location": 1.0},
        ], False

    if "rainbow" in color_mode:
        return _rainbow_stops(), True

    return [], False


def build_index(themes_dir: pathlib.Path, repo_root: pathlib.Path):
    """Walks themes_dir for *.json files and returns the list of per-theme
    index entries, in deterministic (collection, filename) order.
    """
    entries = []

    for file_path in sorted(themes_dir.rglob("*.json")):
        rel_path = file_path.relative_to(repo_root).as_posix()
        collection = _collection_for(file_path)
        # themes/community/<github-username>/<name>.json — attribute the
        # contributor from the per-user directory.
        rel_parts = file_path.relative_to(themes_dir).parts
        author = rel_parts[1] if rel_parts[0] == "community" and len(rel_parts) >= 3 else None

        try:
            doc = json.loads(file_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"skipping {rel_path}: {exc}", file=sys.stderr)
            continue

        themes = doc.get("themes")
        if not isinstance(themes, list):
            print(f"skipping {rel_path}: no 'themes' array", file=sys.stderr)
            continue

        if len(themes) != 1:
            raise ValueError(f"{rel_path}: gallery theme files must contain exactly one theme, found {len(themes)}")

        for theme in themes:
            if not isinstance(theme, dict):
                continue
            name = theme.get("name")
            style = theme.get("style")
            if not isinstance(name, str) or not isinstance(style, dict):
                continue

            color_mode = style.get("colorMode", {})
            stops, is_rainbow = _resolve_stops(color_mode)

            entry = {
                "id": _stable_id(rel_path),
                "name": name,
                "collection": collection,
                "path": rel_path,
                "stops": stops,
                "lifetime": style.get("lifetime"),
                "widthScale": style.get("widthScale"),
                "preview": "assets/previews/" + _stable_id(rel_path) + ".svg",
            }
            if author:
                entry["author"] = author
            if is_rainbow:
                entry["rainbow"] = True

            entries.append((collection, file_path.name, entry))

    entries.sort(key=lambda item: (COLLECTION_ORDER.get(item[0], 99), item[1]))
    return [entry for _, _, entry in entries]


def main():
    themes = build_index(THEMES_DIR, REPO_ROOT)

    output = {
        "_generated_by": "scripts/build_index.py -- do not hand-edit this file",
        "version": 2,
        "themes": themes,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(output, indent=2, sort_keys=False) + "\n", encoding="utf-8"
    )

    print(f"Wrote {len(themes)} theme(s) to {OUTPUT_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
