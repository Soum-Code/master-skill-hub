# ecc-guide

> Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install profiles, and docs — instead of memory. Use when the user asks what ECC includes, how to install or reset it, which skill or command fits a task, or how project onboarding works.

| | |
|---|---|
| **ID** | `affaan-m/ECC:ecc-guide` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 191 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user asks what ECC includes, how to install or reset it, which skill or command fits a task, or how project onboarding works.

## What it says up front

> Use this skill when a user needs help understanding, navigating, installing, or choosing parts of ECC.

## How it is structured

The skill's own section headings, in order:

- When To Use
- Core Principle
- Repository Map
- Response Style
- Common Tasks
  - New User Onboarding
  - Feature Discovery
  - Install Guidance
  - Project Onboarding
  - Troubleshooting
- Output Templates
  - Short Recommendation
  - Search Results
  - Install Plan Summary
- Related Surfaces

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:agent-sort](affaan-m-ecc-agent-sort.md) - Build an evidence-backed ECC install plan for a specific repo by sorting skills, commands, rules, hooks, and e
- [vercel-labs/skills:find-skills](vercel-labs-skills-find-skills.md) - Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for 
- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h
- [anthropic-skills:morning](anthropic-skills-morning.md) - Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task. Use only 

## Invoke / install

- Invoke: `/affaan-m/ECC:ecc-guide`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/ecc-guide --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree dd512144a5984f5f8ca6bf46e3df752b3c93dc17cb562f6c05b8f6c21c70d943 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
