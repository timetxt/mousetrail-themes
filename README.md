# MouseTrail Themes

*[简体中文](README.zh-Hans.md)*

A public library of gradient trail themes for MouseTrail, the macOS cursor-trail app.
Every theme here is a plain, hand-readable JSON file that
describes a trail's color mode (`rainbow`, `fixed`, or a 2–5 stop `gradient`), lifetime,
and width — nothing else. Browse the gallery, one-click add a theme to the app, or
download the `.json` and import it yourself.

## Using a theme

**1. Gallery "Add to MouseTrail" (recommended)**

Open the gallery site (`docs/index.html`, published via GitHub Pages) and click **Add to
MouseTrail** on any theme card. This opens a `mousetrail://import?url=...` deep link that
hands the theme's raw JSON URL to the app, which downloads it, shows a confirmation
dialog listing the theme name(s), and only imports on your confirmation — nothing is
applied silently.

This requires a version of MouseTrail with gradient-theme support. If you're on an older
version, importing a theme with a `gradient` color mode shows an **"update MouseTrail"**
message instead of failing silently or importing incorrectly — themes with only
`rainbow`/`fixed` color modes still import fine on older versions.

**2. Download + manual import**

Click **Download .json** on a theme card (or grab any file directly from `themes/`),
then in MouseTrail go to **Settings → Trail → Import…** and choose the file. This works
on every MouseTrail version — you'll just see the same "update MouseTrail" message on
gradient themes if your app predates gradient support.

## Collections

| Collection | Path | What it is |
|---|---|---|
| **Designer** (flagship) | `themes/official/designer/` | Curated, sophisticated multi-stop palettes — muted, cohesive color stories rather than raw RGB picks. |
| **Neon** | `themes/official/neon/` | Bright, saturated multi-stop gradients, including the built-in **Aurora** and **Sunset** presets that ship with the app. |
| **Community** | `themes/community/` | Contributed via pull request, reviewed by a maintainer before merge. |

## Hand-authoring a theme

See **[THEME-FORMAT.md](THEME-FORMAT.md)** for the full file format reference — every
field, its valid range, and worked examples (including how to convert a hex color to the
`0`–`1` sRGB values this format uses).

## Contributing

Want to add your own theme to the Community collection? See
**[CONTRIBUTING.md](CONTRIBUTING.md)** for how to author, validate, and submit a theme
via pull request.

## License

Themes and repository content in this project are licensed under
**[CC BY-NC 4.0](LICENSE)** (Attribution–NonCommercial) — free to use and share, not for
commercial use, with attribution. This license covers this repository's themes and
content only; it is independent of the MouseTrail application's own license.
