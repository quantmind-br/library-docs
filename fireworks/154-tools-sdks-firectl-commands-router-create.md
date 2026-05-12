---
title: firectl router create
optimized: true
optimized_at: 2026-04-27T20:16:22Z
source: sitemap
fetched_at: 2026-04-27T20:16:22.155115038-03:00
rendered_js: false
tags:
    - cli-command
    - router-creation
    - flag-reference
    - traffic-routing
    - fireworks
category: reference
word_count: 172
---
Create a new traffic router.

```
firectl router create [flags]
```

### Examples

```
firectl router create --deployments=my-deployment1,my-deployment2
firectl router create --strategy=even-load --deployments=my-deployment1,my-deployment2
firectl router create --strategy=weighted-random --deployments=my-deployment1,my-deployment2
```

### Flags

| Flag | Type | Description |
|------|------|-------------|
| `--display-name` | string | Display name of the router |
| `--model` | string | Model to route traffic to |
| `--strategy` | string | Routing strategy (default `weighted-random`) |
| `--deployments` | strings | Deployment names covered by the router |
| `--router-id` | string | Router ID (randomly generated if unset) |
| `--public` | | Make router publicly accessible (private by default) |
| `--dry-run` | | Print the request proto without running it |
| `-o, --output` | Output | Set output format: `text`, `json`, or `flag` (default `text`) |
| `-h, --help` | | help for create |

### Global flags

| Flag | Type | Description |
|------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Falls back to `~/.fireworks/auth.ini` if unset |
| `--api-key` | string | API key for authentication |
| `-p, --profile` | string | Auth and settings profile to use |