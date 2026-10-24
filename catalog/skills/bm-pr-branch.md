# pr-branch

> Create a clean PR branch by filtering out .planning/ commits — ready for code review

| | |
|---|---|
| **ID** | `bm:pr-branch` |
| **Pack** | MLOps / DevOps / Cloud (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 26 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Create a clean branch suitable for pull requests by filtering out .planning/ commits from the current branch. Reviewers see only code changes, not GSD planning artifacts.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash`, `Read`, `AskUserQuestion`

## Related skills

- [bm:ship](bm-ship.md) - Create PR, run review, and prepare for merge after verification passes
- [code-review](code-review.md) - Review the current diff or a PR number, branch or path for correctness bugs at a chosen effort level; optional
- [security-review](security-review.md) - Security review of the pending changes on the current branch.
- [bm:code-review-fix](bm-code-review-fix.md) - Auto-fix issues found by code review in REVIEW.md. Spawns fixer agent, commits each fix atomically, produces R

## Invoke / install

- Invoke: `/bm:pr-branch`  (Skill tool: `bm:pr-branch`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
