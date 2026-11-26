#!/usr/bin/env python3
"""
Year-End Rental Books: workbook generator.

Builds two files in this folder (or --out-dir):
  sample-rental-books-2026.xlsx    fictional owner, 2 properties, 2 PMs, 12 months
  template-rental-books-2026.xlsx  same structure, empty, ready to fill per client

Per-client template with your own property names:
  python3 build_workbook.py --template-only --properties "Oak St Duplex" "Elm Ave House" "Pine Ct"

Every total is a live Excel formula. Inputs are blue text (and yellow cells in the
template). Recalculate and check with LibreOffice afterwards (see README.md).

Bookkeeping prepared for your CPA. Not tax advice, tax preparation or tax filing.
"""
import argparse
from pathlib import Path

from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.pagebreak import Break

YEAR = "2026"
MONTHS = [f"{m} {YEAR}" for m in
          ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]]

DISCLAIMER = ("Bookkeeping prepared for your CPA. This workbook is NOT tax advice, tax preparation "
              "or tax filing. Amounts are compiled from the property manager statements and bank "
              "export supplied by the owner and have not been audited. Your CPA decides how every "
              "item is reported.")
DISCLAIMER_SHORT = "Bookkeeping prepared for your CPA. Not tax advice, tax preparation or tax filing."

# --- Verified sources (checked 26 Nov 2026) ---------------------------------------------
SCHED_E_SRC = "https://www.irs.gov/pub/irs-dft/f1040se--dft.pdf"
SCHED_E_SRC_NOTE = (
    "Line numbers and names taken from the IRS 2026 Schedule E (Form 1040) early-release "
    "DRAFT, created 5/6/26: " + SCHED_E_SRC + " . Cross-checked against the final 2025 form "
    "(https://www.irs.gov/pub/irs-pdf/f1040se.pdf): identical for lines 3-20 except that 2026 "
    "splits line 13 into 13a Vehicle loan and 13b Other. Re-check against the final 2026 form "
    "before delivery: https://www.irs.gov/forms-pubs/about-schedule-e-form-1040")
NEC_SRC = "https://www.irs.gov/instructions/i1099mec"
NEC_SRC_NOTE = (
    "IRS Instructions for Forms 1099-MISC and 1099-NEC (Rev. 12/2026), What's New: for tax years "
    "beginning after 2025 the minimum reporting threshold increased to $2,000 and may be adjusted "
    "for inflation beginning in calendar year 2027. " + NEC_SRC + " . Secondary: "
    "https://www.patriotsoftware.com/blog/accounting/1099-reporting-threshold/")

# Schedule E lines (2026 draft). source: key of a ledger total column, or None.
# Ledger columns: C gross rent, D mgmt fee, E leasing fee, F repairs, G other PM charges.
SCHED_E_LINES = [
    ("3", "Rents received", "C", "Gross rent collected (Ledger)"),
    ("4", "Royalties received", None, "Not applicable to rental-only clients"),
    ("5", "Advertising", None, ""),
    ("6", "Auto and travel (see instructions)", None, ""),
    ("7", "Cleaning and maintenance", None, ""),
    ("8", "Commissions", "E", "Leasing fees (Ledger). CPA to confirm line and timing"),
    ("9", "Insurance", None, ""),
    ("10", "Legal and other professional fees", None, ""),
    ("11", "Management fees", "D", "PM management fees (Ledger)"),
    ("12", "Mortgage interest paid to banks, etc. (see instructions)", None,
     "Not in PM statements. CPA to supply from Form 1098"),
    ("13a", "Interest (see instructions): Vehicle loan", None, ""),
    ("13b", "Interest (see instructions): Other", None, ""),
    ("14", "Repairs", "F", "Repairs (Ledger)"),
    ("15", "Supplies", None, ""),
    ("16", "Taxes", None, ""),
    ("17", "Utilities", None, ""),
    ("18", "Depreciation expense or depletion", None,
     "Not in PM statements. CPA to supply from depreciation schedule"),
    ("19", "Other (list)", "G", "Other PM charges (Ledger, see descriptions and Exceptions)"),
]

# --- Styles ------------------------------------------------------------------------------
F = "Arial"
NAVY = "1F3A5F"
f_base = Font(name=F, size=10)
f_bold = Font(name=F, size=10, bold=True)
f_title = Font(name=F, size=14, bold=True, color=NAVY)
f_sample = Font(name=F, size=11, bold=True, color="C00000")
f_small = Font(name=F, size=9, italic=True, color="555555")
f_head = Font(name=F, size=10, bold=True, color="FFFFFF")
f_input = Font(name=F, size=10, color="0000FF")
fill_head = PatternFill("solid", fgColor=NAVY)
fill_total = PatternFill("solid", fgColor="E8EDF3")
fill_input = PatternFill("solid", fgColor="FFF2CC")
fill_red = PatternFill("solid", fgColor="F8CBAD")
thin = Side(style="thin", color="B7C3D0")
box = Border(left=thin, right=thin, top=thin, bottom=thin)
top2 = Border(top=Side(style="medium", color=NAVY), bottom=thin, left=thin, right=thin)
CUR = '$#,##0.00;($#,##0.00);"-"'
wrap = Alignment(wrap_text=True, vertical="top")
center = Alignment(horizontal="center", vertical="center", wrap_text=True)


class Ctx:
    def __init__(self, sample):
        self.sample = sample


def q(sheet_name):
    return "'" + sheet_name.replace("'", "''") + "'"


def header(ws, ctx, title, ncols):
    ws["A1"] = f"Year-End Rental Books {YEAR}: {title}"
    ws["A1"].font = f_title
    if ctx.sample:
        ws["A2"] = "SAMPLE: fictional data. Not a real owner, property, manager or bank account."
        ws["A2"].font = f_sample
    else:
        ws["A2"] = "TEMPLATE: enter client data in the yellow cells. Everything else is a formula."
        ws["A2"].font = Font(name=F, size=11, bold=True, color="7F6000")
    ws["A3"] = DISCLAIMER_SHORT
    ws["A3"].font = f_small
    for r in (1, 2, 3):
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=ncols)
    ws.row_dimensions[1].height = 22


def print_setup(ws, title_rows):
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_options.horizontalCentered = True
    ws.page_margins.left = ws.page_margins.right = 0.4
    ws.page_margins.top = ws.page_margins.bottom = 0.6
    ws.print_title_rows = title_rows
    ws.oddFooter.left.text = DISCLAIMER_SHORT
    ws.oddFooter.left.size = 8
    ws.oddFooter.right.text = "&A  |  Page &P of &N"
    ws.oddFooter.right.size = 8
    ws.sheet_view.showGridLines = False


def head_row(ws, row, labels):
    for i, lab in enumerate(labels, 1):
        c = ws.cell(row=row, column=i, value=lab)
        c.font, c.fill, c.alignment, c.border = f_head, fill_head, center, box
    ws.row_dimensions[row].height = 44


def inp(cell, ctx, value=None, fmt=None):
    """Mark a cell as an input: blue text; yellow fill in the template."""
    if value is not None:
        cell.value = value
    cell.font = f_input
    if not ctx.sample:
        cell.fill = fill_input
    cell.border = box
    if fmt:
        cell.number_format = fmt


def widths(ws, ws_widths):
    for i, w in enumerate(ws_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


# --- Ledger --------------------------------------------------------------------------------
L_FIRST, L_LAST, L_TOTAL = 9, 20, 21   # month rows and total row on each ledger


def build_ledger(wb, ctx, prop):
    ws = wb.create_sheet(prop["sheet"])
    header(ws, ctx, "Ledger", 11)
    labels = [("A5", "Property:", "B5", prop.get("name")), ("A6", "Address / ID:", "B6", prop.get("address")),
              ("F5", "Property manager:", "H5", prop.get("pm")), ("F6", "Statement format:", "H6", prop.get("fmt"))]
    for lc, lt, vc, v in labels:
        ws[lc] = lt
        ws[lc].font = f_bold
        inp(ws[vc], ctx, v if ctx.sample else None)
    ws.merge_cells("B5:E5"); ws.merge_cells("B6:E6"); ws.merge_cells("F5:G5"); ws.merge_cells("F6:G6")
    ws.merge_cells("H5:J5"); ws.merge_cells("H6:J6")
    if not ctx.sample:
        ws["B5"] = prop["name"]
    ws["A7"] = ("Gross rent and every fee are entered separately, exactly as the PM statement shows them. "
                "Never enter a netted amount. Reserve held (+) or released (-) is not an expense.")
    ws["A7"].font = f_small
    ws.merge_cells("A7:K7")

    head_row(ws, 8, ["Month", "Statement received (Y/N)", "Gross rent collected", "PM management fee",
                     "Leasing fee", "Repairs", "Other PM charges", "Other charge description",
                     "Reserve held (+) / released (-)", "Net owner distribution", "Notes / statement ref"])
    dv = DataValidation(type="list", formula1='"Y,N"', allow_blank=True)
    ws.add_data_validation(dv)
    data = prop.get("months") or [{} for _ in MONTHS]
    for i, m in enumerate(MONTHS):
        r = L_FIRST + i
        d = data[i]
        ws.cell(r, 1, m).font = f_base
        ws.cell(r, 1).border = box
        dv.add(ws.cell(r, 2))
        inp(ws.cell(r, 2), ctx, d.get("recv"))
        ws.cell(r, 2).alignment = Alignment(horizontal="center")
        for col, key in zip("CDEFG", ["rent", "mgmt", "leasing", "repairs", "other"]):
            inp(ws[f"{col}{r}"], ctx, d.get(key), CUR)
        inp(ws[f"H{r}"], ctx, d.get("other_desc"))
        inp(ws[f"I{r}"], ctx, d.get("reserve"), CUR)
        ws[f"J{r}"] = f"=C{r}-D{r}-E{r}-F{r}-G{r}-I{r}"
        ws[f"J{r}"].number_format, ws[f"J{r}"].font, ws[f"J{r}"].border = CUR, f_bold, box
        inp(ws[f"K{r}"], ctx, d.get("note"))
        ws[f"H{r}"].alignment = ws[f"K{r}"].alignment = Alignment(wrap_text=True, vertical="top")
    t = L_TOTAL
    ws[f"A{t}"] = f"Total {YEAR}"
    ws[f"B{t}"] = f'=COUNTIF(B{L_FIRST}:B{L_LAST},"Y")'
    ws[f"B{t}"].number_format = '0" of 12"'
    for col in "CDEFGIJ":
        ws[f"{col}{t}"] = f"=SUM({col}{L_FIRST}:{col}{L_LAST})"
        ws[f"{col}{t}"].number_format = CUR
    for col in "ABCDEFGHIJK":
        c = ws[f"{col}{t}"]
        c.font, c.fill, c.border = f_bold, fill_total, top2
    ws[f"B{t}"].alignment = Alignment(horizontal="center")
    # Missing statement highlight
    ws.conditional_formatting.add(f"A{L_FIRST}:B{L_LAST}",
                                  FormulaRule(formula=[f'$B{L_FIRST}="N"'], fill=fill_red))
    widths(ws, [11, 11, 14, 13, 11, 12, 12, 26, 13, 15, 38])
    ws.freeze_panes = "B9"
    print_setup(ws, "8:8")
    return ws


# --- Bank tie-out ---------------------------------------------------------------------------
def build_tieout(wb, ctx, props):
    ws = wb.create_sheet("Bank tie-out")
    header(ws, ctx, "Bank tie-out", 6)
    ws["A5"] = ("PM net owner distribution for each month (from the Ledger) against the matching deposit(s) "
                "in the owner's bank export. Difference = PM net minus bank. Any non-zero difference is "
                "shaded and must have an entry on the Exceptions sheet.")
    ws["A5"].font, ws["A5"].alignment = f_small, wrap
    ws.merge_cells("A5:F5"); ws.row_dimensions[5].height = 28
    ws["A6"] = "Total unreconciled difference, all properties:"
    ws["A6"].font = f_bold
    ws.merge_cells("A6:D6")
    row = 8
    total_cells = []
    for p in props:
        sh = q(p["sheet"])
        ws.cell(row, 1, f'={sh}!B5&"  |  PM: "&{sh}!H5').font = Font(name=F, size=11, bold=True, color=NAVY)
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=6)
        row += 1
        head_row(ws, row, ["Month", "PM net owner distribution (Ledger)", "Bank deposit(s) from PM",
                           "Deposit date(s) / bank memo", "Difference (PM - bank)", "Exception # / note"])
        row += 1
        first = row
        bank = p.get("bank") or [{} for _ in MONTHS]
        for i, m in enumerate(MONTHS):
            ws.cell(row, 1, m).border = box
            ws[f"B{row}"] = f"={sh}!J{L_FIRST + i}"
            ws[f"B{row}"].number_format = CUR
            ws[f"B{row}"].border = box
            inp(ws[f"C{row}"], ctx, bank[i].get("amt"), CUR)
            inp(ws[f"D{row}"], ctx, bank[i].get("memo"))
            ws[f"E{row}"] = f"=ROUND(B{row}-C{row},2)"
            ws[f"E{row}"].number_format, ws[f"E{row}"].font, ws[f"E{row}"].border = CUR, f_bold, box
            inp(ws[f"F{row}"], ctx, bank[i].get("note"))
            row += 1
        last = row - 1
        ws.cell(row, 1, "Total")
        for col in "BCE":
            ws[f"{col}{row}"] = f"=SUM({col}{first}:{col}{last})"
            ws[f"{col}{row}"].number_format = CUR
        for col in "ABCDEF":
            c = ws[f"{col}{row}"]
            c.font, c.fill, c.border = f_bold, fill_total, top2
        ws.conditional_formatting.add(f"E{first}:E{row}",
                                      FormulaRule(formula=[f"ABS(E{first})>0.004"], fill=fill_red,
                                                  font=Font(name=F, bold=True, color="9C0006")))
        total_cells.append(f"E{row}")
        ws.row_breaks.append(Break(id=row + 1))
        row += 3
    ws["E6"] = "=" + "+".join(total_cells)
    ws["E6"].number_format, ws["E6"].font, ws["E6"].border = CUR, f_bold, box
    ws.conditional_formatting.add("E6", FormulaRule(formula=["ABS(E6)>0.004"], fill=fill_red,
                                                    font=Font(name=F, bold=True, color="9C0006")))
    widths(ws, [12, 20, 18, 40, 18, 30])
    ws.freeze_panes = "A8"
    print_setup(ws, "1:3")
    return ws, total_cells


# --- Exceptions ----------------------------------------------------------------------------
EXC_FIRST, EXC_ROWS = 6, 15


def build_exceptions(wb, ctx, exceptions):
    ws = wb.create_sheet("Exceptions")
    header(ws, ctx, "Exceptions for CPA review", 8)
    head_row(ws, 5, ["#", "Type", "Property", "Month", "Amount", "What we found",
                     "What the CPA / owner should check", "Status"])
    dv_t = DataValidation(type="list", allow_blank=True,
                          formula1='"Unmatched deposit,Missing month,Unclassified charge,Owner-paid expense,Other"')
    dv_s = DataValidation(type="list", formula1='"Open,Resolved"', allow_blank=True)
    ws.add_data_validation(dv_t); ws.add_data_validation(dv_s)
    for i in range(EXC_ROWS):
        r = EXC_FIRST + i
        e = exceptions[i] if i < len(exceptions) else {}
        ws.cell(r, 1, i + 1).alignment = Alignment(horizontal="center", vertical="top")
        ws.cell(r, 1).border = box
        for col, key, fmt in [("B", "type", None), ("C", "prop", None), ("D", "month", None),
                              ("E", "amt", CUR), ("F", "found", None), ("G", "check", None),
                              ("H", "status", None)]:
            inp(ws[f"{col}{r}"], ctx, e.get(key), fmt)
            ws[f"{col}{r}"].alignment = Alignment(wrap_text=True, vertical="top")
        dv_t.add(ws[f"B{r}"]); dv_s.add(ws[f"H{r}"])
        if e:
            ws.row_dimensions[r].height = 54
    last = EXC_FIRST + EXC_ROWS - 1
    ws.conditional_formatting.add(f"H{EXC_FIRST}:H{last}",
                                  FormulaRule(formula=[f'H{EXC_FIRST}="Open"'], fill=fill_red))
    ws[f"A{last + 2}"] = "Open items:"
    ws[f"A{last + 2}"].font = f_bold
    ws[f"C{last + 2}"] = f'=COUNTIF(H{EXC_FIRST}:H{last},"Open")'
    ws[f"C{last + 2}"].font = f_bold
    ws[f"A{last + 3}"] = ("Property names in column C must match the property name on each Ledger exactly, "
                          "so the Summary can count open items per property.")
    ws[f"A{last + 3}"].font = f_small
    widths(ws, [5, 18, 18, 10, 12, 44, 44, 10])
    ws.freeze_panes = "A6"
    print_setup(ws, "5:5")
    return ws, f"Exceptions!$C${EXC_FIRST}:$C${last}", f"Exceptions!$H${EXC_FIRST}:$H${last}"


# --- Contractors ---------------------------------------------------------------------------
def build_contractors(wb, ctx, props, contractors):
    ws = wb.create_sheet("Contractors")
    header(ws, ctx, "Contractors paid in " + YEAR, 8)
    ws["A5"] = "1099-NEC reporting threshold for payments in " + YEAR + ":"
    ws["A5"].font = f_bold
    ws.merge_cells("A5:D5")
    ws["E5"] = 2000
    ws["E5"].number_format = "$#,##0"
    ws["E5"].font, ws["E5"].border = f_input, box
    ws["E5"].comment = Comment(NEC_SRC_NOTE, "Year-End Rental Books", width=420, height=160)
    ws["A6"] = ("Source: IRS Instructions for Forms 1099-MISC and 1099-NEC (Rev. 12/2026): threshold rose "
                "from $600 to $2,000 for tax years beginning after 2025. " + NEC_SRC)
    ws["A6"].font, ws["A6"].alignment = f_small, wrap
    ws.merge_cells("A6:H6"); ws.row_dimensions[6].height = 26
    ws["A7"] = ("The flag only marks totals at or above the threshold. Whether a Form 1099-NEC is required, and "
                "whether you or the PM files it, is for your CPA to decide.")
    ws["A7"].font, ws["A7"].alignment = f_small, wrap
    ws.merge_cells("A7:H7"); ws.row_dimensions[7].height = 26
    head_row(ws, 9, ["Payee", "Service", "Property / properties", "Paid by (PM or owner)",
                     "Total paid in " + YEAR, "At or above threshold?", "W-9 / TIN on file?", "Notes"])
    n = max(10, len(contractors) + 2)
    first = 10
    for i in range(n):
        r = first + i
        c = contractors[i] if i < len(contractors) else {}
        for col, key, fmt in [("A", "payee", None), ("B", "service", None), ("C", "props", None),
                              ("D", "paidby", None), ("E", "total", CUR), ("G", "w9", None), ("H", "note", None)]:
            inp(ws[f"{col}{r}"], ctx, c.get(key), fmt)
            ws[f"{col}{r}"].alignment = Alignment(wrap_text=True, vertical="top")
        ws[f"F{r}"] = f'=IF(E{r}="","",IF(E{r}>=$E$5,"YES: review for 1099-NEC","No"))'
        ws[f"F{r}"].font, ws[f"F{r}"].border = f_bold, box
        ws[f"F{r}"].alignment = Alignment(vertical="top")
    last = first + n - 1
    ws.conditional_formatting.add(f"F{first}:F{last}",
                                  FormulaRule(formula=[f'LEFT(F{first},3)="YES"'], fill=fill_red))
    r = last + 2
    ws[f"A{r}"] = "Check: contractor payments listed above"
    ws[f"E{r}"] = f"=SUM(E{first}:E{last})"
    ws[f"A{r+1}"] = "Check: repairs per Ledgers (all properties)"
    ws[f"E{r+1}"] = "=" + "+".join(f"{q(p['sheet'])}!F{L_TOTAL}" for p in props)
    ws[f"A{r+2}"] = "Difference (explain on Exceptions if not zero)"
    ws[f"E{r+2}"] = f"=ROUND(E{r}-E{r+1},2)"
    for rr in (r, r + 1, r + 2):
        ws[f"A{rr}"].font = f_bold
        ws.merge_cells(f"A{rr}:D{rr}")
        ws[f"E{rr}"].number_format, ws[f"E{rr}"].font, ws[f"E{rr}"].border = CUR, f_bold, box
    ws.conditional_formatting.add(f"E{r+2}", FormulaRule(formula=[f"ABS(E{r+2})>0.004"], fill=fill_red))
    widths(ws, [28, 18, 22, 14, 14, 27, 12, 34])
    ws.freeze_panes = "A10"
    print_setup(ws, "9:9")
    return ws


# --- Schedule E map --------------------------------------------------------------------------
def build_sched_e(wb, ctx, props, owner_paid):
    ws = wb.create_sheet("Schedule E map")
    ncols = 3 + 3 * len(props) + 1
    header(ws, ctx, "Schedule E map", ncols)
    ws["A5"] = ("Annual totals per property, placed against the Schedule E (Form 1040) Part I line where they "
                "would usually go. A starting point for your CPA, who confirms every line. Lines 21-26 "
                "(net income or loss, loss limits, totals) are left to your CPA.")
    ws["A5"].font, ws["A5"].alignment = f_small, wrap
    ws.merge_cells(start_row=5, start_column=1, end_row=5, end_column=ncols)
    ws.row_dimensions[5].height = 28
    ws["A6"] = "Source: IRS 2026 Schedule E (Form 1040) draft, " + SCHED_E_SRC + " (see note)"
    ws["A6"].font = Font(name=F, size=9, italic=True, color="0563C1")
    ws["A6"].hyperlink = SCHED_E_SRC
    ws["A6"].comment = Comment(SCHED_E_SRC_NOTE, "Year-End Rental Books", width=460, height=200)
    ws.merge_cells(start_row=6, start_column=1, end_row=6, end_column=ncols)

    hr = 8
    for i, p in enumerate(props):
        c0 = 4 + 3 * i
        cell = ws.cell(hr, c0, f"={q(p['sheet'])}!B5")
        ws.merge_cells(start_row=hr, start_column=c0, end_row=hr, end_column=c0 + 2)
        cell.font, cell.fill, cell.alignment = f_head, fill_head, center
        for k in range(3):
            ws.cell(hr, c0 + k).border = box
    labels = ["Line", "Schedule E line name (2026)", "Where the amount comes from"]
    for p in props:
        labels += ["From PM statements", "Owner-paid / CPA-supplied", "Line total"]
    labels.append("Notes")
    head_row(ws, hr + 1, labels)
    ws.row_dimensions[hr + 1].height = 44
    for c in range(1, 4):
        ws.cell(hr, c).fill = fill_head
    ws.cell(hr, ncols).fill = fill_head

    r = hr + 2
    first = r
    line_rows = {}
    for ln, name, src, desc in SCHED_E_LINES:
        line_rows[ln] = r
        ws.cell(r, 1, ln).alignment = Alignment(horizontal="center")
        ws.cell(r, 2, name)
        ws.cell(r, 3, desc).font = Font(name=F, size=9, color="555555")
        for i, p in enumerate(props):
            c0 = 4 + 3 * i
            a, b, t = (get_column_letter(c0 + k) for k in range(3))
            if src:
                ws[f"{a}{r}"] = f"={q(p['sheet'])}!{src}{L_TOTAL}"
            ws[f"{a}{r}"].number_format = CUR
            inp(ws[f"{b}{r}"], ctx, owner_paid.get((p["key"], ln)), CUR)
            ws[f"{t}{r}"] = f"={a}{r}+{b}{r}"
            ws[f"{t}{r}"].number_format, ws[f"{t}{r}"].font = CUR, f_bold
        note = {"8": "Leasing fees paid to the PM. CPA to confirm the line and whether any amount "
                     "relates to a lease running past " + YEAR + ".",
                "12": "Owner to send Form 1098 to the CPA.",
                "18": "CPA maintains the depreciation schedule.",
                "19": "Itemise using the Ledger descriptions. Unclassified items are on Exceptions."}.get(ln, "")
        ws.cell(r, ncols, note).font = Font(name=F, size=9, color="555555")
        for c in range(1, ncols + 1):
            ws.cell(r, c).border = box
            if ws.cell(r, c).alignment.horizontal is None:
                ws.cell(r, c).alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    # Line 20 total expenses = lines 5 through 19
    ws.cell(r, 1, "20").alignment = Alignment(horizontal="center")
    ws.cell(r, 2, "Total expenses. Add lines 5 through 19")
    ws.cell(r, 3, "Formula")
    e_first, e_last = line_rows["5"], line_rows["19"]
    for i, p in enumerate(props):
        for k in range(3):
            col = get_column_letter(4 + 3 * i + k)
            ws[f"{col}{r}"] = f"=SUM({col}{e_first}:{col}{e_last})"
            ws[f"{col}{r}"].number_format = CUR
    for c in range(1, ncols + 1):
        cell = ws.cell(r, c)
        cell.font, cell.fill, cell.border = f_bold, fill_total, top2
    ws.cell(r, 1).alignment = Alignment(horizontal="center")
    ws[f"A{r + 2}"] = ("Blue / yellow cells in the Owner-paid column are expenses paid outside the PM (from the "
                       "owner's bank export) or amounts the CPA supplies. Each owner-paid amount should also "
                       "appear on the Exceptions sheet.")
    ws[f"A{r + 2}"].font, ws[f"A{r + 2}"].alignment = f_small, wrap
    ws.merge_cells(start_row=r + 2, start_column=1, end_row=r + 2, end_column=ncols)
    ws.row_dimensions[r + 2].height = 26
    widths(ws, [6, 34, 30] + [14, 14, 14] * len(props) + [40])
    ws.freeze_panes = ws.cell(hr + 2, 4)
    print_setup(ws, f"{hr}:{hr + 1}")
    return ws, line_rows


# --- Summary -------------------------------------------------------------------------------
def build_summary(ws, ctx, meta, props, tie_totals, exc_prop_rng, exc_stat_rng):
    header(ws, ctx, "Summary", 11)
    rows = [("Owner:", meta.get("owner")), ("Tax year covered:", YEAR),
            ("Prepared by / date:", meta.get("prepared")), ("Files received:", meta.get("files"))]
    for i, (lab, val) in enumerate(rows):
        r = 5 + i
        ws[f"A{r}"] = lab
        ws[f"A{r}"].font = f_bold
        ws.merge_cells(f"A{r}:B{r}")
        if lab.startswith("Tax year"):
            ws[f"C{r}"] = val
            ws[f"C{r}"].font = f_bold
        else:
            inp(ws[f"C{r}"], ctx, val if ctx.sample else None)
        ws.merge_cells(f"C{r}:K{r}")
    hr = 11
    head_row(ws, hr, ["Property", "Property manager", "Statements received", "Gross rent collected",
                      "PM management fees", "Leasing fees", "Repairs", "Other PM charges",
                      "Net owner distributions", "Bank tie-out difference", "Open exceptions"])
    ws.row_dimensions[hr].height = 44
    r = hr + 1
    first = r
    for p, tcell in zip(props, tie_totals):
        sh = q(p["sheet"])
        ws[f"A{r}"] = f"={sh}!B5"
        ws[f"B{r}"] = f"={sh}!H5"
        ws[f"C{r}"] = f"={sh}!B{L_TOTAL}"
        ws[f"C{r}"].number_format = '0" of 12"'
        ws[f"C{r}"].alignment = Alignment(horizontal="center")
        for col, src in zip("DEFGHI", "CDEFGJ"):
            ws[f"{col}{r}"] = f"={sh}!{src}{L_TOTAL}"
            ws[f"{col}{r}"].number_format = CUR
        ws[f"J{r}"] = f"='Bank tie-out'!{tcell}"
        ws[f"J{r}"].number_format = CUR
        ws[f"K{r}"] = f'=COUNTIFS({exc_prop_rng},A{r},{exc_stat_rng},"Open")'
        ws[f"K{r}"].alignment = Alignment(horizontal="center")
        for c in range(1, 12):
            ws.cell(r, c).border = box
            if ws.cell(r, c).font != f_bold:
                ws.cell(r, c).font = f_base
        r += 1
    last = r - 1
    ws[f"A{r}"] = "Total, all properties"
    ws.merge_cells(f"A{r}:B{r}")
    for col in "DEFGHIJ":
        ws[f"{col}{r}"] = f"=SUM({col}{first}:{col}{last})"
        ws[f"{col}{r}"].number_format = CUR
    ws[f"K{r}"] = f'=COUNTIF({exc_stat_rng},"Open")'
    ws[f"K{r}"].alignment = Alignment(horizontal="center")
    for c in range(1, 12):
        cell = ws.cell(r, c)
        cell.font, cell.fill, cell.border = f_bold, fill_total, top2
    tot = r
    ws.conditional_formatting.add(f"J{first}:J{tot}", FormulaRule(formula=[f"ABS(J{first})>0.004"], fill=fill_red))
    ws.conditional_formatting.add(f"K{first}:K{tot}", FormulaRule(formula=[f"K{first}>0"], fill=fill_red))

    # Status line (live)
    ws["A9"] = "Status:"
    ws["A9"].font = f_bold
    ws.merge_cells("A9:B9")
    ws["C9"] = (f'=IF(D{tot}=0,"Not started: no statements entered yet.",IF(AND(ABS(J{tot})<0.005,K{tot}=0),"Reconciled. Bank tie-out agrees and there are no open '
                f'exceptions.","Prepared, with "&K{tot}&" open exception(s) for CPA review and a bank tie-out '
                f'difference of "&TEXT(J{tot},"$#,##0.00;-$#,##0.00")&". See the Exceptions sheet."))')
    ws["C9"].font = Font(name=F, size=10, bold=True, color="9C0006")
    ws.merge_cells("C9:K9")

    r = tot + 2
    ws[f"A{r}"] = "Important"
    ws[f"A{r}"].font = Font(name=F, size=11, bold=True, color=NAVY)
    ws[f"A{r+1}"] = DISCLAIMER
    ws[f"A{r+1}"].font, ws[f"A{r+1}"].alignment = Font(name=F, size=10, bold=True), wrap
    ws.merge_cells(f"A{r+1}:K{r+1}")
    ws.row_dimensions[r + 1].height = 42
    guide = [
        "How to read this workbook",
        "Ledger – [property]: one per property. Month by month, gross rent and every PM fee kept separate.",
        "Schedule E map: each property's annual totals placed against the 2026 Schedule E line where they usually go.",
        "Bank tie-out: PM net distributions against deposits in the bank export. Shaded rows need attention.",
        "Exceptions: items your CPA or you should look at before the return is prepared.",
        "Contractors: payees and totals for " + YEAR + ", flagged at the 1099-NEC threshold.",
        "Blue text = typed from statements or the bank export. Black = formula. Every total is a live formula.",
    ]
    for i, g in enumerate(guide):
        c = ws[f"A{r + 3 + i}"]
        c.value = g
        c.font = Font(name=F, size=11 if i == 0 else 10, bold=(i == 0), color=NAVY if i == 0 else "000000")
        ws.merge_cells(f"A{r+3+i}:K{r+3+i}")
    if not ctx.sample:
        ws[f"A{r + 3 + len(guide)}"] = ("Template: yellow cells are the only cells to edit. See the sample workbook "
                                        "for a filled-in example of every sheet.")
        ws[f"A{r + 3 + len(guide)}"].font = Font(name=F, size=10, bold=True, color="7F6000")
    widths(ws, [22, 34, 11, 14, 14, 12, 12, 13, 15, 14, 11])
    ws.freeze_panes = f"A{hr + 1}"
    print_setup(ws, f"{hr}:{hr}")


# --- Assemble -----------------------------------------------------------------------------
def build(path, ctx, meta, props, exceptions, contractors, owner_paid):
    wb = Workbook()
    summary = wb.active
    summary.title = "Summary"
    for p in props:
        build_ledger(wb, ctx, p)
    sched, _ = build_sched_e(wb, ctx, props, owner_paid)
    _, tie_totals = build_tieout(wb, ctx, props)
    _, exc_prop, exc_stat = build_exceptions(wb, ctx, exceptions)
    build_contractors(wb, ctx, props, contractors)
    build_summary(summary, ctx, meta, props, tie_totals, exc_prop, exc_stat)
    # Order: Summary, Ledgers..., Schedule E map, Bank tie-out, Exceptions, Contractors
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.font is not None and c.font.name != F:
                    c.font = Font(name=F, size=c.font.size or 10, bold=c.font.bold,
                                  italic=c.font.italic, color=c.font.color)
    wb.properties.title = f"Year-End Rental Books {YEAR}"
    wb.properties.subject = DISCLAIMER_SHORT
    wb.save(path)
    print("wrote", path)


def sheet_name(name):
    return ("Ledger – " + name)[:31]


# --- Fictional sample data ------------------------------------------------------------------
def r2(x):
    return round(x + 1e-9, 2)


def sample_data():
    # Property A: Maple Duplex (2 units), PM Northstar, 8% management fee.
    maple_rent = [2845] * 5 + [1450] + [2875] * 6          # unit B vacant in June, new tenant from July
    maple_rep = {1: (240.00, "Ace Plumbing: kitchen drain"), 4: (1180.00, "Ace Plumbing: water heater"),
                 5: (625.00, "Brightside Painting: unit B turnover"), 8: (95.00, "Handy Pro: door lock"),
                 10: (760.00, "Ace Plumbing: main line"), }
    maple_other = {3: (185.00, "Misc. service charge (no detail on statement)"),
                   11: (45.00, "Year-end statement / 1099 packet fee")}
    maple = []
    for i in range(12):
        rent = maple_rent[i]
        mgmt = r2(rent * 0.08)
        lease = 712.50 if i == 6 else None
        rep, repnote = maple_rep.get(i, (None, ""))
        oth, othd = maple_other.get(i, (None, None))
        res = 250.00 if i == 0 else None
        maple.append(dict(recv="Y", rent=rent, mgmt=mgmt, leasing=lease, repairs=rep, other=oth,
                          other_desc=othd, reserve=res,
                          note="; ".join(x for x in [repnote,
                                                     "Opening reserve funded by PM" if i == 0 else "",
                                                     "Unit B vacant all month" if i == 5 else "",
                                                     "Leasing fee: new unit B tenant (50% of one month)" if i == 6 else ""] if x)))
    # Property B: Birch House (single-family), PM Lakeside, 10% fee + $9 admin fee. August statement missing.
    birch_rep = {0: (150.00, "Handy Pro: gutter cleaning"), 2: (310.00, "Handy Pro: fence repair"),
                 6: (1950.00, "Coolair HVAC: compressor"), 9: (420.00, "Handy Pro: bathroom fan")}
    birch = []
    for i in range(12):
        if i == 7:
            birch.append(dict(recv="N", note="Statement not received. See Exceptions #2."))
            continue
        rep, repnote = birch_rep.get(i, (None, ""))
        birch.append(dict(recv="Y", rent=1875, mgmt=187.50, repairs=rep, other=9.00,
                          other_desc="PM admin / technology fee", note=repnote))

    def net(d):
        return r2((d.get("rent") or 0) - (d.get("mgmt") or 0) - (d.get("leasing") or 0) - (d.get("repairs") or 0)
                  - (d.get("other") or 0) - (d.get("reserve") or 0))

    maple_bank, birch_bank = [], []
    for i in range(12):
        m = MONTHS[i].split()[0]
        a = net(maple[i])
        note = None
        if i == 6:
            a = r2(a + 350.00)
            note = "Exceptions #1"
        maple_bank.append(dict(amt=a, memo=f"{m} 10: ACH NORTHSTAR PM OWNER DRAW", note=note))
        if i == 7:
            birch_bank.append(dict(amt=1412.00, memo="Aug 12: ACH LAKESIDE RENTALS", note="Exceptions #2"))
        else:
            birch_bank.append(dict(amt=net(birch[i]), memo=f"{m} 12: ACH LAKESIDE RENTALS"))

    props = [
        dict(key="A", name="Maple Duplex", sheet=sheet_name("Maple Duplex"),
             address="100 Example Ave, Springfield (fictional)", pm="Northstar Property Mgmt (fictional)",
             fmt="Monthly PDF", months=maple, bank=maple_bank),
        dict(key="B", name="Birch House", sheet=sheet_name("Birch House"),
             address="200 Sample St, Springfield (fictional)", pm="Lakeside Rentals (fictional)",
             fmt="Monthly CSV + PDF", months=birch, bank=birch_bank),
    ]
    exceptions = [
        dict(type="Unmatched deposit", prop="Maple Duplex", month="Jul 2026", amt=-350.00,
             found="Bank deposit from Northstar on Jul 10 is $350.00 more than the July statement's net "
                   "distribution. The statement does not explain the extra amount.",
             check="Ask the PM what the $350.00 is (for example a deposit passed through, or a late "
                   "payment). CPA to decide how it is treated once known.", status="Open"),
        dict(type="Missing month", prop="Birch House", month="Aug 2026", amt=-1412.00,
             found="August statement from Lakeside not received. Bank shows a $1,412.00 deposit on Aug 12 "
                   "with no statement behind it, so August rent and fees are not in the Ledger.",
             check="Owner to request the August statement from Lakeside. Ledger and totals update once "
                   "it is entered.", status="Open"),
        dict(type="Unclassified charge", prop="Maple Duplex", month="Apr 2026", amt=185.00,
             found="Northstar charged $185.00 as 'Misc. service charge' with no description. Currently "
                   "included in Other PM charges (Schedule E map line 19).",
             check="Ask the PM for the invoice. CPA to confirm the right line once the nature is known.",
             status="Open"),
        dict(type="Owner-paid expense", prop="Birch House", month="Mar 2026", amt=1140.00,
             found="Landlord insurance premium of $1,140.00 paid on Mar 3 directly from the owner's bank "
                   "account, not through the PM. Entered in the Owner-paid column on Schedule E map line 9.",
             check="Confirm the policy covers Birch House only and the period it covers.", status="Open"),
    ]
    contractors = [
        dict(payee="Ace Plumbing (fictional)", service="Plumbing", props="Maple Duplex", paidby="PM (Northstar)",
             total=2180.00, w9="Ask PM", note="Three jobs: Feb, May, Nov."),
        dict(payee="Coolair HVAC (fictional)", service="HVAC repair", props="Birch House", paidby="PM (Lakeside)",
             total=1950.00, w9="Ask PM", note="One job in Jul. Just under the threshold."),
        dict(payee="Handy Pro (fictional)", service="General handyman", props="Maple Duplex; Birch House",
             paidby="PM (both)", total=975.00, w9="Ask PM", note="Paid by two different PMs: combined total shown."),
        dict(payee="Brightside Painting (fictional)", service="Painting", props="Maple Duplex",
             paidby="PM (Northstar)", total=625.00, w9="Ask PM", note="Unit B turnover, Jun."),
    ]
    owner_paid = {("B", "9"): 1140.00}
    meta = dict(owner="Jordan Example (fictional owner)",
                prepared="Year-End Rental Books, [delivery date]",
                files="24 PM statements expected, 23 received (Birch House August missing); bank export Jan-Dec 2026")
    return meta, props, exceptions, contractors, owner_paid


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out-dir", default=str(Path(__file__).resolve().parent))
    ap.add_argument("--properties", nargs="+", default=["Property 1", "Property 2"],
                    help="property names for the template (one Ledger sheet each)")
    ap.add_argument("--template-only", action="store_true")
    ap.add_argument("--template-name", default=f"template-rental-books-{YEAR}.xlsx")
    a = ap.parse_args()
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    if not a.template_only:
        meta, props, exc, con, op = sample_data()
        build(out / f"sample-rental-books-{YEAR}.xlsx", Ctx(True), meta, props, exc, con, op)
    tprops = [dict(key=str(i), name=n, sheet=sheet_name(n)) for i, n in enumerate(a.properties)]
    build(out / a.template_name, Ctx(False), {}, tprops, [], [], {})


if __name__ == "__main__":
    main()
