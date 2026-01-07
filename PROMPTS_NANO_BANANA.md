# Nano Banana Pro prompt templates for App Store screenshots

Use these templates when generating final marketing composites.
Hard constraints: do not hallucinate UI, and output EXACT pixel dimensions.

## How to invoke the generate_image.py script

The nano-banana-pro skill includes `scripts/generate_image.py`.

**⚠️ MANDATORY: Always use `--input-image` with the raw screenshot. Never generate from prompt alone.**

```bash
# CORRECT: Composite real screenshot with marketing frame
uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --input-image "./screenshots/raw/en-US/iphone_6_9/01_hero.png" \
  --prompt "Your compositing prompt here" \
  --filename "./screenshots/drafts/en-US/iphone_6_9/01_hero.png" \
  --resolution 1K
```

```bash
# ❌ WRONG: Do NOT do this - generates fake mockup, not real app UI
uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "Your prompt here" \
  --filename "./screenshots/final/en-US/iphone_6_9/01_hero.png" \
  --resolution 2K
```

### Arguments
| Flag | Description |
|------|-------------|
| `--prompt`, `-p` | Required. Text description for compositing |
| `--filename`, `-f` | Required. Output file path |
| `--input-image`, `-i` | **REQUIRED for App Store screenshots.** Path to raw screenshot to composite |
| `--resolution`, `-r` | `1K`, `2K`, or `4K` — see workflow below |
| `--api-key`, `-k` | Optional. Gemini API key (or set `GEMINI_API_KEY` env var) |

### Resolution workflow (draft → approval → final)
| Phase | Resolution | Output folder | Purpose |
|-------|------------|---------------|---------|
| Draft | `1K` | `./screenshots/drafts/` | Fast iteration, get user approval |
| Final | `2K` or `4K` | `./screenshots/final/` | After approval only |

| Device category | Final resolution |
|-----------------|------------------|
| iphone_6_9 (1290x2796) | `2K` |
| iphone_6_5 (1284x2778) | `2K` |
| ipad_13 (2048x2732) | `2K` or `4K` |

**Do NOT generate at 2K/4K until drafts are approved.**

## Global rules to include in every prompt
- Output must be exactly {WIDTH}x{HEIGHT} pixels.
- Use the provided raw screenshot as the only source of in-app UI.
- Do NOT add UI elements, buttons, charts, or features not present in the raw screenshot.
- Keep UI readable and large.
- Keep text inside safe margins (at least ~5% inset from each edge).
- Use a consistent typography + layout system across the full set.
- Do not include prices or references to other platforms.

## Template A — Clean, modern, "Apple-ish"

**Remember: You MUST pass the raw screenshot via `--input-image`.**

PROMPT:
```
Create an App Store marketing screenshot.
Canvas: {WIDTH}x{HEIGHT}px.
Base layer: place the provided raw in-app screenshot prominently (large, crisp, faithful). DO NOT alter or recreate the app UI.
Background: subtle gradient or soft solid using {BRAND_COLORS}.
Overlay text:
Headline: "{HEADLINE}"
Subheadline (optional): "{SUBHEADLINE}"
Constraints:
- Keep all text within safe margins, high contrast, large, legible.
- Do not invent UI elements. Do not change the app UI. Use ONLY what is visible in the input image.
- If the feature requires subscription/IAP, include a small but clear disclosure: "Subscription required" (or user-provided wording).
Export as PNG with no transparency.
```

## Template B — Bold feature callout (still minimal)

**Remember: You MUST pass the raw screenshot via `--input-image`.**

PROMPT:
```
Create an App Store screenshot at {WIDTH}x{HEIGHT}px using the provided raw screenshot (passed via --input-image).
Use a bold background shape system and 1–2 callout labels pointing to real parts of the UI (no fake elements).
Headline: "{HEADLINE}".
Callout labels (max 2): {CALLOUT_1}, {CALLOUT_2}.
Keep UI dominant; keep callouts clean and non-overlapping.
DO NOT recreate or alter the app UI - use exactly what is in the input image.
```

## Template C — Trust / privacy frame

**Remember: You MUST pass the raw screenshot via `--input-image`.**

PROMPT:
```
Create an App Store screenshot at {WIDTH}x{HEIGHT}px using the provided raw screenshot (passed via --input-image).
Headline: "{HEADLINE}" (e.g., "Private by design").
Subheadline: "{SUBHEADLINE}" (e.g., "Your data stays on your device.").
Add a simple trust iconography element ONLY if it is generic (no Apple trademarks, no competitor marks).
No prices, no platform references, no unverifiable claims.
DO NOT recreate or alter the app UI - use exactly what is in the input image.
```

## Output naming
- **Drafts (1K):** `./screenshots/drafts/<locale>/<device_category>/<index>_<slug>.png`
- **Finals (2K/4K):** `./screenshots/final/<locale>/<device_category>/<index>_<slug>.png`
