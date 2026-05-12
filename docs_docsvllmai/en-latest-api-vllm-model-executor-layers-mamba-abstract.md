---
title: abstract - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/mamba/abstract/
source: sitemap
fetched_at: 2026-05-07T21:25:51.987080781-03:00
rendered_js: false
word_count: 88
summary: This document defines the MambaBase abstract base class, which provides a standard interface for implementing custom Mamba-like layers within the vLLM model execution engine.
tags:
    - vllm
    - mamba
    - abstract-base-class
    - model-executor
    - layer-implementation
    - kv-cache
category: reference
---

## vllm.model\_executor.layers.mamba.abstract [¶](#vllm.model_executor.layers.mamba.abstract "Permanent link")

## MambaBase [¶](#vllm.model_executor.layers.mamba.abstract.MambaBase "Permanent link")

Bases: `AttentionLayerBase`

Base class for Mamba-like layers which support the v1 engine. Inherit from this class if you implement a custom layer.

Source code in `vllm/model_executor/layers/mamba/abstract.py`

```
classMambaBase(AttentionLayerBase):
"""
    Base class for Mamba-like layers which support the v1 engine.
    Inherit from this class if you implement a custom layer.
    """

    # Contains the KV cache (mamba state) for the layer
    # in the shape specified by `self.get_state_shape`.
    kv_cache: tuple[torch.Tensor, ...]

    @abstractmethod
    defget_state_shape(self) -> Iterable[tuple[int, ...]]:
"""
        Defines the shape of the state.
        For mamba layers this is usually a (conv_state, ssm_state) tuple.
        In this case, returns (conv_state_shape, ssm_state_shape).
        """
        pass

    @property
    @abstractmethod
    defmamba_type(self) -> str:
        pass

    @abstractmethod
    defget_state_dtype(self) -> tuple[torch.dtype, ...]:
        pass

    defget_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec | None:
        mamba_block_size = vllm_config.cache_config.mamba_block_size
        assert mamba_block_size is not None
        page_size_padded = vllm_config.cache_config.mamba_page_size_padded
        return MambaSpec(
            shapes=tuple(self.get_state_shape()),
            dtypes=self.get_state_dtype(),
            block_size=mamba_block_size,
            page_size_padded=page_size_padded,
            mamba_type=self.mamba_type,
            mamba_cache_mode=vllm_config.cache_config.mamba_cache_mode,
            num_speculative_blocks=(
                vllm_config.speculative_config.num_speculative_tokens
                if vllm_config.speculative_config
                else 0
            ),
        )

    defget_attn_backend(self) -> type[AttentionBackend]:
"""Get the attention backend class for this Mamba layer."""
        return get_mamba_attn_backend(self.mamba_type)
```

### get\_attn\_backend [¶](#vllm.model_executor.layers.mamba.abstract.MambaBase.get_attn_backend "Permanent link")

Get the attention backend class for this Mamba layer.

Source code in `vllm/model_executor/layers/mamba/abstract.py`

```
defget_attn_backend(self) -> type[AttentionBackend]:
"""Get the attention backend class for this Mamba layer."""
    return get_mamba_attn_backend(self.mamba_type)
```

### get\_state\_shape `abstractmethod` [¶](#vllm.model_executor.layers.mamba.abstract.MambaBase.get_state_shape "Permanent link")

Defines the shape of the state. For mamba layers this is usually a (conv\_state, ssm\_state) tuple. In this case, returns (conv\_state\_shape, ssm\_state\_shape).

Source code in `vllm/model_executor/layers/mamba/abstract.py`

```
@abstractmethod
defget_state_shape(self) -> Iterable[tuple[int, ...]]:
"""
    Defines the shape of the state.
    For mamba layers this is usually a (conv_state, ssm_state) tuple.
    In this case, returns (conv_state_shape, ssm_state_shape).
    """
    pass
```