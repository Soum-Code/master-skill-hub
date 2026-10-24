# cardputer-buddy

> Iterate on the Cardputer-Adv MicroPython app bundle (Claude Buddy, Snake, Hello) after the device is already provisioned via m5-onboard. Use when the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command. Trigger on "add an app", "push to the cardputer", "tail the device", "run on the device", or follow-up work after /maker-setup.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:cardputer-buddy` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 47 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to add a new app, push a single changed .py without re-flashing, watch device serial logs, or run a one-shot REPL command.
- Trigger on "add an app", "push to the cardputer", "tail the device", "run on the device", or follow-up work after /maker-setup.

## What it says up front

> The `buddy/` directory in the local `build-with-claude` clone is the MicroPython payload that `m5-onboard` installs onto `/flash/`. Work inside that clone.

## How it is structured

The skill's own section headings, in order:

- Device layout
- Adding an app
- Dev loop tooling (`buddy/scripts/`)

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:m5-onboard](anthropics-claude-plugins-official-m5-onboard.md) - End-to-end onboarding for a freshly-plugged-in M5Stack ESP32 device (Cardputer, Cardputer-Adv, Core, CoreS3, S

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:cardputer-buddy`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/cwc-makers/skills/cardputer-buddy --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree ba428c13a526a56f8cbf59dfedbd93bb6fa88c9b216480d2ee29bb1295fcef33 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
