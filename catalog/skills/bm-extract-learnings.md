# extract-learnings

> Extract decisions, lessons, patterns, and surprises from completed phase artifacts

| | |
|---|---|
| **ID** | `bm:extract_learnings` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 23 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Extract structured learnings from completed phase artifacts (PLAN.md, SUMMARY.md, VERIFICATION.md, UAT.md, STATE.md) into a LEARNINGS.md file that captures decisions, lessons learned, patterns discovered, and surprises encountered.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Grep`, `Glob`, `Agent`

## Related skills

- [bm:cleanup](bm-cleanup.md) - Archive accumulated phase directories from completed milestones
- [bm:validate-phase](bm-validate-phase.md) - Retroactively audit and fill Nyquist validation gaps for a completed phase
- [bm:secure-phase](bm-secure-phase.md) - Retroactively verify threat mitigations for a completed phase
- [bm:add-tests](bm-add-tests.md) - Generate tests for a completed phase based on UAT criteria and implementation

## Invoke / install

- Invoke: `/bm:extract_learnings`  (Skill tool: `bm:extract_learnings`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
