---
title: model_arch - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/model_arch/
source: sitemap
fetched_at: 2026-05-07T21:17:04.159522828-03:00
rendered_js: false
word_count: 255
summary: This document defines the ModelArchitectureConfig dataclass, which specifies the structural parameters and model metadata required by the vLLM runtime for executing various model architectures.
tags:
    - vllm
    - model-architecture
    - configuration
    - runtime-parameters
    - deep-learning
    - dataclass
category: reference
---

Configuration for model architecture that required by vLLM runtime

Source code in `vllm/config/model_arch.py`

```
@dataclass(config=ConfigDict(arbitrary_types_allowed=True))
classModelArchitectureConfig:
"""
    Configuration for model architecture that required by vLLM runtime
    """

    architectures: list[str]
"""List of model architecture class names (e.g., ['LlamaForCausalLM']).
       It can be None upon calling `vllm_config.with_hf_config(config.text_config)`"""

    model_type: str
"""Model type identifier (e.g., 'llama', 'gpt_oss')."""

    text_model_type: str | None
"""Text model type identifier (e.g., 'llama4_text')."""

    hidden_size: int
"""Hidden size of the model."""

    total_num_hidden_layers: int
"""Number of hidden layers in the model."""

    total_num_attention_heads: int
"""Number of attention heads in the model."""

    head_size: int
"""Head dimension of the model."""

    vocab_size: int
"""Vocabulary size of the model."""

    total_num_kv_heads: int
"""Number of key value heads in the model."""

    num_experts: int
"""Number of experts in the model."""

    quantization_config: dict[str, Any] | None
"""Quantization configuration dictionary containing quantization parameters."""

    is_deepseek_mla: bool
"""Whether the model is a DeepSeek MLA model."""

    is_mm_prefix_lm: bool
"""Whether the model uses image bidirectional attention."""

    derived_max_model_len_and_key: tuple[float, str | None]
"""Derived maximum model length and key from the hf config."""
```

### architectures `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.architectures "Permanent link")

List of model architecture class names (e.g., \['LlamaForCausalLM']). It can be None upon calling `vllm_config.with_hf_config(config.text_config)`

### derived\_max\_model\_len\_and\_key `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.derived_max_model_len_and_key "Permanent link")

Derived maximum model length and key from the hf config.

### head\_size `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.head_size "Permanent link")

Head dimension of the model.

### hidden\_size `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.hidden_size "Permanent link")

Hidden size of the model.

### is\_deepseek\_mla `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.is_deepseek_mla "Permanent link")

Whether the model is a DeepSeek MLA model.

### is\_mm\_prefix\_lm `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.is_mm_prefix_lm "Permanent link")

Whether the model uses image bidirectional attention.

### model\_type `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.model_type "Permanent link")

Model type identifier (e.g., 'llama', 'gpt\_oss').

### num\_experts `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.num_experts "Permanent link")

Number of experts in the model.

### quantization\_config `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.quantization_config "Permanent link")

Quantization configuration dictionary containing quantization parameters.

### text\_model\_type `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.text_model_type "Permanent link")

```
text_model_type: str | None
```

Text model type identifier (e.g., 'llama4\_text').

### total\_num\_attention\_heads `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.total_num_attention_heads "Permanent link")

```
total_num_attention_heads: int
```

Number of attention heads in the model.

### total\_num\_hidden\_layers `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.total_num_hidden_layers "Permanent link")

```
total_num_hidden_layers: int
```

Number of hidden layers in the model.

### total\_num\_kv\_heads `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.total_num_kv_heads "Permanent link")

Number of key value heads in the model.

### vocab\_size `instance-attribute` [¶](#vllm.config.model_arch.ModelArchitectureConfig.vocab_size "Permanent link")

Vocabulary size of the model.