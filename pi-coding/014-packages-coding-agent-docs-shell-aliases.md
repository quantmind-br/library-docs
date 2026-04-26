---
title: Shell aliases
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/shell-aliases.md
source: git
fetched_at: 2026-04-26T05:48:28.064875896-03:00
rendered_js: false
word_count: 48
summary: Enable shell aliases in non-interactive bash sessions within the Pi agent by configuring the shell command prefix.
tags:
    - shell-aliases
    - bash-configuration
    - environment-settings
    - automation
    - command-line
category: configuration
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# Shell Aliases

Pi runs bash in non-interactive mode (`bash -c`), which doesn't expand aliases by default.

> [!tip] Enable your shell aliases by adding to `~/.pi/agent/settings.json`:

```json
{
  "shellCommandPrefix": "shopt -s expand_aliases\neval \"$(grep '^alias ' ~/.zshrc)\""
}
```

Adjust the path (`~/.zshrc`, `~/.bashrc`, etc.) to match your shell config.

#shell-aliases #bash-configuration
