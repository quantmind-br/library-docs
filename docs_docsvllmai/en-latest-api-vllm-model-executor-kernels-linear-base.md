---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/kernels/linear/base/
source: sitemap
fetched_at: 2026-05-07T21:23:16.267613395-03:00
rendered_js: false
word_count: 43
summary: This document defines the abstract base class for implementing custom quantized matrix multiplication kernels in vLLM, providing a structured lifecycle for hardware compatibility checks, weight preprocessing, and inference execution.
tags:
    - quantized-kernels
    - matrix-multiplication
    - vllm-framework
    - gpu-acceleration
    - inference-optimization
    - abstract-base-class
category: reference
---

````
classMMLinearKernel(ABC, Generic[_ConfigT, _ParamsT]):
"""Abstract base class for quantized matrix multiplication kernels.

    This class provides the interface for implementing custom quantized linear layer
    kernels in vLLM. Subclasses should implement specific quantization strategies
    (e.g., FP8, INT8) and their corresponding compute kernels.

    Generic Type Parameters:
        _ConfigT: Configuration type for the kernel (subclass of MMLinearLayerConfig).
                  Contains kernel-specific settings like quantization keys, dtypes, etc.
        _ParamsT: Parameter type for the kernel (subclass of Params).
                  Defines the quantized weights and scales needed by the kernel.

    Typical Usage:
        1. Define a config dataclass inheriting from MMLinearLayerConfig
        2. Define a params dataclass inheriting from Params (or FP8Params/Int8Params)
        3. Subclass MMLinearKernel with your config and params types
        4. Implement all abstract methods
        5. Register the kernel with the quantization method

    Example:
        ```python
        @dataclass
        class MyKernelConfig(MMLinearLayerConfig):
            static: bool
            output_dtype: torch.dtype


        @dataclass
        class MyKernelParams(FP8Params):
            custom_scale: torch.Tensor
            CUSTOM_SCALE: ClassVar[str] = "custom_scale"


        class MyKernel(MMLinearKernel[MyKernelConfig, MyKernelParams]):
            @classmethod
            def is_supported(cls, compute_capability=None):
                if compute_capability and compute_capability < 90:
                    return False, "Requires compute capability >= 9.0"
                return True, None

            @classmethod
            def can_implement(cls, config):
                if not config.static:
                    return False, "Only static quantization supported"
                return True, None

            def process_weights_after_loading(self, layer):
                # Preprocess weights for the kernel
                params = self._get_layer_params(layer)
                processed = preprocess_weights(params.weight)
                replace_parameter(layer, params.WEIGHT, processed)

            def _get_layer_params(self, layer, **kwargs):
                return MyKernelParams.from_layer(layer)

            def apply_weights(self, layer, x, bias=None, **kwargs):
                params = self._get_layer_params(layer)
                # Call your custom kernel
                output = my_custom_kernel(x, params.weight, params.weight_scale)
                if bias is not None:
                    output += bias
                return output
        ```

    Lifecycle:
        1. Kernel selection: is_supported() and can_implement() check compatibility
        2. Initialization: __init__() creates kernel instance with config
        3. Weight loading: process_weights_after_loading() preprocesses weights
        4. Inference: apply_weights() executes the quantized matmul
    """

    @classmethod
    @abstractmethod
    defis_supported(
        cls, compute_capability: int | None = None
    ) -> tuple[bool, str | None]:
"""Check if this kernel is supported on the current hardware.

        This method checks hardware-level compatibility (e.g., GPU architecture,
        compute capability, available instructions). It's called during kernel
        selection to filter out kernels that cannot run on the current device.

        Args:
            compute_capability: GPU compute capability (e.g., 80 for A100, 90 for H100).
                               If None, should check the current device.

        Returns:
            A tuple of (is_supported, reason):
                - is_supported: True if the kernel can run on this hardware
                - reason: If not supported, a string explaining why; otherwise None
        """
        raise NotImplementedError

    @classmethod
    @abstractmethod
    defcan_implement(cls, config: _ConfigT) -> tuple[bool, str | None]:
"""Check if this kernel can implement the given configuration.

        This method checks configuration-level compatibility (e.g., quantization
        scheme, group sizes, static vs dynamic quantization). It's called after
        is_supported() to determine if this kernel can handle the specific
        quantization configuration.

        Args:
            config: The kernel configuration to check

        Returns:
            A tuple of (can_implement, reason):
                - can_implement: True if this kernel supports the config
                - reason: If not supported, a string explaining why; otherwise None
            ```
        """
        raise NotImplementedError

    def__init__(self, config: _ConfigT) -> None:
"""Initialize the kernel with the given configuration.

        Args:
            config: Kernel-specific configuration containing settings like
                   quantization keys, output dtypes, etc.
        """
        self.config = config

    @abstractmethod
    defprocess_weights_after_loading(self, layer: torch.nn.Module) -> None:
"""Process and transform weights after loading from checkpoint.

        This method is called once after weights are loaded but before inference.
        Use it to preprocess weights into the format required by your kernel
        (e.g., reordering, padding, format conversion).

        Modifications should be done in-place using replace_parameter() to ensure
        the layer's parameters are properly updated.

        Args:
            layer: The layer module containing the weights to process

        Example:
            ```python
            def process_weights_after_loading(self, layer):
                params = self._get_layer_params(layer)
                # Reorder weights for better memory access
                weight_reordered = reorder_weights(params.weight)
                replace_parameter(layer, params.WEIGHT, weight_reordered)
            ```
        """
        raise NotImplementedError

    # return a covariant type in the subclass
    @abstractmethod
    def_get_layer_params(self, layer: torch.nn.Module, **kwargs: Any) -> _ParamsT:
"""Extract typed parameters from the layer module.

        This internal method retrieves the quantized weights and scales from
        the layer as a typed parameter object. Subclasses should typically
        delegate to ParamsClass.from_layer().

        Args:
            layer: The layer module containing the parameters
            **kwargs: Additional arguments

        Returns:
            A typed parameter object containing weights, scales, and other
            quantization parameters

        Example:
            ```python
            def _get_layer_params(self, layer, **kwargs):
                return MyKernelParams.from_layer(layer)
            ```
        """
        raise NotImplementedError

    defget_output_padding(self) -> int | None:
"""Get the number of output tokens to pad for this kernel.

        Some kernels require input padding for optimal performance.
        Override this method to specify padding requirements.

        Returns:
            Number of tokens to pad, or None for no padding (default)
        """
        return None

    @abstractmethod
    defapply_weights(
        self,
        layer: torch.nn.Module,
        x: torch.Tensor,
        bias: torch.Tensor | None = None,
        **kwargs: Any,
    ) -> torch.Tensor:
"""Apply the quantized weights to the input tensor.

        This is the main inference method that performs the quantized matrix
        multiplication. It should handle input quantization (if needed), call
        the underlying kernel, and apply bias.

        Args:
            layer: The layer module containing the quantized weights
            x: Input tensor of shape [..., in_features]
            bias: Optional bias tensor of shape [out_features]
            **kwargs: Additional kernel-specific arguments

        Returns:
            Output tensor of shape [..., out_features]
        """
        raise NotImplementedError
````