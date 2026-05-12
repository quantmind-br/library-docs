---
title: firectl api-key list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/api-key-list
source: sitemap
fetched_at: 2026-04-27T20:17:02.303565959-03:00
rendered_js: false
word_count: 195
summary: This document details the command syntax and available flags for the `firectl api-key list` command, explaining how users can retrieve lists of API keys with various filtering, ordering, and formatting options.
tags:
    - command-reference
    - api-key-listing
    - flag-options
    - list-command
    - firectl
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl api-key list

List API keys for the authenticated user or account.

```bash
firectl api-key list [flags]
```

## Flags

| Flag | Type | Default | Description |
|---|---|---|---|
| `--all-users` | bool | `false` | Admin only: list API keys for all users in the account. |
| `--filter` | string | — | Only resources satisfying the provided filter. See [AIP-160 filter grammar](https://google.aip.dev/160). |
| `--no-paginate` | bool | `false` | List all resources without pagination. |
| `--order-by` | string | — | Fields to order by. Append ` desc` for descending. |
| `-o`, `--output` | string | `text` | Output format: `text` or `json`. |
| `--page-size` | int32 | — | Maximum number of resources to list per page. |
| `--page-token` | string | — | Page number to list (0 to total pages). |

## Global flags

| Flag | Type | Description |
|---|---|---|
| `-a`, `--account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini`. |
| `--api-key` | string | API key used to authenticate with Fireworks. |
| `-p`, `--profile` | string | Fireworks auth and settings profile to use. |

#command-reference #api-key-listing #firectl
