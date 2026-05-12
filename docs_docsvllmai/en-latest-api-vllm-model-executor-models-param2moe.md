---
title: param2moe - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/param2moe/
source: sitemap
fetched_at: 2026-05-07T21:32:32.947429544-03:00
rendered_js: false
word_count: 4
summary: This document defines the Param2MoEModel class, which implements a Mixture-of-Experts architecture in vLLM, including custom weight loading logic for fused projections and parallelized expert layers.
tags:
    - vllm
    - mixture-of-experts
    - model-architecture
    - weight-loading
    - pipeline-parallelism
    - pytorch
category: api
---

```
classParam2MoEModel(nn.Module):
    def__init__(
        self,
        *,
        vllm_config: VllmConfig,
        prefix: str = "",
    ) -> None:
        super().__init__()

        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config

        self.config = config
        self.vocab_size = config.vocab_size
        self.embed_dim = config.hidden_size
        self.tie_word_embeddings: bool = getattr(config, "tie_word_embeddings", False)

        # Embedding  (HF name: word_embeddings → vLLM name: embed_tokens)
        if get_pp_group().is_first_rank or (
            self.tie_word_embeddings and get_pp_group().is_last_rank
        ):
            self.embed_tokens = VocabParallelEmbedding(
                self.vocab_size,
                self.embed_dim,
                quant_config=quant_config,
                prefix=f"{prefix}.embed_tokens",
            )
        else:
            self.embed_tokens = PPMissingLayer()

        self.start_layer, self.end_layer, self.layers = make_layers(
            config.num_hidden_layers,
            lambda prefix: Param2MoEDecoderLayer(
                vllm_config=vllm_config,
                prefix=prefix,
            ),
            prefix=f"{prefix}.layers",
        )

        self.make_empty_intermediate_tensors = make_empty_intermediate_tensors_factory(
            ["hidden_states", "residual"], config.hidden_size
        )

        if get_pp_group().is_last_rank:
            self.norm = RMSNorm(self.embed_dim, eps=config.rms_norm_eps)
        else:
            self.norm = PPMissingLayer()

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.embed_tokens(input_ids)

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None,
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
            hidden_states, residual = layer(hidden_states, positions, residual)

        if not get_pp_group().is_last_rank:
            return IntermediateTensors(
                {"hidden_states": hidden_states, "residual": residual}
            )

        if residual is None:
            hidden_states = self.norm(hidden_states)
        else:
            hidden_states, _ = self.norm(hidden_states, residual)
        return hidden_states

    defload_weights(
        self,
        weights: Iterable[tuple[str, torch.Tensor]],
    ) -> set[str]:
"""
        Custom weight loader for the inner Param2MoEModel.

        Receives weights that have already been renamed/normalised by the
        outer model and whose ``model.`` prefix has been stripped by
        ``AutoWeightsLoader``.  Handles:
          1. Fused QKV split (query_key_value → qkv_proj q/k/v shards).
          2. gate_proj + up_proj → gate_up_proj stacking (dense + shared-exp).
          3. Routed-expert weights via the fused-MoE mapping.
          4. All remaining weights via their default loader.
        """
        config = self.config
        num_heads: int = config.num_attention_heads
        num_kv_heads: int = config.num_key_value_heads
        head_dim: int = config.head_dim or (config.hidden_size // num_heads)
        q_split = num_heads * head_dim
        kv_split = num_kv_heads * head_dim

        stacked_params_mapping = [
            # (vllm_param_name, ckpt_weight_name, shard_id)
            ("gate_up_proj", "gate_proj", 0),
            ("gate_up_proj", "up_proj", 1),
        ]

        params_dict = dict(self.named_parameters(remove_duplicate=False))
        loaded_params: set[str] = set()
        expert_params_mapping = self.get_expert_mapping()

        for name, loaded_weight in weights:
            # ------------------------------------------------------------------
            # 1. Fused QKV: split into q / k / v shards for QKVParallelLinear
            # ------------------------------------------------------------------
            if name.endswith(".self_attn.qkv_proj.weight"):
                if name not in params_dict:
                    continue
                if is_pp_missing_parameter(name, self):
                    continue

                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                q_w = loaded_weight[:q_split, :]
                k_w = loaded_weight[q_split : q_split + kv_split, :]
                v_w = loaded_weight[q_split + kv_split :, :]
                weight_loader(param, q_w, "q")
                weight_loader(param, k_w, "k")
                weight_loader(param, v_w, "v")
                loaded_params.add(name)
                continue

            # ------------------------------------------------------------------
            # 2. gate_proj / up_proj → gate_up_proj (dense MLP + shared-exp.)
            # ------------------------------------------------------------------
            matched_stacked = False
            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name:
                    continue
                if "mlp.experts" in name:  # routed experts handled below
                    continue
                new_name = name.replace(weight_name, param_name)
                if new_name.endswith(".bias") and new_name not in params_dict:
                    continue
                if new_name not in params_dict:
                    continue
                if is_pp_missing_parameter(new_name, self):
                    continue

                param = params_dict[new_name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                weight_loader(param, loaded_weight, shard_id)
                loaded_params.add(new_name)
                matched_stacked = True
                break

            if matched_stacked:
                continue

            # ------------------------------------------------------------------
            # 3. Routed expert weights → fused-MoE kernel layout
            # ------------------------------------------------------------------
            matched_expert = False
            for (
                param_name,
                weight_name,
                expert_id,
                shard_id,
            ) in expert_params_mapping:
                if weight_name not in name:
                    continue
                new_name = name.replace(weight_name, param_name)
                if is_pp_missing_parameter(new_name, self):
                    continue
                if new_name not in params_dict:
                    continue

                param = params_dict[new_name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                weight_loader(
                    param,
                    loaded_weight,
                    name,
                    shard_id=shard_id,
                    expert_id=expert_id,
                )
                loaded_params.add(new_name)
                matched_expert = True
                break

            if matched_expert:
                continue

            # ------------------------------------------------------------------
            # 4. All other weights: direct load (layernorms, embed_tokens, …)
            # ------------------------------------------------------------------
            if name.endswith(".bias") and name not in params_dict:
                continue
            if name not in params_dict:
                continue
            if is_pp_missing_parameter(name, self):
                continue

            param = params_dict[name]
            weight_loader = getattr(param, "weight_loader", default_weight_loader)
            try:
                weight_loader(param, loaded_weight)
            except Exception as e:
                raise RuntimeError(
                    f"[param2moe] Failed to load weight '{name}' "
                    f"with shape {tuple(loaded_weight.shape)} "
                    f"into param type {type(param).__name__}: {e}"
                ) frome
            loaded_params.add(name)

        return loaded_params

    defget_expert_mapping(self) -> list[tuple[str, str, int, str]]:
        return fused_moe_make_expert_params_mapping(
            self,
            ckpt_gate_proj_name="gate_proj",
            ckpt_down_proj_name="down_proj",
            ckpt_up_proj_name="up_proj",
            num_experts=self.config.num_experts,
        )
```