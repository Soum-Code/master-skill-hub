# data-context-extractor

> Generate or improve a company-specific data analysis skill by extracting tribal knowledge from analysts. BOOTSTRAP MODE - Triggers: "Create a data context skill", "Set up data analysis for our warehouse", "Help me create a skill for our database", "Generate a data skill for [company]" → Discovers schemas, asks key questions, generates initial skill with reference files ITERATION MODE - Triggers: "Add context about [domain]", "The skill needs more info about [topic]", "Update the data skill with [metrics/tables/terminology]", "Improve the [domain] reference" → Loads existing skill, asks targeted questions, appends/updates reference files Use when data analysts want Claude to understand their company's specific data warehouse, terminology, metrics definitions, and common query patterns.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:data-context-extractor` |
| **Pack** | Data & Analytics |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 228 lines in SKILL.md, 6 file(s) |

## When to use it

- BOOTSTRAP MODE - Triggers: "Create a data context skill", "Set up data analysis for our warehouse", "Help me create a skill for our database", "Generate a data skill for [company]" → Discovers schemas, asks key questions, generates initial skill with reference.

## What it says up front

> A meta-skill that extracts company-specific data knowledge from analysts and generates tailored data analysis skills.

## How it is structured

The skill's own section headings, in order:

- How It Works
- Bootstrap Mode
  - Phase 1: Database Connection & Discovery
  - Phase 2: Core Questions (Ask These)
  - Phase 3: Generate the Skill
  - Phase 4: Package and Deliver
- Iteration Mode
  - Step 1: Load Existing Skill
  - Step 2: Identify the Gap
  - Step 3: Targeted Discovery
  - Step 4: Update and Repackage
- Reference File Standards
  - For Table Documentation
  - For Metrics Documentation
  - For Entity Documentation
- Quality Checklist

## What it bundles

- scripts: `scripts/package_data_skill.py`
- reference docs: `references/domain-template.md`, `references/example-output.md`, `references/skill-template.md`, `references/sql-dialects.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/claude-code:Command Development](anthropics-claude-code-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com
- [anthropics/claude-plugins-official:command-development](anthropics-claude-plugins-official-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com
- [anthropics/claude-code:Writing Hookify Rules](anthropics-claude-code-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-plugins-official:writing-hookify-rules](anthropics-claude-plugins-official-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:data-context-extractor`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path data/skills/data-context-extractor --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 8f9a1b80d1ed85874e769b790338cf0afbea18ab8207780e5f84e706702dc70f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
