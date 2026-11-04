# token-card

> Render a token-usage stat card from local Claude Code, Codex, Gemini CLI, and OpenCode session logs and commit it into the repository as a file. Use when someone wants a current usage figure in a README, or asks for a shareable card of their coding-agent activity.

| | |
|---|---|
| **ID** | `affaan-m/ECC:token-card` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 122 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when someone wants a current usage figure in a README, or asks for a shareable card of their coding-agent activity.

## What it says up front

> Produce an SVG card summarising this machine's AI coding agent usage — total tokens, equivalent API cost, current streak, and the split across agents — and write it into the working tree as a file the README can reference.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- The tool this runs
- Workflow
- Output
- Notes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:cost-tracking](affaan-m-ecc-cost-tracking.md) - Track and report Claude Code token usage, spending, and budgets from the local ECC cost-tracker metrics log. U
- [affaan-m/ECC:dmux-workflows](affaan-m-ecc-dmux-workflows.md) - Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows 
- [anthropics/claude-plugins-official:session-report](anthropics-claude-plugins-official-session-report.md) - Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive p
- [anthropics/claude-plugins-official:claude-security](anthropics-claude-plugins-official-claude-security.md) - Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's 

## Invoke / install

- Invoke: `/affaan-m/ECC:token-card`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/token-card --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 74e7ec759cb002487ec2ef524dcb24f665a6ce4f22b1b049942628c364128306 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
