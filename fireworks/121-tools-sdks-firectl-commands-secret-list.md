---
title: firectl secret list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/secret-list
source: sitemap
fetched_at: 2026-04-27T20:16:36.406633408-03:00
rendered_js: false
word_count: 153
summary: List secrets with filtering, ordering, pagination, and output formatting options.
tags:
    - cli-command
    - secret-listing
    - flags
    - reference
    - authentication
    - output-formatting
category: reference
optimized: true
optimized_at: 2026-04-27T20:00:00Z
---
```bash
firectl secret list [flags]
```

### Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--filter` | string | — | Only resources matching the filter. See [AIP-160](https://google.aip.dev/160) for grammar. |
| `--no-paginate` | flag | false | List all resources without pagination. |
| `--order-by` | string | — | Fields to order by. Append ` desc` for descending. |
| `-o, --output` | string | `text` | Output format: `text` or `json`. |
| `--page-size` | int32 | — | Maximum resources per page. |
| `--page-token` | string | — | Page to list (0 to total pages). |

### Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | Auth and settings profile to use. |

#firectl #cli #secret-list #reference