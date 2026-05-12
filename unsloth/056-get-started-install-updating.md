---
title: Updating Unsloth
url: https://unsloth.ai/docs/get-started/install/updating.md
source: llms
fetched_at: 2026-04-27T18:12:58.215114011-03:00
rendered_js: false
word_count: 194
summary: This document provides multiple methods for updating Unsloth Studio and its core libraries, detailing specific command-line instructions for different operating systems, as well as options for forcing reinstallations or reverting to older versions.
tags:
    - unsloth-update
    - studio-update
    - pip-install
    - macos-linux
    - windows-ps
    - dependency-management
category: guide
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Updating Unsloth

## Update Unsloth Studio

Use the same install commands as initial install:

- **MacOS, Linux, WSL:**

  ```bash
  curl -fsSL https://unsloth.ai/install.sh | sh
  ```

- **Windows PowerShell:**

  ```bash
  irm https://unsloth.ai/install.ps1 | iex
  ```

- **Or use the update command:**

  ```bash
  unsloth studio update
  ```

## Update Unsloth Core

```bash
pip install --upgrade unsloth unsloth_zoo
```

## Update without dependency changes

```bash
pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth
pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth_zoo
```

## Revert to an older version

```bash
pip install --force-reinstall --no-cache-dir --no-deps unsloth==2025.1.5
```

`2025.1.5` is one example; substitute any specific release from [Unsloth GitHub releases](https://github.com/unslothai/unsloth/releases).

#unsloth #updating #pip-install
