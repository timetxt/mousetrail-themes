# MouseTrail Theme File Format

*[中文版 (Simplified Chinese)](THEME-FORMAT.zh-Hans.md)*

This is a cheatsheet for the `.json` file MouseTrail exports when you export a
trail style, and for hand-writing or editing your own theme files. Import a
theme from **Settings → Trail → Import…**.

## Envelope

A theme file is one JSON object:

```json
{
  "version": 1,
  "appVersion": "1.1",
  "createdAt": "2026-07-20T12:00:00Z",
  "themes": [
    {
      "name": "my-color",
      "style": {
        "colorMode": { "fixed": { "red": 0.35, "green": 0.55, "blue": 0.28, "alpha": 1 } },
        "lifetime": 0.6,
        "widthScale": 1
      }
    }
  ]
}
```

| Field | Required | Notes |
|---|---|---|
| `version` | Yes | `1` if every theme uses `rainbow` or `fixed` color. `2` if any theme uses `gradient`. A file with a `version` newer than MouseTrail understands is refused with *"This theme file was made by a newer version of MouseTrail. Update MouseTrail to import it."* — nothing is half-imported. |
| `themes` | Yes | Array of theme objects (below). Can hold one theme or many. |
| `appVersion` | No | Informational — the app version that exported the file. Safe to omit or leave out of a hand-written file. |
| `createdAt` | No | Informational — ISO 8601 timestamp. Safe to omit. |

Any field not listed here is ignored on import, so it's safe to add your own
notes as extra top-level or per-theme keys — MouseTrail just skips what it
doesn't recognize.

## Themes

Each entry in `themes` is:

```json
{
  "name": "my-color",
  "style": { "...": "see below" }
}
```

- **`name`** — must be unique within your MouseTrail preset list. If you
  import a theme whose name matches one you already have, MouseTrail keeps
  both: the incoming one is renamed `"Name 2"` (then `"Name 3"`, …) rather
  than overwriting your existing preset.
- **`style`** — the trail's appearance: `colorMode`, `lifetime`, and
  `widthScale`, covered next.

## Color modes

`style.colorMode` is one of three shapes. Exactly one key (`rainbow`,
`fixed`, or `gradient`) should be present — if MouseTrail doesn't recognize
the shape (unknown key, missing key, or a `gradient` with no usable stops),
it falls back to `rainbow` rather than rejecting the file.

### `rainbow` — hue cycles as you move the mouse

```json
{ "colorMode": { "rainbow": {} } }
```

No fields. This is the classic MouseTrail look.

### `fixed` — a single solid color

```json
{ "colorMode": { "fixed": { "red": 0.0, "green": 0.47, "blue": 0.75, "alpha": 1.0 } } }
```

| Field | Range | Meaning |
|---|---|---|
| `red`, `green`, `blue` | `0`–`1` | sRGB color components. |
| `alpha` | `0`–`1` | Opacity — `1` is fully opaque, lower values make the trail more translucent. |

### `gradient` — the trail blends across 2–5 color stops

```json
{
  "colorMode": {
    "gradient": {
      "stops": [
        { "red": 0.4824, "green": 0.3804, "blue": 1.0000, "alpha": 1, "location": 0 },
        { "red": 0.0000, "green": 0.8510, "blue": 1.0000, "alpha": 1, "location": 0.3333 },
        { "red": 0.0000, "green": 0.9608, "blue": 0.6275, "alpha": 1, "location": 0.6667 },
        { "red": 0.6588, "green": 1.0000, "blue": 0.4706, "alpha": 1, "location": 1 }
      ]
    }
  }
}
```

That's MouseTrail's built-in **Aurora** preset, written out in full — see
"Worked example" below for where those numbers come from.

Each stop:

| Field | Range | Meaning |
|---|---|---|
| `red`, `green`, `blue`, `alpha` | `0`–`1` | Same as `fixed`, above. |
| `location` | `0`–`1` | Position along the trail: `0` is the **tail** (oldest, fading-out end), `1` is the **head** (newest, at the cursor). |

Rules for `stops`:

- **2 to 5 stops.** Fewer than 2 or more than 5 isn't rejected — MouseTrail
  normalizes what it's given (a single stop becomes a flat two-stop "gradient"
  of one color; more than 5 stops keeps only the first five) — but write 2–5
  to get the gradient you actually intend.
- Stops are sorted by `location` on import, so you don't have to list them
  in order, but writing them tail-to-head (ascending `location`) is easiest
  to read and edit.
- Out-of-range component or `location` values are clamped into `0`–`1`, not
  rejected.

## Color values: hex to 0–1

MouseTrail stores color components as sRGB doubles from `0` to `1`, not hex.
To convert a hex color `#RRGGBB`, divide each byte by 255:

```
component = hexByte / 255
```

| Hex byte | Decimal | Component |
|---|---|---|
| `#00` | 0 | `0.0000` |
| `#33` | 51 | `0.2000` |
| `#40` | 64 | `0.2510` |
| `#7F` | 127 | `0.4980` |
| `#80` | 128 | `0.5020` |
| `#B3` | 179 | `0.7020` |
| `#CC` | 204 | `0.8000` |
| `#FF` | 255 | `1.0000` |

Worked example: `#7B61FF` → red `0x7B` (123) → `123 / 255 ≈ 0.4824`, green
`0x61` (97) → `97 / 255 ≈ 0.3804`, blue `0xFF` (255) → `255 / 255 = 1.0000`.

## Worked example: Aurora's gradient

MouseTrail's built-in **Aurora** preset uses these four colors, evenly
spaced across the trail (`location` values `0`, `1/3`, `2/3`, `1`):

| Hex | location | red | green | blue |
|---|---|---|---|---|
| `#7B61FF` | `0` | `0.4824` | `0.3804` | `1.0000` |
| `#00D9FF` | `0.3333` | `0.0000` | `0.8510` | `1.0000` |
| `#00F5A0` | `0.6667` | `0.0000` | `0.9608` | `0.6275` |
| `#A8FF78` | `1` | `0.6588` | `1.0000` | `0.4706` |

As a full theme file (this needs `"version": 2` because it contains a
gradient):

```json
{
  "version": 2,
  "themes": [
    {
      "name": "My Aurora Remix",
      "style": {
        "colorMode": {
          "gradient": {
            "stops": [
              { "red": 0.4824, "green": 0.3804, "blue": 1.0000, "alpha": 1, "location": 0 },
              { "red": 0.0000, "green": 0.8510, "blue": 1.0000, "alpha": 1, "location": 0.3333 },
              { "red": 0.0000, "green": 0.9608, "blue": 0.6275, "alpha": 1, "location": 0.6667 },
              { "red": 0.6588, "green": 1.0000, "blue": 0.4706, "alpha": 1, "location": 1 }
            ]
          }
        },
        "lifetime": 0.6,
        "widthScale": 1
      }
    }
  ]
}
```

## Lifetime and width

Alongside `colorMode`, each theme's `style` has two numbers:

| Field | Range | Meaning |
|---|---|---|
| `lifetime` | `0.3`–`1.5` (seconds) | How long a point on the trail stays visible before fading out. Higher = a longer, more persistent trail. |
| `widthScale` | `0.5`–`2.0` | Multiplies MouseTrail's 7pt base stroke width. `1` is the default width; `2` is twice as wide, `0.5` is half as wide. |

Values outside these ranges are **clamped to the nearest valid value, never
rejected** — a `lifetime` of `5` in a hand-edited file imports as `1.5`, not
as an error.

## Tips

- **Evenly spaced gradient stops:** for *N* stops, use `location` values
  `0, 1/(N-1), 2/(N-1), …, 1`. For 4 stops (like Aurora) that's `0, 0.3333,
  0.6667, 1`.
- **Translucent trails:** lower `alpha` (e.g. `0.5`) on a `fixed` color or on
  individual gradient stops for a softer, more transparent trail. Different
  stops can have different `alpha` values, so a gradient can fade in opacity
  as well as color.
- **Importing:**
  - **Settings → Trail → Import…** and choose a `.json` theme file (or a
    legacy `.mousetrailpack` — those still import too).
  - `mousetrail://` links from this theme library's gallery trigger the same
    import flow automatically — MouseTrail downloads and confirms the theme
    before adding it.
  - Importing never overwrites an existing preset with the same name — a
    name collision gets renamed (`"Name 2"`, etc.) instead.
