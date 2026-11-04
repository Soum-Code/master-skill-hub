# skill-stocktake

> Use when auditing Claude skills and commands for quality. Supports Quick Scan (changed skills only) and Full Stocktake modes with sequential subagent batch evaluation.

| | |
|---|---|
| **ID** | `affaan-m/ECC:skill-stocktake` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Spec-driven Dev Workflow, Finance & Accounting, Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 247 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when auditing Claude skills and commands for quality.

## What it says up front

> Slash command (`/skill-stocktake`) that audits all Claude skills and commands using a quality checklist + AI holistic judgment. Supports two modes: Quick Scan for recently changed skills, and Full Stocktake for a complete review.

## How it is structured

The skill's own section headings, in order:

- Scope
  - Targeting a specific project
- Modes
- Quick Scan Flow
- Full Stocktake Flow
  - Phase 1 — Inventory
  - Phase 2 — Quality Evaluation
  - Phase 3 — Summary Table
  - Phase 4 — Consolidation
- Results File Schema
- Notes

## What it bundles

- scripts: `scripts/quick-diff.sh`, `scripts/save-results.sh`, `scripts/scan.sh`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [affaan-m/ECC:skill-host-compat](affaan-m-ecc-skill-host-compat.md) - Lint ECC skills for Codex/Cursor-safe frontmatter and Claude-only substitutions before a skill PR.
- [anthropics/claude-plugins-official:claude-md-improver](anthropics-claude-plugins-official-claude-md-improver.md) - Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix
- [affaan-m/ECC:context-budget](affaan-m-ecc-context-budget.md) - Routes live context checks to the native Codex or Claude Code meter without scanning files, and performs a bou
- [anthropics/claude-plugins-official:session-report](anthropics-claude-plugins-official-session-report.md) - Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive p

## Invoke / install

- Invoke: `/affaan-m/ECC:skill-stocktake`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/skill-stocktake --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 334e4374447ec5347452d9dabb8090758b3a996c8cb8e4494343aeb0a087b30f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
