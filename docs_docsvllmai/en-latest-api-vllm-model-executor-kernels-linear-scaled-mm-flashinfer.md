---
title: flashinfer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/flashinfer/
source: sitemap
fetched_at: 2026-05-07T21:23:49.606808793-03:00
rendered_js: false
word_count: 0
summary: This document describes a conditional implementation of FP8 blockscale GEMM that selects optimized kernels based on input batch size to preserve model accuracy during graph compilation.
tags:
    - fp8-gemm
    - batch-size-optimization
    - torch-compile
    - tensor-quantization
    - graph-compilation
    - kernel-selection
category: api
---

```
def_dynamic_flashinfer_deepgemm_blockscale_gemm_impl(
    input: torch.Tensor,
    weight: torch.Tensor,
    weight_scale: torch.Tensor,
    group_size: int,
    use_deep_gemm_e8m0: bool,
) -> torch.Tensor:
"""
    Conditional FlashInfer FP8 blockscale GEMM with batch-size-dependent selection.

    This function switches between two optimized kernels based on the input batch size:
    - For small batches (M < 32): Uses FlashInfer's DeepGEMM swapAB optimization.
    - For larger batches (M >= 32): Uses the official DeepGEMM kernel.

    The conditional logic must use torch.cond() instead of a simple if-else statement
    to maintain compatibility with torch.compile graph compilation.

    This batch-size-dependent selection is essential for maintaining model accuracy.
    Benchmarks on GSM8K show a significant accuracy gap (88% vs 95%) for DeepSeek-V3.1
    when using FlashInfer's DeepGEMM on M>=32. The M < 32 strategy fixes the accuracy
    drop.

    Args:
        input: Input tensor of shape (batch_size, input_dim) in FP8 format
        weight: Weight tensor of shape (output_dim, input_dim) in FP8 format
        weight_scale: Scale factors for weight quantization (per-group)
        group_size: Quantization group size for the weight tensor
        use_deep_gemm_e8m0: Whether to use the E8M0 format in DeepGEMM quantization

    Returns:
        Output tensor of shape (batch_size, output_dim) in bfloat16 format
    """

    defrun_flashinfer_deepgemm_swapAB(
        input: torch.Tensor,
        weight: torch.Tensor,
        weight_scale: torch.Tensor,
    ) -> torch.Tensor:
        return flashinfer_fp8_blockscale_gemm(
            input=input,
            weight=weight,
            weight_scale=weight_scale,
            out_dtype=torch.bfloat16,
        )

    defrun_deepgemm(
        input: torch.Tensor,
        weight: torch.Tensor,
        weight_scale: torch.Tensor,
    ) -> torch.Tensor:
        q_input, input_scale = per_token_group_quant_fp8(
            input,
            group_size=group_size,
            column_major_scales=True,
            use_ue8m0=use_deep_gemm_e8m0,
        )
        output = torch.empty(
            (q_input.shape[0], weight.shape[0]),
            dtype=torch.bfloat16,
            device=q_input.device,
        )
        fp8_gemm_nt(
            (q_input, input_scale),
            (weight, weight_scale),
            output,
            is_deep_gemm_e8m0_used=use_deep_gemm_e8m0,
        )
        return output

    if envs.VLLM_BATCH_INVARIANT:
        return run_deepgemm(input, weight, weight_scale)

    condition = input.shape[0] < 32

    # PyTorch's torch.compile cannot handle input-dependent control flow in standard
    # Python conditionals. torch.cond() explicitly registers both code paths in the
    # computation graph, allowing torch.compile to capture both branches.
    # without torch.cond, the M < 32 condition won't be able to be captured by torch
    # compile
    return torch.cond(
        condition,
        run_flashinfer_deepgemm_swapAB,
        run_deepgemm,
        (input, weight, weight_scale),
    )
```