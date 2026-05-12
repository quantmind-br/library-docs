---
title: Overview | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/plugins-overview
source: sitemap
fetched_at: 2026-04-26T08:39:19.605232169-03:00
rendered_js: false
word_count: 572
summary: This document provides an overview of the DankMaterialShell plugin system, including supported plugin types, installation methods, development guidelines, and troubleshooting steps.
tags:
    - dankmaterialshell
    - desktop-customization
    - qml-components
    - plugin-system
    - linux-desktop
    - wayland
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Plugins Overview

DankMaterialShell's plugin system extends the desktop with custom widgets, launchers, automation, and integrations via QML components.

## Plugin Location

Plugins live in `~/.config/DankMaterialShell/plugins/`. Each plugin is a directory containing a `plugin.json` manifest and QML components.

- **Official plugins:** [github.com/AvengeMedia/dms-plugins](https://github.com/AvengeMedia/dms-plugins)
- **Plugin registry:** [plugins.danklinux.com](https://plugins.danklinux.com)
- **Registry source:** [github.com/AvengeMedia/dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry)
- **Example plugins:** [github.com/AvengeMedia/DankMaterialShell/tree/master/quickshell/PLUGINS](https://github.com/AvengeMedia/DankMaterialShell/tree/master/quickshell/PLUGINS)

## Plugin Types

Five plugin types, defined by `type` in `plugin.json`:

### 1. Bar Widget (`type: "widget"`)

Widgets appearing in DankBar. Define `horizontalBarPill` and `verticalBarPill` components.

- **Capability:** `dankbar-widget`
- **Use cases:** System monitors, media controls, weather widgets, clock displays

### 2. Control Center Widget (`type: "widget"`)

Widgets appearing in the Control Center quick settings panel. Define `ccWidget*` properties for toggle buttons and detail panels.

- **Capability:** `control-center`
- **Use cases:** VPN toggles, custom shortcuts, service controls

### 3. Launcher Plugin (`type: "launcher"`)

Extends the application launcher with custom searchable items. Define `getItems()` and `executeItem()` functions.

- **Capability:** `launcher`
- **Required field:** `trigger` — trigger string for filtering (e.g., `"#"`, `"!"`, `""` for always-visible)
- **Use cases:** Emoji picker, calculator, web search, custom actions

### 4. Daemon (`type: "daemon"`)

Background services with no UI.

- **Capabilities:** `daemon`, `watch-events`
- **Use cases:** Battery alerts, wallpaper automation, notification handlers

### 5. Desktop Widget (`type: "desktop"`)

Widgets rendering on the desktop background layer via Wayland's wlr-layer-shell protocol. Users drag and resize via corner handles.

- **Capability:** `desktop-widget`
- **Features:**
  - Free positioning anywhere on desktop
  - Resizing with minimum size constraints
  - Multi-monitor support with independent positions per screen
  - Position/size persistence across sessions
- **Use cases:** Desktop clock, system monitor, weather widget, sticky notes

## Installation

### From GitHub

```bash
mkdir -p ~/.config/DankMaterialShell/plugins
cd ~/.config/DankMaterialShell/plugins
git clone https://github.com/author/plugin-name
dms restart
```

### From Plugin Registry

Browse [plugins.danklinux.com](https://plugins.danklinux.com) for installation links and documentation.

### Enable Plugin

1. Open **Settings → Plugins**
2. Click **Scan for Plugins**
3. Toggle the plugin on
4. Add to DankBar layout if applicable
5. Restart shell: `dms restart`

## Official Plugins

Maintained at [dms-plugins](https://github.com/AvengeMedia/dms-plugins):

- **Dank Actions** — Scriptable bar buttons and control center tiles
- **Dank Hooks** — Event-based automation triggers
- **Dank Pomodoro Timer** — Focus timer with notifications
- **Dank Battery Alerts** — Battery threshold warnings

Third-party plugins in the registry:

- **WallpaperShuffler** — Automatic wallpaper rotation
- **WorldClock** — Multi-timezone clock widget
- **PowerUsage** — Real-time power consumption monitor
- **Calculator** — Launcher-based calculator

> [!warning]
> Always review plugin source code before installation. Plugins run with full desktop session permissions.

## Development

See [[018-docs-dankmaterialshell-plugin-development|Plugin Development]] for the complete guide:

- Plugin manifest structure (`plugin.json`)
- Component architecture
- PluginService API
- Settings components
- Bar and Control Center integration
- Launcher plugin development
- Global variables and state management

## Example Plugins

Reference implementations in the main repository:

- [ExampleEmojiPlugin](https://github.com/AvengeMedia/DankMaterialShell/tree/master/quickshell/PLUGINS/ExampleEmojiPlugin) — Launcher plugin with emoji picker
- [LauncherExample](https://github.com/AvengeMedia/DankMaterialShell/tree/master/quickshell/PLUGINS/LauncherExample) — Basic launcher plugin structure

## Plugin Registry Submission

1. Create a public GitHub repository
2. Include `plugin.json`, README, and screenshots
3. Validate manifest against `plugin-schema.json`
4. Submit PR to [dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry)
5. Site rebuilds automatically on merge

## Troubleshooting

**Plugin not detected:**
- Verify `plugin.json` syntax with `jq .`
- Check directory is in `~/.config/DankMaterialShell/plugins/`
- Click "Scan for Plugins" in Settings

**Plugin won't load:**
- Check logs: `dms kill && dms run` from terminal
- Verify component paths in `plugin.json`
- Ensure dependencies are installed

**Settings not working:**
- Add `"permissions": ["settings_write"]` to manifest
- Use `PluginSettings` wrapper component
- Check PluginService is injected properly

## Next Steps

- Browse plugins at [plugins.danklinux.com](https://plugins.danklinux.com)
- Learn development in [[018-docs-dankmaterialshell-plugin-development|Plugin Development]]
- Review examples in the [PLUGINS directory](https://github.com/AvengeMedia/DankMaterialShell/tree/master/PLUGINS)
