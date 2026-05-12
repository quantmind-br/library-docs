---
title: fairseq2_llama - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/fairseq2_llama/
source: sitemap
fetched_at: 2026-05-07T21:29:59.603638403-03:00
rendered_js: false
word_count: 16
summary: This code implements a custom model wrapper class for integrating Fairseq2-formatted Llama models into the vLLM serving framework, providing logic for weight remapping, tensor parallelism support, and parameter reshaping.
tags:
    - vllm
    - fairseq2
    - llama
    - model-loading
    - tensor-parallelism
    - weight-mapping
category: api
---

```
classFairseq2LlamaForCausalLM(LlamaForCausalLM):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__(vllm_config=vllm_config, prefix=prefix)
        self.tp_rank = get_tensor_model_parallel_rank()
        self.tp_size = get_tensor_model_parallel_world_size()
        # For the model loader to read only the relevant checkpoint files
        self.allow_patterns_overrides = [
            # either the full checkpoint
            "model.pt",
            # or the tp-sharded checkpoint of the current rank
            f"model.{self.tp_rank}.pt",
        ]

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        # fairseq2's serialization adds a wrapper to usual .pt state_dict's:
        # { "model_key": my_model_name, "my_model_name": state_dict }
        # which we first need to unpack
        weights_wrapped = dict(weights)
        weights = weights_wrapped[weights_wrapped["model_key"]].items()  # type: ignore

        # remap keys
        fs2_to_vllm_mapper = WeightsMapper(
            orig_to_new_prefix={
                "decoder_frontend.embed.": "model.embed_tokens.",
                "decoder.": "model.",
                "final_proj.": "lm_head.",
            },
            orig_to_new_substr={
                ".self_attn_layer_norm.": ".input_layernorm.",
                ".ffn_layer_norm.": ".post_attention_layernorm.",
                ".self_attn.output_proj.": ".self_attn.o_proj.",
                ".ffn.gate_proj.": ".mlp.gate_proj.",
                ".ffn.inner_proj.": ".mlp.up_proj.",
                ".ffn.output_proj.": ".mlp.down_proj.",
                ".layer_norm.": ".norm.",
            },
        )
        weights = fs2_to_vllm_mapper.apply(weights)

        params = dict(self.named_parameters())

        loader = AutoWeightsLoader(
            self,
            skip_prefixes=(["lm_head."] if self.config.tie_word_embeddings else None),
        )
        return loader.load_weights(
            (
                self.reshape_fairseq2_weights(name, loaded_weight, params)
                for name, loaded_weight in weights
            )
        )

    defflag_sharded_weights(self, params: dict[str, Parameter]):
"""Sets the `is_sharded_weight` flag to True for all sharded weights"""
        for name, param in params.items():
            modules = name.split(".")
            if "norm" in name and len(param.size()) < 2:
                # layer norms are not sharded
                continue
            elif any(emb in modules for emb in ["embed_tokens", "lm_head"]):
                # for now we repeat embedding layers for compatibility
                continue
            else:
                # all other layers are sharded
                set_weight_attrs(param, {"is_sharded_weight": True})

    defreshape_fairseq2_weights(
        self,
        name: str,
        loaded_weight: torch.Tensor,
        params: dict[str, Parameter],
    ) -> tuple[str, torch.Tensor]:
"""Reshape fairseq2's weights."""

        defpermute(w: torch.Tensor, n_heads: int) -> torch.Tensor:
            attn_in = self.config.head_dim * n_heads
            # check for a sharded weight on dim 0
            if attn_in // self.tp_size == w.size()[0]:
                attn_in //= self.tp_size
                n_heads //= self.tp_size
            attn_out = self.config.hidden_size
            return (
                w.view(n_heads, attn_in // n_heads // 2, 2, attn_out)
                .transpose(1, 2)
                .reshape(attn_in, attn_out)
            )

        modules = name.split(".")

        # rotary embeds should be sliced
        if "k_proj" in modules:
            loaded_weight = permute(loaded_weight, self.config.num_key_value_heads)

        elif "q_proj" in modules:
            loaded_weight = permute(loaded_weight, self.config.num_attention_heads)

        # We make the loaded weights compatible with both
        # full checkpoints and tp sharded checkpoints.
        # Embeddings are repeated to fit the vocab size.
        # Other weights are flagged for the weight_loader calls.
        if any(emb in modules for emb in ["embed_tokens", "lm_head"]):
            # Embeddings are sharded on dim 0
            dim = 0
            # In fairseq2, vocab size has to be divisible by tp_size
            # so we don't worry about padding
            if self.tp_size > 1 and loaded_weight.shape[dim] < self.config.vocab_size:
                assert (
                    loaded_weight.shape[dim] * self.tp_size == self.config.vocab_size
                ), "vocab_size should be divisible by tp_size."
                repeats = [1] * len(loaded_weight.size())
                repeats[dim] = self.tp_size
                # repeat to match vocab size and to be easily 'narrow'able
                loaded_weight = loaded_weight.repeat(repeats)
                set_weight_attrs(params[name], {"is_sharded_weight": False})
                # if embeddings are sharded, the rest is too
                if "embed_tokens" in modules:
                    self.flag_sharded_weights(params)

        return name, loaded_weight
```