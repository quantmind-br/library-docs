---
title: Unmanaged window operation behaviour
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/unmanaged-window-operation-behaviour.md
source: git
fetched_at: 2026-02-20T08:50:38.777915-03:00
rendered_js: false
word_count: 51
summary: This document explains how to configure komorebic's behavior when processing commands while an unmanaged or floating window is focused.
tags:
    - komorebic
    - window-management
    - cli-reference
    - configuration-options
    - floating-windows
category: reference
---

# unmanaged-window-operation-behaviour

```
Set the operation behaviour when the focused window is not managed

Usage: komorebic.exe unmanaged-window-operation-behaviour <OPERATION_BEHAVIOUR>

Arguments:
  <OPERATION_BEHAVIOUR>
          Possible values:
          - op:    Process komorebic commands on temporarily unmanaged/floated windows
          - no-op: Ignore komorebic commands on temporarily unmanaged/floated windows

Options:
  -h, --help
          Print help (see a summary with '-h')

```
