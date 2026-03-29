---
title: 'Qwen (Qwen Chat via OAuth):'
url: https://help.router-for.me/configuration/provider/qwen-code
source: crawler
fetched_at: 2026-01-14T22:10:00.619827017-03:00
rendered_js: false
word_count: 24
summary: This document explains how to log in to Qwen Chat using the CLI proxy API, offering an option to avoid opening a browser and instead print a login URL.
tags:
    - cli-proxy-api
    - qwen-login
    - oauth
    - device-flow
    - login-url
category: tutorial
---

[Skip to content](#VPContent)

bash

```
./cli-proxy-api --qwen-login
```

Options: add `--no-browser` to print the login URL instead of opening a browser. Use the Qwen Chat's OAuth device flow.