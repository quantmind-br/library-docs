---
title: Start
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/start.md
source: git
fetched_at: 2026-02-20T08:49:55.59404-03:00
rendered_js: false
word_count: 100
summary: This document provides a reference for the komorebic start command, detailing the options available to launch the komorebi window manager as a background process.
tags:
    - komorebi
    - cli-reference
    - window-manager
    - process-management
    - windows-os
category: reference
---

# start

```
Start komorebi.exe as a background process

Usage: komorebic.exe start [OPTIONS]

Options:
  -c, --config <CONFIG>
          Path to a static configuration JSON file

  -a, --await-configuration
          Wait for 'komorebic complete-configuration' to be sent before processing events

  -t, --tcp-port <TCP_PORT>
          Start a TCP server on the given port to allow the direct sending of SocketMessages

      --whkd
          Start whkd in a background process

      --bar
          Start komorebi-bar in a background process

      --masir
          Start masir in a background process for focus-follows-mouse

      --clean-state
          Do not attempt to auto-apply a dumped state temp file from a previously running instance of komorebi

  -h, --help
          Print help

```
