---
title: Gemini CLI | CLIProxyAPI
url: https://help.router-for.me/agent-client/gemini-cli
source: crawler
fetched_at: 2026-01-14T22:10:03.621596415-03:00
rendered_js: false
word_count: 112
summary: 'This document explains how to configure the CLIProxyAPI server for two authentication methods: Google OAuth and Gemini API key.'
tags:
    - cliproxyapi
    - authentication
    - google-oauth
    - gemini-api-key
    - configuration
category: configuration
---

Start CLIProxyAPI server, and choose one of the following configurations depending on your authentication method.

## Login with Google (OAuth) [​](#login-with-google-oauth)

Set the `CODE_ASSIST_ENDPOINT` environment variable to the URL of the CLI Proxy API server.

bash

```
export CODE_ASSIST_ENDPOINT="http://127.0.0.1:8317"
```

The server will relay the `loadCodeAssist`, `onboardUser`, and `countTokens` requests. And automatically load balance the text generation requests between the multiple accounts.

NOTE

This feature only allows local access because there is currently no way to authenticate the requests.  
127.0.0.1 is hardcoded for load balancing.

## Use Gemini API Key [​](#use-gemini-api-key)

Configure the Gemini API base URL and API key:

bash

```
export GOOGLE_GEMINI_BASE_URL="http://127.0.0.1:8317"
export GEMINI_API_KEY="sk-dummy"
```

NOTE

Unlike OAuth mode, this mode allows CLIProxyAPI to be configured as any IP address or domain.