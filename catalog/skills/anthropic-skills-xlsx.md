# xlsx

> Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .xlsx, .xlsm, .xltx, .csv, or .tsv file (e.g., adding columns, computing formulas, formatting, charting, cleaning messy data); create a new spreadsheet from scratch or from other data sources; or convert between tabular file formats. Trigger especially when the user references a spreadsheet file by name or path — even casually (like "the xlsx in my downloads") — and wants something done to it or produced from it. Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets. The deliverable must be a spreadsheet file. Do NOT trigger when the primary deliverable is a Word document, HTML report, standalone Python script, database pipeline, or Google Sheets API integration, even if tabular data is involved.

| | |
|---|---|
| **ID** | `anthropic-skills:xlsx` |
| **Pack** | Data & Analytics |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | Proprietary. LICENSE.txt has complete terms |
| **Size** | 100 lines in SKILL.md, 53 file(s) |

## When to use it

- Use this skill any time a spreadsheet file is the primary input or output.
- Trigger especially when the user references a spreadsheet file by name or path — even casually (like "the xlsx in my downloads") — and wants something done to it or produced from it.
- Also trigger for cleaning or restructuring messy tabular data files (malformed rows, misplaced headers, junk data) into proper spreadsheets.

## What it says up front

> openpyxl writes formulas as strings with **no cached values**. Until you recalculate, every formula cell reads back as `None` to anything reading cached values — `pandas`, `load_workbook(data_only=True)`, and most previewers.

## How it is structured

The skill's own section headings, in order:

- Requirements for every output
- Recalculate (mandatory whenever the file contains formulas)
- Choosing formulas that survive verification
- openpyxl gotchas
- Financial models
- Dependencies

## What it bundles

- scripts: `scripts/office/helpers/__init__.py`, `scripts/office/helpers/pptx_chart.py`, `scripts/office/helpers/pptx_slide.py`, `scripts/office/helpers/pptx_theme.py`, `scripts/office/soffice.py`, `scripts/office/validate.py`, `scripts/office/validators/__init__.py`, `scripts/office/validators/base.py` ...
- 40 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropic-skills:google-workspace](anthropic-skills-google-workspace.md) - Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch
- [anthropic-skills:docx](anthropic-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word tem
- [anthropic-skills:pptx](anthropic-skills-pptx.md) - Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This include
- [anthropic-skills:docs](anthropic-skills-docs.md) - docs (editable docs people share and comment on; the default for any document, named as a doc or not: a docume

## Invoke / install

- Invoke: `/anthropic-skills:xlsx`  (Skill tool: `anthropic-skills:xlsx`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
