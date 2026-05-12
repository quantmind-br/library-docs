---
title: nemotron_h - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/nemotron_h/
source: sitemap
fetched_at: 2026-05-07T21:32:13.933220348-03:00
rendered_js: false
word_count: 14
summary: This document defines the NemotronHModel class in a PyTorch framework, focusing on implementing a heterogeneous transformer architecture that supports mixed-layer types and MoE (Mixture of Experts) configurations.
tags:
    - pytorch
    - deep-learning
    - transformer-architecture
    - mixture-of-experts
    - model-loading
    - vllm
category: api
---

```
@support_torch_compile
classNemotronHModel(nn.Module):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()

        config: NemotronHConfig = vllm_config.model_config.hf_config
        model_config = vllm_config.model_config
        cache_config = vllm_config.cache_config
        quant_config = vllm_config.quant_config
        parallel_config = vllm_config.parallel_config

        self.config = config

        self.vocab_size = config.vocab_size

        self.embed_tokens = VocabParallelEmbedding(
            self.vocab_size,
            config.hidden_size,
        )

        self.has_moe = "E" in config.hybrid_override_pattern

        defget_layer(prefix: str):
            layer_idx = int(prefix.rsplit(".", 1)[1])
            layer_class = ALL_DECODER_LAYER_TYPES[
                config.hybrid_override_pattern[layer_idx]
            ]
            return layer_class(
                config=config,
                layer_idx=layer_idx,
                model_config=model_config,
                cache_config=cache_config,
                quant_config=quant_config,
                parallel_config=parallel_config,
                prefix=prefix,
            )

        self.start_layer, self.end_layer, self.layers = make_layers(
            len(config.hybrid_override_pattern), get_layer, prefix=f"{prefix}.layers"
        )
        self.make_empty_intermediate_tensors = make_empty_intermediate_tensors_factory(
            ["hidden_states", "residual"], config.hidden_size
        )

        self.norm_f = RMSNorm(config.hidden_size, eps=config.layer_norm_epsilon)

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.embed_tokens(input_ids)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
    ) -> torch.Tensor | IntermediateTensors:
        if get_pp_group().is_first_rank:
            if inputs_embeds is not None:
                hidden_states = inputs_embeds
            else:
                hidden_states = self.embed_input_ids(input_ids)
            residual = None
        else:
            assert intermediate_tensors is not None
            hidden_states = intermediate_tensors["hidden_states"]
            residual = intermediate_tensors["residual"]

        for layer in islice(self.layers, self.start_layer, self.end_layer):
            hidden_states, residual = layer(
                positions=positions,
                hidden_states=hidden_states,
                residual=residual,
            )

        if not get_pp_group().is_last_rank:
            return IntermediateTensors(
                {"hidden_states": hidden_states, "residual": residual}
            )
        hidden_states, _ = self.norm_f(hidden_states, residual)
        return hidden_states

    defis_spec_layer(self, config: NemotronHConfig, weight_name: str) -> bool:
        return weight_name.startswith("mtp.")

    def_get_max_n_routed_experts(self) -> int:
"""Get max n_routed_experts from config or block_configs for puzzle models.

        For heterogeneous models with varying expert counts per layer,
        returns the MAX to ensure all expert weights can be loaded.
        """
        # First try top-level attribute
        n_routed_experts = getattr(self.config, "n_routed_experts", None)
        if n_routed_experts is not None:
            return n_routed_experts

        # For puzzle models, get MAX from all MoE blocks in block_configs
        # (different layers may have different expert counts)
        max_experts = 0
        block_configs = getattr(self.config, "block_configs", None)
        if block_configs:
            for block in block_configs:
                if isinstance(block, dict):
                    if block.get("block_type") == "moe":
                        max_experts = max(max_experts, block.get("n_routed_experts", 0))
                else:
                    # HF converts dicts to objects with attributes
                    if getattr(block, "block_type", "") == "moe":
                        max_experts = max(
                            max_experts, getattr(block, "n_routed_experts", 0)
                        )
        return max_experts

    defget_expert_mapping(self) -> list[tuple[str, str, int, str]]:
        if self.has_moe:
            # (param_name, weight_name, expert_id, shard_id)
            expert_params_mapping = fused_moe_make_expert_params_mapping(
                # - FusedMoe.w1 (aka gate_proj) should be up_proj since that's
                #   what the activation is applied to
                # - FusedMoe.w3 (aka up_proj) should be ignored since we're
                #   using non-gated MoE
                self,
                ckpt_gate_proj_name="up_proj",
                ckpt_down_proj_name="down_proj",
                ckpt_up_proj_name="",
                num_experts=self._get_max_n_routed_experts(),
                num_redundant_experts=getattr(self, "num_redundant_experts", 0),
            )
            return expert_params_mapping

        return []

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        stacked_params_mapping = [
            # (param_name, shard_name, shard_id)
            ("qkv_proj", "q_proj", "q"),
            ("qkv_proj", "k_proj", "k"),
            ("qkv_proj", "v_proj", "v"),
        ]

        expert_params_mapping = self.get_expert_mapping()

        params_dict = dict(self.named_parameters())
        loaded_params: set[str] = set()
        for name, loaded_weight in weights:
            if "scale" in name or "zero_point" in name:
                # Remapping the name of FP8 kv-scale.
                name = maybe_remap_kv_scale_name(name, params_dict)
                if name is None:
                    continue

            # Skip MTP/spec decode layers early (before stacked params mapping)
            if name.startswith("mtp."):
                continue

            # load stacked params
            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name:
                    continue
                name = name.replace(weight_name, param_name)
                # Skip loading extra bias for GPTQ models.
                if name.endswith(".bias") and name not in params_dict:
                    continue

                if is_pp_missing_parameter(name, self):
                    continue

                param = params_dict[name]
                weight_loader = param.weight_loader
                weight_loader(param, loaded_weight, shard_id)
                break

            # load other params
            else:
                is_expert_weight = False
                for mapping in expert_params_mapping:
                    param_name, weight_name, expert_id, shard_id = mapping
                    if weight_name not in name:
                        continue

                    # Anyway, this is an expert weight and should not be
                    # attempted to load as other weights later
                    is_expert_weight = True

                    # Do not modify `name` since the loop may continue here
                    # Instead, create a new variable
                    name_mapped = name.replace(weight_name, param_name)

                    if is_pp_missing_parameter(name_mapped, self):
                        continue
                    param = params_dict[name_mapped]
                    # We should ask the weight loader to return success or not
                    # here since otherwise we may skip experts with other
                    # available replicas.
                    weight_loader = typing.cast(
                        Callable[..., bool], param.weight_loader
                    )
                    success = weight_loader(
                        param,
                        loaded_weight,
                        name_mapped,
                        shard_id=shard_id,
                        expert_id=expert_id,
                        return_success=True,
                    )
                    if success:
                        name = name_mapped
                        break
                else:
                    if is_expert_weight:
                        continue

                    if is_pp_missing_parameter(name, self):
                        continue

                    param = params_dict[name]
                    weight_loader = getattr(
                        param, "weight_loader", default_weight_loader
                    )
                    weight_loader(param, loaded_weight)

            loaded_params.add(name)
        return loaded_params
```