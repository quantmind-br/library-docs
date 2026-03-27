# Pi Coding Agent Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence from setup through advanced extensibility.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://github.com/badlogic/pi-mono/ |
| **Generated** | 2026-03-23 |
| **Total Documents** | 23 |
| **Categories** | Setup & Configuration, Core Features, Concepts & Internals, Extensibility, API & Integration, Contributing |

---

## Document Index

### 1. Setup & Configuration (001-008)
*Essential configuration for getting Pi up and running: settings system, provider auth, model setup, and platform-specific terminal configuration.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-packages-coding-agent-docs-settings.md` | Settings | Comprehensive reference for the Pi configuration system — global and project-specific JSON settings | pi-agent, configuration, json-settings, project-overrides, llm-settings |
| 002 | `002-packages-coding-agent-docs-providers.md` | Providers | Configure and manage authentication for AI providers — subscriptions, API keys, cloud services | authentication, api-keys, oauth, environment-variables, cloud-providers |
| 003 | `003-packages-coding-agent-docs-models.md` | Models | Configure custom AI providers and models via models.json — API compatibility, env vars, model overrides | llm-configuration, custom-models, model-proxies, openai-compatibility |
| 004 | `004-packages-coding-agent-docs-terminal-setup.md` | Terminal setup | Configure terminal emulators for Kitty keyboard protocol — accurate modifier key detection | terminal-configuration, kitty-keyboard-protocol, input-mapping |
| 005 | `005-packages-coding-agent-docs-tmux.md` | Tmux | Configure tmux for extended key reporting — modified Enter key recognition | tmux, terminal-configuration, csi-u, extended-keys |
| 006 | `006-packages-coding-agent-docs-shell-aliases.md` | Shell aliases | Enable shell aliases in Pi by configuring the shell command prefix | shell-aliases, bash-configuration, terminal-settings |
| 007 | `007-packages-coding-agent-docs-windows.md` | Windows | Configure and locate bash shell environment on Windows — Git Bash, WSL, Cygwin | windows-setup, shell-configuration, git-bash, wsl, cygwin |
| 008 | `008-packages-coding-agent-docs-termux.md` | Termux | Install and configure Pi within Termux on Android devices | termux, android, linux-environment, setup-guide |

### 2. Core Features (009-013)
*Day-to-day usage features: keyboard shortcuts, prompt automation, theming, and session management.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 009 | `009-packages-coding-agent-docs-keybindings.md` | Keybindings | Reference for customizing keyboard shortcuts — config file, syntax, available action IDs | keybindings, shortcuts, tui, customization, keyboard-map |
| 010 | `010-packages-coding-agent-docs-prompt-templates.md` | Prompt templates | Create and use Markdown-based prompt templates for workflow automation | prompt-templates, markdown, automation, workflow-optimization |
| 011 | `011-packages-coding-agent-docs-themes.md` | Themes | Create and customize TUI themes via JSON — color tokens, supported formats | tui-customization, theme-engine, json-configuration, color-schemes |
| 012 | `012-packages-coding-agent-docs-tree.md` | Tree | Session history navigation via /tree command — branching trees, state transitions | session-management, tree-navigation, history-tracking, branch-summarization |
| 013 | `013-packages-coding-agent-docs-session.md` | Session | JSONL session file format — entry structure, message types, tree-based conversation storage | jsonl, data-schema, session-management, typescript-types |

### 3. Concepts & Internals (014-015)
*Technical internals: how Pi manages context windows and event streaming.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 014 | `014-packages-coding-agent-docs-compaction.md` | Compaction | Conversation compaction and branch summarization for LLM context window management | llm-context, token-management, session-summarization, compaction-logic |
| 015 | `015-packages-coding-agent-docs-json.md` | Json | JSON event stream mode — output session events as newline-delimited JSON for integration | cli-tool, json-output, event-streaming, developer-integration |

### 4. Extensibility (016-020)
*Extending Pi: building skills, packages, extensions, custom providers, and TUI components.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 016 | `016-packages-coding-agent-docs-skills.md` | Skills | Develop self-contained skill packages that extend agent capabilities | agent-skills, automation, extensibility, skill-development |
| 017 | `017-packages-coding-agent-docs-packages.md` | Packages | Create and manage Pi packages — install via npm, git, or local paths | pi-packages, package-management, extension-development, dependency-management |
| 018 | `018-packages-coding-agent-docs-extensions.md` | Extensions | Build TypeScript extensions — event handling, custom tools, UI integration | typescript, extensions, developer-tools, automation, api-reference |
| 019 | `019-packages-coding-agent-docs-custom-provider.md` | Custom provider | Register/override/unregister custom model providers — API endpoints, auth, OAuth flows | provider-registration, llm-api, oauth-integration, proxy-configuration |
| 020 | `020-packages-coding-agent-docs-tui.md` | Tui | Build custom interactive TUI components with @mariozechner/pi-tui — IME support, overlays | tui, terminal-user-interface, typescript, component-system, ime-support |

### 5. API & Integration (021-022)
*Programmatic access: SDK for embedding Pi and RPC for headless operation.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 021 | `021-packages-coding-agent-docs-sdk.md` | Sdk | Use the Pi SDK to integrate agent capabilities, manage sessions, and stream events programmatically | sdk-documentation, agent-lifecycle, event-streaming, typescript-api |
| 022 | `022-packages-coding-agent-docs-rpc.md` | Rpc | RPC mode for headless operation via JSON-based protocol over stdio | rpc, jsonl, headless-operation, api-protocol, inter-process-communication |

### 6. Contributing (023)
*Developer guidelines for contributing to the Pi codebase.*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 023 | `023-packages-coding-agent-docs-development.md` | Development | Developer setup, reconfiguration, and testing for pi-mono — path resolution, debugging | development-guide, setup-instructions, testing-procedures, debugging |

---

## Quick Reference

### By Topic

| Topic | Files |
|-------|-------|
| **Configuration & Settings** | 001-003, 006 |
| **Terminal & Environment** | 004-005, 007-008 |
| **User Interface** | 009, 011, 020 |
| **Session Management** | 012-014 |
| **Prompt & Workflow** | 010 |
| **Extension Development** | 016-020 |
| **API & Protocol** | 015, 021-022 |
| **Provider Management** | 002-003, 019 |
| **Development** | 023 |

### By Concept

| Concept | Files |
|---------|-------|
| **Authentication & API Keys** | 002, 003, 019 |
| **JSON Configuration** | 001, 003, 011 |
| **TypeScript Development** | 018, 020, 021 |
| **Context Window Management** | 014 |
| **Event Streaming** | 015, 021 |
| **Session Format & History** | 012, 013, 014 |
| **Package Ecosystem** | 016, 017, 018 |
| **Platform-Specific Setup** | 004, 005, 007, 008 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-003** for core configuration: settings system, provider auth, and model setup
- Complete files **004-008** for platform-specific terminal and environment configuration

### Level 2: Core Usage
- Learn keybindings from file **009** for efficient navigation
- Set up prompt templates with file **010** for workflow automation
- Customize appearance with file **011** (themes)

### Level 3: Understanding Sessions
- Explore session navigation with file **012** (tree command)
- Understand session format with file **013** (JSONL structure)
- Learn context management with file **014** (compaction)
- Learn event streaming with file **015** (JSON mode)

### Level 4: Extending Pi
- Build skills with file **016** for agent capability extension
- Create packages with file **017** for distribution
- Develop TypeScript extensions with file **018** for deep integration
- Register custom providers with file **019** for alternative LLM backends
- Build custom TUI components with file **020**

### Level 5: Programmatic Integration
- Use the SDK (file **021**) to embed Pi in applications
- Use RPC mode (file **022**) for headless/automated operation

### Level 6: Contributing
- Follow developer guidelines in file **023** for pi-mono development

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression from setup to advanced extensibility.*
