---
title: Index
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/index.md
source: git
fetched_at: 2026-05-03T09:31:10.31928963-03:00
rendered_js: false
word_count: 295
summary: Central hub for the Pi terminal coding harness — installation, configuration, and extension resources.
tags:
    - coding-agent
    - terminal-tool
    - typescript-extensions
    - cli-utility
    - ai-development
    - development-environment
category: guide
optimized: true
optimized_at: 2026-05-03T12:31:00Z
---
# Pi Documentation

Pi is a minimal terminal coding harness. Designed to stay small at the core while being extended through TypeScript extensions, skills, prompt templates, themes, and pi packages.

## Quick Start

Install pi with npm:

```bash
npm install -g @mariozechner/pi-coding-agent
```

Run it in a project directory:

```bash
pi
```

Authenticate with `/login` for subscription providers, or set an API key (`ANTHROPIC_API_KEY`, etc.) before starting pi.

For the full first-run flow, see [[023-packages-coding-agent-docs-development|Development]].

## Start Here

- [[015-packages-coding-agent-docs-quickstart|Quickstart]] — install, authenticate, and run a first session
- [[105-packages-coding-agent-docs-usage|Using Pi]] — interactive mode, slash commands, context files, and CLI reference
- [[053-packages-coding-agent-docs-providers|Providers]] — subscription and API-key setup for built-in providers
- [[103-packages-coding-agent-docs-settings|Settings]] — global and project settings
- [[099-packages-coding-agent-docs-keybindings|Keybindings]] — default shortcuts and custom keybindings
- [[029-packages-coding-agent-docs-sessions|Sessions]] — session management, branching, and tree navigation
- [[037-packages-coding-agent-docs-compaction|Compaction]] — context compaction and branch summarization

## Customization

- [[025-packages-coding-agent-docs-extensions|Extensions]] — TypeScript modules for tools, commands, events, and custom UI
- [[038-packages-coding-agent-docs-skills|Skills]] — agent skills for reusable on-demand capabilities
- [[028-packages-coding-agent-docs-prompt-templates|Prompt templates]] — reusable prompts that expand from slash commands
- [[031-packages-coding-agent-docs-themes|Themes]] — built-in and custom terminal themes
- [[026-packages-coding-agent-docs-packages|Pi packages]] — bundle and share extensions, skills, prompts, and themes
- [[052-packages-coding-agent-docs-models|Custom models]] — add model entries for supported provider APIs
- [[022-packages-coding-agent-docs-custom-provider|Custom providers]] — implement custom APIs and OAuth flows

## Programmatic Usage

- [[101-packages-coding-agent-docs-sdk|SDK]] — embed pi in Node.js applications
- [[100-packages-coding-agent-docs-rpc|RPC mode]] — integrate over stdin/stdout JSONL
- [[098-packages-coding-agent-docs-json|JSON event stream mode]] — print mode with structured events
- [[104-packages-coding-agent-docs-tui|TUI components]] — build custom terminal UI for extensions

## Reference

- [[102-packages-coding-agent-docs-session-format|Session format]] — JSONL session file format, entry types, and SessionManager API

## Platform Setup

- [[056-packages-coding-agent-docs-windows|Windows]]
- [[030-packages-coding-agent-docs-termux|Termux on Android]]
- [[055-packages-coding-agent-docs-tmux|tmux]]
- [[049-packages-coding-agent-docs-terminal-setup|Terminal setup]]
- [[054-packages-coding-agent-docs-shell-aliases|Shell aliases]]

## Development

- [[023-packages-coding-agent-docs-development|Development]] — local setup, project structure, and debugging

#coding-agent #terminal-tool #ai-development
