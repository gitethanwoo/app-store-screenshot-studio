# App Store Screenshot Studio

A Claude Code skill for generating App Store Connect-ready screenshot sets with Apple compliance baked in.

## What it does

This skill orchestrates:
- **Apple compliance checks** (App Review + App Store Connect screenshot rules)
- **Screenshot storyboard/copy workflow** ("good screenshots" planning)
- **Automated capture** via Xcode Build MCP
- **Marketing compositing** via Nano Banana Pro
- **Validation + packaging** so you're not uploading "almost right" assets

## Prerequisites

This skill depends on two other tools:

### 1. Nano Banana Pro (image generation)
Generates marketing composites from raw screenshots using Google Gemini 3 Pro Image.

Source: [steipete/agent-scripts/skills/nano-banana-pro](https://github.com/steipete/agent-scripts/tree/main/skills/nano-banana-pro)

```bash
# Clone and copy the skill
git clone --depth 1 https://github.com/steipete/agent-scripts /tmp/agent-scripts && \
  cp -r /tmp/agent-scripts/skills/nano-banana-pro ~/.claude/skills/ && \
  rm -rf /tmp/agent-scripts
```

Requires `GEMINI_API_KEY` in your environment.

### 2. XcodeBuildMCP (simulator control)
Builds apps, boots simulators, captures screenshots. See [cameroncooke/XcodeBuildMCP](https://github.com/cameroncooke/XcodeBuildMCP).

```bash
# One-liner for Claude Code
claude mcp add XcodeBuildMCP npx xcodebuildmcp@latest
```

Or add to your MCP config manually (`~/.claude.json` or `.mcp.json`):
```json
{
  "mcpServers": {
    "XcodeBuildMCP": {
      "command": "npx",
      "args": ["-y", "xcodebuildmcp@latest"]
    }
  }
}
```

> **Note:** The skill will check for these dependencies and guide users through installation if missing. Partial workflows are supported (e.g., user provides raw screenshots manually).

## Installation

### One-liner (recommended)
```bash
git clone https://github.com/gitethanwoo/app-store-screenshot-studio ~/.claude/skills/app-store-screenshot-studio
```

Then restart Claude Code.

### Alternative: project-level skill
If you want the skill scoped to a specific project:
```bash
git clone https://github.com/gitethanwoo/app-store-screenshot-studio .claude/skills/app-store-screenshot-studio
```

### For agents
Clone to the user's Claude skills directory:
```bash
git clone https://github.com/gitethanwoo/app-store-screenshot-studio ~/.claude/skills/app-store-screenshot-studio
```
Restart Claude Code to load the skill.

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
