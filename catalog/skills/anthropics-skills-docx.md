# docx

> Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', '.dotx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads. Also use when extracting or reorganizing content from .docx or .dotx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a 'report', 'memo', 'letter', 'template', or similar deliverable as a Word or .docx file, use this skill. Do NOT use for PDFs, spreadsheets, Google Docs, or general coding tasks unrelated to document generation.

| | |
|---|---|
| **ID** | `anthropics/skills:docx` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/skills](https://github.com/anthropics/skills) |
| **License** | Proprietary. LICENSE.txt has complete terms |
| **Size** | 92 lines in SKILL.md, 61 file(s) |

## When to use it

- Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files).
- Also use when extracting or reorganizing content from .docx or .dotx files, inserting or replacing images in documents, performing find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document.
- Do N.

## What it says up front

> A `.docx` is a ZIP archive of XML files. Choose your approach by task:

## How it is structured

The skill's own section headings, in order:

- Creating with docx-js — gotchas
- Verify the output
- Editing existing documents
- Comments
- Dependencies

## What it bundles

- scripts: `scripts/__init__.py`, `scripts/accept_changes.py`, `scripts/comment.py`, `scripts/merge_runs.py`, `scripts/office/helpers/__init__.py`, `scripts/office/helpers/pptx_chart.py`, `scripts/office/helpers/pptx_slide.py`, `scripts/office/helpers/pptx_theme.py` ...
- 45 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropic-skills:docx](anthropic-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word tem
- [anthropic-skills:google-workspace](anthropic-skills-google-workspace.md) - Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch
- [anthropic-skills:pdf](anthropic-skills-pdf.md) - Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text
- [anthropic-skills:docs](anthropic-skills-docs.md) - docs (editable docs people share and comment on; the default for any document, named as a doc or not: a docume

## Invoke / install

- Invoke: `/anthropics/skills:docx`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/skills --path skills/docx --commit dbd4588f9e1033efb41dad4bef2f7947c8993d44 --expect-tree 58130031b77f881105b11780d884d4147beae833c09a75531368eba155e5ea71 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
