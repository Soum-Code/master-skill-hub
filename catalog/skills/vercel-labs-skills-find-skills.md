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

- [google-gemini/gemini-cli:skill-creator](google-gemini-gemini-cli-skill-creator.md) - Guide for creating effective skills. This skill should be used when users want to create a new skill (or updat
- [affaan-m/ECC:ecc-guide](affaan-m-ecc-ecc-guide.md) - Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install 
- [affaan-m/ECC:skill-scout](affaan-m-ecc-skill-scout.md) - Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the us
- [anthropics/claude-plugins-official:example-skill](anthropics-claude-plugins-official-example-skill.md) - This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill tem

## Invoke / install

- Invoke: `/vercel-labs/skills:find-skills`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/skills --path skills/find-skills --commit d3701c11b1101251af14c9d148f026e1a47ebe17 --expect-tree 3345a412fa273126511a93c88265e62d62e2a21e808b99e83333cac20a96df79 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
