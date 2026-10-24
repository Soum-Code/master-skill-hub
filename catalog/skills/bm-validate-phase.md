# validate-phase

> Retroactively audit and fill Nyquist validation gaps for a completed phase

| | |
|---|---|
| **ID** | `bm:validate-phase` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 36 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Audit Nyquist validation coverage for a completed phase. Three states: - (A) VALIDATION.md exists — audit and fill gaps - (B) No VALIDATION.md, SUMMARY.md exists — reconstruct from artifacts - (C) Phase not executed — exit with guidance

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Bash`, `Glob`, `Grep`, `Task`, `AskUserQuestion`

## Related skills

- [bm:secure-phase](bm-secure-phase.md) - Retroactively verify threat mitigations for a completed phase
- [bm:plan-milestone-gaps](bm-plan-milestone-gaps.md) - Create phases to close all gaps identified by milestone audit
- [bm:cleanup](bm-cleanup.md) - Archive accumulated phase directories from completed milestones
- [bm:audit-uat](bm-audit-uat.md) - Cross-phase audit of all outstanding UAT and verification items

## Invoke / install

- Invoke: `/bm:validate-phase`  (Skill tool: `bm:validate-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
