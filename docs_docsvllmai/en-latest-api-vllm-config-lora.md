---
title: lora - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/lora/
source: sitemap
fetched_at: 2026-05-07T21:17:00.936601174-03:00
rendered_js: false
word_count: 508
summary: This document defines the LoRAConfig class in vLLM, which provides configuration options for managing Low-Rank Adaptation (LoRA) adapters, including batch limits, memory management, and performance optimization settings.
tags:
    - vllm
    - lora
    - configuration
    - fine-tuning
    - model-serving
    - adapters
category: reference
---

## LoRAConfig [¶](#vllm.config.lora.LoRAConfig "Permanent link")

Configuration for LoRA.

Source code in `vllm/config/lora.py`

```
@config(config=ConfigDict(arbitrary_types_allowed=True))
classLoRAConfig:
"""Configuration for LoRA."""

    max_lora_rank: MaxLoRARanks = 16
"""Max LoRA rank."""
    max_loras: int = Field(default=1, ge=1)
"""Max number of LoRAs in a single batch."""
    fully_sharded_loras: bool = False
"""By default, only half of the LoRA computation is sharded with tensor
    parallelism. Enabling this will use the fully sharded layers. At high
    sequence length, max rank or tensor parallel size, this is likely faster.
    """
    max_cpu_loras: int | None = None
"""Maximum number of LoRAs to store in CPU memory. Must be >= than
    `max_loras`."""
    lora_dtype: torch.dtype | LoRADType = "auto"
"""Data type for LoRA. If auto, will default to base model dtype."""
    target_modules: list[str] | None = None
"""Restrict LoRA to specific module suffixes (e.g., ["o_proj", "qkv_proj"]).
    If None, all supported LoRA modules are used. This allows deployment-time
    control over which modules have LoRA applied, useful for performance tuning."""
    default_mm_loras: dict[str, str] | None = None
"""Dictionary mapping specific modalities to LoRA model paths; this field
    is only applicable to multimodal models and should be leveraged when a
    model always expects a LoRA to be active when a given modality is present.
    Note that currently, if a request provides multiple additional
    modalities, each of which have their own LoRA, we do NOT apply
    default_mm_loras because we currently only support one lora adapter
    per prompt. When run in offline mode, the lora IDs for n modalities
    will be automatically assigned to 1-n with the names of the modalities
    in alphabetic order."""
    enable_tower_connector_lora: bool = False
"""If `True`, LoRA support for the tower (vision encoder) and connector 
    of multimodal models will be enabled. This is an experimental feature and 
    currently only supports some MM models such as the Qwen VL series. The default 
    is False."""
    specialize_active_lora: bool = False
"""Whether to construct lora kernel grid by the number of active LoRA adapters.
    When set to True, separate cuda graphs will be captured for different counts
    of active LoRAs (powers of 2 up to max_loras), which can improve performance
    for variable LoRA usage patterns at the cost of increased startup time and
    memory usage. Only takes effect when cudagraph_specialize_lora is True.
    """

    defcompute_hash(self) -> str:
"""
        WARNING: Whenever a new field is added to this config,
        ensure that it is included in the factors list if
        it affects the computation graph.

        Provide a hash that uniquely identifies all the configs
        that affect the structure of the computation
        graph from input ids/embeddings to the final hidden states,
        excluding anything before input ids/embeddings and after
        the final hidden states.
        """
        factors: list[Any] = []
        factors.append(self.max_lora_rank)
        factors.append(self.max_loras)
        factors.append(self.fully_sharded_loras)
        factors.append(self.lora_dtype)
        factors.append(self.enable_tower_connector_lora)
        # target_modules affects which modules get LoRA applied
        factors.append(
            tuple(sorted(self.target_modules)) if self.target_modules else None
        )

        hash_str = safe_hash(str(factors).encode(), usedforsecurity=False).hexdigest()
        return hash_str

    @model_validator(mode="after")
    def_validate_lora_config(self) -> Self:
        if self.max_cpu_loras is None:
            self.max_cpu_loras = self.max_loras
        elif self.max_cpu_loras < self.max_loras:
            raise ValueError(
                f"max_cpu_loras ({self.max_cpu_loras}) must be >= "
                f"max_loras ({self.max_loras})."
            )
        if envs.VLLM_LORA_ENABLE_DUAL_STREAM and not current_platform.is_cuda_alike():
            raise ValueError("Dual CUDA streams are only supported on CUDA platforms.")
        if envs.VLLM_LORA_ENABLE_DUAL_STREAM and self.fully_sharded_loras:
            logger.warning_once(
                "fully_sharded_loras isn't compatible with "
                "VLLM_LORA_ENABLE_DUAL_STREAM, set VLLM_LORA_ENABLE_DUAL_STREAM=False"
            )
            envs.VLLM_LORA_ENABLE_DUAL_STREAM = False
        return self

    defverify_with_model_config(self, model_config: ModelConfig):
        if self.lora_dtype in (None, "auto"):
            self.lora_dtype = model_config.dtype
        elif isinstance(self.lora_dtype, str):
            self.lora_dtype = getattr(torch, self.lora_dtype)
```

### default\_mm\_loras `class-attribute` `instance-attribute` [¶](#vllm.config.lora.LoRAConfig.default_mm_loras "Permanent link")

Dictionary mapping specific modalities to LoRA model paths; this field is only applicable to multimodal models and should be leveraged when a model always expects a LoRA to be active when a given modality is present. Note that currently, if a request provides multiple additional modalities, each of which have their own LoRA, we do NOT apply default\_mm\_loras because we currently only support one lora adapter per prompt. When run in offline mode, the lora IDs for n modalities will be automatically assigned to 1-n with the names of the modalities in alphabetic order.

### enable\_tower\_connector\_lora `class-attribute` `instance-attribute` [¶](#vllm.config.lora.LoRAConfig.enable_tower_connector_lora "Permanent link")

```
enable_tower_connector_lora: bool = False
```

If `True`, LoRA support for the tower (vision encoder) and connector of multimodal models will be enabled. This is an experimental feature and currently only supports some MM models such as the Qwen VL series. The default is False.

### fully\_sharded\_loras `class-attribute` `instance-attribute` [¶](#vllm.config.lora.LoRAConfig.fully_sharded_loras "Permanent link")

```
fully_sharded_loras: bool = False
```

By default, only half of the LoRA computation is sharded with tensor parallelism. Enabling this will use the fully sharded layers. At high sequence length, max rank or tensor parallel size, this is likely faster.

### lora\_dtype `class-attribute` `instance-attribute` [¶](#vllm.config.lora.LoRAConfig.lora_dtype "Permanent link")

```
lora_dtype: dtype | LoRADType = 'auto'
```

Data type for LoRA. If auto, will default to base model dtype.

### max\_cpu\_loras `class-attribute` `instance-attribute` [¶](#vllm.config.lora.LoRAConfig.max_cpu_loras "Permanent link")

```
max_cpu_loras: int | None = None
```

Maximum number of LoRAs to store in CPU memory. Must be &gt;= than `max_loras`.

### max\_lora\_rank `class-attribute` `instance-attribute` [¶](#vllm.config.lora.LoRAConfig.max_lora_rank "Permanent link")

```
max_lora_rank: MaxLoRARanks = 16
```

Max LoRA rank.

### max\_loras `class-attribute` `instance-attribute` [¶](#vllm.config.lora.LoRAConfig.max_loras "Permanent link")

```
max_loras: int = Field(default=1, ge=1)
```

Max number of LoRAs in a single batch.

### specialize\_active\_lora `class-attribute` `instance-attribute` [¶](#vllm.config.lora.LoRAConfig.specialize_active_lora "Permanent link")

```
specialize_active_lora: bool = False
```

Whether to construct lora kernel grid by the number of active LoRA adapters. When set to True, separate cuda graphs will be captured for different counts of active LoRAs (powers of 2 up to max\_loras), which can improve performance for variable LoRA usage patterns at the cost of increased startup time and memory usage. Only takes effect when cudagraph\_specialize\_lora is True.

### target\_modules `class-attribute` `instance-attribute` [¶](#vllm.config.lora.LoRAConfig.target_modules "Permanent link")

```
target_modules: list[str] | None = None
```

Restrict LoRA to specific module suffixes (e.g., \["o\_proj", "qkv\_proj"]). If None, all supported LoRA modules are used. This allows deployment-time control over which modules have LoRA applied, useful for performance tuning.

### compute\_hash [¶](#vllm.config.lora.LoRAConfig.compute_hash "Permanent link")

WARNING: Whenever a new field is added to this config, ensure that it is included in the factors list if it affects the computation graph.

Provide a hash that uniquely identifies all the configs that affect the structure of the computation graph from input ids/embeddings to the final hidden states, excluding anything before input ids/embeddings and after the final hidden states.

Source code in `vllm/config/lora.py`

```
defcompute_hash(self) -> str:
"""
    WARNING: Whenever a new field is added to this config,
    ensure that it is included in the factors list if
    it affects the computation graph.

    Provide a hash that uniquely identifies all the configs
    that affect the structure of the computation
    graph from input ids/embeddings to the final hidden states,
    excluding anything before input ids/embeddings and after
    the final hidden states.
    """
    factors: list[Any] = []
    factors.append(self.max_lora_rank)
    factors.append(self.max_loras)
    factors.append(self.fully_sharded_loras)
    factors.append(self.lora_dtype)
    factors.append(self.enable_tower_connector_lora)
    # target_modules affects which modules get LoRA applied
    factors.append(
        tuple(sorted(self.target_modules)) if self.target_modules else None
    )

    hash_str = safe_hash(str(factors).encode(), usedforsecurity=False).hexdigest()
    return hash_str
```