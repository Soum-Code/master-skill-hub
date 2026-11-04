# context-and-decisions

> Govern stable domain context with a narrowly scoped CONTEXT.md when needed, and route hard-to-reverse decisions to ECC's existing architecture-decision-records skill. Use when domain terms require repeated explanation, one term has multiple meanings, unclear language causes module-boundary mistakes, or domain semantics must remain separate from architecture decisions.

| | |
|---|---|
| **ID** | `affaan-m/ECC:context-and-decisions` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 93 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when domain terms require repeated explanation, one term has multiple meanings, unclear language causes module-boundary mistakes, or domain semantics must remain separate from architecture decisions.

## What it says up front

> Govern “what these business terms mean” separately from “why this option was chosen.” Do not create an empty shell when no stable content exists.

## How it is structured

The skill's own section headings, in order:

- Domain Context Artifact: Domain Language Only
- Refine Language During the Conversation
- ADR Handoff: Reuse the Existing Capability
- When to Activate
- When to Use
- How It Works
- Examples
- Anti-Patterns
- Related Skills
- Scheduling and Task Boundary
- Attribution

## What it bundles

- reference docs: `references/source.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:context-and-decisions`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/context-and-decisions --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 2efaf9a0261f87247315f499096f92cd9059d3f9a0a1ef99fa566f3c324065a8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
