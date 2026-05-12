---
title: DMS 1.4 "Saffron Bloom" Released
url: https://danklinux.com/blog/v1-4-release
source: sitemap
fetched_at: 2026-04-26T08:35:09.742517794-03:00
rendered_js: false
word_count: 3627
summary: This document details the features and improvements introduced in DankMaterialShell version 1.4, including a new launcher, enhanced plugin support via DBus, system monitoring, and refined desktop management tools.
tags:
    - release-notes
    - linux-desktop
    - software-update
    - plugin-system
    - ui-customization
    - system-utilities
category: other
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

DankMaterialShell (DMS) 1.4 "Saffron Bloom" introduces a brand new launcher, numerous plugin system improvements enabling GIFs, KDE Connect, Clight, and new possibilities for extending DMS.

**Stats:** 3,100+ commits | 4.3k+ GitHub Stars | 130+ Contributors | 70 Plugins

## Dank Launcher V2

![Dank Launcher V2](https://danklinux.com/img/blog/v1.4/launcher_dark.png)

DMS 1.4 introduces a vicinae-inspired launcher with more options, tighter extension integrations, better performance, configurable tab-actions, a new tiled layout option, and new first-party plugins including GIF and Sticker search.

- Plugins can define context menu and custom tab actions, shift+enter action (such as paste-and-close), and new result types like animated images
- New tiled layout option for the launcher
- New first-party plugins: GIF and Sticker search
- Hide or show any extension from "all" tab, change priority-order, keep custom triggers, and configure more launcher options in DMS settings
- Edit launch options, environment, or hide entries inline from the launcher

## KDE Connect+Valent (Phone Connect), and Clight Integration

DMS v1.4 exposes a DBus client enabling plugins to interact with DBus services natively, which has enabled the development of KDE Connect+Valent and Clight plugins.

![KDE Connect and Valent integration](https://danklinux.com/img/blog/v1.4/kdeconnect_dark.png)

[Phone Connect](https://github.com/AvengeMedia/dms-plugins/tree/master/DankKDEConnect) plugin allows connecting to a phone via KDE Connect or Valent directly from DMS. Receive notifications, send and receive files, synchronize clipboard, view phone battery percentage in the bar, and more.

[Clight](https://github.com/AvengeMedia/dms-plugins/tree/master/DankClight) plugin integrates with [Clight](https://github.com/FedeDP/Clight), an auto-brightness daemon.

The DBus client enables a new category of plugins that can interact with any DBus service in an efficient, event-driven way.

## New Process List/System Monitor

![New System Monitor](https://danklinux.com/img/blog/v1.4/sysmon_dark.png)

The [[086-docs-dgop]] frontend/process monitor has been overhauled with a new, more functional design. Integrated search, full command view, and more relevant information in a single view.

## Window Rule Manager (niri-only)

niri users can manage window rules directly from DMS. An optional keybind `dms ipc call window-rules toggle` creates a rule for the currently focused window. All rules can be re-ordered, edited, and managed from DMS settings.

![Window Rules settings](https://danklinux.com/img/blog/v1.4/windowrulesettings_dark.png)

![New Window Rule modal](https://danklinux.com/img/blog/v1.4/windowrulemodal_dark.png)

### Intelligent Auto-Hide

The dock can auto-hide itself only when floating windows overlap its area, and reveal when they do not. Screen space is recovered when needed without losing quick access.

### Dank Bar Apps Dock Widget

![Dank Bar Apps Dock Widget settings](https://danklinux.com/img/blog/v1.4/dms_apps_dock_widget_dark.png)

New Apps Dock widget for Dank Bar — a standalone dock embedded directly in the bar for pinned and running apps when using a panel-only workflow.

### Max Pinned & Running Apps with Overflow

![Dock overflow and behavior settings](https://danklinux.com/img/blog/v1.4/dms_dock_pinned_running_apps_dark.png)

Set max counts for pinned and running apps separately. Anything beyond the limit collapses into an expandable overflow area with a badge count. Works on both the main dock and the new Apps Dock widget.

## Audio Device Aliases

![Audio Device Aliases](https://danklinux.com/img/blog/v1.4/audio_device_aliases_dark.png)

Built-in Audio Device Aliases powered by WirePlumber. Rename any input or output from Audio Settings, hide unused devices, and push a device above 100% temporarily when needed.

- **Rename devices** — Give devices useful names; original hardware names are preserved
- **Hide devices** — Remove unused or duplicate entries from lists
- **Amplify beyond 100%** — Bump max volume when needed; use caution as excessive amplification may cause distortion

## Automatic Light and Dark Mode

![Automatic Light and Dark Mode](https://danklinux.com/img/blog/v1.4/automatic_light_dark_mode_dark.png)

Automatic theming with time and location-based transitions, plus Gamma Control sync.

- **Time-based mode** — Set sunrise/sunset or custom times
- **Location-based mode** — Manual coordinates or IP geolocation to calculate local sunrise/sunset
- **Gamma Control sync** — Tie into DMS Gamma Control Night Mode so color temperature, brightness, and theme all switch together
- **Quick override** — Force light or dark from the Appearance menu anytime; automatic rules kick back in after

## Notification Enhancements

![Notification Toasts](https://danklinux.com/img/blog/v1.4/notification_toast_dark.png)

![Notification Center](https://danklinux.com/img/blog/v1.4/notification_center_dark.png)

Notifications received a visual overhaul based on Material 3 Expressive — new shadows, motion, and overall feel.

What's new:
- **Independent animation speed** — Notification animations are separate from global UI motion
- **Privacy mode** — Hide message content by default (shows sender and app only), click to reveal
- **Right-click actions** — Right-click any notification to Mute the source, Create a rule, or Dismiss

## Miracle WM Support

![Miracle WM](https://danklinux.com/img/miraclewm.svg)

DMS 1.4 brings full support for [Miracle WM](https://miracle-wm.org/), including keybind cheatsheets, idle monitor integration, workspace switcher, and the rest of the core DMS feature.

Ahead of the upcoming Fedora 44 release which will include a [Dank Miracle spin](https://www.phoronix.com/news/Fedora-44-Dank-MiracleWM), Miracle WM users on Fedora will have DMS available out of the box.

## Available Distributions

DMS is available for Arch Linux, Fedora, openSUSE, Debian, Ubuntu, CentOS, NixOS, Gentoo, and more.

Gentoo users have three community overlays:
- [quilat-overlay](https://github.com/Graght/quilat-overlay) — live ebuild tracking git master, OpenRC + systemd
- [tdgentoo](https://github.com/timdodge/tdgentoo) — versioned ebuild pinned to stable releases
- [dacyberduck](https://codeberg.org/dacyberduck/gentoo-overlay) — `dank-base/dankmaterialshell`

See the [[003-docs-getting-started]] for setup instructions.

## Bug Fixes and Improvements

Since the v1.2 release, DMS has received extensive bug fixes and stability improvements across all components:

**Launcher V2**
- New aggregated "all" tab with plugin/extension results, quick tab actions, and tile mode
- Improved search result responsiveness with highlighted matches
- General performance optimizations including ListView in all tab, filesystem cache for faster first launch
- De-duplicate cached entries by ID
- Support async launcher plugins, cached GIFs, and paste-on-action
- Allow categories in plugins, plugin sort order preference
- Allow disabling each plugin from "all" mode, add IPCs for toggling specific modes
- Add visibility guards, micro size option, and view mode persistence
- Context menu and keyboard navigation improvements
- Fix hover effect, state reset on section changes, dGPU race condition, and plugin icon handling
- Support ScreenCopy in tiles and CachingImage in icon renderer
- Add name, icon, description overrides and hide/unhide options for entries
- Retire spotlight launcher in favor of Dank Launcher V2

**Notifications**
- Refactor notification animations with Material 3 Expressive design
- Add configurable notification rules
- Add left/right keyboard navigation to Current/History tabs
- Cap max animation speed in popout
- Fix crash in modal and keyboard navigation on history tab close
- Update dimensions, text expansion logic, and group expansion card animations
- Handle material icons; tweak toast button padding

**Dock & Bar**
- Intelligent dock auto-hide behavior
- Apps Dock widget for Dank Bar with overflow and configuration options
- Implement Dank Launcher button on the Dock with custom icons/logos
- Pinnable DMS core apps with color options
- Max pinned and running apps with overflow badge count
- Fix intelligent auto-hide on Hyprland
- Resolve icons for pre-substituted app IDs
- Fix option to use custom logos and launcher button persistence
- Fix spacing at scale of running apps, dock, and system tray
- Add click-through option for Dank Bar; fix centering of numerous bar widgets
- Fix property preservation in widgets; enlarge bar icons if widget background is off
- Account for outlineThickness in margin settings; fix widget context focus with autohide enabled

**Clipboard**
- Save pinned clipboard entries with keyboard navigation
- Add popout variant for clipboard widget
- Add option to paste on Enter
- Add `cl copy --download` option for images/videos with portal file transfer
- Add `watch -m` for mime-types
- Fix row layout overflow, pinned entry logic, hash duplication check
- Fix file transfer and export functionality with Flatpak read grants
- Skip `application/vnd.portal.filetransfer` mime in history
- React to changes; fix duplicate clear dialog
- Touch copied history entry to move it to the top; add raw image mime-type to offers in CopyFile
- Fix watch command; quick context menu for clipboard widget

**Themes & Appearance**
- Automatic light and dark mode based on region/time of day with transition time
- Improve handling of custom themes with variants and accents in light/dark mode
- Support matugen v4; sync adwaita accent color by visual similarity
- Add Cosmic light/dark and icon theming support; allow overriding color center theme
- Fix popup transparency setting and overflow of option button groups
- Fix emacs template for both light and dark themes; add dank emacs template
- Fix Zen Browser theme background color in template
- Fix terminals always dark with custom themes
- Post-hook reload GTK4 and qt6ct after matugen changes; do not signal terminals when disabled
- Update dank16 algorithm for smoother gradients; fix Vesktop theme name

**Audio & Media**
- Audio device aliases: rename, hide, and amplify devices via WirePlumber
- Media playback OSD with updated design; add per-device max volume limit setting
- Configurable volume amount on scroll for media widget
- Add player-specific MPRIS volume control via IPC
- Reverse media playback icons and handle screen changes
- Fix volume OSD sliding UI update for vertical layout
- Track art: use URLs directly; Cava: use input source pipewire and auto, remove input config

**Display & Monitor Configuration**
- Support for multiple output profiles with delete/hide disconnected displays
- Add full screen only option for Hyprland, convert VRR to dropdown
- Add disable snap option in display settings
- Fix VRR=0 setting on Hyprland
- Fix dropped disconnected displays on save; fix preview centering with scaling
- Update MangoWC display config syntax

**Window Rules (niri)**
- Settings UI for creating, editing, deleting, and reordering window rules
- IPC to create a window rule for the currently focused toplevel
- Fix checkbox alignment; update default Steam window rules

**Animations**
- Material Animation Refactor based on Material 3 Expressive
- Fine-grained animation settings for modals and popouts
- Revise ListView animations and tweak list view transitions
- Switch to frame animation for kinetic scroll; clean up ripple effect and apply more universally
- Optimize VRAM usage in DankRipple

**Process List & System Monitor**
- Overhaul system monitor popout and app with new design
- Add full keyboard navigation to process list
- Fix clipped graphs; fix default popout focus and default sort direction
- Update gauge sizes; disable animations until list is stable
- Fix Process List popout crash from AppSearch

**Workspace**
- Add workspace rename dialog
- Drag-and-drop workspace reordering for niri; display niri workspace names
- Fix occupied color override; fix overflow with grouped apps and icons
- Fix index numbers with show apps on vertical bar with animation; add icon size offset

**Settings**
- DankCollapsible component
- Optimize sidebar bindings and sidebar scaling improvements
- Settings search index updates
- Fix wallpaper cycle buttons, theme flavor buttons, power and sleep tab button groups
- Make dock position match Dank Bar settings; drop beta from configuration label
- Do not clear caches or apply on startup; fix modal not opening on latest quickshell

**Lock Screen & Greeter**
- DMS Greeter sync with niri include settings (cursor, debug, input, options)
- Fix keyboard layout on Hyprland; add lock at startup action
- Add disable media player option on lock screen
- Remove random facts from greeter and lock; add option to hide profile image
- Fix 12-hour format single digit hours; power off monitors when lock screen activates
- Add support for Debian greetd user/group name
- MangoWC and Scroll Greeter support for NixOS; restore baseline configs and fix Cosmic support
- Add niri override kdl includes; fix greeter directory permissions

**Plugins**
- Add plugin state helpers and toggle support with lazy daemon instantiation
- Give popout customizable header actions; fix reload IPC on failure
- Ensure daemon plugins not instantiated twice; represent featured plugins in built-in browsers
- Fix first plugin install reactivity and confirm third-party repo window

**niri**
- Expose when-locked, inhibited, repeat options through GUI keybind editor
- Support any screenshot editor tool; add ensure colors.kdl existence
- Restore lazy overview spotlight lifecycle to reduce idle VRAM
- Replace github ref; add screencast indicator

**Network & VPN**
- Add support for GlobalProtect VPN using SAML auth flow
- Simplify connection handling; fix VPN popout and widget tooltip positions
- Uncheck "save password" by default

**Wallpaper**
- Support more image formats with case insensitivity
- Only pause cycling when screen is locked or active window is fullscreen
- Fix per-monitor view modes

**Keybinds**
- Do not pass dirs in keybinds; fix MangoWC config traversal in provider

**Widgets**
- Add button color setting and theme text field selection color
- Cleanup rectangles across popouts, modals, OSDs; remove double rectangle artifact in popouts
- Fix cross-monitor handling of widgets
- Notepad widget with quick context menu, cursor color, and QOL updates
- Refresh layout on plugin load; add fallback for Steam app widgets

**i18n**
- General RTL fixes across settings, about tab, and Dank Bar
- Capture missing strings and wrap in I18n.tr()
- Multiple term updates and sync

**Core & Backend**
- Add generic DBus service with QML client (subscribe/introspect/getprop/setprop/call)
- DMS Chroma syntax highlighter for Notepad
- Set Qt platform to wayland;xcb by default
- Add DL helper and gsettingsOrDconf helpers; add screensaver introspect XML methods
- Replace go-localereader directive
- Add IPC handlers for color picker modal and tray icon control; add toast IPCs
- Fix DMS chroma hang on print
- More intelligent Xresources editing for cursor
- Doctor: add cups-pk-helper, MangoWC, labwc; use DBus for service checks; add --copy option
- Polkit: allow empty passwords
- System tray: allow re-ordering items, use id+title as identifier

**Compositor Support**
- Add Miracle WM support; labwc patch improvements
- MangoWC and Scroll Greeter support

**Build & Distribution**
- Deprecate cliphist dependencies
- Update NixOS packaging, vendorHash, and home module
- Support specifying systemd target for NixOS; add qt-imageformats to DMS QML dependencies for NixOS
- Fix Fedora version format and dynamic versioning; update OBS workflows and Makefile
- Support XeroLinux via dankinstall; update Go version and golangci-lint in CI

## Resources

[[003-docs-getting-started|Get Started with DMS]]

Special thanks to [YaLTeR](https://github.com/YaLTeR) for collaborating with the DMS team, for [niri](https://github.com/niri-wm/niri) — the compositor that inspired DMS, and for hosting DMS on the [niri Discord](https://discord.gg/ppWTpKmPgT).

## Thank You

To everyone who has supported DMS through feedback, contributions, sponsorships, donations, and packaging.

Zan, Zendegi, Azadi
