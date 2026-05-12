---
title: interface - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/gpu/model_states/interface/
source: sitemap
fetched_at: 2026-05-07T21:42:37.498981258-03:00
rendered_js: false
word_count: 10
summary: This document defines the ModelSpecificAttnMetadata base class, which provides an interface for managing model-specific attention configuration parameters in the vLLM engine.
tags:
    - vllm
    - attention-mechanism
    - model-metadata
    - python-interface
    - gpu-worker
category: reference
---

Base class for model-specific attention metadata.

Source code in `vllm/v1/worker/gpu/model_states/interface.py`

```
classModelSpecificAttnMetadata:
"""Base class for model-specific attention metadata."""

    defget_extra_common_attn_kwargs(
        self,
        kv_cache_group_id: int,
        num_reqs: int,
    ) -> dict[str, Any]:
        return {}

    defget_extra_attn_kwargs(
        self,
        attn_metadata_builder: Any,
        num_reqs: int,
    ) -> dict[str, Any]:
        return {}
```