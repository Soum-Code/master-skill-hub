# agent-sort

> Build an evidence-backed ECC install plan for a specific repo by sorting skills, commands, rules, hooks, and extras into DAILY vs LIBRARY buckets using parallel repo-aware review passes. Use when ECC should be trimmed to what a project actually needs instead of loading the full bundle.

| | |
|---|---|
| **ID** | `affaan-m/ECC:agent-sort` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Spec-driven Dev Workflow, Software Development, AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 217 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when ECC should be trimmed to what a project actually needs instead of loading the full bundle.

## What it says up front

> Use this skill when a repo needs a project-specific ECC surface instead of the default full install.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Non-Negotiable Rules
- Outputs
- Classification Model
- Evidence Sources
- Parallel Review Passes
- Core Workflow
  - 1. Read the repo
  - 2. Build the evidence table
  - 3. Decide DAILY vs LIBRARY
  - 4. Build the install plan
  - 5. Create the optional library router
  - 6. Verify the result
- Handoffs
- Output Format

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:ecc-guide](affaan-m-ecc-ecc-guide.md) - Answer questions about ECC by reading the live repo surface — agents, skills, commands, hooks, rules, install 
- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h
- [affaan-m/ECC:deepseek-harness-setup](affaan-m-ecc-deepseek-harness-setup.md) - Install and operate Everything Claude Code (ECC) on the DeepSeek Harness (DSH): native skill roots (~/.dsh/ski
- [affaan-m/ECC:nanoclaw-repl](affaan-m-ecc-nanoclaw-repl.md) - Operate and extend NanoClaw, ECC's zero-dependency session-aware REPL, with persistent markdown-backed session

## Invoke / install

- Invoke: `/affaan-m/ECC:agent-sort`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/agent-sort --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 4acf1f352b51b03002644b3d0c73174c430031e25bb08f21bad8f080d047c25d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
