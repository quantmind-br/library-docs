---
title: Workspace layout rule
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/workspace-layout-rule.md
source: git
fetched_at: 2026-02-20T08:50:51.007114-03:00
rendered_js: false
word_count: 63
summary: This document describes the usage and arguments for the komorebic CLI command to add dynamic layout rules to specific workspaces based on container counts.
tags:
    - komorebic
    - window-management
    - workspace-layout
    - dynamic-tiling
    - cli-reference
category: reference
---

# workspace-layout-rule

```
Add a dynamic layout rule for the specified workspace

Usage: komorebic.exe workspace-layout-rule <MONITOR> <WORKSPACE> <AT_CONTAINER_COUNT> <LAYOUT>

Arguments:
  <MONITOR>
          Monitor index (zero-indexed)

  <WORKSPACE>
          Workspace index on the specified monitor (zero-indexed)

  <AT_CONTAINER_COUNT>
          The number of window containers on-screen required to trigger this layout rule

  <LAYOUT>
          [possible values: bsp, columns, rows, vertical-stack, horizontal-stack, ultrawide-vertical-stack, grid, right-main-vertical-stack, scrolling]

Options:
  -h, --help
          Print help

```
