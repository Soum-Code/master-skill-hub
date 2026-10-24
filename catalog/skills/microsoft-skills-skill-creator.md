# skill-creator

> Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry services. Use when creating new skills or updating existing skills.

| | |
|---|---|
| **ID** | `microsoft/skills:skill-creator` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 1314 lines in SKILL.md, 7 file(s) |

## When to use it

- Use when creating new skills or updating existing skills.

## What it says up front

> Guide for creating skills that extend AI agent capabilities, with emphasis on Azure SDKs and Microsoft Foundry.

## How it is structured

The skill's own section headings, in order:

- About Skills
- Core Principles
  - 1. Concise is Key
  - 2. Fresh Documentation First
  - 3. Degrees of Freedom
  - 4. Progressive Disclosure
- Skill Structure
  - SKILL.md Essentials
  - Bundled Resources (Optional)
- Creating Azure SDK Skills
  - Token Budget Guidelines (REQUIRED)
  - Reference Extraction Guide (REQUIRED)
  - Core Workflow Discipline (REQUIRED)
  - Skill Section Order
  - Required Authentication & Lifecycle Callout (Python)
  - Authentication Pattern (All Languages)
  - Anti-Patterns: What NOT to Do (REQUIRED Reading)
  - Efficiency Validation (REQUIRED - Phase 2)
  - Standard Verb Patterns
  - Language-Specific Patterns
  - Required Best Practices in Every Skill (User-Facing)
  - Example Effective Skills (Benchmark Only Structure-Compliant Skills)
  - Handling Deprecated or Rebranded SDKs
  - Example: Azure SDK Skill Structure
- Skill Creation Process
  - Step 1: Gather SDK Context (REQUIRED)
  - Step 2: Understand the Skill
  - Step 3: Plan Product Area Category
  - Step 4: Create the Skill
  - Step 5: Categorize with Symlinks

## What it bundles

- scripts: `scripts/init_skill.py`, `scripts/package_skill.py`, `scripts/quick_validate.py`
- reference docs: `references/azure-sdk-patterns.md`, `references/output-patterns.md`, `references/workflows.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [microsoft/skills:continual-learning](microsoft-skills-continual-learning.md) - Guide for implementing continual learning in AI coding agents — hooks, memory scoping, reflection patterns. Us
- [microsoft/skills:azure-ai-projects-dotnet](microsoft-skills-azure-ai-projects-dotnet.md) - Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections,
- [microsoft/skills:azure-ai-agents-persistent-dotnet](microsoft-skills-azure-ai-agents-persistent-dotnet.md) - Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messa
- [microsoft/skills:azure-identity-dotnet](microsoft-skills-azure-identity-dotnet.md) - Azure Identity library for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use fo

## Invoke / install

- Invoke: `/microsoft/skills:skill-creator`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/skill-creator --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree e3700edf63750aa55864b37a371ed8283f0efbfc295f7d25b3662c1b0a6b2685 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
