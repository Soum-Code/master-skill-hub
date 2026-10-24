# linkedin-humanizer

> Remove the AI tells human readers and LinkedIn's AI-slop filter react to in a post or comment: 2026 vocabulary by paragraph density, reveal bridges, staccato fragments, stacked triads, performed sincerity. Tiered rewriter (forensic / strict / aesthetic / all) plus `--mode audit` pass-fail review and `--mode profile` voice profile builder. Not for beating AI detectors (no edit reliably does). Keywords: humanize, de-AI, reads like ChatGPT, AI slop, scrub AI tells, review this draft, audit before posting.

| | |
|---|---|
| **ID** | `linkedin-humanizer` |
| **Pack** | Careers, Jobs & Hiring (also: Documents, Writing & Content, Communication & Collaboration) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | user |
| **License** | not declared |
| **Size** | 176 lines in SKILL.md, 19 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## How it is structured

The skill's own section headings, in order:

- What changed in V3
- When to use
- Input
- Output
- Modes
- The four passes
  - Pass 1: SCRUB (score, then delete or replace)
  - Pass 2: RHYTHM (restore natural variance)
  - Pass 3: ADD (human fingerprints)
  - Pass 4: SELF-CHECK (over-correction guard)
- Non-negotiable rules
- Tier rationale (short version)
- Example
- Files
- Related skills

## What it bundles

- scripts: `scripts/test_detectors.py`
- reference docs: `references/audit-ai-tells.md`, `references/audit-checklist.md`, `references/audit-examples.md`, `references/detector-list.md`, `references/emoji-patterns.md`, `references/examples.md`, `references/rules-explainer.md`, `references/scrub-rules.md` ...
- 7 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Invoke / install

- Invoke: `/linkedin-humanizer`
- Install: `copy the skill folder into ~/.claude/skills/linkedin-humanizer`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
