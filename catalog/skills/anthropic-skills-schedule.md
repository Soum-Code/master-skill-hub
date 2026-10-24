# schedule

> Create or update a scheduled task that runs automatically. Use when the user says things like "every day", "each morning", "remind me in an hour", "run this at noon", or wants to reschedule an existing task.

| | |
|---|---|
| **ID** | `anthropic-skills:schedule` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | not declared |
| **Size** | 43 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user says things like "every day", "each morning", "remind me in an hour", "run this at noon", or wants to reschedule an existing task.

## How it is structured

The skill's own section headings, in order:

- Updating an existing task
- Creating a new task
  - 1. Analyze the session
  - 2. Draft a prompt
  - 3. Choose a taskName
  - 4. Determine scheduling

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [schedule](schedule.md) - Create, update, list or run scheduled cloud agents (routines) on a cron schedule. Use for recurring cloud agen
- [openai/skills:linear](openai-skills-linear.md) - Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets
- [anthropic-skills:morning](anthropic-skills-morning.md) - Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task. Use only 
- [anthropic-skills:explain-usage](anthropic-skills-explain-usage.md) - Explain where this session's tokens went, with one simple chart in plain language. Use when the user says thin

## Invoke / install

- Invoke: `/anthropic-skills:schedule`  (Skill tool: `anthropic-skills:schedule`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
