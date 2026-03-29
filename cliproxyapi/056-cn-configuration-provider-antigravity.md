---
title: '反重力 (反重力 OAuth 登录): | CLIProxyAPI'
url: https://help.router-for.me/cn/configuration/provider/antigravity
source: crawler
fetched_at: 2026-01-14T22:10:11.505666386-03:00
rendered_js: false
word_count: 12
summary: This document explains how to use the cli-proxy-api command with the --antigravity-login flag to initiate an OAuth login process, including how to specify the local OAuth callback port and prevent automatic browser opening.
tags:
    - cli-proxy-api
    - oauth-login
    - command-line-interface
    - local-port
    - browser-option
category: tutorial
---

[跳转到内容](#VPContent)

bash

```
./cli-proxy-api --antigravity-login
```

本地 OAuth 回调端口为 `51121`。

选项：加上 `--no-browser` 可打印登录地址而不自动打开浏览器。本地 OAuth 回调端口为 `51121`。