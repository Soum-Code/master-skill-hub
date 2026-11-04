# iterative-retrieval

> Pattern for progressively refining context retrieval to solve the subagent context problem. Use when a subagent lacks the context it needs and retrieval must be refined across passes.

| | |
|---|---|
| **ID** | `affaan-m/ECC:iterative-retrieval` |
| **Pack** | general |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 213 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a subagent lacks the context it needs and retrieval must be refined across passes.

## What it says up front

> Solves the "context problem" in multi-agent workflows where subagents don't know what context they need until they start working.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- The Problem
- The Solution: Iterative Retrieval
  - Phase 1: DISPATCH
  - Phase 2: EVALUATE
  - Phase 3: REFINE
  - Phase 4: LOOP
- Practical Examples
  - Example 1: Bug Fix Context
  - Example 2: Feature Implementation
- Integration with Agents
- Best Practices
- Related

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [bm:debug](bm-debug.md) - Systematic debugging with persistent state across context resets
- [affaan-m/ECC:jpa-patterns](affaan-m-ecc-jpa-patterns.md) - JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing,

## Invoke / install

- Invoke: `/affaan-m/ECC:iterative-retrieval`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/iterative-retrieval --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 99464032aca6dfe71da45d1191061d6dcdded8723e14c5cac248eae80b6aab8e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
