---
title: Overview & Architecture | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/overview
source: sitemap
fetched_at: 2026-04-26T08:39:15.619528095-03:00
rendered_js: false
word_count: 185
summary: DankMaterialShell is a Wayland desktop shell built with Quickshell and Go that provides a modular environment for window and application management.
tags:
    - wayland
    - desktop-shell
    - quickshell
    - linux-desktop
    - xdg-mime
    - window-manager
category: concept
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Overview & Architecture

DankMaterialShell (dms) is a Wayland desktop shell built with [Quickshell](https://quickshell.org/) and [Go](https://go.dev/), serving the same purpose as GNOME Shell or KDE Plasma.

## Architecture

DMS uses a client-server architecture:
- **Go backend (`dms`)** — manages system integrations
- **Quickshell-based UI** — spawned as a child process
- **Unix socket communication** — REQ/REP and PUB/SUB patterns

## Browser Picker Modal

DMS displays a modal dialog when URLs are activated, listing installed web browsers for selection. Set defaults with:

```bash
xdg-mime default dms-open.desktop x-scheme-handler/http
xdg-mime default dms-open.desktop x-scheme-handler/https
```

The `dms-open.desktop` entry follows the [freedesktop.org Desktop Entry Specification](https://specifications.freedesktop.org/desktop-entry-spec/desktop-entry-spec-latest.html).

## Contributing

DMS is open source and welcomes contributions — core code, widgets, plugins, and documentation.

#wayland #desktop-shell #quickshell #xdg-mime
