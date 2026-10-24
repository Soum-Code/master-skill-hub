# pptx

> Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx or .potx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates (.potx), layouts, speaker notes, or comments. Trigger whenever the user mentions "deck," "slides," "presentation," or references a .pptx or .potx filename, regardless of what they plan to do with the content afterward. If a .pptx or .potx file needs to be opened, created, or touched, use this skill.

| | |
|---|---|
| **ID** | `anthropics/skills:pptx` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/skills](https://github.com/anthropics/skills) |
| **License** | Proprietary. LICENSE.txt has complete terms |
| **Size** | 239 lines in SKILL.md, 56 file(s) |

## When to use it

- Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both.
- Trigger whenever the user mentions "deck," "slides," "presentation," or references a .pptx or .potx filename, regardless of what they plan to do with the content afterward.

## What it says up front

> A `.pptx` is a ZIP archive of XML files. Choose your approach by task:

## How it is structured

The skill's own section headings, in order:

- Scripts
- Creating with pptxgenjs — gotchas
- Editing existing decks and templates
- Design Ideas
  - Before Starting
  - Color Palettes
  - For Each Slide
  - Typography
  - Spacing
  - Avoid (Common Mistakes)
- QA (Required)
  - Content QA
  - File QA (required)
  - Visual QA
- Converting to Images
- Dependencies

## What it bundles

- scripts: `scripts/__init__.py`, `scripts/add_slide.py`, `scripts/clean.py`, `scripts/office/helpers/__init__.py`, `scripts/office/helpers/pptx_chart.py`, `scripts/office/helpers/pptx_slide.py`, `scripts/office/helpers/pptx_theme.py`, `scripts/office/soffice.py` ...
- 40 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropic-skills:pptx](anthropic-skills-pptx.md) - Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This include
- [anthropic-skills:docx](anthropic-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word tem
- [anthropics/skills:docx](anthropics-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Wo
- [anthropic-skills:pdf](anthropic-skills-pdf.md) - Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text

## Invoke / install

- Invoke: `/anthropics/skills:pptx`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/skills --path skills/pptx --commit dbd4588f9e1033efb41dad4bef2f7947c8993d44 --expect-tree 8f7defcfc4ff81052f2299f7ae529b49948c1cd10fd0832bb6d8435ba6187b18 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
