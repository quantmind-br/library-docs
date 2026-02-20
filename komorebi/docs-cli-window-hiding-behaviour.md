---
title: Window hiding behaviour
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/window-hiding-behaviour.md
source: git
fetched_at: 2026-02-20T08:50:49.186627-03:00
rendered_js: false
word_count: 85
summary: This document describes the command-line usage and options for configuring how windows are hidden during workspace switching or stack cycling in the Komorebi window manager.
tags:
    - komorebi
    - window-management
    - workspace-switching
    - cli-reference
    - window-behavior
category: reference
---

# window-hiding-behaviour

```
Set the window behaviour when switching workspaces / cycling stacks

Usage: komorebic.exe window-hiding-behaviour <HIDING_BEHAVIOUR>

Arguments:
  <HIDING_BEHAVIOUR>
          Possible values:
          - hide:     END OF LIFE FEATURE: Use the SW_HIDE flag to hide windows when switching workspaces (has issues with Electron apps)
          - minimize: Use the SW_MINIMIZE flag to hide windows when switching workspaces (has issues with frequent workspace switching)
          - cloak:    Use the undocumented SetCloak Win32 function to hide windows when switching workspaces

Options:
  -h, --help
          Print help (see a summary with '-h')

```
