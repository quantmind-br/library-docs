---
title: Migrate to Warp from VS Code terminal | Warp
url: https://docs.warp.dev/getting-started/migrate-to-warp/migrate-to-warp-from-vs-code-terminal
source: sitemap
fetched_at: 2026-04-29T15:02:07.294452613-03:00
rendered_js: false
word_count: 534
summary: This document provides guidance on migrating terminal configurations from VS Code to Warp and outlines options for using Warp either alongside or as a replacement for the VS Code editor.
tags:
    - migration
    - configuration
    - warp-terminal
    - vs-code
    - terminal-setup
    - settings-management
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp lets VS Code users choose their own path: keep VS Code for editing and run Warp as the terminal alongside it, or replace both with Warp's built-in code editor. This page walks through reconfiguring your terminal settings for either path.

## What transfers automatically

Warp doesn't ship a VS Code importer — it's a standalone application, not a VS Code extension — but it can do most of the work for you agentically. Your VS Code terminal settings live in your user `settings.json` under keys like `terminal.integrated.*`.

## Use Warp's agent to migrate your settings (recommended)

The fastest way to bring over your VS Code terminal setup is to ask Warp's agent to translate `settings.json` directly. Warp ships a [`settings.toml` file](https://docs.warp.dev/terminal/settings) and a bundled `modify-settings` skill that lets the agent read your existing config and write equivalent values into Warp's settings.

1. In Warp, open a new tab and switch to [[079-agent-platform-warp-agents-interacting-with-agents|Agent Mode]] with `⌘+I` (macOS) or `Ctrl+I` (Linux/Windows).
2. Paste a prompt like:

   > Read my VS Code `settings.json` (`~/Library/Application Support/Code/User/settings.json` on macOS) and port the equivalent terminal settings (`terminal.integrated.*` keys) into my Warp `settings.toml` using the `modify-settings` skill. Show me a diff before applying.

3. Review the proposed diff and approve. Warp hot-reloads `settings.toml`.

## What to reconfigure manually

### Shell

Warp auto-detects your login shell. To override — for example, to match `terminal.integrated.defaultProfile.*` — go to **Settings** → **Features** → **Session** and pick a shell from **Startup shell for new sessions**.

### Font and cursor

In Warp's **Settings** → **Appearance** → **Text, fonts, & cursor**, set the font family and size to match `terminal.integrated.fontFamily` and `terminal.integrated.fontSize`.

### Theme

VS Code's terminal uses the color scheme from your overall editor theme. In Warp, pick a comparable theme from **Settings** → **Appearance** → **Themes**, or [[089-terminal-appearance-custom-themes|create a custom theme]] that matches your VS Code theme's `terminal.*` color tokens.

### Keybindings

Warp's [[016-getting-started-keyboard-shortcuts|default keyboard shortcuts]] are largely consistent with VS Code terminal shortcuts (splits, new tab, find). For any custom bindings you configured in VS Code, add them in Warp's **Settings** → **Keyboard shortcuts**.

## Choosing your setup

### Use Warp alongside VS Code

Many developers keep VS Code as their editor and use Warp as the terminal they switch to for long-running commands, SSH sessions, or AI-assisted workflows. No changes to VS Code needed — just install Warp and open it when you need [[093-terminal-blocks-block-basics|blocks]], [[079-agent-platform-warp-agents-interacting-with-agents|Agent Mode]], or [[247-terminal-sessions-session-restoration|persistent sessions]].

### Replace VS Code with Warp

Warp includes a built-in [[181-code-code-editor|code editor]] with Language Server Protocol (LSP) support, a [[178-code-code-editor-file-tree|file tree]], [[179-code-code-editor-find-and-replace|find and replace]], and [[177-code-code-editor-code-editor-vim-keybindings|Vim keybindings]]. Combined with [[182-code-code-review|Code Review]], many developers use Warp as their primary editor and drop VS Code entirely.

Open a directory with `warp .` from the command line to start editing.

## Warp-native equivalents

| VS Code Terminal Setting | Warp Equivalent |
|---|---|
| `terminal.integrated.fontFamily` | **Settings** → **Appearance** → **Text, fonts, & cursor** |
| `terminal.integrated.fontSize` | **Settings** → **Appearance** → **Text, fonts, & cursor** |
| Editor color scheme with `terminal.*` colors | [[089-terminal-appearance-custom-themes|Custom theme]] |
| Custom `keybindings.json` | **Settings** → **Keyboard shortcuts** |

For an overview of what Warp adds beyond a terminal, see [[013-getting-started-coding-in-warp|Coding in Warp]].

#migration-guide #vs-code-terminal #terminal-configuration #warp-settings