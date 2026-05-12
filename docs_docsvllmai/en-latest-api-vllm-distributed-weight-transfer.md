---
title: weight_transfer - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/weight_transfer/
source: sitemap
fetched_at: 2026-05-07T21:19:03.923230878-03:00
rendered_js: false
word_count: 258
summary: This document describes the WeightTransferEngineFactory, a registry-based component that enables lazy loading, registration, and instantiation of weight transfer engines for distributed inference.
tags:
    - weight-transfer
    - factory-pattern
    - distributed-computing
    - lazy-loading
    - model-inference
    - registry-pattern
category: reference
---

Weight transfer engines for syncing model weights from trainers to inference workers.

Modules:

Name Description `base`

Base class for weight transfer engines.

`factory`

Factory for weight transfer engines with lazy loading.

`ipc_engine`

IPC-based weight transfer engine using CUDA IPC for communication.

`nccl_engine`

NCCL-based weight transfer engine.

`packed_tensor`

Packed tensor utilities for efficient weight transfer.

## WeightTransferEngineFactory [¶](#vllm.distributed.weight_transfer.WeightTransferEngineFactory "Permanent link")

Factory for creating weight transfer engines with lazy loading.

This factory implements a registry pattern that supports: - Lazy loading: Engine modules are only imported when actually needed - Extensibility: Custom engines can be registered at runtime - Centralized registration: All built-in engines registered in one place

Source code in `vllm/distributed/weight_transfer/factory.py`

```
classWeightTransferEngineFactory:
"""Factory for creating weight transfer engines with lazy loading.

    This factory implements a registry pattern that supports:
    - Lazy loading: Engine modules are only imported when actually needed
    - Extensibility: Custom engines can be registered at runtime
    - Centralized registration: All built-in engines registered in one place
    """

    _registry: dict[str, Callable[[], type[WeightTransferEngine]]] = {}

    @classmethod
    defregister_engine(
        cls,
        name: str,
        module_path_or_cls: str | type[WeightTransferEngine],
        class_name: str | None = None,
    ) -> None:
"""Register an engine with lazy-loading or direct class reference.

        Supports two calling conventions:
        1. Lazy loading: register_engine(name, module_path, class_name)
        2. Direct class: register_engine(name, engine_cls)

        Args:
            name: The name to register the engine under (e.g., "nccl")
            module_path_or_cls: Either a module path string for lazy loading,
                or the engine class directly
            class_name: Name of the engine class (required if module_path is string)

        Raises:
            ValueError: If an engine with the same name is already registered
        """
        if name in cls._registry:
            raise ValueError(f"Weight transfer engine '{name}' is already registered.")

        if isinstance(module_path_or_cls, str):
            # Lazy loading path
            module_path = module_path_or_cls
            if class_name is None:
                raise ValueError(
                    "class_name is required when registering with module path"
                )

            defloader() -> type[WeightTransferEngine]:
                module = importlib.import_module(module_path)
                return getattr(module, class_name)

            cls._registry[name] = loader
        else:
            # Direct class registration
            engine_cls = module_path_or_cls
            cls._registry[name] = lambda: engine_cls

    @classmethod
    defcreate_engine(
        cls,
        config: "WeightTransferConfig",
        parallel_config: "ParallelConfig",
    ) -> WeightTransferEngine:
"""Create a weight transfer engine instance.

        Args:
            config: Weight transfer configuration containing the backend name
            parallel_config: Parallel configuration for the engine

        Returns:
            An initialized weight transfer engine instance

        Raises:
            ValueError: If the backend is not registered
        """
        backend = config.backend
        if backend not in cls._registry:
            available = list(cls._registry.keys())
            raise ValueError(
                f"Invalid weight transfer backend: {backend}. "
                f"Available engines: {available}"
            )
        engine_cls = cls._registry[backend]()

        logger.info(
            "Creating weight transfer engine: %s",
            engine_cls.__name__,
        )

        return engine_cls(config, parallel_config)
```

### create\_engine `classmethod` [¶](#vllm.distributed.weight_transfer.WeightTransferEngineFactory.create_engine "Permanent link")

Create a weight transfer engine instance.

Parameters:

Name Type Description Default `config` `WeightTransferConfig`

Weight transfer configuration containing the backend name

*required* `parallel_config` `ParallelConfig`

Parallel configuration for the engine

*required*

Returns:

Type Description `WeightTransferEngine`

An initialized weight transfer engine instance

Raises:

Type Description `ValueError`

If the backend is not registered

Source code in `vllm/distributed/weight_transfer/factory.py`

```
@classmethod
defcreate_engine(
    cls,
    config: "WeightTransferConfig",
    parallel_config: "ParallelConfig",
) -> WeightTransferEngine:
"""Create a weight transfer engine instance.

    Args:
        config: Weight transfer configuration containing the backend name
        parallel_config: Parallel configuration for the engine

    Returns:
        An initialized weight transfer engine instance

    Raises:
        ValueError: If the backend is not registered
    """
    backend = config.backend
    if backend not in cls._registry:
        available = list(cls._registry.keys())
        raise ValueError(
            f"Invalid weight transfer backend: {backend}. "
            f"Available engines: {available}"
        )
    engine_cls = cls._registry[backend]()

    logger.info(
        "Creating weight transfer engine: %s",
        engine_cls.__name__,
    )

    return engine_cls(config, parallel_config)
```

### register\_engine `classmethod` [¶](#vllm.distributed.weight_transfer.WeightTransferEngineFactory.register_engine "Permanent link")

Register an engine with lazy-loading or direct class reference.

Supports two calling conventions: 1. Lazy loading: register\_engine(name, module\_path, class\_name) 2. Direct class: register\_engine(name, engine\_cls)

Parameters:

Name Type Description Default `name` `str`

The name to register the engine under (e.g., "nccl")

*required* `module_path_or_cls` `str | type[WeightTransferEngine]`

Either a module path string for lazy loading, or the engine class directly

*required* `class_name` `str | None`

Name of the engine class (required if module\_path is string)

`None`

Raises:

Type Description `ValueError`

If an engine with the same name is already registered

Source code in `vllm/distributed/weight_transfer/factory.py`

```
@classmethod
defregister_engine(
    cls,
    name: str,
    module_path_or_cls: str | type[WeightTransferEngine],
    class_name: str | None = None,
) -> None:
"""Register an engine with lazy-loading or direct class reference.

    Supports two calling conventions:
    1. Lazy loading: register_engine(name, module_path, class_name)
    2. Direct class: register_engine(name, engine_cls)

    Args:
        name: The name to register the engine under (e.g., "nccl")
        module_path_or_cls: Either a module path string for lazy loading,
            or the engine class directly
        class_name: Name of the engine class (required if module_path is string)

    Raises:
        ValueError: If an engine with the same name is already registered
    """
    if name in cls._registry:
        raise ValueError(f"Weight transfer engine '{name}' is already registered.")

    if isinstance(module_path_or_cls, str):
        # Lazy loading path
        module_path = module_path_or_cls
        if class_name is None:
            raise ValueError(
                "class_name is required when registering with module path"
            )

        defloader() -> type[WeightTransferEngine]:
            module = importlib.import_module(module_path)
            return getattr(module, class_name)

        cls._registry[name] = loader
    else:
        # Direct class registration
        engine_cls = module_path_or_cls
        cls._registry[name] = lambda: engine_cls
```