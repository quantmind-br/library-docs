---
title: Setup | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/cli-setup
source: sitemap
fetched_at: 2026-04-26T08:38:53.512199646-03:00
rendered_js: false
word_count: 143
summary: This document explains how to use the dms setup command to generate default configuration files for niri and Hyprland compositors while avoiding overwriting existing user customizations.
tags:
    - dms-setup
    - config-management
    - niri
    - hyprland
    - compositor-configuration
    - home-manager
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

```
███████╗███████╗████████╗██╗   ██╗██████╗
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
███████╗█████╗     ██║   ██║   ██║██████╔╝
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝
███████║███████╗   ██║   ╚██████╔╝██║
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝
```

`dms setup` generates default configuration files for your compositor (niri or Hyprland). It only writes files that don't already exist or are empty, preserving user customizations.

## Usage

**Deploy all defaults:**
```bash
dms setup
```

**Deploy individual configs:**
```bash
dms setup binds
dms setup colors
dms setup layout
```

## home-manager Integration

If you manage niri or Hyprland config through home-manager, use individual subcommands to avoid conflicts with your declarative config.

For example, to handle keybinds via the niri home-manager module but want DMS defaults for colors and layout:

The niri home-manager module's `niri.includes` option references files under `~/.config/niri/dms/`. See [[010-docs-dankmaterialshell-nixos-flake|the niri integration docs]] for the full list of included files.
