---
title: Installation | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/getting-started/installation
source: crawler
fetched_at: 2026-04-24T17:00:00.554720468-03:00
rendered_js: false
word_count: 378
summary: This document provides comprehensive instructions on getting the Hermes Agent up and running quickly using a one-line installer script for various operating systems like Linux, macOS, Android, and WSL2. It details prerequisites, post-installation steps, and troubleshooting guides.
tags:
    - hermes-agent
    - quick-install
    - setup-guide
    - cli-tool
    - linux-macos
    - android-termux
category: tutorial
---

Get Hermes Agent up and running in under two minutes with the one-line installer.

## Quick Install[​](#quick-install "Direct link to Quick Install")

### Linux / macOS / WSL2[​](#linux--macos--wsl2 "Direct link to Linux / macOS / WSL2")

```bash
curl-fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh |bash
```

### Android / Termux[​](#android--termux "Direct link to Android / Termux")

Hermes now ships a Termux-aware installer path too:

```bash
curl-fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh |bash
```

The installer detects Termux automatically and switches to a tested Android flow:

- uses Termux `pkg` for system dependencies (`git`, `python`, `nodejs`, `ripgrep`, `ffmpeg`, build tools)
- creates the virtualenv with `python -m venv`
- exports `ANDROID_API_LEVEL` automatically for Android wheel builds
- installs a curated `.[termux]` extra with `pip`
- skips the untested browser / WhatsApp bootstrap by default

If you want the fully explicit path, follow the dedicated [Termux guide](https://hermes-agent.nousresearch.com/docs/getting-started/termux).

Windows

Native Windows is **not supported**. Please install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) and run Hermes Agent from there. The install command above works inside WSL2.

### What the Installer Does[​](#what-the-installer-does "Direct link to What the Installer Does")

The installer handles everything automatically — all dependencies (Python, Node.js, ripgrep, ffmpeg), the repo clone, virtual environment, global `hermes` command setup, and LLM provider configuration. By the end, you're ready to chat.

### After Installation[​](#after-installation "Direct link to After Installation")

Reload your shell and start chatting:

```bash
source ~/.bashrc   # or: source ~/.zshrc
hermes             # Start chatting!
```

To reconfigure individual settings later, use the dedicated commands:

```bash
hermes model          # Choose your LLM provider and model
hermes tools          # Configure which tools are enabled
hermes gateway setup  # Set up messaging platforms
hermes config set# Set individual config values
hermes setup          # Or run the full setup wizard to configure everything at once
```

* * *

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

The only prerequisite is **Git**. The installer automatically handles everything else:

- **uv** (fast Python package manager)
- **Python 3.11** (via uv, no sudo needed)
- **Node.js v22** (for browser automation and WhatsApp bridge)
- **ripgrep** (fast file search)
- **ffmpeg** (audio format conversion for TTS)

info

You do **not** need to install Python, Node.js, ripgrep, or ffmpeg manually. The installer detects what's missing and installs it for you. Just make sure `git` is available (`git --version`).

Nix users

If you use Nix (on NixOS, macOS, or Linux), there's a dedicated setup path with a Nix flake, declarative NixOS module, and optional container mode. See the [**Nix & NixOS Setup**](https://hermes-agent.nousresearch.com/docs/getting-started/nix-setup) guide.

* * *

## Manual / Developer Installation[​](#manual--developer-installation "Direct link to Manual / Developer Installation")

If you want to clone the repo and install from source — for contributing, running from a specific branch, or having full control over the virtual environment — see the [Development Setup](https://hermes-agent.nousresearch.com/docs/developer-guide/contributing#development-setup) section in the Contributing guide.

* * *

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

ProblemSolution`hermes: command not found`Reload your shell (`source ~/.bashrc`) or check PATH`API key not set`Run `hermes model` to configure your provider, or `hermes config set OPENROUTER_API_KEY your_key`Missing config after updateRun `hermes config check` then `hermes config migrate`

For more diagnostics, run `hermes doctor` — it will tell you exactly what's missing and how to fix it.