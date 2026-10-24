# inbox

> Triage and review all open GitHub issues and PRs against project templates and contribution guidelines

| | |
|---|---|
| **ID** | `bm:inbox` |
| **Pack** | Communication & Collaboration (also: Productivity & Automation, MLOps / DevOps / Cloud, Software Development) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 39 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> One-command triage of the project's GitHub inbox. Fetches all open issues and PRs, reviews each against the corresponding template requirements (feature, enhancement, bug, chore, fix PR, enhancement PR, feature PR), reports completeness and compliance, and optionally applies labels or closes non-com

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Write`, `Grep`, `Glob`, `AskUserQuestion`

## Related skills

- [bm:docs-update](bm-docs-update.md) - Generate or update project documentation verified against the codebase
- [bm:milestone-summary](bm-milestone-summary.md) - Generate a comprehensive project summary from milestone artifacts for team onboarding and review

## Invoke / install

- Invoke: `/bm:inbox`  (Skill tool: `bm:inbox`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
