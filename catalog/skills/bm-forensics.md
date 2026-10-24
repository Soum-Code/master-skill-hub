# forensics

> Post-mortem investigation for failed GSD workflows — analyzes git history, artifacts, and state to diagnose what went wrong

| | |
|---|---|
| **ID** | `bm:forensics` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 57 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Investigate what went wrong during a GSD workflow execution. Analyzes git history, `.planning/` artifacts, and file system state to detect anomalies and generate a structured diagnostic report.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Grep`, `Glob`

## Related skills

- [bm:next](bm-next.md) - Automatically advance to the next logical step in the GSD workflow
- [bm:settings](bm-settings.md) - Configure GSD workflow toggles and model profile

## Invoke / install

- Invoke: `/bm:forensics`  (Skill tool: `bm:forensics`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
