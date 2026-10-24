# transcribe

> Transcribe audio files to text with optional diarization and known-speaker hints. Use when a user asks to transcribe speech from audio/video, extract text from recordings, or label speakers in interviews or meetings.

| | |
|---|---|
| **ID** | `openai/skills:transcribe` |
| **Pack** | Creative & Media |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 82 lines in SKILL.md, 7 file(s) |

## When to use it

- Use when a user asks to transcribe speech from audio/video, extract text from recordings, or label speakers in interviews or meetings.

## How it is structured

The skill's own section headings, in order:

- Workflow
- Decision rules
- Output conventions
- Dependencies (install if missing)
- Environment
- Skill path (set once)
- CLI quick start
- Reference map

## What it bundles

- scripts: `scripts/transcribe_diarize.py`
- reference docs: `references/api.md`
- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:speech](openai-skills-speech.md) - Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch
- [anthropic-skills:pdf](anthropic-skills-pdf.md) - Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text

## Invoke / install

- Invoke: `/openai/skills:transcribe`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/transcribe --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 017174ad9b913b448d1c13918406c11aa71e238da70cad698b3ab240183eb454 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
