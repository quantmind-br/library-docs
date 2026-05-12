---
title: int_wna16 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/int_wna16/
source: sitemap
fetched_at: 2026-05-07T21:25:08.901373556-03:00
rendered_js: false
word_count: 15
summary: This function performs the post-processing of quantized model weights for the Marlin inference backend, including weight repacking, scale permutation, and activation order handling.
tags:
    - marlin
    - quantization
    - weight-processing
    - gptq
    - model-optimization
    - tensor-manipulation
category: api
---

```
def_process_weights_marlin(
    layer: torch.nn.Module,
    quant_config: "GPTQMarlinConfig",
    input_dtype: torch.dtype | None,
    w13_qweight: torch.Tensor,
    w2_qweight: torch.Tensor,
    w13_scales: torch.Tensor,
    w2_scales: torch.Tensor,
    w13_g_idx: torch.Tensor,
    w2_g_idx: torch.Tensor,
    w13_bias: torch.Tensor | None = None,
    w2_bias: torch.Tensor | None = None,
) -> tuple[
    torch.Tensor,  # w13_qweight
    torch.Tensor,  # w2_qweight
    torch.Tensor,  # w13_scales
    torch.Tensor,  # w2_scales
    torch.Tensor,  # w13_g_idx
    torch.Tensor,  # w2_g_idx
    torch.Tensor,  # w13_g_idx_sort_indices
    torch.Tensor,  # w2_g_idx_sort_indices
    torch.Tensor | None,  # w13_input_global_scale
    torch.Tensor | None,  # w2_input_global_scale
    torch.Tensor | None,  # w13_bias
    torch.Tensor | None,  # w2_bias
]:
"""Standard Marlin weight post-processing shared by MARLIN and
    BATCHED_MARLIN backends.

    Steps
    -----
    1. Optional FP8 preprocessing of packed weights / scales.
    2. Sort / reset g_idx tensors for act-order handling.
    3. Repack weights via ``gptq_marlin_moe_repack``.
    4. Permute scales (and optionally extract INT8 global scales).
    5. Permute bias tensors.
    """
    is_a_8bit = input_dtype is not None and input_dtype.itemsize == 1

    marlin_w13_qweight: torch.Tensor
    marlin_w2_qweight: torch.Tensor
    marlin_w13_scales: torch.Tensor
    marlin_w2_scales: torch.Tensor
    w13_g_idx_sort_indices: torch.Tensor | None = None
    w2_g_idx_sort_indices: torch.Tensor | None = None
    w13_input_global_scale: torch.Tensor | None = None
    w2_input_global_scale: torch.Tensor | None = None
    w13_bias_out: torch.Tensor | None = None
    w2_bias_out: torch.Tensor | None = None

    # --- FP8 weight / scale adjustment ---
    if input_dtype == torch.float8_e4m3fn:
        marlin_w13_qweight = ops.marlin_int4_fp8_preprocess(w13_qweight, inplace=False)
        marlin_w2_qweight = ops.marlin_int4_fp8_preprocess(w2_qweight, inplace=False)
        marlin_w13_scales = w13_scales.data * 512
        marlin_w2_scales = w2_scales.data * 512
    else:
        marlin_w13_qweight = w13_qweight
        marlin_w2_qweight = w2_qweight
        marlin_w13_scales = w13_scales
        marlin_w2_scales = w2_scales

    # --- Process act_order (g_idx) ---
    if quant_config.desc_act:
        num_experts = w13_g_idx.shape[0]
        w13_g_idx_sort_indices = torch.empty_like(w13_g_idx)
        w2_g_idx_sort_indices = torch.empty_like(w2_g_idx)
        w13_sorted_g_idx = torch.empty_like(w13_g_idx)
        w2_sorted_g_idx = torch.empty_like(w2_g_idx)
        for e in range(num_experts):
            w13_g_idx_sort_indices[e] = torch.argsort(w13_g_idx[e]).to(torch.int32)
            w2_g_idx_sort_indices[e] = torch.argsort(w2_g_idx[e]).to(torch.int32)
            w13_sorted_g_idx[e] = w13_g_idx[e][w13_g_idx_sort_indices[e]]
            w2_sorted_g_idx[e] = w2_g_idx[e][w2_g_idx_sort_indices[e]]
    else:
        num_experts = w13_g_idx.shape[0]
        device = w13_g_idx.device
        w13_g_idx = torch.nn.Parameter(
            torch.empty((num_experts, 0), dtype=torch.int32, device=device),
            requires_grad=False,
        )
        w2_g_idx = torch.nn.Parameter(
            torch.empty((num_experts, 0), dtype=torch.int32, device=device),
            requires_grad=False,
        )
        w13_g_idx_sort_indices = torch.nn.Parameter(
            torch.empty((num_experts, 0), dtype=torch.int32, device=device),
            requires_grad=False,
        )
        w2_g_idx_sort_indices = torch.nn.Parameter(
            torch.empty((num_experts, 0), dtype=torch.int32, device=device),
            requires_grad=False,
        )

    # --- Repack weights ---
    marlin_w13_qweight = ops.gptq_marlin_moe_repack(
        marlin_w13_qweight,
        w13_g_idx_sort_indices,
        marlin_w13_qweight.shape[1] * quant_config.pack_factor,
        marlin_w13_qweight.shape[2],
        quant_config.quant_type.size_bits,
        is_a_8bit=is_a_8bit,
    )
    marlin_w2_qweight = ops.gptq_marlin_moe_repack(
        marlin_w2_qweight,
        w2_g_idx_sort_indices,
        marlin_w2_qweight.shape[1] * quant_config.pack_factor,
        marlin_w2_qweight.shape[2],
        quant_config.quant_type.size_bits,
        is_a_8bit=is_a_8bit,
    )

    # --- Permute scales ---
    marlin_w13_scales = marlin_moe_permute_scales(
        s=marlin_w13_scales,
        size_k=layer.intermediate_size_per_partition,
        size_n=marlin_w13_scales.shape[2],
        group_size=quant_config.group_size,
        is_a_8bit=is_a_8bit,
    )
    marlin_w2_scales = marlin_moe_permute_scales(
        s=marlin_w2_scales,
        size_k=marlin_w2_scales.shape[1]
        * (
            quant_config.group_size
            if quant_config.group_size != -1
            else quant_config.pack_factor
        ),
        size_n=marlin_w2_scales.shape[2],
        group_size=quant_config.group_size,
        is_a_8bit=is_a_8bit,
    )

    if input_dtype == torch.int8:
        if layer.num_groups_w13 > 1:
            marlin_w13_scales, w13_input_global_scale = marlin_act_int8_process_scales(
                marlin_w13_scales
            )
        if layer.num_groups_w2 > 1:
            marlin_w2_scales, w2_input_global_scale = marlin_act_int8_process_scales(
                marlin_w2_scales
            )

    # --- Permute bias ---
    if w13_bias is not None:
        w13_bias_out = marlin_permute_bias(w13_bias)
    if w2_bias is not None:
        w2_bias_out = marlin_permute_bias(w2_bias)

    return (
        marlin_w13_qweight,
        marlin_w2_qweight,
        marlin_w13_scales,
        marlin_w2_scales,
        w13_g_idx,
        w2_g_idx,
        w13_g_idx_sort_indices,
        w2_g_idx_sort_indices,
        w13_input_global_scale,
        w2_input_global_scale,
        w13_bias_out,
        w2_bias_out,
    )
```