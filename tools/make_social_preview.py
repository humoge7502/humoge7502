#!/usr/bin/env python3
"""Generate assets/social-preview.png (1280x640) — the command-deck hero as a
static PNG for the GitHub social-preview setting (Settings -> General ->
Social preview). Run: python3 tools/make_social_preview.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
BG_TOP = (11, 16, 28)     # #0B101C
BG_BOT = (7, 10, 17)      # #070A11
SURFACE = (13, 21, 38)    # #0D1526
BORDER = (30, 41, 59)     # #1E293B
CYAN = (34, 211, 238)     # #22D3EE
VIOLET = (167, 139, 250)  # #A78BFA
GREEN = (52, 211, 153)    # #34D399
AMBER = (251, 191, 36)    # #FBBF24
TEXT = (230, 237, 243)    # #E6EDF3
MUTED = (139, 152, 169)   # #8B98A9

MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def draw_text(d, xy, text, fnt, fill):
    d.text(xy, text, font=fnt, fill=fill)

def text_w(text, fnt):
    b = fnt.getbbox(text)
    return b[2] - b[0]

def spaced_text(d, x, y, text, fnt, fill, spacing):
    """Draw text with fixed letter-spacing (PIL has no native support)."""
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        x += fnt.getbbox(ch)[2] - fnt.getbbox(ch)[0] + spacing

def rounded_rect(d, box, r, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=r, fill=fill, outline=outline, width=width)

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

# vertical gradient background
for y in range(H):
    t = y / (H - 1)
    col = tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=col)

# grid
grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(grid)
for x in range(0, W, 44):
    gd.line([(x, 0), (x, H)], fill=(30, 41, 59, 70))
for y in range(0, H, 44):
    gd.line([(0, y), (W, y)], fill=(30, 41, 59, 70))
img = Image.alpha_composite(img.convert("RGBA"), grid).convert("RGB")
d = ImageDraw.Draw(img)

# corner brackets
bk = 16
for (cx, cy, dx, dy) in [(24, 24, 1, 1), (W - 24, 24, -1, 1), (24, H - 24, 1, -1), (W - 24, H - 24, -1, -1)]:
    d.line([(cx, cy + dx * 0), (cx, cy + dy * 34)], fill=CYAN, width=3)
    d.line([(cx, cy), (cx + dx * 34, cy)], fill=CYAN, width=3)

f10 = font(MONO, 18)
# top bar
draw_text(d, (48, 40), "HUMOGE7502 // PROFILE", f10, MUTED)
draw_text(d, (W - 320, 40), "BUILD 2026.09", f10, MUTED)
d.ellipse([W - 236, 45, W - 226, 55], fill=GREEN)

# avatar
ax, ay, ar = 168, 264, 78
d.ellipse([ax - ar, ay - ar, ax + ar, ay + ar], outline=CYAN, width=4)
d.ellipse([ax - ar + 14, ay - ar + 14, ax + ar - 14, ay + ar - 14], fill=SURFACE, outline=BORDER, width=2)
fmono_kp = font(MONO_B, 52)
kp = "KP"
w = text_w(kp, fmono_kp)
draw_text(d, (ax - w / 2, ay - 32), kp, fmono_kp, TEXT)

# identity
fname = font(SANS_B, 50)
spaced_text(d, 296, 212, "KRISHNA PURI", fname, TEXT, 5)
frole = font(MONO, 19)
spaced_text(d, 300, 292, "SYSTEMS ENGINEER", frole, CYAN, 6)
ftag = font(MONO, 16)
draw_text(d, (300, 336), "deterministic money paths · post-quantum · real-time telemetry", ftag, MUTED)

# core systems panel
px, py, pw, ph = 852, 148, 388, 276
rounded_rect(d, [px, py, px + pw, py + ph], 14, SURFACE, BORDER, 2)
d.polygon([(px, py), (px, py - 22), (px + 22, py)], fill=CYAN)
fpanel = font(MONO, 15)
draw_text(d, (px + 26, py + 22), "CORE SYSTEMS", font(MONO, 15), VIOLET)
rows = [
    ("ORACLE 23AI OLTP", GREEN, "ONLINE"),
    ("TIMESCALE TELEMETRY", GREEN, "ONLINE"),
    ("OCPP 1.6J GATEWAY", GREEN, "ONLINE"),
    ("PQC CBOM SCANNER", GREEN, "ONLINE"),
    ("BASE L2 ATTESTATION", GREEN, "ONLINE"),
    ("FULL-PROFILE BENCH", AMBER, "PENDING"),
]
ystart = py + 58
for i, (label, color, status) in enumerate(rows):
    ry = ystart + i * 34
    draw_text(d, (px + 26, ry), label, fpanel, MUTED)
    d.ellipse([px + 312, ry + 4, px + 322, ry + 14], fill=color)
    draw_text(d, (px + 332, ry), status, font(MONO, 14), color)

# terminal footer
tx, ty, tw, th = 48, 512, W - 96, 74
rounded_rect(d, [tx, ty, tx + tw, ty + th], 10, (7, 11, 18), BORDER, 2)
fterm = font(MONO, 17)
draw_text(d, (72, 538), "$", fterm, CYAN)
cmd = 'gh profile --engines volthub_csms,qtrust --discipline "trade-offs named, claims receipted, races proven in CI"'
draw_text(d, (96, 538), cmd, fterm, TEXT)
d.rectangle([96, 556, 396, 559], fill=BORDER)
d.rectangle([96, 556, 176, 559], fill=CYAN)

# footer signal line
d.rectangle([48, H - 26, W - 48, H - 24], fill=BORDER)
for x in range(48, W - 48, 8):
    t = (x - 48) / (W - 96)
    col = tuple(int(CYAN[i] + (VIOLET[i] - CYAN[i]) * t) for i in range(3))
    d.line([(x, H - 26), (min(x + 6, W - 48), H - 26)], fill=col, width=2)

img.save("assets/social-preview.png")
print("wrote assets/social-preview.png (1280x640)")