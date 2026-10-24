# task-management

> Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking commitments.

| | |
|---|---|
| **ID** | `productivity:task-management` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `productivity` v1.3.1 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 92 lines in SKILL.md, 1 file(s) |

## When to use it

- Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking commitments.

## What it says up front

> Tasks are tracked in a simple `TASKS.md` file that both you and the user can edit.

## How it is structured

The skill's own section headings, in order:

- File Location
- Dashboard Setup (First Run)
- Format & Template
- How to Interact
- Conventions
- Extracting Tasks

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-code:Plugin Settings](anthropics-claude-code-plugin-settings.md) - This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-conf
- [anthropics/claude-plugins-official:plugin-settings](anthropics-claude-plugins-official-plugin-settings.md) - This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-conf
- [anthropics/claude-code:Writing Hookify Rules](anthropics-claude-code-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-plugins-official:writing-hookify-rules](anthropics-claude-plugins-official-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki

## Invoke / install

- Invoke: `/productivity:task-management`  (Skill tool: `productivity:task-management`)
- Install: `bundled with Claude desktop (Cowork plugin 'productivity'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
