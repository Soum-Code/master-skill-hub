# eval-harness

> Eval-driven development (EDD) framework for AI coding sessions — define capability and regression evals before coding, grade with code-based, model-based, rule, or human graders, and track pass@k and pass^k reliability. Use when defining pass/fail criteria for agent tasks, measuring agent reliability, building regression suites for prompt or agent changes, or benchmarking across model versions.

| | |
|---|---|
| **ID** | `affaan-m/ECC:eval-harness` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 306 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when defining pass/fail criteria for agent tasks, measuring agent reliability, building regression suites for prompt or agent changes, or benchmarking across model versions.

## What it says up front

> A formal evaluation framework for Claude Code sessions, implementing eval-driven development (EDD) principles.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Philosophy
- Eval Types
  - Capability Evals
  - Regression Evals
- Grader Types
  - 1. Code-Based Grader
  - 2. Model-Based Grader
  - 3. Human Grader
- Metrics
  - pass@k
  - pass^k
- Eval Workflow
  - 1. Define (Before Coding)
  - 2. Implement
  - 3. Evaluate
  - 4. Report
- Integration Patterns
  - Pre-Implementation
  - During Implementation
  - Post-Implementation
- Eval Storage
- Best Practices
- Example: Adding Authentication
- Local Framework Utilities
- Product Evals (v1.8)
  - Grader Types
  - pass@k Guidance
  - Eval Anti-Patterns
  - Minimal Eval Artifact Layout

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:agent-eval](affaan-m-ecc-agent-eval.md) - Head-to-head comparison of coding agents (Claude Code, Aider, Codex, etc.) on custom tasks with pass rate, cos
- [affaan-m/ECC:dmux-workflows](affaan-m-ecc-dmux-workflows.md) - Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows 
- [affaan-m/ECC:claude-devfleet](affaan-m-ecc-claude-devfleet.md) - Orchestrate multi-agent coding tasks via Claude DevFleet — plan projects, dispatch parallel agents in isolated
- [affaan-m/ECC:cost-aware-llm-pipeline](affaan-m-ecc-cost-aware-llm-pipeline.md) - Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic,

## Invoke / install

- Invoke: `/affaan-m/ECC:eval-harness`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/eval-harness --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 11d1fedf34d23eac7464422646a8dea9e37186ed0200fd94455e930ad4bc52d7 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
