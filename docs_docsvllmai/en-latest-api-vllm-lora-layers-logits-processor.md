---
title: logits_processor - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/lora/layers/logits_processor/
source: sitemap
fetched_at: 2026-05-07T21:22:36.003175226-03:00
rendered_js: false
word_count: 0
summary: This document defines a LoRA-enabled LogitsProcessor wrapper class that manages the application of LoRA adapters to model logit outputs, including support for vocabulary mapping and parallel processing.
tags:
    - lora
    - logits-processor
    - machine-learning
    - tensor-parallelism
    - adapter-tuning
    - pytorch
category: api
---

```
classLogitsProcessorWithLoRA(BaseLayerWithLoRA):
"""
    LoRA wrapper for LogitsProcessor, with extra logic to handle the
    application of the LoRA adapter and added LoRA vocabulary.

    Args:
        base_layer: LogitsProcessor layer
        hidden_size: hidden size of the model
        dtype: data type of the model
        device: device of the model
        sharded_to_full_mapping: index mapping from sharded vocab to full vocab
            received from base_layer.get_sharded_to_full_mapping(). If None,
            no reindexing will be done.
    """

    def__init__(
        self,
        base_layer: LogitsProcessor,
        hidden_size: int,
        dtype: torch.dtype,
        device: torch.device,
        sharded_to_full_mapping: list[int] | None,
    ) -> None:
        super().__init__()
        self.base_layer = base_layer
        self.hidden_size = hidden_size
        self.dtype = dtype
        self.device = device
        self.tp_size = get_tensor_model_parallel_world_size()
        self.tp_rank = get_tensor_model_parallel_rank()
        self.sharded_to_full_mapping = sharded_to_full_mapping

    @property
    deflogits_as_input(self):
        return self.base_layer.logits_as_input

    @property
    defvocab_size(self):
        return self.base_layer.vocab_size

    @property
    defscale(self):
        return self.base_layer.scale

    @property
    defsoft_cap(self):
        return self.base_layer.soft_cap

    @property
    defuse_all_gather(self):
        return self.base_layer.use_all_gather

    @property
    deforg_vocab_size(self):
        return self.base_layer.org_vocab_size

    @property
    definclude_gpu_probs_tensor(self):
        return self.base_layer.include_gpu_probs_tensor

    @property
    defshould_modify_greedy_probs_inplace(self):
        return self.base_layer.should_modify_greedy_probs_inplace

    defcreate_lora_weights(
        self,
        max_loras: int,
        lora_config: LoRAConfig,
        model_config: PretrainedConfig | None = None,
    ) -> None:
        # TODO: Verify if this condition can be further relaxed
        if self.base_layer.vocab_size > 258048:
            raise ValueError("When using LoRA, vocab size must be <= 258048")
        self.lora_a_stacked = torch.zeros(
            (
                max_loras,
                1,
                lora_config.max_lora_rank,
                self.hidden_size,
            ),
            dtype=lora_config.lora_dtype,
            device=self.device,
        )
        self.lora_b_stacked = torch.zeros(
            (
                max_loras,
                1,
                self.base_layer.vocab_size,
                lora_config.max_lora_rank,
            ),
            dtype=lora_config.lora_dtype,
            device=self.device,
        )

        if self.sharded_to_full_mapping is not None:
            self.sharded_to_full_mapping_gpu = torch.tensor(
                self.sharded_to_full_mapping, device=self.device, dtype=torch.long
            )
        else:
            self.sharded_to_full_mapping_gpu = None

    defreset_lora(self, index: int):
        self.lora_a_stacked[index] = 0
        self.lora_b_stacked[index] = 0

    defset_lora(
        self,
        index: int,
        lora_a: torch.Tensor | list[torch.Tensor],
        lora_b: torch.Tensor | list[torch.Tensor],
    ):
        assert isinstance(lora_a, torch.Tensor)
        assert isinstance(lora_b, torch.Tensor)
        self.reset_lora(index)
        self.lora_a_stacked[index, 0, : lora_a.shape[0], : lora_a.shape[1]].copy_(
            lora_a, non_blocking=True
        )
        self.lora_b_stacked[index, 0, : lora_b.shape[0], : lora_b.shape[1]].copy_(
            lora_b, non_blocking=True
        )

    def_get_logits(
        self,
        hidden_states: torch.Tensor,
        lm_head: VocabParallelEmbedding,
        embedding_bias: torch.Tensor | None = None,
    ) -> torch.Tensor | None:
        # Get the logits for the next tokens.
        if hasattr(lm_head, "base_layer"):
            actual_lm_head = lm_head.base_layer
        else:
            actual_lm_head = lm_head
        logits = actual_lm_head.quant_method.apply(actual_lm_head, hidden_states)
        if embedding_bias is not None:
            logits += embedding_bias

        # Gather logits for TP
        logits = self.base_layer._gather_logits(logits)

        if logits is None:
            return None

        if self.sharded_to_full_mapping_gpu is not None:
            # Reindex full logits tensor to ensure 1:1 mapping between
            # index and token_id
            # Example for:
            #   org_vocab_size = 4
            #   added_vocab_size = 2
            #   pad_to_size = 8
            #   tp_size = 2

            # indices:  [0, 1, 2,  3, 4, 5, 6,  7]
            # token_id: [0, 1, 4, -1, 2, 3, 5, -1]

            # Therefore, the mapping is expected to be:
            # [0, 1, 4, 6, 2, 3, 5, 7] so that when we reindex,
            # we get:
            # indices:  [0, 1, 2, 3, 4, 5,  6,  7]
            # token_id: [0, 1, 2, 3, 4, 5, -1, -1]
            logits = logits[:, self.sharded_to_full_mapping_gpu]

        lora_output: torch.Tensor | None = self.punica_wrapper.add_lora_logits(
            logits, hidden_states, self.lora_a_stacked, self.lora_b_stacked, 1.0
        )

        if not current_platform.can_update_inplace():
            logits = lora_output

        # Remove paddings in vocab (if any).
        logits = logits[:, : self.base_layer.vocab_size]
        return logits

    defforward(self, *args, **kwargs):
        return type(self.base_layer).forward(self, *args, **kwargs)

    @classmethod
    defcan_replace_layer(
        cls,
        source_layer: nn.Module,
        lora_config: LoRAConfig,
        packed_modules_list: list,
        model_config: PretrainedConfig | None = None,
    ) -> bool:
        # Special handling for the LogitsProcessor.
        return False
```