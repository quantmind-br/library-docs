---
title: Using terminal programs to provide Linux desktop components
title: Using terminal programs to provide Linux desktop components
word_count: 299
summary: This document explains how to use the kitty desktop-ui kitten to integrate terminal-based components into a Linux desktop environment using XDG portals.
category: guide
optimized: true
optimized_at: 2026-05-04T20:45:08Z
---
# Using terminal programs to provide Linux desktop components

The desktop-ui kitten provides desktop environment components using keyboard-friendly, terminal-first UI. It relies on the [[016-kittens-panel|panel kitten]] under the hood. Check its [documentation](panel_compat) for window manager compatibility.

## Features

- Replace GUI File Open/Save dialogs with [[005-kittens-choose-files|choose-files kitten]] running in a semi-transparent kitty overlay.
- Command-line management of desktop light/dark modes.

## How to install

> [!NOTE]
> This kitten relies on the [[016-kittens-panel|panel kitten]]. Check its window manager compatibility first.

```bash
kitten desktop-ui enable-portal
```

Set environment variables system-wide (in `/etc/environment` or equivalent):

```
QT_QPA_PLATFORMTHEME=xdgdesktopportal
GTK_USE_PORTAL=1
```

Reboot. GUI applications should now use the [[005-kittens-choose-files|choose-files kitten]] for file dialogs.

Control color scheme:

```bash
kitten desktop-ui set-color-scheme dark
kitten desktop-ui set-color-scheme light
```

Check current value:

```bash
dbus-send --session --print-reply --dest=org.freedesktop.portal.Desktop /org/freedesktop/portal/desktop org.freedesktop.portal.Settings.Read string:org.freedesktop.appearance color_scheme
```

## How it works

Modern Linux desktops have [portals](https://flatpak.github.io/xdg-desktop-portal/docs/index.html) that provide facilities like file dialogs and desktop settings over DBUS. This kitten implements a backend for these services. When GUI applications are told to use portals, the kitten replaces parts of the desktop experience.

Multiple backend implementations exist (KDE, GNOME, various window managers). Service discovery and backend selection happens via `/usr/lib/xdg-desktop-portal`. Configure in `~/.local/share/xdg-desktop-portal/` (see [portals.conf man page](https://man.archlinux.org/man/portals.conf.5)). The `kitten desktop-ui enable-portal` command handles setup automatically; edit the patched conf file for custom service selection.

## Troubleshooting

### DBUS auto-start

```bash
dbus-send --session --print-reply --dest=org.freedesktop.impl.portal.desktop.kitty \
    /net/kovidgoyal/kitty/portal org.freedesktop.DBus.Properties.GetAll \
    string:net.kovidgoyal.kitty.settings
```

If it prints the version property, DBUS is working. If not, check `~/.local/share/dbus-1/services/org.freedesktop.impl.portal.desktop.kitty.service` — its `Exec` key must point to the full path of the kitten executable.

### Check portal backend

```bash
dbus-send --session --print-reply --dest=org.freedesktop.portal.Desktop \
    /org/freedesktop/portal/desktop org.freedesktop.portal.Settings.Read \
    string:net.kovidgoyal.kitty string:status
```

A reply means the kitten is in use. A "not found" error means another backend is being used.

### Debug portal selection

```bash
/usr/lib/xdg-desktop-portal -r v
```

Outputs debug info showing which backend is chosen for each service.

### GUI applications not using choose-files

Ensure the environment variables are set globally. Test explicitly:

```bash
QT_QPA_PLATFORMTHEME=xdgdesktopportal GTK_USE_PORTAL=1 my-gui-app
```

Not all applications use portals. Report failures to those applications' developers.

## Configuration

Create `desktop-ui-portal.conf` in the kitty config directory. See configuration directives below.
