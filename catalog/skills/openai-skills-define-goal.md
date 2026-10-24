# define-goal

> Help the user define a concrete, measurable goal before starting work, especially when they ask to use the goal tool, create a goal, set an objective, clarify success criteria, or turn a fuzzy intention into a quantitative outcome. Use this skill for goal creation and goal refinement only; it does not manage durable snapshots, decision logs, or long-running execution artifacts.

| | |
|---|---|
| **ID** | `openai/skills:define-goal` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 100 lines in SKILL.md, 3 file(s) |

## When to use it

- Use this skill for goal creation and goal refinement only; it does not manage durable snapshots, decision logs, or long-running execution artifacts.

## How it is structured

The skill's own section headings, in order:

- Overview
- Workflow
- Goal Quality Bar
- Quantification Heuristics
- Clarifying Questions

## What it bundles

- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [product-management:write-spec](product-management-write-spec.md) - Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user re
- [anthropic-skills:chrome-browser](anthropic-skills-chrome-browser.md) - Read this skill before the first step that uses Claude in Chrome, the browser extension whose tools are named 

## Invoke / install

- Invoke: `/openai/skills:define-goal`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/define-goal --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 419d2b48335b6e07174b8ed8b19d1877409f246722559e37ccf0d908a10a54de --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
