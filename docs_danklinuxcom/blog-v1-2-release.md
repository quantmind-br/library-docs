---
title: DMS 1.2 "Spicy Miso" Released
url: https://danklinux.com/blog/v1-2-release
source: sitemap
fetched_at: 2026-01-24T13:31:58.862615461-03:00
rendered_js: false
word_count: 2482
---

We're excited to announce DankMaterialShell (DMS) 1.2 "Spicy Miso"! This release features numerous new features and major improvements to both the DMS core and plugin system.

2,800+Commits

3.3k+GitHub Stars

100+Contributors

40Plugins

## What's New[​](#whats-new "Direct link to What's New")

### Desktop Widgets & Plugins[​](#desktop-widgets--plugins "Direct link to Desktop Widgets & Plugins")

DMS 1.2 introduces Desktop Widgets - small applets that live on your desktop, below windows and above your wallpaper. Position, resize, and configure them per-display.

The plugin system makes building your own widgets straightforward - see the [plugin development guide](https://danklinux.com/docs/dankmaterialshell/plugin-development#desktop-plugins) to get started.

### Theme Registry[​](#theme-registry "Direct link to Theme Registry")

![Theme Registry](https://danklinux.com/img/blog/v1.2/themeregistrylight.png)![Theme Registry](https://danklinux.com/img/blog/v1.2/themeregistry.png)

Theme browser integrated into DMS settings.

DMS 1.2 introduces a theme system where a single theme can have multiple variants and accent colors. The plugin registry now includes a [Theme Registry](https://danklinux.com/plugins?tab=themes) with community-developed themes available for easy installation. Learn how to [contribute your own themes](https://github.com/AvengeMedia/dms-plugin-registry/blob/master/CONTRIBUTING.md#contributing-a-theme).

### Native Clipboard and History[​](#native-clipboard-and-history "Direct link to Native Clipboard and History")

![Clipboard Settings](https://danklinux.com/img/blog/v1.2/clipboardlight.png)![Clipboard Settings](https://danklinux.com/img/blog/v1.2/clipboard.png)

Configure clipboard history size, entry limits, and auto-cleanup behavior.

Full, zero-dependency clipboard and clipboard history integration.

- No dependency on external tools, such as cliphist or wl-clipboard.
- Configurable max entry size, retention duration, and automatic cleanup.
- Search API and CLI with pagination, filtering by text, images, or any mime type.
- Automatically ignores data from password managers (such as KeepassXC and 1Password). Preventing sensitive data from being stored in the clipboard history.
- Export & import functionality
- Migration tool for transferring history from cliphist.

### Monitor Configurator[​](#monitor-configurator "Direct link to Monitor Configurator")

![Monitor Configuration](https://danklinux.com/img/blog/v1.2/monitorlight.png)![Monitor Configuration](https://danklinux.com/img/blog/v1.2/monitordark.png)

Configure display settings directly from DMS Settings.

Configure display settings directly from DMS Settings. Available for niri, Hyprland, and MangoWC. Includes positioning, resolution, refresh rate, VRR, full layout customization (niri), HDR (Hyprland), scaling, mirroring (Hyprland), and more.

### Notification Improvements[​](#notification-improvements "Direct link to Notification Improvements")

![Notification Center](https://danklinux.com/img/blog/v1.2/notiflight.png)![Notification Center](https://danklinux.com/img/blog/v1.2/notifdark.png)

Notification center with history and swipe-to-dismiss.

Notifications get several new features and improvements:

- Configurable history with variable size, expirations, and auto-cleanup
- Gestures to dismiss notifications
- Ability to display on lock screen (count only, name only, or full content - based on privacy preference)

### Cursor & Layout Configuration[​](#cursor--layout-configuration "Direct link to Cursor & Layout Configuration")

![Cursor Control Settings](https://danklinux.com/img/blog/v1.2/cursor-control.png)

Cursor theme, size, and behavior settings.

![Layout Override Settings](https://danklinux.com/img/blog/v1.2/layout.png)

Override gaps, corner radius, and border size.

Customize your compositor settings directly from DMS Settings. Available for niri, Hyprland, and MangoWC:

- **Cursor** - Choose from available cursor themes, adjust size, and configure compositor-specific hiding behavior (hide on typing, hide on touch, inactive timeout)
- **Gaps** - Adjust gaps around windows
- **Borders & Corner Radius** - Override theme defaults for window border width and corner radius
- **Focus Ring** - Customize focus ring color, width, and style

Cursor settings are automatically applied to XWayland applications via XResources, ensuring consistent appearance across native Wayland and XWayland apps.

### DMS Doctor[​](#dms-doctor "Direct link to DMS Doctor")

![DMS Doctor](https://danklinux.com/img/blog/v1.2/doctorlight.png)![DMS Doctor](https://danklinux.com/img/blog/v1.2/doctordark.png)

System check dialog showing service status and optional features.

New `dms doctor` command for diagnosing configuration issues and conflicts that may negatively affect DMS feature availability or performance. Also available via DMS GUI.

Shout out to [@LuckShiba](https://github.com/LuckShiba) for the contribution!

### Keyboard Shortcuts Editor for niri, Hyprland & MangoWC[​](#keyboard-shortcuts-editor-for-niri-hyprland--mangowc "Direct link to Keyboard Shortcuts Editor for niri, Hyprland & MangoWC")

![Keyboard Shortcuts](https://danklinux.com/img/blog/v1.2/bindslight.png)![Keyboard Shortcuts](https://danklinux.com/img/blog/v1.2/bindsdark.png)

Configure keyboard shortcuts with search, filtering, and conflict detection.

The world famous DMS keyboard shortcuts tool is now available for niri, Hyprland, and MangoWC. Search, edit, and add new keybinds directly from DMS Settings.

### Settings Search[​](#settings-search "Direct link to Settings Search")

![Settings Search](https://danklinux.com/img/blog/v1.2/searchlight.png)![Settings Search](https://danklinux.com/img/blog/v1.2/searchdark.png)

Search across all settings to quickly find what you need.

New settings search makes it easier to find what you want to change. Includes integrated launcher search with `?` by default.

### i18n: RTL Support[​](#i18n-rtl-support "Direct link to i18n: RTL Support")

![RTL Language Support](https://danklinux.com/img/blog/v1.2/rtllight.png)![RTL Language Support](https://danklinux.com/img/blog/v1.2/rtldark.png)

DMS Settings displayed in Farsi with full RTL layout support.

DMS 1.2 introduces proper support for right-to-left languages with proper layout mirroring across components. DMS currently has translations for Hebrew and Farsi.

To contribute to translations see the [pinned github issue](https://github.com/AvengeMedia/DankMaterialShell/issues/324)

### Launcher Improvements[​](#launcher-improvements "Direct link to Launcher Improvements")

![Launcher File Search](https://danklinux.com/img/blog/v1.2/launcherlight.png)![Launcher File Search](https://danklinux.com/img/blog/v1.2/launcherdark.png)

Indexed filesystem search with the /path prefix.

The DMS launcher has undergone several improvements. Performance improvements, support for plugins to define context menus (with full keyboard navigation), built-in settings search, and a new first-party plugin for searching keybinds (niri, Hyprland, MangoWC, Sway, and custom providers via `dms keybinds`).

DMS' launcher with plugins supports calculator, niri window management, CLI commands with history, emoji and gitmoji search, web search, extremely fast indexed filesystem search, and more. It also work on the niri overview without any triggers needed.

## Debian SID, OpenSUSE Slowroll, Leap 16.0, and CentOS Stream 10 Packages[​](#debian-sid-opensuse-slowroll-leap-160-and-centos-stream-10-packages "Direct link to Debian SID, OpenSUSE Slowroll, Leap 16.0, and CentOS Stream 10 Packages")

DMS 1.2 expands distribution support with official packages now available for:

- **Debian SID** - Rolling release packages via OBS
- **OpenSUSE Slowroll** - Packages via OBS
- **OpenSUSE Leap 16.0** - Packages via OBS
- **CentOS Stream 10** - Packages via COPR

These are in addition to existing packages for Debian, Ubuntu, Fedora, Arch Linux, and NixOS.

Packages include DMS, niri, quickshell, dgop, dsearch, and other core dependencies. See the [installation guide](https://danklinux.com/docs/getting-started) for setup instructions.

## Upgrade Notes[​](#upgrade-notes "Direct link to Upgrade Notes")

warning

This release contains changes that may require manual intervention.

### (Breaking) Theme Updates[​](#breaking-theme-updates "Direct link to (Breaking) Theme Updates")

Ghostty and VSCode theming have changed and will stop working without manual intervention.

Ghostty & VS Code Theme Changes

**Ghostty**

The theme path has changed to `~/.config/ghostty/themes/danktheme`. Update your Ghostty configuration:

```
# ~/.config/ghostty/config
# Add this
theme= dankcolors

# ! Remove this
# config-file = ./config-dankcolors
```

**VS Code / Codium**

The theme extension needs to be reinstalled due to internal changes:

1. Uninstall the current "Dank material shell theme" extension
2. Reinstall from the extensions marketplace: search for "Dank material shell theme" by "DankLinux"
3. Ctrl+Shift+P -&gt; "Preferences: Color Theme" -&gt; Select "Dynamic Base16 DankShell"
4. Trigger theme re-generation - change theme in DMS Settings or restart DMS
5. Fully exit and restart VSCode

### Clipboard History Migration[​](#clipboard-history-migration "Direct link to Clipboard History Migration")

Steps are recommended to remove existing clipboard history daemon and migrate existing history to the new DMS clipboard system.

Cleanup & Migration Steps

**1. Cleanup old clipboard history integration:**

Remove the `wl-paste --watch cliphist store` daemon/startup from your compositor configuration.

```
// ~/.config/niri/config.kdl
spawn-at-startup "wl-paste --watch cliphist store"// REMOVE THIS LINE
```

```
# ~/.config/hypr/hyprland.conf
exec-once= wl-paste --watch cliphist store # REMOVE THIS LINE
```

**2. Configure DMS clipboard settings (optional):**

Before migrating, you may want to configure your retention settings in DMS Settings -&gt; System -&gt; Clipboard. You can configure maximum entry size, total entries, and retention durations. Only required if you want to override the defaults.

**3. Migrate clipboard history from `cliphist` to DMS:**

Clipboard history will not be automatically migrated from previous versions. You can still access it with the `cliphist` CLI. New clipboard history located in `~/.cache/DankMaterialShell/clipboard/db` - this is a [bbolt](https://github.com/etcd-io/bbolt) database.

To migrate old history:

```
# First stop DMS
systemctl --user stop dms # Or dms kill, if not using systemd
# Run migration (optionally override path with cliphist-migrate /path/to/db)
dms cl cliphist-migrate
# Start DMS again
systemctl --user start dms # or dms run -d, if not using systemd
```

You can then uninstall cliphist and remove the old database at `~/.cache/cliphist/db`

`wl-clipboard` can also be removed, although it's useful to keep for plugins or scripts that depend on it.

```
# DMS clipboard CLI has feature-parity with wl-clipboard
# To copy text:
echo"Hello, World!"| dms cl copy
# To paste text:
dms cl paste
```

### Compositor Configuration Updates[​](#compositor-configuration-updates "Direct link to Compositor Configuration Updates")

For niri or Hyprland you can run `dms setup` to generate a new compositor configuration - monitor configuration will be preserved and original configuration will be backed up. The main change is migrating to a more modular configuration.

Changes are required only if you wish to use the new cursor, output, layout, and keybind controls from DMS Settings.

niri

Required to use GUI cursor and output settings.

1. Create new files

```
mkdir-p ~/.config/niri/dms
touch ~/.config/niri/dms/cursor.kdl
touch ~/.config/niri/dms/outputs.kdl
```

2. Move existing configuration to new files

```
// ~/.config/niri/dms/cursor.kdl
// Move cursor {} block from config.kdl
cursor {
    xcursor-theme "Bibata-Original-Ice"
    xcursor-size 24
}

// ~/.config/niri/dms/outputs.kdl
// Move output {} blocks from config.kdl
output "DP-1"{
    position 00
    scale 1.0
    transform normal
}
```

3. Include new files in your config

```
// ~/.config/niri/config.kdl
// Recommended to place at the end of the file
include "dms/cursor.kdl"
include "dms/outputs.kdl"
include "dms/layout.kdl"
```

Hyprland

Required to use GUI cursor, output, layout, and keybind settings.

1. Create new files

```
mkdir-p ~/.config/hypr/dms
touch ~/.config/hypr/dms/cursor.conf
touch ~/.config/hypr/dms/outputs.conf
touch ~/.config/hypr/dms/layout.conf
touch ~/.config/hypr/dms/binds.conf
```

2. Move existing configuration to new files

```
# ~/.config/hypr/dms/cursor.conf
# Move cursor settings from hyprland.conf
env= HYPRCURSOR_THEME,Bibata-Original-Ice
env= HYPRCURSOR_SIZE,24
env= XCURSOR_THEME,Bibata-Original-Ice
env= XCURSOR_SIZE,24

# ~/.config/hypr/dms/outputs.conf
# Move monitor lines from hyprland.conf
monitor = DP-1,2560x1440@144,0x0,1

# ~/.config/hypr/dms/layout.conf
# Move general layout settings from hyprland.conf
general {
    gaps_in =5
    gaps_out =10
    border_size =2
}

# ! Binds do not need to be moved, only edited/new binds via GUI will be stored here
```

3. Source new files in your config

```
# ~/.config/hypr/hyprland.conf
# Recommended to place at the end of the file
source= ./dms/cursor.conf
source= ./dms/outputs.conf
source= ./dms/layout.conf
source= ./dms/binds.conf
```

MangoWC

Required to use GUI cursor, output, layout, and keybind settings.

1. Create new files

```
mkdir-p ~/.config/mangowc/dms
touch ~/.config/mangowc/dms/cursor.conf
touch ~/.config/mangowc/dms/outputs.conf
touch ~/.config/mangowc/dms/layout.conf
touch ~/.config/mangowc/dms/binds.conf
```

2. Move existing configuration to new files

```
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

3. Source new files in your config

```
# ~/.config/mangowc/mangowc.conf
# Recommended to place at the end of the file
source= ./dms/cursor.conf
source= ./dms/outputs.conf
source= ./dms/layout.conf
source= ./dms/binds.conf
```

### NixOS Updates[​](#nixos-updates "Direct link to NixOS Updates")

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

- Added support for config includes with niri-flake. DMS-generated configuration files now work seamlessly with niri's flake-based setup

**Plugin Registry Flake**

- New [dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry) Nix flake provides all community plugins as packages
- Plugins are automatically updated daily from the registry
- Simple declarative installation - just enable plugins by their ID
- Works with both NixOS and Home Manager modules

note

The DMS Flake options name was now changed from `programs.dankMaterialShell` to `programs.dank-material-shell`. The modules names also changed. While the old module names will still work, you'll receive a deprecation warning informing about the new name.

info

The documentation for the [nixpkgs module](https://danklinux.com/docs/dankmaterialshell/nixos) will get updated as soon as DMS 1.2 gets into `nixos-unstable`.

Please check [the documentation](https://danklinux.com/docs/dankmaterialshell/nixos-flake) for more information in how to configure DMS 1.2 with the new features.

## Bug Fixes and Improvements[​](#bug-fixes-and-improvements "Direct link to Bug Fixes and Improvements")

|- View Details (300+ commits) -|

Since the v1.0 release, DMS has received extensive bug fixes and stability improvements across all components:

**Clipboard**

- Native clipboard and history implementation with zero external dependencies
- Add cliphist-migrate CLI for importing existing history
- Add shift+enter to paste from clipboard history modal
- Configurable persistence, mime-type handling, and auto-cleanup
- Automatically ignore sensitive mime types from password managers
- Fix mime type selection and nil offer handling

**Bar & Dock**

- Add shadow option for bars
- Add scroll wheel behavior configuration
- Add bar get/setPosition IPC
- Improve high-DPI scrolling logic
- Fix exclusive zone popup positioning
- Fix reveal on overview/niri when auto-hide enabled
- Fix tooltip positioning with adjacent bars
- Improve pinned app re-ordering feedback
- Make control center widget per-instance
- Add option to show bar when hidden and no windows
- Respect compact mode on vertical bar
- Mouse wheel options for media player widget
- Fix widget base hover blend logic
- Add isolate running apps by display option

**Desktop Widgets & Plugins**

- New desktop widget plugin type with draggable per-monitor widgets
- Built-in clock and system monitor desktop widgets
- Add grid/grid size hints for widget positioning
- Add overlay IPC and overview option
- Enable desktop plugins by default
- Fix widget display toggle and key event handling
- Centralize config in desktop widgets tab
- Add niri overview only option
- Persistent plugins with async updates
- Fix first plugin install reactivity
- Hide uninstall/update buttons for system plugins
- IPC visibility conditions for plugins

**Display & Monitor Configuration**

- Add configurator for niri, Hyprland, and MangoWC
- Configure position, VRR, orientation, resolution, refresh rate
- Add Hyprland HDR options
- Add niri-specific layout options
- Add mirroring option for Hyprland
- Add disable output option for Hyprland
- Fix reverted state for position
- Fix text-alignment in model mode
- Explicitly write scale 1 for niri
- Add adaptiveSyncSupported to wlroutput API

**Notifications**

- Add configurable persistent history with variable size and expiration
- Add swipe to dismiss functionality
- Add support for lock screen display (count, app name, or full detail)
- Add compact mode with expansion in history and popup
- Add image persistence
- Right-click to toggle Do Not Disturb
- Add Do Not Disturb to IPC
- Add modal function for clearing all notifications
- Fix notifications being transient when history disabled
- Fix redundant height animation and spacing improvements
- Minimize rapid window creation/destruction

**Themes & Matugen**

- Theme registry with community themes and variants
- Support for accent colors and theme variants
- Add color reload capability to VSCode theme
- Add GTK theme method and fix light mode
- Move Ghostty theming to new path
- Add Zen Browser template
- Add gruvbox material custom theme varieties
- Add neovim to matugen pipeline with soothing theme
- Fix adw-gtk3 setting in light mode
- Set cursor color for themes
- Fix terminals always dark with custom themes
- Update VSCode template with improved highlighting

**Cursor & Layout**

- DMS Cursor Control for size and theme in niri
- Create/update XResources for XWayland apps
- Add Hyprland and MangoWC cursor config support
- Add GUI gaps, window radius, and border overrides
- Support for niri, Hyprland, and MangoWC layouts

**Launcher**

- Built-in settings search plugin with ? trigger
- Support for plugins to define context menus
- Add ID search fallback for non-English apps
- Allow terminal apps
- F10 as alt for menu key
- Optimize bindings and filters
- Fix invalid icon rendering

**Settings**

- Add search across all settings
- Add doctor command with GUI integration
- Add battery charge limit setting
- Add lock screen layout settings
- Add volume and brightness percentages
- Fix desktop widget accordion row height
- Fix generic color selector clipping
- Fix theme application of default-settings
- Guard saving before load completed
- Make default height screen-aware
- Read-only handling refactor

**Network & VPN**

- Support hidden SSIDs
- Listen to NetworkManager wired interface
- Use nmcli for route metrics
- Right-click VPN widget to quick connect
- Aggregate VPN import errors with toast details
- Support pkcs11 prompts
- Cache pkcs11 pin input

**Keyboard & Input**

- Initial support for writable Hyprland and MangoWC keybinds
- Add media control bindings for audio playback
- Fix keybind handling of cooldown-ms parameter
- Fix empty string args and screenshot-window options
- Add log if ShortcutInhibitor is missing
- Accept numpad enter key for screenshot selection

**Lock Screen & Power**

- Add fade to monitor off option
- Clear lock screen textbox on Escape
- Handle case where session lock is rejected
- Fix font alignment
- Add PAM login fallback
- Fade to lock and monitor off by default

**Audio & Media**

- Recreate media players on pipewire device change
- Add option to disable visualizer in bar widget
- Add scroll wheel behavior configuration
- Allow adjusting notification volume
- Larger option for media player widget

**i18n & RTL**

- Initial RTL support for notifications, settings, control center, launcher
- Fix RTL alignment of settings sidebar and plugin settings
- Add Farsi and Hungarian translations
- General term cleanup and sync

**niri**

- Add gaps and radius override
- Add warnings on auto-generated files
- Fix effectiveScreenAssignment in modal
- Fix gap reactivity
- Handle window urgency event
- Preserve remaining settings when turning off output
- Release focus for popouts on overview
- Track open modals for focus transfers
- Hack for config includes with niri flake

**Hyprland**

- Always use single window mode
- Fix cursor setting
- Change DPMS off to DPMS toggle
- Update reference config for 0.53
- Smart compositor entry point detection

**Core & Backend**

- Add resolve-include recursive functionality
- Add test coverage for wayland stack with race detection
- Mock wayland context for tests
- Detect quickshell crash on SIGTERM
- Exit non-zero on SIGUSR1 for systemd restart
- Preserve quickshell exit code
- Fix socket reported CLI version
- Use stdlib for XDG dirs
- Implement screensaver interface for idle inhibitor
- Poll with wake pipe instead of read deadlines

**Greeter**

- Change Hyprland startup to exec-once
- Use FolderListModel for session iteration
- Add launch timeout
- Simplify start-hyprland check
- Fix per-monitor and per-mode wallpapers (NixOS)

**Wallpaper**

- Add seconds to wallpaper cycling
- Pause cycling when locked
- Encode image URIs
- Clamp max texture size
- Scale texture to physical pixels

**Build & Distribution**

- Debian SID, OpenSUSE Slowroll, Leap 16.0, CentOS Stream 10 packages
- Ubuntu ARM64 support
- Artix Linux and Void Linux widget mappings
- Remove cliphist dependency on dms-git
- OBS and PPA automation improvements
- NixOS module refactoring and fixes

**Miscellaneous**

- Add welcome page with doctor integration for first launch
- Configurable app ID substitutions
- Map steam\_app\_ID to steam\_icon\_ID for game icons
- Flatpak introspection utilities
- Detect flatpak installations of Zen Browser and Vesktop
- Fix touchpad scrolling behavior
- Add group workspace apps toggle
- Reverse workspace scrolling option
- Add hide option for updater widget
- Use volume\_mute icon for volume==0

## Resources[​](#resources "Direct link to Resources")

[Get Started with DMS →](https://danklinux.com/docs/getting-started)

![niri](https://danklinux.com/img/niri.svg)Special thanks to [YaLTeR](https://github.com/YaLTeR) for collaborating with the DMS team, for [niri](https://github.com/YaLTeR/niri) - the compositor that inspired DMS, and for hosting DMS on the [niri Discord](https://discord.gg/ppWTpKmPgT).

## Thank You

To everyone who has supported DMS through feedback, contributions, sponsorships, donations, and packaging.

Zan, Zendegi, Azadi