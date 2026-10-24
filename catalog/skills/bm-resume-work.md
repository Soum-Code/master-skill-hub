# resume-work

> Resume work from previous session with full context restoration

| | |
|---|---|
| **ID** | `bm:resume-work` |
| **Pack** | Spec-driven Dev Workflow (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 64 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Restore complete project context from a previous session. Handle manual-pause (`/bm:pause-work`) and auto-compact (PreCompact hook) handoffs identically.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Write`, `AskUserQuestion`, `SlashCommand`

## Related skills

- [bm:thread](bm-thread.md) - Manage persistent context threads for cross-session work
- [bm:pause-work](bm-pause-work.md) - Create context handoff when pausing work mid-phase
- [bm:session-report](bm-session-report.md) - Generate a session report with token usage estimates, work summary, and outcomes
- [bm:resume-at](bm-resume-at.md) - Schedule a future resume of work - e.g. '/bm:resume-at 09:00', '/bm:resume-at +2h', or '/bm:resume-at 04:00 --

## Invoke / install

- Invoke: `/bm:resume-work`  (Skill tool: `bm:resume-work`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
