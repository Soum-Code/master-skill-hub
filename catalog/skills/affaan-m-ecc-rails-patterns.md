# rails-patterns

> Ruby on Rails framework patterns for Rails 7.1+ and 8.x apps. Covers the directory contract, skinny controllers with service objects, form objects, query objects, idiomatic ActiveRecord, background jobs, ViewComponent, Hotwire, and the Rails 8 Solid stack. Use when building or reviewing Rails apps, controllers, models, services, jobs, or views.

| | |
|---|---|
| **ID** | `affaan-m/ECC:rails-patterns` |
| **Pack** | Careers, Jobs & Hiring |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 476 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building or reviewing Rails apps, controllers, models, services, jobs, or views.

## What it says up front

> Framework patterns for modern Ruby on Rails applications (Rails 7.1+ and 8.x). Rails is opinionated by design; these are the patterns the community has converged on for apps that stay maintainable past the 50-model mark. This skill is the "how." For the "what" and "when" (the decisions about which p

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concepts
  - The directory contract
  - Skinny controllers
  - Service objects
  - Form objects
  - Query objects
  - Background jobs
  - ViewComponent over partials
  - Hotwire: Turbo and Stimulus
  - The Rails 8 Solid stack
- Code Examples
  - Skinny controller with a service object
  - The service object
  - Form object
  - Query object
  - N+1 prevention
  - Counter cache
  - Background job shape
  - ViewComponent
  - Hotwire
  - Acceptable vs unacceptable callbacks
  - Good concern vs bad concern
- Anti-Patterns
  - God controllers
  - Fat models with 30+ methods
  - Callback chains
  - Nested attributes for complex forms
  - Default scopes on critical models
  - Models named after database concepts

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:laravel-patterns](affaan-m-ecc-laravel-patterns.md) - Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and
- [affaan-m/ECC:fastapi-patterns](affaan-m-ecc-fastapi-patterns.md) - FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, 
- [affaan-m/ECC:django-patterns](affaan-m-ecc-django-patterns.md) - Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and 
- [affaan-m/ECC:golang-patterns](affaan-m-ecc-golang-patterns.md) - Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go app

## Invoke / install

- Invoke: `/affaan-m/ECC:rails-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/rails-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 08e78781982da4a0d744c3e633ee7f2ad4e5197fce622c528f2f4d02df70d635 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
