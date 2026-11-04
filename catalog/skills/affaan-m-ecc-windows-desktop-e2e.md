# windows-desktop-e2e

> E2E testing for Windows native desktop apps (WPF, WinForms, Win32/MFC, Qt) using pywinauto and Windows UI Automation. Use when writing E2E tests for a Windows native desktop app with pywinauto or UI Automation.

| | |
|---|---|
| **ID** | `affaan-m/ECC:windows-desktop-e2e` |
| **Pack** | Browser & Web Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 889 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing E2E tests for a Windows native desktop app with pywinauto or UI Automation.

## What it says up front

> End-to-end testing for Windows native desktop applications using **pywinauto** backed by Windows UI Automation (UIA). Covers WPF, WinForms, Win32/MFC, and Qt (5.x / 6.x) — with Qt-specific guidance as a dedicated section.

## How it is structured

The skill's own section headings, in order:

- When to Activate
  - When NOT to Use
- Core Concepts
- Setup & Prerequisites
- Testability Setup (by Framework)
  - WPF
  - WinForms
  - Win32 / MFC
  - Qt — see dedicated section below
- Page Object Model
  - base_page.py
  - login_page.py
  - conftest.py
  - config.py
  - pytest.ini
- Locator Strategy
- Wait Patterns
- Artifact Management
- Per-Step Trace (opt-in)
  - Enable
  - Patch into BasePage
  - Caveats
- Flaky Test Handling
- Test Isolation & Sandbox
  - Tier 1 — Filesystem Isolation (default, always use)
  - Tier 2 — Windows Job Object (optional: process-lifetime containment)
  - Tier 3 — Windows Sandbox (CI full-OS isolation)
  - Tier comparison
  - Prevent hanging tests
- CI/CD Integration

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/agent-browser:electron](vercel-labs-agent-browser-electron.md) - Automate Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify, etc.) using agent-browser via
- [affaan-m/ECC:e2e-testing](affaan-m-ecc-e2e-testing.md) - Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and

## Invoke / install

- Invoke: `/affaan-m/ECC:windows-desktop-e2e`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/windows-desktop-e2e --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 53ec73f966eb8931571de82f1aed70895c29e1e684a1ba9710ab7a6b4c613a4a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
