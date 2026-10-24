# speech

> Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for live calls. Custom voice creation is out of scope.

| | |
|---|---|
| **ID** | `openai/skills:speech` |
| **Pack** | AI / ML Engineering (also: Creative & Media, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 145 lines in SKILL.md, 16 file(s) |

## When to use it

- Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run the bundled CLI (`scripts/text_to_speech.py`) with built-in voices and require `OPENAI_API_KEY` for l.

## How it is structured

The skill's own section headings, in order:

- When to use
- Decision tree (single vs batch)
- Workflow
- Temp and output conventions
- Dependencies (install if missing)
- Environment
- Defaults & rules
- Instruction augmentation
- Examples
  - Single example (narration)
  - Batch example (IVR prompts)
- Instructioning best practices (short list)
- Guidance by use case
- CLI + environment notes
- Reference map

## What it bundles

- scripts: `scripts/text_to_speech.py`
- reference docs: `references/accessibility.md`, `references/audio-api.md`, `references/cli.md`, `references/codex-network.md`, `references/ivr.md`, `references/narration.md`, `references/prompting.md`, `references/sample-prompts.md` ...
- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [microsoft/skills:podcast-generation](microsoft-skills-podcast-generation.md) - Generate AI-powered podcast-style audio narratives using Azure OpenAI's GPT Realtime Mini model via WebSocket.
- [openai/skills:jupyter-notebook](openai-skills-jupyter-notebook.md) - Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations
- [openai/skills:transcribe](openai-skills-transcribe.md) - Transcribe audio files to text with optional diarization and known-speaker hints. Use when a user asks to tran
- [openai/skills:playwright](openai-skills-playwright.md) - Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, s

## Invoke / install

- Invoke: `/openai/skills:speech`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/speech --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree f0fad0334ad2bd59c175034d99dbc655f97ccabc3a3f9e7d26e088e5cc27a531 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
