---
title: laguna - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/laguna/
source: sitemap
fetched_at: 2026-05-07T21:31:18.785497088-03:00
rendered_js: false
word_count: 12
summary: This code implements the Laguna model architecture within a PyTorch-based framework, including model initialization, forward pass logic, and weight loading mechanisms for pipeline parallelism and expert routing.
tags:
    - vllm
    - pytorch
    - model-architecture
    - pipeline-parallelism
    - expert-routing
    - weight-loading
category: reference
---

```
@support_torch_compile
classLagunaModel(nn.Module, EagleModelMixin):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()

        config = vllm_config.model_config.hf_config
        cache_config = vllm_config.cache_config
        quant_config = vllm_config.quant_config
        enable_eplb = vllm_config.parallel_config.enable_eplb
        eplb_config = vllm_config.parallel_config.eplb_config
        self.num_redundant_experts = eplb_config.num_redundant_experts
        self.config = config
        self.quant_config = quant_config

        # Disable the model-level sliding-window fallback in Attention.__init__.
        # Laguna drives SWA per-layer via `layer_types`, passing
        # `per_layer_sliding_window=self.sliding_window` (None for global
        # layers). Without this, global layers whose `per_layer_sliding_window`
        # is None would pick up `cache_config.sliding_window`
        # (populated from `config.sliding_window`) as a fallback, silently
        # applying a 512-token window to full-attention layers.
        if cache_config is not None:
            cache_config.sliding_window = None

        self.vocab_size = config.vocab_size

        if get_pp_group().is_first_rank or (
            config.tie_word_embeddings and get_pp_group().is_last_rank
        ):
            self.embed_tokens = VocabParallelEmbedding(
                config.vocab_size,
                config.hidden_size,
                quant_config=quant_config,
                prefix=f"{prefix}.embed_tokens",
            )
        else:
            self.embed_tokens = PPMissingLayer()

        self.start_layer, self.end_layer, self.layers = make_layers(
            config.num_hidden_layers,
            lambda prefix: LagunaDecoderLayer(
                config=config,
                cache_config=cache_config,
                quant_config=quant_config,
                prefix=prefix,
                enable_eplb=enable_eplb,
            ),
            prefix=f"{prefix}.layers",
        )

        if get_pp_group().is_last_rank:
            self.norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
        else:
            self.norm = PPMissingLayer()

        self.make_empty_intermediate_tensors = make_empty_intermediate_tensors_factory(
            ["hidden_states", "residual"], config.hidden_size
        )

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.embed_tokens(input_ids)

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
    ) -> torch.Tensor | IntermediateTensors:
        if get_pp_group().is_first_rank:
            if inputs_embeds is not None:
                hidden_states = inputs_embeds
            else:
                hidden_states = self.embed_tokens(input_ids)
            residual = None
        else:
            assert intermediate_tensors is not None
            hidden_states = intermediate_tensors["hidden_states"]
            residual = intermediate_tensors["residual"]

        aux_hidden_states = self._maybe_add_hidden_state(
            [], self.start_layer, hidden_states, residual
        )
        for layer_idx, layer in enumerate(
            islice(self.layers, self.start_layer, self.end_layer),
            start=self.start_layer,
        ):
            hidden_states, residual = layer(positions, hidden_states, residual)
            self._maybe_add_hidden_state(
                aux_hidden_states, layer_idx + 1, hidden_states, residual
            )

        if not get_pp_group().is_last_rank:
            return IntermediateTensors(
                {"hidden_states": hidden_states, "residual": residual}
            )

        hidden_states, _ = self.norm(hidden_states, residual)
        if len(aux_hidden_states) > 0:
            return hidden_states, aux_hidden_states
        return hidden_states

    defget_expert_mapping(self) -> list[tuple[str, str, int, str]]:
"""Get expert parameter mapping for weight loading.

        Returns mapping tuples of (param_name, weight_name, expert_id, shard_id)
        that handle both weights and quantization scales.
        """
        return FusedMoE.make_expert_params_mapping(
            self,
            ckpt_gate_proj_name="gate_proj",
            ckpt_down_proj_name="down_proj",
            ckpt_up_proj_name="up_proj",
            num_experts=self.config.num_experts,
            num_redundant_experts=self.num_redundant_experts,
        )

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        stacked_params_mapping = [
            # (param_name, shard_name, shard_id)
            ("qkv_proj", "q_proj", "q"),
            ("qkv_proj", "k_proj", "k"),
            ("qkv_proj", "v_proj", "v"),
            # gate_proj and up_proj are loaded as separate Linears (see
            # LagunaMLP) so no merge entry is needed here.
        ]

        # Suffixes to skip for GPTQ/modelopt models if param doesn't exist
        ignore_suffixes = (
            ".bias",
            "_bias",
            ".k_scale",
            "_k_scale",
            ".v_scale",
            "_v_scale",
            ".weight_scale",
            "_weight_scale",
            ".input_scale",
            "_input_scale",
        )

        params_dict = dict(self.named_parameters())
        loaded_params: set[str] = set()
        expert_params_mapping = self.get_expert_mapping()

        tp_rank = get_tensor_model_parallel_rank()

        for name, loaded_weight in weights:
            # Handle attention sinks (distributed across ranks). Derive the
            # per-rank slice from the parameter's own shape so per-layer
            # variations in head count are handled correctly.
            if "sink" in name:
                param = params_dict.get(name)
                if param is not None:
                    layer_heads_per_rank = param.shape[0]
                    layer_head_start = tp_rank * layer_heads_per_rank
                    narrow_weight = loaded_weight.narrow(
                        0, layer_head_start, layer_heads_per_rank
                    )
                    param.data.copy_(narrow_weight)
                    loaded_params.add(name)
                continue

            # Handle KV cache quantization scales
            if self.quant_config is not None and (
                scale_name := self.quant_config.get_cache_scale(name)
            ):
                param = params_dict[scale_name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                assert loaded_weight.numel() == 1, (
                    f"KV scale numel {loaded_weight.numel()} != 1"
                )
                loaded_weight = loaded_weight.squeeze()
                weight_loader(param, loaded_weight)
                loaded_params.add(scale_name)
                continue

            # Handle stacked params (QKV, gate_up for
            # non-expert layers and shared_expert)
            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name:
                    continue
                # Skip expert weights - handled below via expert_params_mapping
                if "mlp.experts" in name and "shared_expert" not in name:
                    continue
                name = name.replace(weight_name, param_name)

                if name.endswith(ignore_suffixes) and name not in params_dict:
                    continue
                if is_pp_missing_parameter(name, self):
                    continue
                # Remap FP8 kv_scale names for backwards compatibility
                if name.endswith("scale"):
                    name = maybe_remap_kv_scale_name(name, params_dict)
                    if name is None:
                        continue
                if name not in params_dict:
                    continue

                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                if weight_loader == default_weight_loader:
                    weight_loader(param, loaded_weight)
                else:
                    weight_loader(param, loaded_weight, shard_id)
                loaded_params.add(name)
                break
            else:
                # Try expert params mapping (handles weights + quantization scales)
                is_expert_weight = False
                for mapping in expert_params_mapping:
                    param_name, weight_name, expert_id, shard_id = mapping
                    if weight_name not in name:
                        continue

                    # Mark as expert weight so we skip regular loading below
                    is_expert_weight = True

                    # Create mapped name without modifying original
                    name_mapped = name.replace(weight_name, param_name)

                    if is_pp_missing_parameter(name_mapped, self):
                        continue
                    if (
                        name_mapped.endswith(ignore_suffixes)
                        and name_mapped not in params_dict
                    ):
                        continue
                    if name_mapped not in params_dict:
                        continue

                    param = params_dict[name_mapped]
                    # Use return_success to handle expert parallelism correctly
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
                        loaded_params.add(name_mapped)
                        break
                else:
                    # Expert weight not mapped to this rank - skip
                    if is_expert_weight:
                        continue

                    # Remap kv_scale names before the ignore_suffixes filter:
                    # the suffix list includes .k_scale/.v_scale, so filtering
                    # first drops the checkpoint key before remap can rewrite
                    # it to the .attn.* name that exists in params_dict.
                    name = maybe_remap_kv_scale_name(name, params_dict)
                    if name is None:
                        continue

                    if name.endswith(ignore_suffixes) and name not in params_dict:
                        continue

                    if is_pp_missing_parameter(name, self):
                        continue

                    if name not in params_dict:
                        continue

                    param = params_dict[name]
                    weight_loader = getattr(
                        param, "weight_loader", default_weight_loader
                    )
                    weight_loader(param, loaded_weight)
                    loaded_params.add(name)

        return loaded_params
```