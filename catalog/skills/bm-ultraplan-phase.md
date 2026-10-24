# ultraplan-phase

> [BETA] Offload plan phase to Claude Code's ultraplan cloud — drafts remotely while terminal stays free, review in browser with inline comments, import back via /bm:import. Claude Code only.

| | |
|---|---|
| **ID** | `bm:ultraplan-phase` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 34 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Offload GSD's plan phase to Claude Code's ultraplan cloud infrastructure.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Glob`, `Grep`

## Related skills

- [bm:from-gsd2](bm-from-gsd2.md) - Import a GSD-2 (.gsd/) project back to GSD v1 (.planning/) format
- [bm:research-phase](bm-research-phase.md) - Research how to implement a phase (standalone - usually use /bm:plan-phase instead)
- [bm:list-phase-assumptions](bm-list-phase-assumptions.md) - Surface Claude's assumptions about a phase approach before planning
- [bm:review](bm-review.md) - Request cross-AI peer review of phase plans from external AI CLIs

## Invoke / install

- Invoke: `/bm:ultraplan-phase`  (Skill tool: `bm:ultraplan-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
