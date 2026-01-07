# Step 3: Generate Marketing Composites

Detailed guidance for creating App Store marketing screenshots with Nano Banana Pro.

**You should only be reading this after completing Step 2 (Capture Raw Screenshots).**

---

## How to Invoke

```bash
uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --input-image "./screenshots/raw/en-US/iphone_6_9/01_hero.png" \
  --prompt "Your compositing prompt" \
  --filename "./screenshots/drafts/en-US/iphone_6_9/01_hero.png" \
  --resolution 1K
```

### Arguments

| Flag | Required | Description |
|------|----------|-------------|
| `--input-image`, `-i` | **YES** | Path to raw screenshot (NEVER omit this) |
| `--prompt`, `-p` | YES | Compositing instructions |
| `--filename`, `-f` | YES | Output file path |
| `--resolution`, `-r` | YES | `1K` for drafts, `2K`/`4K` for finals |
| `--api-key`, `-k` | No | Gemini API key (or use `GEMINI_API_KEY` env var) |

---

## Resolution Workflow

| Phase | Resolution | Output Folder | When |
|-------|------------|---------------|------|
| **Draft** | `1K` | `./screenshots/drafts/` | Step 3 — for approval |
| **Final** | `2K` or `4K` | `./screenshots/final/` | Step 4 — after approval |

| Device Category | Final Resolution |
|-----------------|------------------|
| iphone_6_9 | `2K` |
| iphone_6_5 | `2K` |
| ipad_13 | `4K` |

**Never generate 2K/4K until drafts are approved.**

---

## Prompt Templates

### Template A: Clean & Modern (Apple-style)

```
Create an App Store marketing screenshot.
Canvas: {WIDTH}x{HEIGHT}px.

Base layer: Place the provided raw screenshot prominently — large, crisp, faithful.
DO NOT alter, recreate, or add to the app UI.

Background: Subtle gradient or soft solid using {BRAND_COLORS}.

Overlay text:
- Headline: "{HEADLINE}"
- Subheadline: "{SUBHEADLINE}"

Constraints:
- Keep text within safe margins (5% inset from edges)
- High contrast, large, legible text
- Do not invent UI elements
- {IAP_DISCLOSURE if needed: "Subscription required"}

Export as PNG, no transparency.
```

### Template B: Feature Callout

```
Create an App Store screenshot at {WIDTH}x{HEIGHT}px.

Use the provided raw screenshot as the base — DO NOT recreate the app UI.

Add:
- Bold background shape/color system
- Headline: "{HEADLINE}"
- 1-2 callout labels pointing to REAL parts of the UI: {CALLOUT_1}, {CALLOUT_2}

Keep the app UI dominant. Callouts should be clean, non-overlapping.
Do not add fake UI elements.
```

### Template C: Trust / Privacy

```
Create an App Store screenshot at {WIDTH}x{HEIGHT}px.

Use the provided raw screenshot as the base — DO NOT recreate the app UI.

- Headline: "{HEADLINE}" (e.g., "Private by design")
- Subheadline: "{SUBHEADLINE}" (e.g., "Your data stays on your device")

May add simple, generic trust iconography (no Apple trademarks, no competitor marks).
No prices, no platform references, no unverifiable claims.
```

---

## Handling Empty States

If the raw screenshot shows an empty state (no data, blank lists, etc.), add this to your prompt:

```
If the app screen appears empty or has placeholder content, populate it with
realistic fictional data that demonstrates the feature in use. Use fictional
names, messages, and content — never real personal data.
```

This is acceptable because:
- It's often impractical to seed perfect demo data in the simulator
- The core UI structure from the screenshot is preserved
- Only content/data is filled in, not new UI elements

---

## Global Rules (Include in Every Prompt)

- Output must be exactly {WIDTH}x{HEIGHT} pixels
- Use the raw screenshot as the ONLY source of app UI structure
- Do NOT add UI elements not present in the screenshot
- If the screen is empty, populate with realistic fictional content (see above)
- Keep UI large and readable
- Keep text inside safe margins (~5% from edges)
- No prices or competitor references
- Include IAP disclosure if the feature requires subscription

---

## Output Naming

**Drafts (Step 3):**
```
./screenshots/drafts/<locale>/<device_category>/<frame_id>.png
```

**Finals (Step 4):**
```
./screenshots/final/<locale>/<device_category>/<index>_<slug>.png
```

---

## Common Mistakes to Avoid

| Mistake | Why It's Wrong |
|---------|----------------|
| Omitting `--input-image` | Generates fake mockup, not real app UI |
| Using `2K`/`4K` for drafts | Wastes time and API cost |
| Prompt says "create an iPhone showing..." | Model may redraw the UI instead of using the input |
| Not specifying exact dimensions | Output may be wrong size for App Store |

---

**After generating, return to [SKILL.md](SKILL.md) for the checkpoint.**
