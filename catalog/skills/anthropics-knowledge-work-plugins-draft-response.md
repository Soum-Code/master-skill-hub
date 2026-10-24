# draft-response

> Draft a professional customer-facing response tailored to the situation and relationship. Use when answering a product question, responding to an escalation or outage, delivering bad news like a delay or won't-fix, declining a feature request, or replying to a billing issue.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:draft-response` |
| **Pack** | Operations & Business |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 419 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when answering a product question, responding to an escalation or outage, delivering bad news like a delay or won't-fix, declining a feature request, or replying to a billing issue.

## What it says up front

> Draft a professional, customer-facing response tailored to the situation, customer relationship, and communication context.

## How it is structured

The skill's own section headings, in order:

- Usage
- Workflow
  - 1. Understand the Context
  - 2. Research Context
  - 3. Generate the Draft
  - 4. Run Quality Checks
  - 5. Offer Iterations
- Customer Communication Best Practices
  - Core Principles
  - Response Structure
  - Length Guidelines
- Tone and Style Guidelines
  - Tone Spectrum
  - Tone Adjustments by Relationship Stage
  - Writing Style Rules
- Situation-Specific Approaches
- Response Templates for Common Scenarios
  - Acknowledging a Bug Report
  - Acknowledging a Billing or Account Issue
  - Responding to a Feature Request You Won't Build
  - Outage or Incident Communication
  - Following Up After Silence
- Follow-up and Escalation Guidance
  - Follow-up Cadence
  - When to Escalate

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [legal:legal-response](legal-legal-response.md) - Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for 

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:draft-response`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path customer-support/skills/draft-response --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree fb9606a6dd895f31d8a83eaa0fd2d3a23681d9a8d87fcc542fdbb9cfc76abba2 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
