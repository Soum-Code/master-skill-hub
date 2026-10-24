# pr-labeling

> Classify a skills CLI pull request from its description and patch, while respecting existing labels.

| | |
|---|---|
| **ID** | `vercel-labs/skills:pr-labeling` |
| **Pack** | MLOps / DevOps / Cloud (also: Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/skills](https://github.com/vercel-labs/skills) |
| **License** | MIT |
| **Size** | 23 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> current labels, and changed file patches. If the head commit no longer matches the triggered commit, stop so a newer run can classify it. 2. If the pull request already has `bug`, `documentation`, or `enhancement`, stop. Keep labels chosen by maintainers or earlier runs. 3. Choose one label from the

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [bm:review](bm-review.md) - Request cross-AI peer review of phase plans from external AI CLIs
- [anthropic-skills:skill-creator](anthropic-skills-skill-creator.md) - Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to c
- [example-skills:skill-creator](example-skills-skill-creator.md) - Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to c

## Invoke / install

- Invoke: `/vercel-labs/skills:pr-labeling`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/skills --path .vc/automations/workflows/pr-labeling/skills/pr-labeling --commit a80e4c9d12d607631249d4d7d059f835d4b2f13a --expect-tree 96b9852c856f0cbc50a62b06d278ff31e68debbbd33d030fc2e40fea85287db1 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
