# google-workspace

> Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or changes a Google file. Use this skill whenever the user wants to create or change a Google Doc, Sheet or Slides file in their Google Drive. Triggers include: a request that names Google Docs, Sheets, Slides or Drive and asks to make, edit, format, copy or rename a file; a docs.google.com link with a request to change that file, even a one-line fix or suggested edits; and any follow-up change to a Google file from earlier in the chat, even "change it" or "add a tab". Includes helper scripts for document positions, cell ranges and slide layout. However, if the user asks for a doc, deck or spreadsheet without naming Google, or gives a Google file only as source material for something new, use Claude's own output type instead. Do NOT use for read-only questions about a Google file, or for Word, Excel, PowerPoint or PDF files.

| | |
|---|---|
| **ID** | `anthropic-skills:google-workspace` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | not declared |
| **Size** | 98 lines in SKILL.md, 9 file(s) |

## When to use it

- Use this skill whenever the user wants to create or change a Google Doc, Sheet or Slides file in their Google Drive.
- Do NOT use for read-only questions about a Google file, or for Word, Excel, PowerPoint or PDF files.

## How it is structured

The skill's own section headings, in order:

- Read the reference before you touch the file
- 1. Check the connectors before you start
- 2. Rules for every file
- 3. Drive, for all three apps
- 4. Helper scripts
- 5. Common failures across apps
- 6. What the connectors can't do

## What it bundles

- scripts: `scripts/docs_index.py`, `scripts/render_export.py`, `scripts/sheets_helper.py`, `scripts/slides_helper.py`
- reference docs: `references/charts.md`, `references/docs.md`, `references/sheets.md`, `references/slides.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropic-skills:docx](anthropic-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word tem
- [anthropic-skills:pptx](anthropic-skills-pptx.md) - Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This include
- [anthropic-skills:docs](anthropic-skills-docs.md) - docs (editable docs people share and comment on; the default for any document, named as a doc or not: a docume
- [anthropic-skills:xlsx](anthropic-skills-xlsx.md) - Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user 

## Invoke / install

- Invoke: `/anthropic-skills:google-workspace`  (Skill tool: `anthropic-skills:google-workspace`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
