---
title: Setup | Dank Linux
url: https://danklinux.com/docs/1.5/dankmaterialshell/cli-setup
source: sitemap
fetched_at: 2026-02-22T18:44:07.436974-03:00
rendered_js: false
word_count: 143
summary: Explains how to use the dms setup command to generate default configuration files for niri and Hyprland compositors, including integration with home-manager.
tags:
    - dms-setup
    - niri
    - hyprland
    - configuration-management
    - home-manager
    - linux-compositor
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

The niri home-manager module's `niri.includes` option references these same files under `~/.config/niri/dms/`. See the [niri integration docs](https://danklinux.com/docs/1.5/dankmaterialshell/nixos-flake#config-includes) for the full list of included files.