# council

> Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid paths exist and you need structured disagreement before choosing.

| | |
|---|---|
| **ID** | `affaan-m/ECC:council` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 205 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when multiple valid paths exist and you need structured disagreement before choosing.

## What it says up front

> Convene four advisors for ambiguous decisions: - the in-context Claude voice - a Skeptic subagent - a Pragmatist subagent - a Critic subagent

## How it is structured

The skill's own section headings, in order:

- When to Use
- When NOT to Use
- Roles
- Workflow
  - 1. Extract the real question
  - 2. Gather only the necessary context
  - 3. Form the Architect position first
  - 4. Launch three independent voices in parallel
  - 5. Synthesize with bias guardrails
  - 6. Present a compact verdict
- Persistence Rule
- Multi-Round Follow-up
- Anti-Patterns
- Related Skills
- Example

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:council-multi-model](affaan-m-ecc-council-multi-model.md) - Add one optional external Codex critique after the existing council has produced a decision draft. Use when an

## Invoke / install

- Invoke: `/affaan-m/ECC:council`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/council --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree af476c4b33465b23364b9365260fbfbca9655452b41f9343e25a0327fb058de9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
