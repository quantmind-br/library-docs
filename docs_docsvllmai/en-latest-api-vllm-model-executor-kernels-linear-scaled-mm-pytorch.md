---
title: pytorch - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/scaled_mm/pytorch/
source: sitemap
fetched_at: 2026-05-07T21:23:50.973307279-03:00
rendered_js: false
word_count: 27
summary: Defines the base class for PyTorch-based FP8 scaled matrix multiplication kernels, including logic for hardware support validation and output padding configuration.
tags:
    - fp8
    - linear-kernels
    - torch-scaled-mm
    - gpu-acceleration
    - matrix-multiplication
category: reference
---

Bases: `FP8ScaledMMLinearKernel`

Base class for FP8 linear kernels using Torch. Each subclass represents a kernel variant for specific device capabilities and torch versions.

Source code in `vllm/model_executor/kernels/linear/scaled_mm/pytorch.py`

```
classTorchFP8ScaledMMLinearKernel(FP8ScaledMMLinearKernel):
"""
    Base class for FP8 linear kernels using Torch.
    Each subclass represents a kernel variant for
    specific device capabilities and torch versions.
    """

    @classmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        if not (current_platform.is_cuda_alike() or current_platform.is_cpu()):
            return False, "requires ROCm, CUDA or CPU."

        if compute_capability is not None and compute_capability < 89:
            return False, "requires compute capability 89 and above."

        return True, None

    defget_output_padding(self) -> int | None:
        # Note: we pad the input because torch._scaled_mm is more performant
        # for matrices with batch dimension > 16.
        # This could change in the future.
        # We also don't pad when using torch.compile,
        # as it breaks with dynamic shapes.
        #
        # The perf gain is still relevant as of 16/1/2026
        # torch version == 2.9.0. More details in the link below:
        # https://github.com/vllm-project/vllm/issues/32269
        vllm_config = get_current_vllm_config().compilation_config
        pad_output = vllm_config.mode < CompilationMode.VLLM_COMPILE
        return 17 if pad_output else None
```