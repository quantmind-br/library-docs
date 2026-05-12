---
title: Migrate to Warp from Cursor | Warp
url: https://docs.warp.dev/getting-started/migrate-to-warp/migrate-to-warp-from-cursor
source: sitemap
fetched_at: 2026-04-29T15:02:04.431884027-03:00
rendered_js: false
word_count: 461
summary: This document provides guidance on migrating terminal and AI assistant configurations from Cursor to the Warp terminal, including options for running both tools together or fully replacing Cursor with Warp's built-in features.
tags:
    - migration
    - cursor-to-warp
    - terminal-setup
    - agent-mode
    - configuration-sync
    - developer-tools
category: guide
optimized: true
optimized_at: 2026-04-29T20:15:00Z
---
# Migrate to Warp from Cursor

Choose your path: **keep Cursor as your editor** and use Warp for terminal/agent work, or **replace Cursor fully** with Warp's built-in code editor and Agent Mode.

---

## What Transfers Automatically

Warp has no Cursor importer. Cursor is built on VS Code codebase — terminal settings live in `settings.json` under keys like `terminal.integrated.fontFamily` and `terminal.integrated.defaultProfile.*`. Open your user settings with **Command Palette** > **Preferences: Open User Settings (JSON)** to reference while reconfiguring Warp.

---

## Agent-Assisted Migration (Recommended)

The fastest path uses Warp's bundled `modify-settings` skill:

1. In Warp, open a new tab and switch to [[198-agent-platform-warp-agents-capabilities-overview|Agent Mode]] with `⌘+I` (macOS) or `Ctrl+I` (Linux/Windows).
2. Prompt:
   > Read my Cursor `settings.json` (`~/Library/Application Support/Cursor/User/settings.json` on macOS) and port the equivalent terminal settings (font, cursor style, default profile) into my Warp `settings.toml` using the `modify-settings` skill. Show me a diff before applying.
3. Review and approve the diff. Warp hot-reloads `settings.toml` immediately.

Alternatively, configure manually via the Settings UI (steps below).

---

## Manual Configuration

### Terminal Settings

Cursor's terminal settings follow VS Code schema. See [[022-getting-started-migrate-to-warp-migrate-to-warp-from-vs-code-terminal|Migrate to Warp from VS Code terminal]] for step-by-step shell, font, theme, and keybinding setup.

### Agent and AI Settings

Cursor's Composer/Agent features map to Warp concepts:

| Cursor Feature | Warp Equivalent |
|---------------|------------------|
| Composer / Agent | [[198-agent-platform-warp-agents-capabilities-overview|Agent Mode]] |
| `.cursorrules` | [[041-agent-platform-warp-agents-capabilities-overview-rules|Rules]] in Warp Drive, or `AGENTS.md` at repo root. Run `/init` to generate one, or copy `.cursorrules` content directly. |
| MCP servers | [[072-agent-platform-warp-agents-agent-context-mcp|MCP]] (native support) |

### Model Choice

Select a model per conversation using Warp's model selector. See [[039-agent-platform-warp-agents-capabilities-overview-model-choice|model choice]].

### Keybindings

| Action | Warp Shortcut |
|--------|---------------|
| Toggle Agent Mode | `⌘+I` (macOS) or `Ctrl+I` (Linux/Windows) |
| Enter Agent Mode (alternate) | `⌘+Enter` or `Ctrl+Shift+Enter` |

See [[016-getting-started-keyboard-shortcuts|keyboard shortcuts]] for full reference.

---

## Choosing Your Setup

### Option A: Warp Alongside Cursor

Keep Cursor for in-file AI assistance. Use Warp for:

- Long-running commands and background processes
- SSH sessions
- Agent Mode for autonomous coding tasks

### Option B: Replace Cursor with Warp

Warp's built-in [[181-code-code-editor|code editor]] includes:

- Language Server Protocol (LSP) support
- [[178-code-code-editor-file-tree|File tree]]
- [[179-code-code-editor-find-and-replace|Find and replace]]
- [[177-code-code-editor-code-editor-vim-keybindings|Vim keybindings]]
- [[182-code-code-review|Code Review]] panel
- [[144-knowledge-and-collaboration-warp-drive|Warp Drive]] (notebooks, workflows, environment variables)
- [[198-agent-platform-warp-agents-capabilities-overview|Agent Mode]]

---

## Warp-Native Equivalents

| Cursor Feature | Warp Equivalent |
|---------------------|------------------|
| Code editor | [[181-code-code-editor|Built-in code editor]] |
| Composer / Agent | [[198-agent-platform-warp-agents-capabilities-overview|Agent Mode]] |
| `.cursorrules` | [[041-agent-platform-warp-agents-capabilities-overview-rules|Rules]] / `AGENTS.md` |
| Model selection | [[039-agent-platform-warp-agents-capabilities-overview-model-choice|Model selector]] |
| Tab files | [[220-knowledge-and-collaboration-warp-drive-agent-mode-context|Agent Mode context]] |
| MCP servers | [[072-agent-platform-warp-agents-agent-context-mcp|MCP]] |
| Code review | [[182-code-code-review|Code Review panel]] |

For a tour of Warp's development workflow, see [[013-getting-started-coding-in-warp|Coding in Warp]].

#migration-guide #cursor-to-warp #configuration-sync