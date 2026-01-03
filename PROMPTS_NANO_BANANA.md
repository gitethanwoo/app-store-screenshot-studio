# Nano Banana Pro prompt templates for App Store screenshots

Use these templates when generating final marketing composites.
Hard constraints: do not hallucinate UI, and output EXACT pixel dimensions.

## How to invoke the generate_image.py script

The nano-banana-pro skill includes `scripts/generate_image.py`. Invoke it via:

```bash
# Basic generation (new image from prompt)
uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Your prompt here" \
  --filename "./screenshots/final/en-US/iphone_6_9/01_hero.png" \
  --resolution 2K

# Edit existing image (compositing raw screenshot)
uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Your prompt here" \
  --input-image "./screenshots/raw/en-US/iphone_6_9/01_hero.png" \
  --filename "./screenshots/final/en-US/iphone_6_9/01_hero.png" \
  --resolution 2K
```

### Arguments
| Flag | Description |
|------|-------------|
| `--prompt`, `-p` | Required. Text description for generation/editing |
| `--filename`, `-f` | Required. Output file path |
| `--resolution`, `-r` | Optional. `1K`, `2K`, or `4K` (default: 1K) |
| `--input-image`, `-i` | Optional. Path to image to edit (for compositing) |
| `--api-key`, `-k` | Optional. Gemini API key (or set `GEMINI_API_KEY` env var) |

### Resolution mapping for App Store sizes
| Device category | Recommended resolution |
|-----------------|----------------------|
| iphone_6_9 (1290x2796) | `2K` |
| iphone_6_5 (1284x2778) | `2K` |
| ipad_13 (2048x2732) | `2K` or `4K` |

## Global rules to include in every prompt
- Output must be exactly {WIDTH}x{HEIGHT} pixels.
- Use the provided raw screenshot as the only source of in-app UI.
- Do NOT add UI elements, buttons, charts, or features not present in the raw screenshot.
- Keep UI readable and large.
- Keep text inside safe margins (at least ~5% inset from each edge).
- Use a consistent typography + layout system across the full set.
- Do not include prices or references to other platforms.

## Template A — Clean, modern, "Apple-ish"
PROMPT:
Create an App Store marketing screenshot.
Canvas: {WIDTH}x{HEIGHT}px.
Base layer: place the provided raw in-app screenshot prominently (large, crisp, faithful).
Background: subtle gradient or soft solid using {BRAND_COLORS}.
Overlay text:
Headline: "{HEADLINE}"
Subheadline (optional): "{SUBHEADLINE}"
Constraints:
- Keep all text within safe margins, high contrast, large, legible.
- Do not invent UI elements. Do not change the app UI.
- If the feature requires subscription/IAP, include a small but clear disclosure: "Subscription required" (or user-provided wording).
Export as PNG with no transparency.

## Template B — Bold feature callout (still minimal)
PROMPT:
Create an App Store screenshot at {WIDTH}x{HEIGHT}px using the provided raw screenshot.
Use a bold background shape system and 1–2 callout labels pointing to real parts of the UI (no fake elements).
Headline: "{HEADLINE}".
Callout labels (max 2): {CALLOUT_1}, {CALLOUT_2}.
Keep UI dominant; keep callouts clean and non-overlapping.

## Template C — Trust / privacy frame
PROMPT:
Create an App Store screenshot at {WIDTH}x{HEIGHT}px using the provided raw screenshot.
Headline: "{HEADLINE}" (e.g., "Private by design").
Subheadline: "{SUBHEADLINE}" (e.g., "Your data stays on your device.").
Add a simple trust iconography element ONLY if it is generic (no Apple trademarks, no competitor marks).
No prices, no platform references, no unverifiable claims.

## Output naming
Write output to:
`./screenshots/final/<locale>/<device_category>/<index>_<slug>.png`
