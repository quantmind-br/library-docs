---
title: device - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/device/
source: sitemap
fetched_at: 2026-05-07T21:16:55.036927099-03:00
rendered_js: false
word_count: 65
summary: This document describes the implementation of a hash computation method used to uniquely identify configuration settings that influence the structure of the model's computation graph.
tags:
    - configuration
    - computation-graph
    - hash-generation
    - vllm-internals
    - model-architecture
category: reference
---

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

Source code in `vllm/config/device.py`

```
defcompute_hash(self) -> str:
"""
    WARNING: Whenever a new field is added to this config,
    ensure that it is included in the factors list if
    it affects the computation graph.

    Provide a hash that uniquely identifies all the configs
    that affect the structure of the computation
    graph from input ids/embeddings to the final hidden states,
    excluding anything before input ids/embeddings and after
    the final hidden states.
    """
    # no factors to consider.
    # the device/platform information will be summarized
    # by torch/vllm automatically.
    factors: list[Any] = []
    hash_str = safe_hash(str(factors).encode(), usedforsecurity=False).hexdigest()
    return hash_str
```