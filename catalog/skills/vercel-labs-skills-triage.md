# triage

> Identify focused, evidence-backed skills CLI bug fixes worth quuu's attention.

| | |
|---|---|
| **ID** | `vercel-labs/skills:triage` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/skills](https://github.com/vercel-labs/skills) |
| **License** | MIT |
| **Size** | 121 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Use `read_pull_request` with the triggering PR number. Record its head SHA, state, labels, description, and every changed file patch. Stop if it is closed, the head differs from the triggered SHA, or `triage:bug-fix` is already present. The separate `pr-labeling` workflow's `bug` label is neither ev

## How it is structured

The skill's own section headings, in order:

- Read the actual change
- Require a valid bug fix
- Describe verification honestly
- Find unlinked matching issues
- Label and hand off once

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/vercel-labs/skills:triage`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/skills --path .vc/automations/workflows/triage/skills/triage --commit a80e4c9d12d607631249d4d7d059f835d4b2f13a --expect-tree 19c79235be1ef9967e7053721fdaee482e3785f81eb1d497e82a8e6c55bc9488 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
