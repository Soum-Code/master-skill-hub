# council-multi-model

> Add one optional external Codex critique after the existing council has produced a decision draft. Use when an ambiguous, high-consequence decision would benefit from a separate model invocation's attempt to break the synthesis. Requires explicit consent before sending the compact draft and disagreement to OpenAI, labels same-provider reviews honestly, and marks the review absent when the adapter is unavailable.

| | |
|---|---|
| **ID** | `affaan-m/ECC:council-multi-model` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 168 lines in SKILL.md, 2 file(s) |

## When to use it

- Use when an ambiguous, high-consequence decision would benefit from a separate model invocation's attempt to break the synthesis.

## What it says up front

> Run the existing `council` workflow first. This skill adds only one optional post-draft node: ask Codex to attack the council synthesis before the user makes the final decision.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Provider Relationship
- Workflow
  - 1. Finish the normal council draft
  - 2. Build the minimum review packet
  - 3. Ask for transfer consent
  - 4. Run the bounded adapter
  - 5. Present without hiding disagreement
- Persistence
- Related

## What it bundles

- scripts: `scripts/review-with-codex.js`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [affaan-m/ECC:council](affaan-m-ecc-council.md) - Convene a four-voice council for ambiguous decisions, tradeoffs, and go/no-go calls. Use when multiple valid p
- [affaan-m/ECC:production-audit](affaan-m-ecc-production-audit.md) - Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what b

## Invoke / install

- Invoke: `/affaan-m/ECC:council-multi-model`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/council-multi-model --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 3d894501158f63490a3ff7d1162da29be21bac2b4763e1687e1a27c7a539b7ab --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
