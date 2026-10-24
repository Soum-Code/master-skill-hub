# notion-research-documentation

> Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

| | |
|---|---|
| **ID** | `openai/skills:notion-research-documentation` |
| **Pack** | Product Management (also: Research & Learning, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 60 lines in SKILL.md, 23 file(s) |

## When to use it

- Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or reports with citations.

## How it is structured

The skill's own section headings, in order:

- Quick start
- Workflow
  - 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
  - 1) Gather sources
  - 2) Select the format
  - 3) Synthesize
  - 4) Create the doc
  - 5) Finalize & handoff
- References and examples

## What it bundles

- reference docs: `reference/advanced-search.md`, `reference/citations.md`, `reference/comparison-format.md`, `reference/comparison-template.md`, `reference/comprehensive-report-format.md`, `reference/comprehensive-report-template.md`, `reference/format-selection-guide.md`, `reference/quick-brief-format.md` ...
- 11 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:customer-research](anthropics-knowledge-work-plugins-customer-research.md) - Multi-source research on a customer question or topic with source attribution. Use when a customer asks someth
- [openai/skills:notion-meeting-intelligence](openai-skills-notion-meeting-intelligence.md) - Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas

## Invoke / install

- Invoke: `/openai/skills:notion-research-documentation`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/notion-research-documentation --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree f9d7ce5df22bc68f869b57bb528b4a1cdd3b937574d813bb6ede1bb64cf1cb1c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
