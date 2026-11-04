# kubernetes-patterns

> Kubernetes workload patterns, resource management, RBAC, probes, autoscaling, ConfigMap/Secret handling, and kubectl debugging for production-grade deployments. Use when writing or reviewing Kubernetes manifests, or debugging probes, RBAC, autoscaling, or resource limits.

| | |
|---|---|
| **ID** | `affaan-m/ECC:kubernetes-patterns` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 757 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing or reviewing Kubernetes manifests, or debugging probes, RBAC, autoscaling, or resource limits.

## What it says up front

> Production-grade Kubernetes patterns for deploying, managing, and debugging workloads reliably.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- When to Use
- How It Works
- Examples
- Core Workload Patterns
  - Deployment — Production Template
- Probes — Liveness, Readiness, Startup
- Services and Ingress
  - Service Types
  - Ingress with TLS
- ConfigMaps and Secrets
  - ConfigMap — Non-sensitive configuration
  - Secrets — Sensitive data
- Resource Requests and Limits
- RBAC — Roles and ServiceAccounts
  - Principle of Least Privilege
- Horizontal Pod Autoscaler (HPA)
- PodDisruptionBudget (PDB)
- Namespaces and Multi-Tenancy
- Jobs and CronJobs
- kubectl Debugging Cheatsheet
  - Diagnosing Common Errors
- Anti-Patterns
- Best Practices Checklist
  - Security
  - Reliability
  - Observability
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:api-design](affaan-m-ecc-api-design.md) - REST API design patterns including resource naming, status codes, pagination, filtering, error responses, vers
- [affaan-m/ECC:redis-patterns](affaan-m-ecc-redis-patterns.md) - Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection m
- [affaan-m/ECC:dart-flutter-patterns](affaan-m-ecc-dart-flutter-patterns.md) - Production-ready Dart and Flutter patterns covering null safety, immutable state with Freezed, async compositi
- [affaan-m/ECC:kotlin-coroutines-flows](affaan-m-ecc-kotlin-coroutines-flows.md) - Kotlin Coroutines and Flow patterns for Android and KMP — structured concurrency, Flow operators, StateFlow, e

## Invoke / install

- Invoke: `/affaan-m/ECC:kubernetes-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/kubernetes-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree edb0b736d12dff70e638150973bc58c07b409050dd21e52a545aae16cb66b1ba --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
