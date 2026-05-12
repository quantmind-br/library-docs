---
title: firectl deployment delete - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/deployment-delete
source: sitemap
fetched_at: 2026-04-27T20:17:51.461194202-03:00
rendered_js: false
word_count: 165
summary: This documentation explains the command structure and various flags available for deleting a deployment using the `firectl` tool.
tags:
    - deployment-delete
    - command-line
    - firectl
    - flags
    - api
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl deployment delete

Delete a deployment.

```
firectl deployment delete [flags]
```

## Examples

```bash
firectl deployment delete my-deployment
firectl deployment delete accounts/my-account/deployments/my-deployment
```

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--dry-run` | | | Print the request proto without running it |
| `--hard` | | | Hard delete the deployment |
| `--ignore-checks` | | | Skip checking if the deployment is in use before deleting |
| `-o, --output` | Output | `text` | Set the output format to `text`, `json`, or `flag` |
| `--wait` | | | Wait until the deployment is deleted |
| `--wait-timeout` | duration | `1h0m0s` | Maximum time to wait when using `--wait` flag |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. If not specified, reads from `~/.fireworks/auth.ini` |
| `--api-key` | string | API key used to authenticate with Fireworks |
| `-p, --profile` | string | Fireworks auth and settings profile to use |

#firectl #deployment #delete #command-line #reference
