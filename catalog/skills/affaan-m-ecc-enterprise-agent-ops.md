# enterprise-agent-ops

> Operational controls for long-lived or cloud-hosted agent systems — runtime lifecycle (start, pause, stop, restart), observability (logs, metrics, traces), least-privilege safety scopes and kill switches, and rollout/rollback change management with audit logs and success/cost metrics. Use when running production agent fleets on PM2, systemd, or containers that need monitoring, incident response, or deployment gates.

| | |
|---|---|
| **ID** | `affaan-m/ECC:enterprise-agent-ops` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 52 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when running production agent fleets on PM2, systemd, or containers that need monitoring, incident response, or deployment gates.

## What it says up front

> Use this skill for cloud-hosted or continuously running agent systems that need operational controls beyond single CLI sessions.

## How it is structured

The skill's own section headings, in order:

- Operational Domains
- Baseline Controls
- Metrics to Track
- Incident Pattern
- Deployment Integrations

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:enterprise-agent-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/enterprise-agent-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 255d2bda920804dff052d833386679eb93e31672b5fdda0bc7b992269381a139 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
