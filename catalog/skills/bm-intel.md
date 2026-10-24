# intel

> Query, inspect, or refresh codebase intelligence files in .planning/intel/

| | |
|---|---|
| **ID** | `bm:intel` |
| **Pack** | Spec-driven Dev Workflow (also: Software Development) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 174 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Check if intel is enabled by reading `.planning/config.json` directly using the Read tool.

## How it is structured

The skill's own section headings, in order:

- Step 0 -- Banner
- Step 1 -- Config Gate
- Step 2 -- Parse Argument
  - Step 2a -- Query
  - Step 2b -- Status
  - Step 2c -- Diff
- Step 3 -- Refresh (Agent Spawn)
- Step 4 -- Post-Refresh Summary
- Anti-Patterns

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Task`

## Related skills

- [bm:graphify](bm-graphify.md) - Build, query, and inspect the project knowledge graph in .planning/graphs/
- [bm:map-codebase](bm-map-codebase.md) - Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents

## Invoke / install

- Invoke: `/bm:intel`  (Skill tool: `bm:intel`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
