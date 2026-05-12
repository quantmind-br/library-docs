---
title: row_parallel_linear - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/row_parallel_linear/
source: sitemap
fetched_at: 2026-05-07T21:22:38.214824453-03:00
rendered_js: false
word_count: 0
summary: This document defines a PyTorch layer class that extends row-parallel linear layers with support for sharded LoRA weights, enabling memory-efficient model parallelism for large language models.
tags:
    - pytorch
    - lora
    - model-parallelism
    - tensor-parallelism
    - distributed-training
    - deep-learning
category: concept
---

```
classRowParallelLinearWithShardedLoRA(RowParallelLinearWithLoRA):
"""
    Differs from RowParallelLinearWithLoRA by slicing the
    LoRA B's also.

    Based on S-LoRA, slicing happens along the output dim.
    This yields a combined partial sum from the row parallel base
    layer and column partitioned output from the LoRA.
    """

    defslice_lora_b(self, lora_b: torch.Tensor) -> torch.Tensor:
        shard_size = self.lora_b_stacked[0].shape[2]
        start_idx = self.tp_rank * shard_size
        end_idx = (self.tp_rank + 1) * shard_size
        lora_b = lora_b[start_idx:end_idx, :]
        return lora_b

    defapply(self, x: torch.Tensor, bias: torch.Tensor | None = None) -> torch.Tensor:
        output = self.base_layer.quant_method.apply(self.base_layer, x, bias)

        x = x.view(-1, x.shape[-1])
        output, out_orig_shape = output.view(-1, output.shape[-1]), output.shape
        buffer = torch.zeros(
            (self.n_slices, x.shape[0], self.lora_a_stacked[0].shape[2]),
            dtype=torch.float32,
            device=x.device,
        )

        shrunk_buffer: torch.Tensor | None = self.punica_wrapper.add_shrink(
            buffer, x, self.lora_a_stacked, 1.0
        )
        if not current_platform.can_update_inplace():
            buffer = shrunk_buffer
        if self.tp_size > 1:
            buffer = tensor_model_parallel_all_reduce(buffer)

        # following S-LoRA, allows the fusing of all_gather and all_reduce
        # by adding the column partitioned lora output to a slice of output
        # tensor, which is a partial sum due to row parallel. All that
        # remains is a standard all_reduce. User should be aware though that
        # the output is not the same as a normal row_parallel, it should be
        # reduced before being used
        # NOTE offset are based on the rank.
        shard_size = self.lora_b_stacked[0].shape[2]
        offset_start = self.tp_rank * shard_size
        lora_output: torch.Tensor | None = self.punica_wrapper.add_expand(
            output,
            buffer,
            self.lora_b_stacked,
            self.output_slices,
            offset_start=offset_start,
            add_input=True,
        )

        if not current_platform.can_update_inplace():
            output = lora_output

        output = output.view(*out_orig_shape)
        return output

    @classmethod
    @_fully_sharded_can_replace
    defcan_replace_layer(
        cls,
        source_layer: nn.Module,
        lora_config: LoRAConfig,
        packed_modules_list: list,
        model_config: PretrainedConfig | None = None,
    ) -> bool:
        # specifying kwargs so they can be easily accessed in decorator
        return super().can_replace_layer(
            source_layer=source_layer,
            lora_config=lora_config,
            packed_modules_list=packed_modules_list,
            model_config=model_config,
            decorate=False,
        )
```