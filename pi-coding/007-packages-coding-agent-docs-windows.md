---
title: Windows
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/windows.md
source: git
fetched_at: 2026-04-26T05:48:43.538822697-03:00
rendered_js: false
word_count: 49
summary: Bash shell requirements and search order for running Pi on Windows, including custom shell path configuration.
tags:
    - windows-setup
    - bash-shell
    - configuration
    - environment-setup
    - path-settings
category: configuration
optimized: true
optimized_at: 2026-04-26T09:00:00Z
---

# Windows Setup

Pi requires a bash shell on Windows. Search order:

1. Custom path from `~/.pi/agent/settings.json`
2. Git Bash (`C:\Program Files\Git\bin\bash.exe`)
3. `bash.exe` on PATH (Cygwin, MSYS2, WSL)

For most users, [Git for Windows](https://git-scm.com/download/win) is sufficient.

## Custom Shell Path

```json
{
  "shellPath": "C:\\cygwin64\\bin\\bash.exe"
}
```

#windows-setup #bash-shell #configuration
