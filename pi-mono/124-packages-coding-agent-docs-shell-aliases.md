---
title: Shell aliases
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/shell-aliases.md
source: git
fetched_at: 2026-03-03T03:40:55.857189-03:00
rendered_js: false
word_count: 48
summary: explains how to configure shell alias expansion for a non-interactive environment (like Pi's agent) by injecting shell commands into settings
tags:
    - shell-config
    - command-line
    - bash-alias
    - agent-environment
    - scripting-alias
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
