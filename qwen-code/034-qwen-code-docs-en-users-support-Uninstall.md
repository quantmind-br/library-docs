---
title: Uninstall
url: https://qwenlm.github.io/qwen-code-docs/en/users/support/Uninstall
source: github_pages
fetched_at: 2026-04-09T09:04:29.587002308-03:00
rendered_js: true
word_count: 140
summary: This document provides instructions on how to properly uninstall a CLI tool, differentiating the steps required based on whether it was initially run via npx or installed globally using npm.
tags:
    - uninstall
    - npm-cli
    - npx
    - global-installation
    - cleanup
    - command-line
category: guide
---

Your uninstall method depends on how you ran the CLI. Follow the instructions for either npx or a global npm installation.

## Method 1: Using npx[](#method-1-using-npx)

npx runs packages from a temporary cache without a permanent installation. To “uninstall” the CLI, you must clear this cache, which will remove qwen-code and any other packages previously executed with npx.

The npx cache is a directory named `_npx` inside your main npm cache folder. You can find your npm cache path by running `npm config get cache`.

**For macOS / Linux**

```
# The path is typically ~/.npm/_npx
rm -rf "$(npm config get cache)/_npx"
```

**For Windows**

*Command Prompt*

```
:: The path is typically %LocalAppData%\npm-cache\_npx
rmdir /s /q "%LocalAppData%\npm-cache\_npx"
```

*PowerShell*

```
# The path is typically $env:LocalAppData\npm-cache\_npx
Remove-Item -Path (Join-Path $env:LocalAppData "npm-cache\_npx") -Recurse -Force
```

## Method 2: Using npm (Global Install)[](#method-2-using-npm-global-install)

If you installed the CLI globally (e.g. `npm install -g @qwen-code/qwen-code`), use the `npm uninstall` command with the `-g` flag to remove it.

```
npm uninstall -g @qwen-code/qwen-code
```

This command completely removes the package from your system.

Last updated on March 31, 2026

[Terms of Service](https://qwenlm.github.io/qwen-code-docs/en/users/support/tos-privacy/ "Terms of Service")[Introduction](https://qwenlm.github.io/qwen-code-docs/en/users/ide-integration/ide-integration/ "Introduction")