# pdf

> Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple PDFs into one, splitting PDFs apart, rotating pages, adding watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs, extracting images, and OCR on scanned PDFs to make them searchable. If the user mentions a .pdf file or asks to produce one, use this skill.

| | |
|---|---|
| **ID** | `anthropic-skills:pdf` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | Proprietary. LICENSE.txt has complete terms |
| **Size** | 315 lines in SKILL.md, 12 file(s) |

## When to use it

- Use this skill whenever the user wants to do anything with PDF files.

## What it says up front

> This guide covers essential PDF processing operations using Python libraries and command-line tools. For advanced features, JavaScript libraries, and detailed examples, see REFERENCE.md. If you need to fill out a PDF form, read FORMS.md and follow its instructions.

## How it is structured

The skill's own section headings, in order:

- Overview
- Quick Start
- Python Libraries
  - pypdf - Basic Operations
  - pdfplumber - Text and Table Extraction
  - reportlab - Create PDFs
- Command-Line Tools
  - pdftotext (poppler-utils)
  - qpdf
  - pdftk (if available)
- Common Tasks
  - Extract Text from Scanned PDFs
  - Add Watermark
  - Extract Images
  - Password Protection
- Quick Reference
- Next Steps

## What it bundles

- scripts: `scripts/check_bounding_boxes.py`, `scripts/check_fillable_fields.py`, `scripts/convert_pdf_to_images.py`, `scripts/create_validation_image.py`, `scripts/extract_form_field_info.py`, `scripts/extract_form_structure.py`, `scripts/fill_fillable_fields.py`, `scripts/fill_pdf_form_with_annotations.py`
- 3 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropic-skills:docx](anthropic-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word tem
- [anthropic-skills:pptx](anthropic-skills-pptx.md) - Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This include
- [anthropic-skills:google-workspace](anthropic-skills-google-workspace.md) - Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch
- [productivity:task-management](productivity-task-management.md) - Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, want

## Invoke / install

- Invoke: `/anthropic-skills:pdf`  (Skill tool: `anthropic-skills:pdf`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
