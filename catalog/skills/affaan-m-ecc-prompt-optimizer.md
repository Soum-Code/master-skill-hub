# prompt-optimizer

> Analyze draft prompts, detect intent and missing context, match ECC commands, skills, and agents, and output a ready-to-paste optimized prompt with diagnosis and rationale — advisory only, never executes the task. Use when the user says 'optimize prompt', 'improve my prompt', 'rewrite this prompt', 'help me prompt', 优化prompt, 改进prompt, 怎么写prompt, or 帮我优化这个指令; not for requests to optimize code or performance.

| | |
|---|---|
| **ID** | `affaan-m/ECC:prompt-optimizer` |
| **Pack** | AI / ML Engineering (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 388 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user says 'optimize prompt', 'improve my prompt', 'rewrite this prompt', 'help me prompt', 优化prompt, 改进prompt, 怎么写prompt, or 帮我优化这个指令; not for requests to optimize code or performance.

## What it says up front

> Analyze a draft prompt, critique it, match it to ECC ecosystem components, and output a complete optimized prompt the user can paste and run.

## How it is structured

The skill's own section headings, in order:

- When to Use
  - Do Not Use When
- How It Works
  - Analysis Pipeline
  - Phase 0: Project Detection
  - Phase 1: Intent Detection
  - Phase 2: Scope Assessment
  - Phase 3: ECC Component Matching
  - Phase 4: Missing Context Detection
  - Phase 5: Workflow & Model Recommendation
- Output Format
  - Section 1: Prompt Diagnosis
  - Section 2: Recommended ECC Components
  - Section 3: Optimized Prompt — Full Version
  - Section 4: Optimized Prompt — Quick Version
  - Section 5: Enhancement Rationale
  - Footer
- Examples
  - Trigger Examples
  - Example 1: Vague Chinese Prompt (Project Detected)
  - Example 2: Moderate English Prompt
  - Example 3: EPIC Project
- Related Components

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:ecc-recipes](affaan-m-ecc-ecc-recipes.md) - Map a described workflow to the right ECC command group with run-order and stop condition, or browse all comma
- [affaan-m/ECC:prompt-caching-strategy](affaan-m-ecc-prompt-caching-strategy.md) - Optimize LLM prompt caching hit rate to reduce API costs and improve latency. Analyzes prompt structure, ident
- [affaan-m/ECC:ecc-guide](affaan-m-ecc-ecc-guide.md) - Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install 
- [affaan-m/ECC:counterparty-channel-discipline](affaan-m-ecc-counterparty-channel-discipline.md) - Per-channel strict prompts, mention gating, silent observation, and a communication autonomy policy for agents

## Invoke / install

- Invoke: `/affaan-m/ECC:prompt-optimizer`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/prompt-optimizer --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 40de9a451387021b6f85038d166b9e192d3fde82ffde81ad1f5bd1e2bb22db4e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
