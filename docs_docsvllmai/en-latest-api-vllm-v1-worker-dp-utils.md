---
title: dp_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/worker/dp_utils/
source: sitemap
fetched_at: 2026-05-07T21:42:12.253384448-03:00
rendered_js: false
word_count: 350
summary: This document provides a reference for utility functions used to synchronize data parallel (DP) ranks, specifically regarding microbatching decisions, CUDA graph modes, and token padding alignment.
tags:
    - data-parallelism
    - cudagraphs
    - microbatching
    - vllm
    - distributed-training
    - tensor-synchronization
category: reference
---

## \_post\_process\_cudagraph\_mode [¶](#vllm.v1.worker.dp_utils._post_process_cudagraph_mode "Permanent link")

```
_post_process_cudagraph_mode(tensor: Tensor) -> int
```

Synchronize cudagraph\_mode across DP ranks by taking the minimum. If any rank has NONE (0), all ranks use NONE. This ensures all ranks send consistent values (all padded or all unpadded).

Source code in `vllm/v1/worker/dp_utils.py`

```
def_post_process_cudagraph_mode(tensor: torch.Tensor) -> int:
"""
    Synchronize cudagraph_mode across DP ranks by taking the minimum.
    If any rank has NONE (0), all ranks use NONE.
    This ensures all ranks send consistent values (all padded or all unpadded).
    """
    return int(tensor[3, :].min().item())
```

## \_synchronize\_dp\_ranks [¶](#vllm.v1.worker.dp_utils._synchronize_dp_ranks "Permanent link")

1. Decides if each DP rank is going to microbatch. Either all ranks run with microbatching or none of them do.
2. Determines the total number of tokens that each rank will run. When running microbatched or if cudagraph is enabled (synced across ranks), all ranks will be padded out so that they run with the same number of tokens.
3. Synchronizes cudagraph\_mode across ranks by taking the minimum.

tuple[

Name Type Description `should_ubatch` `bool`

Are all DP ranks going to microbatch

`num_tokens_after_padding` `Tensor | None`

A tensor containing the total number of

`int`

tokens per-microbatch for each DP rank including any DP padding.

`synced_cudagraph_mode` `tuple[bool, Tensor | None, int]`

The synchronized cudagraph mode (min across ranks)

]

Source code in `vllm/v1/worker/dp_utils.py`

```
def_synchronize_dp_ranks(
    num_tokens_unpadded: int,
    num_tokens_padded: int,
    should_attempt_ubatching: bool,
    cudagraph_mode: int,
    parallel_config: ParallelConfig,
) -> tuple[bool, torch.Tensor | None, int]:
"""
    1. Decides if each DP rank is going to microbatch. Either all ranks
    run with microbatching or none of them do.

    2. Determines the total number of tokens that each rank will run.
    When running microbatched or if cudagraph is enabled (synced across ranks),
    all ranks will be padded out so that they run with the same number of tokens.

    3. Synchronizes cudagraph_mode across ranks by taking the minimum.

    Returns: tuple[
        should_ubatch: Are all DP ranks going to microbatch
        num_tokens_after_padding: A tensor containing the total number of
        tokens per-microbatch for each DP rank including any DP padding.
        synced_cudagraph_mode: The synchronized cudagraph mode (min across ranks)
    ]

    """
    assert num_tokens_padded >= num_tokens_unpadded

    # Coordinate between the DP ranks via an All Reduce
    # to determine the total number of tokens that each rank
    # will run and if we are using ubatching or not.
    tensor = _run_ar(
        should_ubatch=should_attempt_ubatching,
        orig_num_tokens_per_ubatch=num_tokens_unpadded,
        padded_num_tokens_per_ubatch=num_tokens_padded,
        cudagraph_mode=cudagraph_mode,
        parallel_config=parallel_config,
    )

    # Synchronize cudagraph_mode across ranks first (take min).
    # This is needed before DP padding decision since we use the synced
    # cudagraph mode to determine whether DP padding is needed.
    synced_cudagraph_mode = _post_process_cudagraph_mode(tensor)

    # Check conditions for microbatching
    should_ubatch = _post_process_ubatch(tensor, parallel_config.num_ubatches)

    # DP padding is needed when cudagraph is enabled (synced across ranks)
    # or when ubatching/DBO is active (ubatching requires uniform batch
    # sizes across DP ranks currently).
    # Use the synced runtime cudagraph mode rather than the compilation config
    # so we can avoid padding when cudagraph is not enabled for this step.
    should_dp_pad = synced_cudagraph_mode != 0 or should_ubatch

    # Pad all DP ranks up to the maximum token count across ranks if
    # should_dp_pad is True
    num_tokens_after_padding = _post_process_dp_padding(
        tensor,
        should_dp_pad,
    )

    return should_ubatch, num_tokens_after_padding, synced_cudagraph_mode
```

## coordinate\_batch\_across\_dp [¶](#vllm.v1.worker.dp_utils.coordinate_batch_across_dp "Permanent link")

```
coordinate_batch_across_dp(
    num_tokens_unpadded: int,
    allow_microbatching: bool,
    parallel_config: ParallelConfig,
    num_tokens_padded: int | None = None,
    uniform_decode: bool | None = None,
    cudagraph_mode: int = 0,
) -> tuple[bool, Tensor | None, int]
```

Coordinates amongst all DP ranks to determine if and how the full batch should be split into microbatches.

Parameters:

Name Type Description Default `num_tokens_unpadded` `int`

Number of tokens without accounting for padding

*required* `allow_microbatching` `bool`

If microbatching should be attempted

*required* `parallel_config` `ParallelConfig`

The parallel config

*required* `num_tokens_padded` `int | None`

Number of tokens including any non-DP padding (CUDA graphs, TP, etc)

`None` `uniform_decode` `bool | None`

Only used if allow\_microbatching is True. True if the batch only contains single token decodes

`None` `cudagraph_mode` `int`

The cudagraph mode for this rank (0=NONE, 1=PIECEWISE, 2=FULL). DP padding is enabled when synced cudagraph mode across ranks is not NONE.

`0`

tuple[

Name Type Description `ubatch_slices` `bool`

if this is set then all DP ranks have agreed to

`Tensor | None`

microbatch

`num_tokens_after_padding` `int`

A tensor containing the total number of

`tuple[bool, Tensor | None, int]`

tokens per-microbatch for each DP rank including padding. Will be

`tuple[bool, Tensor | None, int]`

padded up to the max value across all DP ranks when cudagraph is enabled.

`synced_cudagraph_mode` `tuple[bool, Tensor | None, int]`

The synchronized cudagraph mode (min across ranks)

]

Source code in `vllm/v1/worker/dp_utils.py`

```
defcoordinate_batch_across_dp(
    num_tokens_unpadded: int,
    allow_microbatching: bool,
    parallel_config: ParallelConfig,
    num_tokens_padded: int | None = None,
    uniform_decode: bool | None = None,
    cudagraph_mode: int = 0,
) -> tuple[bool, torch.Tensor | None, int]:
"""
    Coordinates amongst all DP ranks to determine if and how the full batch
    should be split into microbatches.

    Args:
        num_tokens_unpadded: Number of tokens without accounting for padding
        allow_microbatching: If microbatching should be attempted
        parallel_config: The parallel config
        num_tokens_padded: Number of tokens including any non-DP padding (CUDA graphs,
            TP, etc)
        uniform_decode: Only used if allow_microbatching is True. True if the batch
            only contains single token decodes
        cudagraph_mode: The cudagraph mode for this rank (0=NONE, 1=PIECEWISE, 2=FULL).
            DP padding is enabled when synced cudagraph mode across ranks is not NONE.

    Returns: tuple[
        ubatch_slices: if this is set then all DP ranks have agreed to
        microbatch
        num_tokens_after_padding: A tensor containing the total number of
        tokens per-microbatch for each DP rank including padding. Will be
        padded up to the max value across all DP ranks when cudagraph is enabled.
        synced_cudagraph_mode: The synchronized cudagraph mode (min across ranks)
    ]

    """
    if parallel_config.data_parallel_size == 1:
        # Early exit.
        return False, None, cudagraph_mode

    # If the caller has explicitly enabled microbatching.
    should_attempt_ubatching = False
    if allow_microbatching:
        # Check preconditions for microbatching
        assert uniform_decode is not None
        should_attempt_ubatching = check_ubatch_thresholds(
            parallel_config,
            num_tokens_unpadded,
            uniform_decode=uniform_decode,
        )

    if num_tokens_padded is None:
        num_tokens_padded = num_tokens_unpadded

    (should_ubatch, num_tokens_after_padding, synced_cudagraph_mode) = (
        _synchronize_dp_ranks(
            num_tokens_unpadded,
            num_tokens_padded,
            should_attempt_ubatching,
            cudagraph_mode,
            parallel_config,
        )
    )

    return (should_ubatch, num_tokens_after_padding, synced_cudagraph_mode)
```