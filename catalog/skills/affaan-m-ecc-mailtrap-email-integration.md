# mailtrap-email-integration

> Guides agents through integrating transactional email sending via Mailtrap's Email API, including sandbox testing, domain verification, and API authentication. Use when implementing email-sending features, debugging delivery issues, or setting up safe dev/staging email testing.

| | |
|---|---|
| **ID** | `affaan-m/ECC:mailtrap-email-integration` |
| **Pack** | Software Development (also: Communication & Collaboration, Documents, Writing & Content) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 78 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when implementing email-sending features, debugging delivery issues, or setting up safe dev/staging email testing.

## What it says up front

> Patterns for adding transactional email sending to an application using Mailtrap's Email API and Sandbox, covering authentication, environment separation, and common delivery pitfalls.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concepts
- Code Examples
- Anti-Patterns
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:email-ops](affaan-m-ecc-email-ops.md) - Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use
- [microsoft/skills:continual-learning](microsoft-skills-continual-learning.md) - Guide for implementing continual learning in AI coding agents — hooks, memory scoping, reflection patterns. Us
- [affaan-m/ECC:agent-runtime-gateway-smoke-test](affaan-m-ecc-agent-runtime-gateway-smoke-test.md) - Verify a local agent API, temporary gateway tunnel, and remote sandbox callback with a tool-free task, then re
- [affaan-m/ECC:ralphinho-rfc-pipeline](affaan-m-ecc-ralphinho-rfc-pipeline.md) - Split an RFC into a multi-agent execution DAG — decompose into work units with dependencies and acceptance tes

## Invoke / install

- Invoke: `/affaan-m/ECC:mailtrap-email-integration`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/mailtrap-email-integration --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 9cd3152568017d731e19ddcea3f67e536a274c229f71e9dfcb16e00de099df0c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
