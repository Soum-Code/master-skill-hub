# fast

> Execute a trivial task inline — no subagents, no planning overhead

| | |
|---|---|
| **ID** | `bm:fast` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 31 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Execute a trivial task directly in the current context without spawning subagents or generating PLAN.md files. For tasks too small to justify planning overhead: typo fixes, config changes, small refactors, forgotten commits, simple additions.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Bash`, `Grep`, `Glob`

## Related skills

- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization
- [bm:autonomous](bm-autonomous.md) - Run all remaining phases autonomously — discuss→plan→execute per phase
- [bm:quick](bm-quick.md) - Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents

## Invoke / install

- Invoke: `/bm:fast`  (Skill tool: `bm:fast`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
