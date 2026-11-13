# Quarantine

These failed vetting. Findings show rule ids and short excerpts only. Do not install them.

| Repo / skill | Why | Pinned commit |
|---|---|---|
| Egonex-AI/Understand-Anything:understand-domain | persistence (extract-domain-context.py:106) | `a6ea402476` |
| JimLiu/baoyu-skills:baoyu-post-to-wechat | exfil-sink (scripts/wechat-article.ts:109); cred-paths (scripts/wechat-extend-config.test.ts:163); cred-paths (scripts/wechat-extend-config.test.ts:164) | `ca703c2d7c` |
| addyosmani/agent-skills:source-driven-development | inj-override (SKILL.md:110) | `301b02b12b` |
| affaan-m/ECC:homelab-pihole-dns | raw-ip-url (SKILL.md:177); raw-ip-url (SKILL.md:178) | `b38be6a7f6` |
| affaan-m/ECC:skill-comply | cred-paths (tests/test_runner.py:390) | `b38be6a7f6` |
| affaan-m/ECC:story-lifecycle | inj-override (SKILL.md:87) | `b38be6a7f6` |
| anbeime/skill:chrome-automation | exec-remote (scripts/auto-install-mac.sh:68); cred-paths (scripts/start-chrome-mac.sh:8); cred-paths (scripts/start-chrome-mac.sh:9) | `d7d186b45d` |
| anbeime/skill:xiaoyue-companion | persistence (setup_scheduled_task.ps1:25) | `d7d186b45d` |
| anthropics/claude-code:Plugin Structure | exfil-sink (SKILL.md:383) | `2eff7a8d21` |
| anthropics/claude-plugins-official:plugin-structure | exfil-sink (SKILL.md:383) | `0412be76f5` |
| anthropics/claude-plugins-official:receipts | inj-override (SKILL.md:142); inj-override (scripts/mine-transcripts.mjs:347) | `0412be76f5` |
| anthropics/knowledge-work-plugins:nextflow-development | exec-remote (scripts/check_environment.py:120) | `02717ef044` |
| anthropics/skills:claude-api | cred-paths (shared/evals/report/build-report-lite.mjs:28); cred-paths (shared/evals/report/runner-scaffold.mjs:112); inj-override (shared/model-migration.md:863) | `2c5958ecac` |
| career-ops-hq/career-ops:career-ops | no-skill-md (:0); symlink (SKILL.md:0) | `e83160c170` |
| code-yeongyu/oh-my-openagent:data-scientist | exec-remote (scripts/setup-uv.ps1:28); exec-remote (scripts/setup-uv.sh:39); exec-remote (scripts/setup-uv.sh:41) | `2faeda01ea` |
| code-yeongyu/oh-my-openagent:frontend | exec-remote (scripts/perfection/lighthouse-audit.py:13) | `2faeda01ea` |
| code-yeongyu/oh-my-openagent:programming | exec-remote (scripts/go/new-project.ts:8); exec-remote (scripts/python/new-project.ts:6); exec-remote (scripts/python/new-project.ts:7) | `2faeda01ea` |
| code-yeongyu/oh-my-openagent:ultimate-browsing | inj-secret-exfil (references/insane-search/jina.md:66) | `2faeda01ea` |
| coreyhaines31/marketingskills:directory-submissions | exfil-sink (references/submission-tracker-template.csv:158) | `96798cf387` |
| coreyhaines31/marketingskills:lead-magnets | inj-override (evals/evals.json:100); inj-override (references/content-to-skill-corpus-design.md:42) | `96798cf387` |
| davila7/claude-code-templates:claude-code-guide | inj-override (SKILL.md:56) | `21be197f10` |
| davila7/claude-code-templates:owasp-security | inj-override (SKILL.md:709); inj-override (examples/prompt-injection.txt:18); inj-override (examples/prompt-injection.txt:22) | `21be197f10` |
| garrytan/gstack:benchmark-models | cred-paths (SKILL.md.tmpl:94) | `6f7488a70f` |
| garrytan/gstack:browse | inj-override (src/cli.ts:1299); exfil-sink (src/content-security.ts:325); exfil-sink (src/content-security.ts:327) | `6f7488a70f` |
| garrytan/gstack:careful | destructive (SKILL.md.tmpl:67); exec-remote (SKILL.md.tmpl:69); destructive (bin/check-careful.sh:36) | `6f7488a70f` |
| garrytan/gstack:gstack | exec-remote (.github/docker/Dockerfile.ci:102); cred-paths (.github/scripts/dia-gui-readiness.c:76); cred-paths (.github/scripts/qualify-dia-macos.ts:1014) | `6f7488a70f` |
| garrytan/gstack:gstack-upgrade | exec-remote (SKILL.md.tmpl:178) | `6f7488a70f` |
| heygen-com/hyperframes:frost-sequence-camera-orbit | exec-obfuscated (assets/frost.js:1063) | `618c486734` |
| nanocoai/nanoclaw:add-cursor | secret-material (payload/container/agent-runner/src/providers/cursor.gateway-proxy.test.ts:67); inj-secret-exfil (payload/container/agent-runner/src/providers/cursor.gateway-proxy.test.ts:587) | `bdfb2f1df7` |
| nanocoai/nanoclaw:add-dashboard | inj-secret-exfil (SKILL.md:87) | `bdfb2f1df7` |
| nanocoai/nanoclaw:add-iron-proxy | exec-remote (scripts/install-claude.sh:10); exec-remote (scripts/install-claude.sh:34) | `bdfb2f1df7` |
| nanocoai/nanoclaw:add-onecli | exec-remote (scripts/install-claude.sh:11); exec-remote (scripts/install-claude.sh:32); exec-remote (scripts/register-claude-token.sh:30) | `bdfb2f1df7` |
| nanocoai/nanoclaw:add-teams | exfil-sink (SKILL.md:111) | `bdfb2f1df7` |
| nanocoai/nanoclaw:add-telegram | exfil-sink (SKILL.md:138); exfil-sink (SKILL.md:176) | `bdfb2f1df7` |
| nexu-io/open-design:docs-page | exec-remote (example.html:83) | `07a86b1041` |
| openai/skills:cloudflare-deploy | exfil-sink (references/pages-functions/patterns.md:14) | `49f948faa9` |
| openai/skills:screenshot | exec-obfuscated (scripts/take_screenshot.py:27) | `49f948faa9` |
| sickn33/agentic-awesome-skills:007 | inj-override (references/ai-agent-security.md:20); inj-roleplay (references/ai-agent-security.md:20); inj-override (references/ai-agent-security.md:412) | `828257c303` |
| sickn33/agentic-awesome-skills:2slides-ppt-generator | inj-secret-exfil (SKILL.md:37) | `828257c303` |
| sickn33/agentic-awesome-skills:agent-evals | inj-override (SKILL.md:163); inj-roleplay (SKILL.md:164); inj-override (SKILL.md:267) | `828257c303` |
| sickn33/agentic-awesome-skills:agent-evaluation | inj-override (references/architecture-sketches.md:392) | `828257c303` |
| sno-ai/sno-station-skills:pl | cred-paths (scripts/exec-trust.t:89) | `1c92b0ff89` |
| sno-ai/sno-station-skills:rem-reflect | persistence (scripts/journey-ops.test.ts:2); persistence (scripts/journey-ops.test.ts:83); persistence (scripts/journey-ops.test.ts:84) | `1c92b0ff89` |
| thedotmack/claude-mem:Agent Cost Report | cred-paths (scripts/tests/test_render.py:168) | `989a98a2fb` |
| thedotmack/claude-mem:do | no-skill-md (:0); symlink (SKILL.md:0) | `989a98a2fb` |
| thedotmack/claude-mem:mode-creator | exfil-sink (scripts/configure-telegram.mjs:108) | `989a98a2fb` |
| thedotmack/claude-mem:openclaw | exec-remote (install.sh:419); exec-remote (install.sh:422); exec-remote (install.sh:479) | `989a98a2fb` |
| thedotmack/claude-mem:request-progress | cred-paths (scripts/request-groups.mjs:3216); cred-paths (scripts/request-groups.mjs:3224); exfil-sink (scripts/request-groups.mjs:3318) | `989a98a2fb` |
| titanwings/distilly:distilly | cred-paths (tools/dingtalk_auto_collector.py:498); cred-paths (tools/feishu_browser.py:38) | `0afc45c29c` |
