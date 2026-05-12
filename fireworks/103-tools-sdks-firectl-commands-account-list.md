---
title: firectl account list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/account-list
source: sitemap
fetched_at: 2026-04-27T20:17:01.788535609-03:00
rendered_js: false
word_count: 175
summary: This document details the various command-line flags available for the `firectl account list` command, explaining how users can customize the listing process.
tags:
    - command-line
    - account-listing
    - flags
    - filtering
    - pagination
    - api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl account list

List all accounts accessible to the authenticated user.

```bash
firectl account list [flags]
```

## Flags

| Flag | Type | Default | Description |
|---|---|---|---|
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

#command-line #account-listing #firectl
