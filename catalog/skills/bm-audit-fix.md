# audit-fix

> Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit

| | |
|---|---|
| **ID** | `bm:audit-fix` |
| **Pack** | Finance & Accounting (also: Security & Privacy) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 34 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Run an audit, classify findings as auto-fixable vs manual-only, then autonomously fix auto-fixable issues with test verification and atomic commits.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Bash`, `Grep`, `Glob`, `Agent`, `AskUserQuestion`

## Related skills

- [bm:code-review-fix](bm-code-review-fix.md) - Auto-fix issues found by code review in REVIEW.md. Spawns fixer agent, commits each fix atomically, produces R
- [finance:audit-support](finance-audit-support.md) - Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards. Us

## Invoke / install

- Invoke: `/bm:audit-fix`  (Skill tool: `bm:audit-fix`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
