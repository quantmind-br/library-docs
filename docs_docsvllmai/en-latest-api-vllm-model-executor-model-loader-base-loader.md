---
title: base_loader - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/base_loader/
source: sitemap
fetched_at: 2026-05-07T21:28:35.918482291-03:00
rendered_js: false
word_count: 77
summary: This document defines the BaseModelLoader abstract base class in vLLM, which provides a framework for downloading models and loading their weights into memory.
tags:
    - vllm
    - model-loading
    - python-abc
    - weight-initialization
    - model-executor
    - machine-learning
category: reference
---

## BaseModelLoader [¶](#vllm.model_executor.model_loader.base_loader.BaseModelLoader "Permanent link")

Bases: `ABC`

Base class for model loaders.

Source code in `vllm/model_executor/model_loader/base_loader.py`

```
classBaseModelLoader(ABC):
"""Base class for model loaders."""

    def__init__(self, load_config: LoadConfig):
        self.load_config = load_config

    @abstractmethod
    defdownload_model(self, model_config: ModelConfig) -> None:
"""Download a model so that it can be immediately loaded."""
        raise NotImplementedError

    @abstractmethod
    defload_weights(self, model: nn.Module, model_config: ModelConfig) -> None:
"""Load weights into a model. This standalone API allows
        inplace weights loading for an already-initialized model"""
        raise NotImplementedError

    @instrument(span_name="Load model")
    defload_model(
        self, vllm_config: VllmConfig, model_config: ModelConfig, prefix: str = ""
    ) -> nn.Module:
"""Load a model with the given configurations."""
        device_config = vllm_config.device_config
        load_config = vllm_config.load_config
        load_device = (
            device_config.device if load_config.device is None else load_config.device
        )
        target_device = torch.device(load_device)
        with set_default_torch_dtype(model_config.dtype):
            with target_device:
                model = initialize_model(
                    vllm_config=vllm_config,
                    model_config=model_config,
                    prefix=prefix,
                )

            log_model_inspection(model)

            logger.debug("Loading weights on %s ...", load_device)
            self.load_weights(model, model_config)

            # Log peak GPU memory after loading weights. This is needed
            # to have test coverage on peak memory for online quantization.
            if current_platform.is_cuda_alike():
                peak_memory = torch.accelerator.max_memory_allocated()
                logger.debug_once(
                    "Peak GPU memory after loading weights: %s GiB",
                    format_gib(peak_memory),
                )

            # Process weights into kernel format. Note that when using online
            # quantization, weights are (typically) quantized as they are loaded.
            if _has_online_quant(model):
                finalize_layerwise_processing(model, model_config)

            process_weights_after_loading(model, model_config, target_device)

        return model.eval()
```

### download\_model `abstractmethod` [¶](#vllm.model_executor.model_loader.base_loader.BaseModelLoader.download_model "Permanent link")

Download a model so that it can be immediately loaded.

Source code in `vllm/model_executor/model_loader/base_loader.py`

```
@abstractmethod
defdownload_model(self, model_config: ModelConfig) -> None:
"""Download a model so that it can be immediately loaded."""
    raise NotImplementedError
```

### load\_model [¶](#vllm.model_executor.model_loader.base_loader.BaseModelLoader.load_model "Permanent link")

Load a model with the given configurations.

Source code in `vllm/model_executor/model_loader/base_loader.py`

```
@instrument(span_name="Load model")
defload_model(
    self, vllm_config: VllmConfig, model_config: ModelConfig, prefix: str = ""
) -> nn.Module:
"""Load a model with the given configurations."""
    device_config = vllm_config.device_config
    load_config = vllm_config.load_config
    load_device = (
        device_config.device if load_config.device is None else load_config.device
    )
    target_device = torch.device(load_device)
    with set_default_torch_dtype(model_config.dtype):
        with target_device:
            model = initialize_model(
                vllm_config=vllm_config,
                model_config=model_config,
                prefix=prefix,
            )

        log_model_inspection(model)

        logger.debug("Loading weights on %s ...", load_device)
        self.load_weights(model, model_config)

        # Log peak GPU memory after loading weights. This is needed
        # to have test coverage on peak memory for online quantization.
        if current_platform.is_cuda_alike():
            peak_memory = torch.accelerator.max_memory_allocated()
            logger.debug_once(
                "Peak GPU memory after loading weights: %s GiB",
                format_gib(peak_memory),
            )

        # Process weights into kernel format. Note that when using online
        # quantization, weights are (typically) quantized as they are loaded.
        if _has_online_quant(model):
            finalize_layerwise_processing(model, model_config)

        process_weights_after_loading(model, model_config, target_device)

    return model.eval()
```

### load\_weights `abstractmethod` [¶](#vllm.model_executor.model_loader.base_loader.BaseModelLoader.load_weights "Permanent link")

Load weights into a model. This standalone API allows inplace weights loading for an already-initialized model

Source code in `vllm/model_executor/model_loader/base_loader.py`

```
@abstractmethod
defload_weights(self, model: nn.Module, model_config: ModelConfig) -> None:
"""Load weights into a model. This standalone API allows
    inplace weights loading for an already-initialized model"""
    raise NotImplementedError
```

## log\_model\_inspection [¶](#vllm.model_executor.model_loader.base_loader.log_model_inspection "Permanent link")

```
log_model_inspection(model: Module) -> None
```

Log model structure if VLLM\_LOG\_MODEL\_INSPECTION=1.

Source code in `vllm/model_executor/model_loader/base_loader.py`

```
deflog_model_inspection(model: nn.Module) -> None:
"""Log model structure if VLLM_LOG_MODEL_INSPECTION=1."""
    if not envs.VLLM_LOG_MODEL_INSPECTION:
        return

    fromvllm.model_inspectionimport format_model_inspection

    logger.info("vLLM model structure:\n%s", format_model_inspection(model))
```