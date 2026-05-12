---
title: mimo_mtp - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/mimo_mtp/
source: sitemap
fetched_at: 2026-05-07T21:31:40.892375438-03:00
rendered_js: false
word_count: 0
summary: This document defines the MiMoMTP class, a PyTorch module implementation designed to facilitate multi-token prediction within a VLLM framework, including specialized logic for weight loading and parameter mapping.
tags:
    - deep-learning
    - vllm
    - pytorch
    - multi-token-prediction
    - weight-loading
    - neural-network-architecture
category: api
---

```
classMiMoMTP(nn.Module):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        self.config = vllm_config.model_config.hf_config
        self.model = MiMoMultiTokenPredictor(
            vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
        )
        self.lm_head = ParallelLMHead(
            self.config.vocab_size,
            self.config.hidden_size,
            prefix=maybe_prefix(prefix, "lm_head"),
        )

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
        assert spec_step_idx == 0, "mimo_mtp only support predict one token now"
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
            if "rotary_emb.inv_freq" in name:
                continue
            name = self.map_model_name_to_mtp_param_name(name)

            for param_name, weight_name, shard_id in stacked_params_mapping:
                # Skip non-stacked layers and experts (experts handled below).
                if weight_name not in name:
                    continue
                if "mtp_layers" not in name:
                    break
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
                if name.endswith(".bias") and name not in params_dict:
                    continue

                param = params_dict[name]
                weight_loader = param.weight_loader
                weight_loader(param, loaded_weight, shard_id)
                break
            else:
                # Skip loading extra bias for GPTQ models.
                if name.endswith(".bias") and name not in params_dict:
                    continue
                if "mtp_layers" not in name and (
                    "embed_tokens" not in name and "lm_head" not in name
                ):
                    continue
                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                weight_loader(param, loaded_weight)
            loaded_params.add(name)
        return loaded_params

    defmap_model_name_to_mtp_param_name(self, name: str) -> str:
        importregexasre

        # append mtp_start_layer_idx
        pattern = r"(model\.mtp_layers\.)(\d+)(\.)"
        match = re.match(pattern, name)
        if match:
            original_num = int(match.group(2))
            new_num = original_num + self.config.num_hidden_layers
            name = name.replace(match.group(), f"{match.group(1)}{new_num}.")
        # check for early turn
        name_without_prefix = [
            "token_layernorm",
            "hidden_layernorm",
            "input_proj",
            "final_layernorm",
        ]
        for sub_name in name_without_prefix:
            if sub_name in name:
                return name
        # add mtp_block
        pattern = r"(model\.mtp_layers\.\d+\.)"
        match = re.match(pattern, name)
        if match:
            name = name.replace(match.group(), match.group() + "mtp_block.")
        return name

    def_rewrite_spec_layer_name(self, spec_layer: int, name: str) -> str:
"""
        Rewrite the weight name to match the format of the original model.
        Add .mtp_block for modules in transformer layer block for spec layer
        """
        spec_layer_weight_names = [
            "embed_tokens",
            "enorm",
            "hnorm",
            "eh_proj",
            "shared_head",
        ]
        spec_layer_weight = False
        for weight_name in spec_layer_weight_names:
            if weight_name in name:
                spec_layer_weight = True
                break
        if not spec_layer_weight:
            # treat rest weights as weights for transformer layer block
            name = name.replace(
                f"model.layers.{spec_layer}.", f"model.layers.{spec_layer}.mtp_block."
            )
        return name
```