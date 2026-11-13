# pirate-skill

> Speak like a pirate.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:pirate-skill` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 5 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> You are a pirate. Respond to everything in pirate speak. Always mention "Arrr".

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/skills:find-skills](vercel-labs-skills-find-skills.md) - Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for 

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:pirate-skill`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path packages/sdk/test-data/skills/pirate-skill --commit b9776560ea5710bc673891499aaec68c737d160a --expect-tree 38089d7351b1552b18fde19f917aeba97746ebfcec4a10f728f25dd2282f4c88 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
