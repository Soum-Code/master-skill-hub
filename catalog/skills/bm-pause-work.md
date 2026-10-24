# pause-work

> Create context handoff when pausing work mid-phase

| | |
|---|---|
| **ID** | `bm:pause-work` |
| **Pack** | Spec-driven Dev Workflow (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 39 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Create `.continue-here.md` handoff file to preserve complete work state across sessions.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`

## Related skills

- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [bm:resume-work](bm-resume-work.md) - Resume work from previous session with full context restoration
- [bm:thread](bm-thread.md) - Manage persistent context threads for cross-session work
- [bm:insert-phase](bm-insert-phase.md) - Insert urgent work as decimal phase (e.g., 72.1) between existing phases

## Invoke / install

- Invoke: `/bm:pause-work`  (Skill tool: `bm:pause-work`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
