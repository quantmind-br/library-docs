---
title: DMS 1.2 "Spicy Miso" Released
url: https://danklinux.com/blog/v1-2-release
source: sitemap
fetched_at: 2026-04-26T08:35:03.39641168-03:00
rendered_js: false
word_count: 2552
summary: This document outlines the major new features and improvements introduced in DankMaterialShell (DMS) version 1.2, including desktop widgets, theme management, clipboard history, and expanded compositor support.
tags:
    - dms
    - linux
    - desktop-environment
    - wayland
    - release-notes
    - software-update
category: other
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

DMS 1.2 "Spicy Miso" brings numerous new features and major improvements to both the DMS core and plugin system.

**Stats:** 2,800+ commits | 3.3k+ GitHub Stars | 100+ Contributors | 40 Plugins

## What's New

### Desktop Widgets & Plugins

DMS 1.2 introduces Desktop Widgets — small applets that live on your desktop, below windows and above your wallpaper. Position, resize, and configure them per-display.

The plugin system makes building your own widgets straightforward — see the [[018-docs-dankmaterialshell-plugin-development#desktop-plugins|plugin development guide]] to get started.

### Theme Registry

![Theme Registry](https://danklinux.com/img/blog/v1.2/themeregistrylight.png)![Theme Registry](https://danklinux.com/img/blog/v1.2/themeregistry.png)

DMS 1.2 introduces a theme system where a single theme can have multiple variants and accent colors. The plugin registry now includes a [Theme Registry](https://danklinux.com/plugins?tab=themes) with community-developed themes available for easy installation. Learn how to [contribute your own themes](https://github.com/AvengeMedia/dms-plugin-registry/blob/master/CONTRIBUTING.md#contributing-a-theme).

### Native Clipboard and History

![Clipboard Settings](https://danklinux.com/img/blog/v1.2/clipboardlight.png)![Clipboard Settings](https://danklinux.com/img/blog/v1.2/clipboard.png)

Full, zero-dependency clipboard and clipboard history integration.

- No dependency on external tools (cliphist, wl-clipboard)
- Configurable max entry size, retention duration, and automatic cleanup
- Search API and CLI with pagination, filtering by text, images, or any mime type
- Automatically ignores data from password managers (KeepassXC, 1Password)
- Export and import functionality
- Migration tool for transferring history from cliphist

### Monitor Configurator

![Monitor Configuration](https://danklinux.com/img/blog/v1.2/monitorlight.png)![Monitor Configuration](https://danklinux.com/img/blog/v1.2/monitordark.png)

Configure display settings directly from DMS Settings. Available for niri, Hyprland, and MangoWC: positioning, resolution, refresh rate, VRR, full layout customization (niri), HDR (Hyprland), scaling, mirroring (Hyprland), and more.

### Notification Improvements

![Notification Center](https://danklinux.com/img/blog/v1.2/notiflight.png)![Notification Center](https://danklinux.com/img/blog/v1.2/notifdark.png)

Notifications received several new features:
- Configurable history with variable size, expirations, and auto-cleanup
- Gestures to dismiss notifications
- Ability to display on lock screen (count only, name only, or full content based on privacy preference)

### Cursor & Layout Configuration

![Cursor Control Settings](https://danklinux.com/img/blog/v1.2/cursor-control.png)

Customize compositor settings directly from DMS Settings. Available for niri, Hyprland, and MangoWC:

- **Cursor** — Choose cursor themes, adjust size, configure compositor-specific hiding behavior (hide on typing, hide on touch, inactive timeout)
- **Gaps** — Adjust gaps around windows
- **Borders & Corner Radius** — Override theme defaults for window border width and corner radius
- **Focus Ring** — Customize focus ring color, width, and style

Cursor settings are automatically applied to XWayland applications via XResources, ensuring consistent appearance across native Wayland and XWayland apps.

### DMS Doctor

![DMS Doctor](https://danklinux.com/img/blog/v1.2/doctorlight.png)![DMS Doctor](https://danklinux.com/img/blog/v1.2/doctordark.png)

New `dms doctor` command for diagnosing configuration issues and conflicts that may negatively affect DMS feature availability or performance. Also available via DMS GUI.

Shout out to [@LuckShiba](https://github.com/LuckShiba) for the contribution!

### Keyboard Shortcuts Editor for niri, Hyprland & MangoWC

![Keyboard Shortcuts](https://danklinux.com/img/blog/v1.2/bindslight.png)![Keyboard Shortcuts](https://danklinux.com/img/blog/v1.2/bindsdark.png)

Configure keyboard shortcuts with search, filtering, and conflict detection. The world-famous DMS keyboard shortcuts tool is now available for niri, Hyprland, and MangoWC.

### Settings Search

![Settings Search](https://danklinux.com/img/blog/v1.2/searchlight.png)![Settings Search](https://danklinux.com/img/blog/v1.2/searchdark.png)

New settings search makes it easier to find what you want to change. Includes integrated launcher search with `?` by default.

### i18n: RTL Support

![RTL Language Support](https://danklinux.com/img/blog/v1.2/rtllight.png)![RTL Language Support](https://danklinux.com/img/blog/v1.2/rtldark.png)

DMS 1.2 introduces proper support for right-to-left languages with proper layout mirroring across components. DMS currently has translations for Hebrew and Farsi.

To contribute to translations see the [pinned GitHub issue](https://github.com/AvengeMedia/DankMaterialShell/issues/324).

### Launcher Improvements

![Launcher File Search](https://danklinux.com/img/blog/v1.2/launcherlight.png)![Launcher File Search](https://danklinux.com/img/blog/v1.2/launcherdark.png)

The DMS launcher has undergone several improvements: performance improvements, support for plugins to define context menus (with full keyboard navigation), built-in settings search, and a new first-party plugin for searching keybinds (niri, Hyprland, MangoWC, Sway, and custom providers via `dms keybinds`).

DMS' launcher with plugins supports calculator, niri window management, CLI commands with history, emoji and gitmoji search, web search, extremely fast indexed filesystem search, and more. It also works on the niri overview without any triggers needed.

## Debian SID, OpenSUSE Slowroll, Leap 16.0, and CentOS Stream 10 Packages

DMS 1.2 expands distribution support with official packages now available for:
- **Debian SID** — Rolling release packages via OBS
- **OpenSUSE Slowroll** — Packages via OBS
- **OpenSUSE Leap 16.0** — Packages via OBS
- **CentOS Stream 10** — Packages via COPR

In addition to existing packages for Debian, Ubuntu, Fedora, Arch Linux, and NixOS.

Packages include DMS, niri, quickshell, dgop, dsearch, and other core dependencies. See the [[003-docs-getting-started]] for setup instructions.

## Upgrade Notes

> [!warning]
> This release contains changes that may require manual intervention.

### (Breaking) Theme Updates

Ghostty and VSCode theming have changed and will stop working without manual intervention.

**Ghostty**

The theme path has changed to `~/.config/ghostty/themes/danktheme`. Update your Ghostty configuration:

```toml
# ~/.config/ghostty/config
# Add this
theme = dankcolors
# ! Remove this
# config-file = ./config-dankcolors
```

**VS Code / Codium**

The theme extension needs to be reinstalled due to internal changes:

1. Uninstall the current "Dank material shell theme" extension
2. Reinstall from the extensions marketplace: search for "Dank material shell theme" by "DankLinux"
3. Ctrl+Shift+P -> "Preferences: Color Theme" -> Select "Dynamic Base16 DankShell"
4. Trigger theme re-generation — change theme in DMS Settings or restart DMS
5. Fully exit and restart VSCode

### Clipboard History Migration

Steps are recommended to remove existing clipboard history daemon and migrate existing history to the new DMS clipboard system.

**1. Cleanup old clipboard history integration:**

Remove the `wl-paste --watch cliphist store` daemon/startup from your compositor configuration.

```js
// ~/.config/niri/config.kdl
spawn-at-startup "wl-paste --watch cliphist store" // REMOVE THIS LINE
```

```toml
# ~/.config/hypr/hyprland.conf
exec-once = wl-paste --watch cliphist store # REMOVE THIS LINE
```

**2. Configure DMS clipboard settings (optional):**

Before migrating, configure your retention settings in DMS Settings -> System -> Clipboard. You can configure maximum entry size, total entries, and retention durations. Only required if you want to override the defaults.

**3. Migrate clipboard history from `cliphist` to DMS:**

New clipboard history is located in `~/.cache/DankMaterialShell/clipboard/db` (a [bbolt](https://github.com/etcd-io/bbolt) database). To migrate old history:

```bash
# First stop DMS
systemctl --user stop dms # Or dms kill, if not using systemd
# Run migration (optionally override path with cliphist-migrate /path/to/db)
dms cl cliphist-migrate
# Start DMS again
systemctl --user start dms # or dms run -d, if not using systemd
```

You can then uninstall cliphist and remove the old database at `~/.cache/cliphist/db`.

`wl-clipboard` can also be removed, although it is useful to keep for plugins or scripts that depend on it. DMS clipboard CLI has feature-parity with wl-clipboard:

```bash
# To copy text:
echo "Hello, World!" | dms cl copy
# To paste text:
dms cl paste
```

### Compositor Configuration Updates

For niri or Hyprland you can run `dms setup` to generate a new compositor configuration — monitor configuration will be preserved and the original configuration will be backed up. Changes are required only if you wish to use the new cursor, output, layout, and keybind controls from DMS Settings.

**niri**

Required to use GUI cursor and output settings.

1. Create new files:

```bash
mkdir -p ~/.config/niri/dms
touch ~/.config/niri/dms/cursor.kdl
touch ~/.config/niri/dms/outputs.kdl
```

2. Move existing configuration to new files:

```js
// ~/.config/niri/dms/cursor.kdl
// Move cursor {} block from config.kdl
cursor {
    xcursor-theme "Bibata-Original-Ice"
    xcursor-size 24
}
// ~/.config/niri/dms/outputs.kdl
// Move output {} blocks from config.kdl
output "DP-1" {
    position 0 0
    scale 1.0
    transform normal
}
```

3. Include new files in your config:

```js
// ~/.config/niri/config.kdl
// Recommended to place at the end of the file
include "dms/cursor.kdl"
include "dms/outputs.kdl"
include "dms/layout.kdl"
```

**Hyprland**

Required to use GUI cursor, output, layout, and keybind settings.

1. Create new files:

```bash
mkdir -p ~/.config/hypr/dms
touch ~/.config/hypr/dms/cursor.conf
touch ~/.config/hypr/dms/outputs.conf
touch ~/.config/hypr/dms/layout.conf
touch ~/.config/hypr/dms/binds.conf
```

2. Move existing configuration to new files:

```bash
# ~/.config/hypr/dms/cursor.conf
# Move cursor settings from hyprland.conf
env = HYPRCURSOR_THEME,Bibata-Original-Ice
env = HYPRCURSOR_SIZE,24
env = XCURSOR_THEME,Bibata-Original-Ice
env = XCURSOR_SIZE,24
# ~/.config/hypr/dms/outputs.conf
# Move monitor lines from hyprland.conf
monitor = DP-1,2560x1440@144,0x0,1
# ~/.config/hypr/dms/layout.conf
# Move general layout settings from hyprland.conf
general {
    gaps_in = 5
    gaps_out = 10
    border_size = 2
}
# ! Binds do not need to be moved, only edited/new binds via GUI will be stored here
```

3. Source new files in your config:

```bash
# ~/.config/hypr/hyprland.conf
# Recommended to place at the end of the file
source = ./dms/cursor.conf
source = ./dms/outputs.conf
source = ./dms/layout.conf
source = ./dms/binds.conf
```

**MangoWC**

Required to use GUI cursor, output, layout, and keybind settings.

1. Create new files:

```bash
mkdir -p ~/.config/mangowc/dms
touch ~/.config/mangowc/dms/cursor.conf
touch ~/.config/mangowc/dms/outputs.conf
touch ~/.config/mangowc/dms/layout.conf
touch ~/.config/mangowc/dms/binds.conf
```

2. Move existing configuration to new files:

```bash
# ~/.config/mangowc/dms/cursor.conf
# Move cursor settings from mangowc.conf
cursor_size=24
cursor_theme=Bibata-Original-Ice
# ~/.config/mangowc/dms/outputs.conf
# Move output blocks from mangowc.conf
monitorrule=DP-2,0.55,1,tile,0,1,0,0,2560,1440,144
monitorrule=eDP-1,0.55,1,tile,0,1,2560,0,2560,1600,240
# ~/.config/mangowc/dms/layout.conf
# Move layout settings from mangowc.conf
border_radius=13
gappih=4
gappiv=4
gappoh=4
gappov=4
borderpx=2
# ~/.config/mangowc/dms/binds.conf
# Moving binds is not required, only edited/new binds via GUI will be stored here
```

3. Source new files in your config:

```bash
# ~/.config/mangowc/mangowc.conf
# Recommended to place at the end of the file
source = ./dms/cursor.conf
source = ./dms/outputs.conf
source = ./dms/layout.conf
source = ./dms/binds.conf
```

### NixOS Updates

DMS 1.2 brings significant improvements to NixOS integration and the flake-based installation experience:

**Home Manager Module Enhancements**
- New `clipboardSettings` option for declarative clipboard configuration
- Plugins can now include per-plugin settings directly in their configuration
- Removed `default*` settings options in favor of being able to set the actual settings file
- Improved plugin installation and management through home-manager module

**NixOS Module Improvements**
- Added plugin support in NixOS module with declarative installation
- Enabled `power-profiles-daemon` and `accounts-daemon` by default for better power management and user account integration
- QML dependencies are now properly included in `dms-shell` package

**Niri Integration**
- Added support for config includes with niri-flake; DMS-generated configuration files now work seamlessly with niri's flake-based setup

**Plugin Registry Flake**
- New [dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry) Nix flake provides all community plugins as packages
- Plugins are automatically updated daily from the registry
- Simple declarative installation — just enable plugins by their ID
- Works with both NixOS and Home Manager modules

> [!info]
> The DMS Flake options name was changed from `programs.dankMaterialShell` to `programs.dank-material-shell`. The modules names also changed. While the old module names will still work, you will receive a deprecation warning informing about the new name.

> [!info]
> The documentation for the [[055-docs-dankmaterialshell-nixos|nixpkgs module]] and [[010-docs-dankmaterialshell-nixos-flake|flake-based setup]] will get updated as soon as DMS 1.2 gets into `nixos-unstable`.

## Bug Fixes and Improvements

Since the v1.0 release, DMS has received extensive bug fixes and stability improvements across all components:

**Clipboard**
- Native clipboard and history implementation with zero external dependencies
- Add cliphist-migrate CLI for importing existing history
- Add shift+enter to paste from clipboard history modal
- Configurable persistence, mime-type handling, and auto-cleanup
- Automatically ignore sensitive mime types from password managers
- Fix mime type selection and nil offer handling

**Bar & Dock**
- Add shadow option for bars; add scroll wheel behavior configuration
- Add bar get/setPosition IPC; improve high-DPI scrolling logic
- Fix exclusive zone popup positioning; fix reveal on overview/niri when auto-hide enabled
- Fix tooltip positioning with adjacent bars; improve pinned app re-ordering feedback
- Make control center widget per-instance; add option to show bar when hidden and no windows
- Respect compact mode on vertical bar; mouse wheel options for media player widget
- Fix widget base hover blend logic; add isolate running apps by display option

**Desktop Widgets & Plugins**
- New desktop widget plugin type with draggable per-monitor widgets
- Built-in clock and system monitor desktop widgets
- Add grid/grid size hints for widget positioning; add overlay IPC and overview option
- Enable desktop plugins by default; fix widget display toggle and key event handling
- Centralize config in desktop widgets tab; add niri overview only option
- Persistent plugins with async updates; fix first plugin install reactivity
- Hide uninstall/update buttons for system plugins; IPC visibility conditions for plugins

**Display & Monitor Configuration**
- Add configurator for niri, Hyprland, and MangoWC
- Configure position, VRR, orientation, resolution, refresh rate
- Add Hyprland HDR options; add niri-specific layout options
- Add mirroring option for Hyprland; add disable output option for Hyprland
- Fix reverted state for position; fix text-alignment in model mode
- Explicitly write scale 1 for niri; add adaptiveSyncSupported to wlroutput API

**Notifications**
- Add configurable persistent history with variable size and expiration
- Add swipe to dismiss functionality; add support for lock screen display
- Add compact mode with expansion in history and popup; add image persistence
- Right-click to toggle Do Not Disturb; add Do Not Disturb to IPC
- Add modal function for clearing all notifications
- Fix notifications being transient when history disabled
- Fix redundant height animation and spacing improvements; minimize rapid window creation/destruction

**Themes & Matugen**
- Theme registry with community themes and variants; support for accent colors and theme variants
- Add color reload capability to VSCode theme; add GTK theme method and fix light mode
- Move Ghostty theming to new path; add Zen Browser template
- Add gruvbox material custom theme varieties; add neovim to matugen pipeline with soothing theme
- Fix adw-gtk3 setting in light mode; set cursor color for themes
- Fix terminals always dark with custom themes; update VSCode template with improved highlighting

**Cursor & Layout**
- DMS Cursor Control for size and theme in niri; create/update XResources for XWayland apps
- Add Hyprland and MangoWC cursor config support
- Add GUI gaps, window radius, and border overrides; support for niri, Hyprland, and MangoWC layouts

**Launcher**
- Built-in settings search plugin with `?` trigger; support for plugins to define context menus
- Add ID search fallback for non-English apps; allow terminal apps
- F10 as alt for menu key; optimize bindings and filters; fix invalid icon rendering

**Settings**
- Add search across all settings; add doctor command with GUI integration
- Add battery charge limit setting; add lock screen layout settings
- Add volume and brightness percentages; fix desktop widget accordion row height
- Fix generic color selector clipping; fix theme application of default-settings
- Guard saving before load completed; make default height screen-aware; read-only handling refactor

**Network & VPN**
- Support hidden SSIDs; listen to NetworkManager wired interface
- Use nmcli for route metrics; right-click VPN widget to quick connect
- Aggregate VPN import errors with toast details; support pkcs11 prompts; cache pkcs11 pin input

**Keyboard & Input**
- Initial support for writable Hyprland and MangoWC keybinds; add media control bindings for audio playback
- Fix keybind handling of cooldown-ms parameter; fix empty string args and screenshot-window options
- Add log if ShortcutInhibitor is missing; accept numpad enter key for screenshot selection

**Lock Screen & Power**
- Add fade to monitor off option; clear lock screen textbox on Escape
- Handle case where session lock is rejected; fix font alignment; add PAM login fallback
- Fade to lock and monitor off by default

**Audio & Media**
- Recreate media players on pipewire device change; add option to disable visualizer in bar widget
- Add scroll wheel behavior configuration; allow adjusting notification volume
- Larger option for media player widget

**i18n & RTL**
- Initial RTL support for notifications, settings, control center, launcher
- Fix RTL alignment of settings sidebar and plugin settings
- Add Farsi and Hungarian translations; general term cleanup and sync

**niri**
- Add gaps and radius override; add warnings on auto-generated files
- Fix effectiveScreenAssignment in modal; fix gap reactivity; handle window urgency event
- Preserve remaining settings when turning off output; release focus for popouts on overview
- Track open modals for focus transfers; hack for config includes with niri flake

**Hyprland**
- Always use single window mode; fix cursor setting; change DPMS off to DPMS toggle
- Update reference config for 0.53; smart compositor entry point detection

**Core & Backend**
- Add resolve-include recursive functionality; add test coverage for wayland stack with race detection
- Mock wayland context for tests; detect quickshell crash on SIGTERM
- Exit non-zero on SIGUSR1 for systemd restart; preserve quickshell exit code
- Fix socket reported CLI version; use stdlib for XDG dirs
- Implement screensaver interface for idle inhibitor; poll with wake pipe instead of read deadlines

**Greeter**
- Change Hyprland startup to exec-once; use FolderListModel for session iteration
- Add launch timeout; simplify start-hyprland check
- Fix per-monitor and per-mode wallpapers (NixOS)

**Wallpaper**
- Add seconds to wallpaper cycling; pause cycling when locked
- Encode image URIs; clamp max texture size; scale texture to physical pixels

**Build & Distribution**
- Debian SID, OpenSUSE Slowroll, Leap 16.0, CentOS Stream 10 packages
- Ubuntu ARM64 support; Artix Linux and Void Linux widget mappings
- Remove cliphist dependency on dms-git; OBS and PPA automation improvements
- NixOS module refactoring and fixes

**Miscellaneous**
- Add welcome page with doctor integration for first launch; configurable app ID substitutions
- Map steam\_app\_ID to steam\_icon\_ID for game icons
- Flatpak introspection utilities; detect flatpak installations of Zen Browser and Vesktop
- Fix touchpad scrolling behavior; add group workspace apps toggle
- Reverse workspace scrolling option; add hide option for updater widget
- Use volume\_mute icon for volume==0

## Resources

[[003-docs-getting-started|Get Started with DMS]]

![niri](https://danklinux.com/img/niri.svg)

Special thanks to [YaLTeR](https://github.com/YaLTeR) for collaborating with the DMS team, for [niri](https://github.com/niri-wm/niri) — the compositor that inspired DMS, and for hosting DMS on the [niri Discord](https://discord.gg/ppWTpKmPgT).

## Thank You

To everyone who has supported DMS through feedback, contributions, sponsorships, donations, and packaging.

Zan, Zendegi, Azadi
