---
title: gemma4_mtp - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/gemma4_mtp/
source: sitemap
fetched_at: 2026-05-07T21:30:17.915089512-03:00
rendered_js: false
word_count: 291
summary: This document describes the implementation of the Gemma4 Multi-Token Prediction (MTP) model within the vLLM framework, focusing on its architecture for speculative decoding and efficient KV cache sharing.
tags:
    - gemma4
    - mtp
    - speculative-decoding
    - vllm
    - kv-cache
    - multi-token-prediction
    - machine-learning-models
category: api
---

Inference-only Gemma4 MTP (Multi-Token Prediction) model.

The Gemma4 assistant model is a lightweight decoder that shares KV cache with the target (backbone) model. All assistant decoder layers are KV-shared: they only have Q projections (no K/V projections or norms), and read K/V from the target model's cache at runtime.

Checkpoint layout (`gemma4_assistant`)::

```
model.embed_tokens.*          -- token embeddings
model.layers.{i}.*            -- decoder layers (Q-only attention + MLP)
model.norm.*                  -- final RMSNorm
pre_projection.*              -- Linear(2 * backbone_hidden_size, hidden_size)
post_projection.*             -- Linear(hidden_size, backbone_hidden_size)
lm_head.*                     -- language model head (tied to embed_tokens)
masked_embedding.centroids.*  -- centroid projection (when use_ordered_embeddings)
masked_embedding.token_ordering -- token-to-centroid mapping buffer
```

## Gemma4MTP [¶](#vllm.model_executor.models.gemma4_mtp.Gemma4MTP "Permanent link")

Bases: `Module`

Gemma4 Multi-Token Prediction model for speculative decoding.

forward() returns (draft\_hidden\_states, backbone\_hidden\_states). The proposer uses draft\_hidden\_states for compute\_logits (via the draft-dim lm\_head) and backbone\_hidden\_states for the hidden-state feedback buffer.

Source code in `vllm/model_executor/models/gemma4_mtp.py`

```
@support_torch_compile
classGemma4MTP(nn.Module):
"""Gemma4 Multi-Token Prediction model for speculative decoding.

    forward() returns (draft_hidden_states, backbone_hidden_states).
    The proposer uses draft_hidden_states for compute_logits (via
    the draft-dim lm_head) and backbone_hidden_states for the
    hidden-state feedback buffer.
    """

    has_own_lm_head = True

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "pre_projection.": "model.pre_projection.",
            "post_projection.": "model.post_projection.",
        },
    )

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.speculative_config.draft_model_config.hf_config
        text_config = _get_text_config(config)
        self.config = config

        self.model = Gemma4MultiTokenPredictor(
            vllm_config=vllm_config,
            prefix=maybe_prefix(prefix, "draft_model"),
        )

        # lm_head operates in draft-dim.  Tied to embed_tokens at init
        # so load_weights populates both from a single checkpoint entry.
        # After embedding sharing, lm_head.weight still references the
        # original draft-dim tensor.
        self.lm_head = ParallelLMHead(
            text_config.vocab_size,
            text_config.hidden_size,
            prefix=maybe_prefix(prefix, "lm_head"),
        )
        if getattr(config, "tie_word_embeddings", True):
            self.lm_head.weight = self.model.embed_tokens.weight

        self.logits_processor = LogitsProcessor(
            text_config.vocab_size,
            soft_cap=getattr(text_config, "final_logit_softcapping", None),
        )

        if getattr(config, "use_ordered_embeddings", False):
            num_centroids = getattr(config, "num_centroids", 2048)
            top_k = getattr(config, "centroid_intermediate_top_k", 32)
            self.masked_embedding = Gemma4MTPMaskedEmbedder(
                hidden_size=text_config.hidden_size,
                vocab_size=text_config.vocab_size,
                num_centroids=num_centroids,
                centroid_intermediate_top_k=top_k,
            )
            logger.info(
                "Gemma4 MTP: centroids masking enabled "
                "(num_centroids=%d, top_k=%d, active_tokens=%d/%d).",
                num_centroids,
                top_k,
                top_k * (text_config.vocab_size // num_centroids),
                text_config.vocab_size,
            )
        else:
            self.masked_embedding = None

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
        **kwargs: object,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        return self.model(
            input_ids,
            positions,
            hidden_states,
            intermediate_tensors,
            inputs_embeds,
            spec_step_idx,
        )

    def_get_full_lm_head_weight(self) -> torch.Tensor:
        lm_head_weight = self.lm_head.weight
        tp_size = get_tensor_model_parallel_world_size()
        if tp_size > 1:
            lm_head_weight = tensor_model_parallel_all_gather(
                lm_head_weight,
                dim=0,
            )
        return lm_head_weight[: self.masked_embedding.vocab_size]

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
        spec_step_idx: int = 0,
    ) -> torch.Tensor | None:
        if self.masked_embedding is not None:
            return self.masked_embedding(
                hidden_states,
                self._get_full_lm_head_weight(),
            )
        return self.logits_processor(self.lm_head, hidden_states)

    defget_top_tokens(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor:
"""Sparse argmax via centroids masking. Returns token IDs directly."""
        return self.masked_embedding.get_top_tokens(
            hidden_states,
            self._get_full_lm_head_weight(),
        )

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
```

### get\_top\_tokens [¶](#vllm.model_executor.models.gemma4_mtp.Gemma4MTP.get_top_tokens "Permanent link")

Sparse argmax via centroids masking. Returns token IDs directly.

Source code in `vllm/model_executor/models/gemma4_mtp.py`

```
defget_top_tokens(
    self,
    hidden_states: torch.Tensor,
) -> torch.Tensor:
"""Sparse argmax via centroids masking. Returns token IDs directly."""
    return self.masked_embedding.get_top_tokens(
        hidden_states,
        self._get_full_lm_head_weight(),
    )
```

## Gemma4MTPAttention [¶](#vllm.model_executor.models.gemma4_mtp.Gemma4MTPAttention "Permanent link")

Bases: `Module`

Q-only attention for Gemma4 MTP layers.

K/V come from the target model's KV cache via `kv_sharing_target_layer_name` (set by the proposer after model construction).

Source code in `vllm/model_executor/models/gemma4_mtp.py`

```
classGemma4MTPAttention(nn.Module):
"""Q-only attention for Gemma4 MTP layers.

    K/V come from the target model's KV cache via
    ``kv_sharing_target_layer_name`` (set by the proposer after
    model construction).
    """

    def__init__(
        self,
        config,
        hidden_size: int,
        num_heads: int,
        num_kv_heads: int,
        head_dim: int,
        max_position_embeddings: int,
        cache_config: CacheConfig | None = None,
        quant_config: QuantizationConfig | None = None,
        attn_logits_soft_cap: float | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        self.config = config
        self.hidden_size = hidden_size

        tp_size = get_tensor_model_parallel_world_size()
        self.total_num_heads = num_heads
        self.num_heads = self.total_num_heads // tp_size
        self.total_num_kv_heads = num_kv_heads
        self.num_kv_heads = max(1, self.total_num_kv_heads // tp_size)
        self.head_dim = head_dim
        self.q_size = self.num_heads * self.head_dim
        self.scaling = 1.0

        self.q_proj = ColumnParallelLinear(
            hidden_size,
            self.total_num_heads * self.head_dim,
            bias=config.attention_bias,
            quant_config=None,
            prefix=f"{prefix}.q_proj",
        )
        self.o_proj = RowParallelLinear(
            self.total_num_heads * self.head_dim,
            hidden_size,
            bias=config.attention_bias,
            quant_config=None,
            prefix=f"{prefix}.o_proj",
        )
        self.q_norm = RMSNorm(self.head_dim, eps=config.rms_norm_eps)

        layer_idx = extract_layer_index(prefix)
        layer_type = config.layer_types[layer_idx]
        self.is_sliding = layer_type == "sliding_attention"
        sliding_window = config.sliding_window if self.is_sliding else None

        if layer_type in config.rope_parameters:
            rope_parameters = dict(config.rope_parameters[layer_type])
        else:
            rope_parameters = dict(config.rope_parameters.copy())
            if self.is_sliding:
                rope_parameters["rope_theta"] = getattr(
                    config, "rope_local_base_freq", 10000.0
                )

        self.rotary_emb = get_rope(
            self.head_dim,
            max_position=max_position_embeddings,
            rope_parameters=rope_parameters,
            is_neox_style=True,
        )

        # kv_sharing_target_layer_name is set after model construction
        # by Gemma4Proposer._setup_gemma4_kv_sharing().
        self.is_kv_shared_layer = True
        self.attn = Attention(
            self.num_heads,
            self.head_dim,
            self.scaling,
            num_kv_heads=self.num_kv_heads,
            cache_config=cache_config,
            quant_config=quant_config,
            logits_soft_cap=attn_logits_soft_cap,
            per_layer_sliding_window=sliding_window,
            prefix=f"{prefix}.attn",
        )

    defforward(
        self,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
        **kwargs,
    ) -> torch.Tensor:
        q, _ = self.q_proj(hidden_states)

        q = q.unflatten(-1, (self.num_heads, self.head_dim))
        q = self.q_norm(q)
        q = q.flatten(-2, -1)

        q, _ = self.rotary_emb(positions, q, None)

        # Attention reads K/V from the target's cache via KV sharing;
        # these dummy tensors are never consumed but required by the API.
        num_tokens = q.shape[0]
        kv_dummy = torch.empty(
            num_tokens,
            self.num_kv_heads * self.head_dim,
            dtype=q.dtype,
            device=q.device,
        )
        attn_output = self.attn(q, kv_dummy, kv_dummy)
        output, _ = self.o_proj(attn_output)
        return output
```

## Gemma4MTPMaskedEmbedder [¶](#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder "Permanent link")

Bases: `Module`

Sparse logit computation via centroid-based vocabulary masking.

Instead of computing logits against the full vocabulary, projects hidden states to centroid scores, selects top-K centroids, and computes logits only for the ~top\_k * (vocab\_size / num\_centroids) tokens belonging to those centroids.

Source code in `vllm/model_executor/models/gemma4_mtp.py`

```
classGemma4MTPMaskedEmbedder(nn.Module):
"""Sparse logit computation via centroid-based vocabulary masking.

    Instead of computing logits against the full vocabulary, projects
    hidden states to centroid scores, selects top-K centroids, and
    computes logits only for the ~top_k * (vocab_size / num_centroids)
    tokens belonging to those centroids.
    """

    token_ordering: torch.Tensor

    def__init__(
        self,
        hidden_size: int,
        vocab_size: int,
        num_centroids: int,
        centroid_intermediate_top_k: int,
    ) -> None:
        super().__init__()
        self.hidden_size = hidden_size
        self.vocab_size = vocab_size
        self.num_centroids = num_centroids
        self.centroid_intermediate_top_k = centroid_intermediate_top_k
        self.vocab_size_per_centroid = vocab_size // num_centroids
        self.num_selected = centroid_intermediate_top_k * self.vocab_size_per_centroid

        self.centroids = nn.Linear(hidden_size, num_centroids, bias=False)
        self.register_buffer(
            "token_ordering",
            torch.empty(vocab_size, dtype=torch.long),
        )

    def_select_and_score(
        self,
        hidden_states: torch.Tensor,
        lm_head_weight: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
"""Centroid selection + sparse dot product.

        Returns:
            logits: (num_tokens, num_selected) sparse logits.
            indices: (num_tokens, num_selected) corresponding vocab indices.
        """
        num_tokens = hidden_states.shape[0]
        _, top_k_indices = torch.topk(
            self.centroids(hidden_states),
            k=self.centroid_intermediate_top_k,
            dim=-1,
        )
        clusters = self.token_ordering.view(
            self.num_centroids,
            self.vocab_size_per_centroid,
        )
        selected = clusters[top_k_indices]
        embeddings = lm_head_weight[selected.reshape(-1)].view(
            num_tokens,
            self.num_selected,
            self.hidden_size,
        )
        logits = torch.einsum("td,tsd->ts", hidden_states, embeddings)
        return logits, selected.view(num_tokens, -1)

    defforward(
        self,
        hidden_states: torch.Tensor,
        lm_head_weight: torch.Tensor,
    ) -> torch.Tensor:
"""Full-vocab logits with non-selected positions masked to -inf."""
        logits, indices = self._select_and_score(hidden_states, lm_head_weight)
        output = torch.full(
            (hidden_states.shape[0], self.vocab_size),
            fill_value=torch.finfo(hidden_states.dtype).min,
            dtype=hidden_states.dtype,
            device=hidden_states.device,
        )
        return output.scatter_(-1, indices, logits)

    defget_top_tokens(
        self,
        hidden_states: torch.Tensor,
        lm_head_weight: torch.Tensor,
    ) -> torch.Tensor:
"""Sparse argmax — returns vocab token IDs without full-vocab tensor."""
        logits, indices = self._select_and_score(hidden_states, lm_head_weight)
        return indices.gather(-1, logits.argmax(-1, keepdim=True)).squeeze(-1)
```

### \_select\_and\_score [¶](#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder._select_and_score "Permanent link")

Centroid selection + sparse dot product.

Returns:

Name Type Description `logits` `Tensor`

(num\_tokens, num\_selected) sparse logits.

`indices` `Tensor`

(num\_tokens, num\_selected) corresponding vocab indices.

Source code in `vllm/model_executor/models/gemma4_mtp.py`

```
def_select_and_score(
    self,
    hidden_states: torch.Tensor,
    lm_head_weight: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
"""Centroid selection + sparse dot product.

    Returns:
        logits: (num_tokens, num_selected) sparse logits.
        indices: (num_tokens, num_selected) corresponding vocab indices.
    """
    num_tokens = hidden_states.shape[0]
    _, top_k_indices = torch.topk(
        self.centroids(hidden_states),
        k=self.centroid_intermediate_top_k,
        dim=-1,
    )
    clusters = self.token_ordering.view(
        self.num_centroids,
        self.vocab_size_per_centroid,
    )
    selected = clusters[top_k_indices]
    embeddings = lm_head_weight[selected.reshape(-1)].view(
        num_tokens,
        self.num_selected,
        self.hidden_size,
    )
    logits = torch.einsum("td,tsd->ts", hidden_states, embeddings)
    return logits, selected.view(num_tokens, -1)
```

### forward [¶](#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder.forward "Permanent link")

Full-vocab logits with non-selected positions masked to -inf.

Source code in `vllm/model_executor/models/gemma4_mtp.py`

```
defforward(
    self,
    hidden_states: torch.Tensor,
    lm_head_weight: torch.Tensor,
) -> torch.Tensor:
"""Full-vocab logits with non-selected positions masked to -inf."""
    logits, indices = self._select_and_score(hidden_states, lm_head_weight)
    output = torch.full(
        (hidden_states.shape[0], self.vocab_size),
        fill_value=torch.finfo(hidden_states.dtype).min,
        dtype=hidden_states.dtype,
        device=hidden_states.device,
    )
    return output.scatter_(-1, indices, logits)
```

### get\_top\_tokens [¶](#vllm.model_executor.models.gemma4_mtp.Gemma4MTPMaskedEmbedder.get_top_tokens "Permanent link")

Sparse argmax — returns vocab token IDs without full-vocab tensor.

Source code in `vllm/model_executor/models/gemma4_mtp.py`

```
defget_top_tokens(
    self,
    hidden_states: torch.Tensor,
    lm_head_weight: torch.Tensor,
) -> torch.Tensor:
"""Sparse argmax — returns vocab token IDs without full-vocab tensor."""
    logits, indices = self._select_and_score(hidden_states, lm_head_weight)
    return indices.gather(-1, logits.argmax(-1, keepdim=True)).squeeze(-1)
```

## Gemma4MultiTokenPredictor [¶](#vllm.model_executor.models.gemma4_mtp.Gemma4MultiTokenPredictor "Permanent link")

Bases: `Module`

Source code in `vllm/model_executor/models/gemma4_mtp.py`

```
classGemma4MultiTokenPredictor(nn.Module):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()

        config = vllm_config.speculative_config.draft_model_config.hf_config
        text_config = _get_text_config(config)
        self.config = text_config

        self.hidden_size = text_config.hidden_size
        self.backbone_hidden_size = getattr(
            config, "backbone_hidden_size", self.hidden_size
        )
        self.vocab_size = text_config.vocab_size
        self.num_mtp_layers = text_config.num_hidden_layers

        self.embed_tokens = VocabParallelEmbedding(
            self.vocab_size,
            self.hidden_size,
        )

        self.pre_projection = ColumnParallelLinear(
            2 * self.backbone_hidden_size,
            self.hidden_size,
            bias=False,
            gather_output=True,
            prefix=f"{prefix}.pre_projection",
        )

        self.post_projection = RowParallelLinear(
            self.hidden_size,
            self.backbone_hidden_size,
            bias=False,
            input_is_parallel=False,
            prefix=f"{prefix}.post_projection",
        )

        self.layers = nn.ModuleList(
            Gemma4MTPDecoderLayer(
                text_config,
                cache_config=vllm_config.cache_config,
                quant_config=vllm_config.quant_config,
                prefix=f"{prefix}.layers.{idx}",
            )
            for idx in range(self.num_mtp_layers)
        )

        self.norm = RMSNorm(self.hidden_size, eps=text_config.rms_norm_eps)

        # After embedding sharing, embed_tokens is replaced with the
        # target model's backbone-dim embedding.  Scale by
        # sqrt(backbone_hidden_size) to match the target's convention.
        self.register_buffer(
            "normalizer",
            torch.tensor(self.backbone_hidden_size**0.5),
            persistent=False,
        )

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.embed_tokens(input_ids) * self.normalizer

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        stacked_params_mapping = [
            ("gate_up_proj", "gate_proj", 0),
            ("gate_up_proj", "up_proj", 1),
        ]

        params_dict = dict(self.named_parameters())
        params_dict.update(dict(self.named_buffers()))
        loaded_params: set[str] = set()

        for name, loaded_weight in weights:
            if "rotary_emb.inv_freq" in name:
                continue

            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name:
                    continue
                name = name.replace(weight_name, param_name)
                if name.endswith(".bias") and name not in params_dict:
                    continue
                if name not in params_dict:
                    continue
                param = params_dict[name]
                weight_loader = param.weight_loader
                weight_loader(param, loaded_weight, shard_id)
                break
            else:
                if name.endswith(".bias") and name not in params_dict:
                    continue
                if name not in params_dict:
                    continue
                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                weight_loader(param, loaded_weight)
            loaded_params.add(name)

        return loaded_params

    defforward(
        self,
        input_ids: torch.Tensor,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        spec_step_idx: int = 0,
    ) -> tuple[torch.Tensor, torch.Tensor]:
"""Returns (draft_hidden_states, backbone_hidden_states).

        draft_hidden_states: draft-dim, used by compute_logits via lm_head.
        backbone_hidden_states: backbone-dim, stored in the proposer's
            hidden-state buffer and fed back as input to the next step.
        """
        if inputs_embeds is None:
            inputs_embeds = self.embed_input_ids(input_ids)

        combined = torch.cat([inputs_embeds, hidden_states], dim=-1)
        hidden_states, _ = self.pre_projection(combined)

        residual = None
        for layer in self.layers:
            hidden_states, residual = layer(
                positions=positions,
                hidden_states=hidden_states,
                residual=residual,
            )

        draft_hidden_states = self.norm(hidden_states)

        backbone_hidden_states, _ = self.post_projection(draft_hidden_states)
        return draft_hidden_states, backbone_hidden_states
```

### forward [¶](#vllm.model_executor.models.gemma4_mtp.Gemma4MultiTokenPredictor.forward "Permanent link")

Returns (draft\_hidden\_states, backbone\_hidden\_states).

draft\_hidden\_states: draft-dim, used by compute\_logits via lm\_head. backbone\_hidden\_states: backbone-dim, stored in the proposer's hidden-state buffer and fed back as input to the next step.

Source code in `vllm/model_executor/models/gemma4_mtp.py`

```
defforward(
    self,
    input_ids: torch.Tensor,
    positions: torch.Tensor,
    hidden_states: torch.Tensor,
    intermediate_tensors: IntermediateTensors | None = None,
    inputs_embeds: torch.Tensor | None = None,
    spec_step_idx: int = 0,
) -> tuple[torch.Tensor, torch.Tensor]:
"""Returns (draft_hidden_states, backbone_hidden_states).

    draft_hidden_states: draft-dim, used by compute_logits via lm_head.
    backbone_hidden_states: backbone-dim, stored in the proposer's
        hidden-state buffer and fed back as input to the next step.
    """
    if inputs_embeds is None:
        inputs_embeds = self.embed_input_ids(input_ids)

    combined = torch.cat([inputs_embeds, hidden_states], dim=-1)
    hidden_states, _ = self.pre_projection(combined)

    residual = None
    for layer in self.layers:
        hidden_states, residual = layer(
            positions=positions,
            hidden_states=hidden_states,
            residual=residual,
        )

    draft_hidden_states = self.norm(hidden_states)

    backbone_hidden_states, _ = self.post_projection(draft_hidden_states)
    return draft_hidden_states, backbone_hidden_states
```