---
title: firectl api-key create
optimized: true
optimized_at: 2026-04-27T20:18:04Z
source: sitemap
fetched_at: 2026-04-27T20:18:04.886238131-03:00
rendered_js: false
tags:
    - api-creation
    - command-line
    - flags
    - api-key
    - service-account
    - fireworks
category: reference
word_count: 143
---
Create a new API key.

```
firectl api-key create [flags]
```

### Examples

```
firectl api-key create
firectl api-key create --service-account=my-service-account
firectl api-key create --key-name="Production Key" --service-account=ci-bot
firectl api-key create --key-name="Temporary Key" --expire-time="2025-12-31 23:59:59"
```

### Flags

| Flag | Type | Description |
|------|------|-------------|
| `--dry-run` | | Print the request proto without running it |
| `--expire-time` | string | Expiry time in `YYYY-MM-DD[ HH:MM:SS]` format |
| `--key-name` | string | Name of the key (default `default`) |
| `-o, --output` | Output | Set output format: `text`, `json`, or `flag` (default `text`) |
| `--service-account` | string | Admin only: create key for the specified service account |
| `-h, --help` | | help for create |

### Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Falls back to `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |