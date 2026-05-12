---
title: Mxfp8LinearKernel - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel/
source: sitemap
fetched_at: 2026-05-07T21:23:28.903433903-03:00
rendered_js: false
word_count: 24
summary: This document defines the abstract base class for MXFP8 quantized linear kernels, outlining the required interface for various GEMM backend implementations within the vLLM executor.
tags:
    - mxfp8
    - linear-kernel
    - gemm-backend
    - quantization
    - abstract-base-class
    - model-executor
category: reference
---

Bases: `ABC`

Base class for MXFP8 quantized linear kernels.

Each subclass implements a specific GEMM backend (FlashInfer CUTLASS, Marlin, emulation).

Source code in `vllm/model_executor/kernels/linear/mxfp8/Mxfp8LinearKernel.py`

```
classMxfp8LinearKernel(ABC):
"""Base class for MXFP8 quantized linear kernels.

    Each subclass implements a specific GEMM backend (FlashInfer CUTLASS,
    Marlin, emulation).
    """

    def__init__(self, c: Mxfp8LinearLayerConfig) -> None:
        assert self.can_implement(c)[0]
        assert self.is_supported()[0]
        self.config = c

    @classmethod
    @abstractmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    defcan_implement(cls, c: Mxfp8LinearLayerConfig) -> tuple[bool, str | None]:
        raise NotImplementedError

    @abstractmethod
    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
        raise NotImplementedError

    @abstractmethod
    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
        raise NotImplementedError
```