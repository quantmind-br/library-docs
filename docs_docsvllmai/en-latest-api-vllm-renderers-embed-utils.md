---
title: embed_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/renderers/embed_utils/
source: sitemap
fetched_at: 2026-05-07T21:35:19.967456196-03:00
rendered_js: false
word_count: 30
summary: This function provides an asynchronous wrapper for safe_load_prompt_embeds to prevent blocking the asyncio event loop during data decoding and loading.
tags:
    - asyncio
    - prompt-embeddings
    - non-blocking
    - torch-load
    - thread-pool
category: api
---

## safe\_load\_prompt\_embeds\_async `module-attribute` [¶](#vllm.renderers.embed_utils.safe_load_prompt_embeds_async "Permanent link")

```
safe_load_prompt_embeds_async = make_async(
    safe_load_prompt_embeds
)
```

Async variant of `safe_load_prompt_embeds` that defers the decode to a thread-pool executor, so the asyncio event loop is not blocked by the base64 decode + `torch.load` work.