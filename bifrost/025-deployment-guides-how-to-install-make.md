---
title: Install make command
url: https://docs.getbifrost.ai/deployment-guides/how-to/install-make.md
source: llms
fetched_at: 2026-01-21T19:43:17.294141273-03:00
rendered_js: false
word_count: 159
summary: This document provides instructions for installing the make build tool across different operating systems including Windows, Ubuntu, and macOS.
tags:
    - installation
    - make
    - build-tools
    - windows
    - macos
    - ubuntu
    - package-managers
category: guide
---

# Install make command

> This guide explains how to install make command.

## Windows

### Option A: Chocolatey (easy)

```
# Run in an elevated PowerShell (Run as Administrator)
choco install make
# verify
make --version
```

### Option B: Scoop (no admin needed)

```
# In a normal PowerShell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
iwr get.scoop.sh -useb | iex
scoop install make
make --version
```

### Option C: MSYS2 (full Unix-like env)

```
# 1) Install MSYS2 from https://www.msys2.org/
# 2) In "MSYS2 MSYS" terminal:
pacman -Syu         # then reopen terminal if asked
pacman -S make
make --version
```

<Note> Visual Studio’s nmake is a different tool (not GNU make). </Note>

## Ubuntu / Debian

```
sudo apt update
# Pulls in compilers and common build tools, including make
sudo apt install build-essential
# (or just) sudo apt install make
make --version
```

## macOS

### Option A: Xcode Command Line Tools (most common)

```
xcode-select --install   # follow the prompt
make --version
```

This provides Apple’s/BSD-flavored make, which is fine for most projects.

### Option B: Homebrew (get GNU make ≥ 4.x as gmake)

```
# Install Homebrew if needed: https://brew.sh
brew install make
gmake --version
```

If a project specifically requires GNU make as make, you can use:

echo 'alias make="gmake"' >> \~/.zshrc && source \~/.zshrc

## Troubleshooting tips

* If make isn’t found, restart your terminal (or on Windows, open a new PowerShell) so your PATH updates.
* Run which make (where make on Windows) to confirm which binary you’re using.
* For Windows builds that depend on Unix tools (sed, grep, etc.), prefer MSYS2 or WSL for a smoother experience.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt