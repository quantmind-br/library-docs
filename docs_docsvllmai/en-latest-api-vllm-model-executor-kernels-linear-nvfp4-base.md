---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/nvfp4/base/
source: sitemap
fetched_at: 2026-05-07T21:23:36.031840682-03:00
rendered_js: false
word_count: 216
summary: This document defines the base class and configuration structure for NVFP4 quantized linear kernels, establishing an interface for implementing and selecting GEMM backends in hardware-accelerated environments.
tags:
    - nvfp4
    - quantization
    - linear-kernels
    - gemm
    - model-execution
    - hardware-acceleration
    - abstract-base-class
category: reference
---

## NvFp4LinearKernel [¶](#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel "Permanent link")

Bases: `ABC`

Base class for NVFP4 quantized linear kernels.

Each subclass implements a specific GEMM backend (CUTLASS, Marlin, etc). The kernel selection mechanism iterates over registered subclasses in priority order,calling `is_supported` and `can_implement` to find the best match for the current hardware.

Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`

```
classNvFp4LinearKernel(ABC):
"""Base class for NVFP4 quantized linear kernels.

    Each subclass implements a specific GEMM backend (CUTLASS, Marlin, etc).
    The kernel selection mechanism iterates over registered subclasses in
    priority order,calling ``is_supported`` and ``can_implement`` to find the best
    match for the current hardware.
    """

    def__init__(self, config: NvFp4LinearLayerConfig) -> None:
        assert self.can_implement(config)[0]
        assert self.is_supported()[0]
        self.config = config

    @classmethod
    @abstractmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
"""Return whether this kernel can run on the current platform."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    defcan_implement(cls, config: NvFp4LinearLayerConfig) -> tuple[bool, str | None]:
"""Return whether this kernel can handle *config*."""
        raise NotImplementedError

    @abstractmethod
    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
"""Transform weights into the format required by this kernel.

        Called once after checkpoint weights have been loaded onto the
        device.  Implementations should repack / swizzle / pad weights
        and scales in-place on *layer*.
        """
        raise NotImplementedError

    @abstractmethod
    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
    ) -> torch.Tensor:
"""Run the quantized GEMM."""
        raise NotImplementedError
```

### apply\_weights `abstractmethod` [¶](#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.apply_weights "Permanent link")

Run the quantized GEMM.

Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`

```
@abstractmethod
defapply_weights(
    self,
    layer: torch.nn.Module,
    x: torch.Tensor,
    bias: torch.Tensor | None = None,
) -> torch.Tensor:
"""Run the quantized GEMM."""
    raise NotImplementedError
```

### can\_implement `abstractmethod` `classmethod` [¶](#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.can_implement "Permanent link")

Return whether this kernel can handle *config*.

Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`

```
@classmethod
@abstractmethod
defcan_implement(cls, config: NvFp4LinearLayerConfig) -> tuple[bool, str | None]:
"""Return whether this kernel can handle *config*."""
    raise NotImplementedError
```

### is\_supported `abstractmethod` `classmethod` [¶](#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.is_supported "Permanent link")

```
is_supported(
    compute_capability: int | None = None,
) -> tuple[bool, str | None]
```

Return whether this kernel can run on the current platform.

Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`

```
@classmethod
@abstractmethod
defis_supported(
    cls, compute_capability: int | None = None
) -> tuple[bool, str | None]:
"""Return whether this kernel can run on the current platform."""
    raise NotImplementedError
```

### process\_weights\_after\_loading `abstractmethod` [¶](#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearKernel.process_weights_after_loading "Permanent link")

```
process_weights_after_loading(layer: Module) -> None
```

Transform weights into the format required by this kernel.

Called once after checkpoint weights have been loaded onto the device. Implementations should repack / swizzle / pad weights and scales in-place on *layer*.

Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`

```
@abstractmethod
defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
"""Transform weights into the format required by this kernel.

    Called once after checkpoint weights have been loaded onto the
    device.  Implementations should repack / swizzle / pad weights
    and scales in-place on *layer*.
    """
    raise NotImplementedError
```

## NvFp4LinearLayerConfig `dataclass` [¶](#vllm.model_executor.kernels.linear.nvfp4.base.NvFp4LinearLayerConfig "Permanent link")

Configuration for an NVFP4 linear layer.

All NVFP4 layers share the same structure: packed uint8 weights (2 FP4 values per byte), FP8-E4M3 per-block weight scales (group size 16), and scalar global scales for both weights and activations.

Source code in `vllm/model_executor/kernels/linear/nvfp4/base.py`

```
@dataclass
classNvFp4LinearLayerConfig:
"""Configuration for an NVFP4 linear layer.

    All NVFP4 layers share the same structure: packed uint8 weights (2 FP4 values per
    byte), FP8-E4M3 per-block weight scales (group size 16), and scalar global
    scales for both weights and activations.
    """

    pass
```