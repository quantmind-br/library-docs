---
title: Migrate to Warp from Windows Terminal | Warp
url: https://docs.warp.dev/getting-started/migrate-to-warp/migrate-to-warp-from-windows-terminal
source: sitemap
fetched_at: 2026-04-29T15:02:08.20178441-03:00
rendered_js: false
word_count: 530
summary: This document provides instructions for migrating terminal configurations, settings, and workflows from Windows Terminal to the Warp terminal application.
tags:
    - migration
    - windows-terminal
    - warp-terminal
    - configuration
    - settings-management
    - setup-guide
category: guide
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp on Windows covers everything you use Windows Terminal for today — profiles, PowerShell, color schemes, keybindings — with Agent Mode and blocks on top. This page walks through the migration.

## What transfers automatically

Warp doesn't ship a Windows Terminal importer, but it can do most of the work for you agentically. Windows Terminal stores its settings in a single JSON file at `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`.

## Use Warp's agent to migrate your settings (recommended)

The fastest way to bring over your Windows Terminal setup is to ask Warp's agent to translate `settings.json` directly. Warp ships a [`settings.toml` file](https://docs.warp.dev/terminal/settings) and a bundled `modify-settings` skill that lets the agent read your existing config and write equivalent values into Warp's settings, including translating your color schemes into a Warp [[089-terminal-appearance-custom-themes|custom theme]].

1. Paste a prompt like:

   > Read my Windows Terminal `settings.json` at `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json` and port the active profile and color scheme into my Warp `settings.toml` using the `modify-settings` skill. Create a matching custom theme. Show me a diff before applying.

2. Review the proposed diff and approve. Warp hot-reloads `settings.toml`.

## What to reconfigure manually

### Default shell

Warp on Windows supports PowerShell (`pwsh` and `powershell.exe`), Command Prompt (`cmd`), bash, zsh, and fish. Warp auto-detects your login shell; to override, go to **Settings** → **Features** → **Session** and pick a shell from **Startup shell for new sessions**.

If you use PowerShell modules or a custom `$PROFILE`, Warp loads them the same way Windows Terminal does.

### Profiles

Windows Terminal uses profiles to group shell, theme, starting directory, and font together. Warp doesn't have a single profile concept; instead, match each dimension separately:

| Profile Setting | Warp Location |
|---|---|
| Shell | **Settings** → **Features** → **Session** |
| Starting directory | **Settings** → **Features** → **Session** → Working directory |
| Font family, size | **Settings** → **Appearance** → **Text, fonts, & cursor** |
| Color scheme | **Settings** → **Appearance** → **Themes** (create a [[089-terminal-appearance-custom-themes|custom theme]]) |
| Reusable layouts | [[127-terminal-windows-tab-configs|Tab configs]] for each workflow |

### Color scheme

Windows Terminal's `schemes` array defines foreground, background, cursor, and ANSI colors. To match an existing scheme:

1. Copy the color values from the scheme you use in your `settings.json`.
2. Open **Settings** → **Appearance** → **Themes** in Warp and either pick a preset that matches or [[089-terminal-appearance-custom-themes|create a custom theme]].

### Keybindings

Warp's [[016-getting-started-keyboard-shortcuts|default keyboard shortcuts]] cover most Windows Terminal bindings. For custom bindings from `settings.json`'s `actions` array, add them in **Settings** → **Keyboard shortcuts**.

### Prompt

If you use `oh-my-posh` or a custom PowerShell prompt, it continues to work in Warp. To choose between Warp's native prompt and your existing shell prompt, go to **Settings** → **Appearance** → **Prompt**. See [[257-terminal-settings-all-settings|prompt]].

## Warp-native equivalents

| Windows Terminal Feature | Warp Equivalent |
|---|---|
| Profiles | Separate settings: shell, theme, [[127-terminal-windows-tab-configs|tab configs]] |
| Color schemes | [[089-terminal-appearance-custom-themes|Custom themes]] |
| `oh-my-posh` prompts | Work natively (same `$PROFILE` loading) |
| Split panes | [[125-terminal-windows-split-panes|Split panes]] |
| Tabs | [[127-terminal-windows-tabs|Tabs]] |

Beyond Windows Terminal's feature set, Warp adds [[199-agent-platform-warp-agents-warp-agents|Agent Mode]], [[093-terminal-blocks-block-basics|blocks]], and [[144-knowledge-and-collaboration-warp-drive|Warp Drive]]. See [[015-getting-started-installation-and-setup|Warp for Windows installation]] if you haven't installed yet.

#migration-guide #windows-terminal #warp-settings