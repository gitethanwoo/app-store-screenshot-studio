#!/usr/bin/env python3
"""
Validate App Store screenshot assets (basic checks):
- File extension is .png/.jpg/.jpeg
- Pixel dimensions match one of Apple's accepted sizes for key iPhone/iPad categories
- Warn if alpha/transparency is present
- Warn if any folder appears to have >10 screenshots (common App Store Connect limit)

Usage:
  python scripts/validate_screenshots.py ./screenshots/final
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Missing dependency: Pillow. Install with: pip install pillow", file=sys.stderr)
    sys.exit(2)


# Accepted sizes (subset focused on common iOS/iPadOS submission paths).
# Source: App Store Connect Help "Screenshot specifications".
ALLOWED_SIZES = {
    # iPhone 6.9" display
    (1260, 2736), (2736, 1260),
    (1290, 2796), (2796, 1290),
    (1320, 2868), (2868, 1320),

    # iPhone 6.5" display
    (1284, 2778), (2778, 1284),
    (1242, 2688), (2688, 1242),

    # iPad 13" display
    (2064, 2752), (2752, 2064),
    (2048, 2732), (2732, 2048),
}


VALID_EXTS = {".png", ".jpg", ".jpeg"}


def has_alpha(img: Image.Image) -> bool:
    if img.mode in ("RGBA", "LA"):
        return True
    if img.mode == "P" and "transparency" in img.info:
        return True
    return False


def main(root: Path) -> int:
    if not root.exists():
        print(f"Path does not exist: {root}", file=sys.stderr)
        return 2

    files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in VALID_EXTS]
    if not files:
        print(f"No images found under: {root}", file=sys.stderr)
        return 2

    issues: list[str] = []
    warnings: list[str] = []

    # Count images per leaf directory (rough proxy for "per device category" folders).
    per_dir_counts = defaultdict(int)

    for f in sorted(files):
        per_dir_counts[f.parent] += 1
        try:
            with Image.open(f) as img:
                w, h = img.size

                if (w, h) not in ALLOWED_SIZES:
                    issues.append(f"[SIZE] {f}: {w}x{h} is not in allowed size list")

                if has_alpha(img):
                    warnings.append(f"[ALPHA] {f}: image appears to contain transparency/alpha; consider flattening to RGB")
        except Exception as e:
            issues.append(f"[READ] {f}: failed to open/read image ({e})")

    for d, count in sorted(per_dir_counts.items(), key=lambda x: str(x[0])):
        if count > 10:
            warnings.append(f"[COUNT] {d}: contains {count} images (App Store Connect commonly allows max 10 per device size)")

    print("Validation summary")
    print(f"- Scanned: {len(files)} image(s)")
    print(f"- Issues:  {len(issues)}")
    print(f"- Warnings:{len(warnings)}")
    print()

    if warnings:
        print("Warnings:")
        for w in warnings:
            print("  " + w)
        print()

    if issues:
        print("Issues:")
        for i in issues:
            print("  " + i)
        print()
        return 1

    print("OK: No blocking issues detected.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=str, help="Root directory of final screenshots (e.g., ./screenshots/final)")
    args = parser.parse_args()

    sys.exit(main(Path(args.root)))
