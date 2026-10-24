# morning

> Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task. Use only when the user explicitly asks to run, see, or set up their morning brief, or if they invoke /morning by name. A question about their day, schedule, or calendar is not by itself a request for the brief; answer it directly instead.

| | |
|---|---|
| **ID** | `anthropic-skills:morning` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | not declared |
| **Size** | 153 lines in SKILL.md, 3 file(s) |

## When to use it

- Use only when the user explicitly asks to run, see, or set up their morning brief, or if they invoke /morning by name.

## How it is structured

The skill's own section headings, in order:

- Context
- Setup
- Gather
- Sort
- Write
  - Visual anchor
  - Important things
  - Sections
  - The button
- Build
- Verify
- Voice
- Design
- Ground rules

## What it bundles

- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:schedule](anthropic-skills-schedule.md) - Create or update a scheduled task that runs automatically. Use when the user says things like "every day", "ea
- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [productivity:task-management](productivity-task-management.md) - Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, want
- [anthropics/skills:academy-guide](anthropics-skills-academy-guide.md) - Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product

## Invoke / install

- Invoke: `/anthropic-skills:morning`  (Skill tool: `anthropic-skills:morning`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
