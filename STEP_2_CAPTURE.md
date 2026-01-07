# Step 2: Capture Raw Screenshots

Detailed guidance for capturing screenshots via Xcode Build MCP.

**You should only be reading this after completing Step 1 (Screenshot Brief).**

---

## Simulator Selection

Choose simulators that output accepted pixel sizes:

| Category | Simulator | Output Size |
|----------|-----------|-------------|
| iphone_6_9 | iPhone 15 Pro Max, iPhone 16 Pro Max | 1290x2796 |
| iphone_6_5 | iPhone 14 Plus, iPhone 15 Plus | 1284x2778 |
| ipad_13 | iPad Pro 13" | 2048x2732 or 2064x2752 |

If your simulator outputs a different size, pick a different device.

---

## Make Screenshots Deterministic

Set up the app for predictable captures:

- **Seed data:** Use a demo account or mock data
- **Disable animations:** Where possible, to avoid motion blur
- **Mock network:** Ensure consistent content loads
- **Block interruptions:** No push notifications, permission dialogs, or toasts

Use fictional names/emails/messages only.

---

## Standardize the Status Bar (Optional)

If Xcode Build MCP exposes simctl status bar controls, set:
- Time: 9:41
- Battery: 100%
- Wi-Fi: Full signal

This makes the set look polished and intentional.

---

## Capture Methods

### Option A: XCUITest (Preferred)
- Navigate to each screen from the brief programmatically
- Capture with identifiers matching `frame_id`
- Most deterministic

### Option B: simctl screenshot
- Launch app manually or via automation
- Use `simctl screenshot` to capture
- Faster to set up, less deterministic

---

## Output Convention

Save raw screenshots to:
```
./screenshots/raw/<locale>/<device_category>/<frame_id>.png
```

Example:
```
./screenshots/raw/en-US/iphone_6_9/01_hero.png
./screenshots/raw/en-US/iphone_6_9/02_search.png
```

---

## Sanity Checks

Before returning to the main workflow, verify:

- [ ] Each image has correct pixel dimensions for its device category
- [ ] No real personal data visible
- [ ] UI is crisp (no motion blur)
- [ ] All frames from the brief are captured

**Then return to [SKILL.md](SKILL.md) Step 2 Checkpoint.**
