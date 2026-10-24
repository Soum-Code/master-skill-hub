# huggingface-trackio

> Track and visualize ML training experiments with Trackio. Use when logging metrics during training (Python API), firing alerts for training diagnostics, or retrieving/analyzing logged metrics (CLI). Supports real-time dashboard visualization, alerts with webhooks, HF Space syncing, and JSON output for automation.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-trackio` |
| **Pack** | AI / ML Engineering (also: Data & Analytics) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 118 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when logging metrics during training (Python API), firing alerts for training diagnostics, or retrieving/analyzing logged metrics (CLI).

## What it says up front

> Trackio is an experiment tracking library for logging and visualizing ML training metrics. It syncs to Hugging Face Spaces for real-time monitoring dashboards.

## How it is structured

The skill's own section headings, in order:

- Three Interfaces
- When to Use Each
  - Python API → Logging
  - Python API → Alerts
  - CLI → Retrieving
- Minimal Logging Setup
  - Minimal Retrieval
- Autonomous ML Experiment Workflow

## What it bundles

- reference docs: `references/alerts.md`, `references/logging_metrics.md`, `references/retrieving_metrics.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:trl-training](huggingface-skills-trl-training.md) - Post-train LLMs with TRL (Transformers Reinforcement Learning) — SFT, DPO, GRPO, KTO, and reward-model trainin

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-trackio`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-trackio --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 4dc98cc45fe3706ddd03d78db3e89088dc2f728a7e7d45bd0832bc06e0d2b682 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
