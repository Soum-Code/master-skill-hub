# resume-at

> Schedule a future resume of work - e.g. '/bm:resume-at 09:00', '/bm:resume-at +2h', or '/bm:resume-at 04:00 --cmd /bm:execute-phase 9'

| | |
|---|---|
| **ID** | `bm:resume-at` |
| **Pack** | Spec-driven Dev Workflow (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 90 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Schedule a future Claude Code session that automatically resumes the current GSD project at the requested time. Useful for: coming back after a usage/token cap, kicking off work overnight so HANDOFF restores the morning session, or queuing a future GSD command (e.g. `/bm:execute-phase 9` at 04:00) f

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Skill`, `AskUserQuestion`, `Bash`

## Related skills

- [bm:remove-phase](bm-remove-phase.md) - Remove a future phase from roadmap and renumber subsequent phases
- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization
- [bm:resume-work](bm-resume-work.md) - Resume work from previous session with full context restoration
- [bm:autonomous](bm-autonomous.md) - Run all remaining phases autonomously — discuss→plan→execute per phase

## Invoke / install

- Invoke: `/bm:resume-at`  (Skill tool: `bm:resume-at`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
