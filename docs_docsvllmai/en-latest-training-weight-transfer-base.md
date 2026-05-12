---
title: Base Class and Custom Engines
url: https://docs.vllm.ai/en/latest/training/weight_transfer/base/
source: sitemap
fetched_at: 2026-05-07T21:15:25.16081122-03:00
rendered_js: false
word_count: 290
summary: This document describes the vLLM weight transfer system, providing instructions on how to implement and register a custom backend engine using the WeightTransferEngine abstract base class.
tags:
    - vllm
    - distributed-training
    - weight-transfer
    - custom-engine
    - distributed-computing
    - machine-learning-infrastructure
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/training/weight_transfer/base.md "Edit this page")

The weight transfer system is built on an abstract base class that defines the contract between vLLM's worker infrastructure and the transport backend. You can implement custom backends by subclassing [`WeightTransferEngine`](https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine "            WeightTransferEngine") and registering them with the [`WeightTransferEngineFactory`](https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/factory/#vllm.distributed.weight_transfer.factory.WeightTransferEngineFactory "            WeightTransferEngineFactory").

## WeightTransferEngine[¶](#weighttransferengine "Permanent link")

The [`WeightTransferEngine`](https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightTransferEngine "            WeightTransferEngine") is a generic abstract class parameterized by two dataclass types:

- **`TInitInfo`** (extends [`WeightTransferInitInfo`](https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightTransferInitInfo "            WeightTransferInitInfo            dataclass   ")): Backend-specific initialization parameters.
- **`TUpdateInfo`** (extends [`WeightTransferUpdateInfo`](https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo "            WeightTransferUpdateInfo            dataclass   ")): Backend-specific weight update metadata.

### Abstract Methods[¶](#abstract-methods "Permanent link")

Subclasses must implement these four methods:

Method Side Description `init_transfer_engine(init_info)` Inference Initialize the communication channel on each inference worker `receive_weights(update_info, load_weights)` Inference Receive weights and call `load_weights` incrementally `shutdown()` Inference Clean up resources `trainer_send_weights(iterator, trainer_args)` Trainer Static method to send weights from the trainer process

### Request Classes[¶](#request-classes "Permanent link")

The API-level request classes provide backend-agnostic serialization using plain dictionaries. The engine's `parse_init_info` and `parse_update_info` methods convert these dictionaries into typed dataclasses.

```
fromvllm.distributed.weight_transfer.baseimport (
    WeightTransferInitRequest,
    WeightTransferUpdateRequest,
)

# Init request (dict is converted to backend-specific TInitInfo)
init_request = WeightTransferInitRequest(
    init_info={"master_address": "10.0.0.1", "master_port": 29500, ...}
)

# Update request (dict is converted to backend-specific TUpdateInfo)
update_request = WeightTransferUpdateRequest(
    update_info={"names": [...], "dtype_names": [...], "shapes": [...]}
)
```

### WeightTransferUpdateInfo[¶](#weighttransferupdateinfo "Permanent link")

The base [`WeightTransferUpdateInfo`](https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/base/#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo "            WeightTransferUpdateInfo            dataclass   ") includes an `is_checkpoint_format` flag:

```
@dataclass
classWeightTransferUpdateInfo(ABC):
    is_checkpoint_format: bool = True
```

When `is_checkpoint_format=True` (the default), vLLM applies layerwise weight processing (repacking, renaming, etc.) on the received weights before loading them. Set to `False` if the trainer has already converted weights to the kernel format expected by the model.

## Implementing a Custom Engine[¶](#implementing-a-custom-engine "Permanent link")

To create a custom weight transfer backend:

### 1. Define Info Dataclasses[¶](#1-define-info-dataclasses "Permanent link")

```
fromdataclassesimport dataclass
fromvllm.distributed.weight_transfer.baseimport (
    WeightTransferEngine,
    WeightTransferInitInfo,
    WeightTransferUpdateInfo,
)

@dataclass
classMyInitInfo(WeightTransferInitInfo):
    endpoint: str
    token: str

@dataclass
classMyUpdateInfo(WeightTransferUpdateInfo):
    names: list[str]
    dtype_names: list[str]
    shapes: list[list[int]]
    # Add custom fields as needed
```

### 2. Implement the Engine[¶](#2-implement-the-engine "Permanent link")

```
fromcollections.abcimport Callable, Iterator
fromtypingimport Any
importtorch

classMyWeightTransferEngine(WeightTransferEngine[MyInitInfo, MyUpdateInfo]):
    init_info_cls = MyInitInfo
    update_info_cls = MyUpdateInfo

    definit_transfer_engine(self, init_info: MyInitInfo) -> None:
        # Set up connection to trainer using init_info.endpoint, etc.
        ...

    defreceive_weights(
        self,
        update_info: MyUpdateInfo,
        load_weights: Callable[[list[tuple[str, torch.Tensor]]], None],
    ) -> None:
        # Receive each weight and call load_weights incrementally
        for name, dtype_name, shape in zip(
            update_info.names, update_info.dtype_names, update_info.shapes
        ):
            dtype = getattr(torch, dtype_name)
            weight = self._fetch_weight(name, shape, dtype)
            load_weights([(name, weight)])

    defshutdown(self) -> None:
        # Clean up resources
        ...

    @staticmethod
    deftrainer_send_weights(
        iterator: Iterator[tuple[str, torch.Tensor]],
        trainer_args: dict[str, Any],
    ) -> None:
        # Send weights from the trainer process
        for name, tensor in iterator:
            # Send tensor via custom transport
            ...
```

Important

The `load_weights` callable passed to `receive_weights` should be called **incrementally** (one or a few weights at a time) rather than accumulating all weights first. This avoids GPU out-of-memory errors with large models.

### 3. Register with the Factory[¶](#3-register-with-the-factory "Permanent link")

```
fromvllm.distributed.weight_transfer.factoryimport WeightTransferEngineFactory

# Option 1: Lazy loading (recommended for built-in engines)
WeightTransferEngineFactory.register_engine(
    "my_backend",
    "my_package.my_module",
    "MyWeightTransferEngine",
)

# Option 2: Direct class registration
WeightTransferEngineFactory.register_engine(
    "my_backend",
    MyWeightTransferEngine,
)
```

Once registered, users can select your backend via `WeightTransferConfig(backend="my_backend")`.

## WeightTransferEngineFactory[¶](#weighttransferenginefactory "Permanent link")

The factory uses a registry pattern with lazy loading. Built-in engines (`nccl` and `ipc`) are registered at import time but their modules are only loaded when the backend is actually requested. This avoids importing heavy dependencies (like NCCL communicators) when they aren't needed.

```
fromvllm.distributed.weight_transfer.factoryimport WeightTransferEngineFactory

# Create an engine from config
engine = WeightTransferEngineFactory.create_engine(
    config=weight_transfer_config,
    parallel_config=parallel_config,
)
```