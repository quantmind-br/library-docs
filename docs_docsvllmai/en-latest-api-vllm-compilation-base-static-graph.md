---
title: base_static_graph - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/compilation/base_static_graph/
source: sitemap
fetched_at: 2026-05-07T21:16:11.016368059-03:00
rendered_js: false
word_count: 207
summary: This document defines the AbstractStaticGraphWrapper interface used by vLLM to encapsulate and execute callables within a static graph capture framework.
tags:
    - vllm
    - static-graph
    - cuda-graphs
    - graph-capture
    - python-protocol
    - compute-compilation
category: reference
---

## vllm.compilation.base\_static\_graph [¶](#vllm.compilation.base_static_graph "Permanent link")

## AbstractStaticGraphWrapper [¶](#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper "Permanent link")

Bases: `Protocol`

StaticGraphWrapper interface that allows platforms to wrap a callable to be captured as a static graph.

Source code in `vllm/compilation/base_static_graph.py`

```
classAbstractStaticGraphWrapper(Protocol):
"""
    StaticGraphWrapper interface that allows platforms to wrap a callable
    to be captured as a static graph.
    """

    def__init__(
        self,
        runnable: Callable[..., Any],
        vllm_config: VllmConfig,
        runtime_mode: CUDAGraphMode,
        **kwargs: Any,
    ) -> None:
"""
        Initializes the StaticGraphWrapper class with graph capturing and
        execution-related configurations.

        Args:
            runnable (Callable): The callable to be wrapped and captured.
            vllm_config (VllmConfig): Global configuration for vLLM.
            runtime_mode (CUDAGraphMode): The style of the static
                graph runtime. See CUDAGraphMode in vllm/config.py.
                Note that only the subset enum `NONE`, `PIECEWISE` and `FULL`
                are used as concrete runtime mode for cudagraph dispatching.
        Keyword Args:
            kwargs: Additional keyword arguments for platform-specific
                configurations.
        """
        raise NotImplementedError

    def__call__(self, *args: Any, **kwargs: Any) -> Any:
"""
        Executes the wrapped callable.

        If the current runtime mode in the ForwardContext matches the runtime
        mode of this instance, it replays the CUDAGraph or captures it using
        the callable if it hasn't been captured yet. Otherwise, it calls the
        original callable directly.

        Args:
            *args: Variable length input arguments to be passed into the
                callable.
            **kwargs: Keyword arguments to be passed into the callable.

        Returns:
            Any: Output of the executed callable.
        """
        raise NotImplementedError
```

### \_\_call\__ [¶](#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__call__ "Permanent link")

Executes the wrapped callable.

If the current runtime mode in the ForwardContext matches the runtime mode of this instance, it replays the CUDAGraph or captures it using the callable if it hasn't been captured yet. Otherwise, it calls the original callable directly.

Parameters:

Name Type Description Default `*args` `Any`

Variable length input arguments to be passed into the callable.

`()` `**kwargs` `Any`

Keyword arguments to be passed into the callable.

`{}`

Returns:

Name Type Description `Any` `Any`

Output of the executed callable.

Source code in `vllm/compilation/base_static_graph.py`

```
def__call__(self, *args: Any, **kwargs: Any) -> Any:
"""
    Executes the wrapped callable.

    If the current runtime mode in the ForwardContext matches the runtime
    mode of this instance, it replays the CUDAGraph or captures it using
    the callable if it hasn't been captured yet. Otherwise, it calls the
    original callable directly.

    Args:
        *args: Variable length input arguments to be passed into the
            callable.
        **kwargs: Keyword arguments to be passed into the callable.

    Returns:
        Any: Output of the executed callable.
    """
    raise NotImplementedError
```

### \_\_init\__ [¶](#vllm.compilation.base_static_graph.AbstractStaticGraphWrapper.__init__ "Permanent link")

Initializes the StaticGraphWrapper class with graph capturing and execution-related configurations.

Parameters:

Name Type Description Default `runnable` `Callable`

The callable to be wrapped and captured.

*required* `vllm_config` `VllmConfig`

Global configuration for vLLM.

*required* `runtime_mode` `CUDAGraphMode`

The style of the static graph runtime. See CUDAGraphMode in vllm/config.py. Note that only the subset enum `NONE`, `PIECEWISE` and `FULL` are used as concrete runtime mode for cudagraph dispatching.

*required*

Keyword Args: kwargs: Additional keyword arguments for platform-specific configurations.

Source code in `vllm/compilation/base_static_graph.py`

```
def__init__(
    self,
    runnable: Callable[..., Any],
    vllm_config: VllmConfig,
    runtime_mode: CUDAGraphMode,
    **kwargs: Any,
) -> None:
"""
    Initializes the StaticGraphWrapper class with graph capturing and
    execution-related configurations.

    Args:
        runnable (Callable): The callable to be wrapped and captured.
        vllm_config (VllmConfig): Global configuration for vLLM.
        runtime_mode (CUDAGraphMode): The style of the static
            graph runtime. See CUDAGraphMode in vllm/config.py.
            Note that only the subset enum `NONE`, `PIECEWISE` and `FULL`
            are used as concrete runtime mode for cudagraph dispatching.
    Keyword Args:
        kwargs: Additional keyword arguments for platform-specific
            configurations.
    """
    raise NotImplementedError
```