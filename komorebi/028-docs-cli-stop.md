---
title: Stop
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/stop.md
source: git
fetched_at: 2026-02-20T08:50:00.800597-03:00
rendered_js: false
word_count: 55
summary: This document describes the stop command for the komorebic CLI, which terminates the komorebi window manager process and optionally stops associated background services like whkd and masir.
tags:
    - komorebi
    - window-management
    - cli-reference
    - process-termination
    - command-line-interface
category: reference
---

# stop

```
Stop the komorebi.exe process and restore all hidden windows

Usage: komorebic.exe stop [OPTIONS]

Options:
      --whkd
          Stop whkd if it is running as a background process

      --bar
          Stop komorebi-bar if it is running as a background process

      --masir
          Stop masir if it is running as a background process

  -h, --help
          Print help

```
