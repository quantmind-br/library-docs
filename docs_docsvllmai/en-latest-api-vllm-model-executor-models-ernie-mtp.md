---
title: ernie_mtp - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/ernie_mtp/
source: sitemap
fetched_at: 2026-05-07T21:29:51.903291855-03:00
rendered_js: false
word_count: 0
summary: This document defines the ErnieMTP PyTorch module, detailing its architecture, forward pass logic, and specific weight loading mechanisms for the Multi-Token Predictor implementation.
tags:
    - pytorch
    - neural-networks
    - model-architecture
    - weight-loading
    - deep-learning
    - vllm
category: reference
---

```
classErnieMTP(nn.Module):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()

        self.config = vllm_config.model_config.hf_config
        self.model = ErnieMultiTokenPredictor(
            vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
        )
        self.lm_head = ParallelLMHead(
            self.config.vocab_size,
            self.config.hidden_size,
            prefix=maybe_prefix(prefix, "lm_head"),
        )

        if self.config.tie_word_embeddings:
            self.lm_head.weight = self.model.embed_tokens.weight

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.model.embed_input_ids(input_ids)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        spec_step_idx: int = 0,
    ) -> torch.Tensor:
        assert spec_step_idx == 0, "ernie_mtp only support predict one token"
        hidden_states = self.model(
            input_ids, positions, hidden_states, inputs_embeds, spec_step_idx
        )
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
        spec_step_idx: int = 0,
    ) -> torch.Tensor | None:
        return self.model.compute_logits(hidden_states, self.lm_head, spec_step_idx)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        stacked_params_mapping = [
            ("qkv_proj", "q_proj", "q"),
            ("qkv_proj", "k_proj", "k"),
            ("qkv_proj", "v_proj", "v"),
            ("gate_up_proj", "gate_proj", 0),
            ("gate_up_proj", "up_proj", 1),
        ]

        params_dict = dict(self.named_parameters())
        loaded_params: set[str] = set()
        for name, loaded_weight in weights:
            if self.config.tie_word_embeddings and name.endswith("lm_head.weight"):
                continue
            if "rotary_emb.inv_freq" in name:
                continue
            if "mtp" in name:
                name = self._rewrite_spec_layer_name(self.config, name)

            for param_name, weight_name, shard_id in stacked_params_mapping:
                # Skip non-stacked layers and experts (experts handled below).
                if weight_name not in name:
                    continue
                if "mtp" not in name:
                    continue
                # We have mlp.experts[0].gate_proj in the checkpoint.
                # Since we handle the experts below in expert_params_mapping,
                # we need to skip here BEFORE we update the name, otherwise
                # name will be updated to mlp.experts[0].gate_up_proj, which
                # will then be updated below in expert_params_mapping
                # for mlp.experts[0].gate_gate_up_proj, which breaks load.
                if ("mlp.experts." in name) and name not in params_dict:
                    continue
                name = name.replace(weight_name, param_name)
                # Skip loading extra bias for GPTQ models.
                if (
                    name.endswith(".bias") or name.endswith("_bias")
                ) and name not in params_dict:
                    continue
                # Skip layers on other devices.
                if is_pp_missing_parameter(name, self):
                    continue

                param = params_dict[name]
                weight_loader = param.weight_loader
                weight_loader(param, loaded_weight, shard_id)
                break
            else:
                # Skip loading extra bias for GPTQ models.
                if (
                    name.endswith(".bias") or name.endswith("_bias")
                ) and name not in params_dict:
                    continue
                # Skip layers on other devices.
                if is_pp_missing_parameter(name, self):
                    continue

                # According to DeepSeek-V3 Technical Report, MTP modules
                # shares embedding layer. We only load the first weights.
                if "mtp_" not in name and (
                    "embed_tokens" not in name and "lm_head" not in name
                ):
                    continue

                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                weight_loader(param, loaded_weight)
            loaded_params.add(name)
        return loaded_params

    def_rewrite_spec_layer_name(self, config: PretrainedConfig, name: str) -> str:
"""
        Rewrite the weight name to match the format of the original model.
        """
        spec_layer_weight_names = [
            "embed_tokens",
            "mtp_emb_norm",
            "mtp_hidden_norm",
            "mtp_linear_proj",
        ]
        layer_idx = config.num_hidden_layers
        for weight_name in spec_layer_weight_names:
            if weight_name in name:
                name = name.replace(
                    f"model.{weight_name}.0.",
                    f"model.layers.{layer_idx}.{weight_name}.",
                )
                return name
        name = name.replace(
            "model.mtp_block.0.", f"model.layers.{layer_idx}.mtp_block."
        )
        return name
```