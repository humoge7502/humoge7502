#!/usr/bin/env python3
"""Generate the placeholder avatar for the profile pack.

Run:  python3 tools/make_avatar.py
Output: assets/avatar.png (400x400)

Replace assets/avatar.png with a real photo before publishing:
  - square crop, 400x400 (or larger, it scales down)
  - face centered, ~60% of the frame height
  - PNG or JPG; keep the filename avatar.png
The hero.svg references it by relative path, so nothing else changes.
"""
from PIL import Image, ImageDraw, ImageFont

SIZE = 400
BG = (10, 14, 23)      # #0A0E17
SURFACE = (17, 23, 38) # #111726
CYAN = (34, 211, 238)  # #22D3EE
VIOLET = (167, 139, 250)  # #A78BFA
TEXT = (230, 237, 243) # #E6EDF3

FONT_PATHS = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

def load_font(size):
    for path in FONT_PATHS:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()

img = Image.new("RGB", (SIZE, SIZE), BG)
d = ImageDraw.Draw(img)

# subtle background grid
step = 40
for x in range(0, SIZE, step):
    d.line([(x, 0), (x, SIZE)], fill=(30, 41, 59, 255), width=1)
for y in range(0, SIZE, step):
    d.line([(0, y), (SIZE, y)], fill=(30, 41, 59, 255), width=1)

# inner surface disc
d.ellipse([40, 40, SIZE - 40, SIZE - 40], fill=SURFACE, outline=(30, 41, 59), width=3)

# dual accent ring (cyan arc + violet arc, approximated with chord segments)
ring = 24
d.arc([30, 30, SIZE - 30, SIZE - 30], start=0, end=180, fill=CYAN, width=ring)
d.arc([30, 30, SIZE - 30, SIZE - 30], start=180, end=360, fill=VIOLET, width=ring)

# monogram
font = load_font(150)
text = "KP"
bbox = d.textbbox((0, 0), text, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
d.text(((SIZE - w) / 2 - bbox[0], (SIZE - h) / 2 - bbox[1]), text, font=font, fill=TEXT)

img.save("assets/avatar.png")
print("wrote assets/avatar.png (400x400 placeholder)")