# Quarantine

These failed vetting. Findings show rule ids and short excerpts only. Do not install them.

| Repo / skill | Why | Pinned commit |
|---|---|---|
| Egonex-AI/Understand-Anything:understand-domain | persistence (extract-domain-context.py:106) | `4e6d329901` |
| JimLiu/baoyu-skills:baoyu-post-to-wechat | exfil-sink (scripts/wechat-article.ts:109); cred-paths (scripts/wechat-extend-config.test.ts:163); cred-paths (scripts/wechat-extend-config.test.ts:164) | `0a27d7d40e` |
| addyosmani/agent-skills:source-driven-development | inj-override (SKILL.md:110) | `301b02b12b` |
| anthropics/claude-code:Plugin Structure | exfil-sink (SKILL.md:383) | `2eff7a8d21` |
| anthropics/claude-plugins-official:plugin-structure | exfil-sink (SKILL.md:383) | `a7ba5b93db` |
| anthropics/claude-plugins-official:receipts | inj-override (SKILL.md:142); inj-override (scripts/mine-transcripts.mjs:347) | `a7ba5b93db` |
| anthropics/knowledge-work-plugins:nextflow-development | exec-remote (scripts/check_environment.py:120) | `2574e29377` |
| anthropics/skills:claude-api | cred-paths (shared/evals/report/build-report-lite.mjs:28); cred-paths (shared/evals/report/runner-scaffold.mjs:112); inj-override (shared/model-migration.md:863) | `ca45fc496a` |
| career-ops-hq/career-ops:career-ops | no-skill-md (:0); symlink (SKILL.md:0) | `20b9fd3a9c` |
| code-yeongyu/oh-my-openagent:data-scientist | exec-remote (scripts/setup-uv.ps1:28); exec-remote (scripts/setup-uv.sh:39); exec-remote (scripts/setup-uv.sh:41) | `7d4a61e0d8` |
| code-yeongyu/oh-my-openagent:frontend | exec-remote (scripts/perfection/lighthouse-audit.py:13) | `7d4a61e0d8` |
| code-yeongyu/oh-my-openagent:programming | exec-remote (scripts/go/new-project.ts:8); exec-remote (scripts/python/new-project.ts:6); exec-remote (scripts/python/new-project.ts:7) | `7d4a61e0d8` |
| code-yeongyu/oh-my-openagent:ultimate-browsing | inj-secret-exfil (references/insane-search/jina.md:66) | `7d4a61e0d8` |
| coreyhaines31/marketingskills:directory-submissions | exfil-sink (references/submission-tracker-template.csv:158) | `88c79f6528` |
| coreyhaines31/marketingskills:lead-magnets | inj-override (evals/evals.json:100); inj-override (references/content-to-skill-corpus-design.md:42) | `88c79f6528` |
| garrytan/gstack:benchmark-models | cred-paths (SKILL.md.tmpl:94) | `6f7488a70f` |
| garrytan/gstack:browse | inj-override (src/cli.ts:1299); exfil-sink (src/content-security.ts:325); exfil-sink (src/content-security.ts:327) | `6f7488a70f` |
| garrytan/gstack:careful | destructive (SKILL.md.tmpl:67); exec-remote (SKILL.md.tmpl:69); destructive (bin/check-careful.sh:36) | `6f7488a70f` |
| garrytan/gstack:gstack | exec-remote (.github/docker/Dockerfile.ci:102); cred-paths (.github/scripts/dia-gui-readiness.c:76); cred-paths (.github/scripts/qualify-dia-macos.ts:1014) | `6f7488a70f` |
| garrytan/gstack:gstack-upgrade | exec-remote (SKILL.md.tmpl:178) | `6f7488a70f` |
| heygen-com/hyperframes:frost-sequence-camera-orbit | exec-obfuscated (assets/frost.js:1063) | `618c486734` |
| nanocoai/nanoclaw:add-cursor | secret-material (payload/container/agent-runner/src/providers/cursor.gateway-proxy.test.ts:67); inj-secret-exfil (payload/container/agent-runner/src/providers/cursor.gateway-proxy.test.ts:587) | `acc2b1c8f5` |
| nanocoai/nanoclaw:add-dashboard | inj-secret-exfil (SKILL.md:87) | `acc2b1c8f5` |
| nanocoai/nanoclaw:add-iron-proxy | exec-remote (scripts/install-claude.sh:10); exec-remote (scripts/install-claude.sh:34) | `acc2b1c8f5` |
| nanocoai/nanoclaw:add-onecli | exec-remote (scripts/install-claude.sh:11); exec-remote (scripts/install-claude.sh:32); exec-remote (scripts/register-claude-token.sh:30) | `acc2b1c8f5` |
| nanocoai/nanoclaw:add-teams | exfil-sink (SKILL.md:111) | `acc2b1c8f5` |
| nanocoai/nanoclaw:add-telegram | exfil-sink (SKILL.md:138); exfil-sink (SKILL.md:176) | `acc2b1c8f5` |
| nexu-io/open-design:docs-page | exec-remote (example.html:83) | `5a0c477779` |
| openai/skills:cloudflare-deploy | exfil-sink (references/pages-functions/patterns.md:14) | `49f948faa9` |
| openai/skills:screenshot | exec-obfuscated (scripts/take_screenshot.py:27) | `49f948faa9` |
| sickn33/agentic-awesome-skills:007 | inj-override (references/ai-agent-security.md:20); inj-roleplay (references/ai-agent-security.md:20); inj-override (references/ai-agent-security.md:412) | `c5ddd3aa2c` |
| sickn33/agentic-awesome-skills:2slides-ppt-generator | inj-secret-exfil (SKILL.md:37) | `c5ddd3aa2c` |
| sickn33/agentic-awesome-skills:agent-evals | inj-override (SKILL.md:163); inj-roleplay (SKILL.md:164); inj-override (SKILL.md:267) | `c5ddd3aa2c` |
| sickn33/agentic-awesome-skills:agent-evaluation | inj-override (references/architecture-sketches.md:392) | `c5ddd3aa2c` |
| sno-ai/sno-station-skills:pl | cred-paths (scripts/exec-trust.t:89) | `1c92b0ff89` |
| sno-ai/sno-station-skills:rem-reflect | persistence (scripts/journey-ops.test.ts:2); persistence (scripts/journey-ops.test.ts:83); persistence (scripts/journey-ops.test.ts:84) | `1c92b0ff89` |
| thedotmack/claude-mem:Agent Cost Report | cred-paths (scripts/tests/test_render.py:168) | `26ccf4d8a0` |
| thedotmack/claude-mem:do | no-skill-md (:0); symlink (SKILL.md:0) | `26ccf4d8a0` |
| thedotmack/claude-mem:mode-creator | exfil-sink (scripts/configure-telegram.mjs:108) | `26ccf4d8a0` |
| thedotmack/claude-mem:openclaw | exec-remote (install.sh:419); exec-remote (install.sh:422); exec-remote (install.sh:479) | `26ccf4d8a0` |
| titanwings/distilly:distilly | cred-paths (tools/dingtalk_auto_collector.py:498); cred-paths (tools/feishu_browser.py:38) | `0afc45c29c` |
