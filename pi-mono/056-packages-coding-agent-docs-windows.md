---
title: Windows Setup
url: https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/windows.md
source: git
fetched_at: 2026-05-03T09:31:31.569085417-03:00
rendered_js: false
word_count: 45
summary: Bash shell requirements and configuration for Pi on Windows.
tags:
    - windows-setup
    - bash-shell
    - configuration
    - environment-setup
    - shell-path
category: configuration
optimized: true
optimized_at: 2026-05-03T12:00:00Z
---
Pi requires a bash shell on Windows. Checked locations in order:

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

#windows-setup #bash-shell #configuration #environment-setup #shell-path
