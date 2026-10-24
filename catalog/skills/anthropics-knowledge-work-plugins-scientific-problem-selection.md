# scientific-problem-selection

> This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic scientific decisions. Use this skill when users ask to pitch a new research idea, work through a project problem, evaluate project risks, plan research strategy, navigate decision trees, or get help choosing what scientific problem to work on. Typical requests include "I have an idea for a project", "I'm stuck on my research", "help me evaluate this project", "what should I work on", or "I need strategic advice about my research".

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:scientific-problem-selection` |
| **Pack** | Product Management (also: Spec-driven Dev Workflow, Research & Learning) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 270 lines in SKILL.md, 11 file(s) |

## When to use it

- Use this skill when users ask to pitch a new research idea, work through a project problem, evaluate project risks, plan research strategy, navigate decision trees, or get help choosing what scientific problem to work on.

## What it says up front

> A conversational framework for systematic scientific problem selection based on Fischbach & Walsh's "Problem choice and decision trees in science and engineering" (Cell, 2024).

## How it is structured

The skill's own section headings, in order:

- Getting Started
- Option 1: Pitch an Idea
  - Initial Prompt
  - Response Approach
  - Follow-up Prompt
  - Workflow
- Option 2: Troubleshoot a Problem
  - Initial Prompt
  - Response Approach
  - Follow-up Prompt
  - Workflow
- Option 3: Ask a Strategic Question
  - Initial Prompt
  - Response Approach
  - Follow-up Prompt
  - Workflow
- Core Framework Concepts
  - The Central Insight
  - The Time Paradox
  - Evaluation Axes
  - The Risk Paradox
  - The Parameter Paradox
  - The Adversity Principle
- The 9 Skills Overview
- Skill Workflow
- Key Design Principles
- Who Should Use These Skills
  - Graduate Students (Primary Audience)
  - Postdocs
  - Principal Investigators

## What it bundles

- reference docs: `references/01-intuition-pumps.md`, `references/02-risk-assessment.md`, `references/03-optimization-function.md`, `references/04-parameter-strategy.md`, `references/05-decision-tree.md`, `references/06-adversity-planning.md`, `references/07-problem-inversion.md`, `references/08-integration-synthesis.md` ...
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [product-management:write-spec](product-management-write-spec.md) - Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user re
- [anthropics/claude-code:Plugin Settings](anthropics-claude-code-plugin-settings.md) - This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-conf
- [anthropics/claude-plugins-official:plugin-settings](anthropics-claude-plugins-official-plugin-settings.md) - This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-conf
- [bm:explore](bm-explore.md) - Socratic ideation and idea routing — think through ideas before committing to plans

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:scientific-problem-selection`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path bio-research/skills/scientific-problem-selection --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 18b25f7e7641e816ad62f4ea2293469794d3367a20345a2d5c349cd6a8512676 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
