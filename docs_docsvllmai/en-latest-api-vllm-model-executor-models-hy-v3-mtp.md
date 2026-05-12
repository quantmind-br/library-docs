---
title: hy_v3_mtp - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/hy_v3_mtp/
source: sitemap
fetched_at: 2026-05-07T21:30:47.818752199-03:00
rendered_js: false
word_count: 0
summary: This document defines the HYV3MTP class, a PyTorch-based module used for multi-token prediction within a VLLM-compatible architecture, including logic for weight loading, parameter sharding, and tensor manipulation.
tags:
    - vllm
    - multi-token-prediction
    - pytorch
    - model-architecture
    - weight-loading
    - tensor-manipulation
category: reference
---

```
classHYV3MTP(nn.Module):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        self.config = vllm_config.model_config.hf_config
        self.quant_config = vllm_config.quant_config
        self.model = HYV3MultiTokenPredictor(
            vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
        )

        self.sampler = Sampler()

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        spec_step_idx: int = 0,
    ) -> torch.Tensor:
        hidden_states = self.model(
            input_ids, positions, hidden_states, inputs_embeds, spec_step_idx
        )
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
        spec_step_idx: int = 0,
    ) -> torch.Tensor | None:
        return self.model.compute_logits(hidden_states, spec_step_idx)

    defsample(
        self,
        logits: torch.Tensor,
        sampling_metadata: SamplingMetadata,
    ) -> SamplerOutput | None:
        next_tokens = self.sampler(logits, sampling_metadata)
        return next_tokens

    def_split_qkv_weight(self, qkv: torch.Tensor):
        num_attention_heads = self.config.num_attention_heads
        num_kv_heads = getattr(
            self.config, "num_key_value_heads", self.config.num_attention_heads
        )
        num_key_value_groups = num_attention_heads // num_kv_heads
        hidden_size = self.config.hidden_size

        if hasattr(self.config, "head_dim"):
            attention_head_dim = self.config.head_dim
        elif hasattr(self.config, "attention_head_dim"):
            attention_head_dim = self.config.attention_head_dim
        else:
            attention_head_dim = self.config.hidden_size // num_attention_heads

        qkv = qkv.reshape(
            num_kv_heads, num_key_value_groups + 2, attention_head_dim, hidden_size
        )
        q, k, v = torch.split(qkv, (num_key_value_groups, 1, 1), dim=1)
        q = q.reshape(-1, hidden_size)
        k = k.reshape(-1, hidden_size)
        v = v.reshape(-1, hidden_size)
        return torch.concat((q, k, v))

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        cla_factor = _get_cla_factor(self.config)
        stacked_params_mapping = [
            # (param_name, shard_name, shard_id)
            (".qkv_proj", ".q_proj", "q"),
            (".qkv_proj", ".k_proj", "k"),
            (".qkv_proj", ".v_proj", "v"),
            (".gate_up_proj", ".gate_proj", 0),
            (".gate_up_proj", ".up_proj", 1),
        ]

        num_attention_heads = self.config.num_attention_heads
        num_kv_heads = getattr(
            self.config, "num_key_value_heads", self.config.num_attention_heads
        )
        split_params_mapping = [
            (".gate_up_proj", ".gate_and_up_proj", 2, [(1, 1), (0, 1)], None),
            (
                ".qkv_proj",
                ".qkv_proj",
                num_attention_heads + num_kv_heads * 2,
                [("q", num_attention_heads), ("k", num_kv_heads), ("v", num_kv_heads)],
                self._split_qkv_weight,
            ),
        ]

        if _is_moe(self.config):
            expert_params_mapping = FusedMoE.make_expert_params_mapping(
                self,
                ckpt_gate_proj_name="gate_proj",
                ckpt_down_proj_name="down_proj",
                ckpt_up_proj_name="up_proj",
                num_experts=self.config.num_experts,
            )
        else:
            expert_params_mapping = {}

        params_dict = dict(self.named_parameters())

        # V3 shared weights mapping:
        # - embed_tokens: from main model's model.embed_tokens.weight
        # - lm_head: from main model's lm_head.weight → MTP shared_head.head
        #   (HF infer_mtp uses head_weight=self.lm_head.weight, not the
        #    checkpoint's model.layers.<N>.shared_head.weight)
        # - No norm mapping (V3 MTP has no intermediate norm before lm_head)
        mtp_start = self.config.num_hidden_layers
        v3_shared_weights = {
            "model.embed_tokens.weight": "model.embed_tokens.weight",
            "lm_head.weight": f"model.layers.{mtp_start}.shared_head.head.weight",
        }

        for name, loaded_weight in weights:
            # Intercept shared weights before any other processing
            if name in v3_shared_weights:
                target_name = v3_shared_weights[name]
                if target_name in params_dict:
                    param = params_dict[target_name]
                    weight_loader = getattr(
                        param, "weight_loader", default_weight_loader
                    )
                    weight_loader(param, loaded_weight)
                continue

            if "rotary_emb.inv_freq" in name:
                continue
            if "gate_proj_bias" in name:
                name = name.replace("gate_proj_bias", "gate_proj.bias")
            if "up_proj_bias" in name:
                name = name.replace("up_proj_bias", "up_proj.bias")
            if "rotary_emb.cos_cached" in name or "rotary_emb.sin_cached" in name:
                continue
            if self.config.tie_word_embeddings and "lm_head.weight" in name:
                continue
            if self.quant_config is not None and (
                scale_name := self.quant_config.get_cache_scale(name)
            ):
                param = params_dict[scale_name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                loaded_weight = loaded_weight[0]
                weight_loader(param, loaded_weight)
                continue
            spec_layer = get_spec_layer_idx_from_weight_name(self.config, name)
            if spec_layer is None:
                continue
            name = self._rewrite_spec_layer_name(spec_layer, name)
            # Skip weights that _rewrite_spec_layer_name marked for skipping
            if name == "__skip__":
                continue
            if "scale" in name:
                name = maybe_remap_kv_scale_name(name, params_dict)
                if name is None:
                    continue
            is_found = False

            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name:
                    continue
                if "mlp.experts" in name:
                    continue
                if weight_name == ".q_proj":
                    match = re.search(r"layers\.\d+", name)
                    if match:
                        layer_id = int(match.group(0).split(".")[-1])
                        if cla_factor > 1 and layer_id % cla_factor != 0:
                            continue
                name = name.replace(weight_name, param_name)
                if name.endswith(".bias") and name not in params_dict:
                    continue

                if is_pp_missing_parameter(name, self):
                    continue

                param = params_dict[name]
                weight_loader = param.weight_loader
                weight_loader(param, loaded_weight, shard_id)

                is_found = True
                break
            if is_found:
                continue

            for param_name, weight_name, den, split_param, func in split_params_mapping:
                if weight_name not in name:
                    continue
                name = name.replace(weight_name, param_name)
                if name.endswith(".bias") and name not in params_dict:
                    continue

                if is_pp_missing_parameter(name, self):
                    continue

                assert loaded_weight.shape[0] % den == 0
                units = loaded_weight.shape[0] // den

                param = params_dict[name]
                weight_loader = param.weight_loader
                offset = 0
                for shard_id, num in split_param:
                    new_offset = offset + num * units
                    if func:
                        weight_loader(
                            param, func(loaded_weight)[offset:new_offset], shard_id
                        )
                    else:
                        weight_loader(param, loaded_weight[offset:new_offset], shard_id)
                    offset = new_offset

                break
            else:
                if name.endswith(".bias") and name not in params_dict:
                    continue
                for mapping in expert_params_mapping:
                    param_name, weight_name, expert_id, shard_id = mapping
                    if weight_name not in name:
                        continue
                    name = name.replace(weight_name, param_name)
                    if is_pp_missing_parameter(name, self):
                        continue
                    param = params_dict[name]
                    weight_loader = param.weight_loader
                    weight_loader(
                        param,
                        loaded_weight,
                        name,
                        shard_id=shard_id,
                        expert_id=expert_id,
                    )
                    break
                else:
                    if is_pp_missing_parameter(name, self):
                        continue

                    if "mlp.gate.wg." in name:
                        name = name.replace("wg.", "")
                    # V3 checkpoint: mlp.router.gate -> mlp.gate
                    if "mlp.router.gate." in name:
                        name = name.replace("router.gate.", "gate.")

                    param = params_dict[name]
                    weight_loader = getattr(
                        param, "weight_loader", default_weight_loader
                    )
                    weight_loader(param, loaded_weight)

    def_rewrite_spec_layer_name(self, spec_layer: int, name: str) -> str:
"""Rewrite spec layer weight names to match vLLM module structure."""
        # Skip embed_tokens (doesn't exist in V3 MTP checkpoint under spec
        # layer) and shared_head (we use main model's lm_head instead)
        if f"model.layers.{spec_layer}.embed_tokens" in name:
            return "__skip__"
        if f"model.layers.{spec_layer}.shared_head" in name:
            return "__skip__"

        spec_layer_weight_names = ["enorm", "hnorm", "eh_proj", "final_layernorm"]
        spec_layer_weight = False
        for weight_name in spec_layer_weight_names:
            if weight_name in name:
                spec_layer_weight = True
                break
        if not spec_layer_weight:
            # Transformer block weights go under .mtp_block
            name = name.replace(
                f"model.layers.{spec_layer}.", f"model.layers.{spec_layer}.mtp_block."
            )
        return name
```