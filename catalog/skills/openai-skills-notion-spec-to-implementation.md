# notion-spec-to-implementation

> Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

| | |
|---|---|
| **ID** | `openai/skills:notion-spec-to-implementation` |
| **Pack** | Product Management |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 59 lines in SKILL.md, 19 file(s) |

## When to use it

- Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them.

## How it is structured

The skill's own section headings, in order:

- Quick start
- Workflow
  - 0) If any MCP call fails because Notion MCP is not connected, pause and set it up:
  - 1) Locate and read the spec
  - 2) Choose plan depth
  - 3) Create tasks
  - 4) Link artifacts
  - 5) Track progress
- References and examples

## What it bundles

- reference docs: `reference/milestone-summary-template.md`, `reference/progress-tracking.md`, `reference/progress-update-template.md`, `reference/quick-implementation-plan.md`, `reference/spec-parsing.md`, `reference/standard-implementation-plan.md`, `reference/task-creation-template.md`, `reference/task-creation.md`
- 10 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [finance:close-management](finance-close-management.md) - Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning 
- [product-management:write-spec](product-management-write-spec.md) - Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user re
- [bm:research-phase](bm-research-phase.md) - Research how to implement a phase (standalone - usually use /bm:plan-phase instead)
- [bm:fast](bm-fast.md) - Execute a trivial task inline — no subagents, no planning overhead

## Invoke / install

- Invoke: `/openai/skills:notion-spec-to-implementation`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/notion-spec-to-implementation --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 97286f3f85ca2d72161e95d110512fd860e6c72810d7180bc767cbbc9b5f7d17 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
