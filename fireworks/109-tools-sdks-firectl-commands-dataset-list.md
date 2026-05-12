---
title: firectl dataset list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/dataset-list
source: sitemap
fetched_at: 2026-04-27T20:17:04.418195419-03:00
rendered_js: false
word_count: 164
summary: Lists all datasets in the account.
tags:
    - dataset-listing
    - resource-management
    - firectl
    - cli
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
> [!info] Command
> `firectl dataset list [flags]`

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--filter` | string | | Only list resources matching the filter. See [AIP-160 filter grammar](https://google.aip.dev/160) |
| `-h`, `--help` | | | Help for list |
| `--no-paginate` | | | List all resources without pagination |
| `--order-by` | string | | Fields to order by. Append ` desc` for descending |
| `-o`, `--output` | string | `text` | Output format: `text` or `json` |
| `--page-size` | int32 | | Maximum resources per page |
| `--page-token` | string | | Page number (0 to total pages) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if not set |
| `--api-key` | string | API key for authentication |
| `-p`, `--profile` | string | Auth and settings profile to use |

#dataset #firectl