# App Store Screenshot Studio

A Claude Code skill for generating App Store Connect-ready screenshot sets with Apple compliance baked in.

## What it does

This skill orchestrates:
- **Apple compliance checks** (App Review + App Store Connect screenshot rules)
- **Screenshot storyboard/copy workflow** ("good screenshots" planning)
- **Automated capture** via Xcode Build MCP
- **Marketing compositing** via Nano Banana Pro
- **Validation + packaging** so you're not uploading "almost right" assets

## Installation

### As a personal skill (all projects)
```bash
cp -r app-store-screenshot-studio ~/.claude/skills/
```

### As a project skill (this repo only)
```bash
cp -r app-store-screenshot-studio .claude/skills/
```

Then restart Claude Code.

## Usage

Just ask Claude for App Store screenshots:

> "Generate App Store screenshots for my app"

> "Create marketing screenshots for App Store submission"

> "I need App Store Connect-ready images for iPhone and iPad"

Claude will automatically:
1. Create a screenshot brief/storyboard
2. Capture raw screenshots via Xcode Build MCP
3. Generate marketing composites via Nano Banana Pro
4. Validate sizing and compliance
5. Package for submission

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill definition and workflow |
| `REFERENCE_APPLE.md` | Apple compliance checklist |
| `REFERENCE_SIZES.md` | Accepted screenshot dimensions |
| `PLAYBOOK_XCODE_MCP.md` | Guide for capturing raw screenshots |
| `PROMPTS_NANO_BANANA.md` | Prompt templates for marketing composites |
| `scripts/validate_screenshots.py` | Validation script for final assets |

## Validation script

Requires Pillow:
```bash
pip install pillow
```

Run validation:
```bash
python scripts/validate_screenshots.py ./screenshots/final
```

## Apple compliance (built-in)

The skill enforces:
- No misrepresentation of app features
- Screenshots show app in use (not just splash screens)
- IAP/subscription disclosures when needed
- No prices in overlays
- No references to other platforms
- Fictional/demo data only
- Exact pixel dimensions for each device category

## License

MIT
