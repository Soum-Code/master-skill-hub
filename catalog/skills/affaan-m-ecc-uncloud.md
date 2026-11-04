# uncloud

> Use when managing an Uncloud cluster — deploying services, configuring Caddy ingress, adding static proxy routes for non-cluster devices, publishing ports, scaling, inspecting logs, or managing machines and volumes with the `uc` CLI.

| | |
|---|---|
| **ID** | `affaan-m/ECC:uncloud` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 345 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when managing an Uncloud cluster — deploying services, configuring Caddy ingress, adding static proxy routes for non-cluster devices, publishing ports, scaling, inspecting logs, or managing machines and volumes with the `uc` CLI.

## What it says up front

> Reference for the `uc` CLI — a decentralised self-hosting platform using Docker containers, WireGuard mesh networking, and Caddy reverse proxy.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- How It Works
- Examples
- Core Concepts
- CLI Quick Reference
  - Machines
  - Services
  - Images
  - Volumes
  - Caddy
  - DNS & Context
- Port Publishing
  - HTTP/HTTPS (via Caddy reverse proxy)
  - TCP/UDP (host-bound, bypasses Caddy)
- Compose File Extensions
  - `x-ports` — publish ports with domains
  - `x-caddy` — custom Caddy config for service
  - `x-machines` — placement constraints
  - Full multi-service example
- Routing to External (Non-Cluster) Devices
- Service DNS (Internal)
- Scaling & Global Services
- Image Tag Templates (in compose.yaml)
- Common Workflows
- Common Mistakes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:uncloud`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/uncloud --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 98ab37d674c21a8a0ec091db795d9c2c3cd85f66a988ce88b25c2f27572ab15c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
