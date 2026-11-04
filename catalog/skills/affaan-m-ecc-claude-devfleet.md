# claude-devfleet

> Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated worktrees, monitor progress, and read structured reports. Use when dispatching parallel coding agents across isolated worktrees and tracking their reports.

| | |
|---|---|
| **ID** | `affaan-m/ECC:claude-devfleet` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 113 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when dispatching parallel coding agents across isolated worktrees and tracking their reports.

## What it says up front

> Use this skill when you need to dispatch multiple Claude Code agents to work on coding tasks in parallel. Each agent runs in an isolated git worktree with full tooling.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Setup
- How It Works
  - Tools
  - Workflow: Plan → Dispatch → Monitor → Report
  - Concurrency
- Examples
  - Full auto: plan and launch
  - Manual: step-by-step control
  - Sequential with review
- Guidelines

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:notion-spec-to-implementation](openai-skills-notion-spec-to-implementation.md) - Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature 
- [affaan-m/ECC:dmux-workflows](affaan-m-ecc-dmux-workflows.md) - Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows 
- [affaan-m/ECC:team-builder](affaan-m-ecc-team-builder.md) - Interactive picker that discovers available agent personas via the claude agents command and agents/ markdown 
- [bm:progress](bm-progress.md) - Check project progress, show context, and route to next action (execute or plan). Use --forensic to append a 6

## Invoke / install

- Invoke: `/affaan-m/ECC:claude-devfleet`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/claude-devfleet --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 6f41605004ca33ea22a3d172a2a4dd5406f34a3b6fd8410bd84d17fdb1936f39 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
