---
title: api_server - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/api_server/
source: sitemap
fetched_at: 2026-05-07T21:19:19.872246654-03:00
rendered_js: false
word_count: 123
summary: This document provides a reference for the demonstration API server endpoints used for testing AsyncEngine and performance benchmarks in vLLM.
tags:
    - vllm
    - api-server
    - async-engine
    - performance-testing
    - api-reference
    - health-check
category: api
---

## vllm.entrypoints.api\_server [¶](#vllm.entrypoints.api_server "Permanent link")

NOTE: This API server is used only for demonstrating usage of AsyncEngine and simple performance benchmarks. It is not intended for production use. For production use, we recommend using our OpenAI compatible server. We are also not going to accept PRs modifying this file, please change `vllm/entrypoints/openai/api_server.py` instead.

## generate `async` [¶](#vllm.entrypoints.api_server.generate "Permanent link")

```
generate(request: Request) -> Response
```

Generate completion for the request.

The request should be a JSON object with the following fields: - prompt: the prompt to use for the generation. - stream: whether to stream the results or not. - other fields: the sampling parameters (See `SamplingParams` for details).

Source code in `vllm/entrypoints/api_server.py`

```
@app.post("/generate")
async defgenerate(request: Request) -> Response:
"""Generate completion for the request.

    The request should be a JSON object with the following fields:
    - prompt: the prompt to use for the generation.
    - stream: whether to stream the results or not.
    - other fields: the sampling parameters (See `SamplingParams` for details).
    """
    request_dict = await request.json()
    return await _generate(request_dict, raw_request=request)
```

## health `async` [¶](#vllm.entrypoints.api_server.health "Permanent link")

Health check.

Source code in `vllm/entrypoints/api_server.py`

```
@app.get("/health")
async defhealth() -> Response:
"""Health check."""
    return Response(status_code=200)
```