---
title: attention_layer_base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention_layer_base/
source: sitemap
fetched_at: 2026-05-07T21:24:06.345697838-03:00
rendered_js: false
word_count: 82
summary: This document defines the base abstract class for attention layers within the vLLM framework, establishing a standardized interface for backend retrieval and KV cache specifications.
tags:
    - vllm
    - attention-layer
    - abstract-base-class
    - kv-cache
    - model-executor
    - backend-interface
category: reference
---

## vllm.model\_executor.layers.attention\_layer\_base [¶](#vllm.model_executor.layers.attention_layer_base "Permanent link")

Base class for attention-like layers.

## AttentionLayerBase [¶](#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase "Permanent link")

Bases: `ABC`

Base class for attention-like layers (Attention, Mamba, etc.) that support the v1 engine.

This provides a common interface for getting attention backends from different layer types.

Source code in `vllm/model_executor/layers/attention_layer_base.py`

```
classAttentionLayerBase(ABC):
"""
    Base class for attention-like layers (Attention, Mamba, etc.)
    that support the v1 engine.

    This provides a common interface for getting attention backends
    from different layer types.
    """

    impl: "AttentionImpl"

    @abstractmethod
    defget_attn_backend(self) -> type[AttentionBackend]:
"""Get the attention backend class for this layer."""
        pass

    @abstractmethod
    defget_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec | None:
"""
        Get the KV cache spec for this layer.
        May be None if the layer does not need KV cache.
        """
        pass
```

### get\_attn\_backend `abstractmethod` [¶](#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase.get_attn_backend "Permanent link")

Get the attention backend class for this layer.

Source code in `vllm/model_executor/layers/attention_layer_base.py`

```
@abstractmethod
defget_attn_backend(self) -> type[AttentionBackend]:
"""Get the attention backend class for this layer."""
    pass
```

### get\_kv\_cache\_spec `abstractmethod` [¶](#vllm.model_executor.layers.attention_layer_base.AttentionLayerBase.get_kv_cache_spec "Permanent link")

Get the KV cache spec for this layer. May be None if the layer does not need KV cache.

Source code in `vllm/model_executor/layers/attention_layer_base.py`

```
@abstractmethod
defget_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec | None:
"""
    Get the KV cache spec for this layer.
    May be None if the layer does not need KV cache.
    """
    pass
```