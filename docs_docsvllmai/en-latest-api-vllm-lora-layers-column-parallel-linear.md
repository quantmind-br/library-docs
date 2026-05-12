---
title: column_parallel_linear - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/column_parallel_linear/
source: sitemap
fetched_at: 2026-05-07T21:22:34.398808103-03:00
rendered_js: false
word_count: 0
summary: This document defines a merged column parallel linear layer implementation with LoRA support, facilitating the handling of multiple packed sublayers and their corresponding low-rank adaptation weights within a parallelized training framework.
tags:
    - pytorch
    - lora
    - tensor-parallelism
    - neural-network-layers
    - model-parallelism
    - deep-learning
category: api
---

```
classMergedColumnParallelLinearWithLoRA(ColumnParallelLinearWithLoRA):
"""ColumnParallelLinear layer that is composed of 2 sublayers (slices)
    packed together (e.g. gate_proj + up_proj -> gate_up_proj).

    This means we have 2 LoRAs, each applied to one half of the layer.

    Both slices must have the same size.
    """

    def__init__(
        self, base_layer: MergedColumnParallelLinear | QKVParallelLinear
    ) -> None:
        super().__init__(base_layer)
        # There are two LoRA layers
        # the output_sizes in MergedColumnParallelLinear is not sharded by tp
        # we need to divide it by the tp_size to get correct slices size
        output_sizes = self.base_layer.output_sizes
        self.output_slices = tuple(
            divide(output_size, self.tp_size) for output_size in output_sizes
        )
        self.n_slices = len(self.output_slices)
        self.output_ids = (self.tp_rank,) * self.n_slices

    defcreate_lora_weights(
        self,
        max_loras: int,
        lora_config: LoRAConfig,
        model_config: PretrainedConfig | None = None,
    ) -> None:
"""
        The main reason for overriding this function is to enhance  code
        maintainability.
        """
        self.lora_config = lora_config

        lora_a_output_size_per_partition = (
            lora_config.max_lora_rank
            if not lora_config.fully_sharded_loras
            else divide(lora_config.max_lora_rank, self.tp_size)
        )

        self.lora_a_stacked = tuple(
            torch.zeros(
                max_loras,
                1,
                lora_a_output_size_per_partition,
                self.input_size,
                dtype=lora_config.lora_dtype,
                device=self.device,
            )
            for _ in range(self.n_slices)
        )
        self.lora_b_stacked = tuple(
            torch.zeros(
                max_loras,
                1,
                output_size,
                lora_config.max_lora_rank,
                dtype=lora_config.lora_dtype,
                device=self.device,
            )
            for output_size in self.output_slices
        )

    defslice_lora_a(
        self, lora_a: list[torch.Tensor | None]
    ) -> list[torch.Tensor | None]:
        return lora_a

    defslice_lora_b(
        self, lora_b: list[torch.Tensor | None]
    ) -> list[torch.Tensor | None]:
        sliced_lora_b = [None] * self.n_slices
        for i, (shard_id, shard_size) in enumerate(
            zip(self.output_ids, self.output_slices)
        ):
            if (lora_b_i := lora_b[i]) is not None:
                sliced_lora_b[i] = lora_b_i[
                    shard_size * shard_id : shard_size * (shard_id + 1), :
                ]
        return sliced_lora_b

    defset_lora(
        self,
        index: int,
        lora_a: torch.Tensor | list[torch.Tensor],
        lora_b: torch.Tensor | list[torch.Tensor],
    ):
        self.reset_lora(index)

        if self.tp_size > 1:
            lora_a = self.slice_lora_a(lora_a)
            lora_b = self.slice_lora_b(lora_b)

        for i in range(self.n_slices):
            if (lora_a_i := lora_a[i]) is not None:
                self.lora_a_stacked[i][
                    index, 0, : lora_a_i.shape[0], : lora_a_i.shape[1]
                ].copy_(lora_a_i, non_blocking=True)
            if (lora_b_i := lora_b[i]) is not None:
                self.lora_b_stacked[i][
                    index, 0, : lora_b_i.shape[0], : lora_b_i.shape[1]
                ].copy_(lora_b_i, non_blocking=True)

    defapply(self, x: torch.Tensor, bias: torch.Tensor | None = None) -> torch.Tensor:
        merged_cls = maybe_get_oot_by_class(MergedColumnParallelLinear)
        # Effectively unsharded subclasses can safely reuse their custom
        # forward() implementation before applying the LoRA delta.
        if (
            self.tp_size == 1
            and type(self.base_layer) is not merged_cls
            and type(self.base_layer).forward is not merged_cls.forward
        ):
            return self._apply_base_forward(x)
        return _mcp_apply(x, bias, self)

    @classmethod
    defcan_replace_layer(
        cls,
        source_layer: nn.Module,
        lora_config: LoRAConfig,
        packed_modules_list: list,
        model_config: PretrainedConfig | None = None,
        decorate: bool = True,
    ) -> bool:
        merged_cls = maybe_get_oot_by_class(MergedColumnParallelLinear)
        if not isinstance(source_layer, merged_cls) or len(packed_modules_list) != 2:
            return False

        tp_size = getattr(source_layer, "tp_size", 1)
        if type(source_layer) is merged_cls:
            if not decorate:
                return True
            return not lora_config.fully_sharded_loras or tp_size == 1

        # Only support effectively unsharded subclasses here. Sharded
        # subclasses may have custom communication semantics that the generic
        # merged-column LoRA path does not know how to preserve.
        return tp_size == 1
```