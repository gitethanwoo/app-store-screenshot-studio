# Xcode Build MCP playbook for capturing raw screenshots

Goal: produce clean, deterministic raw screenshots at accepted pixel sizes.

## 1) Pick simulators that output accepted sizes
Recommended defaults (widely available in modern Xcode):
- iPhone: choose a "Pro Max / Plus" simulator that outputs 1290x2796 (fits iphone_6_9 accepted sizes)
- iPad: choose an iPad Pro/Air simulator that outputs 2048x2732 or 2064x2752 (fits ipad_13 accepted sizes)

If your simulator outputs a size not accepted for the category you need, recapture on a different simulator.

## 2) Make screenshots deterministic
Best practices:
- Add a UI testing mode (launch argument or env var) to:
  - seed data
  - disable animations where possible
  - mock network responses
  - log in automatically with a demo account
- Use fictional names/emails/messages.
- Ensure no push notifications, permission popups, or random toasts appear mid-capture.

## 3) Standardize the status bar (optional but recommended)
If your MCP exposes simctl, set:
- time to 9:41
- full battery
- strong Wi-Fi
This makes the set look intentional.

## 4) Capture method options
Preferred: XCUITest screenshot runner
- Navigate to each target screen/state from the Screenshot Brief.
- Capture with stable identifiers that match frame_id.

Alternative: simctl screenshot
- Launch app and navigate via UI automation, then grab screenshots via simctl.
- This is faster to hack but can be less deterministic.

## 5) Output convention
Write raw screenshots to:
`./screenshots/raw/<locale>/<device_category>/<frame_id>.png`

Example:
`./screenshots/raw/en-US/iphone_6_9/01_hero.png`

## 6) Sanity checks
After capture:
- verify each raw image has the expected pixel dimensions for the device_category
- verify no personal data is visible
- verify UI is crisp and not motion-blurred
