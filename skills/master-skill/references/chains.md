# Chains

Multi-skill workflows. Invoke each skill when its step begins.

## Land a job - research, tailor, polish

1. `anthropic-skills:deep-research` - Research the company, team and role requirements
2. `skill-hub:job-search-copilot` - Decode the JD, map evidence, tailor resume and cover letter truthfully
3. `anthropic-skills:docx` - Produce the resume / cover letter as a Word file
4. `anthropic-skills:humanizer` - Strip AI tells so it reads like you
5. `linkedin-profile-optimizer` - Align the LinkedIn profile with the same story

## Prepare for an ML / AI interview

1. `anthropic-skills:deep-research` - Research the company, team and stack
2. `skill-hub:ml-interview-prep` - Plan, drill, mock and debrief with a graded log
3. `skill-hub:job-search-copilot` - Offer comparison and negotiation once offers arrive

## LinkedIn profile and posts

1. `linkedin-profile-optimizer` - Audit and rewrite headline, About, Experience
2. `linkedin-humanizer` - Make posts and comments read human

## Build and ship an LLM application

1. `claude-api` - Correct model ids, params, caching, tool use
2. `example-skills:mcp-builder` - Wrap tools/data as an MCP server
3. `engineering:testing-strategy` - Test plan incl. evals for non-deterministic output
4. `engineering:deploy-checklist` - Pre-deploy checklist and rollback plan

## Plan and audit AI evaluation

1. `bm:ai-integration-phase` - Pick framework, design eval strategy and guardrails
2. `bm:eval-review` - Audit the implemented eval coverage

## Spec-driven delivery from idea to shipped PR

1. `bm:new-project` - Capture goals, requirements and roadmap
2. `bm:plan-phase` - Plan the next phase with goal-backward checks
3. `bm:execute-phase` - Execute plans with atomic commits
4. `bm:verify-work` - Verify the phase goal is actually met
5. `bm:ship` - Open the PR

## Debug, fix, then lock it in with tests

1. `engineering:debug` - Reproduce, isolate, find root cause
2. `bm:add-tests` - Add regression tests
3. `code-review` - Review the fix before merging

## Pre-merge quality pass

1. `simplify` - Remove duplication, tighten code
2. `code-review` - Find correctness bugs in the diff
3. `security-review` - Check the change for security issues

## Design and build a polished web UI

1. `impeccable:impeccable` - Shape the design direction and critique it
2. `frontend-design:frontend-design` - Implement distinctive production-grade UI
3. `example-skills:webapp-testing` - Drive the page with Playwright to verify it

## Researched report or briefing

1. `anthropic-skills:deep-research` - Multi-source research with citations
2. `anthropic-skills:docx` - Deliver as a Word document
3. `anthropic-skills:humanizer` - Polish the prose

## Research-backed slide deck

1. `anthropic-skills:deep-research` - Gather the substance
2. `anthropic-skills:pptx` - Build the deck

## Spreadsheet to insight

1. `anthropic-skills:xlsx` - Clean and structure the data
2. `dataviz` - Choose charts and colors that read clearly
3. `product-management:metrics-review` - Interpret trends and call out actions

## Production incident to postmortem

1. `engineering:incident-response` - Triage, communicate, mitigate
2. `operations:runbook` - Turn the fix into a runbook
3. `engineering:documentation` - Write the postmortem

## Research to spec to stakeholder update

1. `product-management:synthesize-research` - Distill user research
2. `product-management:write-spec` - Write the spec
3. `product-management:roadmap-update` - Place it on the roadmap
4. `product-management:stakeholder-update` - Tell stakeholders

## Contract intake and review

1. `legal:triage-nda` - Fast green/yellow/red classification for NDAs
2. `legal:review-contract` - Clause-by-clause review and redlines
3. `legal:legal-risk-assessment` - Grade the risks
4. `legal:signature-request` - Route for e-signature

## Month-end close

1. `finance:journal-entry` - Prepare journal entries
2. `finance:reconciliation` - Reconcile accounts
3. `finance:financial-statements` - Generate statements
4. `finance:variance-analysis` - Explain the variances

## Create a new skill safely

1. `anthropic-skills:skill-creator` - Draft, test and tune the skill
2. `skill-hub:skill-vetter` - Static security vet before sharing

## Operate a website

1. `anthropic-skills:built-in-browser` - Use the in-app browser pane first
2. `agent-browser` - CLI automation for scripted flows
3. `example-skills:webapp-testing` - Playwright for local web apps
