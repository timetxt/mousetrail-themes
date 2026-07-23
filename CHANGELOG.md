# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
