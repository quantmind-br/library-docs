---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/offloader/base/
source: sitemap
fetched_at: 2026-05-07T21:33:52.225833841-03:00
rendered_js: false
word_count: 302
summary: This document defines the base architecture and factory methods for model parameter offloading strategies, enabling efficient management of memory and compute resources during inference.
tags:
    - model-offloading
    - inference-optimization
    - vllm
    - memory-management
    - parameter-storage
category: reference
---

Base classes for model parameter offloading.

## BaseOffloader [¶](#vllm.model_executor.offloader.base.BaseOffloader "Permanent link")

Bases: `ABC`

Base class for model parameter offloading strategies.

Offloaders control how model parameters are stored and loaded during inference. Different strategies trade memory for compute/transfer time.

Source code in `vllm/model_executor/offloader/base.py`

```
classBaseOffloader(ABC):
"""Base class for model parameter offloading strategies.

    Offloaders control how model parameters are stored and loaded during
    inference. Different strategies trade memory for compute/transfer time.
    """

    @abstractmethod
    defwrap_modules(
        self,
        modules_generator: Generator[nn.Module, None, None],
    ) -> list[nn.Module]:
"""Wrap modules with offloading logic.

        Args:
            modules_generator: Generator yielding modules to potentially offload.

        Returns:
            List of modules, potentially with offloading hooks installed.
        """
        pass

    defpost_init(self):
"""Called after model construction completes.

        Offloaders can use this to:
        - Finalize parameter storage
        - Start initial prefetching
        - Allocate shared resources
        """
        return

    defsync_prev_onload(self) -> None:  # noqa: B027
"""Sync previous onload operations. Override in subclasses."""
        pass

    defjoin_after_forward(self) -> None:  # noqa: B027
"""Join streams after forward. Override in subclasses."""
        pass

    def_wait_for_layer(self, layer_idx: int) -> None:  # noqa: B027
"""Wait for layer prefetch. Override in subclasses."""
        pass

    def_start_prefetch(self, layer_idx: int) -> None:  # noqa: B027
"""Start layer prefetch. Override in subclasses."""
        pass
```

### \_start\_prefetch [¶](#vllm.model_executor.offloader.base.BaseOffloader._start_prefetch "Permanent link")

```
_start_prefetch(layer_idx: int) -> None
```

Start layer prefetch. Override in subclasses.

Source code in `vllm/model_executor/offloader/base.py`

```
def_start_prefetch(self, layer_idx: int) -> None:  # noqa: B027
"""Start layer prefetch. Override in subclasses."""
    pass
```

### \_wait\_for\_layer [¶](#vllm.model_executor.offloader.base.BaseOffloader._wait_for_layer "Permanent link")

```
_wait_for_layer(layer_idx: int) -> None
```

Wait for layer prefetch. Override in subclasses.

Source code in `vllm/model_executor/offloader/base.py`

```
def_wait_for_layer(self, layer_idx: int) -> None:  # noqa: B027
"""Wait for layer prefetch. Override in subclasses."""
    pass
```

### join\_after\_forward [¶](#vllm.model_executor.offloader.base.BaseOffloader.join_after_forward "Permanent link")

```
join_after_forward() -> None
```

Join streams after forward. Override in subclasses.

Source code in `vllm/model_executor/offloader/base.py`

```
defjoin_after_forward(self) -> None:  # noqa: B027
"""Join streams after forward. Override in subclasses."""
    pass
```

### post\_init [¶](#vllm.model_executor.offloader.base.BaseOffloader.post_init "Permanent link")

Called after model construction completes.

Offloaders can use this to: - Finalize parameter storage - Start initial prefetching - Allocate shared resources

Source code in `vllm/model_executor/offloader/base.py`

```
defpost_init(self):
"""Called after model construction completes.

    Offloaders can use this to:
    - Finalize parameter storage
    - Start initial prefetching
    - Allocate shared resources
    """
    return
```

### sync\_prev\_onload [¶](#vllm.model_executor.offloader.base.BaseOffloader.sync_prev_onload "Permanent link")

```
sync_prev_onload() -> None
```

Sync previous onload operations. Override in subclasses.

Source code in `vllm/model_executor/offloader/base.py`

```
defsync_prev_onload(self) -> None:  # noqa: B027
"""Sync previous onload operations. Override in subclasses."""
    pass
```

### wrap\_modules `abstractmethod` [¶](#vllm.model_executor.offloader.base.BaseOffloader.wrap_modules "Permanent link")

Wrap modules with offloading logic.

Parameters:

Name Type Description Default `modules_generator` `Generator[Module, None, None]`

Generator yielding modules to potentially offload.

*required*

Returns:

Type Description `list[Module]`

List of modules, potentially with offloading hooks installed.

Source code in `vllm/model_executor/offloader/base.py`

```
@abstractmethod
defwrap_modules(
    self,
    modules_generator: Generator[nn.Module, None, None],
) -> list[nn.Module]:
"""Wrap modules with offloading logic.

    Args:
        modules_generator: Generator yielding modules to potentially offload.

    Returns:
        List of modules, potentially with offloading hooks installed.
    """
    pass
```

## NoopOffloader [¶](#vllm.model_executor.offloader.base.NoopOffloader "Permanent link")

Bases: `BaseOffloader`

No-op offloader that returns modules as-is without any offloading.

Source code in `vllm/model_executor/offloader/base.py`

```
classNoopOffloader(BaseOffloader):
"""No-op offloader that returns modules as-is without any offloading."""

    defwrap_modules(
        self,
        modules_generator: Generator[nn.Module, None, None],
    ) -> list[nn.Module]:
"""Return modules unchanged."""
        return list(modules_generator)
```

### wrap\_modules [¶](#vllm.model_executor.offloader.base.NoopOffloader.wrap_modules "Permanent link")

Return modules unchanged.

Source code in `vllm/model_executor/offloader/base.py`

```
defwrap_modules(
    self,
    modules_generator: Generator[nn.Module, None, None],
) -> list[nn.Module]:
"""Return modules unchanged."""
    return list(modules_generator)
```

## create\_offloader [¶](#vllm.model_executor.offloader.base.create_offloader "Permanent link")

Create an offloader based on the offload configuration.

Uses the explicit `offload_backend` selector. When set to `"auto"`, selects prefetch if `offload_group_size > 0`, UVA if `cpu_offload_gb > 0`, otherwise noop.

Source code in `vllm/model_executor/offloader/base.py`

```
defcreate_offloader(offload_config: "OffloadConfig") -> BaseOffloader:
"""Create an offloader based on the offload configuration.

    Uses the explicit ``offload_backend`` selector.  When set to ``"auto"``,
    selects prefetch if ``offload_group_size > 0``, UVA if
    ``cpu_offload_gb > 0``, otherwise noop.
    """
    fromvllm.model_executor.offloader.prefetchimport PrefetchOffloader
    fromvllm.model_executor.offloader.uvaimport UVAOffloader

    backend = offload_config.offload_backend
    uva = offload_config.uva
    prefetch = offload_config.prefetch

    if backend == "auto":
        if prefetch.offload_group_size > 0:
            backend = "prefetch"
        elif uva.cpu_offload_gb > 0:
            backend = "uva"
        else:
            return NoopOffloader()

    if backend == "prefetch":
        return PrefetchOffloader(
            group_size=prefetch.offload_group_size,
            num_in_group=prefetch.offload_num_in_group,
            prefetch_step=prefetch.offload_prefetch_step,
            offload_params=prefetch.offload_params,
            mode="cpu",
        )
    elif backend == "uva":
        return UVAOffloader(
            cpu_offload_max_bytes=int(uva.cpu_offload_gb * 1024**3),
            cpu_offload_params=uva.cpu_offload_params,
        )
    else:
        return NoopOffloader()
```

## get\_offloader [¶](#vllm.model_executor.offloader.base.get_offloader "Permanent link")

```
get_offloader() -> BaseOffloader
```

Get the global offloader instance.

Source code in `vllm/model_executor/offloader/base.py`

```
defget_offloader() -> BaseOffloader:
"""Get the global offloader instance."""
    return _instance
```

## set\_offloader [¶](#vllm.model_executor.offloader.base.set_offloader "Permanent link")

```
set_offloader(instance: BaseOffloader) -> None
```

Set the global offloader instance.

Source code in `vllm/model_executor/offloader/base.py`

```
defset_offloader(instance: BaseOffloader) -> None:
"""Set the global offloader instance."""
    global _instance
    _instance = instance
    if isinstance(instance, NoopOffloader):
        logger.debug_once("Offloader set to NoopOffloader (no offloading).")
    else:
        logger.info_once("Offloader set to %s", type(instance).__name__)
```

## should\_pin\_memory [¶](#vllm.model_executor.offloader.base.should_pin_memory "Permanent link")

```
should_pin_memory() -> bool
```

Check if pinned memory should be used for weight offloading.

Combines the platform capability check with the user override env var. On unified-memory systems (e.g. GH200) pinned memory eats into GPU memory, so users can disable it via VLLM\_WEIGHT\_OFFLOADING\_DISABLE\_PIN\_MEMORY.

Source code in `vllm/model_executor/offloader/base.py`

```
defshould_pin_memory() -> bool:
"""Check if pinned memory should be used for weight offloading.

    Combines the platform capability check with the user override env var.
    On unified-memory systems (e.g. GH200) pinned memory eats into GPU
    memory, so users can disable it via VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY.
    """
    return (
        is_pin_memory_available() and not envs.VLLM_WEIGHT_OFFLOADING_DISABLE_PIN_MEMORY
    )
```