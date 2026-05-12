---
title: Migrate to Warp from macOS Terminal | Warp
url: https://docs.warp.dev/getting-started/migrate-to-warp/migrate-to-warp-from-macos-terminal
source: sitemap
fetched_at: 2026-04-29T15:02:07.439621316-03:00
rendered_js: false
word_count: 436
summary: This document provides instructions for migrating terminal preferences and settings from macOS Terminal.app to the Warp terminal emulator, covering both AI-assisted migration and manual configuration methods.
tags:
    - migration-guide
    - macos-terminal
    - terminal-configuration
    - warp-settings
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp gives Terminal.app users everything they already have — shell, theme, font, prompt — plus split panes, tabs, blocks, and Agent Mode for an AI-assisted workflow. This page walks through both an agent-driven migration and the manual GUI steps.

## What transfers automatically

Warp doesn't ship a Terminal.app importer, but it can do most of the work for you agentically. Most Terminal.app users run near-default settings, so the migration usually takes only a few minutes either way.

## Use Warp's agent to migrate your settings (recommended)

The fastest way to bring over a Terminal.app theme is to ask Warp's agent to translate it directly. Warp ships a [`settings.toml` file](https://docs.warp.dev/terminal/settings) and a bundled `modify-settings` skill that lets the agent read your Terminal.app preferences and write equivalent values into Warp's settings, including creating a matching [[089-terminal-appearance-custom-themes|custom theme]].

1. Paste a prompt like:

   > Read my Terminal.app preferences with `defaults read com.apple.Terminal` and port the active profile (theme, font, window size) into my Warp `settings.toml` using the `modify-settings` skill. Create a matching custom theme. Show me a diff before applying.

2. Review the proposed diff and approve. Warp hot-reloads `settings.toml`.

## What to reconfigure manually

### Shell

Warp auto-detects your login shell on first launch. macOS has shipped with `zsh` as the default since Catalina (2019); if you changed your shell with `chsh`, Warp picks that up too.

To change it later, go to **Settings** → **Features** → **Session** and pick a shell from **Startup shell for new sessions**.

### Theme and colors

Terminal.app ships with a handful of profiles (Basic, Pro, Homebrew, Ocean, etc.). Match them in Warp:

1. Open **Settings** → **Appearance** → **Themes**.
2. Pick a preset theme. Warp's built-in library includes many themes similar to Terminal.app's defaults.
3. For exact color matches, [[089-terminal-appearance-custom-themes|create a custom theme]] using the ANSI color values from Terminal.app's **Settings** → **Profiles** → **Text** tab.

### Font

In **Settings** → **Appearance** → **Text, fonts, & cursor**, set the font family and size to match your Terminal.app settings.

### Window size and transparency

Configure in **Settings** → **Appearance** → **Size, opacity, & blurring**. See [[238-terminal-appearance-size-opacity-blurring|size, opacity, and blurring]].

### Prompt

Terminal.app uses whatever prompt your shell's PS1 (or zsh's PROMPT) defines. In Warp, choose:

1. [**Warp prompt**](https://docs.warp.dev/terminal/appearance/prompt#warp-prompt) — Warp's native prompt with drag-and-drop chips for git branch, directory, and more.
2. [**Shell prompt (PS1)**](https://docs.warp.dev/terminal/appearance/prompt#custom-prompt) — keeps your existing shell prompt exactly as it appears in Terminal.app.

## Warp-native equivalents

Beyond matching Terminal.app, Warp adds [[079-agent-platform-warp-agents-interacting-with-agents|Agent Mode]] for natural-language commands, [[093-terminal-blocks-block-basics|blocks]] for structured command output, and [[144-knowledge-and-collaboration-warp-drive|Warp Drive]] for shared workflows.

New to Warp? Start with the [[025-getting-started-quickstart|Warp quickstart]].

#migration-guide #macos-terminal #terminal-configuration #warp-settings