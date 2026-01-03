# App Store Connect screenshot sizing quick reference

## File formats + count
- Screenshots: 1–10 per device size.
- Formats: .png, .jpg, .jpeg

## Recommended strategy
If the app UI is the same across device sizes/locales, prefer creating only the highest-resolution required screenshots per platform. App Store Connect can scale down for smaller sizes.

If you want per-size custom layouts, generate additional sizes intentionally.

## iPhone (key categories)
### iphone_6_9 (recommended "top" iPhone category)
Accepted sizes:
- Portrait: 1260x2736, 1290x2796, 1320x2868
- Landscape: 2736x1260, 2796x1290, 2868x1320

### iphone_6_5 (fallback)
Accepted sizes:
- Portrait: 1284x2778, 1242x2688
- Landscape: 2778x1284, 2688x1242

Important: 6.5" is required if the app runs on iPhone and you do NOT provide 6.9" screenshots.

## iPad (key category)
### ipad_13 (required if app runs on iPad)
Accepted sizes:
- Portrait: 2064x2752, 2048x2732
- Landscape: 2752x2064, 2732x2048

## Notes
- For most iOS apps, shipping iphone_6_9 + ipad_13 (if iPad supported) is sufficient.
- Keep orientation consistent per set unless you have a strong reason to mix.
