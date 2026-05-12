---
title: firectl model list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-list
source: sitemap
fetched_at: 2026-04-27T20:16:38.625198651-03:00
rendered_js: false
word_count: 209
summary: Lists all models available in the account.
tags:
    - model-listing
    - resource-management
    - firectl
    - cli
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
> [!info] Command
> `firectl model list [flags]`

## Examples

```bash
# List all models
firectl model list

# Search by name (partial match)
firectl model list --search deepseek

# Filter by kind
firectl model list --kind HF_PEFT_ADDON

# Filter by state
firectl model list --state READY

# Combine filters
firectl model list --search deepseek --kind HF_PEFT_ADDON

# Use raw filter for advanced queries
firectl model list --filter 'create_time > timestamp("2025-01-01T00:00:00Z")'
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--filter` | string | | Only list resources matching the filter. See [AIP-160 filter grammar](https://google.aip.dev/160) |
| `-h`, `--help` | | | Help for list |
| `--kind` | string | | Filter by model kind (e.g., `HF_PEFT_ADDON`, `HF_BASE_MODEL`, `DRAFT_ADDON`) |
| `--no-paginate` | | | List all resources without pagination |
| `--order-by` | string | | Fields to order by. Append ` desc` for descending |
| `-o`, `--output` | string | `text` | Output format: `text` or `json` |
| `--page-size` | int32 | | Maximum resources per page |
| `--page-token` | string | | Page number (0 to total pages) |
| `--search` | string | | Filter models by name (searches `model_id` and `display_name`) |
| `--state` | string | | Filter by state (e.g., `READY`, `UPLOADING`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if not set |
| `--api-key` | string | API key for authentication |
| `-p`, `--profile` | string | Auth and settings profile to use |

#model #firectl