# trl-training

> Post-train LLMs with TRL (Transformers Reinforcement Learning) — SFT, DPO, GRPO, KTO, and reward-model training. Use when writing or debugging training code with the TRL Python API or the trl CLI.

| | |
|---|---|
| **ID** | `huggingface/skills:trl-training` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 78 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing or debugging training code with the TRL Python API or the trl CLI.

## What it says up front

> Each method pairs a `*Trainer` class with a `*Config` dataclass. Configs extend `transformers.TrainingArguments`, so all of its arguments work in any trainer config.

## How it is structured

The skill's own section headings, in order:

- Dataset formats
- SFT: the fields that matter
- GRPO: online RL
- CLI

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [example-skills:mcp-builder](example-skills-mcp-builder.md) - Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with externa
- [huggingface/skills:huggingface-trackio](huggingface-skills-huggingface-trackio.md) - Track and visualize ML training experiments with Trackio. Use when logging metrics during training (Python API

## Invoke / install

- Invoke: `/huggingface/skills:trl-training`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/trl-training --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree d13739d6f4873dc983026022a7c3a4119ba54c0c4f2adc6f020c80e29fdd6830 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
