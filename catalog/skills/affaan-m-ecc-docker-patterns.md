# docker-patterns

> Docker and Docker Compose patterns for local development, hardened CLI installer harnesses, container security, networking, volumes, and multi-service orchestration. Use when creating or reviewing Dockerfiles and Compose services, testing installers across Linux distributions, or planning accurate native macOS and Windows validation.

| | |
|---|---|
| **ID** | `affaan-m/ECC:docker-patterns` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 560 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when creating or reviewing Dockerfiles and Compose services, testing installers across Linux distributions, or planning accurate native macOS and Windows validation.

## What it says up front

> Docker and Docker Compose best practices for containerized development.

## How it is structured

The skill's own section headings, in order:

- Docker Compose for Local Development
  - Standard Web App Stack
  - Development vs Production Dockerfile
  - Override Files
- Networking
  - Service Discovery
  - Custom Networks
  - Exposing Only What's Needed
- Volume Strategies
  - Common Patterns
- Container Security
  - Dockerfile Hardening
  - Compose Security
  - Secret Management
- Hardened CLI Installer Harnesses
  - Respect the Platform Boundary
  - Enforce the Isolation Contract
  - Exercise the ECC Plugin Setup Harness
  - Start, Open, Reconnect, and Clean Up a Named Session
  - Authenticate Codex Inside the Networked Session
- .dockerignore
- Debugging
  - Common Commands
  - Debugging Network Issues
- Anti-Patterns

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:dmux-workflows](affaan-m-ecc-dmux-workflows.md) - Multi-agent orchestration using dmux (tmux pane manager for AI agents). Patterns for parallel agent workflows 
- [affaan-m/ECC:agent-security-hardening](affaan-m-ecc-agent-security-hardening.md) - Security hardening guidance for AI agent frameworks that process untrusted content, invoke tools, write worksp
- [affaan-m/ECC:quarkus-verification](affaan-m-ecc-quarkus-verification.md) - Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests with JaCoCo 

## Invoke / install

- Invoke: `/affaan-m/ECC:docker-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/docker-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 645f5f944e735e688e71965c5b3b9876d215eca0c41c6171d267cfcee90c6f14 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
