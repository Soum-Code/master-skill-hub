# code-review

> Review source files changed during a phase for bugs, security issues, and code quality problems

| | |
|---|---|
| **ID** | `bm:code-review` |
| **Pack** | Software Development (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 56 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Review source files changed during a phase for bugs, security vulnerabilities, and code quality problems.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Glob`, `Grep`, `Write`, `Task`

## Related skills

- [simplify](simplify.md) - Review changed code for reuse, simplification, efficiency and altitude cleanups, then apply the fixes. Quality
- [bm:code-review-fix](bm-code-review-fix.md) - Auto-fix issues found by code review in REVIEW.md. Spawns fixer agent, commits each fix atomically, produces R
- [vercel-labs/agent-browser:dogfood](vercel-labs-agent-browser-dogfood.md) - Systematically explore and test a web application to find bugs, UX issues, and other problems. Use when asked 
- [security-review](security-review.md) - Security review of the pending changes on the current branch.

## Invoke / install

- Invoke: `/bm:code-review`  (Skill tool: `bm:code-review`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
