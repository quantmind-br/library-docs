---
title: llama4_eagle - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/llama4_eagle/
source: sitemap
fetched_at: 2026-05-07T21:31:28.056534441-03:00
rendered_js: false
word_count: 0
summary: This document defines the EagleLlama4ForCausalLM class, which implements a draft model architecture for speculative decoding within the vLLM framework.
tags:
    - vllm
    - speculative-decoding
    - causal-language-model
    - model-architecture
    - pytorch
category: concept
---

```
classEagleLlama4ForCausalLM(Llama4ForCausalLM):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        nn.Module.__init__(self)
        self.config = vllm_config.speculative_config.draft_model_config.hf_config
        target_layer_num = vllm_config.model_config.get_num_layers(
            vllm_config.parallel_config
        )
        # draft model quantization config may differ from target model
        quant_config = VllmConfig.get_quantization_config(
            vllm_config.speculative_config.draft_model_config, vllm_config.load_config
        )
        self.model = LlamaModel(
            vllm_config=vllm_config,
            prefix="model",
            start_layer_id=target_layer_num,
            quant_config=quant_config,
        )
        logit_scale = getattr(self.config, "logit_scale", 1.0)
        self.logits_processor = LogitsProcessor(
            self.config.vocab_size, scale=logit_scale
        )

        self.lm_head = ParallelLMHead(
            self.config.draft_vocab_size,
            self.config.hidden_size,
            prefix=maybe_prefix(prefix, "lm_head"),
        )

        # Set MoE hyperparameters
        self.set_moe_parameters()

    defget_language_model(self) -> torch.nn.Module:
        return self.model

    embed_input_ids = SupportsMultiModal.embed_input_ids  # type: ignore

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
        inputs_embeds: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        return self.model(input_ids, positions, hidden_states, inputs_embeds)

    defget_top_tokens(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor:
"""Vocab-parallel argmax without all-gathering full logits.

        Falls back to full logits when draft_id_to_target_id remapping is
        active, since the shared lm_head covers the full target vocab but
        the draft model only predicts over a subset (draft_vocab_size).
        """
        if (
            hasattr(self, "draft_id_to_target_id")
            and self.draft_id_to_target_id is not None
        ):
            return self.compute_logits(hidden_states).argmax(dim=-1)
        return self.logits_processor.get_top_tokens(self.lm_head, hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> None:
        deftransform(inputs):
            name, loaded_weight = inputs
            name, weight = self.permute_qk_weight_for_rotary(name, loaded_weight)
            if "lm_head" not in name:
                name = "model." + name
            process_eagle_weight(self, name)
            return name, weight

        loader = AutoWeightsLoader(
            self,
            # lm_head is tied with target model (Llama4ForCausalLM)
            skip_prefixes=([]),
        )
        loader.load_weights(map(transform, weights))
```