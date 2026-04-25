---
title: List Models
url: https://lmstudio.ai/docs/developer/openai-compat/models
source: sitemap
fetched_at: 2026-04-07T21:30:38.870945113-03:00
rendered_js: false
word_count: 39
summary: This section explains how to list all available models using the OpenAI-compatible endpoint via a GET request.
tags:
    - openai-compatibility
    - list-models
    - endpoint
    - api-call
    - http-get
category: reference
---

OpenAI Compatible Endpoints

List available models via the OpenAI-compatible endpoint.

- Method: `GET`
- Returns the models visible to the server. The list may include all downloaded models when Just‑In‑Time loading is enabled.

##### cURL

```

curl http://localhost:1234/v1/models
```

This page's source is available on [GitHub](https://github.com/lmstudio-ai/docs/blob/main/1_developer/3_openai-compat/models.md)