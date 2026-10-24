# Spec-driven Dev Workflow

Phase/milestone based project execution - plan, discuss, execute, verify, ship (GSD / Buildomator style).

59 skill(s). Back to the [catalog](../README.md).

| Skill | What it does | Status |
|---|---|---|
| [`anthropics/claude-plugins-official:math-olympiad`](../skills/anthropics-claude-plugins-official-math-olympiad.md) | Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses. Activates when asked to 'solve  | verified |
| [`anthropics/claude-plugins-official:project-artifact`](../skills/anthropics-claude-plugins-official-project-artifact.md) | Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the workstream sequ | verified |
| [`bm:add-backlog`](../skills/bm-add-backlog.md) | Add an idea to the backlog parking lot (999.x numbering) | installed |
| [`bm:add-phase`](../skills/bm-add-phase.md) | Add phase to end of current milestone in roadmap | installed |
| [`bm:analyze-dependencies`](../skills/bm-analyze-dependencies.md) | Analyze phase dependencies and suggest Depends on entries for ROADMAP.md | installed |
| [`bm:audit-milestone`](../skills/bm-audit-milestone.md) | Audit milestone completion against original intent before archiving | installed |
| [`bm:audit-uat`](../skills/bm-audit-uat.md) | Cross-phase audit of all outstanding UAT and verification items | installed |
| [`bm:autonomous`](../skills/bm-autonomous.md) | Run all remaining phases autonomously — discuss→plan→execute per phase | installed |
| [`bm:check-todos`](../skills/bm-check-todos.md) | List pending todos and select one to work on | installed |
| [`bm:cleanup`](../skills/bm-cleanup.md) | Archive accumulated phase directories from completed milestones | installed |
| [`bm:complete-milestone`](../skills/bm-complete-milestone.md) | Archive completed milestone and prepare for next version | installed |
| [`bm:discuss-phase`](../skills/bm-discuss-phase.md) | Gather phase context through adaptive questioning before planning. Use --all to skip area selection and discuss all gray areas interactively. Use --auto to skip interacti | installed |
| [`bm:do`](../skills/bm-do.md) | Route freeform text to the right GSD command automatically | installed |
| [`bm:execute-phase`](../skills/bm-execute-phase.md) | Execute all plans in a phase with wave-based parallelization | installed |
| [`bm:extract_learnings`](../skills/bm-extract-learnings.md) | Extract decisions, lessons, patterns, and surprises from completed phase artifacts | installed |
| [`bm:fast`](../skills/bm-fast.md) | Execute a trivial task inline — no subagents, no planning overhead | installed |
| [`bm:forensics`](../skills/bm-forensics.md) | Post-mortem investigation for failed GSD workflows — analyzes git history, artifacts, and state to diagnose what went wrong | installed |
| [`bm:from-gsd2`](../skills/bm-from-gsd2.md) | Import a GSD-2 (.gsd/) project back to GSD v1 (.planning/) format | installed |
| [`bm:graphify`](../skills/bm-graphify.md) | Build, query, and inspect the project knowledge graph in .planning/graphs/ | installed |
| [`bm:help`](../skills/bm-help.md) | Show available GSD commands and usage guide | installed |
| [`bm:import`](../skills/bm-import.md) | Ingest external plans with conflict detection against project decisions before writing anything. | installed |
| [`bm:insert-phase`](../skills/bm-insert-phase.md) | Insert urgent work as decimal phase (e.g., 72.1) between existing phases | installed |
| [`bm:intel`](../skills/bm-intel.md) | Query, inspect, or refresh codebase intelligence files in .planning/intel/ | installed |
| [`bm:list-phase-assumptions`](../skills/bm-list-phase-assumptions.md) | Surface Claude's assumptions about a phase approach before planning | installed |
| [`bm:list-workspaces`](../skills/bm-list-workspaces.md) | List active GSD workspaces and their status | installed |
| [`bm:manager`](../skills/bm-manager.md) | Interactive command center for managing multiple phases from one terminal | installed |
| [`bm:milestone-summary`](../skills/bm-milestone-summary.md) | Generate a comprehensive project summary from milestone artifacts for team onboarding and review | installed |
| [`bm:mvp-phase`](../skills/bm-mvp-phase.md) | Plan an MVP-mode phase — captures an "As a / I want to / So that" user story, runs SPIDR splitting, then delegates to plan-phase | installed |
| [`bm:new-milestone`](../skills/bm-new-milestone.md) | Start a new milestone cycle — update PROJECT.md and route to requirements | installed |
| [`bm:new-project`](../skills/bm-new-project.md) | Initialize a new project with deep context gathering and PROJECT.md | installed |
| [`bm:new-workspace`](../skills/bm-new-workspace.md) | Create an isolated workspace with repo copies and independent .planning/ | installed |
| [`bm:next`](../skills/bm-next.md) | Automatically advance to the next logical step in the GSD workflow | installed |
| [`bm:pause-work`](../skills/bm-pause-work.md) | Create context handoff when pausing work mid-phase | installed |
| [`bm:plan-milestone-gaps`](../skills/bm-plan-milestone-gaps.md) | Create phases to close all gaps identified by milestone audit | installed |
| [`bm:plan-phase`](../skills/bm-plan-phase.md) | Create detailed phase plan (PLAN.md) with verification loop | installed |
| [`bm:plant-seed`](../skills/bm-plant-seed.md) | Capture a forward-looking idea with trigger conditions — surfaces automatically at the right milestone | installed |
| [`bm:progress`](../skills/bm-progress.md) | Check project progress, show context, and route to next action (execute or plan). Use --forensic to append a 6-check integrity audit after the standard report. | installed |
| [`bm:quick`](../skills/bm-quick.md) | Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents | installed |
| [`bm:remove-phase`](../skills/bm-remove-phase.md) | Remove a future phase from roadmap and renumber subsequent phases | installed |
| [`bm:remove-workspace`](../skills/bm-remove-workspace.md) | Remove a GSD workspace and clean up worktrees | installed |
| [`bm:research-phase`](../skills/bm-research-phase.md) | Research how to implement a phase (standalone - usually use /bm:plan-phase instead) | installed |
| [`bm:resume-at`](../skills/bm-resume-at.md) | Schedule a future resume of work - e.g. '/bm:resume-at 09:00', '/bm:resume-at +2h', or '/bm:resume-at 04:00 --cmd /bm:execute-phase 9' | installed |
| [`bm:resume-work`](../skills/bm-resume-work.md) | Resume work from previous session with full context restoration | installed |
| [`bm:review`](../skills/bm-review.md) | Request cross-AI peer review of phase plans from external AI CLIs | installed |
| [`bm:review-backlog`](../skills/bm-review-backlog.md) | Review and promote backlog items to active milestone | installed |
| [`bm:set-profile`](../skills/bm-set-profile.md) | Switch model profile for GSD agents (quality/balanced/budget/inherit) | installed |
| [`bm:sketch-wrap-up`](../skills/bm-sketch-wrap-up.md) | Package sketch design findings into a persistent project skill for future build conversations | installed |
| [`bm:spec-phase`](../skills/bm-spec-phase.md) | Socratic spec refinement — clarify WHAT a phase delivers with ambiguity scoring before discuss-phase. Produces a SPEC.md with falsifiable requirements locked before imple | installed |
| [`bm:spike-wrap-up`](../skills/bm-spike-wrap-up.md) | Package spike findings into a persistent project skill for future build conversations | installed |
| [`bm:stats`](../skills/bm-stats.md) | Display project statistics — phases, plans, requirements, git metrics, and timeline | installed |
| [`bm:thread`](../skills/bm-thread.md) | Manage persistent context threads for cross-session work | installed |
| [`bm:ultraplan-phase`](../skills/bm-ultraplan-phase.md) | [BETA] Offload plan phase to Claude Code's ultraplan cloud — drafts remotely while terminal stays free, review in browser with inline comments, import back via /bm:import | installed |
| [`bm:undo`](../skills/bm-undo.md) | Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks. | installed |
| [`bm:validate-phase`](../skills/bm-validate-phase.md) | Retroactively audit and fill Nyquist validation gaps for a completed phase | installed |
| [`bm:verify-work`](../skills/bm-verify-work.md) | Validate built features through conversational UAT | installed |
| [`bm:workstreams`](../skills/bm-workstreams.md) | Manage parallel workstreams — list, create, switch, status, progress, complete, and resume | installed |
| [`microsoft/skills:cost-estimation`](../skills/microsoft-skills-cost-estimation.md) | Forecast Azure spend and price planned resources or workloads. WHEN: "forecast Azure spending", "project next month cost", "compare forecast to my planning target", "how  | verified |
| [`openai/skills:define-goal`](../skills/openai-skills-define-goal.md) | Help the user define a concrete, measurable goal before starting work, especially when they ask to use the goal tool, create a goal, set an objective, clarify success cri | verified |
| [`product-management:sprint-planning`](../skills/product-management-sprint-planning.md) | Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan. Use when kicking off a new sprint, sizing a backlog against team availability (accounti | installed |
