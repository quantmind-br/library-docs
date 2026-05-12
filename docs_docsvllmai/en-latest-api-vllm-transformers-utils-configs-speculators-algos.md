---
title: algos - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/configs/speculators/algos/
source: sitemap
fetched_at: 2026-05-07T21:37:41.228024256-03:00
rendered_js: false
word_count: 107
summary: This document describes the function used to transform configuration parameters for the Eagle-3 speculative decoding model into a format compatible with Transformers PreTrainedConfig.
tags:
    - eagle-3
    - speculative-decoding
    - configuration-management
    - vllm
    - model-architecture
    - transformers-library
category: configuration
---

Apply Eagle-3 specific configuration transformations to the `dict` used to construct the Transformers PreTrainedConfig.

Eagle-3 specific fields: - draft\_vocab\_size: Size of the draft model's vocabulary - target\_hidden\_size: Hidden size of the target model - norm\_before\_residual: Whether to apply norm before residual connection - norm\_before\_fc: Whether to apply RMSNorm before the fc projection - eagle\_aux\_hidden\_state\_layer\_ids: List of layer indices from the base model to use as auxiliary inputs for the Eagle3 drafter. These layers provide intermediate hidden states that help the drafter make better predictions. This is the standard field used in Eagle3 checkpoints.

Source code in `vllm/transformers_utils/configs/speculators/algos.py`

```
@register_speculator("eagle3")
defupdate_eagle3(config_dict: dict, pre_trained_config: dict) -> None:
"""
    Apply Eagle-3 specific configuration transformations to the `dict` used to
    construct the Transformers PreTrainedConfig.

    Eagle-3 specific fields:
    - draft_vocab_size: Size of the draft model's vocabulary
    - target_hidden_size: Hidden size of the target model
    - norm_before_residual: Whether to apply norm before residual connection
    - norm_before_fc: Whether to apply RMSNorm before the fc projection
    - eagle_aux_hidden_state_layer_ids: List of layer indices from the base
        model to use as auxiliary inputs for the Eagle3 drafter. These layers
        provide intermediate hidden states that help the drafter make better
        predictions. This is the standard field used in Eagle3 checkpoints.
    """

    pre_trained_config["draft_vocab_size"] = config_dict.get("draft_vocab_size")
    if config_dict.get("target_hidden_size") is not None:
        pre_trained_config["target_hidden_size"] = config_dict["target_hidden_size"]
    pre_trained_config["norm_before_residual"] = config_dict.get(
        "norm_before_residual", True
    )
    pre_trained_config["norm_before_fc"] = config_dict.get("norm_before_fc", False)
    pre_trained_config["architectures"] = ["Eagle3LlamaForCausalLM"]
    if config_dict.get("eagle_aux_hidden_state_layer_ids"):
        pre_trained_config["eagle_aux_hidden_state_layer_ids"] = config_dict[
            "eagle_aux_hidden_state_layer_ids"
        ]
```