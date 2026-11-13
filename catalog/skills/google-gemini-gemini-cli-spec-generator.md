# spec_generator

> Generates a structured Workable Spec JSON to guide a Developer Worker.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:spec_generator` |
| **Pack** | Product Management |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 99 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Extract key technical details from the issue and organize them according to the following strict JSON schema.

## How it is structured

The skill's own section headings, in order:

  - Critical Rules:

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:master-agreement-generator](affaan-m-ecc-master-agreement-generator.md) - Generate review drafts of counterparty master agreements from one template plus a JSON spec, with role-selecte
- [bm:ui-phase](bm-ui-phase.md) - Generate UI design contract (UI-SPEC.md) for frontend phases
- [bm:profile-user](bm-profile-user.md) - Generate developer behavioral profile and create Claude-discoverable artifacts
- [anthropics/knowledge-work-plugins:design-handoff](anthropics-knowledge-work-plugins-design-handoff.md) - Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sh

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:spec_generator`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path tools/caretaker-agent/cloudrun/triage-worker/.gemini/skills/spec_generator --commit b9776560ea5710bc673891499aaec68c737d160a --expect-tree e1d530982852ec27d42bc79577258bf012640050ae93bea8ba33635f16de03ed --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
