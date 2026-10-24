# plan-phase

> Create detailed phase plan (PLAN.md) with verification loop

| | |
|---|---|
| **ID** | `bm:plan-phase` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 61 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Create executable phase prompts (PLAN.md files) for a roadmap phase with integrated research and verification.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Glob`, `Grep`, `Task`, `AskUserQuestion`, `WebFetch`, `mcp__context7__*`

## Related skills

- [bm:plan-milestone-gaps](bm-plan-milestone-gaps.md) - Create phases to close all gaps identified by milestone audit
- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization
- [bm:new-workspace](bm-new-workspace.md) - Create an isolated workspace with repo copies and independent .planning/
- [bm:analyze-dependencies](bm-analyze-dependencies.md) - Analyze phase dependencies and suggest Depends on entries for ROADMAP.md

## Invoke / install

- Invoke: `/bm:plan-phase`  (Skill tool: `bm:plan-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
