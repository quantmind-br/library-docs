---
title: Windows
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/windows.md
source: git
fetched_at: 2026-03-23T14:25:51.303904-03:00
rendered_js: false
word_count: 49
summary: This document describes the process of configuring and locating the required bash shell environment for the Pi application on Windows systems.
tags:
    - windows-setup
    - shell-configuration
    - environment-path
    - git-bash
    - wsl
    - cygwin
category: configuration
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
