---
title: Replay Responses
url: https://epi052.github.io/feroxbuster-docs/examples/replay-proxy
source: github_pages
fetched_at: 2026-02-06T10:56:02.21640665-03:00
rendered_js: true
word_count: 93
summary: This document explains how to use selective proxying in feroxbuster to forward only specific HTTP response status codes to a proxy server.
tags:
    - feroxbuster
    - proxy-configuration
    - http-status-codes
    - web-security
    - command-line-options
category: reference
---

## Replay Responses to a Proxy based on Status Code

[Section titled “Replay Responses to a Proxy based on Status Code”](#replay-responses-to-a-proxy-based-on-status-code)

The `--replay-proxy` and `--replay-codes` options were added as a way to only send a select few responses to a proxy. This is in stark contrast to `--proxy` which proxies EVERY request.

Imagine you only care about proxying responses that have either the status code `200` or `302` (or you just don’t want to clutter up your Burp history). These two options will allow you to fine-tune what gets proxied and what doesn’t.

```

./feroxbuster -u http://127.1 --replay-proxy http://localhost:8080 --replay-codes 200 302 --insecure
```

![replay-proxy-demo](https://epi052.github.io/feroxbuster-docs/images/examples/replay-proxy-demo.gif)