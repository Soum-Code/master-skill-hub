# flutter-dart-code-review

> Library-agnostic Flutter/Dart code review checklist covering widget best practices, state management patterns (BLoC, Riverpod, Provider, GetX, MobX, Signals), Dart idioms, performance, accessibility, security, and clean architecture. Use when reviewing Flutter or Dart code, whatever state management library the project uses.

| | |
|---|---|
| **ID** | `affaan-m/ECC:flutter-dart-code-review` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 437 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when reviewing Flutter or Dart code, whatever state management library the project uses.

## What it says up front

> Comprehensive, library-agnostic checklist for reviewing Flutter/Dart applications. These principles apply regardless of which state management solution, routing library, or DI framework is used.

## How it is structured

The skill's own section headings, in order:

- 1. General Project Health
- 2. Dart Language Pitfalls
- 3. Widget Best Practices
  - Widget decomposition:
  - Const usage:
  - Key usage:
  - Theming & design system:
  - Build method complexity:
- 4. State Management (Library-Agnostic)
  - Architecture:
  - Immutability & value equality (for immutable-state solutions: BLoC, Riverpod, Redux):
  - Reactivity discipline (for reactive-mutation solutions: MobX, GetX, Signals):
  - State shape design:
  - Rebuild optimization:
  - Subscriptions & disposal:
  - Local vs global state:
- 5. Performance
  - Unnecessary rebuilds:
  - Expensive operations in build():
  - Image optimization:
  - Lazy loading:
  - Other:
- 6. Testing
  - Test types and expectations:
  - Coverage targets:
  - Test isolation:
  - Widget test quality:
- 7. Accessibility
  - Semantic widgets:
  - Screen reader support:

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:dart-flutter-patterns](affaan-m-ecc-dart-flutter-patterns.md) - Production-ready Dart and Flutter patterns covering null safety, immutable state with Freezed, async compositi
- [affaan-m/ECC:vue-patterns](affaan-m-ecc-vue-patterns.md) - Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management, 
- [affaan-m/ECC:swiftui-patterns](affaan-m-ecc-swiftui-patterns.md) - SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance op
- [affaan-m/ECC:perl-patterns](affaan-m-ecc-perl-patterns.md) - Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.

## Invoke / install

- Invoke: `/affaan-m/ECC:flutter-dart-code-review`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/flutter-dart-code-review --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 1eb5665cb6bce10b2de901144483b0113cf7fb13c3b9830a89fd05ff372a3f91 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
