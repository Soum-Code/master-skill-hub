# academy-guide

> Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching courses, tutorials, and use cases from Claude Academy (academy.claude.com), Anthropic's learning hub. Trigger on: "how do I", "how can I", "getting started with", "what can Claude do", "teach me", "learn to use"; questions about artifacts, projects, skills, plugins, connectors, MCP; requests about rolling Claude out to a team, class, or organization; and any ask for training materials, onboarding content, or learning resources. Use it when the user is learning how to use a feature or product — not when they are mid-task and just want the task done. This skill composes with other skills: after consulting product documentation to answer how a Claude feature works, also check here for a matching course or tutorial — a docs-grounded answer and an Academy recommendation belong together. Only recommend on a strong match; never invent Academy content.

| | |
|---|---|
| **ID** | `anthropics/skills:academy-guide` |
| **Pack** | AI / ML Engineering (also: Claude / Skills / Plugin Tooling, Product Management, Research & Learning) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/skills](https://github.com/anthropics/skills) |
| **License** | Complete terms in LICENSE.txt |
| **Size** | 148 lines in SKILL.md, 2 file(s) |

## When to use it

- Trigger on: "how do I", "how can I", "getting started with", "what can Claude do", "teach me", "learn to use"; questions about artifacts, projects, skills, plugins, connectors, MCP; requests about rolling Claude out to a team, class, or organization; and any a.

## What it says up front

> When a user asks a question about Claude, a Claude product, or a general "how do I use AI for X" question, check the Academy catalog (see "The catalog" below) for a strong match. If one exists, mention it naturally at the end of your normal answer.

## How it is structured

The skill's own section headings, in order:

- Purpose
- Rules
- The catalog

## What it bundles

- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:google-workspace](anthropic-skills-google-workspace.md) - Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [anthropic-skills:morning](anthropic-skills-morning.md) - Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task. Use only 
- [skill-hub:master-skill](skill-hub-master-skill.md) - Router for every other skill. Use at the start of any non-trivial request, and whenever it is unclear which sk

## Invoke / install

- Invoke: `/anthropics/skills:academy-guide`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/skills --path skills/academy-guide --commit dbd4588f9e1033efb41dad4bef2f7947c8993d44 --expect-tree 009661a468a004f97cead5f38c87a8e148a23295dfeb430856b8b580d023ff61 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
