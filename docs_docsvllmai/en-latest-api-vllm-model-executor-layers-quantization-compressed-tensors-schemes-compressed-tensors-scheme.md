---
title: compressed_tensors_scheme - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme/
source: sitemap
fetched_at: 2026-05-07T21:26:53.10717915-03:00
rendered_js: false
word_count: 109
summary: This document defines the CompressedTensorsScheme abstract base class, which provides a framework for implementing custom quantization schemes including weight creation, forward pass execution, and post-loading cleanup.
tags:
    - quantization
    - compressed-tensors
    - abstract-base-class
    - weight-management
    - model-execution
category: reference
---

Bases: `ABC`

Abstract class used to describe the weight creation and forward pass of different quantization schemes supported by CompressedTensors.

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`

```
classCompressedTensorsScheme(ABC):
"""
    Abstract class used to describe the weight creation and forward pass
    of different quantization schemes supported by CompressedTensors.
    """

    @classmethod
    @abstractmethod
    defget_min_capability(cls) -> int:
"""
        Get minimum device capability.
        """
        raise NotImplementedError()

    @abstractmethod
    defcreate_weights(self, *args, **kwargs):
"""
        Weight creation for the particular scheme. Inputs to this function

        """
        raise NotImplementedError()

    @abstractmethod
    defapply_weights(
        self, layer: torch.nn.Module, x: torch.Tensor, bias: torch.Tensor | None
    ):
"""
        Run the forward pass for the particular scheme. This is where
        scheme-specific dequant/quant steps/kernels should be applied.

        :param layer: torch.nn.Module with the registered weights and
            other parameters relevant to the particular scheme.
        :param x: input to the layer
        :param bias: bias parameter

        """
        raise NotImplementedError()

    @abstractmethod
    defprocess_weights_after_loading(self, layer: torch.nn.Module):
"""
        Called after weight loading is complete for any cleanup that
        needs to occur.
        """
        raise NotImplementedError()
```

Run the forward pass for the particular scheme. This is where scheme-specific dequant/quant steps/kernels should be applied.

:param layer: torch.nn.Module with the registered weights and other parameters relevant to the particular scheme. :param x: input to the layer :param bias: bias parameter

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`

```
@abstractmethod
defapply_weights(
    self, layer: torch.nn.Module, x: torch.Tensor, bias: torch.Tensor | None
):
"""
    Run the forward pass for the particular scheme. This is where
    scheme-specific dequant/quant steps/kernels should be applied.

    :param layer: torch.nn.Module with the registered weights and
        other parameters relevant to the particular scheme.
    :param x: input to the layer
    :param bias: bias parameter

    """
    raise NotImplementedError()

create_weights(*args, **kwargs)
```

Weight creation for the particular scheme. Inputs to this function

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`

```
@abstractmethod
defcreate_weights(self, *args, **kwargs):
"""
    Weight creation for the particular scheme. Inputs to this function

    """
    raise NotImplementedError()

get_min_capability() -> int
```

Get minimum device capability.

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`

```
@classmethod
@abstractmethod
defget_min_capability(cls) -> int:
"""
    Get minimum device capability.
    """
    raise NotImplementedError()

process_weights_after_loading(layer: Module)
```

Called after weight loading is complete for any cleanup that needs to occur.

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/schemes/compressed_tensors_scheme.py`

```
@abstractmethod
defprocess_weights_after_loading(self, layer: torch.nn.Module):
"""
    Called after weight loading is complete for any cleanup that
    needs to occur.
    """
    raise NotImplementedError()
```