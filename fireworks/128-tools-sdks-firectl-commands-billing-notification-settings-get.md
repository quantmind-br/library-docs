---
title: firectl billing notification-settings get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/billing-notification-settings-get
source: sitemap
fetched_at: 2026-04-27T20:17:00.548092773-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - cli-command
    - billing
category: reference
word_count: 90
---
Retrieve current billing notification settings for the account.

```bash
firectl billing notification-settings get [flags]
```

### Example

```bash
firectl billing notification-settings get
```

### Flags

| Flag | Description |
|------|-------------|
| `--dry-run` | Print the request proto without executing |
| `-h, --help` | Help for get |
| `-o, --output` | Output format: `text`, `json`, or `flag` (default: `text`) |

### Global Flags

| Flag | Description |
|------|-------------|
| `-a, --account-id` | Fireworks account ID (reads from `~/.fireworks/auth.ini` if unset) |
| `--api-key` | API key for authentication |
| `-p, --profile` | Auth and settings profile to use |
