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

- [google-gemini/gemini-cli:prs](google-gemini-gemini-cli-prs.md) - Expertise in managing the Git and GitHub Pull Request lifecycle, including staging changes, generating PR desc
- [google-gemini/gemini-cli:pr-creator](google-gemini-gemini-cli-pr-creator.md) - Use this skill when asked to create a pull request (PR). It ensures all PRs follow the repository's establishe
- [google-gemini/gemini-cli:pr-address-comments](google-gemini-gemini-cli-pr-address-comments.md) - Use this skill if the user asks you to help them address GitHub PR comments for their current branch of the Ge
- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin

## Invoke / install

- Invoke: `/vercel-labs/skills:pr-labeling`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/skills --path .automations/pr-labeling/skills/pr-labeling --commit d3701c11b1101251af14c9d148f026e1a47ebe17 --expect-tree 96b9852c856f0cbc50a62b06d278ff31e68debbbd33d030fc2e40fea85287db1 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
