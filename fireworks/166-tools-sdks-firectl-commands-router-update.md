---
title: firectl router update - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/router-update
source: sitemap
fetched_at: 2026-04-27T20:16:27.442381709-03:00
rendered_js: false
word_count: 190
summary: Update a router's configuration including deployments, strategy, display name, and visibility.
tags:
    - firectl-router
    - update
    - cli-command
    - routing
    - deployment
    - configuration
category: reference
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
# firectl router update

Update a router's configuration.

```bash
firectl router update [flags]
```

## Positional Arguments

| Argument | Type | Description |
|----------|------|-------------|
| `router` | string | Router name |

## Flags

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--deployments` | strings | — | Deployment names covered by the router |
| `--display-name` | string | — | Display name of the router |
| `--dry-run` | flag | — | Print the request proto without running it |
| `--public` | flag | — | Make the router publicly reachable |
| `--session-affinity` | flag | — | Enable regional-level session affinity |
| `--strategy` | string | `weighted-random` | Routing strategy: `weighted-random` or `even-load` |
| `-o, --output` | Output | `text` | Output format: `text`, `json`, or `flag` |

## Global Flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |

## Examples

```bash
firectl router update my-router --deployments=my-deployment1,my-deployment2

firectl router update my-router --strategy=weighted-random

firectl router update my-router --strategy=even-load
```

#firectl #router #update #routing #cli
