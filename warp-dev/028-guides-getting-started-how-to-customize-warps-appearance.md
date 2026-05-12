---
title: Customize Warp's Appearance | Guides | Warp
url: https://docs.warp.dev/guides/getting-started/how-to-customize-warps-appearance
source: sitemap
fetched_at: 2026-04-29T15:06:20.85715558-03:00
rendered_js: false
word_count: 221
summary: Configuration guide for Warp terminal themes, input positioning, AI/agent settings, codebase indexing, and team collaboration.
tags:
    - warp-terminal
    - environment-configuration
    - ai-settings
    - productivity-tools
    - terminal-customization
    - team-collaboration
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp is highly customizable — from appearance and keyboard shortcuts to agent behavior and autonomy.

## 1. Changing Themes

Open the Command Palette (`Cmd+P` / `Ctrl+Shift+P`), type "themes", and preview/apply any theme instantly.

## 2. Adjusting Input Placement

Warp's **input bar** has three positions:

| Position | Behavior |
|---|---|
| **Bottom-pinned** | Chat-style; commands flow upward |
| **Scrolling input** | Traditional terminal; input stays near the bottom |
| **Top-pinned** | Input fixed at top; results appear below (Warp-exclusive) |

## 3. Managing AI & Agent Settings

Open **Settings → AI** to control:

- **Model** — e.g., Claude 3.5 for code generation, GPT-4o for planning
- **Agent autonomy** — per-action permissions for reading files, generating diffs, running commands, planning tasks
- **Command whitelist/blocklist** — require confirmation for specific commands

## 4. Indexing Your Codebases

Warp prompts to index your codebase the first time you `cd` into it. Indexing enables faster code navigation, summaries, searches, refactors, and bug fixes. You can also manually re-index a folder from the sidebar anytime.

## 5. Team Collaboration

In the **Teams** tab, invite teammates and share Warp Drive assets (prompts, templates, environment variables), making Warp a shared, contextual workspace.

## 6. Look & Feel

Under **Appearance**, tweak:

- Fonts, app icons, padding, editor density
- VIM mode for command editing
- Custom key bindings
