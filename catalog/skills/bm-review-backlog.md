# review-backlog

> Review and promote backlog items to active milestone

| | |
|---|---|
| **ID** | `bm:review-backlog` |
| **Pack** | Spec-driven Dev Workflow (also: Product Management, Software Development) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 63 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Review all 999.x backlog items and optionally promote them into the active milestone sequence or remove stale entries.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `AskUserQuestion`

## Related skills

- [bm:milestone-summary](bm-milestone-summary.md) - Generate a comprehensive project summary from milestone artifacts for team onboarding and review
- [bm:list-workspaces](bm-list-workspaces.md) - List active GSD workspaces and their status
- [bm:add-phase](bm-add-phase.md) - Add phase to end of current milestone in roadmap

## Invoke / install

- Invoke: `/bm:review-backlog`  (Skill tool: `bm:review-backlog`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
