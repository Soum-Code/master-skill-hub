# microsoft-docs

> Understand Microsoft technologies by querying official documentation. Use whenever the user asks how something works, wants tutorials, needs configuration options, limits, quotas, or best practices for any Microsoft technology (Azure, .NET, M365, Windows, Power Platform, etc.)—even if they don't mention "docs." If the question is about understanding a concept rather than writing code, this is the right skill.

| | |
|---|---|
| **ID** | `microsoft/skills:microsoft-docs` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 78 lines in SKILL.md, 1 file(s) |

## When to use it

- Use whenever the user asks how something works, wants tutorials, needs configuration options, limits, quotas, or best practices for any Microsoft technology (Azure, .NET, M365, Windows, Power Platform, etc.)—even if they don't mention "docs." If the question i.

## What it says up front

> Good queries are specific:

## How it is structured

The skill's own section headings, in order:

- Tools
- When to Use
- Query Effectiveness
- When to Fetch Full Page
- Why Use This
- CLI Alternative

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [engineering:documentation](engineering-documentation.md) - Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README",
- [anthropics/claude-code:Skill Development](anthropics-claude-code-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-plugins-official:skill-development](anthropics-claude-plugins-official-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [example-skills:doc-coauthoring](example-skills-doc-coauthoring.md) - Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documen

## Invoke / install

- Invoke: `/microsoft/skills:microsoft-docs`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/microsoft-docs --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 454409784f47dd05987c16437d820240d0b7b7e6c2dd4f833dcfd31dbf2bcbf9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
