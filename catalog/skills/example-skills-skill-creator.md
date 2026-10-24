# skill-creator

> Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

| | |
|---|---|
| **ID** | `example-skills:skill-creator` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Software Development) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `example-skills` v3b3fad96af16 - [anthropics/skills](https://github.com/anthropics/skills) |
| **License** | Apache-2.0 |
| **Size** | 486 lines in SKILL.md, 18 file(s) |

## When to use it

- Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

## What it says up front

> A skill for creating new skills and iteratively improving them.

## How it is structured

The skill's own section headings, in order:

- Communicating with the user
- Creating a skill
  - Capture Intent
  - Interview and Research
  - Write the SKILL.md
  - Skill Writing Guide
  - Writing Style
  - Test Cases
- Running and evaluating test cases
  - Step 1: Spawn all runs (with-skill AND baseline) in the same turn
  - Step 2: While runs are in progress, draft assertions
  - Step 3: As runs complete, capture timing data
  - Step 4: Grade, aggregate, and launch the viewer
  - What the user sees in the viewer
  - Step 5: Read the feedback
- Improving the skill
  - How to think about improvements
  - The iteration loop
- Advanced: Blind comparison
- Description Optimization
  - Step 1: Generate trigger eval queries
  - Step 2: Review with user
  - Step 3: Run the optimization loop
  - How skill triggering works
  - Step 4: Apply the result
  - Package and Present (only if `present_files` tool is available)
- Claude.ai-specific instructions
- Cowork-Specific Instructions
- Reference files

## What it bundles

- scripts: `eval-viewer/generate_review.py`, `scripts/__init__.py`, `scripts/aggregate_benchmark.py`, `scripts/generate_report.py`, `scripts/improve_description.py`, `scripts/package_skill.py`, `scripts/quick_validate.py`, `scripts/run_eval.py` ...
- reference docs: `references/schemas.md`
- 6 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropic-skills:skill-creator](anthropic-skills-skill-creator.md) - Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to c
- [anthropics/claude-code:Skill Development](anthropics-claude-code-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-plugins-official:skill-development](anthropics-claude-plugins-official-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [cowork-plugin-management:create-cowork-plugin](cowork-plugin-management-create-cowork-plugin.md) - Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a pl

## Invoke / install

- Invoke: `/example-skills:skill-creator`  (Skill tool: `example-skills:skill-creator`)
- Install: `claude plugin marketplace add anthropics/skills && claude plugin install example-skills@anthropic-agent-skills`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
