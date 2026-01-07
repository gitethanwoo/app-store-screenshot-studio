# Step 3: Generate Marketing Composites

Use Nano Banana Pro to composite raw screenshots with marketing text/backgrounds.

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

---

## Resolution Workflow

| Phase | Resolution | Output Folder |
|-------|------------|---------------|
| **Draft** | `1K` | `./screenshots/drafts/` |
| **Final** | `2K` (iPhone) or `4K` (iPad) | `./screenshots/final/` |

**Never generate 2K/4K until drafts are approved.**

---

## Prompt Templates

### Template A: Clean & Modern

```
Create an App Store marketing screenshot.

Place the provided screenshot prominently as the base layer.
DO NOT alter or recreate the app UI.

Background: Subtle gradient using {BRAND_COLORS}.

Headline: "{HEADLINE}"
Subheadline: "{SUBHEADLINE}"

If the screen is empty, populate with realistic fictional content.
```

### Template B: Feature Callout

```
Create an App Store marketing screenshot.

Use the provided screenshot as the base — DO NOT recreate the app UI.

Add:
- Headline: "{HEADLINE}"
- 1-2 callout labels pointing to real parts of the UI

If the screen is empty, populate with realistic fictional content.
```

### Template C: Trust / Privacy

```
Create an App Store marketing screenshot.

Use the provided screenshot as the base — DO NOT recreate the app UI.

Headline: "{HEADLINE}"
Subheadline: "{SUBHEADLINE}"

If the screen is empty, populate with realistic fictional content.
No prices, no competitor references.
```

---

## Output Naming

- **Drafts:** `./screenshots/drafts/<locale>/<device_category>/<frame_id>.png`
- **Finals:** `./screenshots/final/<locale>/<device_category>/<frame_id>.png`

---

## Common Mistakes

| Mistake | Why It's Wrong |
|---------|----------------|
| Omitting `--input-image` | Generates fake mockup instead of using real app UI |
| Using `2K`/`4K` for drafts | Wastes time and API cost |
| Prompt says "create an iPhone showing..." | Model may redraw the UI instead of using the input |

---

**After generating, return to [SKILL.md](SKILL.md) for the checkpoint.**
