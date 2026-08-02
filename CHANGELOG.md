# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **43 themes** drawn from a batch of colour references, taking the library from 15 to 58.
  - *Dopamine cards* (neon) — **Crimson Pop**, **Candy Pop**, **Tangerine Rush**,
    **Honey Glow**, **Lime Surge**, **Aqua Surge**, **Azure Rush**, **Periwinkle Drift**,
    **Ultraviolet Bloom**: saturated four-stop ramps, one per hue family.
  - *Two-tone gradients* (designer) — **Sapphire Sprout**, **Rose Gold**, **Pine Ivory**,
    **Kingfisher**, **Ash Lilac**: a single dark-to-bright sweep between two named colours.
  - *Three-colour palettes* — **Citrus Sea** (neon), plus **Misty Blush**, **Pine Glade**,
    **Cloud Indigo**, **Caramel Latte** (designer).
  - *Soft pastels* (designer) — **Wisteria Veil**, **Meadow Tide**, **Sky Wash**,
    **Sage Whisper**, **Rose Powder**, **Frost Blue**, **Apricot Silk**, **Spring Dew**,
    **Harbor Mist**, **Olive Grove**, **Clay Rose**, **Denim Fade**, **Mandarin Linen**,
    **Spring Day**.
  - *Dark-ground neons* — **Neon Orchid**, **Electric Tide**, **Amber Forge**,
    **Neon Iris**, **Verdant Pulse**, **Firecracker**, **Emerald Lagoon**,
    **Prism Drift**, **Jade Current**, **Voltage**: a near-black tail rising into one or
    two bright accents.
- **Paginated gallery** — the card grid now shows 12 themes per page with numbered page
  controls, so 58 themes no longer render as a single six-thousand-pixel scroll.
  Collection filters reset to the first page, and the page-number window slides around
  the current page so the control keeps a stable width.

## [1.1.0] - 2026-07-24

### Added

- **Reverie** (designer collection) — a soft, dreamy pastel gradient sweeping from
  orchid through lilac and periwinkle to an airy pale cyan. The library is now 15 themes.
- **Live trail experience in the gallery** — click any color board to draw that theme
  as a real fading cursor trail, tune its length (0.3–1.5s) and width (0.5–2.0×), and
  switch themes on the fly. A "Now drawing" indicator names the active theme.
- **Light / dark appearance toggle** in the gallery, beside the existing EN / 简体中文 toggle,
  defaulting to light and remembering your choice.
- App Store and GitHub repository links in the gallery header and both READMEs, so the
  gallery links out to the app and its source.

## [1.0.0] - 2026-07-20

### Added

- Initial release of the MouseTrail theme library: 14 official themes across two
  collections.
- **Designer collection** (`themes/official/designer/`): Cream, Cyberpunk, Matcha,
  Morandi, Peach, Sakura, Tiffany.
- **Neon collection** (`themes/official/neon/`): Aurora, Dream Purple, Forest, Galaxy,
  Mint Breeze, Ocean, Sunset.
- JSON Schema (`schema/theme.schema.json`) and a pure-stdlib validator
  (`scripts/validate_themes.py`) as the local + CI validation entry point.
- GitHub Pages gallery (`docs/`) with EN / 简体中文 language toggle, collection filters,
  and per-theme "Add to MouseTrail" deep link and "Download .json" actions.
- `THEME-FORMAT.md` / `THEME-FORMAT.zh-Hans.md` hand-authoring reference.
- `CONTRIBUTING.md` / `CONTRIBUTING.zh-Hans.md`, a pull request template, and a
  validate-themes CI workflow for community contributions.
- CC BY-NC 4.0 license covering the repository's themes and content.
