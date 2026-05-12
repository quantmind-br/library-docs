---
title: replicated_linear - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/replicated_linear/
source: sitemap
fetched_at: 2026-05-07T21:22:37.206169695-03:00
rendered_js: false
word_count: 110
summary: This document defines the ReplicatedLinearWithLoRA class, which extends base linear layers in vLLM to support LoRA adapters for replicated linear layers.
tags:
    - vllm
    - lora
    - linear-layers
    - tensor-parallelism
    - machine-learning
    - model-optimization
category: reference
---

Bases: `BaseLinearLayerWithLoRA`

Source code in `vllm/lora/layers/replicated_linear.py`

```
classReplicatedLinearWithLoRA(BaseLinearLayerWithLoRA):
    def__init__(self, base_layer: ReplicatedLinear) -> None:
        super().__init__(
            base_layer,
        )
        # To ensure interface compatibility, set to 1 always.
        self.output_size = self.base_layer.output_size
        self.n_slices = 1

    defforward(
        self, input_: torch.Tensor
    ) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor | None]:
"""Forward of ReplicatedLinearWithLoRA

        Args:
            input_: Tensor whose last dimension is `input_size`.

        Returns:
            - output
            - bias
        """
        bias = self.base_layer.bias if not self.base_layer.skip_bias_add else None

        # Matrix multiply.
        output = self.apply(input_, bias)

        output_bias = self.base_layer.bias if self.base_layer.skip_bias_add else None

        if not self.base_layer.return_bias:
            return output

        return output, output_bias

    defapply(self, x: torch.Tensor, bias: torch.Tensor | None = None) -> torch.Tensor:
        # ReplicatedLinear subclasses such as GateLinear override forward() to
        # dispatch custom kernels and/or adjust the output dtype. Apply LoRA on
        # top of the actual base-layer output instead of bypassing that path.
        return self._apply_base_forward(x)

    # ReplicatedLinear should always be replaced, regardless of the fully
    # sharded LoRAs setting, because it is, by definition, copied per GPU.
    @classmethod
    defcan_replace_layer(
        cls,
        source_layer: nn.Module,
        lora_config: LoRAConfig,
        packed_modules_list: list,
        model_config: PretrainedConfig | None = None,
    ) -> bool:
        return isinstance(source_layer, maybe_get_oot_by_class(ReplicatedLinear))

    defslice_lora_a(
        self, lora_a: torch.Tensor | list[torch.Tensor | None]
    ) -> torch.Tensor | list[torch.Tensor | None]:
"""Slice lora a if splitting for tensor parallelism."""
        return lora_a

    defslice_lora_b(
        self, lora_b: torch.Tensor | list[torch.Tensor | None]
    ) -> torch.Tensor | list[torch.Tensor | None]:
"""Slice lora b if splitting with tensor parallelism."""
        return lora_b
```

### forward [¶](#vllm.lora.layers.replicated_linear.ReplicatedLinearWithLoRA.forward "Permanent link")

Forward of ReplicatedLinearWithLoRA

Parameters:

Name Type Description Default `input_` `Tensor`

Tensor whose last dimension is `input_size`.

*required*

Returns:

Type Description `Tensor | tuple[Tensor, Tensor | None]`

- output

`Tensor | tuple[Tensor, Tensor | None]`

- bias

Source code in `vllm/lora/layers/replicated_linear.py`

```
defforward(
    self, input_: torch.Tensor
) -> torch.Tensor | tuple[torch.Tensor, torch.Tensor | None]:
"""Forward of ReplicatedLinearWithLoRA

    Args:
        input_: Tensor whose last dimension is `input_size`.

    Returns:
        - output
        - bias
    """
    bias = self.base_layer.bias if not self.base_layer.skip_bias_add else None

    # Matrix multiply.
    output = self.apply(input_, bias)

    output_bias = self.base_layer.bias if self.base_layer.skip_bias_add else None

    if not self.base_layer.return_bias:
        return output

    return output, output_bias
```

### slice\_lora\_a [¶](#vllm.lora.layers.replicated_linear.ReplicatedLinearWithLoRA.slice_lora_a "Permanent link")

Slice lora a if splitting for tensor parallelism.

Source code in `vllm/lora/layers/replicated_linear.py`

```
defslice_lora_a(
    self, lora_a: torch.Tensor | list[torch.Tensor | None]
) -> torch.Tensor | list[torch.Tensor | None]:
"""Slice lora a if splitting for tensor parallelism."""
    return lora_a
```

### slice\_lora\_b [¶](#vllm.lora.layers.replicated_linear.ReplicatedLinearWithLoRA.slice_lora_b "Permanent link")

Slice lora b if splitting with tensor parallelism.

Source code in `vllm/lora/layers/replicated_linear.py`

```
defslice_lora_b(
    self, lora_b: torch.Tensor | list[torch.Tensor | None]
) -> torch.Tensor | list[torch.Tensor | None]:
"""Slice lora b if splitting with tensor parallelism."""
    return lora_b
```