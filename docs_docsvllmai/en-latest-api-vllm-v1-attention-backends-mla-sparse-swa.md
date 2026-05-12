---
title: sparse_swa - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/mla/sparse_swa/
source: sitemap
fetched_at: 2026-05-07T21:39:35.450722441-03:00
rendered_js: false
word_count: 34
summary: This class implements metadata construction for DeepseekV4 models using sliding window attention (SWA) within the vLLM framework, managing mixed prefill and decode batches.
tags:
    - deepseek
    - vllm
    - sliding-window-attention
    - kv-cache
    - mla
    - attention-metadata
category: concept
---

```
classDeepseekSparseSWAMetadataBuilder(AttentionMetadataBuilder):
"""Builds metadata for DeepseekV4 SWA cache.

    Similar to the indexer, this handles mixed batches by:
    1. Using split_decodes_and_prefills() to determine the boundary
    2. Building separate metadata for decode and prefill portions

    Supports:
    - Mixed decode/prefill batches
    - MTP (Multi-Token Prediction) where decode has query_len > 1
    - Chunked prefill (aligns with the indexer's chunking)
    """

    # Base threshold: query_len <= 1 is decode
    reorder_batch_threshold: int = 1
    _cudagraph_support: ClassVar[AttentionCGSupport] = AttentionCGSupport.UNIFORM_BATCH

    def__init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(self.kv_cache_spec, SlidingWindowMLASpec | MLAAttentionSpec)
        mla_spec = cast(SlidingWindowMLASpec | MLAAttentionSpec, self.kv_cache_spec)
        self.head_size = mla_spec.head_size  # Already considered quantization.
        self.compress_ratio = mla_spec.compress_ratio
        self.block_size = mla_spec.block_size

        # Handle MTP: adjust decode_threshold like the indexer does
        self.num_speculative_tokens = (
            self.vllm_config.speculative_config.num_speculative_tokens
            if self.vllm_config.speculative_config
            else 0
        )
        # With MTP, decode can have query_len up to 1 + num_speculative_tokens.
        # Must match the threshold used by the indexer and flashmla_sparse so
        # that all backends agree on the decode/prefill split.
        self.decode_threshold = (
            self.reorder_batch_threshold + self.num_speculative_tokens
        )

        hf_config = self.vllm_config.model_config.hf_config
        assert hasattr(hf_config, "sliding_window")
        self.window_size = hf_config.sliding_window

        # Detect which DeepseekV4 layer types this model uses so we only build a
        # FlashMLA tile-scheduler plan for types that will actually be called.
        # Models without compress_ratios (pure SWA) fall back to swaonly.
        compress_ratios = getattr(hf_config, "compress_ratios", None) or [1]
        self._layer_types: set[str] = set()
        for ratio in compress_ratios:
            self._layer_types.add(_layer_type_for(int(ratio)))

        max_tokens = self.vllm_config.scheduler_config.max_num_batched_tokens
        self.token_to_req_indices = torch.zeros(
            max_tokens,
            dtype=torch.int32,
            device=self.device,
        )
        self.decode_swa_indices = torch.zeros(
            max_tokens,
            1,
            self.window_size,
            dtype=torch.int32,
            device=self.device,
        )
        self.decode_swa_lens = torch.zeros(
            max_tokens,
            dtype=torch.int32,
            device=self.device,
        )
        self.is_valid_token = torch.zeros(
            max_tokens,
            dtype=torch.bool,
            device=self.device,
        )

    defbuild(
        self,
        common_prefix_len: int,
        common_attn_metadata: CommonAttentionMetadata,
        fast_build: bool = False,
    ) -> DeepseekSparseSWAMetadata:
"""Build SWA metadata for mixed decode/prefill batches.

        The batch is assumed to be reordered with decodes first (by vLLM scheduler).
        We use split_decodes_and_prefills() to find the boundary, then build
        separate window_topk_idxs for each portion.

        For prefill, we use chunked prefill to align with the indexer's chunking.
        """
        num_reqs = common_attn_metadata.num_reqs
        seq_lens = common_attn_metadata.seq_lens
        query_start_loc = common_attn_metadata.query_start_loc
        query_start_loc_cpu = common_attn_metadata.query_start_loc_cpu
        block_table = common_attn_metadata.block_table_tensor
        slot_mapping = common_attn_metadata.slot_mapping

        # Split into decode and prefill portions using configurable threshold
        (num_decodes, num_prefills, num_decode_tokens, num_prefill_tokens) = (
            split_decodes_and_prefills(
                common_attn_metadata, decode_threshold=self.decode_threshold
            )
        )

        # NOTE: Ensure all metadata tensors maintain fixed memory addresses
        # for CUDA graph compatibility.
        query_lens = query_start_loc_cpu[1:] - query_start_loc_cpu[:-1]
        x = torch.repeat_interleave(torch.arange(num_reqs), query_lens).pin_memory()
        token_to_req_indices = self.token_to_req_indices[: x.shape[0]]
        token_to_req_indices.copy_(x, non_blocking=True)

        is_valid_token = self.is_valid_token[: slot_mapping.shape[0]]
        is_valid_token.copy_(slot_mapping >= 0)

        if num_decode_tokens > 0:
            self.decode_swa_lens[num_decode_tokens:] = 0
            _compute_swa_indices_and_lens_kernel[(num_decode_tokens,)](
                self.decode_swa_indices,
                self.decode_swa_indices.stride(0),
                self.decode_swa_lens,
                self.window_size,
                query_start_loc,
                seq_lens,
                token_to_req_indices,
                is_valid_token,
                block_table,
                block_table.stride(0),
                self.block_size,
                TRITON_BLOCK_SIZE=1024,
            )

        # Pre-compute DeepseekV4 prefill metadata shared across all attention layers.
        deepseek_v4_fields = self._build_deepseek_v4_metadata(
            num_decodes,
            num_prefills,
            seq_lens,
            query_start_loc,
        )

        # Per-layer-type tile-scheduler plan holders. Empty FlashMLASchedMeta
        # per present DeepseekV4 layer type; the first flash_mla_with_kvcache call of
        # each type triggers the planner and all same-type layers reuse the
        # resulting plan for the rest of the step.
        tile_sched = self.build_tile_scheduler(num_decode_tokens)

        return DeepseekSparseSWAMetadata(
            seq_lens=seq_lens,
            query_start_loc=query_start_loc,
            query_start_loc_cpu=query_start_loc_cpu,
            block_table=block_table,
            slot_mapping=slot_mapping,
            is_valid_token=is_valid_token,
            token_to_req_indices=token_to_req_indices,
            decode_swa_indices=self.decode_swa_indices[:num_decode_tokens],
            decode_swa_lens=self.decode_swa_lens[:num_decode_tokens],
            block_size=self.block_size,
            num_decodes=num_decodes,
            num_prefills=num_prefills,
            num_decode_tokens=num_decode_tokens,
            num_prefill_tokens=num_prefill_tokens,
            tile_sched_swaonly=tile_sched[_LAYER_TYPE_SWAONLY],
            tile_sched_c4a=tile_sched[_LAYER_TYPE_C4A],
            tile_sched_c128a=tile_sched[_LAYER_TYPE_C128A],
            **deepseek_v4_fields,
        )

    defbuild_tile_scheduler(
        self, num_decode_tokens: int
    ) -> dict[str, FlashMLASchedMeta | None]:
"""Allocate one empty ``FlashMLASchedMeta`` per present DeepseekV4 layer type.

        Returned instances have ``tile_scheduler_metadata`` / ``num_splits``
        set to ``None``; the FlashMLA C++ decode path will allocate them and
        run the tile-scheduler planner on the first ``flash_mla_with_kvcache``
        call of each type. Subsequent same-type calls reuse the plan because
        the tensors (and ``have_initialized``) are populated on the struct.

        Returns all-``None`` when there are no decode tokens this step, so
        ``_forward_decode`` sees a clean sentinel.
        """
        out: dict[str, FlashMLASchedMeta | None] = {
            _LAYER_TYPE_SWAONLY: None,
            _LAYER_TYPE_C4A: None,
            _LAYER_TYPE_C128A: None,
        }
        if num_decode_tokens == 0 or current_platform.is_rocm():
            return out
        for layer_type in self._layer_types:
            # get_mla_metadata() is the official FlashMLA entry point that
            # returns a fresh empty FlashMLASchedMeta; using it keeps this
            # call site aligned with the rest of the vLLM FlashMLA backends
            # that already go through the same stub.
            out[layer_type] = get_mla_metadata()[0]
        return out

    def_build_deepseek_v4_metadata(
        self,
        num_decodes: int,
        num_prefills: int,
        seq_lens: torch.Tensor,
        query_start_loc: torch.Tensor,
    ) -> dict[str, torch.Tensor | None]:
"""Pre-compute DeepseekV4 prefill metadata during the metadata build phase.

        Returns a dict of keyword arguments to pass to the
        DeepseekSparseSWAMetadata constructor.

        Note: C128A topk indices are computed by the FlashMLASparse builder
        (which owns the C128A block_table), not here.
        """
        result: dict[str, torch.Tensor | None] = {}

        # --- Prefill query metadata (single Triton kernel + CPU slicing) ---
        if num_prefills > 0:
            pfx_gather_lens = torch.empty(
                num_prefills, dtype=torch.int32, device=seq_lens.device
            )
            _compute_prefill_metadata_kernel[(1,)](
                pfx_gather_lens,
                seq_lens,
                query_start_loc,
                num_prefills,
                num_decodes,
                self.window_size,
                BLOCK_SIZE=triton.next_power_of_2(num_prefills),
            )

            result["prefill_seq_lens"] = seq_lens[num_decodes:]
            result["prefill_gather_lens"] = pfx_gather_lens

        return result
```