---
title: firectl audit-logs list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/audit-logs-list
source: sitemap
fetched_at: 2026-04-27T20:16:56.157725599-03:00
rendered_js: false
word_count: 222
summary: This documentation explains how to use the `firectl audit-logs list` command to retrieve audit logs for a signed-in user, detailing various filtering options and available flags.
tags:
    - audit-logs
    - list-command
    - filtering
    - cli-usage
    - date-range
    - api-flags
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl audit-logs list

List audit logs for the signed-in user with filtering support. Returns logs from the past 30 days by default.

```bash
firectl audit-logs list [flags]
```

## Examples

```bash
# List all audit logs from the past 30 days
firectl audit-logs list

# Filter by resource (exact or substring match)
firectl audit-logs list --filter 'resource="accounts/my-account/deployments/abc123"'
firectl audit-logs list --filter 'resource="accounts/my-account/models/model123"'
firectl audit-logs list --filter 'resource:model123"'

# Filter by message (exact or substring match)
firectl audit-logs list --filter 'message="CreateDeployment"'
firectl audit-logs list --filter 'message:"Create"'

# Filter by user email
firectl audit-logs list --filter 'email="user@example.com"'

# List logs from a specific date range with filters
firectl audit-logs list --start 2025-01-01 --end 2025-01-02

# Combine multiple filters
firectl audit-logs list --start 2025-01-01 --filter 'resource:"deployment-id"'
```

## Flags

| Flag | Type | Default | Description |
|---|---|---|---|
| `--end` | string | — | End date for audit logs in `YYYY-MM-DD` format. |
| `--filter` | string | — | Only resources satisfying the provided filter. See [AIP-160 filter grammar](https://google.aip.dev/160). |
| `--no-paginate` | bool | `false` | List all resources without pagination. |
| `--order-by` | string | — | Fields to order by. Append ` desc` for descending. |
| `-o`, `--output` | string | `text` | Output format: `text` or `json`. |
| `--page-size` | int32 | — | Maximum number of resources to list per page. |
| `--page-token` | string | — | Page number to list (0 to total pages). |
| `--start` | string | 30 days ago | Start date for audit logs in `YYYY-MM-DD` format. |

## Global flags

| Flag | Type | Description |
|---|---|---|
| `-a`, `--account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini`. |
| `--api-key` | string | API key used to authenticate with Fireworks. |
| `-p`, `--profile` | string | Fireworks auth and settings profile to use. |

#audit-logs #list-command #firectl
