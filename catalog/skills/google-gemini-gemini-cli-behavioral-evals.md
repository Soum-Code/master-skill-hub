# behavioral-evals

> Guidance for creating, running, fixing, and promoting behavioral evaluations. Use when verifying agent decision logic, debugging failures, debugging prompt steering, or adding workspace regression tests.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:behavioral-evals` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 57 lines in SKILL.md, 7 file(s) |

## When to use it

- Use when verifying agent decision logic, debugging failures, debugging prompt steering, or adding workspace regression tests.

## What it says up front

> Behavioral evaluations (evals) are tests that validate the **agent's decision-making** (e.g., tool choice) rather than pure functionality. They are critical for verifying prompt changes, debugging steerability, and preventing regressions.

## How it is structured

The skill's own section headings, in order:

- Overview
- 🔄 Workflow Decision Tree
- 📋 Quick Checklist
  - 1. Setup Workspace
  - 2. Write Assertions
  - 3. Verify
- 📦 Bundled Resources

## What it bundles

- reference docs: `references/creating.md`, `references/fixing.md`, `references/promoting.md`, `references/running.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:continuous-agent-loop](affaan-m-ecc-continuous-agent-loop.md) - Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. Use when runn
- [affaan-m/ECC:healthcare-eval-harness](affaan-m-ecc-healthcare-eval-harness.md) - Patient safety evaluation harness for healthcare application deployments. Automated test suites for CDSS accur
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [anthropics/claude-plugins-official:agent-development](anthropics-claude-plugins-official-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:behavioral-evals`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path .gemini/skills/behavioral-evals --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree beea01ff2c143cf815692f6672d0a9505f57df9f2c5b2008df691f5c7a0c1bf5 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
