---
title: rope - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/gpu/mm/rope/
source: sitemap
fetched_at: 2026-05-07T21:42:33.364843812-03:00
rendered_js: false
word_count: 11
summary: This document defines a state management class for handling multi-dimensional Rotary Positional Embeddings (RoPE) variants, specifically M-RoPE and XD-RoPE, within a deep learning framework.
tags:
    - rope
    - positional-embedding
    - tensor-management
    - deep-learning
    - gpu-kernel
category: concept
---

```
classRopeState:
"""Unified state for multi-dimensional RoPE variants (M-RoPE, XD-RoPE).

    M-RoPE: 3 dims, uses position delta for decode.
    XD-RoPE: 3 or 4 dims, delta is 0 (decode uses orig_pos for all dims).

    NOTE: `positions` is implemented with one additional dummy position on
    purpose to make it non-contiguous so that it can work with torch compile.
    See detailed explanation in
    https://github.com/vllm-project/vllm/pull/12128#discussion_r1926431923

    NOTE: When M-RoPE is enabled, position ids are 3D regardless of the
    modality of inputs. For text-only inputs, each dimension has identical
    position IDs, making M-RoPE functionally equivalent to 1D-RoPE.
    See page 5 of https://arxiv.org/abs/2409.12191
    """

    def__init__(
        self,
        num_dims: int,
        has_delta: bool,
        max_num_reqs: int,
        max_num_tokens: int,
        max_model_len: int,
        device: torch.device,
    ):
        self.num_dims = num_dims
        self.has_delta = has_delta
        self.max_num_reqs = max_num_reqs
        self.max_num_tokens = max_num_tokens
        self.max_model_len = max_model_len
        self.device = device

        # NOTE(woosuk): This tensor can be extremely large (e.g., several GBs)
        # wasting a lot of CPU memory.
        self.prefill_positions = StagedWriteTensor(
            (max_num_reqs * num_dims, max_model_len),
            dtype=torch.int32,
            device=device,
            uva_instead_of_gpu=True,
        )
        self.positions = torch.zeros(
            (num_dims, max_num_tokens + 1), dtype=torch.int64, device=device
        )

        # Delta is non-zero for M-RoPE, always 0 for XD-RoPE.
        self.prefill_delta = UvaBackedTensor(max_num_reqs, dtype=torch.int32)

    definit_prefill_positions(
        self,
        req_idx: int,
        model: nn.Module,
        prefill_token_ids: list[int],
        mm_features: list,
    ) -> None:
        if self.has_delta:
            mrope_model = cast(SupportsMRoPE, model)
            prefill_positions, delta = mrope_model.get_mrope_input_positions(
                prefill_token_ids, mm_features
            )
            self.prefill_delta.np[req_idx] = delta
        else:
            xdrope_model = cast(SupportsXDRoPE, model)
            prefill_positions = xdrope_model.get_xdrope_input_positions(
                prefill_token_ids, mm_features
            )

        for i in range(self.num_dims):
            pos = prefill_positions[i].tolist()
            self.prefill_positions.stage_write(self.num_dims * req_idx + i, 0, pos)

    defapply_staged_writes(self) -> None:
        self.prefill_positions.apply_write()
        if self.has_delta:
            self.prefill_delta.copy_to_uva()

    defget_positions(self, num_tokens: int) -> torch.Tensor:
        return self.positions[:, :num_tokens]

    defprepare_positions(
        self,
        idx_mapping: torch.Tensor,
        query_start_loc: torch.Tensor,
        prefill_lens: torch.Tensor,
        num_computed_tokens: torch.Tensor,
    ) -> None:
        num_reqs = idx_mapping.shape[0]
        _prepare_rope_positions_kernel[(num_reqs,)](
            self.positions,
            self.positions.stride(0),
            self.prefill_positions.gpu,
            self.num_dims * self.max_model_len,
            self.max_model_len,
            self.prefill_delta.gpu,
            idx_mapping,
            query_start_loc,
            prefill_lens,
            num_computed_tokens,
            BLOCK_SIZE=1024,
            NUM_DIMS=self.num_dims,
        )
```