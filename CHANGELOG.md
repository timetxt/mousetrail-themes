# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
