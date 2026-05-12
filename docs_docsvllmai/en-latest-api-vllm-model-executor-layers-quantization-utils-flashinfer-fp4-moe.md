---
title: flashinfer_fp4_moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/utils/flashinfer_fp4_moe/
source: sitemap
fetched_at: 2026-05-07T21:27:50.839980028-03:00
rendered_js: false
word_count: 0
summary: This function prepares and transforms weight and scale tensors for the NvFP4 MoE backend by applying row interleaving and converting scale factors to the MMA layout required by the FlashInfer CuteDSL wrapper.
tags:
    - nvfp4
    - moe-layer
    - weight-transformation
    - flashinfer
    - cutedsl
    - tensor-manipulation
category: api
---

```
defprepare_nvfp4_moe_layer_for_flashinfer_cutedsl(
    layer: "FusedMoE",
    w13: torch.Tensor,
    w13_scale: torch.Tensor,
    w13_scale_2: torch.Tensor,
    a13_scale: torch.Tensor,
    w2: torch.Tensor,
    w2_scale: torch.Tensor,
    w2_scale_2: torch.Tensor,
    a2_scale: torch.Tensor,
) -> tuple[
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
    torch.Tensor,
]:
"""Prepare weights for the CuteDSL wrapper-based NvFP4 MoE backend.

    Converts weight scale factors to MMA layout expected by CuteDslMoEWrapper,
    and interleaves w13 gate/linear rows.
    """
    fromflashinfer.cute_dsl.utilsimport convert_sf_to_mma_layout

    # Global scaling factors (same as other FlashInfer backends).
    num_experts = w13.shape[0]
    a13_scale = a13_scale.max().to(torch.float32).expand(num_experts)
    a2_scale = a2_scale.max().to(torch.float32).expand(num_experts)

    half = w13.shape[1] // 2
    w13 = torch.cat([w13[:, half:], w13[:, :half]], dim=1)
    w13_scale = torch.cat([w13_scale[:, half:], w13_scale[:, :half]], dim=1)

    # Interleave up/gate rows for w13 weights and scales.
    w13 = interleave_linear_and_gate(w13, group_size=64, dim=1)
    w13_scale = interleave_linear_and_gate(w13_scale, group_size=64, dim=1)

    # Convert w13 scale factors: linear → swizzled → MMA layout.
    w13_scale = swizzle_blockscale(w13_scale)
    E, M_padded, K_sf_padded = w13_scale.shape
    w13_scale_flat = w13_scale.reshape(E * M_padded, K_sf_padded)
    w13_scale = convert_sf_to_mma_layout(
        w13_scale_flat,
        m=M_padded,
        k=K_sf_padded * 16,
        num_groups=E,
        sf_vec_size=16,
    )

    # Convert w2 scale factors: linear → swizzled → MMA layout.
    w2_scale = swizzle_blockscale(w2_scale)
    E, M_padded, K_sf_padded = w2_scale.shape
    w2_scale_flat = w2_scale.reshape(E * M_padded, K_sf_padded)
    w2_scale = convert_sf_to_mma_layout(
        w2_scale_flat,
        m=M_padded,
        k=K_sf_padded * 16,
        num_groups=E,
        sf_vec_size=16,
    )

    return (
        w13,
        w13_scale,
        w13_scale_2,
        a13_scale,
        w2,
        w2_scale,
        w2_scale_2,
        a2_scale,
    )
```