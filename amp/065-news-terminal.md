---
title: Terminal Improvements
url: https://ampcode.com/news/terminal
source: crawler
fetched_at: 2026-02-06T02:08:49.075837678-03:00
rendered_js: false
word_count: 96
summary: This document outlines updates to terminal command execution in Amp, including shell environment integration, new interactive controls, and improved output rendering.
tags:
    - terminal-commands
    - amp-platform
    - vs-code-integration
    - command-execution
    - user-interface
    - shell-environment
category: reference
---

We have made multiple changes to how we run terminal commands in Amp:

**Environment** — Commands now run by default in the integrated VS Code terminal inheriting your shell environment including Python virtual environments and direnv configuration.

**Interactivity** — Use the new "View in Terminal" button to interact with commands that require stdin, or the new "Detach" button to let the command continue running in the background.

**Output** — Progress bars with ANSI escape codes now render beautifully in the UI without eating up your context window, only the final output is presented to the model.