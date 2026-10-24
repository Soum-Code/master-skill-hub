# notion-meeting-intelligence

> Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.

| | |
|---|---|
| **ID** | `openai/skills:notion-meeting-intelligence` |
| **Pack** | Communication & Collaboration |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 61 lines in SKILL.md, 19 file(s) |

## When to use it

- Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees.

## How it is structured

The skill's own section headings, in order:

- Quick start
- Workflow
  - 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
  - 1) Gather inputs
  - 2) Choose format
  - 3) Build the agenda/pre-read
  - 4) Enrich with research
  - 5) Finalize and share
- References and examples

## What it bundles

- reference docs: `reference/brainstorming-template.md`, `reference/decision-meeting-template.md`, `reference/one-on-one-template.md`, `reference/retrospective-template.md`, `reference/sprint-planning-template.md`, `reference/status-update-template.md`, `reference/template-selection-guide.md`
- 11 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [legal:meeting-briefing](legal-meeting-briefing.md) - Prepare structured briefings for meetings with legal relevance and track resulting action items. Use when prep
- [openai/skills:notion-research-documentation](openai-skills-notion-research-documentation.md) - Research across Notion and synthesize into structured documentation; use when gathering info from multiple Not
- [bm:new-project](bm-new-project.md) - Initialize a new project with deep context gathering and PROJECT.md

## Invoke / install

- Invoke: `/openai/skills:notion-meeting-intelligence`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/notion-meeting-intelligence --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 22e4d317a1429b3f17da107e2654af5f4220d9fdea3025b43ada5e69caf82b7a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
