# nutrient-document-processing

> Process, convert, OCR, extract, redact, sign, and fill documents using the Nutrient DWS API. Works with PDFs, DOCX, XLSX, PPTX, HTML, and images. Use when converting, OCRing, extracting from, redacting, signing, or filling documents via the Nutrient DWS API.

| | |
|---|---|
| **ID** | `affaan-m/ECC:nutrient-document-processing` |
| **Pack** | Documents, Writing & Content (also: Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 169 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when converting, OCRing, extracting from, redacting, signing, or filling documents via the Nutrient DWS API.

## What it says up front

> Process documents with the [Nutrient DWS Processor API](https://www.nutrient.io/api/). Convert formats, extract text and tables, OCR scanned documents, redact PII, add watermarks, digitally sign, and fill PDF forms.

## How it is structured

The skill's own section headings, in order:

- Setup
- Operations
  - Convert Documents
  - Extract Text and Data
  - OCR Scanned Documents
  - Redact Sensitive Information
  - Add Watermarks
  - Digital Signatures
  - Fill PDF Forms
- MCP Server (Alternative)
- When to Use
- Links

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:visa-doc-translate](affaan-m-ecc-visa-doc-translate.md) - Translate visa document images (bank deposit, employment, income, and retirement certificates; HEIC, PNG, or J
- [anthropic-skills:pdf](anthropic-skills-pdf.md) - Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text
- [anthropics/skills:docx](anthropics-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Wo
- [anthropic-skills:docx](anthropic-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word tem

## Invoke / install

- Invoke: `/affaan-m/ECC:nutrient-document-processing`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/nutrient-document-processing --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c043e90b7f9349f8f9c8e6edc8a6aa782e404ac6017343ebadd08ffe6ae0580d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
