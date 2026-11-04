# docs-governance

> Route broad documentation-governance requests to existing ECC skills and run an opt-in, read-only audit of mapped documentation roles, links, ADR indexes, and evidence references. Use when a user asks for documentation governance, project-knowledge organization, documentation integrity, or a deterministic docs audit without naming a narrower skill.

| | |
|---|---|
| **ID** | `affaan-m/ECC:docs-governance` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 121 lines in SKILL.md, 5 file(s) |

## When to use it

- Use when a user asks for documentation governance, project-knowledge organization, documentation integrity, or a deterministic docs audit without naming a narrower skill.

## What it says up front

> Use this optional router to select the smallest existing ECC capability for a documentation-governance request. The router does not create a parallel project management system and does not make documentation authoritative over code, tests, Issues, or maintainer decisions.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Role Contract
- Intent Routing
- Read-Only Audit
- When to Use
- How It Works
- Examples
- Boundaries

## What it bundles

- scripts: `scripts/audit-docs.py`, `scripts/markdown_links.py`, `scripts/module_audit.py`
- reference docs: `references/artifact-role-contract.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [affaan-m/ECC:module-governance](affaan-m-ecc-module-governance.md) - Establish or maintain a business module's local agent instructions, domain-context links, and interface owners
- [affaan-m/ECC:ecc-guide](affaan-m-ecc-ecc-guide.md) - Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install 
- [affaan-m/ECC:living-docs-governance](affaan-m-ecc-living-docs-governance.md) - Keep a long-lived project's documentation from rotting by assigning existing project docs clear constitution, 
- [anthropic-skills:google-workspace](anthropic-skills-google-workspace.md) - Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch

## Invoke / install

- Invoke: `/affaan-m/ECC:docs-governance`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/docs-governance --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree d051c9a4f8ebc13a4c8463feb9c817788464032c90258d8cd13f317c6c9cc71b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
