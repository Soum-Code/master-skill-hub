# Skill catalog

211 skills across 19 packs. Every page is generated from the skill's own SKILL.md, so the descriptions are the authors' words, not a summary I made up.

## Packs (industries and roles)

| Pack | Skills | What it covers |
|---|---|---|
| [Spec-driven Dev Workflow](packs/dev-workflow.md) | 55 | Phase/milestone based project execution - plan, discuss, execute, verify, ship (GSD / Buildomator style). |
| [Software Development](packs/software-dev.md) | 24 | Writing, reviewing, debugging, testing and architecting code across languages. |
| [Claude / Skills / Plugin Tooling](packs/meta-tooling.md) | 19 | Building and tuning skills, plugins, MCP servers, hooks, settings, keybindings, mods. |
| [Web, Frontend & UI Design](packs/web-frontend-design.md) | 19 | UI/UX, design systems, typography, layout, accessibility, landing pages, visual polish. |
| [Productivity & Automation](packs/productivity-automation.md) | 13 | Tasks, memory, scheduling, recurring jobs, inbox, notes, daily briefs, personal workflows. |
| [Legal & Compliance](packs/legal-compliance.md) | 10 | Contract review, NDAs, compliance checks, risk assessment, e-signature, privacy/DPA. |
| [Communication & Collaboration](packs/communication-collab.md) | 9 | Slack, email, meetings, standups, internal comms, stakeholder updates, briefings. |
| [Documents, Writing & Content](packs/docs-content.md) | 8 | Word/PDF/slides, technical writing, editing, humanizing text, comms, blogs, social posts. |
| [Finance & Accounting](packs/finance-accounting.md) | 7 | Journal entries, reconciliations, close, financial statements, audit support, SOX, variance analysis. |
| [Browser & Web Automation](packs/browser-automation.md) | 6 | Driving browsers, scraping, form filling, E2E tests, screenshots, web research. |
| [Operations & Business](packs/operations-business.md) | 6 | Process design, capacity planning, vendor management, status reports, change management. |
| [Creative & Media](packs/creative-media.md) | 5 | Generative art, GIFs, imagery, themes, branding, video/audio helpers. |
| [MLOps / DevOps / Cloud](packs/mlops-devops.md) | 5 | CI/CD, deployment, containers, infra, monitoring, incidents, runbooks, release management. |
| [Product Management](packs/product-mgmt.md) | 5 | PRDs, roadmaps, specs, sprint planning, stakeholder updates, user research synthesis. |
| [Research & Learning](packs/research-learning.md) | 5 | Deep research, literature review, brainstorming, explaining, study and teaching aids. |
| [AI / ML Engineering](packs/ai-ml.md) | 4 | LLM apps, agents, RAG, prompt and eval work, model APIs, MCP, notebooks, ML research. |
| [Careers, Jobs & Hiring](packs/careers-jobs.md) | 4 | Resumes, CVs, cover letters, LinkedIn, interview prep, portfolios, job search, networking. |
| [Data & Analytics](packs/data-analytics.md) | 4 | SQL, spreadsheets, dashboards, charts, statistics, metrics, BI, data cleaning. |
| [Security & Privacy](packs/security.md) | 3 | Security review, vulnerability analysis, secrets hygiene, threat modelling, safe skill vetting. |

## Multi-skill chains

- **Land a job - research, tailor, polish**: `anthropic-skills:deep-research` -> `skill-hub:job-search-copilot` -> `anthropic-skills:docx` -> `anthropic-skills:humanizer` -> `linkedin-profile-optimizer`
- **Prepare for an ML / AI interview**: `anthropic-skills:deep-research` -> `skill-hub:ml-interview-prep` -> `skill-hub:job-search-copilot`
- **LinkedIn profile and posts**: `linkedin-profile-optimizer` -> `linkedin-humanizer`
- **Build and ship an LLM application**: `claude-api` -> `example-skills:mcp-builder` -> `engineering:testing-strategy` -> `engineering:deploy-checklist`
- **Plan and audit AI evaluation**: `bm:ai-integration-phase` -> `bm:eval-review`
- **Spec-driven delivery from idea to shipped PR**: `bm:new-project` -> `bm:plan-phase` -> `bm:execute-phase` -> `bm:verify-work` -> `bm:ship`
- **Debug, fix, then lock it in with tests**: `engineering:debug` -> `bm:add-tests` -> `code-review`
- **Pre-merge quality pass**: `simplify` -> `code-review` -> `security-review`
- **Design and build a polished web UI**: `impeccable:impeccable` -> `frontend-design:frontend-design` -> `example-skills:webapp-testing`
- **Researched report or briefing**: `anthropic-skills:deep-research` -> `anthropic-skills:docx` -> `anthropic-skills:humanizer`
- **Research-backed slide deck**: `anthropic-skills:deep-research` -> `anthropic-skills:pptx`
- **Spreadsheet to insight**: `anthropic-skills:xlsx` -> `dataviz` -> `product-management:metrics-review`
- **Production incident to postmortem**: `engineering:incident-response` -> `operations:runbook` -> `engineering:documentation`
- **Research to spec to stakeholder update**: `product-management:synthesize-research` -> `product-management:write-spec` -> `product-management:roadmap-update` -> `product-management:stakeholder-update`
- **Contract intake and review**: `legal:triage-nda` -> `legal:review-contract` -> `legal:legal-risk-assessment` -> `legal:signature-request`
- **Month-end close**: `finance:journal-entry` -> `finance:reconciliation` -> `finance:financial-statements` -> `finance:variance-analysis`
- **Create a new skill safely**: `anthropic-skills:skill-creator` -> `skill-hub:skill-vetter`
- **Operate a website**: `anthropic-skills:built-in-browser` -> `agent-browser` -> `example-skills:webapp-testing`

## Pending review

- [0 candidates](candidates.md) vetted and waiting for a human OK
- [0 quarantined](quarantine.md) repos that failed vetting

## Everything, A to Z

| Skill | Pack | Description |
|---|---|---|
| [`agent-browser`](skills/agent-browser.md) | browser-automation | Fast browser automation CLI for AI agents (vercel-labs/agent-browser). Use when the user asks to interact with a website, fill a form, click something |
| [`anthropic-skills:built-in-browser`](skills/anthropic-skills-built-in-browser.md) | browser-automation | Read this skill before the first step that uses the built-in browser, the browser pane inside the Claude desktop app (also called the in-app browser,  |
| [`anthropic-skills:chrome-browser`](skills/anthropic-skills-chrome-browser.md) | browser-automation | Read this skill before the first step that uses Claude in Chrome, the browser extension whose tools are named mcp__claude-in-chrome__* (also called Ch |
| [`anthropic-skills:clean-user-facing-text`](skills/anthropic-skills-clean-user-facing-text.md) | docs-content | Clean and finalize authorized natural-language text intended for readers by auditing suspicious invisible Unicode and rewriting prose while preserving |
| [`anthropic-skills:computer-use`](skills/anthropic-skills-computer-use.md) | meta-tooling | Read this skill before the first step of any request to do something in an app on the person's own computer (Notes, Finder, System Settings, any deskt |
| [`anthropic-skills:consolidate-memory`](skills/anthropic-skills-consolidate-memory.md) | productivity-automation | Reflective pass over your memory files — merge duplicates, fix stale facts, prune the index. |
| [`anthropic-skills:deep-research`](skills/anthropic-skills-deep-research.md) | research-learning | Use this skill when the user's prompt requires (1) researching a topic across multiple sources, comparing options or alternatives, analyzing trends or |
| [`anthropic-skills:docs`](skills/anthropic-skills-docs.md) | docs-content | docs (editable docs people share and comment on; the default for any document, named as a doc or not: a document, report, proposal, resume, cover lett |
| [`anthropic-skills:docx`](skills/anthropic-skills-docx.md) | docs-content | Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word templates (.dotx). Triggers include: any me |
| [`anthropic-skills:explain-usage`](skills/anthropic-skills-explain-usage.md) | research-learning | Explain where this session's tokens went, with one simple chart in plain language. Use when the user says things like "explain my usage", "where did m |
| [`anthropic-skills:google-workspace`](skills/anthropic-skills-google-workspace.md) | docs-content | Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or changes a Google file. Use this skill when |
| [`anthropic-skills:humanizer`](skills/anthropic-skills-humanizer.md) | docs-content | Personal writing filter that strips AI-sounding tells (Wikipedia's "Signs of AI writing" patterns) and Claude's own verbal tics out of any text Claude |
| [`anthropic-skills:import-memory`](skills/anthropic-skills-import-memory.md) | productivity-automation | Import a memory export from another AI assistant into Claude's memory — conversationally, additively, and with the content treated as data. |
| [`anthropic-skills:morning`](skills/anthropic-skills-morning.md) | productivity-automation | Render the user's morning brief as a styled HTML artifact, or set it up as a recurring weekday task. Use only when the user explicitly asks to run, se |
| [`anthropic-skills:pdf`](skills/anthropic-skills-pdf.md) | docs-content | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging  |
| [`anthropic-skills:pptx`](skills/anthropic-skills-pptx.md) | docs-content | Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or |
| [`anthropic-skills:schedule`](skills/anthropic-skills-schedule.md) | productivity-automation | Create or update a scheduled task that runs automatically. Use when the user says things like "every day", "each morning", "remind me in an hour", "ru |
| [`anthropic-skills:setup-claude`](skills/anthropic-skills-setup-claude.md) | meta-tooling | Guided setup — install role-matched plugins, connect your tools, try a skill. |
| [`anthropic-skills:setup-cowork`](skills/anthropic-skills-setup-cowork.md) | meta-tooling | Guided setup — install role-matched plugins, connect your tools, try a skill. |
| [`anthropic-skills:skill-creator`](skills/anthropic-skills-skill-creator.md) | meta-tooling | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or opt |
| [`anthropic-skills:xlsx`](skills/anthropic-skills-xlsx.md) | data-analytics | Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an ex |
| [`bm:add-backlog`](skills/bm-add-backlog.md) | dev-workflow | Add an idea to the backlog parking lot (999.x numbering) |
| [`bm:add-phase`](skills/bm-add-phase.md) | dev-workflow | Add phase to end of current milestone in roadmap |
| [`bm:add-tests`](skills/bm-add-tests.md) | software-dev | Generate tests for a completed phase based on UAT criteria and implementation |
| [`bm:add-todo`](skills/bm-add-todo.md) | productivity-automation | Capture idea or task as todo from current conversation context |
| [`bm:ai-integration-phase`](skills/bm-ai-integration-phase.md) | ai-ml | Generate AI design contract (AI-SPEC.md) for phases that involve building AI systems — framework selection, implementation guidance from official docs |
| [`bm:analyze-dependencies`](skills/bm-analyze-dependencies.md) | dev-workflow | Analyze phase dependencies and suggest Depends on entries for ROADMAP.md |
| [`bm:audit-fix`](skills/bm-audit-fix.md) | finance-accounting | Autonomous audit-to-fix pipeline — find issues, classify, fix, test, commit |
| [`bm:audit-milestone`](skills/bm-audit-milestone.md) | dev-workflow | Audit milestone completion against original intent before archiving |
| [`bm:audit-uat`](skills/bm-audit-uat.md) | dev-workflow | Cross-phase audit of all outstanding UAT and verification items |
| [`bm:autonomous`](skills/bm-autonomous.md) | dev-workflow | Run all remaining phases autonomously — discuss→plan→execute per phase |
| [`bm:check-todos`](skills/bm-check-todos.md) | dev-workflow | List pending todos and select one to work on |
| [`bm:cleanup`](skills/bm-cleanup.md) | dev-workflow | Archive accumulated phase directories from completed milestones |
| [`bm:code-review`](skills/bm-code-review.md) | software-dev | Review source files changed during a phase for bugs, security issues, and code quality problems |
| [`bm:code-review-fix`](skills/bm-code-review-fix.md) | software-dev | Auto-fix issues found by code review in REVIEW.md. Spawns fixer agent, commits each fix atomically, produces REVIEW-FIX.md summary. |
| [`bm:complete-milestone`](skills/bm-complete-milestone.md) | dev-workflow | Archive completed milestone and prepare for next version |
| [`bm:debug`](skills/bm-debug.md) | software-dev | Systematic debugging with persistent state across context resets |
| [`bm:discuss-phase`](skills/bm-discuss-phase.md) | dev-workflow | Gather phase context through adaptive questioning before planning. Use --all to skip area selection and discuss all gray areas interactively. Use --au |
| [`bm:do`](skills/bm-do.md) | dev-workflow | Route freeform text to the right GSD command automatically |
| [`bm:docs-update`](skills/bm-docs-update.md) | software-dev | Generate or update project documentation verified against the codebase |
| [`bm:eval-review`](skills/bm-eval-review.md) | ai-ml | Retroactively audit an executed AI phase's evaluation coverage — scores each eval dimension as COVERED/PARTIAL/MISSING and produces an actionable EVAL |
| [`bm:execute-phase`](skills/bm-execute-phase.md) | dev-workflow | Execute all plans in a phase with wave-based parallelization |
| [`bm:explore`](skills/bm-explore.md) | research-learning | Socratic ideation and idea routing — think through ideas before committing to plans |
| [`bm:extract_learnings`](skills/bm-extract-learnings.md) | dev-workflow | Extract decisions, lessons, patterns, and surprises from completed phase artifacts |
| [`bm:fast`](skills/bm-fast.md) | dev-workflow | Execute a trivial task inline — no subagents, no planning overhead |
| [`bm:forensics`](skills/bm-forensics.md) | dev-workflow | Post-mortem investigation for failed GSD workflows — analyzes git history, artifacts, and state to diagnose what went wrong |
| [`bm:from-gsd2`](skills/bm-from-gsd2.md) | dev-workflow | Import a GSD-2 (.gsd/) project back to GSD v1 (.planning/) format |
| [`bm:graphify`](skills/bm-graphify.md) | dev-workflow | Build, query, and inspect the project knowledge graph in .planning/graphs/ |
| [`bm:health`](skills/bm-health.md) | productivity-automation | Diagnose planning directory health and optionally repair issues |
| [`bm:help`](skills/bm-help.md) | dev-workflow | Show available GSD commands and usage guide |
| [`bm:import`](skills/bm-import.md) | dev-workflow | Ingest external plans with conflict detection against project decisions before writing anything. |
| [`bm:inbox`](skills/bm-inbox.md) | communication-collab | Triage and review all open GitHub issues and PRs against project templates and contribution guidelines |
| [`bm:ingest-docs`](skills/bm-ingest-docs.md) | software-dev | Scan a repo for mixed ADRs, PRDs, SPECs, and DOCs and bootstrap or merge the full .planning/ setup from them. Classifies each doc in parallel, synthes |
| [`bm:insert-phase`](skills/bm-insert-phase.md) | dev-workflow | Insert urgent work as decimal phase (e.g., 72.1) between existing phases |
| [`bm:intel`](skills/bm-intel.md) | dev-workflow | Query, inspect, or refresh codebase intelligence files in .planning/intel/ |
| [`bm:join-discord`](skills/bm-join-discord.md) | communication-collab | Join the GSD Discord community |
| [`bm:list-phase-assumptions`](skills/bm-list-phase-assumptions.md) | dev-workflow | Surface Claude's assumptions about a phase approach before planning |
| [`bm:list-workspaces`](skills/bm-list-workspaces.md) | dev-workflow | List active GSD workspaces and their status |
| [`bm:manager`](skills/bm-manager.md) | dev-workflow | Interactive command center for managing multiple phases from one terminal |
| [`bm:map-codebase`](skills/bm-map-codebase.md) | software-dev | Analyze codebase with parallel mapper agents to produce .planning/codebase/ documents |
| [`bm:milestone-summary`](skills/bm-milestone-summary.md) | dev-workflow | Generate a comprehensive project summary from milestone artifacts for team onboarding and review |
| [`bm:mvp-phase`](skills/bm-mvp-phase.md) | dev-workflow | Plan an MVP-mode phase — captures an "As a / I want to / So that" user story, runs SPIDR splitting, then delegates to plan-phase |
| [`bm:new-ddd`](skills/bm-new-ddd.md) | software-dev | Initialize a new project using Documentation-Driven Development. Research, then write user-facing docs (SPEC.md) as the spec, then user validates docs |
| [`bm:new-milestone`](skills/bm-new-milestone.md) | dev-workflow | Start a new milestone cycle — update PROJECT.md and route to requirements |
| [`bm:new-project`](skills/bm-new-project.md) | dev-workflow | Initialize a new project with deep context gathering and PROJECT.md |
| [`bm:new-workspace`](skills/bm-new-workspace.md) | dev-workflow | Create an isolated workspace with repo copies and independent .planning/ |
| [`bm:next`](skills/bm-next.md) | dev-workflow | Automatically advance to the next logical step in the GSD workflow |
| [`bm:note`](skills/bm-note.md) | productivity-automation | Zero-friction idea capture. Append, list, or promote notes to todos. |
| [`bm:pause-work`](skills/bm-pause-work.md) | dev-workflow | Create context handoff when pausing work mid-phase |
| [`bm:plan-milestone-gaps`](skills/bm-plan-milestone-gaps.md) | dev-workflow | Create phases to close all gaps identified by milestone audit |
| [`bm:plan-phase`](skills/bm-plan-phase.md) | dev-workflow | Create detailed phase plan (PLAN.md) with verification loop |
| [`bm:plant-seed`](skills/bm-plant-seed.md) | dev-workflow | Capture a forward-looking idea with trigger conditions — surfaces automatically at the right milestone |
| [`bm:pr-branch`](skills/bm-pr-branch.md) | mlops-devops | Create a clean PR branch by filtering out .planning/ commits — ready for code review |
| [`bm:profile-user`](skills/bm-profile-user.md) | meta-tooling | Generate developer behavioral profile and create Claude-discoverable artifacts |
| [`bm:progress`](skills/bm-progress.md) | dev-workflow | Check project progress, show context, and route to next action (execute or plan). Use --forensic to append a 6-check integrity audit after the standar |
| [`bm:quick`](skills/bm-quick.md) | dev-workflow | Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents |
| [`bm:reapply-patches`](skills/bm-reapply-patches.md) | communication-collab | Reapply local modifications after a GSD update |
| [`bm:remember-access`](skills/bm-remember-access.md) | productivity-automation | Capture or review how this project connects to external systems (GitHub, AWS, npm, SSH, etc.) so future sessions know the auth recipe. Auto-detection  |
| [`bm:remove-phase`](skills/bm-remove-phase.md) | dev-workflow | Remove a future phase from roadmap and renumber subsequent phases |
| [`bm:remove-workspace`](skills/bm-remove-workspace.md) | dev-workflow | Remove a GSD workspace and clean up worktrees |
| [`bm:research-phase`](skills/bm-research-phase.md) | dev-workflow | Research how to implement a phase (standalone - usually use /bm:plan-phase instead) |
| [`bm:resume-at`](skills/bm-resume-at.md) | dev-workflow | Schedule a future resume of work - e.g. '/bm:resume-at 09:00', '/bm:resume-at +2h', or '/bm:resume-at 04:00 --cmd /bm:execute-phase 9' |
| [`bm:resume-work`](skills/bm-resume-work.md) | dev-workflow | Resume work from previous session with full context restoration |
| [`bm:review`](skills/bm-review.md) | dev-workflow | Request cross-AI peer review of phase plans from external AI CLIs |
| [`bm:review-backlog`](skills/bm-review-backlog.md) | dev-workflow | Review and promote backlog items to active milestone |
| [`bm:scan`](skills/bm-scan.md) | software-dev | Rapid codebase assessment — lightweight alternative to /bm:map-codebase |
| [`bm:secure-phase`](skills/bm-secure-phase.md) | security | Retroactively verify threat mitigations for a completed phase |
| [`bm:session-report`](skills/bm-session-report.md) | docs-content | Generate a session report with token usage estimates, work summary, and outcomes |
| [`bm:set-profile`](skills/bm-set-profile.md) | dev-workflow | Switch model profile for GSD agents (quality/balanced/budget/inherit) |
| [`bm:settings`](skills/bm-settings.md) | meta-tooling | Configure GSD workflow toggles and model profile |
| [`bm:ship`](skills/bm-ship.md) | mlops-devops | Create PR, run review, and prepare for merge after verification passes |
| [`bm:sketch`](skills/bm-sketch.md) | web-frontend-design | Sketch UI/design ideas with throwaway HTML mockups, or propose what to sketch next (frontier mode) |
| [`bm:sketch-wrap-up`](skills/bm-sketch-wrap-up.md) | dev-workflow | Package sketch design findings into a persistent project skill for future build conversations |
| [`bm:spec-phase`](skills/bm-spec-phase.md) | dev-workflow | Socratic spec refinement — clarify WHAT a phase delivers with ambiguity scoring before discuss-phase. Produces a SPEC.md with falsifiable requirements |
| [`bm:spike`](skills/bm-spike.md) | research-learning | Spike an idea through experiential exploration, or propose what to spike next (frontier mode) |
| [`bm:spike-wrap-up`](skills/bm-spike-wrap-up.md) | dev-workflow | Package spike findings into a persistent project skill for future build conversations |
| [`bm:stats`](skills/bm-stats.md) | dev-workflow | Display project statistics — phases, plans, requirements, git metrics, and timeline |
| [`bm:thread`](skills/bm-thread.md) | dev-workflow | Manage persistent context threads for cross-session work |
| [`bm:ui-phase`](skills/bm-ui-phase.md) | web-frontend-design | Generate UI design contract (UI-SPEC.md) for frontend phases |
| [`bm:ui-review`](skills/bm-ui-review.md) | web-frontend-design | Retroactive 6-pillar visual audit of implemented frontend code |
| [`bm:ultraplan-phase`](skills/bm-ultraplan-phase.md) | dev-workflow | [BETA] Offload plan phase to Claude Code's ultraplan cloud — drafts remotely while terminal stays free, review in browser with inline comments, import |
| [`bm:undo`](skills/bm-undo.md) | dev-workflow | Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks. |
| [`bm:update`](skills/bm-update.md) | meta-tooling | Update GSD to latest version with changelog display |
| [`bm:validate-phase`](skills/bm-validate-phase.md) | dev-workflow | Retroactively audit and fill Nyquist validation gaps for a completed phase |
| [`bm:verify-work`](skills/bm-verify-work.md) | dev-workflow | Validate built features through conversational UAT |
| [`bm:version`](skills/bm-version.md) | meta-tooling | Print the installed GSD plugin version and check online for updates |
| [`bm:workstreams`](skills/bm-workstreams.md) | dev-workflow | Manage parallel workstreams — list, create, switch, status, progress, complete, and resume |
| [`claude-api`](skills/claude-api.md) | ai-ml | Reference for the Claude API and Anthropic SDKs - model ids, pricing, streaming, tool use, MCP, agents, prompt caching, token counting, model migratio |
| [`claude-code-setup:claude-automation-recommender`](skills/claude-code-setup-claude-automation-recommender.md) | meta-tooling | Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommend |
| [`code-review`](skills/code-review.md) | software-dev | Review the current diff or a PR number, branch or path for correctness bugs at a chosen effort level; optionally post inline PR comments or apply fixe |
| [`cowork-plugin-management:cowork-plugin-customizer`](skills/cowork-plugin-management-cowork-plugin-customizer.md) | meta-tooling | Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, set up plugin, configure plugin, tailor  |
| [`cowork-plugin-management:create-cowork-plugin`](skills/cowork-plugin-management-create-cowork-plugin.md) | meta-tooling | Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a plugin, build a plugin, make a new plugin, |
| [`dataviz`](skills/dataviz.md) | data-analytics | Create any chart, graph, plot, dashboard or data visualization in any medium (HTML/SVG artifact, matplotlib, plotly, d3). Read before choosing chart c |
| [`engineering:architecture`](skills/engineering-architecture.md) | software-dev | Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision w |
| [`engineering:code-review`](skills/engineering-code-review.md) | software-dev | Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or  |
| [`engineering:debug`](skills/engineering-debug.md) | software-dev | Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not pro |
| [`engineering:deploy-checklist`](skills/engineering-deploy-checklist.md) | mlops-devops | Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI st |
| [`engineering:documentation`](skills/engineering-documentation.md) | software-dev | Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide",  |
| [`engineering:incident-response`](skills/engineering-incident-response.md) | mlops-devops | Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert that |
| [`engineering:standup`](skills/engineering-standup.md) | communication-collab | Generate a standup update from recent activity. Use when preparing for daily standup, summarizing yesterday's commits and PRs and ticket moves, format |
| [`engineering:system-design`](skills/engineering-system-design.md) | software-dev | Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right arc |
| [`engineering:tech-debt`](skills/engineering-tech-debt.md) | software-dev | Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or wh |
| [`engineering:testing-strategy`](skills/engineering-testing-strategy.md) | software-dev | Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need" |
| [`example-skills:algorithmic-art`](skills/example-skills-algorithmic-art.md) | creative-media | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code |
| [`example-skills:brand-guidelines`](skills/example-skills-brand-guidelines.md) | web-frontend-design | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when b |
| [`example-skills:canvas-design`](skills/example-skills-canvas-design.md) | web-frontend-design | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece |
| [`example-skills:doc-coauthoring`](skills/example-skills-doc-coauthoring.md) | software-dev | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, deci |
| [`example-skills:frontend-design`](skills/example-skills-frontend-design.md) | web-frontend-design | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and |
| [`example-skills:internal-comms`](skills/example-skills-internal-comms.md) | communication-collab | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill |
| [`example-skills:mcp-builder`](skills/example-skills-mcp-builder.md) | ai-ml | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools.  |
| [`example-skills:skill-creator`](skills/example-skills-skill-creator.md) | meta-tooling | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or opt |
| [`example-skills:slack-gif-creator`](skills/example-skills-slack-gif-creator.md) | creative-media | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users |
| [`example-skills:theme-factory`](skills/example-skills-theme-factory.md) | web-frontend-design | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with |
| [`example-skills:web-artifacts-builder`](skills/example-skills-web-artifacts-builder.md) | web-frontend-design | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui |
| [`example-skills:webapp-testing`](skills/example-skills-webapp-testing.md) | browser-automation | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, ca |
| [`fewer-permission-prompts`](skills/fewer-permission-prompts.md) | meta-tooling | Scan transcripts for common read-only Bash and MCP tool calls and add a prioritized allowlist to project settings to reduce permission prompts. |
| [`finance:audit-support`](skills/finance-audit-support.md) | finance-accounting | Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards. Use when generating testing workpapers, se |
| [`finance:close-management`](skills/finance-close-management.md) | operations-business | Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning the close calendar, tracking close progr |
| [`finance:financial-statements`](skills/finance-financial-statements.md) | finance-accounting | Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis. Use when preparin |
| [`finance:journal-entry`](skills/finance-journal-entry.md) | finance-accounting | Prepare journal entries with proper debits, credits, and supporting detail. Use when booking month-end accruals (AP, payroll, prepaid), recording depr |
| [`finance:journal-entry-prep`](skills/finance-journal-entry-prep.md) | finance-accounting | Prepare journal entries with proper debits, credits, and supporting documentation for month-end close. Use when booking accruals, prepaid amortization |
| [`finance:reconciliation`](skills/finance-reconciliation.md) | finance-accounting | Reconcile accounts by comparing GL balances to subledgers, bank statements, or third-party data. Use when performing bank reconciliations, GL-to-suble |
| [`finance:sox-testing`](skills/finance-sox-testing.md) | finance-accounting | Generate SOX sample selections, testing workpapers, and control assessments. Use when planning quarterly or annual SOX 404 testing, pulling a sample f |
| [`finance:variance-analysis`](skills/finance-variance-analysis.md) | data-analytics | Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyzing budget vs. actual, period-over-perio |
| [`frontend-design:frontend-design`](skills/frontend-design-frontend-design.md) | web-frontend-design | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and |
| [`impeccable:impeccable`](skills/impeccable-impeccable.md) | web-frontend-design | Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or |
| [`init`](skills/init.md) | software-dev | Initialize a project with a CLAUDE.md that documents the codebase for future sessions. |
| [`karpathy-guidelines`](skills/karpathy-guidelines.md) | software-dev | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical  |
| [`keybindings-help`](skills/keybindings-help.md) | meta-tooling | Customize keyboard shortcuts, rebind keys, add chord bindings or edit ~/.claude/keybindings.json. |
| [`legal:brief`](skills/legal-brief.md) | communication-collab | Generate contextual briefings for legal work — daily summary, topic research, or incident response. Use when starting your day and need a scan of lega |
| [`legal:compliance-check`](skills/legal-compliance-check.md) | legal-compliance | Run a compliance check on a proposed action, product feature, or business initiative, surfacing applicable regulations, required approvals, and risk a |
| [`legal:legal-response`](skills/legal-legal-response.md) | legal-compliance | Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a template |
| [`legal:legal-risk-assessment`](skills/legal-legal-risk-assessment.md) | legal-compliance | Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal e |
| [`legal:meeting-briefing`](skills/legal-meeting-briefing.md) | communication-collab | Prepare structured briefings for meetings with legal relevance and track resulting action items. Use when preparing for contract negotiations, board m |
| [`legal:review-contract`](skills/legal-review-contract.md) | legal-compliance | Review a contract against your organization's negotiation playbook — flag deviations, generate redlines, provide business impact analysis. Use when re |
| [`legal:signature-request`](skills/legal-signature-request.md) | legal-compliance | Prepare and route a document for e-signature — run a pre-signature checklist, configure signing order, and send for execution. Use when a contract is  |
| [`legal:triage-nda`](skills/legal-triage-nda.md) | legal-compliance | Rapidly triage an incoming NDA and classify it as GREEN (standard approval), YELLOW (counsel review), or RED (full legal review). Use when a new NDA a |
| [`legal:vendor-check`](skills/legal-vendor-check.md) | legal-compliance | Check the status of existing agreements with a vendor across all connected systems — CLM, CRM, email, and document storage — with gap analysis and upc |
| [`linkedin-humanizer`](skills/linkedin-humanizer.md) | careers-jobs | Remove the AI tells human readers and LinkedIn's AI-slop filter react to in a post or comment: 2026 vocabulary by paragraph density, reveal bridges, s |
| [`linkedin-profile-optimizer`](skills/linkedin-profile-optimizer.md) | careers-jobs | Audit and rewrite a LinkedIn profile end-to-end for 2026: headline, About 7-step, Featured, banner, photo, Experience metrics, Skills, custom URL, rec |
| [`loop`](skills/loop.md) | productivity-automation | Run a prompt or slash command on a recurring interval, or let the model self-pace. Use when the user wants to poll for status or repeat something on a |
| [`modern-web-guidance:chrome-extensions`](skills/modern-web-guidance-chrome-extensions.md) | browser-automation | Build and publish Chrome Extensions using Manifest V3 best practices. Use this skill whenever the user asks to create, modify, debug, or understand Ch |
| [`modern-web-guidance:modern-web-guidance`](skills/modern-web-guidance-modern-web-guidance.md) | software-dev | Search tool for modern web development best practices. MANDATORY: Execute FIRST for all HTML/CSS and clientside JS tasks. Do NOT skip — web APIs evolv |
| [`operations:capacity-plan`](skills/operations-capacity-plan.md) | operations-business | Plan resource capacity — workload analysis and utilization forecasting. Use when heading into quarterly planning, the team feels overallocated and you |
| [`operations:change-request`](skills/operations-change-request.md) | operations-business | Create a change management request with impact analysis and rollback plan. Use when proposing a system or process change that needs approval, preparin |
| [`operations:compliance-tracking`](skills/operations-compliance-tracking.md) | legal-compliance | Track compliance requirements and audit readiness. Trigger with "compliance", "audit prep", "SOC 2", "ISO 27001", "GDPR", "regulatory requirement", or |
| [`operations:process-doc`](skills/operations-process-doc.md) | operations-business | Document a business process — flowcharts, RACI, and SOPs. Use when formalizing a process that lives in someone's head, building a RACI to clarify who  |
| [`operations:process-optimization`](skills/operations-process-optimization.md) | operations-business | Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bott |
| [`operations:risk-assessment`](skills/operations-risk-assessment.md) | legal-compliance | Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or whe |
| [`operations:runbook`](skills/operations-runbook.md) | mlops-devops | Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably, tu |
| [`operations:status-report`](skills/operations-status-report.md) | operations-business | Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health wi |
| [`operations:vendor-review`](skills/operations-vendor-review.md) | legal-compliance | Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor proposal, deciding whether to renew or replace |
| [`playwright-cli`](skills/playwright-cli.md) | browser-automation | Official Microsoft browser automation CLI (@playwright/cli). Use when the user asks to automate browser interactions, run/generate Playwright tests, n |
| [`plugin-authoring`](skills/plugin-authoring.md) | meta-tooling | Make a mod - a change to Claude's own interface or behaviour such as a panel, status line, toast, slash command or hook on tool calls. |
| [`product-management:brainstorm`](skills/product-management-brainstorm.md) | product-mgmt | Brainstorm a product idea, problem space, or strategic question with a sharp thinking partner |
| [`product-management:competitive-brief`](skills/product-management-competitive-brief.md) | product-mgmt | Create a competitive analysis brief for one or more competitors or a feature area. Use when informing product strategy or feature prioritization, buil |
| [`product-management:metrics-review`](skills/product-management-metrics-review.md) | data-analytics | Review and analyze product metrics with trend analysis and actionable insights. Use when running a weekly, monthly, or quarterly metrics review, inves |
| [`product-management:product-brainstorming`](skills/product-management-product-brainstorming.md) | product-mgmt | Brainstorm product ideas, explore problem spaces, and challenge assumptions as a thinking partner. Use when exploring a new opportunity, generating so |
| [`product-management:roadmap-update`](skills/product-management-roadmap-update.md) | product-mgmt | Update, create, or reprioritize your product roadmap. Use when adding a new initiative and deciding what moves to make room, shifting priorities after |
| [`product-management:sprint-planning`](skills/product-management-sprint-planning.md) | dev-workflow | Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan. Use when kicking off a new sprint, sizing a backlog against team av |
| [`product-management:stakeholder-update`](skills/product-management-stakeholder-update.md) | communication-collab | Generate a stakeholder update tailored to audience and cadence. Use when writing a weekly or monthly status for leadership, announcing a launch, escal |
| [`product-management:synthesize-research`](skills/product-management-synthesize-research.md) | research-learning | Synthesize user research from interviews, surveys, and feedback into structured insights. Use when you have a pile of interview notes, survey response |
| [`product-management:write-spec`](skills/product-management-write-spec.md) | product-mgmt | Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scopin |
| [`productivity:memory-management`](skills/productivity-memory-management.md) | productivity-automation | Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude unders |
| [`productivity:start`](skills/productivity-start.md) | productivity-automation | Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your e |
| [`productivity:task-management`](skills/productivity-task-management.md) | productivity-automation | Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help t |
| [`productivity:update`](skills/productivity-update.md) | communication-collab | Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or  |
| [`reverse-engineer-anything`](skills/reverse-engineer-anything.md) | security | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. Use shipped-artifact or requested runtime evi |
| [`run`](skills/run.md) | software-dev | Launch and drive this project's app to see a change working. Use when asked to run, start or screenshot the app or to confirm a change works end to en |
| [`schedule`](skills/schedule.md) | productivity-automation | Create, update, list or run scheduled cloud agents (routines) on a cron schedule. Use for recurring cloud agents or one-time scheduled runs. |
| [`security-review`](skills/security-review.md) | security | Security review of the pending changes on the current branch. |
| [`simplify`](skills/simplify.md) | software-dev | Review changed code for reuse, simplification, efficiency and altitude cleanups, then apply the fixes. Quality only, not bug hunting. |
| [`skill-hub:job-search-copilot`](skills/skill-hub-job-search-copilot.md) | careers-jobs | End-to-end job search help for tech, AI/ML and data roles. Use for resume or CV tailoring, job description analysis, cover letters, referral and recru |
| [`skill-hub:master-skill`](skills/skill-hub-master-skill.md) | meta-tooling | Router for every other skill. Use at the start of any non-trivial request, and whenever it is unclear which skill, plugin or workflow fits - "which sk |
| [`skill-hub:ml-interview-prep`](skills/skill-hub-ml-interview-prep.md) | careers-jobs | Interview preparation for ML engineer, AI engineer, MLOps, data scientist and applied-LLM roles. Use for "prep me for an ML interview", a study plan f |
| [`skill-hub:skill-vetter`](skills/skill-hub-skill-vetter.md) | meta-tooling | Security-vet an Agent Skill, plugin folder or a GitHub repo of skills before installing or sharing it. Use whenever the user is about to install, copy |
| [`taste-skill:brandkit`](skills/taste-skill-brandkit.md) | creative-media | Premium brand-kit image generation skill for creating high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations.  |
| [`taste-skill:brutalist-skill`](skills/taste-skill-brutalist-skill.md) | web-frontend-design | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. Rigid grids, extreme type scale contrast, utilitarian colo |
| [`taste-skill:gpt-tasteskill`](skills/taste-skill-gpt-tasteskill.md) | web-frontend-design | Elite UX/UI & Advanced GSAP Motion Engineer. Enforces Python-driven true randomization for layout variance, strict AIDA page structure, wide editorial |
| [`taste-skill:image-to-code-skill`](skills/taste-skill-image-to-code-skill.md) | creative-media | Elite website image-to-code skill for Codex. For visually important web tasks, it must first generate the design image(s) itself, deeply analyze them, |
| [`taste-skill:imagegen-frontend-mobile`](skills/taste-skill-imagegen-frontend-mobile.md) | creative-media | Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobi |
| [`taste-skill:imagegen-frontend-web`](skills/taste-skill-imagegen-frontend-web.md) | web-frontend-design | Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITICAL OUTPUT RULE — generate ONE separate  |
| [`taste-skill:minimalist-skill`](skills/taste-skill-minimalist-skill.md) | web-frontend-design | Clean editorial-style interfaces. Warm monochrome palette, typographic contrast, flat bento grids, muted pastels. No gradients, no heavy shadows. |
| [`taste-skill:output-skill`](skills/taste-skill-output-skill.md) | software-dev | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply |
| [`taste-skill:redesign-skill`](skills/taste-skill-redesign-skill.md) | web-frontend-design | Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns, and applies high-end design standards w |
| [`taste-skill:soft-skill`](skills/taste-skill-soft-skill.md) | web-frontend-design | Teaches the AI to design like a high-end agency. Defines the exact fonts, spacing, shadows, card structures, and animations that make a website feel e |
| [`taste-skill:stitch-skill`](skills/taste-skill-stitch-skill.md) | web-frontend-design | Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typo |
| [`taste-skill:taste-skill`](skills/taste-skill-taste-skill.md) | web-frontend-design | Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfa |
| [`taste-skill:taste-skill-v1`](skills/taste-skill-taste-skill-v1.md) | web-frontend-design | The original v1 taste-skill, preserved for projects depending on its exact behavior. The current default is `design-taste-frontend` (v2 experimental), |
| [`update-config`](skills/update-config.md) | meta-tooling | Configure the Claude Code harness via settings.json - hooks, permissions, environment variables and other automated behaviours. |
| [`workflow-authoring`](skills/workflow-authoring.md) | meta-tooling | Reference for writing a Workflow tool script that orchestrates multiple subagents - script API, resume, quality patterns, worked examples. |
