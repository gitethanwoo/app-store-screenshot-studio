# Step 2: Capture Raw Screenshots

Use Xcode Build MCP to capture screenshots from the simulator.

## Simulator Selection

Pick a simulator that outputs the right size:

| Category | Simulator | Size |
|----------|-----------|------|
| iphone_6_9 | iPhone 15/16 Pro Max | 1290x2796 |
| ipad_13 | iPad Pro 13" | 2048x2732 |

## What to Do

1. Build and run the app
2. Navigate to each screen from the brief
3. Capture screenshot via Xcode Build MCP

## Output Convention

```
./screenshots/raw/<locale>/<device_category>/<frame_id>.png
```

Example: `./screenshots/raw/en-US/iphone_6_9/01_hero.png`

## Notes

- Empty states are fine — Nano Banana Pro can populate them with fictional content
- Don't stress about perfect demo data

**Return to [SKILL.md](SKILL.md) Step 2 Checkpoint when done.**
