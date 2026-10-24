# docs-update

> Generate or update project documentation verified against the codebase

| | |
|---|---|
| **ID** | `bm:docs-update` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 49 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Generate and update up to 9 documentation files for the current project. Each doc type is written by a gsd-doc-writer subagent that explores the codebase directly — no hallucinated paths, phantom endpoints, or stale signatures.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Bash`, `Glob`, `Grep`, `Task`, `AskUserQuestion`

## Related skills

- [init](init.md) - Initialize a project with a CLAUDE.md that documents the codebase for future sessions.
- [bm:new-milestone](bm-new-milestone.md) - Start a new milestone cycle — update PROJECT.md and route to requirements
- [bm:milestone-summary](bm-milestone-summary.md) - Generate a comprehensive project summary from milestone artifacts for team onboarding and review
- [openai/skills:figma-create-design-system-rules](openai-skills-figma-create-design-system-rules.md) - Generates custom design system rules for the user's codebase. Use when user says "create design system rules",

## Invoke / install

- Invoke: `/bm:docs-update`  (Skill tool: `bm:docs-update`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
