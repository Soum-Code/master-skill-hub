# autonomous-loops

> Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven multi-agent DAG systems. Retained for compatibility only: when new autonomous loop guidance is needed, use continuous-agent-loop instead.

| | |
|---|---|
| **ID** | `affaan-m/ECC:autonomous-loops` |
| **Pack** | Spec-driven Dev Workflow (also: Productivity & Automation, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 618 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Patterns, architectures, and reference implementations for running Claude Code autonomously in loops. Covers everything from simple `claude -p` pipelines to full RFC-driven multi-agent DAG orchestration.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Loop Pattern Spectrum
- 1. Sequential Pipeline (`claude -p`)
  - Core Insight
  - Key Design Principles
  - Variations
- 2. NanoClaw REPL
  - How It Works
  - When NanoClaw vs Sequential Pipeline
- 3. Infinite Agentic Loop
  - Architecture: Two-Prompt System
  - The Pattern
  - Implementation via Claude Code Commands
  - Batching Strategy
  - Key Insight: Uniqueness via Assignment
- 4. Continuous Claude PR Loop
  - Core Loop
  - Installation
  - Usage
  - Cross-Iteration Context: SHARED_TASK_NOTES.md
  - CI Failure Recovery
  - Completion Signal
  - Key Configuration
- 5. The De-Sloppify Pattern
  - The Problem
  - Why Not Negative Instructions?
  - The Solution: Separate Pass
  - In a Loop Context
  - Key Insight
- 6. Ralphinho / RFC-Driven DAG Orchestration

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [anthropics/claude-plugins-official:agent-development](anthropics-claude-plugins-official-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [affaan-m/ECC:ralphinho-rfc-pipeline](affaan-m-ecc-ralphinho-rfc-pipeline.md) - Split an RFC into a multi-agent execution DAG — decompose into work units with dependencies and acceptance tes
- [affaan-m/ECC:continuous-agent-loop](affaan-m-ecc-continuous-agent-loop.md) - Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. Use when runn

## Invoke / install

- Invoke: `/affaan-m/ECC:autonomous-loops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/autonomous-loops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 4ae650cc1e8101e5056565d2aa5606490ec7dabfdfc3a118e5bedb51aae6a453 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
