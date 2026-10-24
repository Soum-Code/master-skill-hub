# new-milestone

> Start a new milestone cycle — update PROJECT.md and route to requirements

| | |
|---|---|
| **ID** | `bm:new-milestone` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 45 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Start a new milestone: questioning → research (optional) → requirements → roadmap.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Task`, `AskUserQuestion`

## Related skills

- [bm:new-project](bm-new-project.md) - Initialize a new project with deep context gathering and PROJECT.md
- [bm:milestone-summary](bm-milestone-summary.md) - Generate a comprehensive project summary from milestone artifacts for team onboarding and review
- [bm:stats](bm-stats.md) - Display project statistics — phases, plans, requirements, git metrics, and timeline
- [bm:docs-update](bm-docs-update.md) - Generate or update project documentation verified against the codebase

## Invoke / install

- Invoke: `/bm:new-milestone`  (Skill tool: `bm:new-milestone`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
