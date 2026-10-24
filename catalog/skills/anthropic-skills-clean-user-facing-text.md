# clean-user-facing-text

> Clean and finalize authorized natural-language text intended for readers by auditing suspicious invisible Unicode and rewriting prose while preserving facts, meaning, and the writer's voice. Use when the user asks to clean, humanize, polish, or finalize articles, manuscripts, reports, documentation, emails, product copy, UI text, Markdown, or HTML prose, or when a project rule or instruction file explicitly requires this workflow. Don't use for code-only tasks or undisclosed authorship evasion; leave code, commands, identifiers, paths, APIs, formulas, citations, required disclosures, and verbatim quotations unchanged.

| | |
|---|---|
| **ID** | `anthropic-skills:clean-user-facing-text` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | MIT |
| **Size** | 192 lines in SKILL.md, 11 file(s) |

## When to use it

- Use when the user asks to clean, humanize, polish, or finalize articles, manuscripts, reports, documentation, emails, product copy, UI text, Markdown, or HTML prose, or when a project rule or instruction file explicitly requires this workflow.
- Don't use for code-only tasks or undisclosed authorship evasion; leave code, commands, identifiers, paths, APIs, formulas, citations, required disclosures,.

## What it says up front

> Apply a final text-hygiene pass to prose the user owns or is authorized to process. Treat Unicode cleanup as deterministic and statistical-watermark reduction as best-effort; never claim that a rewrite proves human authorship or is undetectable. Preserve required academic, legal, platform, and regul

## How it is structured

The skill's own section headings, in order:

- Workflow
- Scoring
- Deterministic Unicode pass
- Detector levers
- Voice and domain presets
  - Plain-language sub-mode
- Code boundary
- Reporting

## What it bundles

- scripts: `scripts/clean_text.py`, `scripts/common.py`, `scripts/inspect_text.py`, `scripts/score_stylometry.py`, `scripts/text_unicode.py`
- reference docs: `references/detectors.md`, `references/responsible-use.md`, `references/watermark-notes.md`, `references/writing-in-your-voice.md`
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Invoke / install

- Invoke: `/anthropic-skills:clean-user-facing-text`  (Skill tool: `anthropic-skills:clean-user-facing-text`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
