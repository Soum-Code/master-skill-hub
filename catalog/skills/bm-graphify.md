# graphify

> Build, query, and inspect the project knowledge graph in .planning/graphs/

| | |
|---|---|
| **ID** | `bm:graphify` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 195 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Check if graphify is enabled by reading `.planning/config.json` directly using the Read tool.

## How it is structured

The skill's own section headings, in order:

- Step 0 -- Banner
- Step 1 -- Config Gate
- Step 2 -- Parse Argument
  - Step 2a -- Query
  - Step 2b -- Status
  - Step 2c -- Diff
- Step 3 -- Build (Agent Spawn)
- Anti-Patterns

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Task`

## Related skills

- [bm:intel](bm-intel.md) - Query, inspect, or refresh codebase intelligence files in .planning/intel/
- [bm:from-gsd2](bm-from-gsd2.md) - Import a GSD-2 (.gsd/) project back to GSD v1 (.planning/) format
- [bm:spike-wrap-up](bm-spike-wrap-up.md) - Package spike findings into a persistent project skill for future build conversations
- [bm:stats](bm-stats.md) - Display project statistics — phases, plans, requirements, git metrics, and timeline

## Invoke / install

- Invoke: `/bm:graphify`  (Skill tool: `bm:graphify`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
