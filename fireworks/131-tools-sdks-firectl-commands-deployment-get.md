---
title: firectl deployment get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-get
source: sitemap
fetched_at: 2026-04-27T20:17:49.464056771-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - cli-command
    - deployment
category: reference
word_count: 88
---
Retrieve details for a specific deployment.

```bash
firectl deployment get [flags]
```

### Examples

```bash
firectl deployment get my-deployment
firectl deployment get accounts/my-account/deployments/my-deployment
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
