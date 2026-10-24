# docx

> Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word templates (.dotx). Triggers include: any mention of Microsoft Word Documents, such as 'Word doc', 'word document', '.docx', '.dotx', 'microsoft doc'. Also use when extracting or reorganizing content from .docx or .dotx files, inserting or replacing images in documents, find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document. If the user asks for a deliverable as a Word or .docx file (to download, email or print), use this skill. However, if they ask for a document, page, report, memo, or notes WITHOUT naming a file format and the session offers Claude's own dedicated document or page skill or connector, use that instead, even if they will email or print it. Do NOT use for PDFs, spreadsheets, Google Docs, or coding unrelated to document generation.

| | |
|---|---|
| **ID** | `anthropic-skills:docx` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | Proprietary. LICENSE.txt has complete terms |
| **Size** | 94 lines in SKILL.md, 61 file(s) |

## When to use it

- Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word templates (.dotx).
- Also use when extracting or reorganizing content from .docx or .dotx files, inserting or replacing images in documents, find-and-replace in Word files, working with tracked changes or comments, or converting content into a polished Word document.
- Do NOT use for PDFs, spread.

## What it says up front

> If you are about to make a new document and this session offers Claude's own docs (a Docs connector, docs skill or Docs artifact type), and the user has neither named Word/.docx/.dotx, asked for tracked changes, nor supplied a .docx/.dotx file to change or use as a template, make the document there

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

- [anthropics/skills:docx](anthropics-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Wo
- [anthropic-skills:google-workspace](anthropic-skills-google-workspace.md) - Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch
- [anthropic-skills:pptx](anthropic-skills-pptx.md) - Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This include
- [anthropic-skills:docs](anthropic-skills-docs.md) - docs (editable docs people share and comment on; the default for any document, named as a doc or not: a docume

## Invoke / install

- Invoke: `/anthropic-skills:docx`  (Skill tool: `anthropic-skills:docx`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
