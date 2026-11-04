# santa-method

> Multi-agent adversarial verification: two independent reviewers with the same rubric must both pass before output ships, with a fix-and-re-review convergence loop and human escalation cap. Use when gating publishing, production deploys, compliance or brand-sensitive content, or hallucination-prone claims before they ship.

| | |
|---|---|
| **ID** | `affaan-m/ECC:santa-method` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 308 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when gating publishing, production deploys, compliance or brand-sensitive content, or hallucination-prone claims before they ship.

## What it says up front

> Multi-agent adversarial verification framework. Make a list, check it twice. If it's naughty, fix it until it's nice.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Architecture
- Phase Details
  - Phase 1: Make a List (Generate)
  - Phase 2: Check It Twice (Independent Dual Review)
  - Rubric Design
  - Phase 3: Naughty or Nice (Verdict Gate)
  - Phase 4: Fix Until Nice (Convergence Loop)
- Implementation Patterns
  - Pattern A: Claude Code Subagents (Recommended)
  - Pattern B: Sequential Inline (Fallback)
  - Pattern C: Batch Sampling
- Failure Modes and Mitigations
- Integration with Other Skills
- Metrics
- Cost Analysis

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:verification-loop](affaan-m-ecc-verification-loop.md) - Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s
- [affaan-m/ECC:ralphinho-rfc-pipeline](affaan-m-ecc-ralphinho-rfc-pipeline.md) - Split an RFC into a multi-agent execution DAG — decompose into work units with dependencies and acceptance tes

## Invoke / install

- Invoke: `/affaan-m/ECC:santa-method`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/santa-method --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 1e911102dd807866ca1cbd2196cc8ca3f0f348c2f11f4d3bfc18ac143c385273 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
