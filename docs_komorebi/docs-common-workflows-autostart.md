---
title: Autostart
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/autostart.md
source: git
fetched_at: 2026-02-20T08:51:03.798299-03:00
rendered_js: false
word_count: 76
summary: This document explains how to configure the komorebi tiling window manager to launch automatically upon Windows startup using the command-line interface.
tags:
    - komorebi
    - autostart
    - windows-startup
    - configuration
    - tiling-window-manager
    - cli
category: guide
---

# Autostart

If you would like to autostart `komorebi`, you can use the `komorebic enable-autostart` command to generate a shortcut
in the `shell:startup` folder.

```
Generates the komorebi.lnk shortcut in shell:startup to autostart komorebi

Usage: komorebic.exe enable-autostart [OPTIONS]

Options:
  -c, --config <CONFIG>
          Path to a static configuration JSON file

  -f, --ffm
          Enable komorebi's custom focus-follows-mouse implementation

      --whkd
          Enable autostart of whkd

      --ahk
          Enable autostart of ahk

      --bar
          Enable autostart of komorebi-bar

  -h, --help
          Print help
```
