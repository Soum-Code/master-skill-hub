# agent-self-evaluation

> Use after completing any non-trivial task. The agent self-rates its output on 5 axes — accuracy, completeness, clarity, actionability, conciseness — with concrete evidence per criterion. Produces a structured 1-5 scorecard with specific improvement suggestions.

| | |
|---|---|
| **ID** | `affaan-m/ECC:agent-self-evaluation` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 183 lines in SKILL.md, 7 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> After completing a complex task, the agent pauses to rate its own output against a structured 5-axis rubric. This is NOT a pass/fail gate — it's a deliberate reflection step that catches omissions, flags overconfidence, and surface areas for improvement before the user has to.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concepts
  - The 5 Evaluation Axes
  - Scoring Scale
  - The Evidence Rule
- Workflow
  - Step 1: Collect the Raw Material
  - Step 2: Score Each Axis Independently
  - Step 3: Produce the Evaluation Report
  - Step 4: Apply the Improvement
- Code Examples
  - Example: Good Evaluation (Score 4+)
  - Example: Weak Evaluation (Score 2-3)
- Anti-Patterns
  - "Everything is a 5"
  - Over-penalizing for scope creep
  - Using the evaluation to re-litigate
  - Mixing personal preference with objective gaps
- Best Practices
- Related Skills

## What it bundles

- scripts: `scripts/evaluate.py`
- reference docs: `references/evaluation-criteria.md`, `references/hook-integration.md`
- 3 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Invoke / install

- Invoke: `/affaan-m/ECC:agent-self-evaluation`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/agent-self-evaluation --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree cae810d973d352e8a8e75ec6d0e97de4eeb79fffa68335ad3b75cf5b4c49756f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
