# Contributing a theme

*[简体中文](CONTRIBUTING.zh-Hans.md)*

Thanks for considering a contribution to the Community collection. This is a short,
mechanical process: write a theme file, validate it locally, open a pull request.

## 1. Write your theme file

Add a new file at `themes/community/<github-username>/<kebab-case-name>.json` —
a folder named after your GitHub username, e.g.
`themes/community/octocat/midnight-teal.json`. Use a name that's descriptive and doesn't collide
with an existing theme (theme *names* — the `name` field inside the file — must be
unique across the whole repo, not just your file).

Follow **[THEME-FORMAT.md](THEME-FORMAT.md)** for the exact JSON shape: the envelope
(`version`, `themes`), each theme's `name` and `style`, and the three `colorMode` shapes
(`rainbow`, `fixed`, `gradient`). A `gradient` theme needs 2–5 stops and `version: 2`;
a `rainbow`/`fixed`-only file uses `version: 1`.

A minimal example:

```json
{
  "version": 2,
  "themes": [
    {
      "name": "Midnight Teal",
      "style": {
        "colorMode": {
          "gradient": {
            "stops": [
              { "red": 0.02, "green": 0.11, "blue": 0.16, "alpha": 1, "location": 0 },
              { "red": 0.04, "green": 0.36, "blue": 0.42, "alpha": 1, "location": 0.5 },
              { "red": 0.30, "green": 0.80, "blue": 0.76, "alpha": 1, "location": 1 }
            ]
          }
        },
        "lifetime": 0.6,
        "widthScale": 1.0
      }
    }
  ]
}
```

## 2. Validate locally

Run the repo's pure-stdlib validator before opening a PR — no dependencies to install:

```
python3 scripts/validate_themes.py
```

This checks JSON validity, required fields, value ranges, stop counts, the
`version`/content consistency rule, and theme-name uniqueness across the repo. Fix
anything it reports; it exits non-zero (with every violation listed) if something's
wrong.

## 3. Generate its swatch

Run the repo's pure-stdlib swatch generator so your theme gets a preview image in the
README tables:

```
python3 scripts/build_swatches.py
```

This (re)writes `assets/swatches/<github-username>-<your-file-stem>.svg` and prunes any orphaned swatch
files. Commit the generated SVG along with your theme file — CI fails the build if the
generated assets are out of date (see the `validate-themes` workflow).

## 4. Open a pull request

Open a PR against this repo with your new file under `themes/community/<github-username>/`
and its generated `assets/swatches/<github-username>-<stem>.svg`. The `validate-themes` GitHub Actions workflow
runs the same validator plus a JSON Schema check automatically on your PR — it's a
**helper only**: it does not merge anything, and a green check does not guarantee
acceptance. **Merging is by maintainer review.**

The PR template has a short checklist — fill it out; it mirrors the steps above.

## License

By submitting a theme, you agree to license your contribution under the same
**[CC BY-NC 4.0](LICENSE)** terms that cover the rest of this repository's content.
