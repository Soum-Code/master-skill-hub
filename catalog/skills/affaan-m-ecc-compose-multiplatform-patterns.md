# compose-multiplatform-patterns

> Compose Multiplatform and Jetpack Compose patterns for KMP projects — state management, navigation, theming, performance, and platform-specific UI. Use when building Compose or Jetpack Compose UI, state, navigation, or theming in a KMP project.

| | |
|---|---|
| **ID** | `affaan-m/ECC:compose-multiplatform-patterns` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 301 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building Compose or Jetpack Compose UI, state, navigation, or theming in a KMP project.

## What it says up front

> Patterns for building shared UI across Android, iOS, Desktop, and Web using Compose Multiplatform and Jetpack Compose. Covers state management, navigation, theming, and performance.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- State Management
  - ViewModel + Single State Object
  - Collecting State in Compose
  - Event Sink Pattern
- Navigation
  - Type-Safe Navigation (Compose Navigation 2.8+)
  - Dialog and Bottom Sheet Navigation
- Composable Design
  - Slot-Based APIs
  - Modifier Ordering
- KMP Platform-Specific UI
  - expect/actual for Platform Composables
- Performance
  - Stable Types for Skippable Recomposition
  - Use `key()` and Lazy Lists Correctly
  - Defer Reads with `derivedStateOf`
  - Avoid Allocations in Recomposition
- Theming
  - Material 3 Dynamic Theming
- Anti-Patterns to Avoid
- References

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:swiftui-patterns](affaan-m-ecc-swiftui-patterns.md) - SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance op
- [affaan-m/ECC:frontend-patterns](affaan-m-ecc-frontend-patterns.md) - Frontend development patterns for React, Next.js, state management, performance optimization, and UI best prac
- [affaan-m/ECC:vue-patterns](affaan-m-ecc-vue-patterns.md) - Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management, 
- [affaan-m/ECC:android-clean-architecture](affaan-m-ecc-android-clean-architecture.md) - Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure, dependency rules

## Invoke / install

- Invoke: `/affaan-m/ECC:compose-multiplatform-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/compose-multiplatform-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 3cf8e2a6842e8aa528995a94b2ca36114fc5573b0883bcfc2237734dcaea09a8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
