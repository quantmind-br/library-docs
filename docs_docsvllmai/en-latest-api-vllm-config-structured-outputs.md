---
title: structured_outputs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/structured_outputs/
source: sitemap
fetched_at: 2026-05-07T21:17:15.860448769-03:00
rendered_js: false
word_count: 65
summary: This document describes the implementation of a hash calculation method for configuration files that influence the computation graph in a machine learning model.
tags:
    - computation-graph
    - hash-calculation
    - configuration-management
    - vllm
    - model-architecture
category: reference
---

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

Source code in `vllm/config/structured_outputs.py`

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
    # this config will not affect the computation graph.
    factors: list[Any] = []
    hash_str = safe_hash(str(factors).encode(), usedforsecurity=False).hexdigest()
    return hash_str
```