# effort

> Estimates the implementation effort required to address the given issue.

| | |
|---|---|
| **ID** | `google-gemini/gemini-cli:effort` |
| **Pack** | general |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |
| **License** | Apache-2.0 |
| **Size** | 35 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Analyze the issue content (title, body) AND the **code exploration output** (the discovered source files, coupled UI components, and test files) to estimate the effort required to implement a fix.

## How it is structured

The skill's own section headings, in order:

  - JSON Output Format:
  - Effort Levels:

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:hf-mem](huggingface-skills-hf-mem.md) - Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from 

## Invoke / install

- Invoke: `/google-gemini/gemini-cli:effort`
- Install: `python skills/skill-vetter/scripts/install.py google-gemini/gemini-cli --path tools/caretaker-agent/cloudrun/triage-worker/.gemini/skills/effort --commit 62bab5b232c15b925d31e655ce844ab939c882b7 --expect-tree bc220c379f1594bf99e9985d75f74835340e71fccb248e0b7b1be976299bd8ce --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
