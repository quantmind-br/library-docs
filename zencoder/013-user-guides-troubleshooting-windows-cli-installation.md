---
title: CLI Installation Issues on Windows - Zencoder Docs
url: https://docs.zencoder.ai/user-guides/troubleshooting/windows-cli-installation
source: crawler
fetched_at: 2026-01-23T09:28:34.944954127-03:00
rendered_js: false
word_count: 64
summary: This document provides troubleshooting steps to resolve PowerShell execution policy errors encountered when installing AI CLI tools on Windows systems.
tags:
    - windows
    - powershell
    - troubleshooting
    - installation-error
    - cli
    - execution-policy
category: guide
---

## Fixing Failed CLI Installations on Windows

When installing Claude Code or OpenAI Codex through the [Universal AI Platform](https://docs.zencoder.ai/features/universal-cli-platform) on Windows, you may encounter PowerShell execution policy errors that prevent the installation from completing.

## The Issue

During the installation process, you might see an error message like this:

```
C:\Users\[Username]\AppData\Local\Temp\InstallClaudeCode.ps1 : File 
C:\Users\[Username]\AppData\Local\Temp\InstallClaudeCode.ps1 cannot be loaded 
because running scripts is disabled on this system. 
For more information, see about_Execution_Policies at 
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ C:\Users\[Username]\AppData\Local\Temp\InstallClaudeCode.ps1
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

## The Solution

To resolve this issue, you need to modify PowerShell’s execution policy for your user account.