# google-workspace-ops

> Operate across Google Drive, Docs, Sheets, and Slides as one workflow surface for plans, trackers, decks, and shared documents. Use when the user needs to find, summarize, edit, migrate, or clean up Google Workspace assets without dropping to raw tool calls.

| | |
|---|---|
| **ID** | `affaan-m/ECC:google-workspace-ops` |
| **Pack** | Spec-driven Dev Workflow (also: Documents, Writing & Content) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 97 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user needs to find, summarize, edit, migrate, or clean up Google Workspace assets without dropping to raw tool calls.

## What it says up front

> This skill is for operating shared docs, spreadsheets, and decks as working systems, not just editing one file in isolation.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Preferred Tool Surface
- Workflow
  - 1. Find the asset
  - 2. Inspect before editing
  - 3. Edit with precision
  - 4. Keep the working system clean
- Output Format
- Good Use Cases

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:investor-materials](affaan-m-ecc-investor-materials.md) - Create and update pitch decks, one-pagers, investor memos, accelerator applications, financial models, and fun
- [anthropic-skills:google-workspace](anthropic-skills-google-workspace.md) - Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch
- [affaan-m/ECC:customer-billing-ops](affaan-m-ecc-customer-billing-ops.md) - Operate customer billing workflows such as subscriptions, refunds, churn triage, billing-portal recovery, and 
- [affaan-m/ECC:unified-notifications-ops](affaan-m-ecc-unified-notifications-ops.md) - Operate notifications as one ECC-native workflow across GitHub, Linear, desktop alerts, hooks, and connected c

## Invoke / install

- Invoke: `/affaan-m/ECC:google-workspace-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/google-workspace-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 4684b25a4820470a217048df8fc01bc4da6b37745f92ada83e9730d9be8da4e8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
