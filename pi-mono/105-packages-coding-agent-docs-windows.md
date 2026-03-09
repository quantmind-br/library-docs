---
title: Windows
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/windows.md
source: git
fetched_at: 2026-03-03T03:41:32.052515-03:00
rendered_js: false
word_count: 49
summary: guide to setting up the bash shell for Pi on Windows through Git for Windows or custom configuration paths
tags:
    - windows-shell
    - bash-installation
    - cygwin-git
    - wsl-git
    - path-configuration
category: guide
---

# Windows Setup

Pi requires a bash shell on Windows. Checked locations (in order):

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
