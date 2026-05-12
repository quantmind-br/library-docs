---
title: Changing kitty colors
title: Changing kitty colors
word_count: 300
summary: This document explains how to use the themes kitten to manage, customize, and automate color theme switching in the kitty terminal emulator.
category: guide
optimized: true
optimized_at: 2026-05-04T20:45:24Z
---
# Changing kitty colors

The themes kitten provides 300+ pre-built color themes from `kitty-themes <https://github.com/kovidgoyal/kitty-themes>`_. Launch with:

```bash
kitten themes
```

Features: live color previews, light/dark theme filtering, search by typing theme name characters.

## How It Works

A theme is a `.conf` file with kitty settings. When selected:

1. Kitten copies the `.conf` file to `~/.config/kitty/current-theme.conf`
2. Adds `include current-theme.conf` to `kitty.conf`
3. Comments out existing color settings in `kitty.conf`
4. Signals kitty to reload config

> [!NOTE]
> To preserve custom color settings不被 themes 覆盖, move them to a separate conf file and `include` it after `current-theme.conf`.

## Auto-Theme Based on OS Mode

Kitty can automatically switch themes when the OS changes between dark/light/no-preference modes:

1. Run `kitten themes` and select a theme
2. At the final screen, save it for a specific mode (light/dark/no-preference)
3. Repeat for each mode
4. Restart kitty

This creates three auto-config files:

- `dark-theme.auto.conf`
- `light-theme.auto.conf`
- `no-preference-theme.auto.conf`

Kitty queries the OS color scheme and uses the matching file. These files override **all** other colors including `--override` command-line flags and background images.

> [!NOTE]
> On GNOME, "Dark style" disabled reports as no-preference. Use `no-preference-theme.auto.conf` for light mode on GNOME, or force it:
> ```bash
> gsettings set org.gnome.desktop.interface color-scheme prefer-light
> ```

## Custom Themes

Create your own `.conf` files in `~/.config/kitty/themes/`. The kitten adds them to the theme list automatically.

To override a builtin theme, name your file the same as the builtin theme's display name (not filename). Select that theme once in the kitten to apply.

## Contributing Themes

1. Fork `kitty-themes <https://github.com/kovidgoyal/kitty-themes>`__
2. Use `template.conf <https://github.com/kovidgoyal/kitty-themes/raw/master/template.conf>`__ as a base
3. Submit a pull request to have it merged

## Non-Interactive Usage

```bash
kitten themes --reload-in=all "Dimmed Monokai"
```

Changes the theme instantly in all running kitty instances. The `--reload-in` option controls which instances reload.

#kitty #terminal-emulator #color-themes #configuration #automation
