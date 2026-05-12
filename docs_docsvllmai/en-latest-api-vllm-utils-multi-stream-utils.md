---
title: multi_stream_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/multi_stream_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:46.113796572-03:00
rendered_js: false
word_count: 373
summary: This document describes utility functions designed to perform concurrent execution of tasks on multiple CUDA streams using event-based synchronization.
tags:
    - cuda-streams
    - concurrency
    - pytorch-utilities
    - parallel-execution
    - asynchronous-programming
    - gpu-optimization
category: api
---

## execute\_in\_parallel [¶](#vllm.utils.multi_stream_utils.execute_in_parallel "Permanent link")

Run default\_fn on the current stream and aux\_fns concurrently on aux\_streams.

Generalizes maybe\_execute\_in\_parallel to N aux callables. Slots where aux\_fns\[i] is None are skipped (no stream switch, no event record); their corresponding entry in the returned aux\_results list is None.

start\_event fans out from the current stream to every launched aux stream; done\_events\[i] is recorded after aux\_fns\[i] so the current stream joins before returning. Falls back to sequential execution on the current stream when aux\_streams is None or enable is False; in that case default\_fn runs first, then aux\_fns in order.

Parameters:

Name Type Description Default `default_fn` `Callable[[], Any]`

Callable for the default (current) stream.

*required* `aux_fns` `list[Callable[[], Any] | None]`

Per-aux callables; entries may be None to skip.

*required* `start_event` `Event`

CUDA event recorded on the current stream before default\_fn so each launched aux stream can wait on it.

*required* `done_events` `list[Event]`

One CUDA event per aux slot, recorded after the corresponding aux\_fn. Length must match aux\_fns.

*required* `aux_streams` `list[Stream] | None`

Per-aux CUDA streams. Length must match aux\_fns. Multi-stream is disabled when None.

`None` `enable` `bool`

Opt-in switch for the multi-stream path. Defaults to False, so callers that pass aux\_streams must also pass enable=True (typically gated by an env var) to actually overlap. When False, execution falls back to sequential on the current stream.

`False`

Returns:

Type Description `Any`

Tuple of (default\_result, aux\_results) where aux\_results\[i] is the

`list[Any]`

result of aux\_fns\[i] (or None when skipped).

Source code in `vllm/utils/multi_stream_utils.py`

```
defexecute_in_parallel(
    default_fn: Callable[[], Any],
    aux_fns: list[Callable[[], Any] | None],
    start_event: torch.cuda.Event,
    done_events: list[torch.cuda.Event],
    aux_streams: list[torch.cuda.Stream] | None = None,
    enable: bool = False,
) -> tuple[Any, list[Any]]:
"""Run default_fn on the current stream and aux_fns concurrently on
    aux_streams.

    Generalizes maybe_execute_in_parallel to N aux callables. Slots where
    aux_fns[i] is None are skipped (no stream switch, no event record); their
    corresponding entry in the returned aux_results list is None.

    start_event fans out from the current stream to every launched aux stream;
    done_events[i] is recorded after aux_fns[i] so the current stream joins
    before returning. Falls back to sequential execution on the current stream
    when aux_streams is None or enable is False; in that case default_fn runs
    first, then aux_fns in order.

    Args:
        default_fn: Callable for the default (current) stream.
        aux_fns: Per-aux callables; entries may be None to skip.
        start_event: CUDA event recorded on the current stream before
            default_fn so each launched aux stream can wait on it.
        done_events: One CUDA event per aux slot, recorded after the
            corresponding aux_fn. Length must match aux_fns.
        aux_streams: Per-aux CUDA streams. Length must match aux_fns.
            Multi-stream is disabled when None.
        enable: Opt-in switch for the multi-stream path. Defaults to False,
            so callers that pass aux_streams must also pass enable=True
            (typically gated by an env var) to actually overlap. When False,
            execution falls back to sequential on the current stream.

    Returns:
        Tuple of (default_result, aux_results) where aux_results[i] is the
        result of aux_fns[i] (or None when skipped).
    """
    aux_results: list[Any]
    if aux_streams is None or not enable:
        default_result = default_fn()
        aux_results = [fn() if fn is not None else None for fn in aux_fns]
        return default_result, aux_results

    assert len(aux_fns) == len(aux_streams) == len(done_events), (
        "aux_fns, aux_streams, and done_events must be the same length"
    )

    aux_results = [None] * len(aux_fns)
    pending: list[torch.cuda.Event] = []

    start_event.record()
    for i, fn in enumerate(aux_fns):
        if fn is None:
            continue
        with torch.cuda.stream(aux_streams[i]):
            start_event.wait()
            aux_results[i] = fn()
            done_events[i].record()
        pending.append(done_events[i])

    default_result = default_fn()

    for ev in pending:
        ev.wait()

    return default_result, aux_results
```

## maybe\_execute\_in\_parallel [¶](#vllm.utils.multi_stream_utils.maybe_execute_in_parallel "Permanent link")

Run two functions potentially in parallel on separate CUDA streams.

When aux\_stream is provided, fn0 runs on the current (default) stream and fn1 runs on aux\_stream, synchronized via CUDA events. When aux\_stream is None, both functions execute sequentially on the current stream.

This design follows TensorRT-LLM's maybe\_execute\_in\_parallel pattern (tensorrt\_llm/\_torch/modules/multi\_stream\_utils.py).

Parameters:

Name Type Description Default `fn0` `Callable[[], Any]`

Callable for the default stream.

*required* `fn1` `Callable[[], Any]`

Callable for the auxiliary stream.

*required* `event0` `Event`

CUDA event recorded before fn0 so aux\_stream can wait.

*required* `event1` `Event`

CUDA event recorded after fn1 so default stream can wait.

*required* `aux_stream` `Stream | None`

The second CUDA stream for fn1. Multi-stream is disabled when aux\_stream is None.

`None`

Returns:

Type Description `tuple[Any, Any]`

Tuple of (fn0\_result, fn1\_result).

Source code in `vllm/utils/multi_stream_utils.py`

```
defmaybe_execute_in_parallel(
    fn0: Callable[[], Any],
    fn1: Callable[[], Any],
    event0: torch.cuda.Event,
    event1: torch.cuda.Event,
    aux_stream: torch.cuda.Stream | None = None,
) -> tuple[Any, Any]:
"""Run two functions potentially in parallel on separate CUDA streams.

    When aux_stream is provided, fn0 runs on the current (default) stream and
    fn1 runs on aux_stream, synchronized via CUDA events.  When aux_stream is
    None, both functions execute sequentially on the current stream.

    This design follows TensorRT-LLM's maybe_execute_in_parallel pattern
    (tensorrt_llm/_torch/modules/multi_stream_utils.py).

    Args:
        fn0: Callable for the default stream.
        fn1: Callable for the auxiliary stream.
        event0: CUDA event recorded before fn0 so aux_stream can wait.
        event1: CUDA event recorded after fn1 so default stream can wait.
        aux_stream: The second CUDA stream for fn1.
            Multi-stream is disabled when aux_stream is None.

    Returns:
        Tuple of (fn0_result, fn1_result).
    """
    if aux_stream is not None:
        event0.record()
        result0 = fn0()
        with torch.cuda.stream(aux_stream):
            event0.wait()
            result1 = fn1()
            event1.record()
        event1.wait()
    else:
        result0 = fn0()
        result1 = fn1()
    return (result0, result1)
```