# slack-gif-creator

> Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack."

| | |
|---|---|
| **ID** | `example-skills:slack-gif-creator` |
| **Pack** | Creative & Media (also: Communication & Collaboration, Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `example-skills` v3b3fad96af16 - [anthropics/skills](https://github.com/anthropics/skills) |
| **License** | Complete terms in LICENSE.txt |
| **Size** | 255 lines in SKILL.md, 7 file(s) |

## When to use it

- Use when users request animated GIFs for Slack like "make me a GIF of X doing Y for Slack.".

## What it says up front

> A toolkit providing utilities and knowledge for creating animated GIFs optimized for Slack.

## How it is structured

The skill's own section headings, in order:

- Slack Requirements
- Core Workflow
- Drawing Graphics
  - Working with User-Uploaded Images
  - Drawing from Scratch
  - Making Graphics Look Good
- Available Utilities
  - GIFBuilder (`core.gif_builder`)
  - Validators (`core.validators`)
  - Easing Functions (`core.easing`)
  - Frame Helpers (`core.frame_composer`)
- Animation Concepts
  - Shake/Vibrate
  - Pulse/Heartbeat
  - Bounce
  - Spin/Rotate
  - Fade In/Out
  - Slide
  - Zoom
  - Explode/Particle Burst
- Optimization Strategies
- Philosophy
- Dependencies

## What it bundles

- scripts: `core/easing.py`, `core/frame_composer.py`, `core/gif_builder.py`, `core/validators.py`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Invoke / install

- Invoke: `/example-skills:slack-gif-creator`  (Skill tool: `example-skills:slack-gif-creator`)
- Install: `claude plugin marketplace add anthropics/skills && claude plugin install example-skills@anthropic-agent-skills`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
