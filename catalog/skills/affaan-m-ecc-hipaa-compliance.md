# hipaa-compliance

> HIPAA-specific entrypoint for healthcare privacy and security work. Use when a task is explicitly framed around HIPAA, PHI handling, covered entities, BAAs, breach posture, or US healthcare compliance requirements.

| | |
|---|---|
| **ID** | `affaan-m/ECC:hipaa-compliance` |
| **Pack** | Legal & Compliance |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 80 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a task is explicitly framed around HIPAA, PHI handling, covered entities, BAAs, breach posture, or US healthcare compliance requirements.

## What it says up front

> Use this as the HIPAA-specific entrypoint when a task is clearly about US healthcare compliance. This skill intentionally stays thin and canonical:

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- HIPAA-Specific Guardrails
- Examples
  - Example 1: Product request framed as HIPAA
  - Example 2: Vendor/tooling decision
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:hipaa-compliance`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/hipaa-compliance --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree b4a58f2cd413efa86fd349fc7c4156e68731968a45a25435073d95007c23af26 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
