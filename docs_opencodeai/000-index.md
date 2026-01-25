---
description: Auto-generated documentation index for OpenCode AI coding agent
generated: 2026-01-25T01:50:00Z
source: https://opencode.ai/sitemap.xml
total_docs: 38
categories: 9
---

# OpenCode Documentation Index

> Organized index for AI agent consumption. Documents follow logical learning sequence.

## Metadata Summary

| Property | Value |
|----------|-------|
| **Source** | https://opencode.ai/sitemap.xml |
| **Generated** | 2026-01-25T01:50:00Z |
| **Total Documents** | 38 |
| **Categories** | Introduction, Release Notes, Interfaces, Configuration, Features, Integrations, API/SDK, Enterprise, Reference |

---

## Document Index

### 1. Introduction & Overview (001-002)
*Core introduction to OpenCode and getting started guides*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 001 | `001-index.md` | The open source AI coding agent | Introduces OpenCode, an open-source AI coding agent supporting multiple LLM providers and editors | ai-coding-assistant, open-source, llm-integration, privacy-focused |
| 002 | `002-docs.md` | Intro | Getting started guide covering installation, configuration with LLM providers, and basic usage | installation-guide, cli-tools, llm-providers, developer-workflows |

### 2. Release Notes (003)
*Version updates and migration guides*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 003 | `003-docs-1-0.md` | Migrating to 1.0 | OpenCode 1.0 release with TUI rewrite using Zig/SolidJS, UX updates, breaking keybinding changes | release-notes, tui, breaking-changes, software-update |

### 3. Interfaces & Usage (004-009)
*Different ways to interact with OpenCode: TUI, CLI, IDE, Web, ACP*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 004 | `004-docs-tui.md` | TUI | Terminal user interface guide: slash commands, file referencing, interface configuration | terminal-interface, slash-commands, keyboard-shortcuts |
| 005 | `005-docs-cli.md` | CLI | CLI reference: commands and flags for agents, sessions, authentication, server operations | cli-commands, agent-management, mcp-server, authentication |
| 006 | `006-docs-ide.md` | IDE | IDE integration for VS Code, Cursor: installation, keyboard shortcuts, troubleshooting | ide-integration, vscode-extension, keyboard-shortcuts |
| 007 | `007-docs-web.md` | Web | Browser-based interface: server setup, network settings, security, session management | web-interface, server-configuration, remote-access |
| 008 | `008-docs-acp.md` | ACP Support | Agent Client Protocol integration for Zed, JetBrains, Neovim | agent-client-protocol, acp-integration, zed-editor, neovim-plugins |
| 009 | `009-docs-keybinds.md` | Keybinds | Default keyboard shortcuts and keybinding configuration | keybindings, keyboard-shortcuts, shortcut-mapping |

### 4. Configuration (010-019)
*Core configuration: providers, models, modes, permissions, rules, formatters, LSP, network, themes*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 010 | `010-docs-config.md` | Config | JSON/JSONC configuration: locations, precedence rules, model/server/UI settings | json-configuration, precedence-rules, server-settings |
| 011 | `011-docs-providers.md` | Providers | Connecting LLM providers: credential management, environment setup | llm-providers, authentication, api-setup |
| 012 | `012-docs-models.md` | Models | LLM model configuration: defaults, options, model variants | llm-configuration, model-selection, model-variants |
| 013 | `013-docs-modes.md` | Modes | Operational modes (build, plan): built-in and custom mode configuration | modes, tool-permissions, ai-behavior, custom-modes |
| 014 | `014-docs-permissions.md` | Permissions | Action permissions: allow/prompt/block tools, pattern matching, wildcards | access-control, security-configuration, wildcard-matching |
| 015 | `015-docs-rules.md` | Rules | Custom instructions via AGENTS.md files, rule precedence, Claude Code compatibility | custom-instructions, agents-md, project-rules |
| 016 | `016-docs-formatters.md` | Formatters | Language-specific formatters: configuration, customization, disabling | code-formatting, auto-formatting, prettier |
| 017 | `017-docs-lsp.md` | LSP Servers | Language Server Protocol integration for codebase feedback | lsp, language-server-protocol, code-analysis |
| 018 | `018-docs-network.md` | Network | Enterprise network: proxies, custom CA certificates | proxy-configuration, enterprise-setup, certificate-management |
| 019 | `019-docs-themes.md` | Themes | Built-in and custom themes, terminal requirements, JSON theme files | theming, terminal-colors, custom-themes |

### 5. Features & Capabilities (020-027)
*Agents, commands, skills, tools, plugins, MCP servers, sharing*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 020 | `020-docs-agents.md` | Agents | Primary and subagents: built-in types, interaction, JSON/Markdown configuration | ai-agents, workflow-automation, llm-orchestration |
| 021 | `021-docs-commands.md` | Commands | Custom commands: Markdown/JSON config, prompt placeholders, shell injection | custom-commands, automation, prompt-templates |
| 022 | `022-docs-skills.md` | Agent Skills | SKILL.md definitions: directory placement, frontmatter, permissions | agent-skills, skill-md, automation |
| 023 | `023-docs-tools.md` | Tools | Built-in and custom tools: functions, execution permissions | llm-tools, permission-management, mcp-servers |
| 024 | `024-docs-custom-tools.md` | Custom Tools | Creating LLM-callable tools: TypeScript helper, Zod validation, scripts | custom-tools, typescript, zod-validation |
| 025 | `025-docs-plugins.md` | Plugins | Plugin development: installation, dependencies, event-driven hooks | plugin-development, javascript, typescript, event-hooks |
| 026 | `026-docs-mcp-servers.md` | MCP servers | Model Context Protocol: local/remote server integration, OAuth | model-context-protocol, mcp-server, oauth-authentication |
| 027 | `027-docs-share.md` | Share | Conversation sharing: manual/automatic modes, unsharing, privacy | collaboration, sharing-mode, privacy-security |

### 6. Integrations (028-029)
*CI/CD platform integrations*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 028 | `028-docs-github.md` | GitHub | GitHub Actions: issue triage, feature implementation, PR automation | github-actions, automation, workflow-integration |
| 029 | `029-docs-gitlab.md` | GitLab | GitLab CI/CD: pipelines, GitLab Duo, issue triage, code generation | gitlab-ci, ai-automation, devops-integration |

### 7. API & SDK (030-031)
*Programmatic access to OpenCode*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 030 | `030-docs-sdk.md` | SDK | @opencode-ai/sdk: type-safe JS/TS client, session management | opencode-sdk, javascript, typescript, api-client |
| 031 | `031-docs-server.md` | Server | Headless HTTP server: OpenAPI 3.1 REST endpoints reference | openapi, rest-api, http-server, api-reference |

### 8. Enterprise & Zen (032-035)
*Enterprise deployment and Zen model gateway*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 032 | `032-docs-enterprise.md` | Enterprise | Enterprise deployment: SSO, AI gateways, data privacy, NPM registry | enterprise-security, sso-integration, data-privacy |
| 033 | `033-enterprise.md` | Enterprise solutions | Security, data privacy, deployment model, code ownership | enterprise-deployment, security, software-licensing |
| 034 | `034-docs-zen.md` | Zen | OpenCode Zen: curated AI gateway, pricing, API endpoints, teams | opencode-zen, ai-models, api-gateway, pricing |
| 035 | `035-zen.md` | Zen Models | Curated AI models for coding: benchmarking, pay-as-you-go pricing | coding-agents, ai-models, benchmarking, llm-hosting |

### 9. Reference & Resources (036-038)
*Ecosystem, brand guidelines, troubleshooting*

| # | File | Title | Summary | Keywords |
|---|------|-------|---------|----------|
| 036 | `036-docs-ecosystem.md` | Ecosystem | Community plugins, projects, agents extending OpenCode | community-projects, ecosystem, extensions, plugins |
| 037 | `037-brand.md` | Brand | Official brand resources and visual assets | brand-guidelines, visual-identity, brand-assets |
| 038 | `038-docs-troubleshooting.md` | Troubleshooting | Debugging: log locations, plugin management, error resolution | troubleshooting, debugging, error-handling, logs |

---

## Quick Reference

### By Topic

| Topic | File Range |
|-------|------------|
| **Getting Started** | 001-002 |
| **User Interfaces** | 004-009 |
| **Configuration** | 010-019 |
| **Agents & Automation** | 020-022 |
| **Tools & Extensions** | 023-027 |
| **CI/CD Integration** | 028-029 |
| **API Access** | 030-031 |
| **Enterprise** | 032-033 |
| **Zen Models** | 034-035 |

### By Concept

| Concept | Files |
|---------|-------|
| **Installation** | 001, 002, 006 |
| **LLM Configuration** | 010, 011, 012, 034 |
| **Permissions & Security** | 014, 018, 032 |
| **Extensibility** | 024, 025, 026 |
| **Keyboard Shortcuts** | 004, 006, 009 |
| **Custom Behavior** | 013, 015, 020, 021, 022 |

---

## Learning Path

### Level 1: Foundation (Start Here)
- Read files **001-002** for introduction and overview
- Understand what OpenCode is and how to install it

### Level 2: Interface Mastery
- Learn the TUI in file **004** for terminal usage
- Explore CLI commands in file **005** for automation
- Set up IDE integration with file **006** for VS Code/Cursor

### Level 3: Configuration
- Master JSON config in file **010**
- Configure LLM providers with files **011-012**
- Understand modes and permissions with files **013-014**

### Level 4: Customization
- Create custom rules with file **015**
- Build agents and commands with files **020-022**
- Develop tools and plugins with files **024-025**

### Level 5: Advanced & Enterprise
- Integrate with CI/CD using files **028-029**
- Use SDK/API with files **030-031**
- Deploy enterprise with files **032-033**
- Use Zen models with files **034-035**

### Level 6: Reference & Support
- Explore ecosystem in file **036**
- Troubleshoot issues with file **038**

---

*This index is auto-generated and optimized for AI agent search. Files are numbered sequentially following a logical learning progression from introduction to advanced topics.*
