# scan

> Rapid codebase assessment — lightweight alternative to /bm:map-codebase

| | |
|---|---|
| **ID** | `bm:scan` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 28 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Run a focused codebase scan for a single area, producing targeted documents in `.planning/codebase/`. Accepts an optional `--focus` flag (`tech`, `arch`, `quality`, `concerns`, or `tech+arch` (default)), OR a `--drift` mode (mutually exclusive with `--focus`) that runs `gsd-tools verify drift` and p

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Grep`, `Glob`, `Agent`, `AskUserQuestion`

## Related skills

- [bm:map-codebase](bm-map-codebase.md) - Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents

## Invoke / install

- Invoke: `/bm:scan`  (Skill tool: `bm:scan`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
