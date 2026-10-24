# m5-onboard

> End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, Stick) — detect on USB, flash UIFlow 2.0 firmware, and install the Claude Buddy MicroPython app bundle. Use whenever the user plugs in or wants to flash/provision/reset an M5Stack or ESP32 board, or says "m5-onboard go".

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:m5-onboard` |
| **Pack** | Careers, Jobs & Hiring |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 186 lines in SKILL.md, 1 file(s) |

## When to use it

- Use whenever the user plugs in or wants to flash/provision/reset an M5Stack or ESP32 board, or says "m5-onboard go".

## What it says up front

> This skill automates the full cold-start workflow for an M5Stack ESP32 device: detect on USB, identify model, flash UIFlow 2.0, and push a MicroPython app bundle onto `/flash/` so the device boots into user software. The apps we ship (Claude Buddy, Snake, Hello) talk over BLE or USB. The workflow ru

## How it is structured

The skill's own section headings, in order:

- Where the scripts live
- When to use
  - Which variant to assume
- The workflow
  - Relaying physical steps to the user (REQUIRED)
  - Stages
- Critical gotchas (baked into the scripts — do not second-guess)
- After provisioning (what the user sees on the device)
- Files
- Dependencies
- Platform notes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:cardputer-buddy](anthropics-claude-plugins-official-cardputer-buddy.md) - Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already p

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:m5-onboard`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/cwc-makers/skills/m5-onboard --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree e20b0d5e68356823090acd77d57f4e373cc162d05ab78f95ba7a90f75493c7c1 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
