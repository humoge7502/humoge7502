#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_og.py — renders the 1280x640 social preview PNG for the profile repo
(GitHub: Settings → Social preview). Composites the dark hero console over a
chassis-colored canvas with a matching footer strip.

Run after build_assets.py:   python3 tools/make_og.py
Needs: cairosvg, Pillow.
"""

import os

import cairosvg
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.dirname(HERE)
ASSETS = os.path.join(PACK, "assets")

W, H = 1280, 640
BG = (10, 14, 20)          # #0A0E14 — same chassis color as the SVGs
GREEN = (74, 222, 128)     # #4ADE80
MUTED = (90, 102, 117)     # #5A6675

MONO_TTF = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def main():
    hero_png = os.path.join(ASSETS, "hero-console.svg")
    tmp = os.path.join(ASSETS, "_hero_tmp.png")
    cairosvg.svg2png(url=hero_png, write_to=tmp, output_width=W)

    hero = Image.open(tmp).convert("RGB")
    canvas = Image.new("RGB", (W, H), BG)
    canvas.paste(hero, (0, (H - hero.height) // 2 - 14))

    d = ImageDraw.Draw(canvas)
    # footer strip, aligned with the hero's bottom telemetry bar
    fy = H - 96
    d.rectangle([0, fy, W, fy + 2], fill=GREEN)
    d.rectangle([0, 0, 4, H], fill=GREEN)
    d.rectangle([W - 4, 0, W, H], fill=GREEN)

    f_big = ImageFont.truetype(MONO_BOLD, 26)
    f_small = ImageFont.truetype(MONO_TTF, 16)
    d.text((32, fy + 26), "KRISHNA PURI — OPERATOR CONSOLE", font=f_big, fill=(230, 237, 243))
    d.text((32, fy + 62), "receipts over claims · every badge is a live CI status", font=f_small, fill=MUTED)
    link = "github.com/humoge7502"
    lw = d.textlength(link, font=f_small)
    d.text((W - 32 - lw, fy + 44), link, font=f_small, fill=GREEN)

    out = os.path.join(ASSETS, "og-profile.png")
    canvas.save(out, "PNG", optimize=True)
    os.remove(tmp)
    print(f"  {os.path.relpath(out, PACK):48s} {os.path.getsize(out)/1024:7.1f} KB")


if __name__ == "__main__":
    main()
