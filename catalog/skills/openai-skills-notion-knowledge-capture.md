# notion-knowledge-capture

> Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.

| | |
|---|---|
| **ID** | `openai/skills:notion-knowledge-capture` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 57 lines in SKILL.md, 18 file(s) |

## When to use it

- Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linking.

## How it is structured

The skill's own section headings, in order:

- Quick start
- Workflow
  - 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
  - 1) Define the capture
  - 2) Locate destination
  - 3) Extract and structure
  - 4) Create/update in Notion
  - 5) Link and surface
- References and examples

## What it bundles

- reference docs: `reference/database-best-practices.md`, `reference/decision-log-database.md`, `reference/documentation-database.md`, `reference/faq-database.md`, `reference/how-to-guide-database.md`, `reference/learning-database.md`, `reference/team-wiki-database.md`
- 10 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/openai/skills:notion-knowledge-capture`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/notion-knowledge-capture --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 5288674876a5f47a95ed81abdba0b073e763f8fc56d801bcd2c3381137c247d8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
