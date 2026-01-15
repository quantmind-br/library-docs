---
title: 凭证目录 | CLIProxyAPI
url: https://help.router-for.me/cn/configuration/auth-dir
source: crawler
fetched_at: 2026-01-14T22:10:08.518085634-03:00
rendered_js: false
word_count: 9
summary: This document explains the `auth-dir` parameter, which specifies the location where Google account authentication tokens are stored in JSON files after running a login command.
tags:
    - authentication
    - credentials
    - auth-dir
    - token-storage
    - google-accounts
category: configuration
---

## 凭证目录 [​](#%E5%87%AD%E8%AF%81%E7%9B%AE%E5%BD%95)

`auth-dir` 参数指定凭证目录的存储位置。 当您运行登录命令时，应用程序将在此目录中创建包含 Google 账户身份验证令牌的 JSON 文件。多个账户可用于轮询。