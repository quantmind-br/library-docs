---
title: 'Gemini CLI (Gemini via OAuth):'
url: https://help.router-for.me/configuration/provider/gemini-cli
source: crawler
fetched_at: 2026-01-14T22:09:58.763657717-03:00
rendered_js: false
word_count: 45
summary: This document explains how to log in to the Gemini Code CLI using the proxy API, including how to specify a project ID and customize the login process.
tags:
    - cli
    - proxy-api
    - login
    - project-id
    - oauth-callback
category: api
---

bash

```
./cli-proxy-api --login
```

If you are an existing `Gemini Code` user, you may need to specify a project ID:

bash

```
./cli-proxy-api --login --project_id <your_project_id>
```

The local OAuth callback uses port `8085`.

Options: add `--no-browser` to print the login URL instead of opening a browser. The local OAuth callback uses port `8085`.