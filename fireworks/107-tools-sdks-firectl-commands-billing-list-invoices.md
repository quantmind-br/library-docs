---
title: firectl billing list-invoices
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/billing-list-invoices
source: sitemap
fetched_at: 2026-04-27T20:17:55.169099464-03:00
rendered_js: false
word_count: 98
summary: Lists all billing invoices for the account.
tags:
    - billing-management
    - invoice-listing
    - firectl
    - cli
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
> [!info] Command
> `firectl billing list-invoices [flags]`

## Examples

```
firectl billing list-invoices
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `-h`, `--help` | | | Help for list-invoices |
| `--show-pending` | bool | | If true, only pending invoices are shown |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a`, `--account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if not set |
| `--api-key` | string | API key for authentication |
| `-p`, `--profile` | string | Auth and settings profile to use |

#billing #firectl