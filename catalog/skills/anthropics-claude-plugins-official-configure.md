# configure

> Set up the Discord channel — save the bot token and review access policy. Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:configure` |
| **Pack** | AI / ML Engineering (also: Communication & Collaboration, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 100 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user pastes a Discord bot token, asks to configure Discord, asks "how do I set this up" or "who can reach me," or wants to check channel status.

## What it says up front

> Writes the bot token to `~/.claude/channels/discord/.env` and orients the user on access policy. The server reads both files at boot.

## How it is structured

The skill's own section headings, in order:

- Dispatch on arguments
  - No args — status and guidance
  - `` — save it
  - `clear` — remove the token
- Implementation notes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash(ls *)`, `Bash(mkdir *)`

## Related skills

- [anthropics/claude-plugins-official:access](anthropics-claude-plugins-official-access.md) - Manage Discord channel access — approve pairings, edit allowlists, set DM/group policy. Use when the user asks
- [anthropics/claude-code:Writing Hookify Rules](anthropics-claude-code-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-plugins-official:writing-hookify-rules](anthropics-claude-plugins-official-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [productivity:task-management](productivity-task-management.md) - Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, want

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:configure`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path external_plugins/discord/skills/configure --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree e29afb65a97f98093466071f467dfdac1b3cff36717096b5c42e999be51d7887 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
