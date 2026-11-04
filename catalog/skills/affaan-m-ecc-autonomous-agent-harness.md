# autonomous-agent-harness

> Transform Claude Code into a fully autonomous agent system with persistent memory, scheduled operations, computer use, and task queuing. Replaces standalone agent frameworks (Hermes, AutoGPT) by leveraging Claude Code's native crons, dispatch, MCP tools, and memory. Use when the user wants continuous autonomous operation, scheduled tasks, or a self-directing agent loop.

| | |
|---|---|
| **ID** | `affaan-m/ECC:autonomous-agent-harness` |
| **Pack** | Productivity & Automation (also: AI / ML Engineering, Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 272 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants continuous autonomous operation, scheduled tasks, or a self-directing agent loop.

## What it says up front

> Combine Claude Code's session tools with separately configured scheduling, memory, and computer-use integrations. This is a setup pattern, not a bundled always-on runtime.

## How it is structured

The skill's own section headings, in order:

- Consent and Safety Boundaries
- When to Activate
- Architecture
- Core Components
  - 1. Persistent Memory
  - 2. Scheduled Operations (Crons)
  - 3. Dispatch / Remote Agents
  - 4. Computer Use
  - 5. Task Queue
- Replacing Hermes
- Setup Guide
  - Step 1: Configure MCP Servers
  - Step 2: Create Base Crons
  - Step 3: Initialize Memory Graph
  - Step 4: Enable Computer Use (Optional)
- Example Workflows
  - Autonomous PR Reviewer
  - Personal Research Agent
  - Meeting Prep Agent
- Constraints

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:autonomous-loops](affaan-m-ecc-autonomous-loops.md) - Patterns and architectures for autonomous Claude Code loops — from simple sequential pipelines to RFC-driven m
- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h
- [affaan-m/ECC:agentic-os](affaan-m-ecc-agentic-os.md) - Build persistent multi-agent operating systems on Claude Code. Covers kernel architecture, specialist agents, 
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 

## Invoke / install

- Invoke: `/affaan-m/ECC:autonomous-agent-harness`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/autonomous-agent-harness --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree ec12e20a8ffe5d8ebd24e29b3ed7dc8ece08b0590d37369fdd98fe7cbd1a470b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
