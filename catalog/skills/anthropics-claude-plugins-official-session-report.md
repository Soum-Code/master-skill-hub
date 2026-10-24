# session-report

> Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:session-report` |
| **Pack** | Data & Analytics (also: Documents, Writing & Content, Operations & Business, Productivity & Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 43 lines in SKILL.md, 3 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Produce a self-contained HTML report of Claude Code usage and save it to the current working directory.

## How it is structured

The skill's own section headings, in order:

- Steps
- Notes

## What it bundles

- scripts: `analyze-sessions.mjs`
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [bm:session-report](bm-session-report.md) - Generate a session report with token usage estimates, work summary, and outcomes
- [init](init.md) - Initialize a project with a CLAUDE.md that documents the codebase for future sessions.
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:session-report`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/session-report/skills/session-report --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree eda13751d8037ae5701489074190dc45d4a9a6f04d147f6d6c24a48aafe8988e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
