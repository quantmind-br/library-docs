---
title: Setup | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-setup
source: sitemap
fetched_at: 2026-04-07T21:32:51.358209866-03:00
rendered_js: false
word_count: 143
summary: This document explains how the `dms setup` command generates default configuration files for compositors like niri or Hyprland, detailing that it only writes to non-existent or empty files.
tags:
    - compositor-setup
    - configuration-management
    - niri
    - hyprland
    - default-settings
category: guide
---

```
███████╗███████╗████████╗██╗   ██╗██████╗
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
███████╗█████╗     ██║   ██║   ██║██████╔╝
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝
███████║███████╗   ██║   ╚██████╔╝██║
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝
```

The `dms setup` command generates default configuration files for your compositor (niri or Hyprland). It only writes files that don't already exist or are empty, so it won't clobber anything you've customized.

Running `dms setup` with no arguments deploys all defaults at once. You can also deploy individual configs one at a time.

Running `dms setup` with no subcommand deploys all of the above.

If you manage your niri or Hyprland config through home-manager, you probably don't want `dms setup` writing files that conflict with your declarative config. Instead, use the individual subcommands to generate only the pieces you need.

For example, if you handle keybinds through the niri home-manager module but want DMS defaults for colors and layout:

The niri home-manager module's `niri.includes` option references these same files under `~/.config/niri/dms/`. See the [niri integration docs](https://danklinux.com/docs/dankmaterialshell/nixos-flake#config-includes) for the full list of included files.