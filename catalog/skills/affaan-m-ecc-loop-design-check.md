# loop-design-check

> Design a goal-oriented agent loop or review one for failure modes: spinning, Goodhart-gaming the verifier, or running a wrong answer to completion. Covers machine-decidable goals, loop types, plan/build/judge skeletons, and runaway prevention; mechanism wiring lives in autonomous-loops. Use when designing, writing, or checking an agent loop. 中文触发：写 loop、设计 loop、做一个 loop、检查 loop 对不对、loop 体检、loop 会不会跑飞、可判定目标、五个崩法、plan build judge。

| | |
|---|---|
| **ID** | `affaan-m/ECC:loop-design-check` |
| **Pack** | Software Development (also: Productivity & Automation, Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 144 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when designing, writing, or checking an agent loop.

## What it says up front

> ① the task repeats weekly or more ② verification can be automated ③ the token budget can take it ④ the agent has tools that actually *run and see the result*

## How it is structured

The skill's own section headings, in order:

- When to use / not
- Red-line premise: two levels of feedback
- Action 1 — Write a loop (5 steps)
  - Step 0 · Subtract first: should you even build it? (4-condition gate, any miss = veto)
  - Step 1 · Define a *machine-decidable* goal (the hard part — the loop lives or dies here)
  - Step 2 · Pick the loop type
  - Step 3 · Pick a skeleton
  - Step 4 · Add damping (against oscillation / runaway)
  - Step 5 · Land in three stages (don't go fully automatic on day one)
- Action 2 — Review a loop (checklist = five failure modes)
- Worked example — reviewing a "nightly green-keeper" loop
- One-line close

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:continuous-agent-loop](affaan-m-ecc-continuous-agent-loop.md) - Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. Use when runn
- [affaan-m/ECC:orch-build-mvp](affaan-m-ecc-orch-build-mvp.md) - Orchestrate bootstrapping a working MVP from a design or spec document — ingest the SDD/PRD, plan thin vertica
- [affaan-m/ECC:typescript-patterns](affaan-m-ecc-typescript-patterns.md) - TypeScript patterns for strict, type-safe, maintainable code in modern TypeScript and JavaScript applications.

## Invoke / install

- Invoke: `/affaan-m/ECC:loop-design-check`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/loop-design-check --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e78223344b44a6e95b884ad48c73eb264a5909e79b5f87a6f581ae08b48e57ca --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
