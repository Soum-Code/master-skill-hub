# remove-phase

> Remove a future phase from roadmap and renumber subsequent phases

| | |
|---|---|
| **ID** | `bm:remove-phase` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 32 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Remove an unstarted future phase from the roadmap and renumber all subsequent phases to maintain a clean, linear sequence.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Glob`

## Related skills

- [bm:add-phase](bm-add-phase.md) - Add phase to end of current milestone in roadmap
- [bm:analyze-dependencies](bm-analyze-dependencies.md) - Analyze phase dependencies and suggest Depends on entries for ROADMAP.md
- [bm:resume-at](bm-resume-at.md) - Schedule a future resume of work - e.g. '/bm:resume-at 09:00', '/bm:resume-at +2h', or '/bm:resume-at 04:00 --
- [bm:remove-workspace](bm-remove-workspace.md) - Remove a GSD workspace and clean up worktrees

## Invoke / install

- Invoke: `/bm:remove-phase`  (Skill tool: `bm:remove-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
