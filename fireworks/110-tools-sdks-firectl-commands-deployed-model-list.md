---
title: firectl deployed-model list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployed-model-list
source: sitemap
fetched_at: 2026-04-27T20:16:49.242726069-03:00
rendered_js: false
word_count: 166
summary: Lists all deployed models for the account.
tags:
    - deployed-models
    - resource-listing
    - firectl
    - cli
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
> [!info] Command
> `firectl deployed-model list [flags]`

## Examples

```
firectl deployed-model list
```

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

#deployed-model #firectl