---
title: Workspace rule
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/workspace-rule.md
source: git
fetched_at: 2026-02-20T08:50:56.981189-03:00
rendered_js: false
word_count: 51
summary: This document explains the usage and arguments for the workspace-rule command, which assigns specific applications to designated monitors and workspaces.
tags:
    - komorebic
    - cli
    - workspace-management
    - window-rules
    - configuration
category: reference
---

# workspace-rule

```
Add a rule to associate an application with a workspace

Usage: komorebic.exe workspace-rule <IDENTIFIER> <ID> <MONITOR> <WORKSPACE>

Arguments:
  <IDENTIFIER>
          [possible values: exe, class, title, path]

  <ID>
          Identifier as a string

  <MONITOR>
          Monitor index (zero-indexed)

  <WORKSPACE>
          Workspace index on the specified monitor (zero-indexed)

Options:
  -h, --help
          Print help

```
