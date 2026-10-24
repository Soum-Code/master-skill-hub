# thread

> Manage persistent context threads for cross-session work

| | |
|---|---|
| **ID** | `bm:thread` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 226 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Create, list, close, or resume persistent context threads — lightweight cross-session knowledge stores for work spanning multiple sessions that doesn't belong to any specific phase.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`

## Related skills

- [bm:resume-work](bm-resume-work.md) - Resume work from previous session with full context restoration
- [bm:pause-work](bm-pause-work.md) - Create context handoff when pausing work mid-phase
- [bm:debug](bm-debug.md) - Systematic debugging with persistent state across context resets
- [bm:session-report](bm-session-report.md) - Generate a session report with token usage estimates, work summary, and outcomes

## Invoke / install

- Invoke: `/bm:thread`  (Skill tool: `bm:thread`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
