---
title: firectl model update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-update
source: sitemap
fetched_at: 2026-04-27T20:17:35.758962683-03:00
rendered_js: false
word_count: 223
summary: Update a model's metadata including display name, description, URLs, and capability flags.
tags:
    - command-reference
    - model-update
    - flags
    - fireworks-cli
    - configuration
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl model update

Update a model's metadata.

```bash
firectl model update [flags]
```

## Positional Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `model` | string | Model name or resource name |

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--default-draft-model` | string | Default speculative draft model for deployments |
| `--default-draft-token-count` | int32 | Default speculative draft token count for deployments |
| `--description` | string | Model description |
| `--display-name` | string | Display name |
| `--dry-run` | flag | Print the request proto without running it |
| `--github-url` | string | GitHub URL of the model |
| `--hugging-face-url` | string | Hugging Face URL of the model |
| `--public` | flag | Whether the model is publicly accessible |
| `--supports-image-input` | flag | Whether the model supports image inputs |
| `--supports-tools` | flag | Whether the model supports function calling |
| `-o, --output` | Output | Output format: `text`, `json`, or `flag` (default `text`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |

## Examples

```bash
firectl model update my-model --display-name="New Name"

firectl model update accounts/my-account/models/my-model --display-name="New Name"
```

#firectl #model #update #cli
