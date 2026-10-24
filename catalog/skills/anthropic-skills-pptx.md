# pptx

> Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations as PowerPoint (.pptx) files; reading, parsing, or extracting text from any .pptx or .potx file (even if the extracted content will be used elsewhere, like in an email, summary, or creating a different type of slide deck); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates (.potx), layouts, speaker notes, or comments. Trigger whenever the user asks for a PowerPoint or .pptx file, or references a .pptx or .potx filename, regardless of what they plan to do with the content afterward. However, when the user asks for a deck, slides, a slide deck, or a presentation without naming a file format, default to using a dedicated slide-deck artifact type or a separate slides skill if this session offers one; otherwise, use this skill.

| | |
|---|---|
| **ID** | `anthropic-skills:pptx` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | Proprietary. LICENSE.txt has complete terms |
| **Size** | 272 lines in SKILL.md, 58 file(s) |

## When to use it

- Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both.
- Trigger whenever the user asks for a PowerPoint or .pptx file, or references a .pptx or .potx filename, regardless of what they plan to do with the content afterward.
- However, when the user asks for a deck, slides, a slide deck, or a presentation without naming a file format, default to using a dedica.

## What it says up front

> If this session offers a dedicated slide-deck artifact type or a separate slides skill, and the user has neither asked for a PowerPoint/.pptx file nor supplied a .pptx/.potx file to edit, fill in, or convert, build the deck with that type or skill instead. A .pptx/.potx file given only as source mat

## How it is structured

The skill's own section headings, in order:

- Scripts
- Creating with pptxgenjs — gotchas
  - Structured decks
- Editing existing decks and templates
- Deck content and flow
- Design Ideas
  - Before Starting
  - Color Palettes
  - For Each Slide
  - Typography
  - Spacing
  - Avoid (Common Mistakes)
- QA (Required)
  - Content QA (required)
  - File QA (required)
  - Visual QA (required)
- Converting to Images
- Dependencies

## What it bundles

- scripts: `scripts/__init__.py`, `scripts/add_slide.py`, `scripts/apply_theme.js`, `scripts/clean.py`, `scripts/office/helpers/__init__.py`, `scripts/office/helpers/pptx_chart.py`, `scripts/office/helpers/pptx_slide.py`, `scripts/office/helpers/pptx_theme.py` ...
- 40 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropic-skills:docx](anthropic-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word tem
- [anthropic-skills:google-workspace](anthropic-skills-google-workspace.md) - Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch
- [anthropic-skills:pdf](anthropic-skills-pdf.md) - Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text
- [anthropic-skills:xlsx](anthropic-skills-xlsx.md) - Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user 

## Invoke / install

- Invoke: `/anthropic-skills:pptx`  (Skill tool: `anthropic-skills:pptx`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
