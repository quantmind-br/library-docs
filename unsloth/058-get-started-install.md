---
title: Unsloth Installation
url: https://unsloth.ai/docs/get-started/install.md
source: llms
fetched_at: 2026-04-27T18:12:53.489475868-03:00
rendered_js: false
word_count: 180
summary: This document provides instructions on how to install Unsloth through various methods, including Unsloth Studio (web UI), core code installation for different operating systems like MacOS and Windows, and offers a mechanism to query the documentation dynamically.
tags:
    - unsloth-installation
    - studio-setup
    - system-requirements
    - linux-install
    - windows-ps
    - cli-commands
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Unsloth Installation

Unsloth has two modes: [[098-new-studio-install|Unsloth Studio]] (web UI) or Unsloth Core (code-based). See [[112-get-started-fine-tuning-for-beginners-unsloth-requirements|system requirements]] for prerequisites.

Studio works on MacOS, Linux, Windows, NVIDIA, and more. Use the same install commands to update or run `unsloth studio update`.

## Quick Install

**MacOS, Linux, WSL:**

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

**Windows PowerShell:**

```bash
irm https://unsloth.ai/install.ps1 | iex
```

## Launch

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

## Install Variants

| Platform | Doc |
|---|---|
| MacOS | [[054-get-started-install-mac\|Install on MacOS]] |
| pip / uv | [[055-get-started-install-pip-install\|Install via pip and uv]] |
| Windows | [[057-get-started-install-windows-installation\|Fine-tune LLMs on Windows]] |
| Docker | [[052-get-started-install-docker\|Install via Docker]] |
| Update | [[056-get-started-install-updating\|Updating Unsloth]] |
| AMD GPU | [[051-get-started-install-amd\|Fine-tune on AMD GPUs]] |
| Intel GPU | [[053-get-started-install-intel\|Fine-tune on Intel GPUs]] |
| Conda | [[055-get-started-install-pip-install\|Install via pip and uv]] (conda section) |
| VS Code | [[055-get-started-install-pip-install\|Install via pip and uv]] (vs-code section) |
| Google Colab | [[055-get-started-install-pip-install\|Install via pip and uv]] (colab section) |

#unsloth #installation #studio
