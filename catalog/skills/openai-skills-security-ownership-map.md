# security-ownership-map

> Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for graph databases and visualization. Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters). Do not trigger for general maintainer lists or non-security ownership questions.

| | |
|---|---|
| **ID** | `openai/skills:security-ownership-map` |
| **Pack** | Security & Privacy |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 207 lines in SKILL.md, 8 file(s) |

## When to use it

- Trigger only when the user explicitly wants a security-oriented ownership or bus-factor analysis grounded in git history (for example: orphaned sensitive code, security maintainers, CODEOWNERS reality checks for risk, sensitive hotspots, or ownership clusters).

## How it is structured

The skill's own section headings, in order:

- Overview
- Requirements
- Workflow
- Quick start
- Sensitivity rules
- Output artifacts
- LLM query helper
- Basic security queries
  - Summary format (default)
- Graph persistence
- Notes

## What it bundles

- scripts: `scripts/build_ownership_map.py`, `scripts/community_maintainers.py`, `scripts/query_ownership.py`, `scripts/run_ownership_map.py`
- reference docs: `references/neo4j-import.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:security-threat-model](openai-skills-security-threat-model.md) - Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse pat
- [openai/skills:security-best-practices](openai-skills-security-best-practices.md) - Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only 

## Invoke / install

- Invoke: `/openai/skills:security-ownership-map`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/security-ownership-map --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 9e3abb15ab65c2e5818d6f05d207c8d5534a9836fb9434b71f2201c47bdd7980 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
