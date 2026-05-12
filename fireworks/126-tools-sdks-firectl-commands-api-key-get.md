---
title: firectl api-key get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/api-key-get
source: sitemap
fetched_at: 2026-04-27T20:16:59.533963929-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - cli-command
    - api-key
category: reference
word_count: 89
---
Retrieve an API key by its ID.

```bash
firectl api-key get [flags]
```

### Example

```bash
firectl api-key get <key-id>
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
