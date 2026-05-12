---
title: deep_gemm_warmup - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/warmup/deep_gemm_warmup/
source: sitemap
fetched_at: 2026-05-07T21:33:58.920917716-03:00
rendered_js: false
word_count: 143
summary: This module provides utility functions for pre-compiling and warming up DeepGEMM JIT kernels used in FP8 linear layers to ensure optimal performance during model execution.
tags:
    - vllm
    - deep-gemm
    - warmup
    - jit-compilation
    - fp8-quantization
    - tensor-processing
category: reference
---

## vllm.model\_executor.warmup.deep\_gemm\_warmup [¶](#vllm.model_executor.warmup.deep_gemm_warmup "Permanent link")

Warmup deep\_gemm kernels. DeepGEMM JIT's the kernels. The warmup aims to JIT all the kernels that would be used during model execution beforehand.

Extract weights, weight scales and num\_topk from FusedMoE module.

Source code in `vllm/model_executor/warmup/deep_gemm_warmup.py`

```
def_extract_data_from_fused_moe_module(
    m: torch.nn.Module,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, int]:
"""
    Extract weights, weight scales and num_topk from FusedMoE module.
    """
    assert isinstance(m, FusedMoE)
    w13 = m.w13_weight
    w13_s = (
        m.w13_weight_scale_inv
        if hasattr(m, "w13_weight_scale_inv")
        else m.w13_weight_scale
    )
    w2 = m.w2_weight
    w2_s = (
        m.w2_weight_scale_inv
        if hasattr(m, "w2_weight_scale_inv")
        else m.w2_weight_scale
    )
    num_topk = m.top_k

    assert isinstance(w13, torch.Tensor)
    assert isinstance(w13_s, torch.Tensor)
    assert isinstance(w2, torch.Tensor)
    assert isinstance(w2_s, torch.Tensor)
    return w13, w13_s, w2, w2_s, num_topk
```

Extract weights, weight scales and quantization block sizes from the given LinearBase module.

Source code in `vllm/model_executor/warmup/deep_gemm_warmup.py`

```
def_extract_data_from_linear_base_module(
    m: torch.nn.Module,
) -> tuple[torch.Tensor, torch.Tensor, list[int]]:
"""
    Extract weights, weight scales and quantization block sizes from the given
    LinearBase module.
    """
    assert isinstance(m, LinearBase)
    assert isinstance(m.quant_method, Fp8LinearMethod)
    assert m.quant_method.block_quant
    assert m.quant_method.quant_config is not None

    w = m.weight
    ws = m.weight_scale_inv if hasattr(m, "weight_scale_inv") else m.weight_scale
    quant_block_size = m.quant_method.quant_config.weight_block_size

    assert isinstance(w, torch.Tensor)
    assert isinstance(ws, torch.Tensor)
    assert quant_block_size is not None
    return (w, ws, quant_block_size)
```

## \_fp8\_linear\_may\_use\_deep\_gemm [¶](#vllm.model_executor.warmup.deep_gemm_warmup._fp8_linear_may_use_deep_gemm "Permanent link")

```
_fp8_linear_may_use_deep_gemm(module: Module) -> bool
```

Return True if the input module/layer could be processed with DeepGEMM.

Source code in `vllm/model_executor/warmup/deep_gemm_warmup.py`

```
def_fp8_linear_may_use_deep_gemm(module: torch.nn.Module) -> bool:
"""
    Return True if the input module/layer could be processed with DeepGEMM.
    """

    # FIXME: this logic is brittle and incorrect - since we
    # could use DeepGEMM with for than just Fp8LinearMethod
    block_size = get_mk_alignment_for_contiguous_layout()[0]
    if not (
        isinstance(module, LinearBase)
        and isinstance(module.quant_method, Fp8LinearMethod)
        and not isinstance(module.quant_method, Mxfp8OnlineLinearMethod)
        and getattr(module.quant_method, "block_quant", False)
        and not getattr(module.quant_method, "use_marlin", True)
    ):
        return False

    w, _, block_sizes = _extract_data_from_linear_base_module(module)
    return (
        block_sizes == get_mk_alignment_for_contiguous_layout()
        and w.ndim == 2
        and w.shape[0] % block_size == 0
        and w.shape[1] % block_size == 0
    )
```

## \_generate\_optimal\_warmup\_m\_values [¶](#vllm.model_executor.warmup.deep_gemm_warmup._generate_optimal_warmup_m_values "Permanent link")

Generate M values that cover all possible DeepGEMM kernel configurations. Reference: https://github.com/deepseek-ai/DeepGEMM/blob/79f48ee15a82dd5fad5cd9beaa393c1f755e6b55/csrc/jit\_kernels/heuristics/common.hpp

Parameters:

Name Type Description Default `max_tokens` `int`

Maximum number of tokens to warmup for

*required* `n` `int`

The actual N dimension from the weight tensor

*required* `device` `device`

The torch device to get properties from.

*required*

Source code in `vllm/model_executor/warmup/deep_gemm_warmup.py`

```
def_generate_optimal_warmup_m_values(
    max_tokens: int, n: int, device: torch.device
) -> list[int]:
"""
    Generate M values that cover all possible DeepGEMM kernel configurations.
    Reference: https://github.com/deepseek-ai/DeepGEMM/blob/79f48ee15a82dd5fad5cd9beaa393c1f755e6b55/csrc/jit_kernels/heuristics/common.hpp

    Args:
        max_tokens: Maximum number of tokens to warmup for
        n: The actual N dimension from the weight tensor
        device: The torch device to get properties from.
    """

    # DeepGEMM's possible block sizes
    block_ms = [64, 128, 256]
    block_ns = list(range(16, min(257, n + 1), 16))
    num_sms = num_compute_units(device.index)

    m_values = set()

    # Always include small cases
    m_values.update([1, 2, 4] + [i for i in range(8, 65, 8)])

    # Collect M values where different wave patterns occur
    for block_m in block_ms:
        for block_n in block_ns:
            if block_n > n:
                continue

            # Add key M boundaries for this block combination
            for wave in range(1, 11):  # Up to 10 waves
                # M where this block config transitions to next wave
                target_blocks = wave * num_sms
                m = target_blocks * block_m // cdiv(n, block_n)
                if 1 <= m <= max_tokens:
                    m_values.add(m)

            # Add block_m boundaries
            for multiple in range(1, max_tokens // block_m + 1):
                m = multiple * block_m
                if m <= max_tokens:
                    m_values.add(m)

    return sorted(m_values)
```

## \_get\_fp8\_gemm\_nt\_m\_values [¶](#vllm.model_executor.warmup.deep_gemm_warmup._get_fp8_gemm_nt_m_values "Permanent link")

Get the M values to warmup for a given weight tensor.

Source code in `vllm/model_executor/warmup/deep_gemm_warmup.py`

```
def_get_fp8_gemm_nt_m_values(w: torch.Tensor, max_tokens: int) -> list[int]:
"""Get the M values to warmup for a given weight tensor."""
    n, _ = w.size()
    device = w.device

    # Use optimal M values only if VLLM_DEEP_GEMM_WARMUP is set to "relax".
    # Otherwise warmup all token sizes to avoid JIT compilation in hotpath
    if envs.VLLM_DEEP_GEMM_WARMUP == "relax":
        return _generate_optimal_warmup_m_values(max_tokens, n, device)
    else:
        assert envs.VLLM_DEEP_GEMM_WARMUP == "full", (
            "Expected "
            'VLLM_DEEP_GEMM_WARMUP env to be set to "full" but got '
            f"{envs.VLLM_DEEP_GEMM_WARMUP}"
        )
        return list(range(1, max_tokens + 1))
```