---
title: rocm_aiter_fa - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/rocm_aiter_fa/
source: sitemap
fetched_at: 2026-05-07T21:39:40.21713897-03:00
rendered_js: false
word_count: 7
summary: This document defines the AiterFlashAttentionImpl class, which implements optimized flash attention mechanisms for decoder models, including support for sliding window attention and chunked KV cache processing on ROCm hardware.
tags:
    - flash-attention
    - rocm
    - kv-cache
    - decoder-model
    - attention-mechanism
    - machine-learning-optimization
category: concept
---

```
classAiterFlashAttentionImpl(AttentionImpl):
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
        attn_type: AttentionType = AttentionType.DECODER,
        kv_sharing_target_layer_name: int | None = None,
    ) -> None:
        self.num_heads = num_heads
        self.head_size = head_size
        self.scale = float(scale)
        self.num_kv_heads = num_kv_heads
        if alibi_slopes is not None:
            alibi_slopes = torch.tensor(alibi_slopes, dtype=torch.float32)
        self.alibi_slopes = alibi_slopes
        if sliding_window is None:
            self.sliding_window = (-1, -1)
        else:
            self.sliding_window = (sliding_window - 1, 0)
        self.kv_cache_dtype = kv_cache_dtype
        if logits_soft_cap is None:
            # In flash-attn, setting logits_soft_cap as 0 means no soft cap.
            logits_soft_cap = 0.0
        self.logits_soft_cap = logits_soft_cap
        self.kv_sharing_target_layer_name = kv_sharing_target_layer_name

        assert self.num_heads % self.num_kv_heads == 0
        self.num_queries_per_kv = self.num_heads // self.num_kv_heads

        if attn_type != AttentionType.DECODER:
            raise NotImplementedError(
                "Only decoder self-attention is supported for "
                "AiterFlashAttentionImpl. ENCODER_DECODER is not supported "
                "because the prefill path uses cu_seqlens_k set to decoder "
                "query_start_loc with causal=True, which is incorrect for "
                "cross-attention."
            )

    defextend_for_sliding_window(
        self,
        attn_metadata: AiterFlashAttentionMetadata,
        query: torch.Tensor,
        key_cache,
        value_cache,
        output: torch.Tensor,
        cu_seqlens_q: torch.Tensor,
        max_seqlen_q: int,
        block_table: torch.Tensor,
        k_scale: float,
        v_scale: float,
    ):
        assert attn_metadata.extend_metadata is not None
        assert attn_metadata.extend_metadata.chunk_context_metadata is not None
        chunked_metadata = attn_metadata.extend_metadata.chunk_context_metadata
        swa_metadata = chunked_metadata.swa_metadata
        assert swa_metadata is not None
        swa_cu_seqlens = swa_metadata.swa_cu_seqlens
        swa_seq_starts = swa_metadata.swa_seq_starts
        swa_token_to_batch = swa_metadata.swa_token_to_batch
        swa_max_seqlens = swa_metadata.swa_max_seqlens
        swa_total_tokens = swa_metadata.swa_total_tokens
        key_fetched, value_fetched = (
            swa_metadata.swa_workspace[0],
            swa_metadata.swa_workspace[1],
        )
        cp_mha_gather_cache(
            key_cache=key_cache,
            value_cache=value_cache,
            key=key_fetched,
            value=value_fetched,
            block_tables=block_table,
            k_scales=k_scale,
            v_scales=v_scale,
            cu_seqlens_kv=swa_cu_seqlens,
            token_to_batch=swa_token_to_batch,
            seq_starts=swa_seq_starts,
            dequant=is_quantized_kv_cache(self.kv_cache_dtype),
            kv_cache_layout="NHD",
            total_tokens=swa_total_tokens,
        )

        rocm_aiter_ops.flash_attn_varlen_func(
            q=query,
            k=key_fetched,
            v=value_fetched,
            cu_seqlens_q=cu_seqlens_q,
            cu_seqlens_k=swa_cu_seqlens,
            max_seqlen_q=max_seqlen_q,
            max_seqlen_k=swa_max_seqlens,
            min_seqlen_q=1,
            dropout_p=0.0,
            softmax_scale=self.scale,
            causal=True,
            window_size=self.sliding_window,
            alibi_slopes=self.alibi_slopes,
            return_lse=False,
            out=output,
        )

    defextend_forward(
        self,
        attn_metadata: AiterFlashAttentionMetadata,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        key_cache: torch.Tensor,
        value_cache: torch.Tensor,
        output: torch.Tensor,
        cu_seqlens_q: torch.Tensor,
        max_seqlen_q: int,
        max_seqlen_k: int,
        min_seqlen_q: int,
        block_table: torch.Tensor,
        slot_mapping: torch.Tensor,
        k_scale: torch.Tensor,
        v_scale: torch.Tensor,
    ):
        if self.sliding_window[0] != -1:
            self.extend_for_sliding_window(
                attn_metadata,
                query,
                key_cache,
                value_cache,
                output,
                cu_seqlens_q,
                max_seqlen_q,
                block_table,
                k_scale,
                v_scale,
            )
            return
        out, lse = rocm_aiter_ops.flash_attn_varlen_func(
            q=query,
            k=key,
            v=value,
            cu_seqlens_q=cu_seqlens_q,
            cu_seqlens_k=cu_seqlens_q,
            max_seqlen_q=max_seqlen_q,
            max_seqlen_k=max_seqlen_q,
            min_seqlen_q=min_seqlen_q,
            dropout_p=0.0,
            softmax_scale=self.scale,
            causal=True,
            window_size=self.sliding_window,
            alibi_slopes=self.alibi_slopes,
            return_lse=True,
        )
        assert attn_metadata.extend_metadata is not None
        chunk_context_metadata = attn_metadata.extend_metadata.chunk_context_metadata
        num_chunks = chunk_context_metadata.num_chunks
        workspace = chunk_context_metadata.workspace
        cu_seqlens_kv = chunk_context_metadata.cu_seq_lens_chunk
        max_seqlens = chunk_context_metadata.max_seq_lens
        chunk_starts = chunk_context_metadata.chunk_starts
        token_to_batch = chunk_context_metadata.token_to_batch
        total_token_per_batch = chunk_context_metadata.total_token_per_batch
        key_fetched, value_fetched = workspace[0], workspace[1]
        chunked_output = None
        chunked_lse = None
        for chunk_idx in range(num_chunks):
            cp_mha_gather_cache(
                key_cache=key_cache,
                value_cache=value_cache,
                key=key_fetched,
                value=value_fetched,
                block_tables=block_table,
                k_scales=k_scale,
                v_scales=v_scale,
                cu_seqlens_kv=cu_seqlens_kv[chunk_idx],
                token_to_batch=token_to_batch[chunk_idx],
                seq_starts=chunk_starts[chunk_idx],
                dequant=is_quantized_kv_cache(self.kv_cache_dtype),
                kv_cache_layout="SHUFFLE"
                if rocm_aiter_ops.is_shuffle_kv_cache_enabled()
                else "NHD",
                total_tokens=total_token_per_batch[chunk_idx],
            )

            suf_out, suf_lse = rocm_aiter_ops.flash_attn_varlen_func(
                q=query,
                k=key_fetched,
                v=value_fetched,
                cu_seqlens_q=cu_seqlens_q,
                cu_seqlens_k=cu_seqlens_kv[chunk_idx],
                max_seqlen_q=max_seqlen_q,
                max_seqlen_k=max_seqlens[chunk_idx],
                min_seqlen_q=min_seqlen_q,
                dropout_p=0.0,
                softmax_scale=self.scale,
                causal=False,
                window_size=self.sliding_window,
                alibi_slopes=self.alibi_slopes,
                return_lse=True,
            )
            if chunked_output is None:
                chunked_output = suf_out
                chunked_lse = suf_lse
            else:
                tmp_output = torch.empty_like(out)
                tmp_lse = torch.empty_like(lse)
                merge_attn_states(
                    output=tmp_output,
                    output_lse=tmp_lse,
                    prefix_output=chunked_output,
                    prefix_lse=chunked_lse,
                    suffix_output=suf_out,
                    suffix_lse=suf_lse,
                )
                chunked_output = tmp_output
                chunked_lse = tmp_lse

        merge_attn_states(
            output=output,
            prefix_output=chunked_output,
            prefix_lse=chunked_lse,
            suffix_output=out,
            suffix_lse=lse,
        )

    defforward(
        self,
        layer: torch.nn.Module,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        kv_cache: torch.Tensor,
        attn_metadata: AiterFlashAttentionMetadata,
        output: torch.Tensor,
        output_scale: torch.Tensor | None = None,
        output_block_scale: torch.Tensor | None = None,
    ) -> torch.Tensor:
"""Forward pass with AiterFlashAttention.

        Args:
            query: shape = [num_tokens, num_heads, head_size]
            key: shape = [num_tokens, num_kv_heads, head_size]
            value: shape = [num_tokens, num_kv_heads, head_size]
            kv_cache: shape =
                [2, num_blocks, block_size, num_kv_heads, head_size]
            attn_metadata: Metadata for attention.
        Returns:
            shape = [num_tokens, num_heads * head_size]
        NOTE: FP8 quantization, flash-attn expect the size of
              {q,k,v}_descale to be (num_sequences, num_kv_heads).
              We use torch's .expand() to avoid duplicating values
        """
        if output_scale is not None or output_block_scale is not None:
            raise NotImplementedError(
                "fused output quantization is not yet supported "
                "for AiterFlashAttentionImpl"
            )

        if attn_metadata is None:
            # Profiling run.
            return output.fill_(0)

        # IMPORTANT!
        # NOTE(woosuk): With piece-wise CUDA graphs, this method is
        # executed in eager-mode PyTorch. Thus, we need to be careful
        # about any CPU overhead in this method. For example, `view`
        # and `slice` (or `[:n]`) operations are surprisingly slow even
        # in the case they do not invoke any GPU ops.
        # Minimize the PyTorch ops in this method as much as possible.
        # Whenever making a change in this method, please benchmark the
        # performance to make sure it does not introduce any overhead.
        num_actual_tokens = attn_metadata.num_actual_tokens
        key_cache, value_cache = kv_cache.unbind(0)

        if is_quantized_kv_cache(self.kv_cache_dtype):
            key_cache = key_cache.view(current_platform.fp8_dtype())
            value_cache = value_cache.view(current_platform.fp8_dtype())

        # decode:extend:prefill
        query = query[:num_actual_tokens]
        if key is not None:
            key = key[:num_actual_tokens]
        if value is not None:
            value = value[:num_actual_tokens]

        output_actual_tokens = output[:num_actual_tokens]

        num_decodes = attn_metadata.num_decodes
        num_prefills = attn_metadata.num_prefills
        num_extends = attn_metadata.num_extends

        num_decode_tokens = attn_metadata.num_decode_tokens
        num_extend_tokens = attn_metadata.num_extend_tokens
        if not attn_metadata.use_cascade:
            # calculate for pure prefills
            if num_prefills > 0:
                assert attn_metadata.prefill_metadata is not None

                prefill_query = query[num_decode_tokens + num_extend_tokens :]
                prefill_key = key[num_decode_tokens + num_extend_tokens :]
                prefill_value = value[num_decode_tokens + num_extend_tokens :]

                rocm_aiter_ops.flash_attn_varlen_func(
                    q=prefill_query,
                    k=prefill_key,
                    v=prefill_value,
                    cu_seqlens_q=attn_metadata.prefill_metadata.query_start_loc,
                    cu_seqlens_k=attn_metadata.prefill_metadata.query_start_loc,
                    max_seqlen_q=attn_metadata.prefill_metadata.max_query_len,
                    max_seqlen_k=attn_metadata.prefill_metadata.max_seq_len,
                    min_seqlen_q=1,
                    dropout_p=0.0,
                    softmax_scale=self.scale,
                    causal=attn_metadata.causal,
                    window_size=self.sliding_window,
                    alibi_slopes=self.alibi_slopes,
                    out=output_actual_tokens[num_decode_tokens + num_extend_tokens :],
                )

            # calculate for extends
            if num_extends > 0:
                assert attn_metadata.extend_metadata is not None
                extend_tokens_slice = slice(
                    num_decode_tokens, num_decode_tokens + num_extend_tokens
                )
                extend_queries = query[extend_tokens_slice]
                extend_keys = key[extend_tokens_slice]
                extend_values = value[extend_tokens_slice]
                extend_outputs = output[extend_tokens_slice]
                k_scale = layer._k_scale
                v_scale = layer._v_scale
                if rocm_aiter_ops.is_shuffle_kv_cache_enabled():
                    k_scale = attn_metadata.k_scale
                    v_scale = attn_metadata.v_scale
                self.extend_forward(
                    attn_metadata=attn_metadata,
                    query=extend_queries,
                    key=extend_keys,
                    value=extend_values,
                    key_cache=key_cache,
                    value_cache=value_cache,
                    output=extend_outputs,
                    cu_seqlens_q=attn_metadata.extend_metadata.query_start_loc,
                    max_seqlen_q=attn_metadata.extend_metadata.max_query_len,
                    max_seqlen_k=attn_metadata.extend_metadata.max_seq_len,
                    min_seqlen_q=1,
                    block_table=attn_metadata.block_table[
                        num_decodes : num_decodes + num_extends
                    ],
                    slot_mapping=attn_metadata.slot_mapping[
                        num_decodes : num_decodes + num_extends
                    ],
                    k_scale=k_scale,
                    v_scale=v_scale,
                )

            # calculate for decodes
            if num_decodes > 0:
                assert attn_metadata.decode_metadata is not None
                decode_max_query_len = attn_metadata.decode_metadata.max_query_len

                # Multi-token speculative decode path.
                if decode_max_query_len > 1:
                    assert not rocm_aiter_ops.is_shuffle_kv_cache_enabled(), (
                        "Shuffle KV cache layout is not supported with "
                        "speculative decoding (multi-token decode)."
                    )
                    if not attn_metadata.causal:
                        fromaiter.ops.triton.attention.mha_v3import (
                            flash_attn_with_kvcache,
                        )

                        descale_shape = (num_decodes, key_cache.shape[2])
                        decode_query = query[:num_decode_tokens].reshape(
                            num_decodes,
                            decode_max_query_len,
                            query.shape[1],
                            query.shape[2],
                        )
                        decode_out = flash_attn_with_kvcache(
                            q=decode_query,
                            k_cache=key_cache,
                            v_cache=value_cache,
                            cache_seqlens=attn_metadata.seq_lens[:num_decodes],
                            softmax_scale=self.scale,
                            causal=attn_metadata.causal,
                            window_size=self.sliding_window,
                            softcap=self.logits_soft_cap,
                            q_descale=None,
                            k_descale=layer._k_scale.expand(descale_shape),
                            v_descale=layer._v_scale.expand(descale_shape),
                            page_table=attn_metadata.block_table[:num_decodes],
                        )
                        output[:num_decode_tokens].copy_(
                            decode_out.reshape(
                                num_decode_tokens,
                                query.shape[1],
                                query.shape[2],
                            )
                        )
                    else:
                        # Non-uniform query lengths can appear in real serving
                        # traffic (e.g. mixed datasets). Fall back to varlen
                        # unified_attention instead of asserting.
                        fromaiter.ops.triton.unified_attentionimport (
                            unified_attention,
                        )

                        descale_shape = (
                            num_decodes,
                            key_cache.shape[2],
                        )
                        unified_attention(
                            q=query[:num_decode_tokens],
                            k=key_cache,
                            v=value_cache,
                            out=output[:num_decode_tokens],
                            cu_seqlens_q=attn_metadata.query_start_loc[
                                : num_decodes + 1
                            ],
                            max_seqlen_q=decode_max_query_len,
                            seqused_k=attn_metadata.seq_lens[:num_decodes],
                            max_seqlen_k=attn_metadata.max_seq_len,
                            softmax_scale=self.scale,
                            causal=True,
                            alibi_slopes=self.alibi_slopes,
                            window_size=self.sliding_window,
                            block_table=attn_metadata.block_table[:num_decodes],
                            softcap=self.logits_soft_cap,
                            q_descale=None,
                            k_descale=layer._k_scale.expand(descale_shape),
                            v_descale=layer._v_scale.expand(descale_shape),
                        )
                    return

                # The ll4mi kernel in paged_attention_v1 requires
                # HEAD_SIZE >= 16 * NWARPS (= 64 on ROCm with NWARPS=4).
                # For smaller head sizes or sliding window attention,
                # fall back to the unified_attention triton kernel which
                # handles both correctly.
                _MIN_HEAD_SIZE_FOR_LL4MI = 64
                use_unified_attention = self.head_size < _MIN_HEAD_SIZE_FOR_LL4MI

                if use_unified_attention:
                    assert not rocm_aiter_ops.is_shuffle_kv_cache_enabled(), (
                        "unified_attention fallback with shuffle layout "
                        "is not supported yet."
                    )
                    fromaiter.ops.triton.unified_attentionimport (
                        unified_attention,
                    )

                    decode_cu_seqlens_q = attn_metadata.query_start_loc[
                        : num_decodes + 1
                    ]
                    descale_shape = (
                        num_decodes,
                        key_cache.shape[2],
                    )
                    unified_attention(
                        q=query[:num_decode_tokens],
                        k=key_cache,
                        v=value_cache,
                        out=output[:num_decode_tokens],
                        cu_seqlens_q=decode_cu_seqlens_q,
                        max_seqlen_q=1,
                        seqused_k=attn_metadata.seq_lens[:num_decodes],
                        max_seqlen_k=attn_metadata.max_seq_len,
                        softmax_scale=self.scale,
                        causal=True,
                        alibi_slopes=self.alibi_slopes,
                        window_size=self.sliding_window,
                        block_table=attn_metadata.block_table[:num_decodes],
                        softcap=self.logits_soft_cap,
                        q_descale=None,
                        k_descale=layer._k_scale.expand(descale_shape),
                        v_descale=layer._v_scale.expand(descale_shape),
                    )
                elif rocm_aiter_ops.is_shuffle_kv_cache_enabled():
                    _, num_heads, head_size = query.shape
                    num_seqs = attn_metadata.seq_lens.shape[0]
                    max_num_partitions = (
                        attn_metadata.max_seq_len + _PARTITION_SIZE_ROCM - 1
                    ) // _PARTITION_SIZE_ROCM
                    tmp_out = torch.empty(
                        (num_seqs, num_heads, max_num_partitions, head_size),
                        dtype=query.dtype,
                        device=query.device,
                    )
                    exp_sums = torch.empty(
                        (num_seqs, num_heads, max_num_partitions),
                        dtype=torch.float32,
                        device=query.device,
                    )
                    max_logits = torch.empty_like(exp_sums)
                    num_blocks, block_size, num_kv_heads, _ = key_cache.shape
                    x = 16 // key_cache.element_size()
                    k_cache_template = torch.empty(
                        [num_blocks, num_kv_heads, head_size // x, block_size, x],
                        dtype=key_cache.dtype,
                        device="meta",
                    )
                    v_cache_template = torch.empty(
                        [num_blocks, num_kv_heads, block_size // x, head_size, x],
                        dtype=value_cache.dtype,
                        device="meta",
                    )
                    new_key_cache = key_cache.view_as(k_cache_template)
                    new_value_cache = value_cache.view_as(v_cache_template)
                    k_qscale = (
                        layer._k_scale
                        if attn_metadata.k_scale is None
                        else attn_metadata.k_scale
                    )
                    v_qscale = (
                        layer._v_scale
                        if attn_metadata.v_scale is None
                        else attn_metadata.v_scale
                    )
                    rocm_aiter_ops.paged_attention_common(
                        Q=query[:num_decode_tokens],
                        K=new_key_cache,
                        V=new_value_cache,
                        tmp_out=tmp_out,
                        max_logits=max_logits,
                        exp_sums=exp_sums,
                        max_seq_len=attn_metadata.max_seq_len,
                        block_tables=attn_metadata.block_table[:num_decodes],
                        context_lens=attn_metadata.seq_lens[:num_decodes],
                        block_tables_stride0=attn_metadata.block_table[
                            :num_decodes
                        ].stride(0),
                        scale=self.scale,
                        K_QScale_hip=k_qscale,
                        V_QScale_hip=v_qscale,
                        K_QScale_asm=k_qscale,
                        V_QScale_asm=v_qscale,
                        out_=output[:num_decode_tokens],
                        kv_cache_dtype=self.kv_cache_dtype,
                    )
                else:
                    _, num_heads, head_size = query.shape
                    nbytes_per_qo_elem = torch.finfo(query.dtype).bits // 8
                    num_seqs = attn_metadata.seq_lens.shape[0]
                    max_num_partitions = (
                        attn_metadata.max_seq_len + _PARTITION_SIZE_ROCM - 1
                    ) // _PARTITION_SIZE_ROCM

                    workspace_buffer = torch.empty(
                        (num_seqs * num_heads * max_num_partitions * head_size)
                        * nbytes_per_qo_elem
                        + 2 * (num_seqs * num_heads * max_num_partitions) * 4,
                        dtype=torch.uint8,
                        device=output.device,
                    )

                    # import so that aiter register the op to the namespace of
                    # torch.ops.aiter
                    importaiter  # noqa: F401

                    torch.ops.aiter.paged_attention_v1(
                        output[:num_decode_tokens],
                        workspace_buffer,
                        query[:num_decode_tokens],
                        key_cache,
                        value_cache,
                        self.scale,
                        attn_metadata.block_table[:num_decodes],
                        attn_metadata.query_start_loc[:num_decodes],
                        attn_metadata.seq_lens[:num_decodes],
                        attn_metadata.max_seq_len,
                        self.alibi_slopes,
                        self.kv_cache_dtype,
                        "NHD",
                        self.logits_soft_cap,
                        layer._k_scale,
                        layer._v_scale,
                        None,
                        _PARTITION_SIZE_ROCM,
                        1,
                        self.sliding_window[0] + 1,
                    )
        else:
            raise NotImplementedError(
                "Cascade attention is not implemented for ROCM AITER"
            )

        return output

    defdo_kv_cache_update(
        self,
        layer: AttentionLayer,
        key: torch.Tensor,
        value: torch.Tensor,
        kv_cache: torch.Tensor,
        slot_mapping: torch.Tensor,
    ):
        key_cache, value_cache = kv_cache.unbind(0)

        # key and value may be None in the case of cross attention. They are
        # calculated once based on the output from the encoder and then cached
        # in KV cache.
        if is_quantized_kv_cache(self.kv_cache_dtype):
            key_cache = key_cache.view(current_platform.fp8_dtype())
            value_cache = value_cache.view(current_platform.fp8_dtype())
        # Reshape the input keys and values and store them in the cache.
        # Skip this if sharing KV cache with an earlier attention layer.
        # NOTE(woosuk): Here, key and value are padded while slot_mapping
        # is not padded. However, we don't need to do
        # key[:num_actual_tokens] and value[:num_actual_tokens] because
        # the reshape_and_cache_flash op uses the slot_mapping's shape
        # to determine the number of actual tokens.
        if rocm_aiter_ops.is_shuffle_kv_cache_enabled():
            # We may calculate per token quant scale in
            # reshape_and_cache_shuffle_triton which might differ from
            # vllm's style when shuffle layout is used.
            k_scale = layer._k_scale
            v_scale = layer._v_scale
            assert k_scale is not None and v_scale is not None, (
                "k_scale and v_scale are required for shuffled update"
            )
            # TODO: Add correct KV cache handling for hybrid model. KV cache
            # may not be contiguous if mamba state exists.
            reshape_and_cache_shuffle_triton(
                key,
                value,
                key_cache,
                value_cache,
                slot_mapping,
                self.kv_cache_dtype,
                k_scale,
                v_scale,
            )
        else:
            torch.ops._C_cache_ops.reshape_and_cache_flash(
                key,
                value,
                key_cache,
                value_cache,
                slot_mapping,
                self.kv_cache_dtype,
                layer._k_scale,
                layer._v_scale,
            )

    deffused_rope_kvcache_supported(self):
        # Only support fusion when shuffle KV cache layout is not used;
        # shuffle layout uses a different cache update path.
        return (
            rocm_aiter_ops.is_enabled()
            and not rocm_aiter_ops.is_shuffle_kv_cache_enabled()
        )

    defdo_rope_and_kv_cache_update(
        self,
        layer: AttentionLayer,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        positions: torch.Tensor,
        cos_sin_cache: torch.Tensor,
        is_neox: bool,
        kv_cache: torch.Tensor,
        layer_slot_mapping: torch.Tensor,
    ):
        key_cache, value_cache = kv_cache.unbind(0)
        flash_layout = True

        is_fp8_kv_cache = is_quantized_kv_cache(self.kv_cache_dtype)
        if is_fp8_kv_cache:
            key_cache = key_cache.view(current_platform.fp8_dtype())
            value_cache = value_cache.view(current_platform.fp8_dtype())

        rocm_aiter_ops.triton_rope_and_cache(
            query,
            key,
            value,
            positions,
            cos_sin_cache,
            is_neox,
            key_cache,
            value_cache,
            layer_slot_mapping,
            layer._k_scale,
            layer._v_scale,
            flash_layout,
            is_fp8_kv_cache,
        )
```