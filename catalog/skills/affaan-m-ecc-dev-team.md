# dev-team

> Simulate a collaborative dev team session where multiple role-based personas (PM, Architect, Developer, QA) respond to the same problem together in one session. Use when designing a feature, reviewing a proposal, or onboarding a new initiative and you want multi-role perspective without switching agents manually.

| | |
|---|---|
| **ID** | `affaan-m/ECC:dev-team` |
| **Pack** | Communication & Collaboration |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 204 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when designing a feature, reviewing a proposal, or onboarding a new initiative and you want multi-role perspective without switching agents manually.

## What it says up front

> Run a multi-persona session where PM, Architect, Developer, and QA each respond from their own perspective in a single turn.

## How it is structured

The skill's own section headings, in order:

- When to Activate
  - When NOT to Use
- Personas
- Workflow
  - 1. Extract the topic
  - 2. Build a bounded project-context summary
  - 3. Launch four personas in parallel
  - 4. Present all four responses
  - 5. Offer follow-up
- Persistence Rule
- Anti-Patterns
- Relationship to council and team-builder
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:team-agent-orchestration](affaan-m-ecc-team-agent-orchestration.md) - Run team-based orchestration for agent squads: work items with owners and scope, agent Kanban state, branch is
- [affaan-m/ECC:blueprint](affaan-m-ecc-blueprint.md) - Turn a one-line objective into a step-by-step construction plan for multi-session, multi-agent engineering pro

## Invoke / install

- Invoke: `/affaan-m/ECC:dev-team`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/dev-team --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e37fbabb3e4b5be1f88e2429a20c9d6b7b594997b43c08eb032b55a1e06ffca9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
