# plan-canvas

> Open plans and HTML artifacts in a local browser canvas where the human annotates elements, chats, and approves or requests changes without leaving the page. Use when presenting a plan for review, or when feedback like "move this, change that" is easier pointed at than typed.

| | |
|---|---|
| **ID** | `affaan-m/ECC:plan-canvas` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 199 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when presenting a plan for review, or when feedback like "move this, change that" is easier pointed at than typed.

## What it says up front

> Review loop for plans and visual artifacts: you write the artifact, the human reviews it in the browser — annotating the exact element they mean, chatting, and delivering an **Approve plan / Request changes** verdict — while you block on a single CLI call that returns their feedback as JSON.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Stay listening, or the human talks to an empty chair
- Diagrams (Mermaid)
- Rules
- Examples
- Anti-Patterns

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:plan-canvas`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/plan-canvas --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 2eb23e5540cea623876095349a641ac84fb689311c1e3ebea70ee11649b4597d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
