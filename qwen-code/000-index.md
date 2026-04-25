---
description: Auto-generated documentation index for Qwen Code
generated: 2026-04-09T09:10:00Z
source: https://qwenlm.github.io/qwen-code-docs
total_docs: 74
categories: 13
---

# Qwen Code Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://qwenlm.github.io/qwen-code-docs |
| **Generated** | 2026-04-09T09:10:00Z |
| **Total Documents** | 74 |
| **Strategy** | github_pages |
| **Categories** | 13 |

---

## Document Index

### 1. Introduction & Overview (001-003)
*Start here to understand what Qwen Code is and what it can do.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-qwen-code-docs.md` | Qwen | Introduces Qwen Code, an open-source AI agent for the terminal designed to assist developers in understanding codebases and automating tasks across interactive, headless, IDE, and SDK modes. | ai-agent, terminal, developer-tools, open-source, coding-assistance |
| 002 | `002-qwen-code-docs-en-users-overview.md` | Qwen Code overview | Introduces Qwen Code as an agentic coding tool for the terminal covering installation, basic usage, debugging, navigation, and workflow automation. | agentic-coding, terminal-tool, developer-assistant, code-generation, installation-guide |
| 003 | `003-qwen-code-docs-en-showcase.md` | Showcase | Demonstrates Qwen Code capabilities across tasks — natural language commands for coding, content creation, system management, and more. | quick-start, ai-coding-partner, video-creation, workflow-automation |

### 2. Quick Start & Installation (004-005)
*Get up and running quickly with installation and common workflows.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 004 | `004-qwen-code-docs-en-users-quickstart.md` | Quickstart | Walkthrough of how to install, configure, and use Qwen Code — from basic code generation and debugging to complex Git operations. | quickstart, coding-assistant, ai-programming, cli-tool, installation |
| 005 | `005-qwen-code-docs-en-users-common-workflow.md` | Common workflows | Comprehensive guide detailing workflows for understanding codebases, fixing bugs, refactoring code, and creating pull requests. | qwen-code, workflow-guide, code-analysis, debugging, documentation |

### 3. Configuration & Settings (006-014)
*Configure authentication, model providers, memory, security, and appearance.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 006 | `006-qwen-code-docs-en-users-configuration-settings.md` | Qwen Code Configuration | Comprehensive configuration system explaining settings priority across layers — from defaults to command-line arguments. | configuration, settings-file, api-key, environment-variables, setup-guide |
| 007 | `007-qwen-code-docs-en-users-configuration-auth.md` | Authentication | Three authentication methods: OAuth, Alibaba Cloud Coding Plan, and API Key — with guidance on configuring model providers. | authentication, api-key, model-providers, settings-configuration, setup-guide |
| 008 | `008-qwen-code-docs-en-users-configuration-model-providers.md` | Model Providers | Configure multiple AI model providers using settings.json modelProviders — covers OpenAI, Anthropic, Gemini, and self-hosted models. | qwen-code, model-providers, ai-configuration, api-setup, llm-integration |
| 009 | `009-qwen-code-docs-en-users-configuration-memory.md` | Memory | Configuration options for memory management and model providers. | user-guide, configuration, settings, memory, model-providers |
| 010 | `010-qwen-code-docs-en-users-configuration-qwen-ignore.md` | Ignoring Files | The .qwenignore feature for excluding paths and files from operations, similar to .gitignore. | qwen-code, ignore-file, git-ignore, path-exclusion, glob-patterns |
| 011 | `011-qwen-code-docs-en-users-configuration-themes.md` | Themes | Customize appearance with built-in themes or create custom color schemes via configuration files. | theme-customization, color-schemes, settings-configuration, cli-usage |
| 012 | `012-qwen-code-docs-en-users-configuration-trusted-folders.md` | Trusted Folders | Security feature controlling which project folders can use full Qwen Code capabilities via explicit trust approval. | security-feature, trusted-folders, code-safety, workspace-control |
| 013 | `013-qwen-code-docs-en-users-features-approval-mode.md` | Approval Mode | Four permission modes — Plan, Default, Auto-Edit, and YOLO — controlling AI interaction levels with code and system resources. | permission-modes, ai-coding-control, code-safety, development-workflow |
| 014 | `014-qwen-code-docs-en-users-features-checkpointing.md` | Checkpointing | Automatically saves project states before AI file modifications; revert changes with /restore command. | checkpointing, version-control, state-management, ai-safety, revert |

### 4. Features & Capabilities (015-023)
*Explore Qwen Code's core features: commands, skills, subagents, MCP, LSP, and more.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 015 | `015-qwen-code-docs-en-users-features-commands.md` | Commands | Comprehensive reference for all commands — session management, slash commands, @ file injection, ! shell commands, and custom shortcuts. | qwen-code, command-reference, slash-commands, file-injection, shell-execution |
| 016 | `016-qwen-code-docs-en-users-features-skills.md` | Agent Skills | Create, manage, and utilize Agent Skills — Skill directory structure, SKILL.md file writing, and best practices for model invocation. | qwen-code, agent-skills, skill-creation, model-extension, project-workflow |
| 017 | `017-qwen-code-docs-en-users-features-sub-agents.md` | Subagents | Specialized AI assistants for delegating focused tasks with specific prompts and tools; managed via CLI. | subagents, ai-assistants, task-delegation, agent-configuration, development-workflow |
| 018 | `018-qwen-code-docs-en-users-features-mcp.md` | Connect Qwen Code to tools via MCP | Model Context Protocol (MCP) for connecting to external tools and data sources — configuration via settings.json and CLI. | mcp, qwen-code, tool-integration, configuration, developer-guide |
| 019 | `019-qwen-code-docs-en-users-features-lsp.md` | Language Server Protocol (LSP) Support | LSP support for advanced code intelligence — find references, diagnostics, configuration across supported languages. | lsp-support, code-intelligence, language-server, developer-tools |
| 020 | `020-qwen-code-docs-en-users-features-headless.md` | Headless Mode | Use Qwen Code in headless mode for scripting and automation — input methods, output formats (text, JSON, stream-JSON), CLI config. | headless-mode, command-line, automation, output-formats, scripting |
| 021 | `021-qwen-code-docs-en-users-features-sandbox.md` | Sandbox | Sandboxing via macOS Seatbelt and containerization (Docker/Podman) for security and isolation when executing code. | sandboxing, security, macos-seatbelt, docker, podman, configuration |
| 022 | `022-qwen-code-docs-en-users-features-language.md` | Internationalization (i18n) & Language | Multilingual capabilities — manage UI language and desired response language from the AI model. | i18n, l10n, language-settings, ui-localization, configuration |
| 023 | `023-qwen-code-docs-en-users-features-token-caching.md` | Token Caching and Cost Optimization | Automatic API cost optimization through token caching with API key authentication — cost reduction and faster responses. | api-cost-optimization, token-caching, api-key-authentication, usage-stats |

### 5. IDE & Editor Integration (024-029)
*Integrate Qwen Code with VS Code, JetBrains, Zed, GitHub Actions, and other editors.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 024 | `024-qwen-code-docs-en-users-ide-integration-ide-integration.md` | IDE Integration | Integrate Qwen Code with IDEs (primarily VS Code) for context-aware features like native diffing. | ide-integration, vscode-setup, code-assistance, workspace-context, diffing |
| 025 | `025-qwen-code-docs-en-users-ide-integration-ide-companion-spec.md` | IDE Companion Plugin: Interface Specification | Technical specification for building companion plugins integrating Qwen Code's IDE mode into editors beyond VS Code. | plugin-development, ide-integration, mcp-protocol, local-server |
| 026 | `026-qwen-code-docs-en-users-integration-vscode.md` | Visual Studio Code | Qwen Code VS Code extension — native sidebar, auto-accept edits mode, installation, and troubleshooting. | vscode, qwen-code, extension-guide, ide-integration, troubleshooting |
| 027 | `027-qwen-code-docs-en-users-integration-jetbrains.md` | JetBrains IDEs | Integrate Qwen Code into JetBrains IDEs via Agent Client Protocol (ACP) — registry or manual configuration. | jetbrains-ide, ai-assistant, agent-client-protocol, installation-guide |
| 028 | `028-qwen-code-docs-en-users-integration-zed.md` | Zed Editor | Native integration with Zed Editor using Agent Client Protocol (ACP) — registry and manual configuration. | zed-editor, ai-assistant, agent-client-protocol, ide-integration |
| 029 | `029-qwen-code-docs-en-users-integration-github-action.md` | Github Actions: qwen-code-action | GitHub Action integrating Qwen Code for PR reviews, issue triage, on-demand collaboration, and tool extensibility. | github-actions, ai-integration, automation-workflow, qwen-code |

### 6. Extensions (030)
*Install and manage Qwen Code extensions from marketplaces.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 030 | `030-qwen-code-docs-en-users-extension-introduction.md` | Qwen Code Extensions | Manage and utilize extensions — install from Gemini CLI and Claude Code Marketplaces, plus commands for management and updates. | extension-management, cli-commands, cross-platform-compatibility, marketplace |

### 7. Reference & Keyboard Shortcuts (032)
*Quick reference for keyboard shortcuts and key bindings.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 032 | `032-qwen-code-docs-en-users-reference-keyboard-shortcuts.md` | Keyboard Shortcuts | Comprehensive reference for keyboard shortcuts — navigation, input manipulation, suggestion selection, and application controls. | keyboard-shortcuts, qwen-code, user-guide, reference, navigation |

### 8. Troubleshooting & Support (033-035)
*Fix common issues, uninstall, or review terms of service.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 033 | `033-qwen-code-docs-en-users-support-troubleshooting.md` | Troubleshooting | Troubleshooting solutions and debugging tips — authentication errors, configuration file management, and system error codes. | troubleshooting, debugging-tips, authentication-errors, error-codes |
| 034 | `034-qwen-code-docs-en-users-support-Uninstall.md` | Uninstall | Uninstall instructions for both npx and global npm installations. | uninstall, npm-cli, npx, global-installation, cleanup |
| 035 | `035-qwen-code-docs-en-users-support-tos-privacy.md` | Terms of Service and Privacy | Terms of service and privacy policies — varies by authentication method; details data collection and telemetry practices. | terms-of-service, privacy-policy, data-collection, ai-assistant |

### 9. Developer Tools Reference (036-047)
*Detailed reference for all built-in tools available to developers.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 036 | `036-qwen-code-docs-en-developers-tools-introduction.md` | Qwen Code Tools | Overview of built-in tools for interacting with local files, shell commands, and web content with security confirmations. | qwen-code, developer-guide, tool-usage, local-environment |
| 037 | `037-qwen-code-docs-en-developers-tools-file-system.md` | File System Tools | Tools for listing directories, reading/writing files, finding files by pattern, regex search, and modifying text in files. | file-system, developer-guide, read-write, search-tools, local-operations |
| 038 | `038-qwen-code-docs-en-developers-tools-multi-file.md` | Multi File Read (read_many_files) | Read content from multiple files using paths or glob patterns — text concatenation and base64 binary handling. | file-reading, tool-usage, base64, glob-patterns, codebase-context |
| 039 | `039-qwen-code-docs-en-developers-tools-shell.md` | Shell Tool (run_shell_command) | Execute shell commands from Qwen Code — foreground/background execution and interactive session capabilities. | run-shell-command, system-interaction, subprocess-execution, qwen-code |
| 040 | `040-qwen-code-docs-en-developers-tools-todo-write.md` | Todo Write (todo_write) | Manage structured task lists for complex coding sessions within Qwen Code. | developer-guide, tool-usage, task-management, coding-session |
| 041 | `041-qwen-code-docs-en-developers-tools-task.md` | Task Tool (task) | Delegate complex multi-step tasks autonomously to specialized subagents for parallel execution. | qwen-code, task-tool, subagent, autonomous-execution, parallel-tasks |
| 042 | `042-qwen-code-docs-en-developers-tools-exit-plan-mode.md` | Exit Plan Mode (exit_plan_mode) | Request user approval before transitioning from planning mode to active code implementation. | developer-guide, implementation-planning, tool-usage, user-approval |
| 043 | `043-qwen-code-docs-en-developers-tools-web-fetch.md` | Web Fetch (web_fetch) | Fetch content from a URL, convert HTML to markdown, and process with an AI model based on a user-provided prompt. | tool-usage, web-fetching, api-guide, url-processing, ai-model |
| 044 | `044-qwen-code-docs-en-developers-tools-web-search.md` | Web Search (web_search) | Internet searches via DashScope, Tavily, and Google — configure via settings files, env vars, or CLI arguments. | web-search, tool-usage, api-integration, configuration-guide, provider-setup |
| 045 | `045-qwen-code-docs-en-developers-tools-memory.md` | Memory (save_memory) | Store and recall specific facts across coding sessions by appending to a designated context file. | qwen-code, memory-saving, tool-usage, context-management |
| 046 | `046-qwen-code-docs-en-developers-tools-mcp-server.md` | MCP Servers with Qwen Code | Configure MCP servers — architecture, transport mechanisms, and settings.json for successful integration. | mcp-protocol, qwen-code, configuration, cli-integration, tool-discovery |
| 047 | `047-qwen-code-docs-en-developers-tools-sandbox.md` | Sandbox (Developer) | Customize sandboxing environment — build custom Docker images and link local source code for development. | sandbox-customization, dockerfile, local-development, source-linking |

### 10. Developer SDK & Architecture (048-050)
*SDK references for TypeScript and Java, plus architecture overview.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 048 | `048-qwen-code-docs-en-developers-architecture.md` | Architecture Overview | High-level architecture — CLI package, backend Core package, extensible tool system, interaction flow, and configuration. | architecture-overview, cli-design, core-backend, tool-system, interaction-flow |
| 049 | `049-qwen-code-docs-en-developers-sdk-typescript.md` | TypeScript SDK | @qwen-code/sdk — installation, quick start, API docs covering query parameters, timeouts, message handling, and permission modes. | sdk-reference, typescript, programmatic-access, querying-interface, tool-control |
| 050 | `050-qwen-code-docs-en-developers-sdk-java.md` | Java SDK | Qwen Code Java SDK — setup via Maven/Gradle, usage examples, architectural layers, and callback mechanisms for session events. | java-sdk, qwen-code, api-integration, session-management, event-handling |

### 11. Extensions Development (051-053)
*Build, configure, and release your own Qwen Code extensions.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 051 | `051-qwen-code-docs-en-developers-extensions-getting-started-extensions.md` | Getting Started with Extensions | Develop custom extensions — from templates to MCP server tools, custom commands, and QWEN.md persistent context. | qwen-code, extension-development, mcp-server, custom-commands, typescript |
| 052 | `052-qwen-code-docs-en-developers-extensions-extension.md` | Extension Guide | Manage, create, and understand extensions — installation, qwen-extension.json config, command conflict resolution, and variables. | extension-management, qwen-code, cli-commands, configuration-guide, custom-commands |
| 053 | `053-qwen-code-docs-en-developers-extensions-extension-releasing.md` | Extension Releasing | Distribute extensions via Git repository or GitHub Releases — advantages, requirements, and best practices. | extension-release, git-repository, github-releases, distribution-methods |

### 12. Contributing & Development (054-059)
*Contribute to Qwen Code, development workflows, testing, and roadmap.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 054 | `054-qwen-code-docs-en-developers-contributing.md` | How to Contribute | Contributor guide — PR guidelines, development workflow, setup, building, testing, linting, and documentation updates. | contribution-process, pull-request-guidelines, development-workflow, testing-guide |
| 055 | `055-qwen-code-docs-en-developers-development-npm.md` | Package Overview | Monorepo architecture with two packages — responsibilities, release process for stable, preview, and nightly versions. | monorepo-architecture, release-workflow, cli-development, versioning-strategy |
| 056 | `056-qwen-code-docs-en-developers-development-telemetry.md` | OpenTelemetry | Implement and configure OpenTelemetry — direct export to Aliyun, local file writing, log/metric structure. | opentelemetry, qwen-code, observability, telemetry, logging, metrics |
| 057 | `057-qwen-code-docs-en-developers-development-integration-tests.md` | Integration Tests | Run, debug, and understand the integration testing framework — commands, env vars for diagnostics, and test output logging. | integration-testing, e2e-testing, test-runner, diagnostics, testing-framework |
| 058 | `058-qwen-code-docs-en-developers-development-issue-and-pr-automation.md` | Issue & PR Automation | Automated workflows for managing and triaging issues and pull requests — contributor processing guidelines. | automation-workflows, issue-triage, pull-request-lifecycle, github-actions |
| 059 | `059-qwen-code-docs-en-developers-roadmap.md` | Roadmap | Phased overview of evolving product capabilities — completed features, planned enhancements, and functional areas. | product-roadmap, feature-tracking, ai-tooling, capability-matrix |

### 13. Blog & Weekly Updates (060-075)
*Blog posts, feature announcements, tutorials, and weekly release notes.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 060 | `060-qwen-code-docs-en-blog.md` | Blog | Aggregates updates and guides — feature releases, improvements, tutorials on AI coding agent usage. | qwen-code, ai-coding-agent, product-updates, tutorials, development-log |
| 061 | `061-qwen-code-docs-en-blog-thinks-like-a-programmer.md` | Announcing Qwen Code | Introduces Qwen Code — an open-source, autonomous AI programming companion powered by Qwen3-Coder with agentic capabilities. | ai-coding, programmer-companion, agentic-workflow, qwen3-coder, open-source |
| 062 | `062-qwen-code-docs-en-blog-feat-skills-oss-styles.md` | One Sentence: Promotional Video | Generate cinematic promotional demo videos for open-source projects using a single natural language prompt. | ai-video-generation, open-source-promotion, demo-video, developer-tools |
| 063 | `063-qwen-code-docs-en-blog-how-to-use-qwencode-cowork.md` | Cowork Use Cases | Qwen Code Cowork — desktop AI assistant for file organization, batch renaming, disk space management, and automation. | ai-assistant, file-management, automation, open-source, desktop-tools |
| 064 | `064-qwen-code-docs-en-blog-how-to-use-qwencode-insight.md` | Qwen Code Insight | Insight feature analyzes conversation history to generate personalized usage reports with actionable recommendations. | qwen-code, ai-usage-review, personalization, productivity-enhancement, feedback-system |
| 065 | `065-qwen-code-docs-en-blog-channels-weixin-launch-announcement.md` | WeChat Channel Integration | Use Qwen Code for coding within WeChat channels — QR code setup, configuration, testing, and customization. | qwen-code, wechat-integration, ai-coding-assistant, configuration-guide |
| 066 | `066-qwen-code-docs-en-blog-obsidian.md` | Qwen Code + Obsidian | Integrate Qwen Code into Obsidian for knowledge management — plugins, auth, writing polish, image generation, web scraping. | obsidian, qwen-code, ai-agent, knowledge-management, markdown |
| 067 | `067-qwen-code-docs-en-blog-qwencode-coding-plan-guide-build-website.md` | Coding Plan: Build Website | Automate portfolio websites, open-source PR submission, and demo video generation using Qwen Code. | qwen-code, ai-programming, portfolio-website, open-source-contribution |
| 068 | `068-qwen-code-docs-en-blog-qwencode-for-university-students.md` | 10 Use Cases for Students | 10 practical use cases for students — academic tasks, career preparation, and technical workflows. | ai-coding-assistant, student-productivity, academic-tools, workflow-automation |
| 069 | `069-qwen-code-docs-en-blog-weekly-update-2026-02-03.md` | Weekly: LSP, Batch Runner | v0.8.1/v0.8.2 stable, v0.9.0 preview — Extension System, LSP support, batch-runner, UI unification, new languages. | qwen-code, lsp-support, extension-system, batch-testing, software-update |
| 070 | `070-qwen-code-docs-en-blog-weekly-update-2026-02-09.md` | Weekly: Skills GA, Session Export | v0.9.0/v0.9.1 stable — Agent Skills GA, session history export, installation improvements, SDK optimizations. | weekly-update, feature-release, agent-skills, session-export, sdk-optimization |
| 071 | `071-qwen-code-docs-en-blog-weekly-update-2026-03-03.md` | Weekly: Insight, Clipboard, Terminal | v0.10.0/v0.11.0 — Insight analytics, clipboard image support, terminal screenshot generation, bug fixes. | qwen-code, feature-update, analytics, clipboard-images, terminal-capture |
| 072 | `072-qwen-code-docs-en-blog-weekly-update-2026-03-06.md` | Weekly: HTML Export, GIF, GitHub | v0.11.1 — HTML export viewer, streaming terminal GIF, built-in GitHub workflow commands, QoL improvements. | release-notes, software-updates, feature-enhancements, github-automation |
| 073 | `073-qwen-code-docs-en-blog-weekly-update-2026-03-13.md` | Weekly: Hooks, Extensions, VS Code | v0.12.0 — Automated Hooks, proactive AI questioning, enhanced extension/MCP management, VS Code sidebar. | release-notes, qwen-code, new-features, workflow-enhancements |
| 074 | `074-qwen-code-docs-en-blog-weekly-update-2026-03-20.md` | Weekly: Token Limit, JetBrains | Token limit 8K→16K, real-time token usage, JetBrains/Zed integration, Plan Mode comparison, Windows fixes. | qwen-code, ai-assistant, token-limit, editor-integration, feature-release |
| 075 | `075-qwen-code-docs-en-blog-weekly-update-2026-03-27.md` | Weekly: Code Review, Hooks, Arena | v0.13.0 — /review for code review, /btw for side questions, Hooks for automated testing, Arena for multi-model comparison. | qwen-code, ai-developer-tools, new-features, workflow-automation, api-integration |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-005 |
| **Configuration & Settings** | 006-014 |
| **Commands & Shortcuts** | 015, 032 |
| **Skills & Agents** | 016-017 |
| **MCP & Integrations** | 018, 046 |
| **IDE Integration** | 024-029 |
| **Sandbox & Security** | 012-013, 021, 047 |
| **SDK & Architecture** | 048-050 |
| **Extension Development** | 030, 051-053 |
| **Developer Tools** | 036-047 |
| **Contributing** | 054-059 |
| **Troubleshooting** | 033-035 |
| **Blog & Updates** | 060-075 |

### By Concept

| Concept | Files |
|---------|-------|
| **MCP (Model Context Protocol)** | 018, 046 |
| **Subagents & Task Delegation** | 017, 041 |
| **Authentication & Security** | 007, 012-013, 021 |
| **Headless & Automation** | 020, 029 |
| **LSP & Code Intelligence** | 019 |
| **Sandbox & Isolation** | 021, 047 |
| **Token Management** | 023 |
| **Internationalization** | 022 |
| **Checkpointing & Version Control** | 014 |
| **Extension System** | 030, 051-053 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-003** for introduction and overview of Qwen Code
- Complete files **004-005** for quick start installation and common workflows

### Level 2: Core Configuration
- Learn settings from files **006-012** for configuration, auth, models, memory, and security
- Understand permission modes and safety features in files **013-014**

### Level 3: Features & Capabilities
- Explore all core features in files **015-023** — commands, skills, subagents, MCP, LSP, headless, sandbox, i18n, token caching

### Level 4: Integration & Extensions
- Set up IDE integrations in files **024-029**
- Install and use extensions with file **030**
- Reference keyboard shortcuts in file **032**

### Level 5: Developer Reference
- Master all built-in tools from files **036-047**
- Build with SDKs using files **048-050**
- Develop extensions with files **051-053**

### Level 6: Contributing & Community
- Contribute to the project using files **054-059**
- Follow blog updates in files **060-075**

### Level 7: Troubleshooting & Support
- Troubleshoot issues with file **033**
- Review terms of service in file **035**
- Uninstall if needed with file **034**

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression from introduction through advanced topics.*
