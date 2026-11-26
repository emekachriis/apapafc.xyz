#!/usr/bin/env python3
"""
Build site/index.html from scripts/site_template.html and the REAL sample workbook values.

  python3 scripts/build_site.py

Reads workbook/sample-rental-books-2026.xlsx (cached values: run the recalc step after
rebuilding the workbook), draws six inline-SVG crops of it plus the worked Bank tie-out
example, writes site/index.html, and prints a contrast report for the palette.
Then run `node scripts/site_assets.js` for the favicon PNGs and the OG image.
"""
from html import escape
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "workbook" / "sample-rental-books-2026.xlsx"
TEMPLATE = ROOT / "scripts" / "site_template.html"
OUT = ROOT / "site" / "index.html"

GROUND, CREAM, PEACH, SKY, MID, INK = "#0a2e0e", "#faf5e8", "#fcab79", "#c7e5f2", "#214224", "#181d26"
INK_MUTED, CREAM_MUTED = "#4f5560", "#b8c6b4"


# ---------- helpers ----------------------------------------------------------------------
def money(v, dash=True):
    if v is None or (dash and abs(v) < 0.005):
        return "-"
    s = f"${abs(v):,.2f}"
    return f"({s})" if v < 0 else s


def tw(text, size):
    """Rough text width for Plus Jakarta Sans (used only to size pills and keep marks clear)."""
    return len(text) * size * 0.56


def wb_values():
    return load_workbook(XLSX, data_only=True)


def find_row(ws, col, value, start=1):
    for r in range(start, ws.max_row + 1):
        if ws.cell(r, col).value == value:
            return r
    raise KeyError(value)


# ---------- SVG sheet crop -------------------------------------------------------------------
class Crop:
    """A window onto one sheet: columns may start left of 0 and run past the right edge."""

    def __init__(self, x0, cols, rail=False, w=360, h=200):
        self.w, self.h, self.rail = w, h, rail
        self.cols = []
        x = x0
        for name, width, align in cols:
            self.cols.append((name, x, width, align))
            x += width
        self.parts, self.y = [], 0
        self.mark = None

    def _cell_text(self, ci, y, rh, text, size=12, weight=400, fill=INK):
        _, x, w, align = self.cols[ci]
        if text in (None, ""):
            return
        t = escape(str(text))
        if align == "r":
            tx, anchor = w - 8, "end"
        elif align == "c":
            tx, anchor = w / 2, "middle"
        else:
            tx, anchor = 8, "start"
        # nested svg = clip to the cell, like a spreadsheet cell with a neighbour
        self.parts.append(
            f'<svg x="{x}" y="{y}" width="{w}" height="{rh}"><text x="{tx}" y="{rh / 2 + size * 0.36:.1f}" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{t}</text></svg>')

    def band(self, text_cells, rh=30):
        """A row above the table, e.g. 'Property: Maple Duplex'."""
        for ci, text, weight in text_cells:
            _, x, w, _ = self.cols[ci]
            self.parts.append(f'<text x="{x + 8}" y="{self.y + rh / 2 + 4.3:.1f}" font-size="12" '
                              f'font-weight="{weight}" fill="{INK}">{escape(text)}</text>')
        self.y += rh

    def header(self, rh=36):
        y = self.y
        self.parts.append(f'<rect x="0" y="{y}" width="{self.w}" height="{rh}" fill="{MID}" fill-opacity=".05"/>')
        for ci, (name, x, w, align) in enumerate(self.cols):
            lines = name.split("\n")
            tx = {"r": w - 8, "c": w / 2}.get(align, 8)
            anchor = {"r": "end", "c": "middle"}.get(align, "start")
            y0 = rh / 2 - (len(lines) - 1) * 6.5 + 3.8
            spans = "".join(f'<tspan x="{tx}" y="{y0 + i * 13:.1f}">{escape(l)}</tspan>' for i, l in enumerate(lines))
            self.parts.append(f'<svg x="{x}" y="{y}" width="{w}" height="{rh}"><text font-size="11" '
                              f'font-weight="500" fill="{INK}" text-anchor="{anchor}">{spans}</text></svg>')
        self.y += rh

    def row(self, cells, rh=30, mark_col=None, mark_dx=None):
        y = self.y
        for ci, c in enumerate(cells):
            if isinstance(c, dict):  # pill
                _, x, w, _ = self.cols[ci]
                pw = tw(c["text"], 11) + 16
                fill, tfill, stroke = {"ok": (SKY, INK, "none"), "flag": (MID, CREAM, "none"),
                                       "miss": (CREAM, INK, INK)}[c["kind"]]
                self.parts.append(
                    f'<svg x="{x}" y="{y}" width="{w}" height="{rh}"><rect x="8" y="{rh / 2 - 9}" width="{pw:.0f}" '
                    f'height="18" rx="9" fill="{fill}" stroke="{stroke}"/><text x="{8 + pw / 2:.1f}" '
                    f'y="{rh / 2 + 3.9:.1f}" font-size="11" fill="{tfill}" text-anchor="middle">'
                    f'{escape(c["text"])}</text></svg>')
            else:
                self._cell_text(ci, y, rh, c)
        if mark_col is not None:
            _, x, w, _ = self.cols[mark_col]
            self.mark = (x + mark_dx, y + rh / 2)
        self.y += rh

    def svg(self, label):
        g = []
        # grid: horizontal lines at every row boundary drawn so far, vertical at column edges
        g.append(f'<g stroke="{MID}" stroke-opacity=".18" stroke-width="1" shape-rendering="crispEdges">')
        for _, x, w, _ in self.cols:
            if 0 < x < self.w:
                g.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{self.h}"/>')
        g.append("</g>")
        lines = self._hlines
        body = "".join(g) + "".join(lines) + "".join(self.parts)
        if self.rail:
            body += f'<rect x="0" y="0" width="4" height="{self.h}" fill="{MID}"/>'
        if self.mark:
            cx, cy = self.mark
            assert 13 < cx < self.w - 20, f"mark off tile: {label}"
            body += (f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="13" fill="{PEACH}" stroke="{INK}" stroke-width="1"/>')
        return (f'<svg viewBox="0 0 {self.w} {self.h}" preserveAspectRatio="xMinYMin slice" role="img" '
                f'aria-label="{escape(label)}" font-family="Plus Jakarta Sans, Arial, sans-serif">{body}</svg>')

    @property
    def _hlines(self):
        return [f'<line x1="0" y1="{y}" x2="{self.w}" y2="{y}" stroke="{MID}" stroke-opacity=".18" '
                f'shape-rendering="crispEdges"/>' for y in self._rows]



# ---------- the six tiles ---------------------------------------------------------------------
def tiles(wb):
    L = wb["Ledger – Maple Duplex"]
    lr = {L.cell(r, 1).value: r for r in range(9, 21)}
    months = ["Jan 2026", "Feb 2026", "Mar 2026", "Apr 2026", "May 2026", "Jun 2026"]
    out = []

    # 1. Ledger, left edge -- mark on Gross rent, March
    c = Crop(4, [("Month", 76, "l"), ("Statement\nreceived", 70, "c"), ("Gross rent\ncollected", 120, "r"),
                 ("PM management\nfee", 120, "r")], rail=True)
    c._rows = [0]
    c.band([(0, "Property", 500), (1, "Maple Duplex", 400)]); c._rows.append(c.y)
    c.header(); c._rows.append(c.y)
    for m in months:
        r = lr[m]
        c.row([m, L.cell(r, 2).value, money(L.cell(r, 3).value), money(L.cell(r, 4).value)],
              mark_col=2 if m == "Mar 2026" else None, mark_dx=22)
        c._rows.append(c.y)
    out.append(("Gross rent, before your PM took anything", "Ledger", c.svg("Ledger crop: gross rent column")))

    # 2. Ledger, middle columns -- mark on management fee, March
    c = Crop(-56, [("Gross rent\ncollected", 120, "r"), ("PM management\nfee", 116, "r"), ("Leasing fee", 92, "r"),
                   ("Repairs", 100, "r"), ("Other PM\ncharges", 100, "r")])
    c._rows = [0]
    c.header(); c._rows.append(c.y)
    for m in months:
        r = lr[m]
        c.row([money(L.cell(r, k).value) for k in (3, 4, 5, 6, 7)],
              mark_col=1 if m == "Mar 2026" else None, mark_dx=22)
        c._rows.append(c.y)
    out.append(("Every fee on its own line", "Ledger", c.svg("Ledger crop: fee columns")))

    # 3. Schedule E map, category column -- mark on Repairs line total (Maple Duplex)
    S = wb["Schedule E map"]
    c = Crop(4, [("Line", 38, "c"), ("Schedule E line name (2026)", 176, "l"), ("Maple Duplex\nline total", 120, "r"),
                 ("Birch House\nfrom PM", 110, "r")], rail=True)
    c._rows = [0]
    c.header(); c._rows.append(c.y)
    for ln in ["11", "12", "13a", "13b", "14", "15"]:
        r = find_row(S, 1, ln, 10)
        c.row([ln, S.cell(r, 2).value, money(S.cell(r, 6).value), money(S.cell(r, 7).value)],
              mark_col=2 if ln == "14" else None, mark_dx=22)
        c._rows.append(c.y)
    out.append(("Totals sorted into Schedule E lines", "Sched E", c.svg("Schedule E map crop: line totals")))

    # 4. Bank tie-out, difference column -- mark on the non-zero difference
    T = wb["Bank tie-out"]
    first = find_row(T, 1, "Jan 2026")
    c = Crop(-52, [("Bank deposit(s)\nfrom PM", 118, "r"), ("Difference\n(PM - bank)", 118, "r"), ("Status", 96, "l"),
                   ("Exception # /\nnote", 110, "l")])
    c._rows = [0]
    c.header(); c._rows.append(c.y)
    for i in range(4, 10):  # May..Oct
        r = first + i
        d = T.cell(r, 5).value
        pill = {"kind": "flag", "text": "Flagged"} if abs(d) > 0.004 else {"kind": "ok", "text": "Matched"}
        c.row([money(T.cell(r, 3).value), money(d), pill, T.cell(r, 6).value],
              mark_col=1 if abs(d) > 0.004 else None, mark_dx=22)
        c._rows.append(c.y)
    out.append(("Deposits matched to your bank, month by month", "Tie-out", c.svg("Bank tie-out crop: differences")))

    # 5. Exceptions, first rows -- mark on the first exception row
    E = wb["Exceptions"]
    c = Crop(4, [("#", 48, "l"), ("Type", 126, "l"), ("Property", 98, "l"), ("Month", 70, "l"), ("Amount", 100, "r")],
             rail=True)
    c._rows = [0]
    c.header(); c._rows.append(c.y)
    for r in range(6, 11):
        v = [E.cell(r, k).value for k in range(1, 6)]
        c.row([v[0], v[1], v[2], v[3], money(v[4]) if v[4] is not None else ""], rh=30,
              mark_col=0 if r == 6 else None, mark_dx=31)
        c._rows.append(c.y)
    out.append(("A short list of questions for your CPA", "Exceptions", c.svg("Exceptions crop: first rows")))

    # 6. Contractors -- mark on the payee flagged at $2,000 or more
    C = wb["Contractors"]
    c = Crop(-40, [("Paid by\n(PM or owner)", 112, "l"), ("Total paid\nin 2026", 104, "r"),
                   ("At or above\nthreshold?", 166, "l"), ("W-9 / TIN\non file?", 90, "l")])
    c._rows = [0]
    c.header(); c._rows.append(c.y)
    for r in range(10, 15):
        tot = C.cell(r, 5).value
        flag = C.cell(r, 6).value or ""
        pill = ({"kind": "flag", "text": "YES: review for 1099-NEC"} if flag.startswith("YES")
                else ({"kind": "ok", "text": "No"} if flag else ""))
        c.row([C.cell(r, 4).value, money(tot) if tot else "", pill, C.cell(r, 7).value],
              mark_col=1 if flag.startswith("YES") else None, mark_dx=22)
        c._rows.append(c.y)
    out.append(("Contractors who may need a 1099", "Contractors", c.svg("Contractors crop: 1099 flag")))

    html = []
    for title, ref, svg in out:
        html.append(f'    <li class="tile"><div class="win">{svg}</div>'
                    f'<div class="cap"><span>{escape(title)}</span><span class="mono">{ref}</span></div></li>')
    return "\n".join(html)


# ---------- worked example ----------------------------------------------------------------
def worked(wb):
    T = wb["Bank tie-out"]
    first = find_row(T, 1, "Jan 2026")
    rows = []
    for i in range(4, 9):  # May..Sep, Maple Duplex block
        r = first + i
        rows.append((T.cell(r, 1).value, T.cell(r, 2).value, T.cell(r, 3).value, T.cell(r, 5).value))
    flagged = [i for i, x in enumerate(rows) if abs(x[3]) > 0.004]
    assert flagged == [2], "worked example expects exactly one flagged month in the middle (Jul)"
    up_h = 11 + 2 * 48 + 44 + 42 + 12    # disc top -> top-band label bottom (2 rows, header, tabs, gap)
    down_h = (48 - 37) + 2 * 48 + 12     # disc bottom -> bottom-band label top (rest of row, 2 rows, gap)

    def mk(n, direction, h):
        return (f'<span class="cn {direction}" style="height:{h}px" aria-hidden="true"></span>'
                f'<span class="mk" aria-hidden="true">{n}</span>')

    labels = {1: "We take this from your PM statement", 2: "We match it to this deposit",
              3: "We flag this for your CPA"}
    h = ['  <div class="panel sheet" role="img" aria-label="Bank tie-out sheet for Maple Duplex, May to September 2026, '
         'with July flagged: PM net payout $1,932.50, bank deposit $2,282.50, difference ($350.00).">',
         '    <div class="rail"></div><div class="sheetbody">',
         f'      <div class="g band top"><div class="lab" style="grid-column:4"><span>{labels[3]}</span></div></div>',
         '      <div class="tabs"><span>Summary</span><span>Ledger</span><span>Sched E</span>'
         '<span class="on">Tie-out</span><span>Exceptions</span><span>Contractors</span></div>',
         '      <div class="g row head"><div>Month</div><div>PM net payout</div><div>Bank deposit</div>'
         '<div>Difference</div><div class="st">Status</div></div>']
    for i, (m, pm, bank, d) in enumerate(rows):
        mon, yr = m.split()
        is_f = i in flagged
        pill = ('<span class="pill flag">Flagged</span>' if is_f else '<span class="pill ok">Matched</span>')
        c1 = (mk(1, "down", down_h) if is_f else "") + money(pm, dash=False)
        c2 = (mk(2, "down", down_h) if is_f else "") + money(bank, dash=False)
        c3 = (mk(3, "up", up_h) if is_f else "") + money(d)
        h.append(f'      <div class="g row"><div>{mon}<span class="yr">&nbsp;{yr}</span></div><div>{c1}</div>'
                 f'<div>{c2}</div><div>{c3}</div><div class="st">{pill}</div></div>')
    h += [f'      <div class="g band bottom"><div class="lab" style="grid-column:2"><span>{labels[1]}</span></div>'
          f'<div class="lab" style="grid-column:3"><span>{labels[2]}</span></div></div>',
          '    </div>', '  </div>',
          '  <ol class="steps-list">' + "".join(f'<li><span class="n">{n}</span><span>{labels[n]}</span></li>'
                                              for n in (1, 2, 3)) + '</ol>']
    return "\n".join(h)


# ---------- contrast ------------------------------------------------------------------------------
def lum(hexc):
    c = [int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def ratio(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True)
    return (la + 0.05) / (lb + 0.05)


def contrast_report():
    pairs = [("cream text on ground", CREAM, GROUND), ("muted cream on ground", CREAM_MUTED, GROUND),
             ("ink on cream", INK, CREAM), ("muted ink on cream", INK_MUTED, CREAM),
             ("ink on peach (CTA)", INK, PEACH), ("ink on sky pill", INK, SKY),
             ("cream on mid-green pill", CREAM, MID), ("peach mark vs cream (needs ink ring)", PEACH, CREAM),
             ("ink ring vs cream", INK, CREAM)]
    print("contrast:")
    for name, a, b in pairs:
        r = ratio(a, b)
        flag = "" if r >= 4.5 or "mark" in name else "  <-- below 4.5"
        print(f"  {name:40s} {r:5.2f}:1{flag}")


def main():
    wb = wb_values()
    page = TEMPLATE.read_text(encoding="utf-8")
    page = page.replace("<!--TILES-->", tiles(wb)).replace("<!--WORKED-->", worked(wb))
    OUT.write_text(page, encoding="utf-8")
    print("wrote", OUT.relative_to(ROOT), f"({len(page) // 1024} KB)")
    contrast_report()


if __name__ == "__main__":
    main()
