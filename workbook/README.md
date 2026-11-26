# Workbook generator: Year-End Rental Books 2026

Bookkeeping prepared for your CPA. Not tax advice, tax preparation or tax filing.

## Files

| File | What it is |
|---|---|
| `build_workbook.py` | Builds the sample and the template (openpyxl). |
| `verify.py` | Recalculates a workbook in LibreOffice (on a copy) and reports formula errors, tie-out differences, the status line and the contractor check. |
| `export.py` | Makes `exports/sample-summary-schedule-e.pdf` and the three website screenshots `exports/shot-*.png`. |
| `sample-rental-books-2026.xlsx` | Fictional owner, 2 properties, 2 PMs, 12 months, 4 seeded exceptions. |
| `template-rental-books-2026.xlsx` | Same structure, empty. Yellow cells are the only cells to edit. |

## Commands

```bash
pip install openpyxl          # once
python3 build_workbook.py     # writes sample + template
python3 verify.py sample-rental-books-2026.xlsx
python3 export.py             # needs LibreOffice + poppler; ImageMagick optional
```

A template for a specific client, with one Ledger sheet per property:

```bash
python3 build_workbook.py --template-only --properties "Oak St Duplex" "Elm Ave House" --template-name smith-rental-books-2026.xlsx
```

## Sheets

1. **Summary**: owner, year, per-property totals, a live status line, and the disclaimer.
2. **Ledger – [property]**: one per property. Gross rent, management fee, leasing fee, repairs and other PM charges are kept in separate columns and never netted. Net owner distribution is a formula. Extra columns: statement received (Y/N), reserve held/released (not an expense), notes.
3. **Schedule E map**: annual totals by property against the 2026 Schedule E Part I lines (3 to 20). Each property has three columns: from PM statements (formula), owner-paid / CPA-supplied (input), and line total.
4. **Bank tie-out**: PM net distribution by month against the bank deposit. Non-zero differences are shaded.
5. **Exceptions**: items for the CPA, each with a type, an amount, what was found, what to check and a status. Open items feed the Summary.
6. **Contractors**: payee totals, flagged at the 1099-NEC threshold, plus a check that the contractor list agrees with ledger repairs.

## Sources (checked 26 Nov 2026)

- **Schedule E lines**: IRS 2026 Schedule E (Form 1040) early-release draft, created 5/6/26: https://www.irs.gov/pub/irs-dft/f1040se--dft.pdf. Same as the final 2025 form for lines 3 to 20, except that **2026 splits line 13 into 13a Vehicle loan and 13b Other**. Re-check against the final 2026 form when the IRS publishes it: https://www.irs.gov/forms-pubs/about-schedule-e-form-1040
- **1099-NEC threshold**: IRS Instructions for Forms 1099-MISC and 1099-NEC (Rev. 12/2026), What's New: the threshold is $2,000 for tax years beginning after 2025, and may be adjusted for inflation from 2027. https://www.irs.gov/instructions/i1099mec. Secondary source: https://www.patriotsoftware.com/blog/accounting/1099-reporting-threshold/

## Per-client routine

1. Generate a template with the client's property names (command above).
2. Type in each PM statement month by month: gross rent and each fee separately.
3. Type the bank deposits into the Bank tie-out. Log every shaded difference on Exceptions.
4. Enter owner-paid expenses from the bank export in the Schedule E map's Owner-paid column, and log each one on Exceptions.
5. Run `python3 verify.py <file>`: 0 errors, and every difference has an exception.
