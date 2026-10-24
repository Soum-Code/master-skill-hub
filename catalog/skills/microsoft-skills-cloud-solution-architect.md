# cloud-solution-architect

> Transform the agent into a Cloud Solution Architect following Azure Architecture Center best practices. Use when designing cloud architectures, reviewing system designs, selecting architecture styles, applying cloud design patterns, making technology choices, or conducting Well-Architected Framework reviews.

| | |
|---|---|
| **ID** | `microsoft/skills:cloud-solution-architect` |
| **Pack** | MLOps / DevOps / Cloud (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 318 lines in SKILL.md, 8 file(s) |

## When to use it

- Use when designing cloud architectures, reviewing system designs, selecting architecture styles, applying cloud design patterns, making technology choices, or conducting Well-Architected Framework reviews.

## What it says up front

> Design well-architected, production-grade cloud systems following Azure Architecture Center best practices. This skill provides:

## How it is structured

The skill's own section headings, in order:

- Overview
- Ten Design Principles for Azure Applications
- Architecture Styles
  - Selection Criteria
- Cloud Design Patterns
  - Messaging & Communication
  - Reliability & Resilience
  - Data Management
  - Design & Structure
  - Security & Access
  - Deployment & Scaling
- Technology Choices
  - Decision Framework
- Best Practices
- Performance Antipatterns
- Mission-Critical Design
- Well-Architected Framework (WAF) Pillars
  - WAF Tradeoff Matrix
- Architecture Review Workflow
  - Step 1: Identify Requirements
  - Step 2: Select Architecture Style
  - Step 3: Choose Technology Stack
  - Step 4: Apply Design Patterns
  - Step 5: Address Cross-Cutting Concerns
  - Step 6: Validate Against WAF Pillars
  - Step 7: Document Decisions
- References
- Source

## What it bundles

- reference docs: `references/architecture-styles.md`, `references/best-practices.md`, `references/design-patterns.md`, `references/design-principles.md`, `references/mission-critical.md`, `references/performance-antipatterns.md`, `references/technology-choices.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [engineering:system-design](engineering-system-design.md) - Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "s
- [engineering:architecture](engineering-architecture.md) - Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka 
- [vercel-labs/agent-skills:web-design-guidelines](vercel-labs-agent-skills-web-design-guidelines.md) - Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility

## Invoke / install

- Invoke: `/microsoft/skills:cloud-solution-architect`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/cloud-solution-architect --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 00e36216a8312dc4023167cf9d25dfaba84a1d151b7a111a7a0c892cc375f88d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
