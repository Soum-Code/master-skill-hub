# session-report

> Generate a session report with token usage estimates, work summary, and outcomes

| | |
|---|---|
| **ID** | `bm:session-report` |
| **Pack** | Documents, Writing & Content (also: Data & Analytics, Operations & Business, Productivity & Automation) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 20 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Generate a structured SESSION_REPORT.md document capturing session outcomes, work performed, and estimated resource usage. Provides a shareable artifact for post-session review.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Write`

## Related skills

- [bm:resume-work](bm-resume-work.md) - Resume work from previous session with full context restoration
- [bm:thread](bm-thread.md) - Manage persistent context threads for cross-session work
- [anthropic-skills:explain-usage](anthropic-skills-explain-usage.md) - Explain where this session's tokens went, with one simple chart in plain language. Use when the user says thin
- [bm:milestone-summary](bm-milestone-summary.md) - Generate a comprehensive project summary from milestone artifacts for team onboarding and review

## Invoke / install

- Invoke: `/bm:session-report`  (Skill tool: `bm:session-report`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
