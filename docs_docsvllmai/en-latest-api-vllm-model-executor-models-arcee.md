---
title: arcee - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/arcee/
source: sitemap
fetched_at: 2026-05-07T21:29:00.896429877-03:00
rendered_js: false
word_count: 0
summary: This document defines the ArceeModel architecture, implementing a pipeline-parallel transformer backbone with support for weight loading, token embedding, and stacked decoder layers.
tags:
    - deep-learning
    - pytorch
    - transformer-models
    - pipeline-parallelism
    - weight-loading
    - model-architecture
category: concept
---

```
@support_torch_compile
classArceeModel(nn.Module, EagleModelMixin):
"""The transformer model backbone for Arcee (embedding layer + stacked
    decoder blocks + final norm)."""

    def__init__(
        self,
        *,
        vllm_config,
        prefix: str = "",
        layer_type: type[nn.Module] = ArceeDecoderLayer,
    ) -> None:
        super().__init__()
        config: LlamaConfig = vllm_config.model_config.hf_config
        cache_config = vllm_config.cache_config
        quant_config = vllm_config.quant_config
        self.quant_config = quant_config
        self.config = config
        self.vocab_size = config.vocab_size

        # Word embeddings (parallelized if using pipeline parallel)
        if get_pp_group().is_first_rank or (
            config.tie_word_embeddings and get_pp_group().is_last_rank
        ):
            self.embed_tokens = VocabParallelEmbedding(
                self.vocab_size,
                config.hidden_size,
                quant_config=quant_config,
            )
        else:
            self.embed_tokens = PPMissingLayer()  # placeholder on non-embedding ranks

        # Build decoder layers across pipeline ranks
        self.start_layer, self.end_layer, self.layers = make_layers(
            config.num_hidden_layers,
            lambda prefix: layer_type(
                config=config,
                cache_config=cache_config,
                quant_config=quant_config,
                prefix=prefix,
            ),
            prefix=f"{prefix}.layers",
        )
        # Final RMSNorm on the last pipeline stage
        if get_pp_group().is_last_rank:
            self.norm = RMSNorm(config.hidden_size, eps=config.rms_norm_eps)
        else:
            self.norm = PPMissingLayer()

        # Prepare factory for empty intermediate tensors
        # (for pipeline scheduling)
        self.make_empty_intermediate_tensors = make_empty_intermediate_tensors_factory(
            ["hidden_states", "residual"], config.hidden_size
        )

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.embed_tokens(input_ids)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None,
        inputs_embeds: torch.Tensor | None = None,
    ) -> torch.Tensor | IntermediateTensors | tuple[torch.Tensor, list[torch.Tensor]]:
        # Embedding lookup (on first pipeline rank)
        if get_pp_group().is_first_rank:
            hidden_states = (
                inputs_embeds
                if inputs_embeds is not None
                else self.embed_input_ids(input_ids)
            )
            residual = None
        else:
            assert intermediate_tensors is not None, (
                "IntermediateTensors must be provided for non-first pipeline ranks"
            )
            hidden_states = intermediate_tensors["hidden_states"]
            residual = intermediate_tensors["residual"]

        aux_hidden_states = self._maybe_add_hidden_state([], 0, hidden_states, residual)
        for idx, layer in enumerate(
            islice(self.layers, self.start_layer, self.end_layer)
        ):
            hidden_states, residual = layer(positions, hidden_states, residual)
            self._maybe_add_hidden_state(
                aux_hidden_states, idx + 1, hidden_states, residual
            )

        if not get_pp_group().is_last_rank:
            # Send intermediate results to the next pipeline stage
            return IntermediateTensors(
                {"hidden_states": hidden_states, "residual": residual}
            )
        # On last rank: apply final layer norm
        hidden_states, _ = self.norm(hidden_states, residual)
        if len(aux_hidden_states) > 0:
            return hidden_states, aux_hidden_states
        return hidden_states

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
"""Load weights, mapping q/k/v projections to fused qkv_proj."""
        stacked_params_mapping = [
            (".qkv_proj", ".q_proj", "q"),
            (".qkv_proj", ".k_proj", "k"),
            (".qkv_proj", ".v_proj", "v"),
        ]

        params_dict = dict(self.named_parameters())
        loaded_params: set[str] = set()

        for name, loaded_weight in weights:
            if "rotary_emb.inv_freq" in name:
                continue
            if "rotary_emb.cos_cached" in name or "rotary_emb.sin_cached" in name:
                continue

            if self.quant_config is not None and (
                scale_name := self.quant_config.get_cache_scale(name)
            ):
                param = params_dict[scale_name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                loaded_weight = (
                    loaded_weight if loaded_weight.dim() == 0 else loaded_weight[0]
                )
                weight_loader(param, loaded_weight)
                loaded_params.add(scale_name)
                continue

            if "scale" in name or "zero_point" in name:
                remapped_name = maybe_remap_kv_scale_name(name, params_dict)
                if remapped_name is None:
                    continue
                name = remapped_name

            mapped = False
            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name:
                    continue

                name = name.replace(weight_name, param_name)

                if name.endswith(".bias") and name not in params_dict:
                    mapped = True
                    break

                if is_pp_missing_parameter(name, self):
                    mapped = True
                    break

                param = params_dict[name]
                weight_loader = param.weight_loader  # type: ignore[attr-defined]
                weight_loader(param, loaded_weight, shard_id)
                loaded_params.add(name)
                mapped = True
                break

            if mapped:
                continue

            if name.endswith(".bias") and name not in params_dict:
                continue

            if is_pp_missing_parameter(name, self):
                continue

            param = params_dict[name]
            weight_loader = getattr(param, "weight_loader", default_weight_loader)
            weight_loader(param, loaded_weight)
            loaded_params.add(name)

        return loaded_params
```