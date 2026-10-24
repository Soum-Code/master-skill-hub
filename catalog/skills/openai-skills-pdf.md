# pdf

> Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

| | |
|---|---|
| **ID** | `openai/skills:pdf` |
| **Pack** | Documents, Writing & Content (also: Web, Frontend & UI Design, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 68 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction.

## How it is structured

The skill's own section headings, in order:

- When to use
- Workflow
- Temp and output conventions
- Dependencies (install if missing)
- Environment
- Rendering command
- Quality expectations
- Final checks

## What it bundles

- 3 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:pdf](anthropic-skills-pdf.md) - Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text

## Invoke / install

- Invoke: `/openai/skills:pdf`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/pdf --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree e88757b30e993242a2c915e3e92bb69b14af7929bbe679ec9b53fb1b0547b168 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
