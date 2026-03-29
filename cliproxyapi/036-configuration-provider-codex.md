---
title: 'Codex (OpenAI via OAuth): | CLIProxyAPI'
url: https://help.router-for.me/configuration/provider/codex
source: crawler
fetched_at: 2026-01-14T22:09:58.729979006-03:00
rendered_js: false
word_count: 24
summary: This document provides instructions on how to log into the CLI proxy API using a bash command. It also mentions an option to prevent the browser from opening and specifies the local OAuth callback port.
tags:
    - cli-proxy-api
    - login
    - oauth
    - bash
    - command-line
category: tutorial
---

[Skip to content](#VPContent)

bash

```
./cli-proxy-api --codex-login
```

Options: add `--no-browser` to print the login URL instead of opening a browser. The local OAuth callback uses port `1455`.