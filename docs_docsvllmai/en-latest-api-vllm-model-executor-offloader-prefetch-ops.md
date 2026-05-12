---
title: prefetch_ops - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/offloader/prefetch_ops/
source: sitemap
fetched_at: 2026-05-07T21:33:53.832452486-03:00
rendered_js: false
word_count: 202
summary: This document defines custom PyTorch operators for managing asynchronous model weight prefetching while ensuring compatibility with torch.compile and CUDA graphs through data dependency registration.
tags:
    - vllm
    - torch-compile
    - cuda-graphs
    - async-prefetch
    - custom-ops
    - memory-management
category: reference
---

## vllm.model\_executor.offloader.prefetch\_ops [¶](#vllm.model_executor.offloader.prefetch_ops "Permanent link")

Custom ops for prefetch offloader torch.compile + CUDA graph compatibility.

These ops use mutates\_args to create data dependencies that prevent the compiler from reordering prefetch/sync operations.

## \_start\_prefetch\_fake [¶](#vllm.model_executor.offloader.prefetch_ops._start_prefetch_fake "Permanent link")

```
_start_prefetch_fake(
    output_tensor: Tensor, layer_idx: int
) -> None
```

Fake implementation for torch.compile tracing.

Source code in `vllm/model_executor/offloader/prefetch_ops.py`

```
def_start_prefetch_fake(
    output_tensor: torch.Tensor,
    layer_idx: int,
) -> None:
"""Fake implementation for torch.compile tracing."""
    return
```

## \_start\_prefetch\_impl [¶](#vllm.model_executor.offloader.prefetch_ops._start_prefetch_impl "Permanent link")

```
_start_prefetch_impl(
    output_tensor: Tensor, layer_idx: int
) -> None
```

Start async prefetch of layer\_idx weights.

Initiates H2D copy on the copy stream for the specified layer.

Parameters:

Name Type Description Default `output_tensor` `Tensor`

Output from forward - declared as mutated to prevent torch.compile from reordering this op before the computation that produces output\_tensor.

*required* `layer_idx` `int`

Index of the layer to prefetch.

*required*

Source code in `vllm/model_executor/offloader/prefetch_ops.py`

```
def_start_prefetch_impl(
    output_tensor: torch.Tensor,
    layer_idx: int,
) -> None:
"""Start async prefetch of layer_idx weights.

    Initiates H2D copy on the copy stream for the specified layer.

    Args:
        output_tensor: Output from forward - declared as mutated to
            prevent torch.compile from reordering this op before the
            computation that produces output_tensor.
        layer_idx: Index of the layer to prefetch.
    """
    get_offloader()._start_prefetch(layer_idx)
```

## \_wait\_prefetch\_fake [¶](#vllm.model_executor.offloader.prefetch_ops._wait_prefetch_fake "Permanent link")

```
_wait_prefetch_fake(
    input_tensor: Tensor, layer_idx: int
) -> None
```

Fake implementation for torch.compile tracing.

Source code in `vllm/model_executor/offloader/prefetch_ops.py`

```
def_wait_prefetch_fake(
    input_tensor: torch.Tensor,
    layer_idx: int,
) -> None:
"""Fake implementation for torch.compile tracing."""
    return
```

## \_wait\_prefetch\_impl [¶](#vllm.model_executor.offloader.prefetch_ops._wait_prefetch_impl "Permanent link")

```
_wait_prefetch_impl(
    input_tensor: Tensor, layer_idx: int
) -> None
```

Wait for prefetch of layer\_idx to complete.

Synchronizes the compute stream with the copy stream to ensure the prefetched weights are ready for use.

Parameters:

Name Type Description Default `input_tensor` `Tensor`

Input to the layer (e.g., hidden\_states) - declared as mutated to create data dependency for torch.compile.

*required* `layer_idx` `int`

Index of the layer to wait for.

*required*

Source code in `vllm/model_executor/offloader/prefetch_ops.py`

```
def_wait_prefetch_impl(
    input_tensor: torch.Tensor,
    layer_idx: int,
) -> None:
"""Wait for prefetch of layer_idx to complete.

    Synchronizes the compute stream with the copy stream to ensure
    the prefetched weights are ready for use.

    Args:
        input_tensor: Input to the layer (e.g., hidden_states) - declared
            as mutated to create data dependency for torch.compile.
        layer_idx: Index of the layer to wait for.
    """
    get_offloader()._wait_for_layer(layer_idx)
```

## register\_prefetch\_offloader\_ops [¶](#vllm.model_executor.offloader.prefetch_ops.register_prefetch_offloader_ops "Permanent link")

```
register_prefetch_offloader_ops() -> None
```

Register custom ops for prefetch offloader.

Must be called before the ops are used. This is typically done at module import time.

Source code in `vllm/model_executor/offloader/prefetch_ops.py`

```
defregister_prefetch_offloader_ops() -> None:
"""Register custom ops for prefetch offloader.

    Must be called before the ops are used. This is typically done
    at module import time.
    """
    direct_register_custom_op(
        op_name="wait_prefetch",
        op_func=_wait_prefetch_impl,
        mutates_args=["input_tensor"],
        fake_impl=_wait_prefetch_fake,
    )

    direct_register_custom_op(
        op_name="start_prefetch",
        op_func=_start_prefetch_impl,
        mutates_args=["output_tensor"],
        fake_impl=_start_prefetch_fake,
    )
```