#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_assets.py — generates every SVG asset for the K/OS "Operator Console"
GitHub profile. Pure standard library (Pillow only when --photo is given).

Usage:
  python3 scripts/build_assets.py                    # monogram slot (no photo)
  python3 scripts/build_assets.py --photo photo.jpg  # bake real portrait in

Outputs to the pack's assets/ directory next to this script's parent.
Assets are deliberately lightweight (< 15 KB each without photo).
"""

import argparse
import base64
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svg_lib import (DARK, LIGHT, MONO, BANNER_W, BANNER_H, GENERATED_BY,
                     esc, _fmt, pixel_brackets, dither_strip, blink_dot,
                     caret, glitch_title, scanlines, chassis, mono,
                     section_strip, mission_card, achievements_strip,
                     icon_fork, icon_shield, icon_selfscan, icon_race,
                     icon_gauge)

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.dirname(HERE)
ASSETS = os.path.join(PACK, "assets")


# ---------------------------------------------------------------------------
# PHOTO EMBEDDING (self-contained SVG — no external refs, renders everywhere)
# ---------------------------------------------------------------------------

def prepare_photo_b64(photo_path, px=320, quality=82):
    """Square-center-crop, downscale, JPEG, base64. Keeps SVG small."""
    from PIL import Image
    im = Image.open(photo_path).convert("RGB")
    w, h = im.size
    s = min(w, h)
    im = im.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))
    im = im.resize((px, px), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


# ---------------------------------------------------------------------------
# HERO — the operator console
# ---------------------------------------------------------------------------

def hero(c, photo_b64=None):
    W, H = BANNER_W, BANNER_H
    p = []

    TOP_H = 34          # top status bar
    BOT_Y = H - 42      # bottom telemetry strip
    RY, RH = 46, BOT_Y - 46 - 10   # panel band

    p.append(chassis(c, W, H, rx=12))
    # subtle vertical sheen (controlled gradient — separates status bar from
    # the working surface)
    p.append(f"""  <defs>
    <linearGradient id="sheen" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{c['line2']}" stop-opacity="0.14"/>
      <stop offset="1" stop-color="{c['bg']}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="frame"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="11"/></clipPath>
    <clipPath id="photoClip"></clipPath>
  </defs>
  <rect x="0" y="0" width="{W}" height="44" fill="url(#sheen)" clip-path="url(#frame)"/>""")

    # ============ TOP STATUS BAR ============
    p.append(f'  <rect x="0" y="0" width="{W}" height="{TOP_H}" fill="{c["panel2"]}"/>')
    p.append(f'  <rect x="0" y="{TOP_H}" width="{W}" height="1.5" fill="{c["line"]}"/>')
    p.append(blink_dot(c, 30, TOP_H / 2, r=4, color=c["green"], dur="2.4s"))
    p.append(mono(f'x="44" y="{TOP_H/2+4}" font-size="11.5" font-weight="700" letter-spacing="2.5"', c["green"], "SYS.ONLINE"))
    p.append(mono(f'x="146" y="{TOP_H/2+4}" font-size="11.5" letter-spacing="1.5"', c["muted"], "K/OS OPERATOR CONSOLE · BUILD 2026.09"))
    p.append(mono(f'x="{W-40}" y="{TOP_H/2+4}" font-size="11" letter-spacing="1" text-anchor="end"', c["faint"], "GITHUB.COM/HUMOGE7502"))

    # ============ LEFT PANEL — OPERATOR LICENSE ============
    LX, LY, LW, LH = 20, RY, 312, RH
    p.append(f'  <rect x="{LX}" y="{LY}" width="{LW}" height="{LH}" rx="10" fill="{c["panel"]}" stroke="{c["line"]}"/>')
    p.append(mono(f'x="{LX+18}" y="{LY+22}" font-size="11" font-weight="700" letter-spacing="2.5"', c["muted"], "OPERATOR LICENSE"))
    p.append(mono(f'x="{LX+LW-18}" y="{LY+22}" font-size="10" letter-spacing="1" text-anchor="end"', c["faint"], "ID 0318-696825"))

    # photo slot (or monogram slot until a portrait is published)
    PSZ = 124
    px, py = LX + (LW - PSZ) / 2, LY + 38
    p.append(f'  <rect x="{_fmt(px)}" y="{py}" width="{PSZ}" height="{PSZ}" rx="10" fill="{c["panel2"]}" stroke="{c["line"]}"/>')
    if photo_b64:
        p.append(f"""  <clipPath id="photoClip"><rect x="{_fmt(px+3)}" y="{py+3}" width="{PSZ-6}" height="{PSZ-6}" rx="8"/></clipPath>
  <image href="{photo_b64}" x="{_fmt(px+3)}" y="{py+3}" width="{PSZ-6}" height="{PSZ-6}" preserveAspectRatio="xMidYMid slice" clip-path="url(#photoClip)"/>
  <rect x="{_fmt(px+3)}" y="{py+3}" width="{PSZ-6}" height="{PSZ-6}" rx="8" fill="{c['green']}" opacity="0.07"/>""")
        p.append(mono(f'x="{_fmt(px+PSZ-12)}" y="{py+PSZ-11}" font-size="9" font-weight="700" letter-spacing="1" text-anchor="end"', c["green"], "ID VERIFIED"))
    else:
        ccx, ccy = px + PSZ / 2, py + PSZ / 2
        p.append(f'  <g opacity="0.22" stroke="{c["line2"]}" stroke-width="1">')
        for gy in range(1, 4):
            p.append(f'  <path d="M {_fmt(px+12)} {py+PSZ*gy/4} H {_fmt(px+PSZ-12)}"/>')
        for gx_ in range(1, 4):
            p.append(f'  <path d="M {_fmt(px+PSZ*gx_/4)} {py+12} V {py+PSZ-12}"/>')
        p.append('  </g>')
        p.append(f'  <g font-family="{MONO}" font-size="40" font-weight="800" letter-spacing="4"><text x="{_fmt(ccx)}" y="{_fmt(ccy+13)}" text-anchor="middle" fill="{c["text"]}" opacity="0.9">KP</text></g>')
        p.append(mono(f'x="{_fmt(ccx)}" y="{_fmt(ccy+40)}" font-size="9" letter-spacing="1" text-anchor="middle"', c["faint"], "SLOT OPEN · see scripts/README"))
    p.append(pixel_brackets(c, px - 6, py - 6, PSZ + 12, PSZ + 12, size=11, color=c["green"], sw=2.5))

    # identity rows
    iy = py + PSZ + 30
    p.append(mono(f'x="{_fmt(LX+LW/2)}" y="{iy}" font-size="15" font-weight="800" letter-spacing="1.5" text-anchor="middle"', c["text"], "K. PURI"))
    p.append(mono(f'x="{_fmt(LX+LW/2)}" y="{iy+19}" font-size="10.5" letter-spacing="1.8" text-anchor="middle"', c["muted"], "CLASS · SYSTEMS ENGINEER"))
    p.append(mono(f'x="{_fmt(LX+LW/2)}" y="{iy+37}" font-size="10.5" letter-spacing="1.2" text-anchor="middle"', c["cyan"], "CALLSIGN · humoge7502"))

    # XP bar — five of six segments earned; the sixth pulses, on purpose.
    xw, xh, xgap = 34, 9, 6
    xbw = 6 * xw + 5 * xgap
    xb0 = LX + (LW - xbw) / 2
    xby = LY + LH - 44
    for i in range(6):
        sx = xb0 + i * (xw + xgap)
        if i < 5:
            p.append(f'  <rect x="{_fmt(sx)}" y="{xby}" width="{xw}" height="{xh}" rx="1.5" fill="{c["green"]}" opacity="0.92"/>')
        else:
            p.append(f'  <rect x="{_fmt(sx)}" y="{xby}" width="{xw}" height="{xh}" rx="1.5" fill="none" stroke="{c["amber"]}" stroke-width="1.4"/>')
            p.append(f'  <rect x="{_fmt(sx)}" y="{xby}" width="{xw}" height="{xh}" rx="1.5" fill="{c["amber"]}"><animate attributeName="opacity" values="0.08;0.45;0.08" dur="2.2s" repeatCount="indefinite"/></rect>')
    p.append(mono(f'x="{_fmt(LX+LW/2)}" y="{xby+24}" font-size="9.5" letter-spacing="1.6" text-anchor="middle"', c["faint"], "LVL 02 · 5/6 XP · THE LAST SEGMENT STAYS OPEN"))

    # ============ RIGHT PANEL — CONSOLE SURFACE ============
    RX = 348
    RW = W - RX - 20
    p.append(f'  <rect x="{RX}" y="{RY}" width="{RW}" height="{RH}" rx="10" fill="{c["panel"]}" stroke="{c["line"]}"/>')

    # glitch title + role line
    p.append(glitch_title(c, RX + 26, RY + 50, "KRISHNA PURI", size=34, weight=800, letter=3))
    p.append(mono(f'x="{RX+27}" y="{RY+76}" font-size="12.5" font-weight="700" letter-spacing="3"', c["cyan"], "SYSTEMS ENGINEER · PROTOCOLS · POST-QUANTUM"))

    # terminal window (a terminal is dark on every theme — that is the point)
    TY = RY + 92
    TH = 86
    p.append(f'  <rect x="{RX+22}" y="{TY}" width="{RW-44}" height="{TH}" rx="8" fill="#05070A" stroke="{c["line"]}"/>')
    p.append(mono(f'x="{RX+RW-40}" y="{TY+18}" font-size="9" letter-spacing="1.5" text-anchor="end"', "#A8B6C6", "TTY1"))
    lines = [
        ("> build: deterministic money paths & concurrent protocols", "#E6EDF3"),
        ("> build: post-quantum migration & attestations  (Q-Trust)", "#E6EDF3"),
        ("> rule:  trade-offs named · claims receipted · CI re-proves", "#4ADE80"),
    ]
    for i, (ln, col) in enumerate(lines):
        p.append(mono(f'x="{RX+42}" y="{TY+38+i*18}" font-size="11.5" letter-spacing="0.3"', col, esc(ln)))
    p.append(caret(c, RX + 44, TY + TH - 12, size=13))

    # status grid 3 x 2
    GY = TY + TH + 12
    ch, cgap = 50, 10
    cw = (RW - 44 - 2 * cgap) / 3
    cells = [
        ("CI · VOLTHUB", "6 JOBS · BOTH ENGINES", c["green"]),
        ("CI · Q-TRUST", "10 WORKFLOWS", c["green"]),
        ("SECURITY", "AUDIT + CODEQL GATED", c["violet"]),
        ("DOCS", "2 LIVE SITES", c["cyan"]),
        ("RELEASES", "10 TAGGED", c["amber"]),
        ("KNOWN CVEs", "0 · GATED IN CI", c["green"]),
    ]
    for i, (label, val, col) in enumerate(cells):
        gx = RX + 22 + (i % 3) * (cw + cgap)
        gy = GY + (i // 3) * (ch + cgap)
        p.append(f'  <rect x="{_fmt(gx)}" y="{gy}" width="{_fmt(cw)}" height="{ch}" rx="6" fill="{c["panel2"]}" stroke="{c["line"]}"/>')
        p.append(f'  <rect x="{_fmt(gx)}" y="{gy}" width="3" height="{ch}" rx="1.5" fill="{col}" opacity="0.85"/>')
        p.append(mono(f'x="{_fmt(gx+15)}" y="{gy+20}" font-size="10.5" font-weight="700" letter-spacing="1.4"', c["muted"], esc(label)))
        p.append(mono(f'x="{_fmt(gx+15)}" y="{gy+38}" font-size="11.5" font-weight="700" letter-spacing="0.6"', col, esc(val)))

    # ============ BOTTOM TELEMETRY STRIP (full width — the HUD footer) ============
    p.append(f'  <rect x="0" y="{BOT_Y}" width="{W}" height="{H-BOT_Y}" fill="{c["panel2"]}"/>')
    p.append(f'  <rect x="0" y="{BOT_Y}" width="{W}" height="2" fill="{c["green"]}" opacity="0.6"/>')
    p.append(mono(f'x="28" y="{BOT_Y+26}" font-size="10" letter-spacing="1.2"', c["muted"],
                  "0x51 0x54 0x52 0x55 0x53 0x54 · 0x56 0x4F 0x4C 0x54 0x48 0x55 0x42 · 0x4B 0x2F 0x4F 0x53"))
    p.append(mono(f'x="{W-40}" y="{BOT_Y+26}" font-size="10" font-weight="700" letter-spacing="1.5" text-anchor="end"', c["green"],
                  "SELECT MISSION BELOW ▾"))

    # scanline overlay + edge rails
    p.append(scanlines(c, W, H, opacity="0.055"))
    p.append(f'  <rect x="0" y="0" width="3" height="{H}" fill="{c["green"]}" opacity="0.5"/>')
    p.append(f'  <rect x="{W-3}" y="0" width="3" height="{H}" fill="{c["green"]}" opacity="0.5"/>')

    alt = ("Operator console for Krishna Puri, systems engineer. Status online. "
           "Left panel: operator license with photo slot and an XP bar with five "
           "of six segments earned, the last deliberately open. Right panel: "
           "terminal with the working rule — trade-offs named, claims receipted, "
           "CI re-proves — and a status grid: VoltHub CI six jobs on both engines, "
           "Q-Trust CI eleven workflows, security audit and CodeQL gated, two docs "
           "sites, ten tagged releases, zero known CVEs.")
    body = "\n".join(p)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(alt)}">
<!-- {GENERATED_BY} -->
{body}
</svg>
"""


# ---------------------------------------------------------------------------
# BUILD EVERYTHING
# ---------------------------------------------------------------------------

SECTIONS = [
    ("00", "live telemetry", "CI status — live"),
    ("01", "missions", "flagship systems"),
    ("02", "loadout", "the stack, and why"),
    ("03", "achievements", "verified unlocks"),
    ("04", "datalog", "current focus"),
    ("05", "activity", "contribution grid"),
    ("06", "comms", "open channel"),
]

ACH_ITEMS = [
    ("FIRST CONTACT", "q-trust forked · 2026-08-30", DARK["cyan"], icon_fork),
    ("FORMAL PROOF", "Halmos symbolic runs in CI", DARK["violet"], icon_shield),
    ("SELF-TARGET", "PQC scanner scans its own repo", DARK["green"], icon_selfscan),
    ("RACE PROVEN", "double-book tests, 2 engines", DARK["amber"], icon_race),
    ("ZERO CVE", "npm audit gated, both lockfiles", DARK["green"], icon_gauge),
]


def write(path, svg):
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    kb = os.path.getsize(path) / 1024
    print(f"  {os.path.relpath(path, PACK):48s} {kb:7.1f} KB")
    import xml.dom.minidom as md
    md.parseString(svg)  # raises if malformed XML


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--photo", default=None, help="path to a square-ish portrait photo")
    ap.add_argument("--out", default=ASSETS, help="output directory")
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    photo = prepare_photo_b64(args.photo) if args.photo else None
    if photo:
        print(f"photo embedded: {len(photo)/1024:.1f} KB base64")

    print("building K/OS operator console assets:")
    write(os.path.join(args.out, "hero-console.svg"), hero(DARK, photo))
    write(os.path.join(args.out, "hero-console-light.svg"), hero(LIGHT, photo))

    for num, title, tag in SECTIONS:
        write(os.path.join(args.out, f"strip-{title.replace(' ', '-')}.svg"),
              section_strip(DARK, num, title, tag))

    write(os.path.join(args.out, "mission-volthub.svg"),
          mission_card(DARK, 1, "VOLTHUB CSMS",
                       "two-engine EV charging — Oracle money path + TimescaleDB telemetry + OCPP 1.6J",
                       "ACTIVE", "v1.4.0", "RACE CONDITIONS", "parallel bookings in CI, both engines", 4,
                       accent=DARK["green"]))
    write(os.path.join(args.out, "mission-qtrust.svg"),
          mission_card(DARK, 2, "Q-TRUST",
                       "post-quantum migration & attestation — CBOM scan · GNN planning · Base L2 seals",
                       "ACTIVE", "v2.2.1", "RSA-2048 / ECDSA AFTER 2030", "NIST IR 8547 timeline + self-scan", 5,
                       accent=DARK["violet"]))

    write(os.path.join(args.out, "achievements-strip.svg"),
          achievements_strip(DARK, ACH_ITEMS, pulse_last=True))
    print("done.")


if __name__ == "__main__":
    main()
