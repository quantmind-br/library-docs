# ForgeCode Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://forgecode.dev/sitemap.xml |
| **Generated** | 2026-03-29 |
| **Total Documents** | 157 |
| **Strategy** | sitemap |
| **Categories** | 18 |

---

## Document Index

### 1. Introduction & Overview (001-002)
*ForgeCode landing page and documentation hub*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-index.md` | ForgeCode | Terminal-based coding harness with AI models, multi-agent architecture, and model selection | terminal-integration, ai-coding, codebase-understanding, multi-agent |
| 002 | `002-docs.md` | ForgeCode | Step-by-step installation and setup guide for ForgeCode CLI | cli-tool, ai-integration, zsh-plugin, terminal-setup |

### 2. Getting Started (003-004)
*Quick start and dependency installation*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 003 | `003-docs-quickstart.md` | ForgeCode | Quickstart guide for ForgeCode: auth, project analysis, code generation, Git ops, debugging | quickstart, project-analysis, code-generation, git-integration |
| 004 | `004-docs-fd-fzf-installation.md` | ForgeCode | Installing zsh dependencies: zsh-syntax-highlighting, fd, fzf per platform | zsh, installation, dependencies, syntax-highlighting, fd, fzf |

### 3. Configuration (005-011)
*forge.yaml settings, environment variables, providers, models, rules*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 005 | `005-docs-forge-configuration.md` | ForgeCode | Root-level forge.yaml config: request management, model params, system settings | configuration, forge-yaml, model-parameters, request-management |
| 006 | `006-docs-environment-configuration.md` | ForgeCode | Environment variables and .env files for API keys, retry, HTTP, tool config | environment-variables, api-keys, http-settings, retry-configuration |
| 007 | `007-docs-custom-providers.md` | ForgeCode | Configuring AI providers: setup, credentials, switching between OpenAI/Anthropic/OpenRouter | ai-provider-configuration, credential-management, provider-login, api-keys |
| 008 | `008-docs-model-selection-guide.md` | ForgeCode | Switching between AI models, trade-offs, and best practices for model choice | model-switching, ai-development, model-selection, development-workflow |
| 009 | `009-docs-error-handling.md` | ForgeCode | Automatic retry with exponential backoff for tool call parsing errors | error-handling, retry-mechanism, exponential-backoff, tool-call-parsing |
| 010 | `010-docs-custom-rules.md` | ForgeCode | Configuring project guidelines via AGENTS.md file in project root | project-guidelines, ai-agents, configuration, development-standards |
| 011 | `011-docs-custom-rules-guide.md` | ForgeCode | Creating project-specific guidelines through AGENTS.md for team coding standards | ai-coding, project-guidelines, development-standards, custom-rules |

### 4. Agent System (012-018)
*Agent configuration, custom agents, delegation, selection, and workflows*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 012 | `012-docs-agent-configuration.md` | ForgeCode | Configuring AI agents: temperature, context compaction, visibility, troubleshooting | agent-configuration, temperature-settings, context-compaction, forge-yaml |
| 013 | `013-docs-agent-definition-guide.md` | ForgeCode | Creating custom AI agents with markdown files: setup, config, tool integration | ai-agents, custom-agents, yaml-configuration, agent-definition |
| 014 | `014-docs-agent-delegation.md` | ForgeCode | Orchestrator agents calling specialist agents as tools via automatic discovery | agent-delegation, tool-usage, orchestrator, specialist-agents |
| 015 | `015-docs-agent-selection-guide.md` | ForgeCode | Selecting agents: built-in Forge, Muse, Sage optimized for different tasks | agent-selection, built-in-agents, workflow-optimization |
| 016 | `016-docs-operating-agents.md` | ForgeCode | Different specialized agents in ForgeCode and when to use each | agent-selection, ai-development, workflow, code-assistance |
| 017 | `017-docs-plan-and-act-guide.md` | ForgeCode | Multi-agent workflow: Muse for planning + Forge for implementation | ai-coding-tools, development-workflow, muse-agent, planning-first |
| 018 | `018-docs-forge-services.md` | ForgeCode | ForgeCode Services: context engine, tool guardrails, skill engine runtime | forgecode-services, runtime-layer, context-engine, skill-engine |

### 5. Features & Capabilities (019-025)
*Auto-complete, file tagging, context compaction, sandbox, skills, custom commands*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 019 | `019-docs-auto-complete.md` | ForgeCode | Auto-complete: file completion, command history, shell navigation | autocomplete, file-completion, command-history, keyboard-shortcuts |
| 020 | `020-docs-file-tagging.md` | ForgeCode | File tagging with @ references for files, directories, images in prompts | file-tagging, prompt-context, code-reference, file-attachments |
| 021 | `021-docs-context-compaction.md` | ForgeCode | Automatic context compaction to extend conversations beyond token limits | context-compaction, token-management, automatic-summation |
| 022 | `022-docs-sandbox-feature.md` | ForgeCode | Isolated dev environments using Git worktrees for parallel agent work | sandbox, git-worktrees, isolation, parallel-development |
| 023 | `023-docs-skills.md` | ForgeCode | Reusable workflow skills via SKILL.md files in .forge/skills directory | skills, workflows, reusable-tasks, skill-md, automation |
| 024 | `024-docs-custom-commands.md` | ForgeCode | Custom commands via Markdown files with YAML frontmatter | custom-commands, cli, workflow-automation, markdown |
| 025 | `025-docs-ignoring-files.md` | ForgeCode | File ignoring with .gitignore/.ignore patterns and precedence rules | file-ignoring, gitignore, ignore-patterns, file-visibility |

### 6. Integrations (026-029)
*MCP, VS Code, ZSH, piping*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 026 | `026-docs-mcp-integration.md` | ForgeCode | MCP integration: connecting agents to external tools, APIs, services | mcp, api-integration, external-tools, agent-configuration |
| 027 | `027-docs-vscode-extension.md` | ForgeCode | VS Code extension for code references and session launching | vscode-extension, code-reference, keyboard-shortcuts, terminal-integration |
| 028 | `028-docs-zsh-support.md` | ForgeCode | Interactive ZSH mode: colon sentinel, agent selection, file tagging | zsh-integration, ai-prompts, command-sentinel, conversation-management |
| 029 | `029-docs-piping-guide.md` | ForgeCode | Piping command output and file content via stdin to ForgeCode | stdin, piping, input-methods, command-line, data-pipeline |

### 7. Reference (030-034)
*CLI reference, commands, tools, shortcuts, shell commands*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 030 | `030-docs-cli-reference.md` | ForgeCode | Complete CLI reference: all commands, flags, interactive and programmatic usage | cli-reference, command-line, configuration, conversations |
| 031 | `031-docs-commands.md` | ForgeCode | Built-in commands documentation: usage, parameters, when to use each | cli-commands, command-reference, ai-tools |
| 032 | `032-docs-tools-reference.md` | ForgeCode | Built-in tools for AI agents: file operations, data processing, communication | ai-agents, file-operations, data-processing, tool-reference |
| 033 | `033-docs-shortcuts.md` | ForgeCode | ZSH keyboard shortcuts: movement, deletion, history, utility | zsh, keyboard-shortcuts, line-editor, terminal |
| 034 | `034-docs-shell-commands.md` | ForgeCode | Executing native shell commands with ! prefix in ForgeCode | shell-commands, command-execution, shell-compatibility |

### 8. Security (035)
*Security model and features*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 035 | `035-docs-security-features.md` | ForgeCode | Security model: restricted shell mode, operational safeguards | security-model, restricted-shell, rbash, operational-security |

### 9. Troubleshooting (036-039)
*npm issues, Windows errors, logging, uninstallation*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 036 | `036-docs-npm-troubleshooting.md` | ForgeCode | Fixing Node.js/npm issues: permissions, PATH, cross-platform | nodejs, npm, troubleshooting, installation, permission-errors |
| 037 | `037-docs-windows-troubleshooting.md` | ForgeCode | Resolving vcruntime140.dll errors by installing Visual C++ Redistributable | windows, dll-error, vcruntime140, visual-cpp, troubleshooting |
| 038 | `038-docs-logging.md` | ForgeCode | JSON-formatted logs: locate, view, filter, analyze with jq | json-logs, troubleshooting, log-analysis, log-filtering, jq-parsing |
| 039 | `039-docs-uninstallation.md` | ForgeCode | Complete uninstall: app, config files, project-specific settings | uninstall, configuration, removal, cleanup |

### 10. Blog - Guides & Best Practices (040-042)
*AI pair programming lessons, architectural constraints, agent landscape*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 040 | `040-blog-ai-agent-best-practices.md` | AI Agent Best Practices: 12 Lessons | 12 lessons from 6 months of AI pair programming: planning, prompts, context | ai-pair-programming, prompt-engineering, code-review, context-management |
| 041 | `041-blog-simple-is-not-easy.md` | Simple Over Easy | Applying Rich Hickey's principles to constrain AI code generation | ai-code-generation, simple-made-easy, architectural-constraints |
| 042 | `042-blog-coding-agents-showdown.md` | Coding Agents Showdown | VSCode forks vs IDE extensions vs CLI agents comparison | vscode-forks, ide-extensions, cli-agents, development-workflows |

### 11. Blog - Model Comparisons (043-051)
*AI model reviews and head-to-head coding comparisons*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 043 | `043-blog-claude-4-initial-impressions-anthropic-ai-coding-breakthrough.md` | Claude 4 Initial Impressions | Claude 4 review: 72.7% SWE-bench, real-world coding capabilities | claude-4, benchmarking, model-comparison, real-world-testing |
| 044 | `044-blog-claude-4-opus-vs-grok-4-comparison-full.md` | Claude 4 Opus vs Grok 4 | Rust coding comparison: speed, cost, accuracy trade-offs | grok-4, claude-4-opus, rust-coding, bug-detection |
| 045 | `045-blog-claude-sonnet-4-vs-gemini-2-5-pro-preview-coding-comparison.md` | Claude Sonnet 4 vs Gemini 2.5 Pro | Speed, cost, instruction adherence comparison for coding | claude-sonnet, gemini-pro, cost-efficiency, execution-speed |
| 046 | `046-blog-deepseek-r1-0528-coding-experience-review.md` | DeepSeek-R1-0528 Review | Open-source reasoning model: capabilities and latency challenges | deepseek-r1, reasoning-model, latency-issues, mixture-of-experts |
| 047 | `047-blog-grok-4-initial-impression.md` | Grok 4 Initial Impressions | xAI's Grok 4: specs, benchmarks, pricing, vs other models | grok-4, benchmarking, llm, xai |
| 048 | `048-blog-kimi-k2-vs-grok-4-comparison-full.md` | Kimi K2 vs Grok 4 | Bug fixing, features, refactoring in Next.js app | kimi-k2, grok-4, nextjs, real-world-testing |
| 049 | `049-blog-kimi-k2-vs-qwen-3-coder-coding-comparison.md` | Kimi K2 vs Qwen-3 Coder | 13 Rust tasks + 2 Frontend refactors comparison | kimi-k2, qwen-3-coder, rust-development, react-frontend |
| 050 | `050-blog-kimi-k2-vs-sonnet-4-vs-gemini-2.5-pro.md` | Sonnet 4 vs Kimi K2 vs Gemini 2.5 Pro | Three-model comparison on Next.js with Velt SDK | sonnet-4, kimi-k2, gemini-2.5-pro, nextjs, bug-fixing |
| 051 | `051-blog-index-vs-no-index-ai-code-agents.md` | Indexed vs Non-Indexed Agents | Apollo 11 code benchmark: indexing vs no-indexing performance | code-indexing, apollo-guidance-computer, vector-search |

### 12. Blog - MCP & Security (052-054)
*MCP spec updates and security vulnerability analysis*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 052 | `052-blog-mcp-spec-updates.md` | MCP 2025-06-18 Spec Update | OAuth 2.0, token binding, auth requirements for MCP | mcp, oauth2, security, authentication, token-binding |
| 053 | `053-blog-prevent-attacks-on-mcp.md` | MCP Security Crisis (Part 1) | Tool description injection, auth weaknesses, supply chain risks | mcp-security, prompt-injection, supply-chain-attacks |
| 054 | `054-blog-prevent-attacks-on-mcp-part2.md` | MCP Security Prevention (Part 2) | Prevention strategies based on OWASP and NIST frameworks | ai-security, prompt-injection, owasp-top-10, credential-security |

### 13. Blog - Benchmarks & Performance (055-056)
*TermBench optimization and agent reliability improvements*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 055 | `055-blog-benchmarks-dont-matter.md` | Benchmarks Don't Matter (Part 1) | 78.4% SOTA on TermBench 2.0: seven failure modes and fixes | benchmark-optimization, tool-usage, non-interactive-mode, term-bench |
| 056 | `056-blog-gpt-5-4-agent-improvements.md` | Benchmarks Don't Matter (Part 2) | 81.8% TermBench 2.0 with GPT 5.4 and Opus 4.6 | agent-runtime, schema-optimization, verification-enforcement |

### 14. Blog - Product & Company (057-062)
*Release announcements, incidents, pricing, and tutorials*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 057 | `057-blog-forge-v0.98.0-release-article.md` | ForgeCode v0.98.0 Release | Browser auth, safety limits, enhanced file operations | browser-authentication, safety-limits, replace-all |
| 058 | `058-blog-forge-v0106-release.md` | ForgeCode v0.106.0 Release | Plan progress tracking, VS Code extension improvements | progress-tracking, vs-code-extension, reliability |
| 059 | `059-blog-graduating-from-early-access-new-pricing-tiers-available.md` | New Pricing Tiers | Free, Pro, Max plans based on early access results | pricing-structure, early-access, subscription-tiers |
| 060 | `060-blog-forge-incident-12-july-2025-rca-2.md` | July 12 RCA | Context compaction caused quality degradation, rollback and fixes | quality-control, conversation-context, cost-optimization, feature-rollback |
| 061 | `061-blog-gcp-cloudflare-anthropic-outage.md` | GCP/Cloudflare Outage | IAM failure cascading across Google Cloud, Cloudflare, Anthropic | cloud-outage, iam-authentication, service-failure, dependency-cascade |
| 062 | `062-blog-use-novita-ai-api-in-forgecode.md` | Novita AI Quick Guide | Integrating Novita as AI provider in ForgeCode | novita-ai, api-integration, coding-models, terminal-workflow |

### 15. Blog - Index & Meta (063-066)
*Blog index, archive, authors, and tags overview*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 063 | `063-blog.md` | Blog Index | Collection of blog posts on AI coding, models, benchmarks | ai-coding-agents, model-comparison, benchmarks |
| 064 | `064-blog-archive.md` | Blog Archive | Archive of blog posts | forgecode, termbench, accuracy, ranking |
| 065 | `065-blog-authors.md` | Blog Authors | Authors page | cookie-settings, privacy, consent |
| 066 | `066-blog-tags.md` | Blog Tags | Tags overview page | forgecode, termbench, accuracy, ranking |

### 16. Blog Tags (067-143)
*Tag index pages linking to related blog posts*

| # | File | Keywords |
|---|------|----------|
| 067 | `067-blog-tags-ai-agent.md` | ai-pair-programming, developer-productivity |
| 068 | `068-blog-tags-ai-agents.md` | ai-code-agents, performance-benchmark, indexed-search |
| 069 | `069-blog-tags-ai-coding-assistant.md` | root-cause-analysis, quality-degradation |
| 070 | `070-blog-tags-ai-coding-tools.md` | ai-coding-assistants, vscode-extensions, cli-tools |
| 071 | `071-blog-tags-ai-coding.md` | ai-coding, model-comparison, developer-tools |
| 072 | `072-blog-tags-ai-models.md` | claude-4, swe-bench, developer-review |
| 073 | `073-blog-tags-ai-safety.md` | mcp-security, vulnerability-analysis, ai-security |
| 074 | `074-blog-tags-ai.md` | grok-4, large-language-model, ai-development |
| 075 | `075-blog-tags-agent-harness.md` | benchmarking, gpt-5-4, opus-4-6 |
| 076 | `076-blog-tags-anthropic.md` | claude-4, ai-coding, swe-bench |
| 077 | `077-blog-tags-apollo-11.md` | ai-code-agents, performance-benchmark, indexed-search |
| 078 | `078-blog-tags-architecture.md` | simple-made-easy, architectural-constraints, ai-generated-code |
| 079 | `079-blog-tags-authentication.md` | mcp-security, vulnerability-analysis, authentication-weaknesses |
| 080 | `080-blog-tags-best-practices.md` | mcp-spec, ai-security, structured-output |
| 081 | `081-blog-tags-bug-fixing.md` | ai-models, code-generation, nextjs |
| 082 | `082-blog-tags-claude-4-opus.md` | claude-4, grok-4, performance-comparison |
| 083 | `083-blog-tags-claude-4.md` | claude-4, ai-coding, swe-bench |
| 084 | `084-blog-tags-claude-sonnet-4.md` | ai-models, nextjs, production-code |
| 085 | `085-blog-tags-cli-agents.md` | ai-coding-assistants, vscode, cli-tools |
| 086 | `086-blog-tags-cloud-security.md` | mcp-security, prompt-injection, credential-handling |
| 087 | `087-blog-tags-cloud.md` | google-cloud, iam-failure, cloudflare |
| 088 | `088-blog-tags-coding-benchmarks.md` | benchmark-optimization, model-performance, failure-modes |
| 089 | `089-blog-tags-coding-experience.md` | ai-coding, latency-testing, deepseek-r1 |
| 090 | `090-blog-tags-coding.md` | ai-code-agents, performance-benchmark, indexed-search |
| 091 | `091-blog-tags-cost-analysis.md` | claude-sonnet-4, gemini-2.5-pro, coding-comparison |
| 092 | `092-blog-tags-deep-seek.md` | ai-coding, latency-testing, deepseek-r1 |
| 093 | `093-blog-tags-defense.md` | mcp-security, prompt-injection, credential-security |
| 094 | `094-blog-tags-dev-ops.md` | google-cloud, iam-failure, cloudflare-outage |
| 095 | `095-blog-tags-developer-best-practices.md` | ai-pair-programming, developer-productivity |
| 096 | `096-blog-tags-developer-experience.md` | ai-comparison, nextjs, claude-sonnet, kimi-k2 |
| 097 | `097-blog-tags-developer-productivity.md` | ai-coding-assistants, vscode, ide-extensions |
| 098 | `098-blog-tags-developer-tools.md` | ai-coding, model-comparison, developer-tools |
| 099 | `099-blog-tags-evaluation.md` | benchmark-optimization, model-performance |
| 100 | `100-blog-tags-forge-code.md` | root-cause-analysis, quality-degradation |
| 101 | `101-blog-tags-gemini-2-5-pro.md` | ai-comparison, nextjs, gemini-pro |
| 102 | `102-blog-tags-gemini.md` | benchmarking, gpt-5-4, opus-4-6 |
| 103 | `103-blog-tags-gpt-5-4.md` | benchmarking, gpt-5-4, opus-4-6 |
| 104 | `104-blog-tags-grok-4.md` | kimi-k2, grok-4, coding-performance |
| 105 | `105-blog-tags-growth.md` | cookie-settings, privacy |
| 106 | `106-blog-tags-ide-extensions.md` | ai-coding-assistants, vscode, ide-extensions |
| 107 | `107-blog-tags-incident-analysis.md` | google-cloud, iam-failure, cloudflare |
| 108 | `108-blog-tags-incident.md` | root-cause-analysis, quality-degradation |
| 109 | `109-blog-tags-instruction-adherence.md` | claude-sonnet-4, gemini-2-5-pro |
| 110 | `110-blog-tags-kimi-k-2-5.md` | novita-ai, forgecode, api-integration |
| 111 | `111-blog-tags-kimi-k-2.md` | kimi-k2, grok-4, coding-performance |
| 112 | `112-blog-tags-launch.md` | cookie-settings, privacy |
| 113 | `113-blog-tags-llm-provider.md` | novita-ai, forgecode, api-integration |
| 114 | `114-blog-tags-llm.md` | grok-4, large-language-model |
| 115 | `115-blog-tags-mcp-spec-updates.md` | mcp-spec, ai-security, structured-output |
| 116 | `116-blog-tags-mcp.md` | mcp-security, vulnerability-assessment, ai-security |
| 117 | `117-blog-tags-model-comparison.md` | ai-models, coding-comparison, model-benchmarking |
| 118 | `118-blog-tags-model-review.md` | grok-4, large-language-model |
| 119 | `119-blog-tags-novita-ai.md` | novita-ai, forgecode, api-integration |
| 120 | `120-blog-tags-opus-4-6.md` | benchmarking, gpt-5-4, reliability |
| 121 | `121-blog-tags-pair-programming.md` | ai-development, pair-programming, best-practices |
| 122 | `122-blog-tags-performance.md` | root-cause-analysis, quality-degradation |
| 123 | `123-blog-tags-product-update.md` | cookie-settings, privacy |
| 124 | `124-blog-tags-productivity.md` | ai-pair-programming, developer-productivity |
| 125 | `125-blog-tags-prompt-injection.md` | mcp-security, ai-security, supply-chain-security |
| 126 | `126-blog-tags-quality-degradation.md` | root-cause-analysis, quality-degradation |
| 127 | `127-blog-tags-qwen-3-coder.md` | kimi-k2, qwen-3-coder, rust-development |
| 128 | `128-blog-tags-rca.md` | root-cause-analysis, quality-degradation |
| 129 | `129-blog-tags-release.md` | forgecode, release-notes, authentication |
| 130 | `130-blog-tags-rust-development.md` | kimi-k2, qwen-3-coder, rust-development |
| 131 | `131-blog-tags-scaling.md` | cookie-settings, privacy |
| 132 | `132-blog-tags-security.md` | mcp-security, vulnerabilities, ai-security |
| 133 | `133-blog-tags-software-engineering.md` | ai-pair-programming, developer-productivity |
| 134 | `134-blog-tags-sre.md` | iam-failure, google-cloud, cloudflare |
| 135 | `135-blog-tags-supply-chain-security.md` | mcp-security, vulnerabilities, supply-chain-risks |
| 136 | `136-blog-tags-swe-bench.md` | claude-4, swe-bench, anthropic |
| 137 | `137-blog-tags-term-bench.md` | benchmarking, performance-optimization, model-evaluation |
| 138 | `138-blog-tags-tool-calling.md` | ai-benchmarking, nextjs, model-comparison |
| 139 | `139-blog-tags-vector-search.md` | ai-code-agents, performance-benchmark, indexed-search |
| 140 | `140-blog-tags-vs-code-forks.md` | ai-coding-assistants, vscode, cli-tools |
| 141 | `141-blog-tags-vulnerabilities.md` | mcp-security, vulnerabilities, ai-security |
| 142 | `142-blog-tags-workflow-optimization.md` | ai-development, best-practices, prompt-engineering |
| 143 | `143-blog-tags-x-ai.md` | grok-4, language-model, ai-benchmarks |

### 17. Releases & Changelog (144-154)
*Release notes sorted newest to oldest*

| # | File | Summary | Keywords |
|---|------|---------|----------|
| 144 | `144-releases.md` | Main releases page (v1.4.0) | release-notes, changelog, bug-fixes |
| 145 | `145-releases-2025-October.md` | v1.2.0 - Agent features, provider integration | changelog, agent-features, performance |
| 146 | `146-releases-2025-September.md` | v0.121.1 - New AI models, ZSH, UI/UX | bug-fixes, feature-updates, zsh-support |
| 147 | `147-releases-2025-August.md` | v0.112.0 - AI agent improvements, providers | release-notes, ai-agents, provider-integration |
| 148 | `148-releases-2025-July.md` | v0.104.2 - Bug fixes, features, docs | changelog, bug-fixes, features, documentation |
| 149 | `149-releases-2025-June.md` | v0.97.1 - Bug fixes, features, maintenance | changelog, release-notes, bug-fixes |
| 150 | `150-releases-2025-May.md` | v0.94.5 - Maintenance release | cookie-settings, privacy |
| 151 | `151-releases-2025-April.md` | v0.79.3 - UI, model selection, file handling | changelog, bug-fixes, feature-updates |
| 152 | `152-releases-2025-March.md` | v0.53.3 - Maintenance release | cookie-settings, privacy |
| 153 | `153-releases-2025-February.md` | v0.25.3 - Maintenance release | cookie-settings, privacy |
| 154 | `154-releases-2025-January.md` | v0.1.2 - CI/CD, database, tool calls | changelog, ci-cd, bug-fixes, feature-updates |

### 18. Legal & Meta (155-157)
*Privacy policy, terms, search*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 155 | `155-privacy.md` | Privacy Policy | Data collection, processing, GDPR, cookies | privacy-policy, data-collection, gdpr-compliance |
| 156 | `156-terms.md` | Terms & Fair Usage | API restrictions, account sharing, acceptable use | fair-usage-policy, api-restrictions, terms-of-service |
| 157 | `157-search.md` | Search | Search page | forgecode, termbench, accuracy, ranking |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Core Docs (product usage)** | 001-039 |
| **Blog Posts (guides & opinions)** | 040-062 |
| **Blog Meta (index, tags)** | 063-143 |
| **Releases (changelog)** | 144-154 |
| **Legal** | 155-157 |

### By Concept

| Concept | Files |
|---------|-------|
| **Agent Configuration** | 012, 013, 014, 015, 016, 017, 018 |
| **MCP & Security** | 026, 035, 052, 053, 054 |
| **Model Comparisons** | 043-051 |
| **Benchmarks & TermBench** | 055, 056 |
| **ZSH & Shell** | 004, 028, 029, 033, 034 |
| **Custom Rules & Skills** | 010, 011, 023, 024 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read **001-002** for introduction and overview
- Complete **003-004** for quick start and setup

### Level 2: Core Configuration
- Configure with **005-011** (forge.yaml, env vars, providers, rules)
- Set up agents with **012-018** (config, custom agents, delegation)

### Level 3: Practical Usage
- Explore features **019-025** (autocomplete, tagging, skills, sandbox)
- Integrate tools **026-029** (MCP, VS Code, ZSH, piping)

### Level 4: Reference & Troubleshooting
- Consult reference docs **030-034** (CLI, commands, tools, shortcuts)
- Troubleshoot with **035-039** (security, npm, Windows, logging)

### Level 5: Blog & Community
- Best practices from **040-042** (AI pair programming, architecture)
- Model comparisons **043-051** for choosing the right model
- Security deep-dives **052-054** (MCP vulnerabilities)
- Changelog **144-154** for version history

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression adapted to the ForgeCode documentation structure.*
