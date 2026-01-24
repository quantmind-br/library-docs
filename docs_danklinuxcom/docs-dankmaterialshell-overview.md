---
title: Overview & Architecture | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/overview
source: sitemap
fetched_at: 2026-01-24T13:33:52.353621305-03:00
rendered_js: false
word_count: 449
summary: This document introduces DankMaterialShell, a Wayland desktop shell built with Quickshell and Go, outlining its feature set, client-server architecture, and system integration methods.
tags:
    - wayland-shell
    - quickshell
    - desktop-environment
    - linux-desktop
    - system-integration
    - go-backend
    - user-interface
category: guide
---

```
██████╗ ███╗   ███╗███████╗
██╔══██╗████╗ ████║██╔════╝
██║  ██║██╔████╔██║███████╗
██║  ██║██║╚██╔╝██║╚════██║
██████╔╝██║ ╚═╝ ██║███████║
╚═════╝ ╚═╝     ╚═╝╚══════╝
```

DankMaterialShell (dms) is a Wayland desktop shell built with [Quickshell](https://quickshell.org/) and [Go](https://go.dev/). It serves a purpose similar to GNOME Shell or KDE Plasma, providing a unified interface for launching applications, managing windows, managing hardware interfaces, notifications, and much more.

## General Features[​](#general-features "Direct link to General Features")

- Launcher (Apps, file search, web search, emoji search, calculations, and extendable with plugins)
- System Tray
- Notifications with grouping support
- Network Management (via NetworkManager, iwd, systemd-networkd, or some hybrid setups)
- VPN Management (via NetworkManager)
- Bluetooth Management (via BlueZ)
- Audio Management (via PipeWire)
- Idle & Power Management
- Brightness controls (Backlight, LEDs, and i2c/ddc)
- Lock Screen
- Process & System Monitoring
- Theming (Light, Dark, Automatic Colors, Premade themes, and Custom Accent Colors)
- Multi-monitor support
- Gamma control (night mode)
- Wallpaper management with transitions, multi-monitor support, and automatic transitioning.
- Clipboard history manager
- System sounds (such as notifications, volume changes, etc.)
- Mpris media controls with audio visualization
- Browser picker modal for URL handling with default browser selection
- Dozens of widgets and plugins available to allow virtually any feature you can imagine.

*There's really too much to list, but those are some of the highlights!*

## Architecture[​](#architecture "Direct link to Architecture")

DankMaterialShell uses a client-server architecture where a Go backend (`dms`) manages system integrations and spawns the Quickshell-based UI as a child process. Communication happens over Unix socket using REQ/REP and PUB/SUB patterns.

**Key Points:**

- **dms** spawns **Quickshell** as a child process
- **dms** and **Quickshell** both integrate with Wayland and D-Bus APIs independently
- **dms** fills gaps that Quickshell doesn't handle natively
- Communication between QML app and dms backend happens via Unix socket

### Component Overview[​](#component-overview "Direct link to Component Overview")

ComponentRole**DankMaterialShell - Quickshell**Frontend powering widgets, modals, and user experience.**DankMaterialShell - Backend (cli)**Bridges DBus, Wayland, and plugin APIs - also a management CLI**dgop**Optional system telemetry service used by resource widgets.**dsearch**Optional filesystem search engine used by the Spotlight launcher.

## Desktop Integration[​](#desktop-integration "Direct link to Desktop Integration")

DankMaterialShell includes a browser picker modal that appears when URLs are activated within the shell.

### Opening URLs[​](#opening-urls "Direct link to Opening URLs")

You can open URLs directly from the terminal using the `dms open` command:

```
dms open https://danklinux.com
```

When a URL is opened, DankMaterialShell displays a modal dialog with a list of installed web browsers, allowing you to select your preferred browser or set a default for future URL openings.

### Setting Default Web Browser[​](#setting-default-web-browser "Direct link to Setting Default Web Browser")

To set DankMaterialShell as your default web browser handler:

```
xdg-settings set default-web-browser dms-open.desktop
```

### File Associations[​](#file-associations "Direct link to File Associations")

You can configure file type associations using `xdg-mime` commands. For example, to set DankMaterialShell as the default handler for specific MIME types:

```
# Set as default for HTTP/HTTPS URLs
xdg-mime default dms-open.desktop x-scheme-handler/http
xdg-mime default dms-open.desktop x-scheme-handler/https
```

### Desktop Entry[​](#desktop-entry "Direct link to Desktop Entry")

The desktop entry file (`dms-open.desktop`) follows the [freedesktop.org Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html) and allows DankMaterialShell to be launched from application menus and integrated with desktop environments.

## Next Steps[​](#next-steps "Direct link to Next Steps")

Continue with [Installation](https://danklinux.com/docs/dankmaterialshell/installation) to get DankMaterialShell running on your system.

DankMaterialShell is open source and welcomes contributions ranging from core code changes to new widgets and plugins to documentation improvements.