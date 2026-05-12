---
title: firectl deployment-shape-version get
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-shape-version-get
source: sitemap
fetched_at: 2026-04-27T20:17:52.569259482-03:00
rendered_js: false
word_count: 113
summary: This documentation details the command structure and available flags for using `firectl` to retrieve deployment shape versions.
tags:
    - firectl
    - deployment-shape-version
    - get
    - flags
    - api-command
category: reference
optimized: true
optimized_at: 2026-04-27T20:17:52.569259482-03:00
---
# firectl deployment-shape-version get

Get a specific deployment shape version.

```bash
firectl deployment-shape-version get [flags]
```

## Examples

```bash
firectl deployment-shape-version get accounts/my-account/deploymentShapes/my-deployment-shape/versions/my-version
firectl deployment-shape-version get accounts/my-account/deploymentShapes/my-deployment-shape/versions/latest
```

## Flags

| Flag | Type | Description |
|------|------|-------------|
| `--dry-run` | | Print the request proto without running it. |
| `-h, --help` | | Help for get |
| `-o, --output` | Output | Output format: `text`, `json`, or `flag` (default: `text`) |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if not specified. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |

#firectl #deployment-shape-version #get #api-command
