---
title: Workspace layout
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/workspace-layout.md
source: git
fetched_at: 2026-02-20T08:50:52.71437-03:00
rendered_js: false
word_count: 47
summary: This document describes the workspace-layout command, which allows users to set specific window tiling layouts for designated monitors and workspaces.
tags:
    - komorebi
    - tiling-window-manager
    - workspace-management
    - cli-reference
    - window-layout
category: reference
---

# workspace-layout

```
Set the layout for the specified workspace

Usage: komorebic.exe workspace-layout <MONITOR> <WORKSPACE> <VALUE>

Arguments:
  <MONITOR>
          Monitor index (zero-indexed)

  <WORKSPACE>
          Workspace index on the specified monitor (zero-indexed)

  <VALUE>
          [possible values: bsp, columns, rows, vertical-stack, horizontal-stack, ultrawide-vertical-stack, grid, right-main-vertical-stack, scrolling]

Options:
  -h, --help
          Print help

```
