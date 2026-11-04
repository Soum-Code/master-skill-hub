# android-clean-architecture

> Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure, dependency rules, UseCases, Repositories, and data layer patterns. Use when structuring modules, layers, or data flow in an Android or KMP project.

| | |
|---|---|
| **ID** | `affaan-m/ECC:android-clean-architecture` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 341 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when structuring modules, layers, or data flow in an Android or KMP project.

## What it says up front

> Clean Architecture patterns for Android and KMP projects. Covers module boundaries, dependency inversion, UseCase/Repository patterns, and data layer design with Room, SQLDelight, and Ktor.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Module Structure
  - Recommended Layout
  - Dependency Rules
- Domain Layer
  - UseCase Pattern
  - Domain Models
  - Repository Interfaces
- Data Layer
  - Repository Implementation
  - Mapper Pattern
  - Room Database (Android)
  - SQLDelight (KMP)
  - Ktor Network Client (KMP)
- Dependency Injection
  - Koin (KMP-friendly)
  - Hilt (Android-only)
- Error Handling
  - Result/Try Pattern
- Convention Plugins (Gradle)
- Anti-Patterns to Avoid
- References

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:kotlin-coroutines-flows](affaan-m-ecc-kotlin-coroutines-flows.md) - Kotlin Coroutines and Flow patterns for Android and KMP — structured concurrency, Flow operators, StateFlow, e
- [affaan-m/ECC:compose-multiplatform-patterns](affaan-m-ecc-compose-multiplatform-patterns.md) - Compose Multiplatform and Jetpack Compose patterns for KMP projects — state management, navigation, theming, p
- [affaan-m/ECC:springboot-patterns](affaan-m-ecc-springboot-patterns.md) - Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, 
- [affaan-m/ECC:fastapi-patterns](affaan-m-ecc-fastapi-patterns.md) - FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, 

## Invoke / install

- Invoke: `/affaan-m/ECC:android-clean-architecture`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/android-clean-architecture --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree a5eb8cb4e4d53bf0c87c17cf72821f4fe6559def3a5301ba6367ff3e8e3593a4 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
