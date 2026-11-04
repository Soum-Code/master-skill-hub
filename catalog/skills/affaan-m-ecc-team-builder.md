# team-builder

> Interactive picker that discovers available agent personas via the claude agents command and agents/ markdown globs, groups them into domains, has the user select up to five, dispatches them in parallel on one task, and synthesizes agreements and conflicts into a unified report. Use when composing a team of agents, browsing available agent personas, or running several specialist agents in parallel.

| | |
|---|---|
| **ID** | `affaan-m/ECC:team-builder` |
| **Pack** | Communication & Collaboration (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 170 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when composing a team of agents, browsing available agent personas, or running several specialist agents in parallel.

## What it says up front

> Interactive menu for browsing and composing agent teams on demand. Works with flat or domain-subdirectory agent collections.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Prerequisites
- Configuration
- How It Works
  - Step 1: Discover Available Agents
  - Step 2: Present Domain Menu
  - Step 3: Handle Selection
  - Step 4: Spawn Agents in Parallel
  - Step 5: Synthesize Results
- Rules
- Examples

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:claude-devfleet](affaan-m-ecc-claude-devfleet.md) - Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated

## Invoke / install

- Invoke: `/affaan-m/ECC:team-builder`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/team-builder --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 62006e40d6f64daa928a6db782c9c7e65993003a71c87f6f1b221b95021dfac6 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
