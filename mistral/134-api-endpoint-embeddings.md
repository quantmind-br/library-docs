---
title: Embeddings
url: https://docs.mistral.ai/api/endpoint/embeddings
source: crawler
fetched_at: 2026-01-29T07:33:18.469693915-03:00
rendered_js: false
word_count: 0
summary: This document provides an example of the JSON response structure for a text embedding API, detailing the format of embedding vectors and usage statistics.
tags:
    - api-response
    - embeddings
    - mistral-ai
    - json-format
    - vector-data
category: reference
---

```
{"data":[{"embedding":[-0.016632080078125,0.0701904296875,0.03143310546875,0.01309967041015625,0.0202789306640625],"index":0,"object":"embedding"},{"embedding":[-0.0230560302734375,0.039337158203125,0.0521240234375,-0.0184783935546875,0.034271240234375],"index":1,"object":"embedding"}],"model":"mistral-embed","object":"list","usage":{"prompt_tokens":15,"completion_tokens":0,"total_tokens":15,"prompt_audio_seconds":null}}
```

```
{"data":[{"embedding":[-0.016632080078125,0.0701904296875,0.03143310546875,0.01309967041015625,0.0202789306640625],"index":0,"object":"embedding"},{"embedding":[-0.0230560302734375,0.039337158203125,0.0521240234375,-0.0184783935546875,0.034271240234375],"index":1,"object":"embedding"}],"model":"mistral-embed","object":"list","usage":{"prompt_tokens":15,"completion_tokens":0,"total_tokens":15,"prompt_audio_seconds":null}}
```