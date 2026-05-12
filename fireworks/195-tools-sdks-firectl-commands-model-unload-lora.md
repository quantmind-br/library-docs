---
title: firectl model unload-lora - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-unload-lora
source: sitemap
fetched_at: 2026-04-27T20:17:27.951411861-03:00
rendered_js: false
word_count: 116
summary: This document describes the usage of the `firectl model unload-lora` command, which is used to remove a specific LoRA model from an existing deployment.
tags:
    - firectl
    - lora-model
    - unload
    - deployment
    - command-line
    - flags
category: reference
optimized: true
optimized_at: 2026-04-27T20:44:11Z
---
Unloads a LoRA model from a dedicated deployment.

```bash
firectl model unload-lora [flags]
```

**Examples**

```bash
firectl model unload-lora my-lora --deployment abcd1234
```

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--deployment` | string | — | Resource name of the deployment where the model is to be undeployed. |
| `--wait` | flag | — | Wait until the model is undeployed. |
| `--wait-timeout` | duration | `30m0s` | Maximum time to wait when using `--wait`. |

| Global Flag | Type | Description |
|-------------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |