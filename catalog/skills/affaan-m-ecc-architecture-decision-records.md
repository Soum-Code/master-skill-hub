# architecture-decision-records

> Capture architectural decisions as numbered ADR markdown files in docs/adr/ with context, alternatives considered, consequences, and an index README. Use when the user says 'record this decision' or 'ADR this', chooses between frameworks or databases, discusses trade-offs, or asks why the codebase is shaped this way.

| | |
|---|---|
| **ID** | `affaan-m/ECC:architecture-decision-records` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 181 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user says 'record this decision' or 'ADR this', chooses between frameworks or databases, discusses trade-offs, or asks why the codebase is shaped this way.

## What it says up front

> Capture architectural decisions as they happen during coding sessions. Instead of decisions living only in Slack threads, PR comments, or someone's memory, this skill produces structured ADR documents that live alongside the code.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- ADR Format
- Workflow
  - Capturing a New ADR
  - Reading Existing ADRs
  - ADR Directory Structure
  - ADR Index Format
- Decision Detection Signals
- What Makes a Good ADR
  - Do
  - Don't
- ADR Lifecycle
- Categories of Decisions Worth Recording
- Integration with Other Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [engineering:architecture](engineering-architecture.md) - Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka 
- [engineering:documentation](engineering-documentation.md) - Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README",

## Invoke / install

- Invoke: `/affaan-m/ECC:architecture-decision-records`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/architecture-decision-records --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 8ee61bfeccf0612b4946d72bf897d43a35e62b30b5d87c095a5d9bea5659c7df --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
