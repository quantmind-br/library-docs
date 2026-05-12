---
title: firectl deployed-model update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployed-model-update
source: sitemap
fetched_at: 2026-04-27T20:17:47.798783127-03:00
rendered_js: false
word_count: 189
summary: Update an existing deployed model's metadata including display name, description, and public visibility.
tags:
    - cli-command
    - deployment-update
    - fireworks-tooling
    - flags
    - model-management
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl deployed-model update

Update a deployed model's metadata.

```bash
firectl deployed-model update [flags]
```

## Positional Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `deployed-model` | string | Deployed model name or resource name |

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--default` | flag | If true, this is the default deployment when querying this model without the `#<deployment>` suffix |
| `--description` | string | Description. Must be fewer than 1000 characters |
| `--display-name` | string | Human-readable name. Must be fewer than 64 characters |
| `--dry-run` | flag | Print the request proto without running it |
| `--public` | flag | If true, the deployed model will be publicly reachable |
| `-o, --output` | Output | Output format: `text`, `json`, or `flag` (default `text`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |

## Examples

```bash
firectl deployed-model update my-deployed-model

firectl deployed-model update accounts/my-account/deployedModels/my-deployed-model
```

#firectl #deployed-model #update #cli #deployment
