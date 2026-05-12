---
title: flex_attention - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/attention/backends/flex_attention/
source: sitemap
fetched_at: 2026-05-07T21:39:10.55907868-03:00
rendered_js: false
word_count: 0
summary: This document defines the FlexAttentionMetadata class, which manages metadata and provides factory methods to generate mask modification functions for paged attention mechanisms in PyTorch.
tags:
    - flexattention
    - attention-mechanism
    - paged-attention
    - pytorch
    - metadata-management
    - mask-modification
category: concept
---

```
@dataclass
classFlexAttentionMetadata:
    causal: bool
    num_actual_tokens: int  # Number of tokens excluding padding.
    max_query_len: int
    query_start_loc: torch.Tensor
    max_seq_len: int
    seq_lens: torch.Tensor
    block_table: torch.Tensor
    slot_mapping: torch.Tensor

    use_cascade: bool
    common_prefix_len: int
    cu_prefix_query_lens: torch.Tensor | None
    prefix_kv_lens: torch.Tensor | None
    suffix_kv_lens: torch.Tensor | None

    # Block info
    total_cache_tokens: int
    block_size: int
    max_possible_sequence_length: int
    num_reqs: int
    physical_to_logical: torch.Tensor
    decode_offset: torch.Tensor
    num_blocks_per_seq: torch.Tensor
    persistent_kv_indices: torch.Tensor
    persistent_kv_num_blocks: torch.Tensor
    persistent_doc_ids: torch.Tensor

    # For logging.
    num_input_tokens: int = 0  # Number of tokens including padding.

    # Flex Metadata
    num_blocks = 0
    block_mask: BlockMask | None = None
    score_mod: _score_mod_signature | None = None
    logical_mask_mod: _mask_mod_signature = causal_mask_mod
    uses_paged_kv: bool = True
    doc_ids: torch.Tensor | None = None
    direct_build: bool = True
    q_block_size: int = 16
    kv_block_size: int = 16
    transformed_score_mod: _score_mod_signature | None = None
    sliding_window: int | None = None
    mm_prefix_range: dict[int, list[tuple[int, int]]] | None = None
    block_sparsity_hint: BlockSparsityHint | None = None

    @cached_property
    deflogical_block_ids(self):
        return torch.arange(
            cdiv(self.max_seq_len, self.block_size),
            device=self.block_table.device,
            dtype=torch.long,
        )

    def_convert_physical_to_logical(
        self,
        request_lookup: torch.Tensor,
        q_idx: torch.Tensor,
        physical_kv_idx: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
"""Convert physical indices to logical indices for both query and kv.

        NB is_within_lower_bound: do sequences start on block_boundaries?

        Returns:
            tuple of (is_valid, logical_q_idx, logical_kv_idx)
        """
        # Map query indices to corresponding request indices
        q_req = request_lookup[q_idx]

        # Convert physical KV indices to logical indices
        physical_kv_block = physical_kv_idx // self.block_size
        physical_kv_offset = physical_kv_idx % self.block_size
        logical_block_idx = self.physical_to_logical[q_req, physical_kv_block]
        logical_kv_idx = logical_block_idx * self.block_size + physical_kv_offset

        # Determine valid kv indices
        live_block = logical_block_idx >= 0
        within_upper_bound = logical_kv_idx < self.seq_lens[q_req]
        within_lower_bound = logical_kv_idx >= 0
        is_valid = live_block & within_upper_bound & within_lower_bound

        # Convert physical query indices to logical indices
        local_q_idx = q_idx - self.query_start_loc[q_req]
        logical_q_idx = local_q_idx + self.decode_offset[q_req]

        return is_valid, logical_q_idx, logical_kv_idx

    defget_paged_mask_mod(self) -> _mask_mod_signature:
"""Creates the mask_mod function for FlexAttention.

        This function creates the combined mask mod function that handles:
            1. The paged attention block mapping
            2. The mapping from packed query sequences to logical query entries

        It also by defaults adds the decoding offset to the query indices.
        With this info we create the "logical" indices that are passed to
        mask_mod functions. This allows mask mod functions to be agnostic to
        layout of the query and key/value tensors.
        """
        assert self.doc_ids is not None

        deffinal_mask_mod(
            b: torch.Tensor,
            h: torch.Tensor,
            q_idx: torch.Tensor,
            physical_kv_idx: torch.Tensor,
        ) -> torch.Tensor:
            (is_valid, logical_q_idx, logical_kv_idx) = (
                self._convert_physical_to_logical(self.doc_ids, q_idx, physical_kv_idx)
            )
            # Apply mask modification only for valid indices
            return torch.where(
                is_valid,
                self.logical_mask_mod(b, h, logical_q_idx, logical_kv_idx),
                False,
            )

        return final_mask_mod

    defget_bidirectional_mask_mod(self) -> _mask_mod_signature:
"""Creates the encoder mask_mod function for FlexAttention.

        Since the encoder bidirectional attention doesn't run with
        KV cache, this function creates a mask based on the
        packed query sequences.
        """
        # Create a lookup mapping from query indices -> request number
        request_lookup = _offsets_to_doc_ids_tensor(self.query_start_loc)

        deffinal_mask_mod(
            b: torch.Tensor,
            h: torch.Tensor,
            q_idx: torch.Tensor,
            kv_idx: torch.Tensor,
        ) -> torch.Tensor:
            return request_lookup[q_idx] == request_lookup[kv_idx]

        return final_mask_mod

    defget_sliding_window_mask_mod(self) -> _mask_mod_signature:
"""Creates the sliding window mask_mod function for FlexAttention.

        Note that the sliding window mask here is bidirectional, we need
        to mask it with the bidirectional/causal mask for encoder/decoder.
        """

        if self.sliding_window is None:
            raise ValueError("sliding_window must be set for sliding window attention")

        defsliding_window_mask_mod(
            b: torch.Tensor, h: torch.Tensor, q_idx: torch.Tensor, kv_idx: torch.Tensor
        ):
            return torch.abs(q_idx - kv_idx) < self.sliding_window

        deffinal_mask_mod(
            b: torch.Tensor,
            h: torch.Tensor,
            q_idx: torch.Tensor,
            physical_kv_idx: torch.Tensor,
        ) -> torch.Tensor:
            (is_valid, logical_q_idx, logical_kv_idx) = (
                self._convert_physical_to_logical(self.doc_ids, q_idx, physical_kv_idx)
            )
            return torch.where(
                is_valid,
                sliding_window_mask_mod(b, h, logical_q_idx, logical_kv_idx),
                False,
            )

        return final_mask_mod if self.uses_paged_kv else sliding_window_mask_mod

    defget_prefix_lm_mask_mod(self) -> _mask_mod_signature:
"""Creates the prefix LM mask_mod function for FlexAttention."""

        assert self.doc_ids is not None
        request_lookup = self.doc_ids

        defprefix_lm_mask_mod(
            b: torch.Tensor,
            h: torch.Tensor,
            cu_q_idx: torch.Tensor,
            q_idx: torch.Tensor,
            kv_idx: torch.Tensor,
        ):
            mask = torch.zeros_like(q_idx, dtype=torch.bool)
            for req, doc_range_lst in (self.mm_prefix_range or {}).items():
                req_mask = request_lookup[cu_q_idx] == req
                for start, end in doc_range_lst:
                    doc_mask_q = (q_idx >= start) & (q_idx <= end)
                    doc_mask_kv = (kv_idx >= start) & (kv_idx <= end)
                    mask = mask | (req_mask & doc_mask_q & doc_mask_kv)
            return mask

        deffinal_mask_mod(
            b: torch.Tensor,
            h: torch.Tensor,
            q_idx: torch.Tensor,
            physical_kv_idx: torch.Tensor,
        ) -> torch.Tensor:
            (is_valid, logical_q_idx, logical_kv_idx) = (
                self._convert_physical_to_logical(self.doc_ids, q_idx, physical_kv_idx)
            )
            return torch.where(
                is_valid,
                prefix_lm_mask_mod(b, h, q_idx, logical_q_idx, logical_kv_idx),
                False,
            )

        return final_mask_mod

    defget_mask_mod(self):
        # Stage-1: initialize the base mask_mod
        # (causal mask for decoder or bidirectional mask for encoder)
        if self.uses_paged_kv:
            mask_mod = self.get_paged_mask_mod()
        else:
            mask_mod = self.get_bidirectional_mask_mod()
        # stage-2: add external mask_mod for special attention during
        # forwarding runtime to create the combined mask_mod.
        if self.sliding_window is not None:
            # Add sliding window mask for sliding window attention
            sliding_window_mask_mod = self.get_sliding_window_mask_mod()
            mask_mod = and_masks(mask_mod, sliding_window_mask_mod)
        if self.mm_prefix_range:
            # Add prefix LM mask for vision-language prefix LM attention
            prefix_lm_mask_mod = self.get_prefix_lm_mask_mod()
            mask_mod = or_masks(mask_mod, prefix_lm_mask_mod)
        return mask_mod

    defget_transformed_score_mod(self) -> _score_mod_signature | None:
"""Creates the transformed score_mod function for FlexAttention.

        This function wraps the user's score_mod to handle physical-to-logical
        index conversion, similar to how get_mask_mod works for mask functions.
        """
        if self.score_mod is None:
            return None

        # Create a lookup mapping from query indices -> request number
        request_lookup = _offsets_to_doc_ids_tensor(self.query_start_loc)
        user_score_mod = self.score_mod

        deftransformed_score_mod(
            score: torch.Tensor,
            b: torch.Tensor,
            h: torch.Tensor,
            q_idx: torch.Tensor,
            physical_kv_idx: torch.Tensor,
        ) -> torch.Tensor:
            (is_valid, logical_q_idx, logical_kv_idx) = (
                self._convert_physical_to_logical(
                    request_lookup, q_idx, physical_kv_idx
                )
            )

            return torch.where(
                is_valid,
                user_score_mod(
                    score, b, h, logical_q_idx, logical_kv_idx, physical_q=q_idx
                ),
                -float("inf"),
            )

        return transformed_score_mod

    def_build_block_mask_direct(self) -> BlockMask:
"""Direct block mask construction for paged KV cache attention.

        This method constructs the block mask directly using
        BlockMask.from_kv_blocks which is much more efficient than the
        generic create_block_mask approach.

        The direct path works as follows:
        1. For each query token, fetch blocks from block_table using max_seq_len
           and exclude out of sliding window blocks if needed.
           (this fetches more blocks than needed for shorter sequences)
        2. Group query tokens into chunks of q_block_size
        3. For each group, deduplicate the blocks using unique_static_unsorted
        4. Create BlockMask using the deduplicated block indices

        Over-estimation occurs when a group of q_block_size tokens contains
        multiple sequence IDs (doc_ids). In this case, we fetch ALL blocks for
        each sequence represented in the group, even though individual query
        tokens may only need a subset of those blocks based on causal masking
        and their position.

        """
        page_to_block_ratio = self.kv_block_size // self.block_size
        if page_to_block_ratio != 1:
            raise ValueError(
                f"FlexAttention currently requires the cache block size "
                f"({self.block_size}) to be equal to the kv_block_size "
                f"({self.kv_block_size}). Please check your model's "
                f"configuration."
            )

        used_pages = self.block_table[
            self.doc_ids, : cdiv(self.max_seq_len, self.block_size)
        ]

        custom_hint = self.block_sparsity_hint is not None

        if self.sliding_window or custom_hint:
            device = used_pages.device
            assert self.doc_ids is not None
            token_indices = torch.arange(
                self.doc_ids.shape[0], device=device, dtype=torch.long
            )
            logical_q_idx = (
                token_indices
                - self.query_start_loc[self.doc_ids]
                + self.decode_offset[self.doc_ids]
            )

            if self.sliding_window:
                assert self.sliding_window is not None
                min_kv_idx = torch.clamp(
                    logical_q_idx - (self.sliding_window - 1), min=0
                )
                min_block_idx = min_kv_idx // self.block_size
                sliding_mask = self.logical_block_ids >= min_block_idx[:, None]
                used_pages.masked_fill_(~sliding_mask, 0)
            if custom_hint:
                assert self.block_sparsity_hint is not None
                q_block_idx = logical_q_idx // self.block_size
                hint_mask = self.block_sparsity_hint.hint_fn(
                    q_block_idx[:, None],
                    self.logical_block_ids[None, :],
                    self.block_size,
                )
                used_pages.masked_fill_(~hint_mask, 0)

        used_pages_padded = pad_to_multiple(
            used_pages, multiple=self.q_block_size, dim=0
        )
        used_pages_padded = used_pages_padded.reshape(
            used_pages_padded.shape[0] // self.q_block_size, -1
        )
        used_pages_padded = used_pages_padded // page_to_block_ratio
        kv_indices = unique_static_unsorted(
            (used_pages_padded.long()), M=self.num_blocks
        ).to(torch.int32)
        kv_indices = copy_to_persistent(self.persistent_kv_indices, kv_indices)

        kv_num_blocks = (kv_indices >= 0).sum(dim=-1).to(torch.int32)
        kv_num_blocks = copy_to_persistent(self.persistent_kv_num_blocks, kv_num_blocks)

        block_mask_kwargs = {
            "seq_lengths": (self.num_actual_tokens, self.total_cache_tokens),
            "kv_num_blocks": kv_num_blocks[None, None],
            "kv_indices": kv_indices[None, None],
            "full_kv_num_blocks": None,
            "full_kv_indices": None,
            "BLOCK_SIZE": (self.q_block_size, self.kv_block_size),
            "mask_mod": self.mask_mod,
        }

        # compute_q_blocks parameter is available in PyTorch 2.9+
        if is_torch_equal_or_newer("2.9.0.dev0"):
            block_mask_kwargs["compute_q_blocks"] = False
        return BlockMask.from_kv_blocks(**block_mask_kwargs)

    defbuild_block_mask(self) -> BlockMask:
        mask_mod = self.get_mask_mod()
        kv_len = (
            self.total_cache_tokens if self.uses_paged_kv else self.num_actual_tokens
        )
        return create_block_mask_compiled(
            mask_mod,
            None,
            None,
            self.num_actual_tokens,
            kv_len,
            device=self.block_table.device,
            BLOCK_SIZE=(self.q_block_size, self.kv_block_size),
        )

    def__post_init__(self):
        assert self.use_cascade is False, "Not implemented yet."
        assert self.common_prefix_len == 0, "Not implemented yet."
        assert self.cu_prefix_query_lens is None, "Not implemented yet."
        assert self.prefix_kv_lens is None, "Not implemented yet."
        assert self.suffix_kv_lens is None, "Not implemented yet."
        # Create a lookup mapping from query indices -> request number
        self.doc_ids = _offsets_to_doc_ids_tensor(self.query_start_loc)
        self.doc_ids = copy_to_persistent(self.persistent_doc_ids, self.doc_ids)
        self.num_blocks = self.total_cache_tokens // self.block_size

        self.mask_mod = self.get_mask_mod()
        self.transformed_score_mod = self.get_transformed_score_mod()
```