---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/compressed_tensors/utils/
source: sitemap
fetched_at: 2026-05-07T21:27:11.484068339-03:00
rendered_js: false
word_count: 165
summary: This function identifies the corresponding quantization target for a specific neural network layer by matching its name, class, or fused component mapping against a predefined configuration group.
tags:
    - quantization
    - model-compression
    - vllm
    - neural-network-layers
    - layer-matching
    - configuration-management
category: api
---

Helper function to look up which "target" in the compressed-tensors config that a layer corresponds to.

Recall that a compressed-tensors configs has a concept of config\_groups, where each layer can be quantized with a different scheme.

targets in each config\_group will be a list of either layer names (or regexes corresponding to layer names) or names of torch Modules.

First, we try to match the layer\_name with a target Second, we try to match the module's name with a target Third, we try to map the layer\_name to a list of fused module names. *All* component module names must match in order for a match to be successful. A successful match returns the first component target

:param layer\_name: layer name :param module: torch.nn.Module :param targets: list of targets to match the layer against :param fused\_mapping: map from fused layer names to its components :param fused\_strategy: either "all" or "any". If using "all", fused layers match if "all" of its components match

Source code in `vllm/model_executor/layers/quantization/compressed_tensors/utils.py`

```
deffind_matched_target(
    layer_name: str | None,
    module: Module,
    targets: Iterable[str],
    fused_mapping: Mapping[str, list[str]] = MappingProxyType({}),
) -> str | None:
"""
    Helper function to look up which "target" in the compressed-tensors
    config that a layer corresponds to.

    Recall that a compressed-tensors configs has a concept of
    config_groups, where each layer can be quantized with a different
    scheme.

    targets in each config_group will be a list of either layer names
    (or regexes corresponding to layer names) or names of torch Modules.

    First, we try to match the layer_name with a target
    Second, we try to match the module's name with a target
    Third, we try to map the layer_name to a list of fused module names.
        *All* component module names must match in order for a match to be
        successful. A successful match returns the first component target

    :param layer_name: layer name
    :param module: torch.nn.Module
    :param targets: list of targets to match the layer against
    :param fused_mapping: map from fused layer names to its components
    :param fused_strategy: either "all" or "any". If using "all", fused
        layers match if "all" of its components match
    """

    if layer_name is None:
        layer_name = ""

    matched_target = (
        _find_first_match(layer_name, targets)
        or _find_first_match(module.__class__.__name__, targets, True)
        or _match_fused_layer(layer_name, targets, fused_mapping)
    )

    return matched_target
```