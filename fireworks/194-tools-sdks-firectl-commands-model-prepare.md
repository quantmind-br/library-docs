---
title: firectl model prepare - Fireworks AI Docs
url: https://docs.fireworks.ai/tools-sdks/firectl/commands/model-prepare
source: sitemap
fetched_at: 2026-04-27T20:17:30.841701114-03:00
rendered_js: false
word_count: 89
summary: This document outlines the usage of the `firectl model prepare` command, detailing its purpose and providing available flags for various functionalities.
tags:
    - command-line
    - model-preparation
    - firectl
    - flags
    - help
    - account-id
category: reference
optimized: true
optimized_at: 2026-04-27T20:44:11Z
---
```bash
firectl model prepare [flags]
```

**Examples**

```bash
firectl model prepare my-model
firectl model prepare accounts/my-account/models/my-model
```

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--wait` | flag | — | Wait until the model preparation is complete. |
| `--wait-timeout` | duration | `30m0s` | Maximum time to wait when using `--wait`. |

| Global Flag | Type | Description |
|-------------|------|-------------|
| `-a, --account-id` | string | Fireworks account ID. Reads from `~/.fireworks/auth.ini` if unset. |
| `--api-key` | string | API key for authentication. |
| `-p, --profile` | string | fireworks auth and settings profile to use. |