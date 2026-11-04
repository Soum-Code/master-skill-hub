# unified-notifications-ops

> Operate notifications as one ECC-native workflow across GitHub, Linear, desktop alerts, hooks, and connected communication surfaces. Use when the real problem is alert routing, deduplication, escalation, or inbox collapse.

| | |
|---|---|
| **ID** | `affaan-m/ECC:unified-notifications-ops` |
| **Pack** | Claude / Skills / Plugin Tooling (also: MLOps / DevOps / Cloud, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 189 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the real problem is alert routing, deduplication, escalation, or inbox collapse.

## What it says up front

> Use this skill when the real problem is not a missing ping. The real problem is a fragmented notification system.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Preferred Surface
- Non-Negotiable Rules
- Event Pipeline
- Default Severity Model
- Workflow
  - 1. Inventory the current surface
  - 2. Decide what deserves interruption
  - 3. Collapse duplicates before adding channels
  - 4. Design the ECC-native workflow
  - 5. Return an action-biased design
- Output Format
- Recommendation Rules
- Good Use Cases
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:google-workspace-ops](affaan-m-ecc-google-workspace-ops.md) - Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and 
- [affaan-m/ECC:email-ops](affaan-m-ecc-email-ops.md) - Evidence-first mailbox triage, drafting, send verification, and sent-mail-safe follow-up workflow for ECC. Use
- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h
- [affaan-m/ECC:deepseek-harness-setup](affaan-m-ecc-deepseek-harness-setup.md) - Install and operate Everything Claude Code (ECC) on the DeepSeek Harness (DSH): native skill roots (~/.dsh/ski

## Invoke / install

- Invoke: `/affaan-m/ECC:unified-notifications-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/unified-notifications-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 9358c3faea50a6956fb4baedd773f28c701ecd6f396a59bbe60bff33d0758eb8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
