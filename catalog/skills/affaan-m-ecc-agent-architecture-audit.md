# agent-architecture-audit

> Full-stack diagnostic for agent and LLM applications. Audits the 12-layer agent stack for wrapper regression, memory pollution, tool discipline failures, hidden repair loops, and rendering corruption. Produces severity-ranked findings with code-first fixes. Essential for developers building agent applications, autonomous loops, or any LLM-powered feature. Use when an agent or LLM feature misbehaves and the failing layer is unknown, or before shipping an agent stack.

| | |
|---|---|
| **ID** | `affaan-m/ECC:agent-architecture-audit` |
| **Pack** | AI / ML Engineering (also: Finance & Accounting, Security & Privacy, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 258 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when an agent or LLM feature misbehaves and the failing layer is unknown, or before shipping an agent stack.

## What it says up front

> A diagnostic workflow for agent systems that hide failures behind wrapper layers, stale memory, retry loops, or transport/rendering mutations.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- The 12-Layer Stack
- Common Failure Patterns
  - 1. Wrapper Regression
  - 2. Memory Contamination
  - 3. Tool Discipline Failure
  - 4. Rendering/Transport Corruption
  - 5. Hidden Agent Layers
- Audit Workflow
  - Phase 1: Scope
  - Phase 2: Evidence Collection
  - Phase 3: Failure Mapping
  - Phase 4: Fix Strategy
- Severity Model
- Output Format
- Quick Diagnostic Questions
- Anti-Patterns to Avoid
- Report Schema
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:chatgpt-apps](openai-skills-chatgpt-apps.md) - Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widge
- [affaan-m/ECC:verification-loop](affaan-m-ecc-verification-loop.md) - Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s
- [affaan-m/ECC:search-first](affaan-m-ecc-search-first.md) - Research-before-coding workflow: search npm/PyPI, MCP servers, skills, and GitHub for existing tools before wr

## Invoke / install

- Invoke: `/affaan-m/ECC:agent-architecture-audit`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/agent-architecture-audit --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 58b6a9b5f260d1b3f80684afaa417a53d8d5bcbb47e247e10c6fb3d278b5758f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
