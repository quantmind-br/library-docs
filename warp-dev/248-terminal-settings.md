---
title: Settings file | Warp
url: https://docs.warp.dev/terminal/settings
source: sitemap
fetched_at: 2026-04-29T15:02:54.497752757-03:00
rendered_js: false
word_count: 509
summary: This document explains how to configure Warp settings using the settings.toml file, including its file structure, synchronization with the UI, and troubleshooting steps.
tags:
    - warp-terminal
    - configuration-file
    - toml-format
    - user-preferences
    - terminal-settings
category: configuration
optimized: true
optimized_at: 2026-04-29T00:00:00Z
---
Warp stores preferences in `settings.toml`. Edit directly in any text editor, check into version control, or generate with a script. Changes take effect immediately.

Settings work alongside the graphical Settings panel. Changes in either place reflect in the other.

## Key features

- **Hot-reload** — Warp watches `settings.toml` for changes and applies them on save.
- **Error recovery** — Invalid TOML or unrecognized values show a warning banner; affected settings fall back to defaults.
- **Automatic migration** — Upgrading to a version with settings file auto-migrates existing preferences.
- **Bidirectional sync** — Settings panel (`⌘+,` macOS, `Ctrl+,` Linux/Windows) writes to `settings.toml`; hand-edits reflect in the panel.
- **Agent-powered editing** — Use Warp's agent with natural language (e.g., "increase font size to 16"). The bundled `modify-settings` skill handles updates.

## Opening your settings file

- In Warp: **Settings** → **Open settings file** at the bottom of the panel.
- Direct path by platform (see below).

## File location

| Platform | Stable | Preview |
|----------|--------|---------|
| macOS | `~/.warp/settings.toml` | `~/.warp-preview/settings.toml` |
| Linux | `~/.config/warp-terminal/settings.toml` | `~/.config/warp-terminal-preview/settings.toml` |
| Windows | `%LOCALAPPDATA%\warp\Warp\config\settings.toml` | `%LOCALAPPDATA%\warp\WarpPreview\config\settings.toml` |

## Settings file format

File uses [TOML v1.1](https://toml.io/en/v1.1.0) syntax. Settings organized into **sections** (TOML tables).

### How sections map to TOML tables

| Section | TOML Table | Description |
|---------|------------|-------------|
| `[general]` | Top-level | Session restoration, tab placement |
| `[appearance]` | Root with subsections | Visual settings: `[appearance.text]`, `[appearance.themes]`, `[appearance.cursor]` |
| `[agents]` | Root with subsections | Agent/AI settings: `[agents.profiles]`, `[agents.warp_agent.input]` |
| `[terminal]` | Root with subsections | Terminal behavior: `[terminal.input]` |

For the complete list of every setting, see [All settings reference](https://docs.warp.dev/terminal/settings/all-settings).

## How settings are applied

### Relationship between Settings panel and file

Settings panel and `settings.toml` represent the same underlying configuration. Changing a toggle in the Settings panel writes to `settings.toml`. Hand-editing updates the Settings panel on next read.

### Error banner

Invalid `settings.toml` shows a dismissible warning banner with an **Open settings file** button. Save a corrected file to clear automatically.

## Common configurations

### Change theme and font

```toml
[appearance.themes]
primary_theme = "One Dark (Nord)"

[appearance.text]
font_size = 14.0
font_family = "JetBrains Mono"
```

### Configure agent permissions

```toml
[agents.profiles]
default = "restrictions"
```

### Enable Vim keybindings

```toml
[editor.vim]
enabled = true
```

## Migrating from previous settings

Warp automatically migrates existing preferences into `settings.toml` when upgrading. No action required — customizations carry over.

## Troubleshooting

### "Your settings file contains an error" banner

Click **Open settings file** and check for:

- **Missing quotes** — String values need double quotes: `font_name = "Hack"`
- **Missing brackets** — Section headers need square brackets: `[appearance.text]`
- **Wrong value types** — Numbers (`font_size = 13.0`), booleans (`true`/`false`), valid enum strings

### Resetting to defaults

Delete (or rename) `settings.toml` and restart Warp. Falls back to built-in defaults. File re-created on next setting change through Settings panel.

### Settings not applying

Confirm you're editing the correct file for your platform and release channel. Multiple release channels each have their own settings directory.

## Related pages

- [All settings reference](https://docs.warp.dev/terminal/settings/all-settings) — Complete list of every setting with descriptions, types, and defaults
- [Custom themes](https://docs.warp.dev/terminal/appearance/custom-themes) — Create and load custom YAML or Base16 themes

#settings #configuration #toml
