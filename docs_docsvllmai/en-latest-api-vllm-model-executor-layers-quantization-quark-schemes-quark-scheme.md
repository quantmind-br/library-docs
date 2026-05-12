---
title: quark_scheme - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/quark/schemes/quark_scheme/
source: sitemap
fetched_at: 2026-05-07T21:27:35.88461084-03:00
rendered_js: false
word_count: 122
summary: Defines the QuarkScheme abstract base class, which provides a standard interface for implementing custom quantization schemes including weight creation, forward pass execution, and post-loading cleanup.
tags:
    - quark
    - quantization
    - model-optimization
    - abstract-base-class
    - weight-management
    - inference
category: reference
---

Bases: `ABC`

Abstract class used to describe the weight creation and forward pass of different quantization schemes supported by Quark.

Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_scheme.py`

```
classQuarkScheme(ABC):
"""
    Abstract class used to describe the weight creation and forward pass
    of different quantization schemes supported by Quark.
    """

    @classmethod
    @abstractmethod
    defget_min_capability(cls) -> int:
"""
        Get minimum device capability.
        """
        raise NotImplementedError

    @abstractmethod
    defcreate_weights(self, *args, **kwargs):
"""
        Weight creation for the particular scheme. Inputs to this function

        """
        raise NotImplementedError

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
        raise NotImplementedError

    @abstractmethod
    defprocess_weights_after_loading(self, layer: torch.nn.Module):
"""
        Called after weight loading is complete for any cleanup that
        needs to occur.
        """
        raise NotImplementedError
```

### apply\_weights `abstractmethod` [¶](#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.apply_weights "Permanent link")

Run the forward pass for the particular scheme. This is where scheme-specific dequant/quant steps/kernels should be applied.

:param layer: torch.nn.Module with the registered weights and other parameters relevant to the particular scheme. :param x: input to the layer :param bias: bias parameter

Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_scheme.py`

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
    raise NotImplementedError
```

### create\_weights `abstractmethod` [¶](#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.create_weights "Permanent link")

```
create_weights(*args, **kwargs)
```

Weight creation for the particular scheme. Inputs to this function

Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_scheme.py`

```
@abstractmethod
defcreate_weights(self, *args, **kwargs):
"""
    Weight creation for the particular scheme. Inputs to this function

    """
    raise NotImplementedError
```

### get\_min\_capability `abstractmethod` `classmethod` [¶](#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.get_min_capability "Permanent link")

```
get_min_capability() -> int
```

Get minimum device capability.

Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_scheme.py`

```
@classmethod
@abstractmethod
defget_min_capability(cls) -> int:
"""
    Get minimum device capability.
    """
    raise NotImplementedError
```

### process\_weights\_after\_loading `abstractmethod` [¶](#vllm.model_executor.layers.quantization.quark.schemes.quark_scheme.QuarkScheme.process_weights_after_loading "Permanent link")

```
process_weights_after_loading(layer: Module)
```

Called after weight loading is complete for any cleanup that needs to occur.

Source code in `vllm/model_executor/layers/quantization/quark/schemes/quark_scheme.py`

```
@abstractmethod
defprocess_weights_after_loading(self, layer: torch.nn.Module):
"""
    Called after weight loading is complete for any cleanup that
    needs to occur.
    """
    raise NotImplementedError
```