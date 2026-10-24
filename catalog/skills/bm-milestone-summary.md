# milestone-summary

> Generate a comprehensive project summary from milestone artifacts for team onboarding and review

| | |
|---|---|
| **ID** | `bm:milestone-summary` |
| **Pack** | Spec-driven Dev Workflow (also: Documents, Writing & Content) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 52 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Generate a structured milestone summary for team onboarding and project review. Reads completed milestone artifacts (ROADMAP, REQUIREMENTS, CONTEXT, SUMMARY, VERIFICATION files) and produces a human-friendly overview of what was built, how, and why.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Grep`, `Glob`

## Related skills

- [bm:review-backlog](bm-review-backlog.md) - Review and promote backlog items to active milestone
- [bm:new-milestone](bm-new-milestone.md) - Start a new milestone cycle — update PROJECT.md and route to requirements
- [bm:docs-update](bm-docs-update.md) - Generate or update project documentation verified against the codebase
- [bm:profile-user](bm-profile-user.md) - Generate developer behavioral profile and create Claude-discoverable artifacts

## Invoke / install

- Invoke: `/bm:milestone-summary`  (Skill tool: `bm:milestone-summary`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
