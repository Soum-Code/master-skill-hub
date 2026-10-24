# continual-learning

> Guide for implementing continual learning in AI coding agents — hooks, memory scoping, reflection patterns. Use when setting up learning infrastructure for agents.

| | |
|---|---|
| **ID** | `microsoft/skills:continual-learning` |
| **Pack** | AI / ML Engineering (also: Research & Learning, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 80 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when setting up learning infrastructure for agents.

## What it says up front

> Your agent forgets everything between sessions. Continual learning fixes that.

## How it is structured

The skill's own section headings, in order:

- The Loop
- Quick Start
- Two-Tier Memory
- How Learnings Get Stored
  - Automatic (via hooks)
  - Agent-native (via store_memory / SQL)
  - Manual (memory files)
- Compaction
- Best Practices

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:skill-creator](microsoft-skills-skill-creator.md) - Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry service

## Invoke / install

- Invoke: `/microsoft/skills:continual-learning`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/continual-learning --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 10b9af8687d649b3e84a5fc675000659c9d3f04192e5c2aed950f3fa0ea313d1 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
