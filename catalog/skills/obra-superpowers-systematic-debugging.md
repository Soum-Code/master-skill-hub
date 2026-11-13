# systematic-debugging

> Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes

| | |
|---|---|
| **ID** | `obra/superpowers:systematic-debugging` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [obra/superpowers](https://github.com/obra/superpowers) |
| **License** | MIT |
| **Size** | 284 lines in SKILL.md, 6 file(s) |

## When to use it

- Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes.

## What it says up front

> If you haven't completed Phase 1, you cannot propose fixes.

## How it is structured

The skill's own section headings, in order:

- Overview
- The Iron Law
- When to Use
- The Four Phases
  - Phase 1: Root Cause Investigation
  - Phase 2: Pattern Analysis
  - Phase 3: Hypothesis and Testing
  - Phase 4: Implementation
- Red Flags - STOP and Follow Process
- your human partner's Signals You're Doing It Wrong
- Common Rationalizations
- Quick Reference
- When Process Reveals "No Root Cause"
- Supporting Techniques

## What it bundles

- scripts: `condition-based-waiting-example.ts`, `find-polluter.sh`
- 3 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [bm:debug](bm-debug.md) - Systematic debugging with persistent state across context resets
- [affaan-m/ECC:orch-fix-defect](affaan-m-ecc-orch-fix-defect.md) - Orchestrate fixing a bug — reproduce it as a failing regression test, fix to green, review, and gated commit —
- [google-gemini/gemini-cli:tui-tester](google-gemini-gemini-cli-tui-tester.md) - Expert guidance for testing Gemini CLI behavior and visual output using terminal automation.
- [vercel-labs/skills:triage](vercel-labs-skills-triage.md) - Identify focused, evidence-backed skills CLI bug fixes worth quuu's attention.

## Invoke / install

- Invoke: `/obra/superpowers:systematic-debugging`
- Install: `python skills/skill-vetter/scripts/install.py obra/superpowers --path skills/systematic-debugging --commit 22f0b463e7a5e579904dd6211a520321035526f7 --expect-tree 9e1fdd5b6a5591d964a1ded4e69511cdd6925f1746647b0da82d825defb087ad --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
