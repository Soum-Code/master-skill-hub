# insert-phase

> Insert urgent work as decimal phase (e.g., 72.1) between existing phases

| | |
|---|---|
| **ID** | `bm:insert-phase` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 33 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Insert a decimal phase for urgent work discovered mid-milestone that must be completed between existing integer phases.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`

## Related skills

- [bm:pause-work](bm-pause-work.md) - Create context handoff when pausing work mid-phase
- [bm:resume-at](bm-resume-at.md) - Schedule a future resume of work - e.g. '/bm:resume-at 09:00', '/bm:resume-at +2h', or '/bm:resume-at 04:00 --

## Invoke / install

- Invoke: `/bm:insert-phase`  (Skill tool: `bm:insert-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
