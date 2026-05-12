---
title: firectl dataset update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/dataset-update
source: sitemap
fetched_at: 2026-04-27T20:17:48.765638758-03:00
word_count: 140
summary: Update an existing dataset's display name via the firectl CLI.
tags:
    - dataset-update
    - firectl
    - command-line-interface
    - flags
    - api-interaction
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl dataset update

Update an existing dataset's metadata.

```bash
firectl dataset update [flags]
```

## Positional Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `dataset` | string | Dataset name or resource name (e.g. `my-dataset` or `accounts/my-account/datasets/my-dataset`) |

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--display-name` | string | New display name for the dataset |
| `--dry-run` | flag | Print the request proto without running it |
| `-o, --output` | Output | Output format: `text`, `json`, or `flag` (default `text`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |

## Examples

```bash
firectl dataset update my-dataset

firectl dataset update accounts/my-account/datasets/my-dataset
```

#firectl #dataset #update #cli
