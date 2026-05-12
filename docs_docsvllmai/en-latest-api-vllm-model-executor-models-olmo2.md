---
title: olmo2 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/olmo2/
source: sitemap
fetched_at: 2026-05-07T21:32:20.874290574-03:00
rendered_js: false
word_count: 153
summary: This document provides the technical implementation details and class definitions for the OLMo2 model architecture within the vLLM framework, including attention mechanisms, decoder layers, and causal language modeling components.
tags:
    - olmo2
    - vllm
    - transformer
    - attention-mechanism
    - causal-lm
    - model-architecture
category: reference
---

Inference-only OLMo2 model compatible with HuggingFace weights.

## Olmo2Attention [¶](#vllm.model_executor.models.olmo2.Olmo2Attention "Permanent link")

Bases: `Module`

This is the attention block where the output is computed as `Attention(LN(x))` in `MLP(LN(x + Attention(LN(x))))` (plus another skip connection).

Source code in `vllm/model_executor/models/olmo2.py`

```
classOlmo2Attention(nn.Module):
"""
    This is the attention block where the output is computed as
    `Attention(LN(x))` in `MLP(LN(x + Attention(LN(x))))`
    (plus another skip connection).
    """

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        self.config = vllm_config.model_config.hf_config
        assert isinstance(self.config, (Olmo2Config, Olmo3Config))

        hidden_size = self.config.hidden_size
        self.tp_size = get_tensor_model_parallel_world_size()
        self.total_num_heads = self.config.num_attention_heads

        assert hidden_size % self.total_num_heads == 0
        assert self.total_num_heads % self.tp_size == 0

        self.num_heads = self.total_num_heads // self.tp_size
        self.total_num_kv_heads = (
            self.config.num_key_value_heads or self.total_num_heads
        )
        if self.total_num_kv_heads >= self.tp_size:
            assert self.total_num_kv_heads % self.tp_size == 0
        else:
            assert self.tp_size % self.total_num_kv_heads == 0

        self.num_kv_heads = max(1, self.total_num_kv_heads // self.tp_size)
        self.head_dim = hidden_size // self.total_num_heads
        self.q_size = self.num_heads * self.head_dim
        self.kv_size = self.num_kv_heads * self.head_dim
        self.max_position_embeddings = self.config.max_position_embeddings

        # Attention input projection. Projects x -> (q, k, v)
        self.qkv_proj = QKVParallelLinear(
            hidden_size,
            self.head_dim,
            self.total_num_heads,
            self.total_num_kv_heads,
            bias=False,
            quant_config=vllm_config.quant_config,
            prefix=f"{prefix}.qkv_proj",
        )

        self.tp_rank = get_tensor_model_parallel_rank()
        self.k_norm = RMSNorm(
            self.total_num_kv_heads * self.head_dim,
            eps=self.config.rms_norm_eps,
        )
        self.q_norm = RMSNorm(self.config.hidden_size, eps=self.config.rms_norm_eps)

        self.scaling = self.head_dim**-0.5

        layer_idx = extract_layer_index(prefix)
        sliding_window = None
        if (
            layer_types := getattr(self.config, "layer_types", None)
        ) is not None and layer_types[layer_idx] == "sliding_attention":
            sliding_window = self.config.sliding_window

        self.attn = Attention(
            self.num_heads,
            self.head_dim,
            self.scaling,
            num_kv_heads=self.num_kv_heads,
            cache_config=vllm_config.cache_config,
            quant_config=vllm_config.quant_config,
            per_layer_sliding_window=sliding_window,
            prefix=f"{prefix}.attn",
        )

        # Rotary embeddings. Rope scaling is only applied on full attention layers.
        if sliding_window is None:
            rope_parameters = self.config.rope_parameters
        else:
            rope_theta = self.config.rope_parameters["rope_theta"]
            rope_parameters = {"rope_type": "default", "rope_theta": rope_theta}
        self.rotary_emb = get_rope(
            self.head_dim,
            max_position=self.max_position_embeddings,
            rope_parameters=rope_parameters,
        )

        # Attention output projection.
        self.o_proj = RowParallelLinear(
            self.total_num_heads * self.head_dim,
            hidden_size,
            bias=False,
            quant_config=vllm_config.quant_config,
            prefix=f"{prefix}.o_proj",
        )

    def_apply_qk_norm(
        self, q: torch.Tensor, k: torch.Tensor
    ) -> tuple[torch.Tensor, torch.Tensor]:
        if self.tp_size > 1:
            q = tensor_model_parallel_all_gather(q.contiguous())
            k = tensor_model_parallel_all_gather(k.contiguous())
        q = self.q_norm(q)
        k = self.k_norm(k)
        if self.tp_size > 1:
            splitter = partial(split_tensor_along_last_dim, num_partitions=self.tp_size)
            q = splitter(q)[self.tp_rank]
            k = splitter(k)[self.tp_rank]
        return q, k

    defforward(
        self,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor:
        qkv, _ = self.qkv_proj(hidden_states)
        q, k, v = qkv.split([self.q_size, self.kv_size, self.kv_size], dim=-1)
        q, k = self._apply_qk_norm(q, k)
        q, k = self.rotary_emb(positions, q, k)
        attn_output = self.attn(q, k, v)
        output, _ = self.o_proj(attn_output)
        return output
```

## Olmo2DecoderLayer [¶](#vllm.model_executor.models.olmo2.Olmo2DecoderLayer "Permanent link")

Bases: `Module`

This is a typical transformer block where the output is computed as `MLP(LN(x + Attention(LN(x))))` (plus another skip connection).

Source code in `vllm/model_executor/models/olmo2.py`

```
classOlmo2DecoderLayer(nn.Module):
"""
    This is a typical transformer block where the output is
    computed as `MLP(LN(x + Attention(LN(x))))`
    (plus another skip connection).
    """

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        assert isinstance(config, (Olmo2Config, Olmo3Config))
        # Attention block.
        self.self_attn = Olmo2Attention(
            vllm_config=vllm_config, prefix=f"{prefix}.self_attn"
        )

        # MLP block.
        self.mlp = Olmo2MLP(vllm_config=vllm_config, prefix=f"{prefix}.mlp")

        # LayerNorm
        self.post_attention_layernorm = RMSNorm(
            config.hidden_size, eps=config.rms_norm_eps
        )

        self.post_feedforward_layernorm = RMSNorm(
            config.hidden_size, eps=config.rms_norm_eps
        )

    defforward(
        self,
        positions: torch.Tensor,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor:
        # Attention block.
        residual = hidden_states
        hidden_states = self.self_attn(positions, hidden_states)
        hidden_states = self.post_attention_layernorm(hidden_states)
        hidden_states = hidden_states + residual

        # MLP block.
        residual = hidden_states
        hidden_states = self.mlp(hidden_states)
        hidden_states = self.post_feedforward_layernorm(hidden_states)
        hidden_states = residual + hidden_states
        return hidden_states
```

## Olmo2ForCausalLM [¶](#vllm.model_executor.models.olmo2.Olmo2ForCausalLM "Permanent link")

Bases: `Module`, `SupportsPP`, `SupportsLoRA`

Extremely barebones HF model wrapper.

Source code in `vllm/model_executor/models/olmo2.py`

```
classOlmo2ForCausalLM(nn.Module, SupportsPP, SupportsLoRA):
"""
    Extremely barebones HF model wrapper.
    """

    packed_modules_mapping = {
        "qkv_proj": [
            "q_proj",
            "k_proj",
            "v_proj",
        ],
        "gate_up_proj": [
            "gate_proj",
            "up_proj",
        ],
    }

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        assert isinstance(config, (Olmo2Config, Olmo3Config))
        self.config = config
        self.model = Olmo2Model(
            vllm_config=vllm_config, prefix=maybe_prefix(prefix, "model")
        )
        if config.tie_word_embeddings:
            self.lm_head = self.model.embed_tokens
        else:
            self.lm_head = ParallelLMHead(
                config.vocab_size,
                config.hidden_size,
                quant_config=vllm_config.quant_config,
                prefix=maybe_prefix(prefix, "lm_head"),
            )
        self.logits_processor = LogitsProcessor(config.vocab_size)
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
            input_ids=input_ids,
            positions=positions,
            intermediate_tensors=intermediate_tensors,
            inputs_embeds=inputs_embeds,
        )
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        logits = self.logits_processor(self.lm_head, hidden_states)
        return logits

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        loader = AutoWeightsLoader(
            self,
            skip_prefixes=(
                ["lm_head.weight"] if self.config.tie_word_embeddings else None
            ),
        )
        return loader.load_weights(weights)
```

## Olmo2MLP [¶](#vllm.model_executor.models.olmo2.Olmo2MLP "Permanent link")

Bases: `Module`

This is the MLP block where the output is computed as `MLP(x)` in `LN(MLP(x + LN(Attention(x))))` (plus another skip connection).

Source code in `vllm/model_executor/models/olmo2.py`

```
classOlmo2MLP(nn.Module):
"""
    This is the MLP block where the output is computed as
    `MLP(x)` in `LN(MLP(x + LN(Attention(x))))`
    (plus another skip connection).
    """

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        assert isinstance(config, (Olmo2Config, Olmo3Config))
        hidden_size = config.hidden_size
        intermediate_size = config.intermediate_size

        # Feed-forward input projection.
        self.gate_up_proj = MergedColumnParallelLinear(
            hidden_size,
            [intermediate_size] * 2,
            bias=False,
            quant_config=vllm_config.quant_config,
            prefix=f"{prefix}.gate_up_proj",
        )

        # Activation function.
        self.act_fn = SiluAndMul()

        # Feed-forward output projection.
        self.down_proj = RowParallelLinear(
            intermediate_size,
            hidden_size,
            bias=False,
            quant_config=vllm_config.quant_config,
            prefix=f"{prefix}.down_proj",
        )

    defforward(
        self,
        x: torch.Tensor,
    ) -> torch.Tensor:
        gate_up, _ = self.gate_up_proj(x)
        x = self.act_fn(gate_up)
        x, _ = self.down_proj(x)
        return x
```

## Olmo2Model [¶](#vllm.model_executor.models.olmo2.Olmo2Model "Permanent link")

Bases: `Module`

Source code in `vllm/model_executor/models/olmo2.py`

```
@support_torch_compile
classOlmo2Model(nn.Module):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        self.config = vllm_config.model_config.hf_config
        assert isinstance(self.config, (Olmo2Config, Olmo3Config))

        self.embed_tokens = VocabParallelEmbedding(
            self.config.vocab_size,
            self.config.hidden_size,
            prefix=f"{prefix}.embed_tokens",
        )
        self.start_layer, self.end_layer, self.layers = make_layers(
            self.config.num_hidden_layers,
            lambda prefix: Olmo2DecoderLayer(vllm_config=vllm_config, prefix=prefix),
            prefix=f"{prefix}.layers",
        )
        self.norm = RMSNorm(
            self.config.hidden_size,
            eps=self.config.rms_norm_eps,
        )
        self.make_empty_intermediate_tensors = make_empty_intermediate_tensors_factory(
            ["hidden_states"], self.config.hidden_size
        )

    defembed_input_ids(self, input_ids: torch.Tensor) -> torch.Tensor:
        return self.embed_tokens(input_ids)

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None,
        inputs_embeds: torch.Tensor | None = None,
    ) -> torch.Tensor | IntermediateTensors:
"""
        :param input_ids: A tensor of shape `(batch_size, seq_len)`.
        """
        if get_pp_group().is_first_rank:
            if inputs_embeds is not None:
                hidden_states = inputs_embeds
            # Get embeddings of input.
            # shape: (batch_size, seq_len, d_model)
            else:
                hidden_states = self.embed_tokens(input_ids)

        else:
            assert intermediate_tensors is not None
            hidden_states = intermediate_tensors["hidden_states"]
            assert isinstance(hidden_states, torch.Tensor)

        # Apply blocks one-by-one.
        for layer in islice(self.layers, self.start_layer, self.end_layer):
            # shape: (batch_size, seq_len, d_model)
            hidden_states = layer(positions, hidden_states)

        if not get_pp_group().is_last_rank:
            return IntermediateTensors({"hidden_states": hidden_states})

        # Apply final layer norm.
        # shape: (batch_size, seq_len or 1, d_model)
        hidden_states = self.norm(hidden_states)
        return hidden_states

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        stacked_params_mapping = [
            # (param_name, shard_name, shard_id)
            ("qkv_proj", "q_proj", "q"),
            ("qkv_proj", "k_proj", "k"),
            ("qkv_proj", "v_proj", "v"),
            ("gate_up_proj", "gate_proj", 0),
            ("gate_up_proj", "up_proj", 1),
        ]

        params_dict = dict(self.named_parameters(remove_duplicate=False))
        loaded_params: set[str] = set()
        for name, loaded_weight in weights:
            if is_pp_missing_parameter(name, self):
                continue
            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name:
                    continue
                name = name.replace(weight_name, param_name)
                # Skip loading extra bias for GPTQ models.
                if name.endswith(".bias") and name not in params_dict:
                    continue
                param = params_dict[name]
                weight_loader = param.weight_loader  # type: ignore
                weight_loader(param, loaded_weight, shard_id)
                break
            else:
                # Skip loading extra bias for GPTQ models.
                if name.endswith(".bias") and name not in params_dict:
                    continue
                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                weight_loader(param, loaded_weight)
            loaded_params.add(name)
        return loaded_params
```

### forward [¶](#vllm.model_executor.models.olmo2.Olmo2Model.forward "Permanent link")

:param input\_ids: A tensor of shape `(batch_size, seq_len)`.

Source code in `vllm/model_executor/models/olmo2.py`

```
defforward(
    self,
    input_ids: torch.Tensor | None,
    positions: torch.Tensor,
    intermediate_tensors: IntermediateTensors | None,
    inputs_embeds: torch.Tensor | None = None,
) -> torch.Tensor | IntermediateTensors:
"""
    :param input_ids: A tensor of shape `(batch_size, seq_len)`.
    """
    if get_pp_group().is_first_rank:
        if inputs_embeds is not None:
            hidden_states = inputs_embeds
        # Get embeddings of input.
        # shape: (batch_size, seq_len, d_model)
        else:
            hidden_states = self.embed_tokens(input_ids)

    else:
        assert intermediate_tensors is not None
        hidden_states = intermediate_tensors["hidden_states"]
        assert isinstance(hidden_states, torch.Tensor)

    # Apply blocks one-by-one.
    for layer in islice(self.layers, self.start_layer, self.end_layer):
        # shape: (batch_size, seq_len, d_model)
        hidden_states = layer(positions, hidden_states)

    if not get_pp_group().is_last_rank:
        return IntermediateTensors({"hidden_states": hidden_states})

    # Apply final layer norm.
    # shape: (batch_size, seq_len or 1, d_model)
    hidden_states = self.norm(hidden_states)
    return hidden_states
```