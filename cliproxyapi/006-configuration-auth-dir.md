---
title: Authentication Directory | CLIProxyAPI
url: https://help.router-for.me/configuration/auth-dir
source: crawler
fetched_at: 2026-01-14T22:09:56.916500644-03:00
rendered_js: false
word_count: 40
summary: This document explains the purpose and function of the `auth-dir` parameter, which specifies the directory for storing authentication tokens used by the application.
tags:
    - authentication
    - tokens
    - configuration
    - auth-dir
    - google-accounts
category: configuration
---

The `auth-dir` parameter specifies where authentication tokens are stored. When you run the login command, the application will create JSON files in this directory containing the authentication tokens for your Google accounts. Multiple accounts can be used for load balancing.