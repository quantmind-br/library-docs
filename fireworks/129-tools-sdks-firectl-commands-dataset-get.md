---
title: firectl dataset get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/dataset-get
source: sitemap
fetched_at: 2026-04-27T20:17:56.878565126-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - cli-command
    - dataset
category: reference
word_count: 87
---
Retrieve a dataset by ID.

```bash
firectl dataset get [flags]
```

### Examples

```bash
firectl dataset get my-dataset
firectl dataset get accounts/my-account/datasets/my-dataset
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
