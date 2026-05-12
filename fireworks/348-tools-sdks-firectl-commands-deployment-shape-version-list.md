---
title: firectl deployment-shape-version list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-shape-version-list
source: sitemap
fetched_at: 2026-04-27T20:16:45.128837686-03:00
rendered_js: false
word_count: 178
summary: This document provides the command structure and available flags for listing deployment shape versions using the `firectl` command line interface.
tags:
    - command-line
    - deployment-shape
    - version-listing
    - flags
    - firectl
category: reference
optimized: true
optimized_at: 2026-04-27T20:16:45.128837686-03:00
---
# firectl deployment-shape-version list

List deployment shape versions.

```bash
firectl deployment-shape-version list [flags]
```

## Examples

```bash
firectl deployment-shape-version list my-deployment-shape
firectl deployment-shape-version list accounts/my-account/deploymentShapes/my-deployment-shape
firectl deployment-shape-version list
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--base-model` | string | Filter out versions not matching the given base model. |
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

#command-line #deployment-shape #version-listing #firectl
