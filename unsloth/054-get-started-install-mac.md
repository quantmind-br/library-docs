---
title: Install Unsloth on MacOS
url: https://unsloth.ai/docs/get-started/install/mac.md
source: llms
fetched_at: 2026-04-27T18:12:55.96547726-03:00
rendered_js: false
word_count: 406
summary: This document provides a comprehensive guide on installing Unsloth locally on macOS, detailing the necessary commands for initial installation and launching the studio. It also outlines clear procedures for uninstalling Unsloth components and managing cached model files.
tags:
    - mac-os
    - unsloth
    - installation
    - macos-guide
    - cli
    - caching
    - studio
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Install Unsloth on MacOS

## Install

```bash
curl -fsSL https://unsloth.ai/install.sh | sh
```

Use the same command to update, or run `unsloth studio update`.

## Launch

```bash
unsloth studio -H 0.0.0.0 -p 8888
```

For detailed Studio install instructions and requirements, see the [Unsloth Studio Installation](https://unsloth.ai/docs/new/studio/install) guide.

## Uninstall

Four-step process to remove Unsloth Studio on macOS:

1. **Remove the application** — `rm -rf ~/.unsloth/studio/unsloth_studio` (keeps checkpoints, exports, history, cache, and chats intact)
2. **Remove shortcuts and symlinks:**

   ```bash
   rm -rf ~/Applications/Unsloth\ Studio.app ~/Desktop/Unsloth\ Studio
   ```

3. **Remove the CLI command:**

   ```bash
   rm -f ~/.local/bin/unsloth
   ```

4. **Remove everything (optional)** — `rm -rf ~/.unsloth` (also deletes history, cache, chats, model checkpoints, and exports)

> [!warning]
> `rm -rf` commands delete everything including history, cache, and chats.

> [!info]
> Downloaded HF model files are stored separately in the Hugging Face cache. None of the uninstall steps above remove them. See **Deleting model files** below.

If dependency issues persist, force reinstall:

```bash
pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth
pip install --upgrade --force-reinstall --no-cache-dir --no-deps unsloth_zoo
```

## Deleting Model Files

Delete old model files via the bin icon in model search, or by removing cached model folders from the HF cache directory.

Default cache location:

```bash
~/.cache/huggingface/hub/
```

If `HF_HUB_CACHE` or `HF_HOME` is set, use that location. On Linux/WSL, `XDG_CACHE_HOME` can also change the default cache root. Check the effective path:

```bash
echo ${HF_HUB_CACHE:-${HF_HOME:-${XDG_CACHE_HOME:-$HOME/.cache}/huggingface}/hub}
```

To delete a specific model, remove its folder (e.g. `models--unsloth--Llama-3.1-8B-bnb-4bit`) from the cache directory. To clear all cached models:

```bash
rm -rf ~/.cache/huggingface/hub/
```

#mac-os #installation #unsloth #caching
