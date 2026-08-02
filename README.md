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

> 🐍 **New in the app:** MouseTrail now has a **Snake Game** — turn your trail into
> a snake, steer it with your mouse, and chase your all-time high score. Free, in
> [the latest version](https://apps.apple.com/au/app/mousetrail/id6787651654?mt=12).

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
| ![Apricot Silk trail swatch](assets/swatches/apricot-silk.svg) | Apricot Silk | `#F2B382` → `#F8D0B0` → `#FBE3D2` → `#FFF8DD` |
| ![Ash Lilac trail swatch](assets/swatches/ash-lilac.svg) | Ash Lilac | `#363636` → `#B0A4E3` |
| ![Caramel Latte trail swatch](assets/swatches/caramel-latte.svg) | Caramel Latte | `#8D6E63` → `#D7CCC8` → `#F5F5F5` |
| ![Clay Rose trail swatch](assets/swatches/clay-rose.svg) | Clay Rose | `#C27B7B` → `#EEAAAA` → `#F6D6D6` → `#FDEEEE` |
| ![Cloud Indigo trail swatch](assets/swatches/cloud-indigo.svg) | Cloud Indigo | `#3949AB` → `#7986CB` → `#ECEFF1` |
| ![Cream trail swatch](assets/swatches/cream.svg) | Cream | `#C9A876` → `#E0C79A` → `#EFDDBB` → `#F7EEDA` |
| ![Cyberpunk trail swatch](assets/swatches/cyberpunk.svg) | Cyberpunk | `#2A1A4D` → `#7B2F87` → `#C24A93` → `#7B6DC4` → `#3CC0CE` |
| ![Denim Fade trail swatch](assets/swatches/denim-fade.svg) | Denim Fade | `#5B8FBE` → `#86A5C4` → `#C1D7EF` → `#E0EDF8` |
| ![Frost Blue trail swatch](assets/swatches/frost-blue.svg) | Frost Blue | `#8CC6ED` → `#C0E0F8` → `#D0E8FF` → `#EDF7FF` |
| ![Harbor Mist trail swatch](assets/swatches/harbor-mist.svg) | Harbor Mist | `#5A97D0` → `#79B0D7` → `#A0C8E8` → `#C6E0F2` |
| ![Kingfisher trail swatch](assets/swatches/kingfisher.svg) | Kingfisher | `#0095D9` → `#F6CB1D` |
| ![Mandarin Linen trail swatch](assets/swatches/mandarin-linen.svg) | Mandarin Linen | `#6B7BB4` → `#89A411` → `#F58E3C` → `#FDEBD3` |
| ![Matcha trail swatch](assets/swatches/matcha.svg) | Matcha | `#6B7A3A` → `#8A9A54` → `#A8B778` → `#CBD3A6` → `#EDE9D2` |
| ![Meadow Tide trail swatch](assets/swatches/meadow-tide.svg) | Meadow Tide | `#90BFCF` → `#AFD1BF` → `#CFE5BB` → `#E0EEB8` |
| ![Misty Blush trail swatch](assets/swatches/misty-blush.svg) | Misty Blush | `#FF6F61` → `#F8BBD0` → `#FFF8E1` |
| ![Morandi trail swatch](assets/swatches/morandi.svg) | Morandi | `#7E8A82` → `#94918E` → `#A99E9A` → `#B3A8AE` → `#C7C4BE` |
| ![Olive Grove trail swatch](assets/swatches/olive-grove.svg) | Olive Grove | `#8CB26C` → `#AAC576` → `#D7E9BC` → `#EEF5E9` |
| ![Peach trail swatch](assets/swatches/peach.svg) | Peach | `#E68A5E` → `#F4B98E` → `#FBDDC2` |
| ![Pine Glade trail swatch](assets/swatches/pine-glade.svg) | Pine Glade | `#4CAF50` → `#81C784` → `#E8F5E9` |
| ![Pine Ivory trail swatch](assets/swatches/pine-ivory.svg) | Pine Ivory | `#0A3D2E` → `#FFD9D1` |
| ![Reverie trail swatch](assets/swatches/reverie.svg) | Reverie | `#B883D3` → `#C4A5DE` → `#A1A9D0` → `#96CCCB` → `#CFEAF1` |
| ![Rose Gold trail swatch](assets/swatches/rose-gold.svg) | Rose Gold | `#FF4777` → `#FBDC92` |
| ![Rose Powder trail swatch](assets/swatches/rose-powder.svg) | Rose Powder | `#F0A0A0` → `#F8C8C8` → `#FBE6E6` → `#FFF5F5` |
| ![Sage Whisper trail swatch](assets/swatches/sage-whisper.svg) | Sage Whisper | `#C2E2C2` → `#CDE5CD` → `#DCE9DC` → `#E8EEDC` |
| ![Sakura trail swatch](assets/swatches/sakura.svg) | Sakura | `#E39BB4` → `#F2B8CE` → `#F9D3E1` → `#FCEDF2` |
| ![Sapphire Sprout trail swatch](assets/swatches/sapphire-sprout.svg) | Sapphire Sprout | `#053154` → `#BCE672` |
| ![Sky Wash trail swatch](assets/swatches/sky-wash.svg) | Sky Wash | `#7EBCF5` → `#98C9F1` → `#B4DCEC` → `#D0ECE9` |
| ![Spring Day trail swatch](assets/swatches/spring-day.svg) | Spring Day | `#FFAAA5` → `#FFD3B6` → `#DCEDC1` → `#A8E6CF` |
| ![Spring Dew trail swatch](assets/swatches/spring-dew.svg) | Spring Dew | `#B2D990` → `#B9DDCF` → `#C1E9E9` → `#E5F1E5` |
| ![Tiffany trail swatch](assets/swatches/tiffany.svg) | Tiffany | `#2E9A94` → `#57BDB5` → `#86D4CD` → `#C0E8E0` → `#EDE6D6` |
| ![Wisteria Veil trail swatch](assets/swatches/wisteria-veil.svg) | Wisteria Veil | `#897CD3` → `#9898DC` → `#B8BBE7` → `#D8DEF7` |

### Neon

Bright, saturated multi-stop gradients in `themes/official/neon/`, including the built-in
**Aurora** and **Sunset** presets that ship with the app.

| Swatch | Name | Colors |
|---|---|---|
| ![Amber Forge trail swatch](assets/swatches/amber-forge.svg) | Amber Forge | `#252712` → `#875712` → `#FCDB56` |
| ![Aqua Surge trail swatch](assets/swatches/aqua-surge.svg) | Aqua Surge | `#06A4C0` → `#01CFD2` → `#19F0D7` → `#9FFFEC` |
| ![Aurora trail swatch](assets/swatches/aurora.svg) | Aurora | `#7B61FF` → `#00D9FF` → `#00F5A0` → `#A8FF78` |
| ![Azure Rush trail swatch](assets/swatches/azure-rush.svg) | Azure Rush | `#0349D5` → `#3673F0` → `#39BEF9` → `#A8E6FF` |
| ![Candy Pop trail swatch](assets/swatches/candy-pop.svg) | Candy Pop | `#FF10AB` → `#FF4FC4` → `#FF84EA` → `#FFC0F5` |
| ![Citrus Sea trail swatch](assets/swatches/citrus-sea.svg) | Citrus Sea | `#48C6F0` → `#FFF0D6` → `#FF8A3D` |
| ![Crimson Pop trail swatch](assets/swatches/crimson-pop.svg) | Crimson Pop | `#D3071C` → `#F74020` → `#FF7375` → `#FFAEAF` |
| ![Dream Purple trail swatch](assets/swatches/dream-purple.svg) | Dream Purple | `#9D7CFF` → `#D291FF` → `#FFB3F7` → `#A8FFF5` |
| ![Electric Tide trail swatch](assets/swatches/electric-tide.svg) | Electric Tide | `#170E29` → `#007EFC` → `#6FE3FC` |
| ![Emerald Lagoon trail swatch](assets/swatches/emerald-lagoon.svg) | Emerald Lagoon | `#1A8B41` → `#38BCBD` → `#4EC94C` |
| ![Firecracker trail swatch](assets/swatches/firecracker.svg) | Firecracker | `#1B1512` → `#F90027` → `#2FDDCC` |
| ![Forest trail swatch](assets/swatches/forest.svg) | Forest | `#1B5E20` → `#4CAF50` → `#8BC34A` → `#CDDC39` → `#FFC107` |
| ![Galaxy trail swatch](assets/swatches/galaxy.svg) | Galaxy | `#2563EB` → `#8B5CF6` → `#EC4899` → `#F97316` → `#FDE047` |
| ![Honey Glow trail swatch](assets/swatches/honey-glow.svg) | Honey Glow | `#FFB209` → `#FFCC42` → `#FFDA77` → `#FDECBC` |
| ![Jade Current trail swatch](assets/swatches/jade-current.svg) | Jade Current | `#087471` → `#1CA041` → `#5BD8BE` |
| ![Lime Surge trail swatch](assets/swatches/lime-surge.svg) | Lime Surge | `#06B606` → `#4CD201` → `#9BF019` → `#CEFF83` |
| ![Mint Breeze trail swatch](assets/swatches/mint-breeze.svg) | Mint Breeze | `#A7F3D0` → `#6EE7B7` → `#38BDF8` → `#E0F2FE` |
| ![Neon Iris trail swatch](assets/swatches/neon-iris.svg) | Neon Iris | `#09212C` → `#00D6DE` → `#DFB6FD` |
| ![Neon Orchid trail swatch](assets/swatches/neon-orchid.svg) | Neon Orchid | `#0D0933` → `#581B72` → `#FE00BE` |
| ![Ocean trail swatch](assets/swatches/ocean.svg) | Ocean | `#0187FF` → `#00C2FF` → `#00E9D2` → `#E0FFFA` |
| ![Periwinkle Drift trail swatch](assets/swatches/periwinkle-drift.svg) | Periwinkle Drift | `#4141BF` → `#7F8EF3` → `#9EABFF` → `#CFD7FE` |
| ![Prism Drift trail swatch](assets/swatches/prism-drift.svg) | Prism Drift | `#8E44AD` → `#4285F4` → `#1ABC9C` → `#7ACC26` |
| ![Sunset trail swatch](assets/swatches/sunset.svg) | Sunset | `#FF6B6B` → `#FFA26B` → `#FFD06B` → `#FFF7A8` |
| ![Tangerine Rush trail swatch](assets/swatches/tangerine-rush.svg) | Tangerine Rush | `#FF5100` → `#FE861D` → `#FFAD66` → `#FFCC92` |
| ![Ultraviolet Bloom trail swatch](assets/swatches/ultraviolet-bloom.svg) | Ultraviolet Bloom | `#5F03A8` → `#A25CFF` → `#C99AFF` → `#E0BAFF` |
| ![Verdant Pulse trail swatch](assets/swatches/verdant-pulse.svg) | Verdant Pulse | `#152C14` → `#00313F` → `#AFFDAB` |
| ![Voltage trail swatch](assets/swatches/voltage.svg) | Voltage | `#3C3C3C` → `#8000FF` → `#FF0080` → `#FFDE00` |

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
