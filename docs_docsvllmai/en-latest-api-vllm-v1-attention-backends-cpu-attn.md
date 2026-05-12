---
title: cpu_attn - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/cpu_attn/
source: sitemap
fetched_at: 2026-05-07T21:39:05.169332752-03:00
rendered_js: false
word_count: 0
summary: This document defines a CPU-based attention implementation class for neural network models, handling both standard attention mechanisms and KV cache operations.
tags:
    - attention-mechanism
    - cpu-backend
    - kv-cache
    - deep-learning
    - transformer
    - neural-networks
category: api
---

```
classCPUAttentionBackendImpl(AttentionImpl):
    def__init__(
        self,
        num_heads: int,
        head_size: int,
        scale: float,
        num_kv_heads: int,
        alibi_slopes: list[float] | None,
        sliding_window: int | None,
        kv_cache_dtype: str,
        logits_soft_cap: float | None = None,
        attn_type: str = AttentionType.DECODER,
        kv_sharing_target_layer_name: str | None = None,
        sinks: torch.Tensor | None = None,
    ) -> None:
        self.kv_sharing_target_layer_name = kv_sharing_target_layer_name
        self.num_heads = num_heads
        self.head_size = head_size
        self.scale = float(scale)
        if logits_soft_cap is not None and attn_type in (
            AttentionType.ENCODER,
            AttentionType.ENCODER_ONLY,
        ):
            logger.warning_once(
                "CPU_ATTN does not support logits softcap for"
                " ENCODER and ENCODER_ONLY, outputs may be slightly off"
            )
        if logits_soft_cap is None:
            logits_soft_cap = 0
        self.logits_soft_cap = logits_soft_cap

        self.num_kv_heads = num_kv_heads
        if alibi_slopes is not None:
            alibi_slopes = torch.tensor(alibi_slopes, dtype=torch.float32)
        self.alibi_slopes = alibi_slopes
        if sliding_window is None:
            self.sliding_window = (-1, -1)
        elif attn_type == AttentionType.ENCODER_ONLY:
            self.sliding_window = (sliding_window - 1, sliding_window - 1)
        else:
            self.sliding_window = (sliding_window - 1, 0)
        self.kv_cache_dtype = kv_cache_dtype
        self.num_queries_per_kv = self.num_heads // self.num_kv_heads

        self.is_fp8_kv_cache = is_quantized_kv_cache(kv_cache_dtype)
        self.attn_type = attn_type

        self.sinks = sinks
        if self.sinks is not None:
            assert self.sinks.shape[0] == num_heads, (
                "Sinks must have the same number of heads as the number of "
                "heads in the layer"
            )

    defforward(
        self,
        layer: AttentionLayer,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        kv_cache: torch.Tensor,
        attn_metadata: CPUAttentionMetadata | None,
        output: torch.Tensor,
        output_scale: torch.Tensor | None = None,
        output_block_scale: torch.Tensor | None = None,
    ) -> torch.Tensor:
"""Forward pass for CPU attention backend.

        Args:
            query: shape = [num_tokens, num_heads, head_size]
            key: shape = [num_tokens, num_kv_heads, head_size]
            value: shape = [num_tokens, num_kv_heads, head_size]
            kv_cache: shape =
                [2, num_blocks, num_kv_heads, block_size, head_size]
            attn_metadata: Metadata for attention.
        Returns:
            shape = [num_tokens, num_heads * head_size]
        """
        if output_scale is not None or output_block_scale is not None:
            raise NotImplementedError(
                "fused output quantization is not yet supported"
                " for CPUAttentionBackendImpl"
            )

        # For warming-up
        if attn_metadata is None:
            return output

        num_actual_tokens = attn_metadata.num_actual_tokens

        # Handle encoder attention differently - no KV cache needed
        if self.attn_type in (AttentionType.ENCODER_ONLY, AttentionType.ENCODER):
            # For encoder attention,
            return self._run_sdpa_forward(
                query[:num_actual_tokens],
                key[:num_actual_tokens],
                value[:num_actual_tokens],
                output[:num_actual_tokens],
                attn_metadata,
                self.attn_type,
            )

        # For decoder and cross-attention, use KV cache, size are
        # [num_blocks, num_kv_heads, block_size, head_size]
        key_cache, value_cache = kv_cache.unbind(0)

        # key and value may be None in the case of cross attention. They are
        # calculated once based on the output from the encoder and then cached
        # in KV cache.
        if (
            self.kv_sharing_target_layer_name is None
            and key is not None
            and value is not None
        ):
            ops.cpu_attn_reshape_and_cache(
                key,
                value,
                key_cache,
                value_cache,
                attn_metadata.slot_mapping,
                attn_metadata.isa,
                k_scale=layer._k_scale_float,
                v_scale=layer._v_scale_float,
                kv_cache_dtype=self.kv_cache_dtype,
            )

        if attn_metadata.use_sdpa_prefill:
            assert self.sinks is None, "Attention sink is unsupported in SDPA prefill"
            num_decode_tokens = attn_metadata.num_decode_tokens
            self._run_sdpa_forward(
                query[num_decode_tokens:num_actual_tokens],
                key[num_decode_tokens:num_actual_tokens],
                value[num_decode_tokens:num_actual_tokens],
                output[num_decode_tokens:num_actual_tokens],
                attn_metadata,
                self.attn_type,
            )
            num_actual_tokens = num_decode_tokens

        if num_actual_tokens > 0:
            ops.cpu_attention_with_kv_cache(
                query=query[:num_actual_tokens],
                key_cache=key_cache,
                value_cache=value_cache,
                output=output[:num_actual_tokens],  # type: ignore
                query_start_loc=attn_metadata.query_start_loc,
                seq_lens=attn_metadata.seq_lens,
                scale=self.scale,
                causal=attn_metadata.causal,
                alibi_slopes=self.alibi_slopes,  # type: ignore
                sliding_window=self.sliding_window,
                block_table=attn_metadata.block_table,
                softcap=self.logits_soft_cap,
                scheduler_metadata=attn_metadata.scheduler_metadata,
                s_aux=self.sinks,
                k_scale=layer._k_scale_float,
                v_scale=layer._v_scale_float,
                kv_cache_dtype=self.kv_cache_dtype,
            )

        return output

    def_run_sdpa_forward(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        output: torch.Tensor,
        attn_metadata: CPUAttentionMetadata,
        attn_type: str,
    ) -> torch.Tensor:
        attn_masks = attn_metadata.sdpa_attn_masks
        if attn_masks is None:
            if self.alibi_slopes is not None:
                attn_masks = _make_alibi_bias(
                    self.alibi_slopes,
                    query.dtype,
                    attn_metadata.sdpa_start_loc,
                )
            elif self.sliding_window[0] != -1 or self.sliding_window[1] != -1:
                assert attn_metadata.seq_lens is not None
                attn_masks = _make_sliding_window_bias(
                    attn_metadata.sdpa_start_loc,
                    self.sliding_window[0],
                    self.sliding_window[1],
                    query.dtype,
                )
            else:
                attn_masks = [None] * (attn_metadata.sdpa_start_loc.size(0) - 1)  # type: ignore
            attn_metadata.sdpa_attn_masks = attn_masks

        query = query.movedim(0, query.dim() - 2)
        key = key.movedim(0, key.dim() - 2)
        value = value.movedim(0, value.dim() - 2)

        causal_attn = attn_type == AttentionType.DECODER

        sdpa_start_loc = attn_metadata.sdpa_start_loc.numpy()  # type: ignore
        for i in range(len(attn_masks)):
            mask = attn_masks[i]
            start_q = sdpa_start_loc[i]
            end_q = sdpa_start_loc[i + 1]
            sub_out = (
                torch.nn.functional.scaled_dot_product_attention(
                    query[None, :, start_q:end_q, :],
                    key[None, :, start_q:end_q, :],
                    value[None, :, start_q:end_q, :],
                    attn_mask=mask,
                    dropout_p=0.0,
                    is_causal=causal_attn and mask is None,
                    scale=self.scale,
                    enable_gqa=self.num_heads > self.num_kv_heads,
                )
                .squeeze(0)
                .movedim(query.dim() - 2, 0)
            )
            output[start_q:end_q, :, :] = sub_out
        return output
```