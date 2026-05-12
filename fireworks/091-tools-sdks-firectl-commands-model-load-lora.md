---
title: firectl model load-lora - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-load-lora
source: sitemap
fetched_at: 2026-04-27T20:17:30.081019472-03:00
rendered_js: false
word_count: 166
summary: This document describes the `firectl model load-lora` command, detailing how to load a LoRA model into a specific deployment resource.
tags:
    - model-loading
    - lora
    - deployment
    - fireworks-cli
    - usage
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Loads a LoRA model to a dedicated deployment. If successful, a DeployedModel resource will be created.

```bash
firectl model load-lora [flags]
```

## Examples

```bash
firectl model load-lora my-lora --deployment my-deployment
```

## Flags

| Flag | Type | Description |
|---|---|---|
| `--deployment` | string | The resource ID of the deployment where the LoRA model is to be loaded. |
| `--public` | | If true, the LoRA model will be publicly available for inference. |
| `--replace-merged-addon` | | Required when loading an addon to a hot reload deployment. Replaces an existing addon if one exists. |
| `--wait` | | Wait until the model is deployed. |
| `--wait-timeout` | duration | Maximum time to wait when using `--wait` flag. (default `30m0s`) |

## Global flags

| Flag | Short | Description |
|---|---|---|
| `--account-id` | `-a` | The Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini`. |
| `--api-key` | | An API key used to authenticate with Fireworks. |
| `--profile` | `-p` | fireworks auth and settings profile to use. |
