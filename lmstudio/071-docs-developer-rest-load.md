---
title: Load a model
url: https://lmstudio.ai/docs/developer/rest/load
source: sitemap
fetched_at: 2026-04-07T21:30:21.997847077-03:00
rendered_js: false
word_count: 0
summary: This document provides a snapshot of the loading status and configuration details for an LLM instance identified as openai/gpt-oss-20b.
tags:
    - llm
    - loading-status
    - configuration
    - gpu-optimization
category: reference
---

```
{
  "type": "llm",
  "instance_id": "openai/gpt-oss-20b",
  "load_time_seconds": 9.099,
  "status": "loaded",
  "load_config": {
    "context_length": 16384,
    "eval_batch_size": 512,
    "flash_attention": true,
    "offload_kv_cache_to_gpu": true,
    "num_experts": 4
  }
}
```