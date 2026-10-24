# security-threat-model

> Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work.

| | |
|---|---|
| **ID** | `openai/skills:security-threat-model` |
| **Pack** | Security & Privacy |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 82 lines in SKILL.md, 5 file(s) |

## When to use it

- Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling.
- Do not trigger for general architecture summaries, code review, or non-security design work.

## How it is structured

The skill's own section headings, in order:

- Quick start
- Workflow
  - 1) Scope and extract the system model
  - 2) Derive boundaries, assets, and entry points
  - 3) Calibrate assets and attacker capabilities
  - 4) Enumerate threats as abuse paths
  - 5) Prioritize with explicit likelihood and impact reasoning
  - 6) Validate service context and assumptions with the user
  - 7) Recommend mitigations and focus paths
  - 8) Run a quality check before finalizing
- Risk prioritization guidance (illustrative, not exhaustive)
- References

## What it bundles

- reference docs: `references/prompt-template.md`, `references/security-controls-and-assets.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:security-best-practices](openai-skills-security-best-practices.md) - Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only 
- [openai/skills:security-ownership-map](openai-skills-security-ownership-map.md) - Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensi
- [engineering:system-design](engineering-system-design.md) - Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "s
- [engineering:testing-strategy](engineering-testing-strategy.md) - Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests fo

## Invoke / install

- Invoke: `/openai/skills:security-threat-model`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/security-threat-model --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree a6abc47c2ccc861c3ab9ab4e0b08169b381c63cb499c582a38c81c67364ec2b3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
