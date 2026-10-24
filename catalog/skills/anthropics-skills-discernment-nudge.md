# discernment-nudge

> After you give a substantive answer or draft that the user may act on — advice or recommendations, drafted artifacts such as goals, plans, pitches, proposals, or emails, estimates or projections, analysis or interpretation of data, factual claims they may rely on, or a multi-step argument — invoke this skill BEFORE finalizing your reply and then, if it applies, append 2-3 short follow-up questions, each tied to something specific in what you just produced, that help the user check key facts, probe the reasoning or assumptions, and notice missing context. Do this at most once per conversation. Skip it when the user asked a trivial how-to or simple lookup, wants a purely educational explanation, asked you only to format, convert, or assemble a file from content they provided, is writing code they will run, is doing creative writing or casual chat, or already asked you to double-check, cite, or review — the skill file explains these boundaries and the exact output format.

| | |
|---|---|
| **ID** | `anthropics/skills:discernment-nudge` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/skills](https://github.com/anthropics/skills) |
| **License** | Complete terms in LICENSE.txt |
| **Size** | 210 lines in SKILL.md, 2 file(s) |

## When to use it

- Skip it when the user asked a trivial how-to or simple lookup, wants a purely educational explanation, asked you only to format, convert, or assemble a file from content they provided, is writing code they will run, is doing creative writing or casual chat, or.

## What it says up front

> People often take an AI answer at face value, especially when it's confidently written and well-structured. That's usually fine — but for substantive answers the user is going to act on (spend money, make a health decision, cite a claim, commit to a plan), a small moment of reflection can catch a ba

## How it is structured

The skill's own section headings, in order:

- Why this exists
- When to offer the nudge
- When not to
- Writing the prompts
- Output format

## What it bundles

- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:docs](anthropic-skills-docs.md) - docs (editable docs people share and comment on; the default for any document, named as a doc or not: a docume
- [anthropic-skills:google-workspace](anthropic-skills-google-workspace.md) - Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch

## Invoke / install

- Invoke: `/anthropics/skills:discernment-nudge`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/skills --path skills/discernment-nudge --commit dbd4588f9e1033efb41dad4bef2f7947c8993d44 --expect-tree d6dde11d9c0c72262039295bfa8d576e71c3470bc77bd65a431511bad8d2f57a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
