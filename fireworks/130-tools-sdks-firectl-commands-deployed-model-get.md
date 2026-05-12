---
title: firectl deployed-model get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployed-model-get
source: sitemap
fetched_at: 2026-04-27T20:17:48.293812157-03:00
rendered_js: false
optimized: true
optimized_at: 2026-04-27T00:00:00Z
tags:
    - cli-command
    - deployed-model
category: reference
word_count: 88
---
Retrieve details for a deployed model.

```bash
firectl deployed-model get [flags]
```

### Examples

```bash
firectl deployed-model get my-deployed-model
firectl deployed-model get accounts/my-account/deployedModels/my-deployed-model
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
