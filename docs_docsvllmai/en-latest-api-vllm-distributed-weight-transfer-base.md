---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/base/
source: sitemap
fetched_at: 2026-05-07T21:19:04.973347242-03:00
rendered_js: false
word_count: 515
summary: This document defines the abstract base class for weight transfer engines, which provides a framework for transporting model weights between trainers and inference workers using pluggable backends.
tags:
    - distributed-computing
    - model-weights
    - abstract-base-class
    - weight-transfer
    - inference-worker
    - backend-architecture
category: reference
---

Base class for weight transfer engines.

## WeightTransferEngine [¶](#vllm.distributed.weight_transfer.base.WeightTransferEngine "Permanent link")

Bases: `ABC`, `Generic[TInitInfo, TUpdateInfo]`

Base class for weight transfer engines that handle transport of model weights from a trainer to inference workers.

This abstraction separates weight transfer transport logic from the worker implementation, allowing different backends (NCCL, CUDA IPC\[TODO], RDMA\[TODO]) to be plugged in.

Subclasses should define

init\_info\_cls: Type of backend-specific initialization info update\_info\_cls: Type of backend-specific update info

Source code in `vllm/distributed/weight_transfer/base.py`

```
classWeightTransferEngine(ABC, Generic[TInitInfo, TUpdateInfo]):
"""
    Base class for weight transfer engines that handle transport of model weights
    from a trainer to inference workers.

    This abstraction separates weight transfer transport logic from the worker
    implementation, allowing different backends (NCCL, CUDA IPC[TODO], RDMA[TODO]) to be
    plugged in.

    Subclasses should define:
        init_info_cls: Type of backend-specific initialization info
        update_info_cls: Type of backend-specific update info
    """

    # Subclasses should override these class attributes
    init_info_cls: type[TInitInfo]
    update_info_cls: type[TUpdateInfo]

    def__init__(
        self, config: WeightTransferConfig, parallel_config: ParallelConfig
    ) -> None:
"""
        Initialize the weight transfer engine.

        Args:
            config: The configuration for the weight transfer engine
            parallel_config: The configuration for the parallel setup
        """
        self.config = config
        self.parallel_config = parallel_config

    defparse_init_info(self, init_dict: dict[str, Any]) -> TInitInfo:
"""
        Construct typed init info from dict with validation.

        Args:
            init_dict: Dictionary containing backend-specific initialization parameters

        Returns:
            Typed backend-specific init info dataclass

        Raises:
            ValueError: If init_dict is invalid for this backend
        """
        try:
            return self.init_info_cls(**init_dict)
        except TypeError as e:
            raise ValueError(
                f"Invalid init_info for {self.__class__.__name__}: {e}"
            ) frome

    defparse_update_info(self, update_dict: dict[str, Any]) -> TUpdateInfo:
"""
        Construct typed update info from dict with validation.

        Args:
            update_dict: Dictionary containing backend-specific update parameters

        Returns:
            Typed backend-specific update info dataclass

        Raises:
            ValueError: If update_dict is invalid for this backend
        """
        try:
            return self.update_info_cls(**update_dict)
        except TypeError as e:
            raise ValueError(
                f"Invalid update_info for {self.__class__.__name__}: {e}"
            ) frome

    @abstractmethod
    definit_transfer_engine(self, init_info: TInitInfo) -> None:
"""
        Initialize the weight transfer mechanism.
        This is called once at the beginning of training.

        Args:
            init_info: Backend-specific initialization info
        """
        raise NotImplementedError

    @abstractmethod
    defreceive_weights(
        self,
        update_info: TUpdateInfo,
        load_weights: Callable[[list[tuple[str, torch.Tensor]]], None],
    ) -> None:
"""
        Receive weights from the trainer and load them incrementally.

        Args:
            update_info: Backend-specific update info containing parameter metadata
                        and any backend-specific data
            load_weights: Callable that loads weights into the model. Called
                         incrementally for each weight to avoid OOM.
        """
        raise NotImplementedError

    @abstractmethod
    defshutdown(self) -> None:
"""
        Shutdown the weight transfer engine.
        This should be called when the worker is shutting down.
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    deftrainer_send_weights(
        iterator: Iterator[tuple[str, torch.Tensor]],
        trainer_args: dict[str, Any] | Any,
    ) -> None:
"""
        Send weights from trainer to inference workers.

        This is a static method that can be called from the trainer process
        to send weights to all inference workers.

        Args:
            iterator: Iterator of model parameters. Returns (name, tensor) tuples.
                     The tensors should be on the appropriate device for the backend.
            trainer_args: Dictionary containing backend-specific arguments needed
                         to send weights. The structure depends on the backend:
                         - NCCL: Contains 'group', 'src', 'packed', etc.
                         - IPC: Contains 'mode' ('http' or 'ray'),
                                'llm_handle' (for Ray), 'url' (for HTTP), etc.

        Example:
            >>> param_iter = ((n, p) for n, p in model.named_parameters())
            >>> engine.trainer_send_weights(param_iter, trainer_args)
        """
        raise NotImplementedError
```

### \_\_init\__ [¶](#vllm.distributed.weight_transfer.base.WeightTransferEngine.__init__ "Permanent link")

Initialize the weight transfer engine.

Parameters:

Name Type Description Default `config` `WeightTransferConfig`

The configuration for the weight transfer engine

*required* `parallel_config` `ParallelConfig`

The configuration for the parallel setup

*required*

Source code in `vllm/distributed/weight_transfer/base.py`

```
def__init__(
    self, config: WeightTransferConfig, parallel_config: ParallelConfig
) -> None:
"""
    Initialize the weight transfer engine.

    Args:
        config: The configuration for the weight transfer engine
        parallel_config: The configuration for the parallel setup
    """
    self.config = config
    self.parallel_config = parallel_config
```

### init\_transfer\_engine `abstractmethod` [¶](#vllm.distributed.weight_transfer.base.WeightTransferEngine.init_transfer_engine "Permanent link")

```
init_transfer_engine(init_info: TInitInfo) -> None
```

Initialize the weight transfer mechanism. This is called once at the beginning of training.

Parameters:

Name Type Description Default `init_info` `TInitInfo`

Backend-specific initialization info

*required*

Source code in `vllm/distributed/weight_transfer/base.py`

```
@abstractmethod
definit_transfer_engine(self, init_info: TInitInfo) -> None:
"""
    Initialize the weight transfer mechanism.
    This is called once at the beginning of training.

    Args:
        init_info: Backend-specific initialization info
    """
    raise NotImplementedError
```

### parse\_init\_info [¶](#vllm.distributed.weight_transfer.base.WeightTransferEngine.parse_init_info "Permanent link")

```
parse_init_info(init_dict: dict[str, Any]) -> TInitInfo
```

Construct typed init info from dict with validation.

Parameters:

Name Type Description Default `init_dict` `dict[str, Any]`

Dictionary containing backend-specific initialization parameters

*required*

Returns:

Type Description `TInitInfo`

Typed backend-specific init info dataclass

Raises:

Type Description `ValueError`

If init\_dict is invalid for this backend

Source code in `vllm/distributed/weight_transfer/base.py`

```
defparse_init_info(self, init_dict: dict[str, Any]) -> TInitInfo:
"""
    Construct typed init info from dict with validation.

    Args:
        init_dict: Dictionary containing backend-specific initialization parameters

    Returns:
        Typed backend-specific init info dataclass

    Raises:
        ValueError: If init_dict is invalid for this backend
    """
    try:
        return self.init_info_cls(**init_dict)
    except TypeError as e:
        raise ValueError(
            f"Invalid init_info for {self.__class__.__name__}: {e}"
        ) frome
```

### parse\_update\_info [¶](#vllm.distributed.weight_transfer.base.WeightTransferEngine.parse_update_info "Permanent link")

```
parse_update_info(
    update_dict: dict[str, Any],
) -> TUpdateInfo
```

Construct typed update info from dict with validation.

Parameters:

Name Type Description Default `update_dict` `dict[str, Any]`

Dictionary containing backend-specific update parameters

*required*

Returns:

Type Description `TUpdateInfo`

Typed backend-specific update info dataclass

Raises:

Type Description `ValueError`

If update\_dict is invalid for this backend

Source code in `vllm/distributed/weight_transfer/base.py`

```
defparse_update_info(self, update_dict: dict[str, Any]) -> TUpdateInfo:
"""
    Construct typed update info from dict with validation.

    Args:
        update_dict: Dictionary containing backend-specific update parameters

    Returns:
        Typed backend-specific update info dataclass

    Raises:
        ValueError: If update_dict is invalid for this backend
    """
    try:
        return self.update_info_cls(**update_dict)
    except TypeError as e:
        raise ValueError(
            f"Invalid update_info for {self.__class__.__name__}: {e}"
        ) frome
```

### receive\_weights `abstractmethod` [¶](#vllm.distributed.weight_transfer.base.WeightTransferEngine.receive_weights "Permanent link")

Receive weights from the trainer and load them incrementally.

Parameters:

Name Type Description Default `update_info` `TUpdateInfo`

Backend-specific update info containing parameter metadata and any backend-specific data

*required* `load_weights` `Callable[[list[tuple[str, Tensor]]], None]`

Callable that loads weights into the model. Called incrementally for each weight to avoid OOM.

*required*

Source code in `vllm/distributed/weight_transfer/base.py`

```
@abstractmethod
defreceive_weights(
    self,
    update_info: TUpdateInfo,
    load_weights: Callable[[list[tuple[str, torch.Tensor]]], None],
) -> None:
"""
    Receive weights from the trainer and load them incrementally.

    Args:
        update_info: Backend-specific update info containing parameter metadata
                    and any backend-specific data
        load_weights: Callable that loads weights into the model. Called
                     incrementally for each weight to avoid OOM.
    """
    raise NotImplementedError
```

### shutdown `abstractmethod` [¶](#vllm.distributed.weight_transfer.base.WeightTransferEngine.shutdown "Permanent link")

Shutdown the weight transfer engine. This should be called when the worker is shutting down.

Source code in `vllm/distributed/weight_transfer/base.py`

```
@abstractmethod
defshutdown(self) -> None:
"""
    Shutdown the weight transfer engine.
    This should be called when the worker is shutting down.
    """
    raise NotImplementedError
```

### trainer\_send\_weights `abstractmethod` `staticmethod` [¶](#vllm.distributed.weight_transfer.base.WeightTransferEngine.trainer_send_weights "Permanent link")

Send weights from trainer to inference workers.

This is a static method that can be called from the trainer process to send weights to all inference workers.

Parameters:

Name Type Description Default `iterator` `Iterator[tuple[str, Tensor]]`

Iterator of model parameters. Returns (name, tensor) tuples. The tensors should be on the appropriate device for the backend.

*required* `trainer_args` `dict[str, Any] | Any`

Dictionary containing backend-specific arguments needed to send weights. The structure depends on the backend: - NCCL: Contains 'group', 'src', 'packed', etc. - IPC: Contains 'mode' ('http' or 'ray'), 'llm\_handle' (for Ray), 'url' (for HTTP), etc.

*required*

Example

> > > param\_iter = ((n, p) for n, p in model.named\_parameters()) engine.trainer\_send\_weights(param\_iter, trainer\_args)

Source code in `vllm/distributed/weight_transfer/base.py`

```
@staticmethod
@abstractmethod
deftrainer_send_weights(
    iterator: Iterator[tuple[str, torch.Tensor]],
    trainer_args: dict[str, Any] | Any,
) -> None:
"""
    Send weights from trainer to inference workers.

    This is a static method that can be called from the trainer process
    to send weights to all inference workers.

    Args:
        iterator: Iterator of model parameters. Returns (name, tensor) tuples.
                 The tensors should be on the appropriate device for the backend.
        trainer_args: Dictionary containing backend-specific arguments needed
                     to send weights. The structure depends on the backend:
                     - NCCL: Contains 'group', 'src', 'packed', etc.
                     - IPC: Contains 'mode' ('http' or 'ray'),
                            'llm_handle' (for Ray), 'url' (for HTTP), etc.

    Example:
        >>> param_iter = ((n, p) for n, p in model.named_parameters())
        >>> engine.trainer_send_weights(param_iter, trainer_args)
    """
    raise NotImplementedError
```

## WeightTransferInitInfo `dataclass` [¶](#vllm.distributed.weight_transfer.base.WeightTransferInitInfo "Permanent link")

Bases: `ABC`

Base class for backend-specific initialization info.

Source code in `vllm/distributed/weight_transfer/base.py`

```
@dataclass
classWeightTransferInitInfo(ABC):  # noqa: B024
"""Base class for backend-specific initialization info."""

    pass
```

## WeightTransferInitRequest `dataclass` [¶](#vllm.distributed.weight_transfer.base.WeightTransferInitRequest "Permanent link")

API-level weight transfer initialization request.

Source code in `vllm/distributed/weight_transfer/base.py`

```
@dataclass
classWeightTransferInitRequest:
"""API-level weight transfer initialization request."""

    init_info: dict[str, Any] = field(default_factory=dict)
```

## WeightTransferUpdateInfo `dataclass` [¶](#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo "Permanent link")

Bases: `ABC`

Base class for backend-specific weight update info.

Source code in `vllm/distributed/weight_transfer/base.py`

```
@dataclass
classWeightTransferUpdateInfo(ABC):  # noqa: B024
"""Base class for backend-specific weight update info."""

    _: KW_ONLY
    is_checkpoint_format: bool = True
"""Set to True if weights are in checkpoint/original model format and need
    layerwise processing. Set to False if weights have already been processed
    into kernel format (repacking, renaming, etc.)."""
```

### is\_checkpoint\_format `class-attribute` `instance-attribute` [¶](#vllm.distributed.weight_transfer.base.WeightTransferUpdateInfo.is_checkpoint_format "Permanent link")

```
is_checkpoint_format: bool = True
```

Set to True if weights are in checkpoint/original model format and need layerwise processing. Set to False if weights have already been processed into kernel format (repacking, renaming, etc.).

## WeightTransferUpdateRequest `dataclass` [¶](#vllm.distributed.weight_transfer.base.WeightTransferUpdateRequest "Permanent link")

API-level weight update request.

Source code in `vllm/distributed/weight_transfer/base.py`

```
@dataclass
classWeightTransferUpdateRequest:
"""API-level weight update request."""

    update_info: dict[str, Any] = field(default_factory=dict)
```