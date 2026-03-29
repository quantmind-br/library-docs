---
title: 'Claude Code (Anthropic via OAuth):'
url: https://help.router-for.me/configuration/provider/claude-code
source: crawler
fetched_at: 2026-01-14T22:09:59.512815832-03:00
rendered_js: false
word_count: 24
summary: This document explains how to use the `cli-proxy-api` command to log in to Claude, including options to control browser behavior and the callback port.
tags:
    - cli
    - proxy-api
    - claude-login
    - oauth
    - command-line
category: guide
---

[Skip to content](#VPContent)

bash

```
./cli-proxy-api --claude-login
```

Options: add `--no-browser` to print the login URL instead of opening a browser. The local OAuth callback uses port `54545`.