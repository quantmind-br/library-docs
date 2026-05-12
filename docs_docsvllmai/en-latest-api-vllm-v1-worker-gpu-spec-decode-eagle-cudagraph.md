---
title: cudagraph - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/gpu/spec_decode/eagle/cudagraph/
source: sitemap
fetched_at: 2026-05-07T21:42:58.430229903-03:00
rendered_js: false
word_count: 0
summary: This document defines the DecodeEagleCudaGraphManager class, which manages CUDA graph capture for decode draft generation by constructing custom attention metadata.
tags:
    - cuda-graph
    - attention-metadata
    - gpu-optimization
    - model-inference
    - decode-generation
category: api
---

```
classDecodeEagleCudaGraphManager(EagleCudaGraphManagerBase):
"""Eagle CudaGraphManager for decode draft generation, building its own
    attention metadata from scratch."""

    defcapture(
        self,
        forward_fn: Callable,
        model_state: ModelState,
        input_buffers: InputBuffers,
        block_tables: BlockTables,
        attn_groups: list[list[AttentionGroup]],
        kv_cache_config: KVCacheConfig,
        progress_bar_desc: str = "Capturing CUDA graphs",
    ) -> None:
        defcreate_forward_fn(
            desc: BatchExecutionDescriptor,
        ) -> tuple[Callable[[CUDAGraphMode], None], CapturedAttentionState]:
            num_tokens = desc.num_tokens
            num_reqs = desc.num_reqs or min(num_tokens, self.max_num_reqs)
            num_tokens_across_dp = (
                torch.full((self.dp_size,), num_tokens, dtype=torch.int32, device="cpu")
                if self.dp_size > 1
                else None
            )
            attn_state = prepare_inputs_to_capture(
                num_reqs,
                num_tokens,
                model_state,
                input_buffers,
                block_tables,
                attn_groups,
                kv_cache_config,
                skip_attn=(desc.cg_mode == CUDAGraphMode.PIECEWISE),
            )
            attn_metadata, slot_mappings = attn_state

            fwd = lambda cg_mode: forward_fn(
                num_reqs,
                num_tokens,
                attn_metadata,
                slot_mappings,
                num_tokens_across_dp,
                cg_mode,
            )
            return fwd, attn_state

        super().capture(create_forward_fn, progress_bar_desc)
```