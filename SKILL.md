---
name: app-store-screenshot-studio
description: Capture real App Store screenshots via Xcode Build MCP, then generate App Store Connect-ready marketing screenshots with Nano Banana Pro (correct sizes, copy, compliance).
---

# App Store Screenshot Studio

You produce App Store Connect-ready screenshot sets by:
1) creating a tight screenshot "story" + copy,
2) capturing real in-app screenshots via Xcode Build MCP,
3) compositing App Store marketing frames via Nano Banana Pro,
4) validating sizing + Apple compliance,
5) packaging assets for submission.

Use this skill when the user asks for App Store screenshots, screenshot automation, App Store Connect-ready images, or "marketing screenshots for submission".

## Dependencies (check before starting)

This skill requires two other tools. Before proceeding, verify they are available:

### 1. Nano Banana Pro (image generation)
- **What it does:** Generates marketing composite images from raw screenshots using Google Gemini 3 Pro Image
- **Check:** Look for the `nano-banana-pro` skill or `/nano-banana-pro` command
- **Source:** https://github.com/steipete/agent-scripts/tree/main/skills/nano-banana-pro
- **Install if missing:**
  ```bash
  git clone --depth 1 https://github.com/steipete/agent-scripts /tmp/agent-scripts && \
    cp -r /tmp/agent-scripts/skills/nano-banana-pro ~/.claude/skills/ && \
    rm -rf /tmp/agent-scripts
  ```
- **Requires:** `GEMINI_API_KEY` environment variable

### 2. XcodeBuildMCP (simulator control)
- **What it does:** Builds apps, boots simulators, captures screenshots via simctl
- **Check:** Look for `XcodeBuildMCP` tools (e.g., `xcodebuild_build`, `simulator_boot`)
- **Install if missing:**
  ```bash
  # One-liner for Claude Code
  claude mcp add XcodeBuildMCP npx xcodebuildmcp@latest
  ```
  Or add to MCP config (`~/.claude.json` or `.mcp.json`):
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
- **Source:** https://github.com/cameroncooke/XcodeBuildMCP

### If dependencies are missing
If either dependency is unavailable:
1. **STOP** and inform the user which dependency is missing
2. **Provide the install command** from above
3. **Offer alternatives:**
   - Without Xcode Build MCP: User can provide raw screenshots manually, then you composite them
   - Without Nano Banana Pro: You can create the screenshot brief and capture raws, but user needs another tool for compositing

Do NOT attempt to proceed with the full workflow if dependencies are missing. Partial workflows are acceptable if clearly communicated.

## Non-negotiables (Apple compliance)
Follow these guardrails every time:
- Never misrepresent the app. Don't add UI, features, badges, or claims the app does not actually provide.
- Screenshots must show the app in use (not just splash/title art; avoid "login-only" sets).
- If a screenshot promotes a feature/content that requires subscription/IAP, the screenshot copy must clearly disclose that.
- Do not include prices or price-like claims in screenshot overlays (examples: "$4.99", "free today", "limited time offer").
- Do not reference other mobile platforms/marketplaces (names, icons, imagery) in screenshots/overlays.
- Use fictional/demo data (names, emails, messages, health/finance info, etc). No real personal data.

If the user's requested copy/layout violates any of the above, STOP and propose compliant alternative copy/layout.

For exact references and common rejection vectors, see [REFERENCE_APPLE.md](REFERENCE_APPLE.md).

## Technical requirements (must validate before "done")
- Output: `.png`, `.jpg`, or `.jpeg`
- Per device size: minimum 1, maximum 10 screenshots.
- Dimensions must exactly match an accepted pixel size for the intended device category.
- Prefer shipping only the highest-resolution required screenshot set per platform when the UI is the same (Apple scales down). Only generate extra sizes if the user explicitly wants per-size customization.

See [REFERENCE_SIZES.md](REFERENCE_SIZES.md).

## Inputs (don't block; infer if missing)
If the user doesn't supply these, make reasonable defaults and clearly state them:
- App name + one-sentence value prop
- Platforms: iOS, iPadOS (assume iOS; ask only if truly unknown)
- Locales to produce (default: en-US)
- Style direction (default: clean/minimal, matches app UI)
- Screenshot count target (default: 7)
- Any "do not show" content (default: avoid all personal data and any sensitive screens)

## Required workflow

### Step 1 — Create the "Screenshot Brief" (storyboard)
Output a concise brief with 5–10 frames, each with:
- frame_id (e.g., 01_hero)
- device_category (e.g., iphone_6_9, ipad_13)
- in-app screen/state to capture (how to reach it)
- headline (2–5 words, benefit-led)
- subheadline (optional, <= 10 words)
- visual emphasis (what to highlight)
- compliance notes (IAP disclosure? privacy wording? avoid claims?)

Rules of thumb:
- One idea per frame.
- Put your strongest value prop first.
- Keep text big, minimal, and scannable.

### Step 2 — Capture raw screenshots via Xcode Build MCP
Use Xcode Build MCP to:
- build the app
- boot the correct simulators for the required device categories
- run an automated screenshot flow (XCUITest / snapshot / simctl)
- export to: `./screenshots/raw/<locale>/<device_category>/<frame_id>.png`

Hard requirements:
- screenshots must be taken from the actual app UI (no Figma/placeholder comps as the base)
- use deterministic data (seeded content, mocked network, demo account)
- keep status bar consistent where possible
- never capture real personal data

If you need play-by-play guidance, see [PLAYBOOK_XCODE_MCP.md](PLAYBOOK_XCODE_MCP.md).

### Step 3 — Generate marketing composites via Nano Banana Pro

**⚠️ CRITICAL: You MUST pass the raw screenshot as `--input-image`. Do NOT generate from text prompts alone.**

This is a two-phase process:

#### Phase A: Generate LOW-RES drafts (1K) for approval
```bash
uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --input-image "./screenshots/raw/en-US/iphone_6_9/01_hero.png" \
  --prompt "Your compositing prompt here" \
  --filename "./screenshots/drafts/en-US/iphone_6_9/01_hero.png" \
  --resolution 1K
```

**Hard requirements for Phase A:**
- `--input-image` is MANDATORY — never omit it
- `--resolution 1K` — drafts must be low-res to save time/cost
- Output to `./screenshots/drafts/` (not `final/`)
- Show drafts to user and get explicit approval before proceeding

#### Phase B: Generate HIGH-RES finals (2K/4K) after approval
Only after user approves the drafts:
```bash
uv run ~/.claude/skills/nano-banana-pro/scripts/generate_image.py \
  --input-image "./screenshots/raw/en-US/iphone_6_9/01_hero.png" \
  --prompt "Same compositing prompt" \
  --filename "./screenshots/final/en-US/iphone_6_9/01_hero.png" \
  --resolution 2K
```

**If you skip `--input-image`, you are generating fake mockups, not compositing real app UI. This violates Apple compliance.**

Composition rules:
- Preserve the raw screenshot faithfully; do not invent UI elements.
- Keep UI large and readable (don't shrink the app UI into a tiny phone).
- Keep headline/subheadline inside safe margins (assume rounded corners and App Store cropping).
- Maintain consistent layout across the set (grid, typography, background system).

Use [PROMPTS_NANO_BANANA.md](PROMPTS_NANO_BANANA.md) templates.

### Step 4 — Validate (and fix before shipping)
You are not "done" until validation passes:
- all images are in accepted pixel sizes for their device_category
- formats are valid (.png/.jpg/.jpeg)
- no transparency/alpha surprises (flatten if unsure)
- per device_category: 1–10 images
- copy passes compliance guardrails (no prices, no other platforms, no unverifiable claims)
- IAP disclosures present when needed
- every locale has a complete set

If scripts are available, run:
`python scripts/validate_screenshots.py ./screenshots/final`

If anything fails: fix by regenerating or recapturing. Don't leave "almost right" assets.

### Step 5 — Package for submission
Produce:
- a ZIP of `./screenshots/final`
- a `screenshots_manifest.json` listing locale → device_category → ordered files

## How to finish your response to the user
Always end with:
1) What you generated (locales, device categories, counts)
2) A file tree showing raw + final paths
3) Any compliance notes (especially IAP disclosure decisions)
4) Next recommended steps (upload order, optional A/B variants)
