---
title: Shell aliases
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/shell-aliases.md
source: git
fetched_at: 2026-03-23T14:25:47.523412-03:00
rendered_js: false
word_count: 48
summary: This document explains how to enable shell aliases in the Pi agent environment by configuring the shell command prefix in the settings file.
tags:
    - shell-aliases
    - bash-configuration
    - pi-agent
    - environment-variables
    - terminal-settings
category: configuration
---

# Shell Aliases

Pi runs bash in non-interactive mode (`bash -c`), which doesn't expand aliases by default.

To enable your shell aliases, add to `~/.pi/agent/settings.json`:

```json
{
  "shellCommandPrefix": "shopt -s expand_aliases\neval \"$(grep '^alias ' ~/.zshrc)\""
}
```

Adjust the path (`~/.zshrc`, `~/.bashrc`, etc.) to match your shell config.
