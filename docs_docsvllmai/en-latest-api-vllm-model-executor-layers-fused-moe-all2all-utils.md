---
title: all2all_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/all2all_utils/
source: sitemap
fetched_at: 2026-05-07T21:24:31.734946182-03:00
rendered_js: false
word_count: 63
summary: This document describes a utility function that adjusts the layer hidden size for Mixture-of-Experts models based on specific parallelization and kernel configuration requirements.
tags:
    - moe
    - hidden-size
    - parallelization
    - kernel-optimization
    - all2all
    - neural-network-layers
category: api
---

Given layer hidden size and MoE configurations, round up hidden\_size if necessary.

Parameters:

Name Type Description Default `hidden_size` `int`

Layer hidden-size

*required* `act_dtype` `dtype`

Data type of the layer activations.

*required* `moe_parallel_config` `FusedMoEParallelConfig`

Fused MoE parallelization strategy configuration.

*required*

Return

Rounded up hidden\_size if rounding up is required based on the configs and all2all backend. Original hidden size otherwise.

Source code in `vllm/model_executor/layers/fused_moe/all2all_utils.py`

```
defmaybe_roundup_layer_hidden_size(
    hidden_size: int,
    act_dtype: torch.dtype,
    moe_parallel_config: FusedMoEParallelConfig,
) -> int:
"""
    Given layer hidden size and MoE configurations, round up hidden_size
    if necessary.

    Args:
        hidden_size: Layer hidden-size
        act_dtype: Data type of the layer activations.
        moe_parallel_config: Fused MoE parallelization strategy configuration.

    Return:
        Rounded up hidden_size if rounding up is required based on the configs
        and all2all backend.
        Original hidden size otherwise.
    """
    if moe_parallel_config.use_deepep_ht_kernels:
        hidden_size = DeepEPHTPrepareAndFinalize.maybe_roundup_layer_hidden_size(
            hidden_size, act_dtype
        )

    if moe_parallel_config.use_deepep_ll_kernels:
        hidden_size = DeepEPLLPrepareAndFinalize.maybe_roundup_layer_hidden_size(
            hidden_size
        )

    if moe_parallel_config.use_nixl_ep_kernels:
        hidden_size = NixlEPPrepareAndFinalize.maybe_roundup_layer_hidden_size(
            hidden_size
        )

    return hidden_size
```