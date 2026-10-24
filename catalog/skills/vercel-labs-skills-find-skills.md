# find-skills

> Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.

| | |
|---|---|
| **ID** | `vercel-labs/skills:find-skills` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/skills](https://github.com/vercel-labs/skills) |
| **License** | MIT |
| **Size** | 142 lines in SKILL.md, 1 file(s) |

## When to use it

- This skill should be used when the user is looking for functionality that might exist as an installable skill.

## What it says up front

> This skill helps you discover and install skills from the open agent skills ecosystem.

## How it is structured

The skill's own section headings, in order:

- When to Use This Skill
- What is the Skills CLI?
- How to Help Users Find Skills
  - Step 1: Understand What They Need
  - Step 2: Check the Leaderboard First
  - Step 3: Search for Skills
  - Step 4: Verify Quality Before Recommending
  - Step 5: Present Options to the User
  - Step 6: Offer to Install
- Common Skill Categories
- Tips for Effective Searches
- When No Skills Are Found

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:example-skill](anthropics-claude-plugins-official-example-skill.md) - This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill tem
- [anthropics/claude-code:Writing Hookify Rules](anthropics-claude-code-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-plugins-official:writing-hookify-rules](anthropics-claude-plugins-official-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 

## Invoke / install

- Invoke: `/vercel-labs/skills:find-skills`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/skills --path skills/find-skills --commit a80e4c9d12d607631249d4d7d059f835d4b2f13a --expect-tree 3345a412fa273126511a93c88265e62d62e2a21e808b99e83333cac20a96df79 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
