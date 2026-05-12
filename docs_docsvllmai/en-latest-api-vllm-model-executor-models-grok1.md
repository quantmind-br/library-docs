---
title: grok1 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/grok1/
source: sitemap
fetched_at: 2026-05-07T21:30:42.794557042-03:00
rendered_js: false
word_count: 0
summary: This document defines the base class architecture for Grok language models within the vLLM framework, providing the structural foundation for model initialization, weight management, and forward pass execution.
tags:
    - grok
    - vllm
    - neural-networks
    - model-architecture
    - pytorch
    - llm-inference
category: reference
---

```
classGrokBaseForCausalLM(nn.Module, SupportsLoRA, SupportsPP):
"""Base class for Grok models with shared logic."""

    fall_back_to_pt_during_load = False

    # Subclasses should override these
    packed_modules_mapping = {
        "qkv_proj": [
            "q_proj",
            "k_proj",
            "v_proj",
        ],
    }

    # Expert weight naming - subclasses override these
    ckpt_gate_proj_name: str = "linear"
    ckpt_down_proj_name: str = "linear_1"
    ckpt_up_proj_name: str = "linear_v"

    defget_weight_name_remapping(self) -> dict[str, str]:
"""Return weight name remapping for this version. Override in subclasses."""
        return {}

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()

        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config

        self.config = config
        self.quant_config = quant_config

        self.model = Grok1Model(
            vllm_config=vllm_config,
            prefix=maybe_prefix(prefix, "model"),
            ckpt_gate_proj_name=self.ckpt_gate_proj_name,
            ckpt_down_proj_name=self.ckpt_down_proj_name,
            ckpt_up_proj_name=self.ckpt_up_proj_name,
            weight_name_remapping=self.get_weight_name_remapping(),
        )

        self.lm_head = ParallelLMHead(
            config.vocab_size,
            config.hidden_size,
            quant_config=quant_config,
            prefix=maybe_prefix(prefix, "lm_head"),
        )

        if self.config.tie_word_embeddings:
            self.lm_head.weight = self.model.embed_tokens.weight

        self.output_multiplier_scale = getattr(
            config, "output_multiplier_scale", DEFAULT_OUTPUT_MULTIPLIER_SCALE
        )
        self.logits_processor = LogitsProcessor(
            config.vocab_size,
            scale=self.output_multiplier_scale,
            soft_cap=getattr(config, "final_logit_softcapping", None),
        )

        self.make_empty_intermediate_tensors = (
            self.model.make_empty_intermediate_tensors
        )

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.model.embed_input_ids(input_ids)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
    ) -> torch.Tensor | IntermediateTensors:
        hidden_states = self.model(
            input_ids, positions, intermediate_tensors, inputs_embeds
        )
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        logits = self.logits_processor(self.lm_head, hidden_states)
        return logits

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        # Skip lm_head when tie_word_embeddings is True
        skip_prefixes = ["lm_head"] if self.config.tie_word_embeddings else None

        loader = AutoWeightsLoader(
            self,
            skip_prefixes=skip_prefixes,
        )
        return loader.load_weights(weights)

    defget_expert_mapping(self) -> list[tuple[str, str, int, str]]:
        return self.model.get_expert_mapping()
```