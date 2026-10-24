# add-phase

> Add phase to end of current milestone in roadmap

| | |
|---|---|
| **ID** | `bm:add-phase` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 44 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Add a new integer phase to the end of the current milestone in the roadmap.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`

## Related skills

- [bm:remove-phase](bm-remove-phase.md) - Remove a future phase from roadmap and renumber subsequent phases
- [bm:cleanup](bm-cleanup.md) - Archive accumulated phase directories from completed milestones
- [bm:analyze-dependencies](bm-analyze-dependencies.md) - Analyze phase dependencies and suggest Depends on entries for ROADMAP.md
- [bm:plan-milestone-gaps](bm-plan-milestone-gaps.md) - Create phases to close all gaps identified by milestone audit

## Invoke / install

- Invoke: `/bm:add-phase`  (Skill tool: `bm:add-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
