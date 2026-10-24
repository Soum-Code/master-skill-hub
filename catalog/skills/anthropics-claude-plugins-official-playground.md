# playground

> Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt. Use when the user asks to make a playground, explorer, or interactive tool for a topic.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:playground` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 77 lines in SKILL.md, 7 file(s) |

## When to use it

- Use when the user asks to make a playground, explorer, or interactive tool for a topic.

## What it says up front

> A playground is a self-contained HTML file with interactive controls on one side, a live preview on the other, and a prompt output at the bottom with a copy button. The user adjusts controls, explores visually, then copies the generated prompt back into Claude.

## How it is structured

The skill's own section headings, in order:

- When to use this skill
- How to use this skill
- Core requirements (every playground)
- State management pattern
- Prompt output pattern
- Common mistakes to avoid

## What it bundles

- 6 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [loop](loop.md) - Run a prompt or slash command on a recurring interval, or let the model self-pace. Use when the user wants to 
- [example-skills:canvas-design](example-skills-canvas-design.md) - Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when
- [anthropics/claude-code:Writing Hookify Rules](anthropics-claude-code-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-plugins-official:writing-hookify-rules](anthropics-claude-plugins-official-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:playground`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/playground/skills/playground --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree 49962d281bbaf2a2cb3cfcd3355e3fe7f3cd2dbaeb89c9c17257d45a4eb39956 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
