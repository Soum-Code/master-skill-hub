# agentic-os

> Build persistent multi-agent operating systems on Claude Code. Covers kernel architecture, specialist agents, slash commands, file-based memory, scheduled automation, and state management without external databases. Use when building a persistent multi-agent system on Claude Code with its own memory, commands, and scheduling.

| | |
|---|---|
| **ID** | `affaan-m/ECC:agentic-os` |
| **Pack** | Software Development (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 389 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building a persistent multi-agent system on Claude Code with its own memory, commands, and scheduling.

## What it says up front

> Treat Claude Code as a persistent runtime / operating system rather than a chat session. This skill codifies the architecture used by production agentic setups: a kernel config that routes tasks to specialist agents, persistent file-based memory, scheduled automation, and a JSON/markdown data layer.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Architecture Overview
  - Layer Responsibilities
- The Kernel
  - Kernel Structure
  - Key Principle
- Specialist Agents
  - Agent Definition Format
  - Multi-Agent Collaboration Pattern
- Commands and Daily Workflows
  - Command Structure
  - Standard Command Set
  - Activating Commands
- Persistent Memory
  - Memory Directory Structure
  - Daily Log Format
  - Auto-Reflection Pattern
- Scheduled Automation
  - macOS: LaunchAgent
  - Linux: systemd Timer
  - Cross-Platform: pm2
- Data Layer
  - JSON for Structured State
  - Markdown for Narrative
  - Schema Evolution
- Anti-Patterns
  - Monolithic Single Agent
  - Stateless Sessions
  - Hardcoded Credentials
  - External Database for Simple State

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:swift-protocol-di-testing](affaan-m-ecc-swift-protocol-di-testing.md) - Protocol-based dependency injection for testable Swift code — mock file system, network, and external APIs usi
- [affaan-m/ECC:autonomous-loops](affaan-m-ecc-autonomous-loops.md) - Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven m
- [affaan-m/ECC:autonomous-agent-harness](affaan-m-ecc-autonomous-agent-harness.md) - Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations, compu
- [affaan-m/ECC:vue-patterns](affaan-m-ecc-vue-patterns.md) - Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management, 

## Invoke / install

- Invoke: `/affaan-m/ECC:agentic-os`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/agentic-os --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 38b925a3937bd34d032c3bca0c63b3e1f255fa703c75f30b61d2127e61ebd69d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
