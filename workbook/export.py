#!/usr/bin/env python3
"""
Export the (already recalculated) sample workbook to:
  exports/sample-summary-schedule-e.pdf   Summary + Schedule E map only
  exports/shot-*.png                      website screenshots

Needs LibreOffice (soffice) and poppler (pdftoppm); ImageMagick is optional (trims margins).
Run build_workbook.py and the recalc step first (see README.md).
"""
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "sample-rental-books-2026.xlsx"
OUT = HERE / "exports"


def hide_sheets(src, dst, keep):
    """Copy the xlsx, marking every sheet not in `keep` hidden (cached values preserved)."""
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "xl/workbook.xml":
                xml = data.decode("utf-8")

                def fix(m):
                    tag = m.group(0)
                    name = re.search(r'name="([^"]*)"', tag).group(1)
                    name = name.replace("&amp;", "&")
                    tag = re.sub(r'\sstate="[^"]*"', "", tag)
                    return tag if name in keep else tag.replace("<sheet ", '<sheet state="hidden" ', 1)

                xml = re.sub(r"<sheet [^>]*/>", fix, xml)
                xml = re.sub(r'activeTab="\d+"', 'activeTab="0"', xml)
                data = xml.encode("utf-8")
            zout.writestr(item, data)


def to_pdf(xlsx, pdf):
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", td, str(xlsx)],
                       check=True, capture_output=True, timeout=180)
        shutil.move(str(Path(td) / (Path(xlsx).stem + ".pdf")), pdf)


def main():
    OUT.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "sample-summary-schedule-e.xlsx"
        hide_sheets(SRC, tmp, {"Summary", "Schedule E map"})
        to_pdf(tmp, OUT / "sample-summary-schedule-e.pdf")
        allpdf = OUT / "sample-all-sheets.pdf"
        to_pdf(SRC, allpdf)
        # One PNG per page at 2x-ish resolution, then pick the pages we want.
        subprocess.run(["pdftoppm", "-r", "160", "-png", str(allpdf), str(Path(td) / "p")], check=True)
        pages = sorted(Path(td).glob("p-*.png"))
        print("pages:", len(pages))
        # Website screenshots: Summary (p1), Maple ledger (p2), Bank tie-out first block (p5)
        for page, name in [(1, "shot-summary.png"), (2, "shot-ledger.png"), (5, "shot-tieout.png")]:
            src = pages[page - 1]
            dst = OUT / name
            if shutil.which("convert"):
                # trim page margins and the footer, keep a small white border
                subprocess.run(["convert", str(src), "-crop", "100%x93%+0+0", "+repage", "-trim", "+repage",
                                "-bordercolor", "white", "-border", "24", str(dst)], check=True)
            else:
                shutil.copy(src, dst)
        allpdf.unlink()  # only needed to make the PNGs
    print("done:", sorted(x.name for x in OUT.iterdir()))


if __name__ == "__main__":
    main()
