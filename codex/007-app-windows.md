---
title: Windows
url: https://developers.openai.com/codex/app/windows.md
source: llms
fetched_at: 2026-04-30T10:15:09.9723396-03:00
rendered_js: false
word_count: 774
summary: This document provides a comprehensive guide for installing, configuring, and troubleshooting the Codex application on the Windows operating system.
tags:
    - windows
    - installation
    - wsl
    - powershell
    - configuration
    - sandboxing
    - development-environment
category: guide
optimized: true
optimized_at: 2026-04-30T13:30:00Z
---
# Windows

The [Codex app for Windows](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) gives you one interface for working across projects, running parallel agent threads, and reviewing results. Supports worktrees, automations, Git, in-app browser, artifact previews, plugins, and skills. Runs natively on Windows using PowerShell and the Windows sandbox, or configure it to run in [WSL2](#windows-subsystem-for-linux-wsl).

## Download and update

Download from the [Microsoft Store](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi), then follow the [[001-quickstart|quickstart]] (select "app" setup).

Update via Microsoft Store > **Downloads** > **Check for updates**.

Enterprise administrators can deploy via Microsoft Store app distribution.

Command-line install:
```powershell
winget install Codex -s msstore
```

## Native sandbox

Supports a native Windows sandbox when the agent runs in PowerShell. Uses Linux sandboxing when running in WSL2. Set sandbox permissions to **Default permissions** in the Composer before sending messages.

> [!warning]
> Full access mode means Codex is not limited to your project directory and might perform unintentional destructive actions leading to data loss. Keep sandbox boundaries in place and use [[061-rules|rules]] for targeted exceptions, or set your approval policy to never to have Codex attempt to solve problems without asking for escalated permissions. See [[041-agent-approvals-security|approval and security setup]].

## Customize dev setup

### Preferred editor

Choose a default app for **Open** (Visual Studio, VS Code, etc.). Override per project if needed.

### Integrated terminal

Choose default terminal:
- PowerShell
- Command Prompt
- Git Bash
- WSL

Applies to new terminal sessions only. Restart app or start a new thread for changes to take effect.

## Windows Subsystem for Linux (WSL)

By default, the Codex app uses the Windows-native agent (PowerShell). It can still work with WSL projects using the `wsl` CLI when needed.

To add a WSL project: **Add new project** (or `Ctrl+O`), type `\\wsl$\` in File Explorer, choose your Linux distribution and folder.

If using the Windows-native agent, prefer storing projects on the Windows filesystem and accessing them from WSL through `/mnt/<drive>/...`. More reliable than opening projects directly from the WSL filesystem.

To run the agent in WSL2: open **Settings**, switch agent from Windows native to WSL, and **restart the app**. Change doesn't take effect until restart. Projects remain in place after restart.

WSL1 was supported through Codex `0.114`. Starting in `0.115`, the Linux sandbox moved to `bubblewrap`, so WSL1 is no longer supported.

Integrated terminal is configured independently from the agent. You can keep the agent in WSL and still use PowerShell in the terminal, or use WSL for both.

## Useful developer tools

Codex works best when these are installed:

| Tool | Purpose | Install command |
|------|---------|-----------------|
| Git | Review panel, inspect/revert changes | `winget install --id Git.Git` |
| Node.js | Common agent task tool | `winget install --id OpenJS.NodeJS.LTS` |
| Python | Common agent task tool | `winget install --id Python.Python.3.14` |
| .NET SDK | Build native Windows apps | `winget install --id Microsoft.DotNet.SDK.10` |
| GitHub CLI | GitHub-specific functionality | `winget install --id GitHub.cli` |

After installing GitHub CLI, run `gh auth login` to enable GitHub features.

If you need different Python or .NET versions, change the package IDs.

## Troubleshooting and FAQ

### Run commands with elevated permissions

Start the Codex app itself as an administrator. Open Start menu, find Codex, choose **Run as administrator**. The agent inherits that permission level.

### PowerShell execution policy blocks commands

If you've never used Node.js or `npm` in PowerShell, the agent or integrated terminal may hit execution policy errors. This can also happen if Codex creates PowerShell scripts.

Error example:
```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

Common fix:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

See Microsoft's [execution policy guide](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies) before changing.

### Local environment scripts on Windows

If your [[050-app-local-environments|local environment]] uses cross-platform commands such as `npm` scripts, you can keep one shared setup script for every platform.

For Windows-specific behavior, create Windows-specific setup scripts or actions. Actions run in the integrated terminal's environment. Local setup scripts run in the agent environment: WSL if the agent uses WSL, PowerShell otherwise.

### Share config, auth, and sessions with WSL

Windows app uses `%USERPROFILE%\.codex`. The Codex CLI inside WSL uses the Linux home directory by default, so it doesn't automatically share configuration, cached auth, or session history.

To share:
- Sync WSL `~/.codex` with `%USERPROFILE%\.codex`
- Or point WSL at the Windows Codex home directory:
  ```bash
  export CODEX_HOME=/mnt/c/Users/<windows-user>/.codex
  ```
  Add to WSL shell profile (`~/.bashrc` or `~/.zshrc`) for persistence.

### Git features are unavailable

Install Git natively on Windows: `winget install Git.Git`.

### Git isn't detected for projects opened from `\\wsl$`

Most reliable workaround: store the project on the native Windows drive and access it in WSL through `/mnt/<drive>/...`.

### `Cmder` isn't listed in the open dialog

Add it to the Windows Start Menu (right-click > **Add to Start**), then restart Codex or reboot.

#windows #installation #wsl #powershell #troubleshooting