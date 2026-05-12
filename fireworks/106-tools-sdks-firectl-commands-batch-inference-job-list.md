---
title: firectl batch-inference-job list
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/batch-inference-job-list
source: sitemap
fetched_at: 2026-04-27T20:16:58.784232035-03:00
rendered_js: false
word_count: 177
summary: This document describes the command `firectl batch-inference-job list`, detailing its purpose which is to retrieve a list of available batch inference jobs, along with various flags to customize the listing operation.
tags:
    - firectl
    - batch-inference-job
    - list
    - command-line
    - flags
    - api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl batch-inference-job list

List all batch inference jobs in the account.

```bash
firectl batch-inference-job list [flags]
```

## Examples

```bash
firectl batch-inference-job list
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

#firectl #batch-inference-job #command-line
