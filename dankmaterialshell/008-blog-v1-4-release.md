---
title: DMS 1.4 "Saffron Bloom" Released
url: https://danklinux.com/blog/v1-4-release
source: sitemap
fetched_at: 2026-02-22T18:42:08.491468-03:00
rendered_js: false
word_count: 1079
summary: This document announces the release of DankMaterialShell 1.4, detailing new features such as a revamped launcher, expanded plugin capabilities, and improved system integration tools.
tags:
    - dankmaterialshell
    - release-notes
    - linux-desktop
    - desktop-environment
    - plugin-system
    - wayland
    - user-interface
category: other
---

We're excited to announce DankMaterialShell (DMS) 1.4 "Saffron Bloom"! This release introduces a brand new launcher, numerous improvements to the plugin system which enables GIFs, KDE Connect, Clight, and a lot of new possibilities for extending DMS features and capabilities.

3,100+Commits

4.3k+GitHub Stars

130+Contributors

70Plugins

## Dank Launcher V2[​](#dank-launcher-v2 "Direct link to Dank Launcher V2")

![Dank Launcher V2](https://danklinux.com/img/blog/v1.4/launcher_dark.png)

The new Dank Launcher V2 with tiled layout and plugin integrations.

DMS 1.4 introduces a new vicinae-inspired launcher, with many more options, tighter extension integrations, better performance, configurable tab-actions, new tiled layout option, and numerous new first-party plugins including GIF and Sticker searchs.

- Plugins can define context menu and custom tab actions, shift+enter action (such as paste-and-close), and new types of results such as animated images.
- New tiled layout option for the launcher.
- New first-party plugins including GIF and Sticker search.
- Hide or show any extension from "all" tab, change priority-order, keep custom triggers, and configure more launcher options in DMS settings.
- Edit launch options, environment, or hide entries inline from the launcher.

## KDE Connect+Valent (Phone Connect), and Clight Integration[​](#kde-connectvalent-phone-connect-and-clight-integration "Direct link to KDE Connect+Valent (Phone Connect), and Clight Integration")

DMS v1.4 exposes a dbus client that enables plugins to interact with dbus services natively, which has enabled the development of KDE Connect+Valent and Clight plugins.

![KDE Connect and Valent integration](https://danklinux.com/img/blog/v1.4/kdeconnect_dark.png)

Phone Connect via KDE Connect / Valent.

[Phone Connect](https://github.com/AvengeMedia/dms-plugins/tree/master/DankKDEConnect) plugin allows you to connect to your phone via KDE Connect or Valent (gnome-based equivalent) directly from DMS. Receive notifications, send and receive files, synchronize clipboard, view phone battery percentage in the bar, and more.

[Clight](https://github.com/AvengeMedia/dms-plugins/tree/master/DankClight) plugin gives integration with [Clight](https://github.com/FedeDP/Clight) which is an auto-brightness daemon.

The new dbus client allows creating an entirely new category of plugins that can interact with any dbus service, which opens up a huge range of possibilities for extensions that need to integrate with other applications and system services - in an efficient, event-driven way.

## New Process List/System Monitor[​](#new-process-listsystem-monitor "Direct link to New Process List/System Monitor")

![New System Monitor](https://danklinux.com/img/blog/v1.4/sysmon_dark.png)

The new built-in System Monitor with process list.

The [dgop](https://danklinux.com/docs/dgop/) frontend/process monitor has gotten an overhaul with a new, more functional design. Integrated search, full command view, and more relevant information in a single view.

## Window Rule Manager (niri-only)[​](#window-rule-manager-niri-only "Direct link to Window Rule Manager (niri-only)")

niri users can now manage window rules directly from DMS. An optional keybind can be used `dms ipc call window-rules toggle` to create a rule for the currently focused window. All rules can be re-ordered, edited, and managed from DMS settings.

![Window Rules settings](https://danklinux.com/img/blog/v1.4/windowrulesettings_dark.png)

![New Window Rule modal](https://danklinux.com/img/blog/v1.4/windowrulemodal_dark.png)

Window Rules settings and the rule creation modal.

### Intelligent Auto-Hide[​](#intelligent-auto-hide "Direct link to Intelligent Auto-Hide")

The dock can now auto-hide itself only when floating windows overlap its area, and reveal when they don't. You get the screen space back when you need it without losing quick access.

### Dank Bar Apps Dock Widget[​](#dank-bar-apps-dock-widget "Direct link to Dank Bar Apps Dock Widget")

![Dank Bar Apps Dock Widget settings](https://danklinux.com/img/blog/v1.4/dms_apps_dock_widget_dark.png)

Configure the standalone Apps Dock widget with overflow options and visual effects.

New Apps Dock widget for Dank Bar — a standalone dock embedded directly in the bar. If you prefer a panel-only workflow without the full dock, this gives you pinned and running apps right in your bar.

### Max Pinned & Running Apps with Overflow[​](#max-pinned--running-apps-with-overflow "Direct link to Max Pinned & Running Apps with Overflow")

![Dock overflow and behavior settings](https://danklinux.com/img/blog/v1.4/dms_dock_pinned_running_apps_dark.png)

New dock behavior controls including max apps and overflow settings.

You can now set max counts for pinned and running apps separately. Anything beyond the limit collapses into an expandable overflow area with a badge count. Works on both the main dock and the new Apps Dock widget.

## Audio Device Aliases[​](#audio-device-aliases "Direct link to Audio Device Aliases")

![Audio Device Aliases](https://danklinux.com/img/blog/v1.4/audio_device_aliases_dark.png)

Rename, hide and (optionally) amplify audio devices directly from DMS.

Built-in Audio Device Aliases powered by WirePlumber. Rename any input or output from Audio Settings, hide devices you never use, and if needed — push a device above 100% temporarily. Original names are kept so you can always revert.

- **Rename devices:** Give your devices actual useful names. Original hardware names are preserved.
- **Hide devices:** Get rid of unused or duplicate entries cluttering your lists.
- **Amplify beyond 100%:** Bump max volume when you need it. **Note:** excessive amplification may cause distortion or hardware issues, use with caution.

## Automatic Light and Dark Mode[​](#automatic-light-and-dark-mode "Direct link to Automatic Light and Dark Mode")

![Automatic Light and Dark Mode](https://danklinux.com/img/blog/v1.4/automatic_light_dark_mode_dark.png)

Automatic theming with time and location-based transitions, plus Gamma Control sync.

Your desktop theme can now switch between light and dark automatically. Set a simple time schedule, or let DMS figure it out from your location (manual coordinates or IP-based). Location mode shows a preview of when the next transition will happen.

- **Time-based mode:** Set sunrise/sunset or custom times.
- **Location-based mode:** Manual coordinates or IP geolocation to calculate local sunrise/sunset.
- **Gamma Control sync:** Tie it into DMS Gamma Control Night Mode so color temperature, brightness, and theme all switch together.
- **Quick override:** Force light or dark from the Appearance menu anytime; automatic rules kick back in after.

## Notification Enhancements[​](#notification-enhancements "Direct link to Notification Enhancements")

![Notification Toasts](https://danklinux.com/img/blog/v1.4/notification_toast_dark.png)

![Notification Center](https://danklinux.com/img/blog/v1.4/notification_center_dark.png)

Notification toasts (left) and the redesigned Notification Center (right).

Notifications got a visual overhaul based on Material 3 Expressive — new shadows, motion, and overall feel. The notification center and toasts both look and behave better.

What's new:

- **Independent animation speed:** Notification animations are now separate from global UI motion, so you can make them snappier or slower without touching everything else.
- **Privacy mode:** Hide message content by default (shows sender and app only), click to reveal. Useful if you share your screen or just want less distraction.
- **Right-click actions:** Right-click any notification to Mute the source, Create a rule, or Dismiss. Works on both toasts and in the Notification Center.

More updates to come!

## Miracle WM Support[​](#miracle-wm-support "Direct link to Miracle WM Support")

![Miracle WM](https://danklinux.com/img/miraclewm.svg)

[Miracle WM](https://miracle-wm.org/) is now a supported compositor.

DMS 1.4 brings full support for [Miracle WM](https://miracle-wm.org/), including keybind cheatsheets, idle monitor integration, workspace switcher, and the rest of the core DMS feature.

This is ahead of the upcoming Fedora 44 release which will include a [Dank Miracle spin](https://www.phoronix.com/news/Fedora-44-Dank-MiracleWM), so Miracle WM users on Fedora will have DMS available out of the box.

## Available Distributions[​](#available-distributions "Direct link to Available Distributions")

DMS is available for Arch Linux, Fedora, openSUSE, Debian, Ubuntu, CentOS, NixOS, Gentoo, and more. Gentoo users have three community overlays to choose from: [quilat-overlay](https://github.com/Graght/quilat-overlay) (live ebuild tracking git master, OpenRC + systemd), [tdgentoo](https://github.com/timdodge/tdgentoo) (versioned ebuild pinned to stable releases), and [dacyberduck](https://codeberg.org/dacyberduck/gentoo-overlay) (`dank-base/dankmaterialshell`).

See the [installation guide](https://danklinux.com/docs/getting-started) for setup instructions.

## Bug Fixes and Improvements[​](#bug-fixes-and-improvements "Direct link to Bug Fixes and Improvements")

|- View Details (200+ commits) -|

## Resources[​](#resources "Direct link to Resources")

[Get Started with DMS →](https://danklinux.com/docs/getting-started)

![niri](https://danklinux.com/img/niri.svg)Special thanks to [YaLTeR](https://github.com/YaLTeR) for collaborating with the DMS team, for [niri](https://github.com/niri-wm/niri) - the compositor that inspired DMS, and for hosting DMS on the [niri Discord](https://discord.gg/ppWTpKmPgT).

## Thank You

To everyone who has supported DMS through feedback, contributions, sponsorships, donations, and packaging.

Zan, Zendegi, Azadi