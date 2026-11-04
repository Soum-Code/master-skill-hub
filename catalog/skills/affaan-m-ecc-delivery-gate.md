# delivery-gate

> Stop hook that blocks Claude from finishing until quality checks pass. Detects rationalization patterns (surface text heuristics), stale learning logs (filesystem mtime), and low disk space. Complements self-audit by mechanically enforcing learning capture habits. Use when Claude should be mechanically blocked from declaring work finished before quality checks and learning capture actually pass.

| | |
|---|---|
| **ID** | `affaan-m/ECC:delivery-gate` |
| **Pack** | AI / ML Engineering (also: Research & Learning) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 134 lines in SKILL.md, 2 file(s) |

## When to use it

- Use when Claude should be mechanically blocked from declaring work finished before quality checks and learning capture actually pass.

## What it says up front

> A **Stop hook** that checks three things before Claude can finish a session, using only **deterministic checks** — file modification timestamps, disk usage, and regex patterns on the transcript text. No AI inference.

## How it is structured

The skill's own section headings, in order:

- What It Checks
- Why
- Install
- Learning Libraries
- Configuration
- Examples
- Limitations
- Compatibility
- Quality
- See Also

## What it bundles

- scripts: `hooks/quality-gate.py`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [affaan-m/ECC:continuous-agent-loop](affaan-m-ecc-continuous-agent-loop.md) - Patterns for continuous autonomous agent loops with quality gates, evals, and recovery controls. Use when runn
- [affaan-m/ECC:verification-loop](affaan-m-ecc-verification-loop.md) - Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s

## Invoke / install

- Invoke: `/affaan-m/ECC:delivery-gate`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/delivery-gate --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 14e7b1fd64367840220c4e3a2ce8d66a84115f81b2a71b5e169240af05c278b1 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
