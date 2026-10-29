#!/usr/bin/env python3
"""Generate the site's vector art (logo, favicon, hero, per-post covers, og source) — stdlib only, deterministic.

  python3 scripts/make_art.py          # writes assets/*.svg (+ assets/og-source.svg for the PNG renderer)

Palette = Grace A direction of F-019 (minimal vector): sea teal, coral (me), indigo, mustard, plum, neutral grey.
"""
import math
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEA = ("#BFE3DC", "#8CCBC7")
FACTIONS = {"me": ("#F2685A", "#C94A3E"), "e1": ("#4B5BD3", "#3A47AE"), "e2": ("#E0B13A", "#B68A1F"),
            "e3": ("#9A4F95", "#783A74"), "n": ("#D5D0C6", "#B8B1A5")}
COVERS = {  # slug: (seed, islands, factions in play)
    "why-island-conquest": (11, 9, ("me", "n", "n", "e1")),
    "the-rules-on-one-page": (23, 7, ("me", "e1", "n")),
    "naming-inkisle": (37, 6, ("me", "n")),
    "art-direction-grace-vs-gpt": (41, 8, ("me", "e1", "e2", "n")),
    "a-playable-prototype-in-a-day": (53, 10, ("me", "e1", "e2", "n", "n")),
    "tuning-the-difficulty": (67, 9, ("me", "e1", "e3", "n")),
    "three-rewrites-of-multi-island-attack": (79, 9, ("me", "me", "e1", "n")),
    "three-ten-second-intros": (83, 8, ("me", "e1", "n")),
    "ink-that-spreads": (89, 9, ("me", "me", "e2", "n")),
    "sound-off-by-default": (97, 7, ("me", "e1", "n")),
    "a-drag-that-forgives": (101, 8, ("me", "e3", "n")),
    "three-stars-one-rule": (103, 7, ("me", "e2", "n")),
    "when-saved-data-breaks": (107, 8, ("me", "e1", "e3", "n")),
    "what-the-app-does-not-have": (109, 6, ("me", "n")),
}


def blob(rng, cx, cy, r, pts=9):
    """closed smooth path around (cx, cy) — Catmull-Rom to cubic Bezier."""
    ang = [2 * math.pi * i / pts + rng.uniform(-.15, .15) for i in range(pts)]
    P = [(cx + math.cos(a) * r * rng.uniform(.78, 1.12), cy + math.sin(a) * r * rng.uniform(.78, 1.12)) for a in ang]
    d = "M%.1f %.1f" % P[0]
    for i in range(pts):
        p0, p1, p2, p3 = P[i - 1], P[i], P[(i + 1) % pts], P[(i + 2) % pts]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += "C%.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + p2)
    return d + "Z"


def scene(w, h, seed, n, facs, labels=True, pad=70):
    rng = random.Random(seed)
    islands = []
    tries = 0
    while len(islands) < n and tries < 4000:
        tries += 1
        r = rng.uniform(26, 52) * (w / 640)
        x, y = rng.uniform(pad, w - pad), rng.uniform(pad, h - pad)
        if all(math.hypot(x - a, y - b) > r + rr + 14 for a, b, rr, _ in islands):
            islands.append((x, y, r, rng.choice(facs)))
    islands[0] = (islands[0][0], islands[0][1], islands[0][2], "me")
    o = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-hidden="true">' % (w, h, w, h),
         '<defs><linearGradient id="s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="%s"/><stop offset="1" stop-color="%s"/></linearGradient></defs>' % SEA,
         '<rect width="%d" height="%d" fill="url(#s)"/>' % (w, h)]
    for k in range(3):
        y0 = h * (.2 + .3 * k)
        o.append('<path d="M0 %.0f Q%.0f %.0f %.0f %.0f T%d %.0f" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2" stroke-dasharray="3 12" stroke-linecap="round"/>'
                 % (y0, w / 4, y0 - 14, w / 2, y0, w, y0 + 6))
    # routes: each island to its nearest neighbour; fleet dot in the owner's colour
    for i, (x, y, r, f) in enumerate(islands):
        near = min((m for m in range(len(islands)) if m != i), key=lambda m: math.hypot(islands[m][0] - x, islands[m][1] - y))
        x2, y2, _, _ = islands[near]
        if f != "n":
            o.append('<path d="M%.0f %.0f L%.0f %.0f" stroke="%s" stroke-width="3" stroke-dasharray="1 9" stroke-linecap="round" opacity=".85"/>' % (x, y, x2, y2, FACTIONS[f][0]))
            t = rng.uniform(.3, .6)
            o.append('<circle cx="%.0f" cy="%.0f" r="5" fill="%s" stroke="#fff" stroke-width="2"/>' % (x + (x2 - x) * t, y + (y2 - y) * t, FACTIONS[f][0]))
    for x, y, r, f in islands:
        top, edge = FACTIONS[f]
        o.append('<path d="%s" fill="#000" opacity=".12" transform="translate(3 6)"/>' % blob(random.Random(int(x * 7 + y)), x, y, r))
        o.append('<path d="%s" fill="#F3EBDD"/>' % blob(random.Random(int(x * 7 + y)), x, y, r))
        o.append('<path d="%s" fill="%s"/>' % (blob(random.Random(int(x * 5 + y * 3)), x, y, r * .74), top))
        if labels:
            o.append('<text x="%.0f" y="%.0f" text-anchor="middle" font-family="system-ui,sans-serif" font-weight="800" font-size="%d" fill="#fff">%d</text>'
                     % (x, y + r * .17, max(12, int(r * .5)), rng.randint(4, 28)))
    o.append("</svg>")
    return "\n".join(o) + "\n"


LOGO = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="48" height="48"><path d="M7 31c-2-9 5-18 15-19 9-1 18 5 19 14 1 8-7 13-16 13-8 0-16-1-18-8z" fill="#F3EBDD"/>'
        '<path d="M15 30c-1-6 3-12 10-12 6 0 11 4 10 10-1 6-7 8-12 8-4 0-7-1-8-6z" fill="#F2685A"/><circle cx="38" cy="10" r="4.2" fill="#F2685A"/><circle cx="31" cy="6" r="2" fill="#F2685A" opacity=".6"/></svg>\n')


def main():
    a = ROOT / "assets"
    (a / "posts").mkdir(parents=True, exist_ok=True)
    (a / "logo.svg").write_text(LOGO, encoding="utf-8")
    (a / "favicon.svg").write_text(LOGO.replace('viewBox="0 0 48 48"', 'viewBox="0 0 48 48"').replace("<path", '<rect width="48" height="48" rx="11" fill="#BFE3DC"/><path', 1), encoding="utf-8")
    (a / "hero.svg").write_text(scene(640, 720, 5, 9, ("me", "e1", "e2", "n", "n")), encoding="utf-8")
    for slug, (seed, n, facs) in COVERS.items():
        (a / "posts" / (slug + ".svg")).write_text(scene(640, 360, seed, n, facs), encoding="utf-8")
    og = scene(1200, 630, 101, 12, ("me", "e1", "e2", "n", "n"), pad=80)
    og = og.replace("</svg>", '<rect x="0" y="0" width="1200" height="630" fill="#14262B" opacity=".0"/>'
                    '<g font-family="system-ui,-apple-system,sans-serif"><rect x="60" y="210" width="560" height="210" rx="28" fill="#14262B" opacity=".86"/>'
                    '<text x="96" y="305" font-size="76" font-weight="800" fill="#fff">InkIsle</text>'
                    '<text x="96" y="360" font-size="30" fill="#BFE3DC">Tint the sea, take the isles</text>'
                    '<text x="96" y="398" font-size="22" fill="#9BB0B3">inkisle.ipe.rest · an ipe() game</text></g></svg>')
    (a / "og-source.svg").write_text(og, encoding="utf-8")
    print("art: wrote logo, favicon, hero, %d covers, og-source" % len(COVERS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
