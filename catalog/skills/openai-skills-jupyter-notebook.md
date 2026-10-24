# jupyter-notebook

> Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

| | |
|---|---|
| **ID** | `openai/skills:jupyter-notebook` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 108 lines in SKILL.md, 12 file(s) |

## When to use it

- Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook.

## How it is structured

The skill's own section headings, in order:

- When to use
- Decision tree
- Skill path (set once)
- Workflow
- Templates and helper script
- Temp and output conventions
- Dependencies (install only when needed)
- Environment
- Reference map

## What it bundles

- scripts: `scripts/new_notebook.py`
- reference docs: `references/experiment-patterns.md`, `references/notebook-structure.md`, `references/quality-checklist.md`, `references/tutorial-patterns.md`
- 6 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:speech](openai-skills-speech.md) - Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch
- [bm:profile-user](bm-profile-user.md) - Generate developer behavioral profile and create Claude-discoverable artifacts
- [anthropics/claude-plugins-official:example-skill](anthropics-claude-plugins-official-example-skill.md) - This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill tem
- [cowork-plugin-management:create-cowork-plugin](cowork-plugin-management-create-cowork-plugin.md) - Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a pl

## Invoke / install

- Invoke: `/openai/skills:jupyter-notebook`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/jupyter-notebook --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree a0dd56574416d864db3dc8c6384a2c246a45d5549a123130ded9f1999036ef8b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
