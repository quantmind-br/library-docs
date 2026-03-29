---
title: 'Antigravity (Antigravity via OAuth): | CLIProxyAPI'
url: https://help.router-for.me/configuration/provider/antigravity
source: crawler
fetched_at: 2026-01-14T22:09:57.678577346-03:00
rendered_js: false
word_count: 28
summary: This document explains how to use the cli-proxy-api tool for antigravity login, including details on the local OAuth callback port and an option to disable automatic browser opening.
tags:
    - cli-proxy-api
    - antigravity-login
    - oauth-callback
    - port-configuration
    - no-browser
category: api
---

bash

```
./cli-proxy-api --antigravity-login
```

The local OAuth callback uses port `51121`.

Options: add `--no-browser` to print the login URL instead of opening a browser. The local OAuth callback uses port `51121`.