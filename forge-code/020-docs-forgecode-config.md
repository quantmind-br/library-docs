---
title: ".forge.toml Configuration Reference"
url: https://forgecode.dev/docs/forgecode-config/
source: sitemap
fetched_at: 2026-04-30T14:09:10.698595253-03:00
rendered_js: false
word_count: 238
summary: "Configuration parameters for ForgeCode, covering resource limits, networking, retry logic, and context compaction."
tags:
  - configuration-file
  - application-settings
  - resource-limits
  - http-settings
  - retry-strategy
  - context-management
category: configuration
optimized: true
---
# `.forge.toml` Configuration Reference

> **TL;DR**
> Global settings for resource limits, networking, retries, and context management.

## Schema
```toml
$schema https://forgecode.dev/schema.json
```

## Resource Limits

| Parameter | Default | Description |
|-----------|---------|-------------|
| `max_tokens` | 20480 | Max tokens per response (1–100,000) |
| `max_file_size_bytes` | 104857600 | Max file size (bytes) |
| `max_parallel_file_reads` | 64 | Max concurrent file reads |
| `max_requests_per_turn` | 100 | Max requests per turn |

## Networking

| Parameter | Default | Description |
|-----------|---------|-------------|
| `connect_timeout_secs` | 30 | Connection timeout |
| `read_timeout_secs` | 900 | Read timeout |
| `max_redirects` | 10 | Max HTTP redirects |
| `tls_backend` | `default` | TLS backend (`default` or `rustls`) |

## Retry Logic

| Parameter | Default | Description |
|-----------|---------|-------------|
| `max_attempts` | 8 | Max retry attempts |
| `initial_backoff_ms` | 200 | Initial backoff (ms) |
| `backoff_factor` | 2 | Backoff multiplier |
| `status_codes` | `[429, 500, ...]` | Retry on these HTTP codes |

## Context Compaction

| Parameter | Default | Description |
|-----------|---------|-------------|
| `token_threshold` | 100000 | Tokens before compaction |
| `max_tokens` | 2000 | Tokens after compaction |
| `retention_window` | 6 | Messages to preserve |

## Updates

| Parameter | Default | Description |
|-----------|---------|-------------|
| `auto_update` | `true` | Auto-install updates |
| `frequency` | `daily` | Update check frequency (`daily`, `weekly`, `always`) |

## Full Example
```toml
max_tokens = 20480
max_file_size_bytes = 104857600

[retry]
max_attempts = 8
initial_backoff_ms = 200

[http]
connect_timeout_secs = 30
read_timeout_secs = 900

[compact]
token_threshold = 100000
max_tokens = 2000

[updates]
auto_update = true
frequency = "daily"
```