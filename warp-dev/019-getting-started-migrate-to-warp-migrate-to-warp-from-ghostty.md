---
title: Migrate to Warp from Ghostty | Warp
url: https://docs.warp.dev/getting-started/migrate-to-warp/migrate-to-warp-from-ghostty
source: sitemap
fetched_at: 2026-04-29T15:02:04.431884027-03:00
rendered_js: false
word_count: 396
summary: This document provides instructions for migrating terminal configurations, themes, and settings from Ghostty to the Warp terminal, utilizing both automated AI agent tools and manual configuration steps.
tags:
    - migration
    - ghostty
    - warp-terminal
    - configuration
    - ai-agent
    - customization
category: guide
optimized: true
optimized_at: 2026-04-29T20:15:00Z
---
# Migrate to Warp from Ghostty

Bring over your Ghostty themes, fonts, and keybindings quickly. Ghostty stores configuration in `~/.config/ghostty/config`.

---

## Agent-Assisted Migration (Recommended)

Warp's `modify-settings` skill reads your Ghostty config and writes equivalent Warp settings, including custom theme translation:

1. In Warp, open a new tab and switch to [[198-agent-platform-warp-agents-capabilities-overview|Agent Mode]] with `⌘+I` (macOS) or `Ctrl+I` (Linux/Windows).
2. Prompt:
   > Read my Ghostty config at `~/.config/ghostty/config` and any referenced theme files in `~/.config/ghostty/themes/`. Port the equivalent settings (theme, font, keybindings, shell) into my Warp `settings.toml` using the `modify-settings` skill, and create a matching custom theme. Show me a diff before applying.
3. Review and approve the diff. Warp hot-reloads `settings.toml` immediately.

Alternatively, configure manually (steps below).

---

## Manual Configuration

### Theme and Colors

1. Open **Settings** > **Appearance** > **Themes** in Warp.
2. Pick a built-in theme or [create a custom theme](https://docs.warp.dev/terminal/appearance/custom-themes) by translating Ghostty colors into a YAML theme file.
3. Ghostty theme files live in `~/.config/ghostty/themes/`. Open the file named in your `theme` setting to copy foreground, background, and 16 ANSI color values.

### Font and Text

1. In **Settings** > **Appearance** > **Text, fonts, & cursor**, match your Ghostty `font-family` and `font-size` values.
2. Enable **Ligatures** if you use them.

### Keybindings

Warp's [[016-getting-started-keyboard-shortcuts|default keyboard shortcuts]] cover most Ghostty bindings. For custom bindings from Ghostty `keybind` lines, open **Settings** > **Keyboard shortcuts** and add manually.

### Shell and Prompt

Warp detects your login shell automatically. To override: **Settings** > **Features** > **Session** > **Startup shell for new sessions**.

For prompts, choose:

- **Warp prompt** — native drag-and-drop context chips. Configure via [[014-getting-started-customizing-warp|Customizing Warp]].
- **Shell prompt (PS1)** — keep your existing prompt configuration.

### Quick Terminal (Quake Mode)

Ghostty's quick terminal maps to Warp's global hotkey: **Settings** > **Features** > **Window** > **Global hotkey**. See [[249-terminal-windows-global-hotkey|global hotkey]] for full configuration.

---

## Warp-Native Equivalents

| Ghostty Feature | Warp Equivalent |
|-----------------|-----------------|
| Config file | `settings.toml` |
| Theme files | [[089-terminal-appearance-custom-themes|Custom themes]] |
| Quick terminal (Quake) | [[249-terminal-windows-global-hotkey|Global hotkey]] |
| Native tabs | [[127-terminal-windows-tabs|Tabs]] |
| Native splits | [[125-terminal-windows-split-panes|Split panes]] |
| Fast terminal | Warp (high-performance renderer) |
| GPU rendering | Warp (Metal/D3D/Vulkan) |

Beyond feature parity, Warp adds [[198-agent-platform-warp-agents-capabilities-overview|Agent Mode]], [[182-code-code-review|Code Review]], and [[144-knowledge-and-collaboration-warp-drive|Warp Drive]] for AI-assisted development and team collaboration.

For more on configuring Warp, see [[014-getting-started-customizing-warp|Customizing Warp]].

#migration-guide #ghostty #terminal-configuration