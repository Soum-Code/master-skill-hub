# code-review-fix

> Auto-fix issues found by code review in REVIEW.md. Spawns fixer agent, commits each fix atomically, produces REVIEW-FIX.md summary.

| | |
|---|---|
| **ID** | `bm:code-review-fix` |
| **Pack** | Software Development (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 53 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Auto-fix issues found by code review. Reads REVIEW.md from the specified phase, spawns gsd-code-fixer agent to apply fixes, and produces REVIEW-FIX.md summary.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Glob`, `Grep`, `Write`, `Edit`, `Task`

## Related skills

- [bm:code-review](bm-code-review.md) - Review source files changed during a phase for bugs, security issues, and code quality problems
- [bm:audit-fix](bm-audit-fix.md) - Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit
- [bm:pr-branch](bm-pr-branch.md) - Create a clean PR branch by filtering out .planning/ commits — ready for code review
- [bm:eval-review](bm-eval-review.md) - Retroactively audit an executed AI phase's evaluation coverage — scores each eval dimension as COVERED/PARTIAL

## Invoke / install

- Invoke: `/bm:code-review-fix`  (Skill tool: `bm:code-review-fix`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
