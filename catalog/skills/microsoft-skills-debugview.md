# debugview

> Sysinternals DebugView CLI (DbgViewCli) for capturing and analyzing usermode and kernel-mode Windows debug output from the command line. USE FOR: capturing OutputDebugString output, kernel DbgPrint/KdPrint capture, boot-time debug logging, remote debug monitoring, filtering debug output by PID or process name, crash dump analysis, automated debug capture with bounded execution. DO NOT USE FOR: non-Windows platforms, application-level logging frameworks (log4j, serilog), Azure Monitor or cloud telemetry, ETW tracing (use WPR/xperf instead), user-mode crash dumps (use WinDbg). Triggers: "debug output", "DbgView", "DebugView", "kernel debug", "capture debug logs", "boot logging", "OutputDebugString", "DbgPrint", "KdPrint", "remote debug monitor", "debug capture CLI".

| | |
|---|---|
| **ID** | `microsoft/skills:debugview` |
| **Pack** | MLOps / DevOps / Cloud (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 292 lines in SKILL.md, 7 file(s) |

## When to use it

- USE FOR: capturing OutputDebugString output, kernel DbgPrint/KdPrint capture, boot-time debug logging, remote debug monitoring, filtering debug output by PID or process name, crash dump analysis, automated debug capture with bounded execution.
- DO NOT USE FOR: non-Windows platforms, application-level logging frameworks (log4j, serilog), Azure Monitor or cloud telemetry, ETW tracing (use WPR/xperf i.

## What it says up front

> Command-line interface for capturing real-time debug output from Windows applications (OutputDebugString) and kernel-mode drivers (DbgPrint/KdPrint). Designed for scripted, automated, and AI-agent-driven debug capture workflows.

## How it is structured

The skill's own section headings, in order:

- Installation
- Requirements
- Core Workflow
- Command-Line Parameters
  - Capture Control
  - Filtering
  - Bounded Execution (AI-Agent Friendly)
  - Time Display
  - Output Format
  - Logging
  - Boot Logging (Requires Admin)
  - Remote Monitoring
  - Crash Dump & File Operations
  - Runtime Control (Inter-Process)
  - Miscellaneous
- Usage Examples
  - Basic Win32 Capture (bounded)
  - Kernel Debug Capture (requires admin)
  - Process-Specific Filtering
  - Pattern-Based Filtering
  - Tail Mode (recent context)
  - Status Check (machine-readable)
  - Boot Logging
  - Remote Monitoring
  - Runtime Control (Pause/Resume/Stop)
  - EULA Acceptance (Unattended)
- Architecture
- Key Design Decisions
- Best Practices
- Bundled Resources

## What it bundles

- scripts: `scripts/boot-logging-workflow.ps1`, `scripts/capture-wrapper.ps1`, `scripts/detect-dbgview.ps1`
- reference docs: `references/driver-ioctls.md`, `references/output-formats.md`, `references/remote-protocol.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Invoke / install

- Invoke: `/microsoft/skills:debugview`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/debugview --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 7e9d8e8f64d8ce9ddea4b3262f82eeab3fc72743cdbf05d454ab5428bcc1c269 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
