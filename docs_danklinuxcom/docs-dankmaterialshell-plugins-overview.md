---
title: Overview | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/plugins-overview
source: sitemap
fetched_at: 2026-01-24T13:33:55.60134242-03:00
rendered_js: false
word_count: 572
summary: This document outlines the architecture of the DankMaterialShell plugin system, detailing the various plugin types, installation procedures, and management of desktop extensions.
tags:
    - dankmaterialshell
    - plugin-system
    - desktop-widgets
    - qml-components
    - wayland
    - extension-management
category: guide
---

```
██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗
██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝
██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗
██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║
██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝
```

DankMaterialShell's plugin system allows extending the desktop with custom widgets, launchers, automation, and integrations through QML components.

## Plugin Location[​](#plugin-location "Direct link to Plugin Location")

Plugins are installed to `~/.config/DankMaterialShell/plugins/`. Each plugin is a directory containing a `plugin.json` manifest and QML components.

**Official plugins:** [github.com/AvengeMedia/dms-plugins](https://github.com/AvengeMedia/dms-plugins) **Plugin registry:** [plugins.danklinux.com](https://plugins.danklinux.com) **Registry source:** [github.com/AvengeMedia/dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry) **Example plugins:** [github.com/AvengeMedia/DankMaterialShell/tree/master/quickshell/PLUGINS](https://github.com/AvengeMedia/DankMaterialShell/tree/master/quickshell/PLUGINS)

## Plugin Types[​](#plugin-types "Direct link to Plugin Types")

DankMaterialShell supports four plugin types defined in `plugin.json`:

### 1. Bar Widget (`type: "widget"`)[​](#1-bar-widget-type-widget "Direct link to 1-bar-widget-type-widget")

Widgets that appear in DankBar. Define `horizontalBarPill` and `verticalBarPill` components for different bar orientations.

**Capabilities:**

- `dankbar-widget` - Appears in DankBar

**Example use cases:** System monitors, media controls, weather widgets, clock displays

### 2. Control Center Widget (`type: "widget"`)[​](#2-control-center-widget-type-widget "Direct link to 2-control-center-widget-type-widget")

Widgets that appear in the Control Center quick settings panel. Define `ccWidget*` properties for toggle buttons and detail panels.

**Capabilities:**

- `control-center` - Appears in Control Center

**Example use cases:** VPN toggles, custom shortcuts, service controls

### 3. Launcher Plugin (`type: "launcher"`)[​](#3-launcher-plugin-type-launcher "Direct link to 3-launcher-plugin-type-launcher")

Extends the application launcher with custom searchable items. Define `getItems()` and `executeItem()` functions.

**Capabilities:**

- `launcher` - Adds items to Spotlight search

**Required fields:**

- `trigger` - Trigger string for filtering (e.g., `"#"`, `"!"`, `""` for always-visible)

**Example use cases:** Emoji picker, calculator, web search, custom actions

### 4. Daemon (`type: "daemon"`)[​](#4-daemon-type-daemon "Direct link to 4-daemon-type-daemon")

Background services with no UI. Run automation, monitoring, or provide services to other plugins.

**Capabilities:**

- `daemon` - Background service
- `watch-events` - React to system events

**Example use cases:** Battery alerts, wallpaper automation, notification handlers

### 5. Desktop Widget (`type: "desktop"`)[​](#desktop-plugin "Direct link to desktop-plugin")

Widgets that render directly on the desktop background layer using Wayland's wlr-layer-shell protocol. Users can drag them anywhere and resize via corner handles.

**Capabilities:**

- `desktop-widget` - Appears on the desktop layer

**Features:**

- Free positioning anywhere on desktop
- Resizing with minimum size constraints
- Multi-monitor support with independent positions per screen
- Position/size persistence across sessions

**Example use cases:** Desktop clock, system monitor, weather widget, sticky notes

## Installation[​](#installation "Direct link to Installation")

### From GitHub[​](#from-github "Direct link to From GitHub")

```
mkdir-p ~/.config/DankMaterialShell/plugins
cd ~/.config/DankMaterialShell/plugins
git clone https://github.com/author/plugin-name
dms restart
```

### From Plugin Registry[​](#from-plugin-registry "Direct link to From Plugin Registry")

Browse [plugins.danklinux.com](https://plugins.danklinux.com) for installation links and documentation.

### Enable Plugin[​](#enable-plugin "Direct link to Enable Plugin")

1. Open **Settings → Plugins**
2. Click **Scan for Plugins**
3. Toggle the plugin on
4. Add to DankBar layout if applicable
5. Restart shell: `dms restart`

## Official Plugins[​](#official-plugins "Direct link to Official Plugins")

Maintained by the DankMaterialShell team at [dms-plugins](https://github.com/AvengeMedia/dms-plugins):

- **Dank Actions** - Scriptable bar buttons and control center tiles
- **Dank Hooks** - Event-based automation triggers
- **Dank Pomodoro Timer** - Focus timer with notifications
- **Dank Battery Alerts** - Battery threshold warnings

Third-party plugins submitted to the registry at [plugins.danklinux.com](https://plugins.danklinux.com):

- **WallpaperShuffler** - Automatic wallpaper rotation
- **WorldClock** - Multi-timezone clock widget
- **PowerUsage** - Real-time power consumption monitor
- **Calculator** - Launcher-based calculator

> Always review plugin source code before installation. Plugins run with full desktop session permissions.

## Development[​](#development "Direct link to Development")

See [Plugin Development](https://danklinux.com/docs/dankmaterialshell/plugin-development) for the complete development guide including:

- Plugin manifest structure (`plugin.json`)
- Component architecture
- PluginService API
- Settings components
- Bar and Control Center integration
- Launcher plugin development
- Global variables and state management

## Example Plugins[​](#example-plugins "Direct link to Example Plugins")

Reference implementations in the main repository:

- [ExampleEmojiPlugin](https://github.com/AvengeMedia/DankMaterialShell/tree/master/PLUGINS/ExampleEmojiPlugin) - Launcher plugin with emoji picker
- [LauncherExample](https://github.com/AvengeMedia/DankMaterialShell/tree/master/PLUGINS/LauncherExample) - Basic launcher plugin structure

## Plugin Registry Submission[​](#plugin-registry-submission "Direct link to Plugin Registry Submission")

To add your plugin to the registry:

1. Create a public GitHub repository
2. Include `plugin.json`, README, and screenshots
3. Validate manifest against `plugin-schema.json`
4. Submit PR to [dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry)
5. Site rebuilds automatically on merge

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

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

## Next Steps[​](#next-steps "Direct link to Next Steps")

- Browse available plugins at [plugins.danklinux.com](https://plugins.danklinux.com)
- Learn plugin development in [Plugin Development](https://danklinux.com/docs/dankmaterialshell/plugin-development)
- Review example code in the [PLUGINS directory](https://github.com/AvengeMedia/DankMaterialShell/tree/master/PLUGINS)