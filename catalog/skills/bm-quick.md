# quick

> Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents

| | |
|---|---|
| **ID** | `bm:quick` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 183 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Execute small, ad-hoc tasks with GSD guarantees (atomic commits, STATE.md tracking). Same system, shorter path: - Spawns gsd-planner (quick mode) + gsd-executor(s) - Quick tasks live in `.planning/quick/` separate from planned phases - Updates STATE.md "Quick Tasks Completed" table (NOT ROADMAP.md)

## How it is structured

The skill's own section headings, in order:

- LIST subcommand
- STATUS subcommand
- RESUME subcommand
- RUN subcommand (default)

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Glob`, `Grep`, `Bash`, `Task`, `AskUserQuestion`

## Related skills

- [bm:fast](bm-fast.md) - Execute a trivial task inline — no subagents, no planning overhead
- [bm:set-profile](bm-set-profile.md) - Switch model profile for GSD agents (quality/balanced/budget/inherit)

## Invoke / install

- Invoke: `/bm:quick`  (Skill tool: `bm:quick`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
