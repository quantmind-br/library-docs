---
title: 'iFlow (iFlow via OAuth): | CLIProxyAPI'
url: https://help.router-for.me/configuration/provider/iflow
source: crawler
fetched_at: 2026-01-14T22:10:00.020010866-03:00
rendered_js: false
word_count: 24
summary: This document provides instructions on how to log in to the CLI proxy API using a bash command. It also explains an option to prevent a browser from opening and notes the default OAuth callback port.
tags:
    - cli-proxy-api
    - login
    - oauth
    - bash
    - command-line
category: api
---

[Skip to content](#VPContent)

bash

```
./cli-proxy-api --iflow-login
```

Options: add `--no-browser` to print the login URL instead of opening a browser. The local OAuth callback uses port `11451`.