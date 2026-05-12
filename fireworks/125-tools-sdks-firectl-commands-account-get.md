---
title: firectl account get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/account-get
source: sitemap
fetched_at: 2026-04-27T20:18:02.458783423-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - cli-command
    - account-retrieval
category: reference
word_count: 92
---
Retrieve account details by ID or use the default account.

```bash
firectl account get [flags]
```

### Examples

```bash
firectl account get
firectl account get my-account
firectl account get accounts/my-account
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
