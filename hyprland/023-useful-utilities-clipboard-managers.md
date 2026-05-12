---
title: Clipboard Managers
url: https://wiki.hypr.land/Useful-Utilities/Clipboard-Managers/
source: sitemap
fetched_at: 2026-04-26T09:48:30.609558616-03:00
rendered_js: false
word_count: 759
summary: This document provides instructions for integrating and configuring various clipboard management tools within the Hyprland window manager environment.
tags:
    - hyprland
    - clipboard-manager
    - wayland
    - linux-desktop
    - system-configuration
    - productivity-tools
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

*Starting method:* manual (`exec-once`)

Clipboard Managers organize and access previously copied content (text and images).

## Tools

- **[cliphist](https://github.com/sentriz/cliphist)** — Wayland `wl-clipboard`, stores text, images, binary data.
- **[clipman](https://github.com/chmouel/clipman)** — Wayland `wl-clipboard`, stores text only.
- **[clipvault](https://github.com/rolv-apneseth/clipvault)** — Wayland `wl-clipboard`, stores text, images, binary data. Extra features: max age, min/max entry length.
- **[clipse](https://github.com/savedra1/clipse)** — Wayland `wl-clipboard`, TUI, text+images, themes, previews, multi-select, pinned items, auto-paste, sensitive content handling.
- **[copyq](https://github.com/hluk/CopyQ)** — Text, images, formats. Searchable history, editing, scripting, tabs, cross-device sync.
- **[wl-clip-persist](https://github.com/Linus789/wl-clip-persist)** — Preserves clipboard data after source app closes.
- **[cursor-clip](https://github.com/Sirulex/cursor-clip)** — Rust/GTK4/Libadwaita, Windows 11-style UI at mouse pointer, all formats.

## cliphist

```ini
exec-once = wl-paste --type text --watch cliphist store
exec-once = wl-paste --type image --watch cliphist store
```

Disable either line based on needs. Bind to a hotkey with your launcher (rofi, dmenu, wofi, fuzzel).

## clipman

```ini
exec-once = wl-paste -t text --watch clipman store --no-persist
```

For primary clipboard manager:

```ini
exec-once = wl-paste -p -t text --watch clipman store -P --histpath="~/.local/share/clipman-primary.json"
```

Ensure `~/.local/share/clipman-primary.json` exists.

## clipvault

```ini
exec-once = wl-paste --watch clipvault store
# exec-once = wl-paste --type text --watch clipvault store
# exec-once = wl-paste --type image --watch clipvault store
# exec-once = wl-paste --watch clipvault store --min-entry-length 2 --max-entries 200 --max-entry-age 2d
```

Bind to hotkey with your launcher.

## clipse

```ini
exec-once = clipse -listen
```

Bind to floating TUI:

```ini
windowrule = float on, size 622 652, stay_focused on, match:class ^(clipse)$
bind = SUPER, V, exec, kitty --class clipse -e clipse
```

Kitty recommended for best image rendering. Class is optional but floating window feels more GUI-like.

## copyq

```ini
exec-once = copyq --start-server
```

If main window cannot close/hide properly, enable "Hide main window" in Preferences → Layout.

## wl-clip-persist

```ini
exec-once = wl-clip-persist --clipboard regular
```

Preserves clipboard after source app closes. For primary selection (middle-click paste):

```ini
exec-once = wl-clip-persist --clipboard primary
```

> [!warning]
> Primary selection mode [has unintended side-effects for some GTK applications](https://github.com/Linus789/wl-clip-persist#primary-selection-mode-breaks-the-selection-system-3).

## cursor-clip

```ini
exec-once = cursor-clip --daemon
```

```ini
bind = SUPER, V, exec, cursor-clip
```

Overlay window positions at mouse location. Windows 11-style UI, GTK4/Libadwaita, supports text/images/files.

#clipboard-manager #wayland #productivity-tools
