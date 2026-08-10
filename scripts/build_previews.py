#!/usr/bin/env python3
"""Create deterministic, local silk-preview SVGs for the public gallery.

The previews are decorative. Theme JSON remains authoritative for all colours
and app behaviour; a missing preview is handled by the page's CSS fallback.
"""

import colorsys
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
THEMES = ROOT / "themes"
OUT = ROOT / "docs" / "assets" / "previews"


def ident(path):
    return "theme-" + path.relative_to(ROOT).as_posix().removesuffix(".json").replace("/", "-").replace("_", "-").lower()


def hex_color(stop):
    part = lambda key: max(0, min(255, round(float(stop.get(key, 0)) * 255)))
    return "#%02X%02X%02X" % (part("red"), part("green"), part("blue"))


def rainbow():
    values = []
    for n in range(6):
        r, g, b = colorsys.hsv_to_rgb(n / 5, 0.85, 1)
        values.append({"red": r, "green": g, "blue": b, "location": n / 5})
    return values


def stops_for(theme):
    mode = theme.get("style", {}).get("colorMode", {})
    if "gradient" in mode:
        stops = mode["gradient"].get("stops", [])
    elif "fixed" in mode:
        stops = [{**mode["fixed"], "location": 0}, {**mode["fixed"], "location": 1}]
    elif "rainbow" in mode:
        stops = rainbow()
    else:
        stops = []
    return sorted(stops, key=lambda item: item.get("location", 0)) or [{"red": .35, "green": .31, "blue": .28, "location": 0}, {"red": .8, "green": .7, "blue": .55, "location": 1}]


def svg(name, stops):
    stop_nodes = "".join('<stop offset="%.3f" stop-color="%s"/>' % (float(s.get("location", 0)), hex_color(s)) for s in stops)
    last = hex_color(stops[-1])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" role="img" aria-label="{html.escape(name)} silk preview">
<defs><linearGradient id="c" x1="0" y1="0" x2="1" y2="1">{stop_nodes}</linearGradient><radialGradient id="v"><stop offset="0" stop-color="#fff" stop-opacity=".08"/><stop offset=".72" stop-color="#050405" stop-opacity=".18"/><stop offset="1" stop-color="#050405" stop-opacity=".72"/></radialGradient><filter id="b"><feGaussianBlur stdDeviation="30"/></filter><filter id="g"><feGaussianBlur stdDeviation="9"/></filter></defs>
<rect width="960" height="600" fill="url(#c)"/>
<path d="M-80 156C126 42 282 250 482 132S786 54 1050 28" fill="none" stroke="#fff8eb" stroke-width="150" opacity=".22" filter="url(#b)"/>
<path d="M-62 184C133 72 288 280 492 160S798 82 1050 52" fill="none" stroke="{last}" stroke-width="96" opacity=".32" filter="url(#b)"/>
<path d="M-80 385C105 270 282 468 480 324S786 244 1050 394" fill="none" stroke="#050405" stroke-width="164" opacity=".56" filter="url(#b)"/>
<path d="M-62 369C120 274 294 448 488 306S792 252 1045 366" fill="none" stroke="#fffaf0" stroke-width="12" opacity=".54" filter="url(#g)"/>
<rect width="960" height="600" fill="url(#v)"/>
</svg>'''


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    expected = set()
    for path in sorted(THEMES.rglob("*.json")):
        doc = json.loads(path.read_text(encoding="utf-8"))
        items = doc.get("themes", [])
        if len(items) != 1:
            raise ValueError(f"{path.relative_to(ROOT)} must contain exactly one theme")
        file = OUT / (ident(path) + ".svg")
        expected.add(file.name)
        file.write_text(svg(items[0].get("name", path.stem), stops_for(items[0])), encoding="utf-8")
    # Do not delete stale assets automatically; report them for deliberate archival.
    stale = sorted(p.name for p in OUT.glob("*.svg") if p.name not in expected)
    if stale:
        print("Warning: stale preview assets (not deleted): " + ", ".join(stale), file=sys.stderr)
    print(f"Wrote {len(expected)} preview(s) to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
