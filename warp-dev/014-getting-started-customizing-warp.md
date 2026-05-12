---
title: Customizing Warp | Warp
url: https://docs.warp.dev/getting-started/customizing-warp
source: sitemap
fetched_at: 2026-04-29T15:01:59.614221114-03:00
rendered_js: false
word_count: 564
summary: This document provides an overview of the configuration options available in the Warp terminal, including appearance, layout, input settings, AI agent behavior, and migration tools.
tags:
    - warp-terminal
    - terminal-configuration
    - workspace-customization
    - ai-settings
    - keyboard-shortcuts
    - dev-tools
category: guide
optimized: true
optimized_at: 2026-04-29T18:00:00Z
---
Warp is deeply customizable. Configure the terminal side (themes, keybindings, tabs, panes) and AI side (model choice, agent autonomy, default mode) independently.

Warp's client is open source under [AGPL v3](https://github.com/warpdotdev/warp/blob/master/LICENSE). See [[285-support-and-community-community-contributing|Contributing to Warp]] to build a custom variant.

## Quick reference

| What to customize | Where to find it | Quick action |
|---|---|---|
| Prompt chips | Right-click prompt area > **Edit prompt** | Drag and drop context chips |
| Model | Model selector in agent conversation | Choose Claude, GPT, Gemini, or Auto |
| Keyboard shortcuts | **Settings** > **Keyboard shortcuts** | Import from another terminal |
| Tabs | **Settings** > **Appearance** > **Tabs** | Switch to sidebar tab layout |
| Tab layouts | **Settings** > **Features** or `/` menu | Save and restore tab layouts |
| Tab configs | **Open settings file** button in Settings footer | — |
| Input mode | **Settings** > **Appearance** > **Input** | Choose Standard or Classic |
| App icon (macOS) | **Settings** > **Appearance** > **Icon** | Pick a custom icon |
| Text appearance | **Settings** > **Appearance** > **Text** | Change font, size, cursor |
| Agent autonomy | **Settings** > **Agents** > **Profiles** | Set what agent can do without asking |
| Default mode | **Settings** > **Agents** > **Warp Agent** > **Input** | Terminal or Agent Mode for new tabs |

## Appearance

Navigate to **Settings** > **Appearance**:

- [[091-terminal-appearance-themes|Themes]] — Pre-loaded themes or create [[089-terminal-appearance-custom-themes|custom themes]] with YAML or background image
- [[027-guides-getting-started-how-to-customize-warps-appearance|Prompt chips]] — Right-click prompt area, drag and drop chips (directory, git branch, Kubernetes context, time)
- [[234-terminal-appearance-app-icons|App icons]] — Custom app icon for your dock (macOS)
- [[237-terminal-appearance-input-position|Input position]] — Move prompt to top or bottom
- [[236-terminal-appearance-pane-dimming|Pane dimming]] — Dim inactive panes to focus the active one

## Layout

Organize your workspace with tabs, panes, and window configurations:

- [[128-terminal-windows-vertical-tabs|Vertical tabs]] — Sidebar layout for more horizontal space
- [[127-terminal-windows-tabs|Tabs]] — Custom titles and colors. Right-click to pick a color.
- [[125-terminal-windows-split-panes|Split panes]] — Divide tabs into multiple panels, side-by-side or stacked
- [[126-terminal-windows-tab-configs|Tab configs]] — Save and restore tab layouts with predefined pane arrangements and startup commands
- [[249-terminal-windows-global-hotkey|Global hotkey]] — Quake Mode with dedicated hotkey window

## Input and editor

Configure how you type and interact with terminal input:

- [[098-terminal-classic-input|Standard vs Classic input]] — Standard provides easier AI access; Classic resembles traditional terminals. Switch in **Settings** > **Appearance** > **Input**.
- [[016-getting-started-keyboard-shortcuts|Keyboard shortcuts]] — Create custom shortcuts or import from another terminal during [[024-getting-started-migrate-to-warp|migration]]
- [[105-terminal-editor-vim|Vim keybindings]] — Enable for keyboard-driven text editing
- **Tab key behavior** — Configure `Tab` in **Settings** > **Features**: accept autosuggestions or trigger completions

## AI and models

Control agent behavior and model selection:

- [[039-agent-platform-warp-agents-capabilities-overview-model-choice|Model choice]] — Choose Claude, GPT, Gemini, or Auto from the model selector
- **Default mode for new sessions** — Set in **Settings** > **Agents** > **Warp Agent** > **Input**: terminal mode or Agent Mode

## Import and sync

Bring existing settings into Warp or sync across machines:

- [[024-getting-started-migrate-to-warp|Migrate from another terminal]] — Per-source guides for iTerm2, Ghostty, macOS Terminal, Windows Terminal, VS Code, Cursor, Claude Code, and more. Includes automatic import for iTerm2.
- [[228-terminal-more-features-settings-sync|Settings sync]] — Sync Warp settings across machines (Beta)

## Next steps

- [[037-agent-platform-warp-agents-capabilities-overview-codebase-context|Codebase Context]] — Open a project and index your codebase for context-aware agent answers