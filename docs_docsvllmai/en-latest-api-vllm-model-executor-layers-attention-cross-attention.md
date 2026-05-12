---
title: cross_attention - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/attention/cross_attention/
source: sitemap
fetched_at: 2026-05-07T21:24:00.105265661-03:00
rendered_js: false
word_count: 30
summary: This document defines the CrossAttention layer and utility functions for encoder-decoder models in the vLLM framework, including key-value cache specification and slot mapping logic.
tags:
    - cross-attention
    - encoder-decoder
    - kv-cache
    - vllm-framework
    - attention-mechanism
    - model-layers
category: reference
---

## CrossAttention [¶](#vllm.model_executor.layers.attention.cross_attention.CrossAttention "Permanent link")

Bases: `Attention`

Cross-attention for encoder-decoder models. Handles attention between decoder queries and encoder keys/values.

Source code in `vllm/model_executor/layers/attention/cross_attention.py`

```
classCrossAttention(Attention):
"""
    Cross-attention for encoder-decoder models.
    Handles attention between decoder queries and encoder keys/values.
    """

    def__init__(
        self,
        num_heads: int,
        head_size: int,
        scale: float,
        cache_config: CacheConfig | None = None,
        attn_type: str | None = None,
        **kwargs,
    ):
        dtype = torch.get_default_dtype()

        if cache_config is not None:
            kv_cache_dtype = cache_config.cache_dtype
        else:
            kv_cache_dtype = "auto"

        if attn_type is not None:
            assert attn_type == AttentionType.ENCODER_DECODER, (
                "CrossAttention only supports AttentionType.ENCODER_DECODER"
            )

        underlying_attn_backend = get_attn_backend(
            head_size,
            dtype,
            kv_cache_dtype,
            attn_type=AttentionType.ENCODER_DECODER,
        )
        attn_backend = create_cross_attention_backend(underlying_attn_backend)

        super().__init__(
            num_heads=num_heads,
            head_size=head_size,
            scale=scale,
            cache_config=cache_config,
            attn_backend=attn_backend,
            attn_type=AttentionType.ENCODER_DECODER,
            **kwargs,
        )

    defget_kv_cache_spec(self, vllm_config: VllmConfig) -> KVCacheSpec:
        return CrossAttentionSpec(
            block_size=vllm_config.cache_config.block_size,
            num_kv_heads=self.num_kv_heads,
            head_size=self.head_size,
            dtype=self.kv_cache_torch_dtype,
            kv_quant_mode=get_kv_quant_mode(self.kv_cache_dtype),
        )
```

## \_get\_cross\_slot\_mapping [¶](#vllm.model_executor.layers.attention.cross_attention._get_cross_slot_mapping "Permanent link")

Get cross-attention slot mappings.

Source code in `vllm/model_executor/layers/attention/cross_attention.py`

```
def_get_cross_slot_mapping(
    encoder_seq_lens: np.ndarray,
    block_table_tensor: torch.Tensor,
    kv_cache_spec: CrossAttentionSpec,
    device: torch.device,
) -> torch.Tensor:
"""Get cross-attention slot mappings."""

    block_size = kv_cache_spec.block_size
    slot_mappings = []

    # Find indices with non-zero encoder sequence lengths
    # The majority of parallel requests will be running the
    # decoder, so this list should be relatively small.
    active_indices = np.nonzero(encoder_seq_lens)[0]

    for req_index in active_indices:
        encoder_seq_len = encoder_seq_lens[req_index].item()

        # Calculate the number of blocks needed for this request
        num_blocks_needed = cdiv(encoder_seq_len, block_size)

        # Get the block IDs for this request from the tensor
        req_block_ids = block_table_tensor[req_index]

        # Get only the blocks we need (first num_blocks_needed blocks)
        needed_block_ids = req_block_ids[:num_blocks_needed]

        # All needed blocks are allocated
        i_values = torch.arange(encoder_seq_len, dtype=torch.int64, device=device)
        block_indices = i_values // block_size
        block_offsets = i_values % block_size
        block_numbers = needed_block_ids[block_indices]
        slot_mapping = block_numbers * block_size + block_offsets

        slot_mappings.append(slot_mapping)

    if slot_mappings:
        return torch.cat(slot_mappings)
    else:
        return torch.empty(0, dtype=torch.int64, device=device)
```