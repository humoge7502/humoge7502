# K/OS Operator Console — asset generator

Every SVG in `../assets/` is **generated**, never hand-edited. Regeneration is
one command and always produces the same output (deterministic, diff-friendly).

## Requirements

- Python 3.9+
- `pip install pillow cairosvg` (cairosvg only needed for `make_og.py`)

## Commands

```bash
# regenerate all assets with the monogram slot (no photo published yet)
python3 scripts/build_assets.py

# regenerate with your portrait baked into the hero (both theme variants)
python3 scripts/build_assets.py --photo photo.jpg

# render the 1280x640 social preview (assets/og-profile.png)
python3 scripts/make_og.py
```

## Photo rules (read before baking)

- Any square-ish photo works — it is center-cropped automatically.
- A neutral background, face lit from the front, reads best at 124 px.
- The photo is **embedded as base64 inside the SVG** — no external requests,
  renders everywhere (GitHub, LinkedIn scrapers, dark and light theme).
- Re-run the command any time you change the photo; commit both
  `hero-console.svg` and `hero-console-light.svg`.

## Files

| File | Purpose |
| :--- | :--- |
| `svg_lib.py` | design tokens (palette, typography), HUD primitives, section strips, mission cards, achievements strip |
| `build_assets.py` | hero console (dark + light) and the full build entrypoint |
| `make_og.py` | 1280x640 social preview composite |

## Design tokens (change here, regenerate, commit)

| Token | Dark value | Meaning |
| :--- | :--- | :--- |
| `bg` | `#0A0E14` | console chassis |
| `green` | `#4ADE80` | mission-passed / money / primary accent |
| `cyan` | `#22D3EE` | telemetry / callsign |
| `amber` | `#FBBF24` | open XP segment, releases |
| `violet` | `#A78BFA` | Q-Trust brand |
| `red` | `#F87171` | threat level only |

Animations are **SMIL only** (`<animate>`) — the one animation technology that
reliably runs inside SVGs rendered as `<img>` on GitHub. No scripts, no CSS
keyframes, no external fonts: the assets are self-contained by construction.
