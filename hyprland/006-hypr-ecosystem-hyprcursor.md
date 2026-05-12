---
title: hyprcursor
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprcursor/
source: sitemap
fetched_at: 2026-04-26T09:49:39.004186032-03:00
rendered_js: false
word_count: 245
summary: Install, configure, and manage hyprcursor themes in Hyprland, including XCursor fallback for incompatible apps.
tags:
    - hyprland
    - cursor-theme
    - configuration
    - linux-desktop
    - xcursor-fallback
    - ui-customization
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

hyprcursor is a cursor theme format with advantages over xcursor.

## Themes

Obtain themes from the Discord server `#hyprcursor-themes` channel. Place themes in `~/.local/share/icons` or `~/.icons`.

> [!warning] Do NOT put cursor themes in system-wide `/usr/share/icons` — permission issues may occur.

## Configuration

Set theme via envvars or `hyprctl setcursor`:

| Env var | Purpose |
|---|---|
| `HYPRCURSOR_THEME` | Theme name |
| `HYPRCURSOR_SIZE` | Cursor size |

```ini
env = HYPRCURSOR_THEME,MyCursor
env = HYPRCURSOR_SIZE,24
```

## Creating / Porting Themes

See the [hyprcursor repo](https://github.com/hyprwm/hyprcursor) `docs/` and `hyprcursor-util/` directories.

## Apps Without Server-Side Cursor Support

Some apps (e.g. GTK) do not support server-side cursors. These fall back to XCursor.

Export `XCURSOR_THEME` and `XCURSOR_SIZE` to a valid XCursor theme, then:

** GTK (gsettings available):**
```sh
gsettings set org.gnome.desktop.interface cursor-theme 'THEME_NAME'
```

** GTK (gsettings unavailable — e.g. NixOS):**
```sh
dconf write /org/gnome/desktop/interface/cursor-theme "'THEME_NAME'"
```

** Flatpak:**
```sh
flatpak override --filesystem=~/.themes:ro --filesystem=~/.icons:ro --user
```
Put themes in both `/usr/share/themes` and `~/.themes`, icons and XCursors in both `/usr/share/icons` and `~/.icons`.

## XCursor Fallback

Without hyprcursor themes installed, Hyprland falls back to XCursor via `XCURSOR_THEME` and `XCURSOR_SIZE`.

## hyprland Icon Cursor

See [[083-faq|FAQ]].

> [!info] Last updated: April 20, 2026

[[008-hypr-ecosystem-hyprshutdown|hyprshutdown]] [[074-hypr-ecosystem-hyprutils|hyprutils]] [[035-hypr-ecosystem-hyprpwcenter|hyprpwcenter]]

#hyprcursor #cursor-theme #hyprland
