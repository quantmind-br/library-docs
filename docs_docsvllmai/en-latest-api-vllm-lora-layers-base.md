---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/base/
source: sitemap
fetched_at: 2026-05-07T21:22:32.156836159-03:00
rendered_js: false
word_count: 88
summary: Defines the base class and interface for implementing LoRA (Low-Rank Adaptation) layers within the vLLM framework, providing methods for weight initialization, slicing, and manipulation.
tags:
    - vllm
    - lora
    - layer-management
    - tensor-parallelism
    - machine-learning
    - pytorch
category: api
---

Bases: `Module`

Source code in `vllm/lora/layers/base.py`

```
classBaseLayerWithLoRA(nn.Module):
    @overload
    defslice_lora_a(
        self, lora_a: list[torch.Tensor | None]
    ) -> list[torch.Tensor | None]: ...
    @overload
    defslice_lora_a(self, lora_a: torch.Tensor) -> torch.Tensor: ...
    defslice_lora_a(
        self, lora_a: torch.Tensor | list[torch.Tensor | None]
    ) -> torch.Tensor | list[torch.Tensor | None]:
"""Slice lora a if splitting for tensor parallelism."""
        ...

    @overload
    defslice_lora_b(
        self, lora_b: list[torch.Tensor | None]
    ) -> list[torch.Tensor | None]: ...
    @overload
    defslice_lora_b(self, lora_b: torch.Tensor) -> torch.Tensor: ...
    defslice_lora_b(
        self, lora_b: torch.Tensor | list[torch.Tensor | None]
    ) -> torch.Tensor | list[torch.Tensor | None]:
"""Slice lora b if splitting with tensor parallelism."""
        ...

    defcreate_lora_weights(
        self,
        max_loras: int,
        lora_config: LoRAConfig,
        model_config: PretrainedConfig | None = None,
    ) -> None:
"""Initializes lora matrices."""
        ...

    defreset_lora(self, index: int):
"""Resets the lora weights at index back to 0."""
        ...

    defset_lora(
        self,
        index: int,
        lora_a: torch.Tensor | list[torch.Tensor],
        lora_b: torch.Tensor | list[torch.Tensor],
    ):
"""Overwrites lora tensors at index."""
        ...

    defset_mapping(
        self,
        punica_wrapper,
    ):
        self.punica_wrapper: PunicaWrapperBase = punica_wrapper

    @classmethod
    defcan_replace_layer(
        cls,
        source_layer: nn.Module,
        lora_config: LoRAConfig,
        packed_modules_list: list,
        model_config: PretrainedConfig | None = None,
    ) -> bool:
"""Returns True if the layer can be replaced by this LoRA layer."""
        raise NotImplementedError
```

### can\_replace\_layer `classmethod` [¶](#vllm.lora.layers.base.BaseLayerWithLoRA.can_replace_layer "Permanent link")

```
can_replace_layer(
    source_layer: Module,
    lora_config: LoRAConfig,
    packed_modules_list: list,
    model_config: PretrainedConfig | None = None,
) -> bool
```

Returns True if the layer can be replaced by this LoRA layer.

Source code in `vllm/lora/layers/base.py`

```
@classmethod
defcan_replace_layer(
    cls,
    source_layer: nn.Module,
    lora_config: LoRAConfig,
    packed_modules_list: list,
    model_config: PretrainedConfig | None = None,
) -> bool:
"""Returns True if the layer can be replaced by this LoRA layer."""
    raise NotImplementedError
```

### create\_lora\_weights [¶](#vllm.lora.layers.base.BaseLayerWithLoRA.create_lora_weights "Permanent link")

```
create_lora_weights(
    max_loras: int,
    lora_config: LoRAConfig,
    model_config: PretrainedConfig | None = None,
) -> None
```

Initializes lora matrices.

Source code in `vllm/lora/layers/base.py`

```
defcreate_lora_weights(
    self,
    max_loras: int,
    lora_config: LoRAConfig,
    model_config: PretrainedConfig | None = None,
) -> None:
"""Initializes lora matrices."""
    ...
```

### reset\_lora [¶](#vllm.lora.layers.base.BaseLayerWithLoRA.reset_lora "Permanent link")

Resets the lora weights at index back to 0.

Source code in `vllm/lora/layers/base.py`

```
defreset_lora(self, index: int):
"""Resets the lora weights at index back to 0."""
    ...
```

### set\_lora [¶](#vllm.lora.layers.base.BaseLayerWithLoRA.set_lora "Permanent link")

Overwrites lora tensors at index.

Source code in `vllm/lora/layers/base.py`

```
defset_lora(
    self,
    index: int,
    lora_a: torch.Tensor | list[torch.Tensor],
    lora_b: torch.Tensor | list[torch.Tensor],
):
"""Overwrites lora tensors at index."""
    ...
```

### slice\_lora\_a [¶](#vllm.lora.layers.base.BaseLayerWithLoRA.slice_lora_a "Permanent link")

Slice lora a if splitting for tensor parallelism.

Source code in `vllm/lora/layers/base.py`

```
defslice_lora_a(
    self, lora_a: torch.Tensor | list[torch.Tensor | None]
) -> torch.Tensor | list[torch.Tensor | None]:
"""Slice lora a if splitting for tensor parallelism."""
    ...
```

### slice\_lora\_b [¶](#vllm.lora.layers.base.BaseLayerWithLoRA.slice_lora_b "Permanent link")

Slice lora b if splitting with tensor parallelism.

Source code in `vllm/lora/layers/base.py`

```
defslice_lora_b(
    self, lora_b: torch.Tensor | list[torch.Tensor | None]
) -> torch.Tensor | list[torch.Tensor | None]:
"""Slice lora b if splitting with tensor parallelism."""
    ...
```