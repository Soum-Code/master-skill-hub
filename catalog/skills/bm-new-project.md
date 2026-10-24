# new-project

> Initialize a new project with deep context gathering and PROJECT.md

| | |
|---|---|
| **ID** | `bm:new-project` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 47 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Initialize a new project through unified flow: questioning → research (optional) → requirements → roadmap.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Write`, `Task`, `AskUserQuestion`

## Related skills

- [init](init.md) - Initialize a project with a CLAUDE.md that documents the codebase for future sessions.
- [bm:new-milestone](bm-new-milestone.md) - Start a new milestone cycle — update PROJECT.md and route to requirements
- [bm:progress](bm-progress.md) - Check project progress, show context, and route to next action (execute or plan). Use --forensic to append a 6
- [openai/skills:notion-meeting-intelligence](openai-skills-notion-meeting-intelligence.md) - Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas

## Invoke / install

- Invoke: `/bm:new-project`  (Skill tool: `bm:new-project`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
