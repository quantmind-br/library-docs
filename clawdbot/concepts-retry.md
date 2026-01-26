---
title: "null"
url: https://docs.clawd.bot/concepts/retry.md
source: llms
fetched_at: 2026-01-26T10:13:02.904912681-03:00
rendered_js: false
word_count: 142
summary: This document outlines the retry policy and error-handling logic for Discord and Telegram integrations, detailing default settings, platform-specific behaviors, and configuration options.
tags:
    - retry-policy
    - error-handling
    - discord-integration
    - telegram-integration
    - http-requests
    - exponential-backoff
    - rate-limiting
category: configuration
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.clawd.bot/llms.txt
> Use this file to discover all available pages before exploring further.

# null

# Retry policy

## Goals

* Retry per HTTP request, not per multi-step flow.
* Preserve ordering by retrying only the current step.
* Avoid duplicating non-idempotent operations.

## Defaults

* Attempts: 3
* Max delay cap: 30000 ms
* Jitter: 0.1 (10 percent)
* Provider defaults:
  * Telegram min delay: 400 ms
  * Discord min delay: 500 ms

## Behavior

### Discord

* Retries only on rate-limit errors (HTTP 429).
* Uses Discord `retry_after` when available, otherwise exponential backoff.

### Telegram

* Retries on transient errors (429, timeout, connect/reset/closed, temporarily unavailable).
* Uses `retry_after` when available, otherwise exponential backoff.
* Markdown parse errors are not retried; they fall back to plain text.

## Configuration

Set retry policy per provider in `~/.clawdbot/clawdbot.json`:

```json5  theme={null}
{
  channels: {
    telegram: {
      retry: {
        attempts: 3,
        minDelayMs: 400,
        maxDelayMs: 30000,
        jitter: 0.1
      }
    },
    discord: {
      retry: {
        attempts: 3,
        minDelayMs: 500,
        maxDelayMs: 30000,
        jitter: 0.1
      }
    }
  }
}
```

## Notes

* Retries apply per request (message send, media upload, reaction, poll, sticker).
* Composite flows do not retry completed steps.