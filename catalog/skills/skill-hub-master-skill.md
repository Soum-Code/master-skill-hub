# master-skill

> Router for every other skill. Use at the start of any non-trivial request, and whenever it is unclear which skill, plugin or workflow fits - "which skill should I use", "best skill for this", "find or recommend a skill", "what can you do for my job search / ML project / data / design / legal / finance work". Picks the best match from a catalog of 200+ skills grouped into industry packs (AI/ML, MLOps, software dev, careers and jobs, data, design, product, finance, legal, security, research), prefers skills already installed, suggests multi-skill chains, and files a skill request when nothing fits. Never installs an unvetted skill. Skip it for trivial one-step questions.

| | |
|---|---|
| **ID** | `skill-hub:master-skill` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | plugin `skill-hub` - [Soum-Code/master-skill-hub](https://github.com/Soum-Code/master-skill-hub) |
| **License** | MIT |
| **Size** | 50 lines in SKILL.md, 24 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> 2. **Route.** Describe the task in one sentence and run the router that sits next to this file:

## How it is structured

The skill's own section headings, in order:

- Run it
- Why a router and not one giant skill
- Safety rules (non-negotiable)
- Packs

## What it bundles

- scripts: `scripts/route.py`
- reference docs: `references/chains.md`, `references/index.md`, `references/packs/ai-ml.md`, `references/packs/browser-automation.md`, `references/packs/careers-jobs.md`, `references/packs/communication-collab.md`, `references/packs/creative-media.md`, `references/packs/data-analytics.md` ...
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [skill-hub:ml-interview-prep](skill-hub-ml-interview-prep.md) - Interview preparation for ML engineer, AI engineer, MLOps, data scientist and applied-LLM roles. Use for "prep

## Invoke / install

- Invoke: `/skill-hub:master-skill`
- Install: `claude plugin marketplace add Soum-Code/master-skill-hub && claude plugin install skill-hub@master-skill-hub`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
