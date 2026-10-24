# map-codebase

> Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents

| | |
|---|---|
| **ID** | `bm:map-codebase` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 70 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Analyze existing codebase using parallel gsd-codebase-mapper agents. Each mapper explores a focus area and **writes documents directly** to `.planning/codebase/`; the orchestrator only receives confirmations, keeping context usage minimal.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Glob`, `Grep`, `Write`, `Task`

## Related skills

- [bm:scan](bm-scan.md) - Rapid codebase assessment — lightweight alternative to /bm:map-codebase
- [init](init.md) - Initialize a project with a CLAUDE.md that documents the codebase for future sessions.
- [bm:intel](bm-intel.md) - Query, inspect, or refresh codebase intelligence files in .planning/intel/
- [bm:code-review-fix](bm-code-review-fix.md) - Auto-fix issues found by code review in REVIEW.md. Spawns fixer agent, commits each fix atomically, produces R

## Invoke / install

- Invoke: `/bm:map-codebase`  (Skill tool: `bm:map-codebase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
