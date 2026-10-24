# add-tests

> Generate tests for a completed phase based on UAT criteria and implementation

| | |
|---|---|
| **ID** | `bm:add-tests` |
| **Pack** | Software Development (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 42 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Generate unit and E2E tests for a completed phase, using its SUMMARY.md, CONTEXT.md, and VERIFICATION.md as specifications.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Bash`, `Glob`, `Grep`, `Task`, `AskUserQuestion`

## Related skills

- [bm:add-phase](bm-add-phase.md) - Add phase to end of current milestone in roadmap
- [bm:cleanup](bm-cleanup.md) - Archive accumulated phase directories from completed milestones
- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization
- [bm:secure-phase](bm-secure-phase.md) - Retroactively verify threat mitigations for a completed phase

## Invoke / install

- Invoke: `/bm:add-tests`  (Skill tool: `bm:add-tests`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
