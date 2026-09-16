# madrileno brand pack

## Colors
| Role | Light | Dark |
|---|---|---|
| Ink (m, text) | `#1E1E24` | `#F5F1EA` |
| Accent (tilde) | `#B5122B` | `#E0304A` |
| Background | `#F5F1EA` / transparent | `#1E1E24` / transparent |

Crimson `#B5122B` is the Comunidad de Madrid flag red. The dark variant is lifted to `#E0304A` so it holds contrast on charcoal.

## Files
- `mark*.svg` — symbol only (lowercase m + tilde), 100×100. Use when the wordmark won't fit.
- `logo*.svg` — horizontal mark + wordmark, transparent background.
- `logo-stacked*.svg` — centered mark above wordmark, for the README hero.
- `wordmark*.svg` — text only; the ñ tilde carries the crimson accent since there's no mark to do it.
- `icon*.svg` — 512×512 rounded tile for the GitHub repo/org avatar (`icon-crimson.svg` is the loud option).
- `favicon.svg` — follows the OS light/dark preference automatically.
- `*-mono.svg` — use `currentColor`; inherits text color wherever it's inlined.

## Usage from other repos (auto light/dark)
The template repos stay brand-free on purpose: `init-project` renames them for downstream users, so a baked-in logo would follow every fork. Reference the assets by raw URL from here instead:
```html
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/madrileno-dev/.github/main/brand/logo-stacked-dark.svg">
    <img alt="madrileño" src="https://raw.githubusercontent.com/madrileno-dev/.github/main/brand/logo-stacked.svg" width="240">
  </picture>
</p>
```

## Rules
- Clear space around the mark: at least the width of one m stem.
- Never recolor the tilde and the m to the same accent except in the mono versions.
- Minimum size for the mark: 16px. Below that, use the tilde alone.
- Wordmark: Manrope SemiBold (600), SIL OFL, outlined to paths — no font dependency. Use Manrope for any headline text next to the logo; body text can be anything.
