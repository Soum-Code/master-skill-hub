# routines

> Set up recurring champion routines as Claude Code scheduled tasks. Use when a champion wants work like a weekly patterns digest, a stale guidance check, or a monthly lead update to happen without kicking it off by hand.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:routines` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 57 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a champion wants work like a weekly patterns digest, a stale guidance check, or a monthly lead update to happen without kicking it off by hand.

## What it says up front

> Say in one line what you'll make: a ready-to-paste `/schedule` line for each routine you pick, adapted to this repo.

## How it is structured

The skill's own section headings, in order:

- Start here
- Then

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:schedule](anthropic-skills-schedule.md) - Create or update a scheduled task that runs automatically. Use when the user says things like "every day", "ea
- [schedule](schedule.md) - Create, update, list or run scheduled cloud agents (routines) on a cron schedule. Use for recurring cloud agen
- [affaan-m/ECC:autonomous-agent-harness](affaan-m-ecc-autonomous-agent-harness.md) - Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations, compu
- [anthropics/claude-plugins-official:office-hours](anthropics-claude-plugins-official-office-hours.md) - Set up and run Claude Code office hours, including the calendar event when the champion's own calendar connect

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:routines`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/champion-kit/skills/routines --commit 0412be76f50ab4f4f8abff3753efa9269fbbca5b --expect-tree 0298f1b1a5cbd268dfbeaf6410c01f573ed7909a7b4abad89ca7feae103b6c64 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
