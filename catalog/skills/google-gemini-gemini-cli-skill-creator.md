# skill-creator

> Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Gemini CLI's capabilities with specialized knowledge, workflows, or tool integrations.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:skill-creator` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 520 lines in SKILL.md, 4 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> This skill provides guidance for creating effective skills.

## How it is structured

The skill's own section headings, in order:

- About Skills
  - What Skills Provide
- Core Principles
  - Concise is Key
  - Set Appropriate Degrees of Freedom
  - Anatomy of a Skill
  - Progressive Disclosure Design Principle
- Skill Creation Process
  - Skill Naming
  - Step 1: Understanding the Skill with Concrete Examples
  - Step 2: Planning the Reusable Skill Contents
  - Step 3: Initializing the Skill
  - Step 4: Edit the Skill
  - Step 5: Packaging a Skill
  - Step 6: Installing and Reloading a Skill
  - Step 7: Iterate

## What it bundles

- 3 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:skill-creator](microsoft-skills-skill-creator.md) - Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry service
- [affaan-m/ECC:skill-scout](affaan-m-ecc-skill-scout.md) - Search existing local, marketplace, GitHub, and web skill sources before creating a new skill. Use when the us
- [vercel-labs/skills:find-skills](vercel-labs-skills-find-skills.md) - Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for 
- [google-gemini/gemini-cli:pr-address-comments](google-gemini-gemini-cli-pr-address-comments.md) - Use this skill if the user asks you to help them address GitHub PR comments for their current branch of the Ge

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:skill-creator`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path packages/core/src/skills/builtin/skill-creator --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree b196c180b23f9d706b05bf8f98447fb15fdbe2add6b3c05fe0464aaaa5d4cd33 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
