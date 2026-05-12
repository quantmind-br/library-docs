---
title: firectl training-shape-version list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/training-shape-version-list
source: sitemap
fetched_at: 2026-04-27T20:16:12.50590246-03:00
rendered_js: false
word_count: 176
summary: This document details the command structure and available flags for the `firectl training-shape-version list` command, allowing users to specify various criteria for listing model versions.
tags:
    - command-line
    - training-shape-version
    - list
    - flags
    - api-interaction
category: reference
optimized: true
optimized_at: 2026-04-27T20:16:12.50590246-03:00
---
# firectl training-shape-version list

List training shape versions.

```bash
firectl training-shape-version list [flags]
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--base-model` | string | Filter versions by base model or compatible latest-validated bucket. |
| `--filter` | string | Only resources satisfying the provided filter. See [AIP-160](https://google.aip.dev/160) for grammar. |
| `--no-paginate` | | List all resources without pagination. |
| `--order-by` | string | Fields to order by. Append ` desc` for descending. |
| `-o, --output` | string | Output format: `text` or `json` (default: `text`) |
| `--page-size` | int32 | Maximum number of resources to list. |
| `--page-token` | string | Page number (0 to total pages). |
| `-h, --help` | | Help for list |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if not specified. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |

#command-line #training-shape-version #list #firectl
