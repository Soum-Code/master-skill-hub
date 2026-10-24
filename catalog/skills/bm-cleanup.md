# cleanup

> Archive accumulated phase directories from completed milestones

| | |
|---|---|
| **ID** | `bm:cleanup` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 24 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Archive phase directories from completed milestones into `.planning/milestones/v{X.Y}-phases/`.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `AskUserQuestion`

## Related skills

- [bm:complete-milestone](bm-complete-milestone.md) - Archive completed milestone and prepare for next version
- [bm:add-phase](bm-add-phase.md) - Add phase to end of current milestone in roadmap
- [bm:secure-phase](bm-secure-phase.md) - Retroactively verify threat mitigations for a completed phase
- [bm:extract_learnings](bm-extract-learnings.md) - Extract decisions, lessons, patterns, and surprises from completed phase artifacts

## Invoke / install

- Invoke: `/bm:cleanup`  (Skill tool: `bm:cleanup`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
