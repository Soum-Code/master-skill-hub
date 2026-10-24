# secure-phase

> Retroactively verify threat mitigations for a completed phase

| | |
|---|---|
| **ID** | `bm:secure-phase` |
| **Pack** | Security & Privacy (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 36 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Verify threat mitigations for a completed phase. Three states: - (A) SECURITY.md exists — audit and verify mitigations - (B) No SECURITY.md, PLAN.md with threat model exists — run from artifacts - (C) Phase not executed — exit with guidance

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Bash`, `Glob`, `Grep`, `Task`, `AskUserQuestion`

## Related skills

- [bm:validate-phase](bm-validate-phase.md) - Retroactively audit and fill Nyquist validation gaps for a completed phase
- [bm:cleanup](bm-cleanup.md) - Archive accumulated phase directories from completed milestones
- [bm:add-tests](bm-add-tests.md) - Generate tests for a completed phase based on UAT criteria and implementation
- [bm:extract_learnings](bm-extract-learnings.md) - Extract decisions, lessons, patterns, and surprises from completed phase artifacts

## Invoke / install

- Invoke: `/bm:secure-phase`  (Skill tool: `bm:secure-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
