# MouseTrail Themes

<div align="center">
  <img src="assets/swatches/aurora.svg" alt="MouseTrail trail theme" width="520">
</div>

<p align="center">
  <strong>Beautiful cursor trails, one click away.</strong>
</p>

<p align="center">
  A public library of gradient trail themes for MouseTrail, the macOS
  cursor-trail app — each a plain, hand-readable JSON file describing a trail's
  color mode (<code>rainbow</code>, <code>fixed</code>, or a 2–5 stop
  <code>gradient</code>), lifetime, and width. Browse the gallery, one-click add
  a theme to the app, or download the <code>.json</code> and import it yourself.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-macOS-475A60.svg" alt="Platform: macOS">
  <img src="https://img.shields.io/badge/format-plain%20JSON-216C83.svg" alt="Format: plain JSON">
  <a href="https://apps.apple.com/au/app/mousetrail/id6787651654?mt=12"><img src="https://img.shields.io/badge/App%20Store-MouseTrail-0D96F6.svg" alt="Get MouseTrail on the App Store"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY--NC%204.0-C8553D.svg" alt="License: CC BY-NC 4.0"></a>
  <a href="https://discord.com/channels/1529997922643476652/1529997923201585244"><img src="https://img.shields.io/badge/discord-community-5865F2.svg" alt="Discord community"></a>
</p>

<p align="center">
  <a href="https://timetxt.github.io/mousetrail-themes/">Gallery</a> ·
  <a href="#using-a-theme">Using a Theme</a> ·
  <a href="#collections">Collections</a> ·
  <a href="THEME-FORMAT.md">Theme Format</a> ·
  <a href="CONTRIBUTING.md">Contributing</a> ·
  <a href="README.zh-Hans.md">简体中文</a>
</p>

**[Browse and try every theme live in the gallery](https://timetxt.github.io/mousetrail-themes/)** —
click any color board and move your pointer to feel that theme drawn as a real cursor
trail, adjust its length and width, then **Add to MouseTrail** in one click or
**[get the app on the App Store](https://apps.apple.com/au/app/mousetrail/id6787651654?mt=12)**.

## Using a theme

**1. Gallery "Add to MouseTrail" (recommended)**

Open the [gallery site](https://timetxt.github.io/mousetrail-themes/) (`docs/index.html`,
published via GitHub Pages) and click **Add to MouseTrail** on any theme card. This opens a `mousetrail://import?url=...` deep link that
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

### Designer (flagship)

Curated, sophisticated multi-stop palettes in `themes/official/designer/` — muted,
cohesive color stories rather than raw RGB picks.

| Swatch | Name | Colors |
|---|---|---|
| ![Cream trail swatch](assets/swatches/cream.svg) | Cream | `#C9A876` → `#E0C79A` → `#EFDDBB` → `#F7EEDA` |
| ![Cyberpunk trail swatch](assets/swatches/cyberpunk.svg) | Cyberpunk | `#2A1A4D` → `#7B2F87` → `#C24A93` → `#7B6DC4` → `#3CC0CE` |
| ![Matcha trail swatch](assets/swatches/matcha.svg) | Matcha | `#6B7A3A` → `#8A9A54` → `#A8B778` → `#CBD3A6` → `#EDE9D2` |
| ![Morandi trail swatch](assets/swatches/morandi.svg) | Morandi | `#7E8A82` → `#94918E` → `#A99E9A` → `#B3A8AE` → `#C7C4BE` |
| ![Peach trail swatch](assets/swatches/peach.svg) | Peach | `#E68A5E` → `#F4B98E` → `#FBDDC2` |
| ![Reverie trail swatch](assets/swatches/reverie.svg) | Reverie | `#B883D3` → `#C4A5DE` → `#A1A9D0` → `#96CCCB` → `#CFEAF1` |
| ![Sakura trail swatch](assets/swatches/sakura.svg) | Sakura | `#E39BB4` → `#F2B8CE` → `#F9D3E1` → `#FCEDF2` |
| ![Tiffany trail swatch](assets/swatches/tiffany.svg) | Tiffany | `#2E9A94` → `#57BDB5` → `#86D4CD` → `#C0E8E0` → `#EDE6D6` |

### Neon

Bright, saturated multi-stop gradients in `themes/official/neon/`, including the built-in
**Aurora** and **Sunset** presets that ship with the app.

| Swatch | Name | Colors |
|---|---|---|
| ![Aurora trail swatch](assets/swatches/aurora.svg) | Aurora | `#7B61FF` → `#00D9FF` → `#00F5A0` → `#A8FF78` |
| ![Dream Purple trail swatch](assets/swatches/dream-purple.svg) | Dream Purple | `#9D7CFF` → `#D291FF` → `#FFB3F7` → `#A8FFF5` |
| ![Forest trail swatch](assets/swatches/forest.svg) | Forest | `#1B5E20` → `#4CAF50` → `#8BC34A` → `#CDDC39` → `#FFC107` |
| ![Galaxy trail swatch](assets/swatches/galaxy.svg) | Galaxy | `#2563EB` → `#8B5CF6` → `#EC4899` → `#F97316` → `#FDE047` |
| ![Mint Breeze trail swatch](assets/swatches/mint-breeze.svg) | Mint Breeze | `#A7F3D0` → `#6EE7B7` → `#38BDF8` → `#E0F2FE` |
| ![Ocean trail swatch](assets/swatches/ocean.svg) | Ocean | `#0187FF` → `#00C2FF` → `#00E9D2` → `#E0FFFA` |
| ![Sunset trail swatch](assets/swatches/sunset.svg) | Sunset | `#FF6B6B` → `#FFA26B` → `#FFD06B` → `#FFF7A8` |

### Community

Contributed via pull request in `themes/community/`, reviewed by a maintainer before
merge. Previews for community themes appear in the gallery (`docs/index.html`) rather
than here.

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
