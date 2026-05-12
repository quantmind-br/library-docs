---
title: firectl reservation list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/reservation-list
source: sitemap
fetched_at: 2026-04-27T20:16:39.876970964-03:00
rendered_js: false
word_count: 167
summary: List reservations with filtering, ordering, pagination, output formatting, and inactive-reservation visibility options.
tags:
    - command-line
    - reservation-list
    - flags
    - filtering
    - pagination
    - output-format
    - global-options
category: reference
optimized: true
optimized_at: 2026-04-27T20:00:00Z
---
```bash
firectl reservation list [flags]
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
| `--show-inactive` | flag | false | Show all reservations including inactive ones. |

### Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | Auth and settings profile to use. |

#firectl #cli #reservation-list #reference