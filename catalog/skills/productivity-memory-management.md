# memory-management

> Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude understands requests like a colleague would. CLAUDE.md for working memory, memory/ directory for the full knowledge base.

| | |
|---|---|
| **ID** | `productivity:memory-management` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `productivity` v1.3.1 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 324 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Memory makes Claude your workplace collaborator - someone who speaks your internal language.

## How it is structured

The skill's own section headings, in order:

- The Goal
- Architecture
- Lookup Flow
- File Locations
- Working Memory Format (CLAUDE.md)
- Deep Memory Format (memory/)
- How to Interact
  - Decoding User Input (Tiered Lookup)
  - Adding Memory
  - Recalling Memory
  - Progressive Disclosure
- Bootstrapping
- Conventions
- What Goes Where
- Promotion / Demotion

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [productivity:start](productivity-start.md) - Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, 

## Invoke / install

- Invoke: `/productivity:memory-management`  (Skill tool: `productivity:memory-management`)
- Install: `bundled with Claude desktop (Cowork plugin 'productivity'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
