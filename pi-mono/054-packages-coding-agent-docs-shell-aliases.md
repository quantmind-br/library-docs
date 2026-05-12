---
title: Shell Aliases
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/shell-aliases.md
source: git
fetched_at: 2026-05-03T09:31:23.751958052-03:00
rendered_js: false
word_count: 35
summary: Enabling shell aliases in Pi's non-interactive bash mode via shellCommandPrefix.
tags:
    - shell-configuration
    - bash
    - zsh
    - aliases
    - automation
category: configuration
optimized: true
optimized_at: 2026-05-03T12:00:00Z
---
Pi runs bash in non-interactive mode (`bash -c`), which doesn't expand aliases by default.

Add to `~/.pi/agent/settings.json` to enable aliases:

```json
{
  "shellCommandPrefix": "shopt -s expand_aliases\neval \"$(grep '^alias ' ~/.zshrc)\""
}
```

Adjust the shell config path (`~/.zshrc`, `~/.bashrc`, etc.) as needed.

#shell-configuration #bash #zsh #aliases #automation
