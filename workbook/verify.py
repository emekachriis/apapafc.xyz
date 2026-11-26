#!/usr/bin/env python3
"""
Recalculate a workbook with LibreOffice (headless, on a copy) and check it.

  python3 verify.py sample-rental-books-2026.xlsx
  python3 verify.py clients/smith-rental-books-2026.xlsx

Reports: formula count, any formula errors (#REF!, #VALUE!, ...), every non-zero bank
tie-out difference, open exceptions, the contractor check, and the Summary status line.
Exit code 1 if any formula error is found. Your file is not modified.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

from openpyxl import load_workbook

ERRORS = ("#REF!", "#VALUE!", "#DIV/0!", "#NAME?", "#N/A", "#NUM!", "#NULL!", "Err:")


def main(path):
    path = Path(path).resolve()
    formulas = load_workbook(path)
    n_formulas = sum(1 for ws in formulas for row in ws.iter_rows() for c in row
                     if isinstance(c.value, str) and c.value.startswith("="))
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx:Calc MS Excel 2007 XML",
                        "--outdir", td, str(path)], check=True, capture_output=True, timeout=180)
        wb = load_workbook(Path(td) / path.name, data_only=True)
    errs = [(ws.title, c.coordinate, c.value) for ws in wb for row in ws.iter_rows() for c in row
            if isinstance(c.value, str) and c.value.startswith(ERRORS)]
    print(f"{path.name}: {n_formulas} formulas, {len(errs)} errors")
    for e in errs[:50]:
        print("  ERROR", *e)

    t = wb["Bank tie-out"]
    print("Bank tie-out, non-zero monthly differences:")
    block = ""
    hits = 0
    for r in range(8, t.max_row + 1):
        a, e = t.cell(r, 1).value, t.cell(r, 5).value
        if isinstance(a, str) and "|" in a:
            block = a.split("|")[0].strip()
        if isinstance(a, str) and a[:3] in ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
                                             "Sep", "Oct", "Nov", "Dec") and isinstance(e, (int, float)) \
                and abs(e) > 0.004:
            hits += 1
            print(f"  {block} {a}: {e:,.2f}   note: {t.cell(r, 6).value}")
    if not hits:
        print("  none")
    print("Status:", wb["Summary"]["C9"].value)
    c = wb["Contractors"]
    for r in range(1, c.max_row + 1):
        if str(c.cell(r, 1).value or "").startswith("Difference"):
            print("Contractors vs ledger repairs difference:", c.cell(r, 5).value)
    return 1 if errs else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
