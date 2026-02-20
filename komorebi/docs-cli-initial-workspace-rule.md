---
title: Initial workspace rule
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/initial-workspace-rule.md
source: git
fetched_at: 2026-02-20T08:48:30.619032-03:00
rendered_js: false
word_count: 54
summary: This document describes the usage and arguments for the initial-workspace-rule command, which allows users to pin specific applications to a monitor and workspace when they first appear.
tags:
    - komorebi
    - window-management
    - workspace-rules
    - cli-reference
    - automation
category: reference
---

# initial-workspace-rule

```
Add a rule to associate an application with a workspace on first show

Usage: komorebic.exe initial-workspace-rule <IDENTIFIER> <ID> <MONITOR> <WORKSPACE>

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
