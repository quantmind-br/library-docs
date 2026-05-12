---
title: nemotron_parse - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/nemotron_parse/
source: sitemap
fetched_at: 2026-05-07T21:32:17.156411078-03:00
rendered_js: false
word_count: 292
summary: This document defines the structural components for a BART-based transformer decoder, including layer definitions, scaled word embeddings, and parallel language head implementations within the vLLM framework.
tags:
    - bart
    - transformer
    - decoder
    - deep-learning
    - pytorch
    - vllm
    - model-architecture
category: reference
---

## BartDecoderLayer [¶](#vllm.model_executor.models.nemotron_parse.BartDecoderLayer "Permanent link")

Bases: `Module`

Source code in `vllm/model_executor/models/nemotron_parse.py`

```
classBartDecoderLayer(nn.Module):
    def__init__(
        self,
        config: BartConfig,
        cache_config: CacheConfig | None = None,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.embed_dim = config.d_model

        self.self_attn = WhisperAttention(
            embed_dim=self.embed_dim,
            num_heads=config.decoder_attention_heads,
            attn_type=AttentionType.DECODER,
            cache_config=cache_config,
            quant_config=quant_config,
            prefix=f"{prefix}.self_attn",
        )
        self.activation_fn = get_act_fn(config.activation_function)

        self.self_attn_layer_norm = nn.LayerNorm(self.embed_dim)
"""
        afeldman-nm: personally I would call this "cross-attention",
        however I left the name as "encoder_attn" to maintain consistency
        with the name of the pretrained weights.
        """
        self.encoder_attn = WhisperCrossAttention(
            self.embed_dim,
            config.decoder_attention_heads,
            cache_config=cache_config,
            quant_config=quant_config,
            prefix=f"{prefix}.encoder_attn",
        )
        self.encoder_attn_layer_norm = nn.LayerNorm(self.embed_dim)

        ffn_hidden_size = self.embed_dim
        ffn_intermediate_size = config.encoder_ffn_dim
        ffn_has_bias = True
        self.fc1 = ColumnParallelLinear(
            ffn_hidden_size,
            ffn_intermediate_size,
            bias=ffn_has_bias,
            quant_config=quant_config,
            prefix=f"{prefix}.fc1",
        )
        self.fc2 = RowParallelLinear(
            ffn_intermediate_size,
            ffn_hidden_size,
            bias=ffn_has_bias,
            quant_config=quant_config,
            prefix=f"{prefix}.fc2",
        )

        self.final_layer_norm = nn.LayerNorm(self.embed_dim)

    defforward(
        self,
        decoder_hidden_states: torch.Tensor,
        encoder_hidden_states: torch.Tensor | None = None,
    ) -> torch.Tensor:
r"""
        Args:
            decoder_hidden_states: torch.Tensor of *decoder* input embeddings.
            encoder_hidden_states: torch.Tensor of *encoder* input embeddings.
        Returns:
            Decoder layer output torch.Tensor
        """
        residual = decoder_hidden_states

        # Self Attention
        hidden_states = self.self_attn(hidden_states=decoder_hidden_states)

        hidden_states = residual + hidden_states
        hidden_states = self.self_attn_layer_norm(hidden_states)

        # Cross-Attention Block

        residual = hidden_states

        hidden_states = self.encoder_attn(
            hidden_states=hidden_states,
            encoder_hidden_states=encoder_hidden_states,
        )

        hidden_states = residual + hidden_states
        hidden_states = self.encoder_attn_layer_norm(hidden_states)

        # Fully Connected
        residual = hidden_states
        fc1_out, _ = self.fc1(hidden_states)
        hidden_states = self.activation_fn(fc1_out)

        hidden_states, _ = self.fc2(hidden_states)

        hidden_states = residual + hidden_states
        hidden_states = self.final_layer_norm(hidden_states)

        return hidden_states
```

### self\_attn\_layer\_norm `instance-attribute` [¶](#vllm.model_executor.models.nemotron_parse.BartDecoderLayer.self_attn_layer_norm "Permanent link")

afeldman-nm: personally I would call this "cross-attention", however I left the name as "encoder\_attn" to maintain consistency with the name of the pretrained weights.

### forward [¶](#vllm.model_executor.models.nemotron_parse.BartDecoderLayer.forward "Permanent link")

```
forward(
    decoder_hidden_states: Tensor,
    encoder_hidden_states: Tensor | None = None,
) -> Tensor
```

Parameters:

Name Type Description Default `decoder_hidden_states` `Tensor`

torch.Tensor of *decoder* input embeddings.

*required* `encoder_hidden_states` `Tensor | None`

torch.Tensor of *encoder* input embeddings.

`None`

Returns: Decoder layer output torch.Tensor

Source code in `vllm/model_executor/models/nemotron_parse.py`

```
defforward(
    self,
    decoder_hidden_states: torch.Tensor,
    encoder_hidden_states: torch.Tensor | None = None,
) -> torch.Tensor:
r"""
    Args:
        decoder_hidden_states: torch.Tensor of *decoder* input embeddings.
        encoder_hidden_states: torch.Tensor of *encoder* input embeddings.
    Returns:
        Decoder layer output torch.Tensor
    """
    residual = decoder_hidden_states

    # Self Attention
    hidden_states = self.self_attn(hidden_states=decoder_hidden_states)

    hidden_states = residual + hidden_states
    hidden_states = self.self_attn_layer_norm(hidden_states)

    # Cross-Attention Block

    residual = hidden_states

    hidden_states = self.encoder_attn(
        hidden_states=hidden_states,
        encoder_hidden_states=encoder_hidden_states,
    )

    hidden_states = residual + hidden_states
    hidden_states = self.encoder_attn_layer_norm(hidden_states)

    # Fully Connected
    residual = hidden_states
    fc1_out, _ = self.fc1(hidden_states)
    hidden_states = self.activation_fn(fc1_out)

    hidden_states, _ = self.fc2(hidden_states)

    hidden_states = residual + hidden_states
    hidden_states = self.final_layer_norm(hidden_states)

    return hidden_states
```

## BartParallelLMHead [¶](#vllm.model_executor.models.nemotron_parse.BartParallelLMHead "Permanent link")

Bases: `ParallelLMHead`

This module overrides ParallelLMHead's forward by dividing by embeddings scale, yielding effectively the inverse of BartScaledWordEmbedding

Source code in `vllm/model_executor/models/nemotron_parse.py`

```
classBartParallelLMHead(ParallelLMHead):
"""
    This module overrides ParallelLMHead's
    forward by dividing by embeddings scale,
    yielding effectively the inverse of
    BartScaledWordEmbedding
    """

    def__init__(
        self, num_embeddings: int, embedding_dim: int, embed_scale: float = 1.0
    ):
        super().__init__(num_embeddings, embedding_dim)
        self.embed_scale = embed_scale

    defforward(self, input_ids: torch.Tensor) -> torch.Tensor:
        return super().forward(input_ids) / self.embed_scale
```

## BartScaledWordEmbedding [¶](#vllm.model_executor.models.nemotron_parse.BartScaledWordEmbedding "Permanent link")

Bases: `VocabParallelEmbedding`

This module overrides VocabParallelEmbedding's forward by multiplying with embeddings scale.

Source code in `vllm/model_executor/models/nemotron_parse.py`

```
classBartScaledWordEmbedding(VocabParallelEmbedding):
"""
    This module overrides VocabParallelEmbedding's
    forward by multiplying with embeddings scale.
    """

    def__init__(
        self, num_embeddings: int, embedding_dim: int, embed_scale: float = 1.0
    ):
        super().__init__(num_embeddings, embedding_dim)
        self.embed_scale = embed_scale

    defforward(self, input_ids: torch.Tensor) -> torch.Tensor:
        return super().forward(input_ids) * self.embed_scale
```

## MBartDecoderNoPos [¶](#vllm.model_executor.models.nemotron_parse.MBartDecoderNoPos "Permanent link")

Bases: `Module`

Transformer decoder consisting of *config.decoder\_layers* layers. Each layer is a \[`BartDecoderLayer`] Args: config: BartConfig embed\_tokens (nn.Embedding): output embedding

Source code in `vllm/model_executor/models/nemotron_parse.py`

```
classMBartDecoderNoPos(nn.Module):
"""
    Transformer decoder consisting of *config.decoder_layers* layers.
    Each layer is a [`BartDecoderLayer`]
    Args:
        config: BartConfig
        embed_tokens (nn.Embedding): output embedding
    """

    def__init__(
        self,
        config: BartConfig,
        cache_config: CacheConfig | None = None,
        quant_config: QuantizationConfig | None = None,
        lora_config: LoRAConfig | None = None,
        embed_tokens: nn.Embedding | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.cache_config = cache_config
        self.quant_config = quant_config
        self.lora_config = lora_config
        embed_scale = math.sqrt(config.d_model) if config.scale_embedding else 1.0

        self.embed_tokens = BartScaledWordEmbedding(
            config.vocab_size, config.d_model, embed_scale=embed_scale
        )

        if embed_tokens is not None:
            self.embed_tokens.weight = embed_tokens.weight

        self.layers = nn.ModuleList(
            [
                MBartDecoderLayer(
                    config,
                    cache_config,
                    quant_config,
                    prefix=f"{prefix}.layers.{layer_idx}",
                )
                for layer_idx in range(config.decoder_layers)
            ]
        )

        self.layernorm_embedding = nn.LayerNorm(config.d_model)
        self.layer_norm = nn.LayerNorm(config.d_model)

    defforward(
        self,
        decoder_input_ids: torch.Tensor | None,
        *,
        encoder_hidden_states: torch.Tensor | None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs,
    ) -> torch.Tensor:
r"""
        Args:
            decoder_input_ids: Indices of *decoder* input sequence tokens in the
                vocabulary. Padding will be ignored by default should you provide it.
            encoder_hidden_states: Tensor of encoder output embeddings
        Returns:
            Decoder output torch.Tensor
        """
        if inputs_embeds is None:
            inputs_embeds = self.embed_tokens(decoder_input_ids)

        hidden_states = self.layernorm_embedding(inputs_embeds)

        # decoder layers

        for decoder_layer in self.layers:
            hidden_states = decoder_layer(
                decoder_hidden_states=hidden_states,
                encoder_hidden_states=encoder_hidden_states,
            )

        hidden_states = self.layer_norm(hidden_states)
        return hidden_states

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        stacked_params_mapping = [
            # (param_name, shard_name, shard_id)
            (".self_attn.qkv_proj", ".self_attn.q_proj", "q"),
            (".self_attn.qkv_proj", ".self_attn.k_proj", "k"),
            (".self_attn.qkv_proj", ".self_attn.v_proj", "v"),
            # MergedColumnParallelLinear uses integer indices (0, 1)
            (".encoder_attn.kv_proj", ".encoder_attn.k_proj", 0),
            (".encoder_attn.kv_proj", ".encoder_attn.v_proj", 1),
        ]
        params_dict = dict(self.named_parameters())
        loaded_params: set[str] = set()
        for name, loaded_weight in weights:
            if name.startswith("embed_positions"):
                continue

            for param_name, weight_name, shard_id in stacked_params_mapping:
                if weight_name not in name:
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

                param = params_dict[name]
                weight_loader = getattr(param, "weight_loader", default_weight_loader)
                weight_loader(param, loaded_weight)
            loaded_params.add(name)
        return loaded_params
```

### forward [¶](#vllm.model_executor.models.nemotron_parse.MBartDecoderNoPos.forward "Permanent link")

```
forward(
    decoder_input_ids: Tensor | None,
    *,
    encoder_hidden_states: Tensor | None,
    inputs_embeds: Tensor | None = None,
    **kwargs,
) -> Tensor
```

Parameters:

Name Type Description Default `decoder_input_ids` `Tensor | None`

Indices of *decoder* input sequence tokens in the vocabulary. Padding will be ignored by default should you provide it.

*required* `encoder_hidden_states` `Tensor | None`

Tensor of encoder output embeddings

*required*

Returns: Decoder output torch.Tensor

Source code in `vllm/model_executor/models/nemotron_parse.py`

```
defforward(
    self,
    decoder_input_ids: torch.Tensor | None,
    *,
    encoder_hidden_states: torch.Tensor | None,
    inputs_embeds: torch.Tensor | None = None,
    **kwargs,
) -> torch.Tensor:
r"""
    Args:
        decoder_input_ids: Indices of *decoder* input sequence tokens in the
            vocabulary. Padding will be ignored by default should you provide it.
        encoder_hidden_states: Tensor of encoder output embeddings
    Returns:
        Decoder output torch.Tensor
    """
    if inputs_embeds is None:
        inputs_embeds = self.embed_tokens(decoder_input_ids)

    hidden_states = self.layernorm_embedding(inputs_embeds)

    # decoder layers

    for decoder_layer in self.layers:
        hidden_states = decoder_layer(
            decoder_hidden_states=hidden_states,
            encoder_hidden_states=encoder_hidden_states,
        )

    hidden_states = self.layer_norm(hidden_states)
    return hidden_states
```

## NemotronParseForConditionalGeneration [¶](#vllm.model_executor.models.nemotron_parse.NemotronParseForConditionalGeneration "Permanent link")

Bases: `Module`, `SupportsMultiModal`

Source code in `vllm/model_executor/models/nemotron_parse.py`

```
@MULTIMODAL_REGISTRY.register_processor(
    NemotronParseMultiModalProcessor,
    info=NemotronParseProcessingInfo,
    dummy_inputs=NemotronParseDummyInputsBuilder,
)
classNemotronParseForConditionalGeneration(nn.Module, SupportsMultiModal):
    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config

        self.config = config
        self.vision_config = config.encoder
        cache_config = vllm_config.cache_config
        quant_config = vllm_config.quant_config

        with self._mark_tower_model(vllm_config, "image"):
            self.encoder = RadioWithNeck(
                config=config, quant_config=quant_config, prefix=f"{prefix}.encoder"
            )

        with self._mark_language_model(vllm_config):
            self.decoder = MBartDecoderNoPos(
                config.decoder,
                cache_config=cache_config,
                quant_config=quant_config,
                prefix=f"{prefix}.decoder",
            )

        self.vocab_size = config.decoder.vocab_size
        self.lm_head = ParallelLMHead(
            config.decoder.vocab_size, config.decoder.d_model, quant_config=quant_config
        )
        self.logits_processor = LogitsProcessor(
            self.vocab_size, config.decoder.vocab_size
        )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return None

        raise ValueError("Only image modality is supported")

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> NemotronParsePixelInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_embeds = kwargs.pop("image_embeds", None)

        if pixel_values is None and image_embeds is None:
            return None

        if pixel_values is not None and image_embeds is not None:
            raise ValueError("Both pixel values and image embeds are provided.")

        if pixel_values is not None:
            h, w = self.config.image_size
            return NemotronParsePixelInputs(
                type="pixel_values",
                data=pixel_values,
                resolve_bindings={
                    "h": h,
                    "w": w,
                },
            )

        if image_embeds is not None:
            raise NotImplementedError

        raise AssertionError("This line should be unreachable.")

    def_process_image_input(
        self, image_input: NemotronParsePixelInputs
    ) -> torch.Tensor:
        assert image_input["type"] == "pixel_values"
        pixel_values = image_input["data"]
        dtype = next(self.encoder.parameters()).dtype
        pixel_values = pixel_values.to(dtype)
        return self.encoder(pixel_values)

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
        image_input = self._parse_and_validate_image_input(**kwargs)
        if image_input is None:
            return None
        vision_embeddings = self._process_image_input(image_input)
        return vision_embeddings

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        encoder_outputs: list[torch.Tensor] | None = None,
        **kwargs,
    ) -> torch.Tensor:
r"""
        Args:
            input_ids: torch.Tensor of *decoder* input token ids.
            positions: torch.Tensor of *decoder* position indices.
            encoder_outputs: List of encoder output tensors (vision embeddings).
                During profiling, this may be None or empty.
        Returns:
            Output torch.Tensor
        """
        inputs_embeds = None
        if encoder_outputs:
            inputs_embeds = torch.cat(encoder_outputs, dim=0)
        hidden_states = self.decoder(
            decoder_input_ids=input_ids, encoder_hidden_states=inputs_embeds
        )
        return hidden_states

    defcompute_logits(
        self,
        hidden_states: torch.Tensor,
    ) -> torch.Tensor | None:
        return self.logits_processor(self.lm_head, hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        lm_head_dict = dict(self.lm_head.named_parameters())

        defis_encoder(name: str) -> bool:
            return name.startswith("encoder")

        defis_decoder(name: str) -> bool:
            return name.startswith("decoder")

        defis_lm_head(name: str):
            return name.startswith("lm_head")

        # Separate weights by component
        encoder_weights = []
        decoder_weights = []

        for name, w in weights:
            if is_encoder(name):
                encoder_weights.append((".".join(name.split(".")[1:]), w))
            elif is_decoder(name):
                decoder_weights.append((".".join(name.split(".")[1:]), w))
            elif is_lm_head(name):
                trimmed_name = ".".join(name.split(".")[1:])
                param = lm_head_dict[trimmed_name]
                with torch.no_grad():
                    default_weight_loader(param, w)
            else:
                logger.info("Found unexpected weight: %s", name)

        # Load encoder weights
        self.encoder.load_weights(encoder_weights)
        # Load decoder weights
        self.decoder.load_weights(decoder_weights)
```

### forward [¶](#vllm.model_executor.models.nemotron_parse.NemotronParseForConditionalGeneration.forward "Permanent link")

Parameters:

Name Type Description Default `input_ids` `Tensor | None`

torch.Tensor of *decoder* input token ids.

*required* `positions` `Tensor`

torch.Tensor of *decoder* position indices.

*required* `encoder_outputs` `list[Tensor] | None`

List of encoder output tensors (vision embeddings). During profiling, this may be None or empty.

`None`

Returns: Output torch.Tensor

Source code in `vllm/model_executor/models/nemotron_parse.py`

```
defforward(
    self,
    input_ids: torch.Tensor | None,
    positions: torch.Tensor,
    encoder_outputs: list[torch.Tensor] | None = None,
    **kwargs,
) -> torch.Tensor:
r"""
    Args:
        input_ids: torch.Tensor of *decoder* input token ids.
        positions: torch.Tensor of *decoder* position indices.
        encoder_outputs: List of encoder output tensors (vision embeddings).
            During profiling, this may be None or empty.
    Returns:
        Output torch.Tensor
    """
    inputs_embeds = None
    if encoder_outputs:
        inputs_embeds = torch.cat(encoder_outputs, dim=0)
    hidden_states = self.decoder(
        decoder_input_ids=input_ids, encoder_hidden_states=inputs_embeds
    )
    return hidden_states
```

## NemotronParsePixelInputs [¶](#vllm.model_executor.models.nemotron_parse.NemotronParsePixelInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- b: Batch size
- c: Number of channels (3)
- h: Height
- w: Width

Source code in `vllm/model_executor/models/nemotron_parse.py`

```
classNemotronParsePixelInputs(TensorSchema):
"""
    Dimensions:
        - b: Batch size
        - c: Number of channels (3)
        - h: Height
        - w: Width
    """

    type: Literal["pixel_values"]
    data: Annotated[torch.Tensor, TensorShape("b", 3, "h", "w")]
```

## RadioWithNeck [¶](#vllm.model_executor.models.nemotron_parse.RadioWithNeck "Permanent link")

Bases: `Module`

Vision encoder using RADIO model with custom neck.

Source code in `vllm/model_executor/models/nemotron_parse.py`

```
classRadioWithNeck(nn.Module):
"""Vision encoder using RADIO model with custom neck."""

    def__init__(
        self,
        config: PretrainedConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.config = config.encoder

        self.model_encoder = self.get_vit_model_from_radio_config(
            config, quant_config=quant_config
        )

        # Neck components
        last_hidden_state = 1024
        self.conv1 = nn.Conv1d(1280, last_hidden_state, 1)
        self.layer_norm1 = nn.LayerNorm(
            last_hidden_state, eps=1e-06, elementwise_affine=True
        )
        self.conv2 = nn.Conv2d(
            last_hidden_state,
            last_hidden_state,
            kernel_size=(1, 4),
            stride=(1, 4),
            padding=0,
            bias=False,
        )
        self.layer_norm2 = nn.LayerNorm(
            last_hidden_state, eps=1e-06, elementwise_affine=True
        )
        self.sum_proj = ColumnParallelLinear(
            3840,
            last_hidden_state,
            quant_config=quant_config,
            prefix=f"{prefix}.sum_proj",
        )
        self.layer_norm3 = nn.LayerNorm(
            last_hidden_state, eps=1e-06, elementwise_affine=True
        )

    defget_vit_model_from_radio_config(
        self,
        hf_config: PretrainedConfig,
        quant_config: QuantizationConfig | None = None,
    ) -> RadioModel:
        hf_config_vision = hf_config.encoder
        model_name = hf_config_vision.args.get("model")
        if model_name is None:
            raise ValueError(f"Unsupported vit model type: {model_name}")

        radio_config = RadioConfig(
            model_name=model_name,
            image_size=hf_config.image_size,
            **hf_config_vision.args,
        )

        return RadioModel(config=radio_config, quant_config=quant_config)

    defforward(self, pixel_values: torch.Tensor, **kwargs) -> torch.Tensor:
        summary, feature = self.model_encoder(pixel_values)

        output = self.conv1(feature.permute(0, 2, 1)).permute(0, 2, 1)
        output = self.layer_norm1(output)

        patch_size = self.config.patch_size
        output = rearrange(
            output,
            "b (h w) d -> b d h w",
            h=pixel_values.shape[-2] // patch_size,
            w=pixel_values.shape[-1] // patch_size,
        )

        output = self.conv2(output)
        output = rearrange(output, "b d h w -> b (h w) d")
        output = self.layer_norm2(output)
        summary = self.layer_norm3(self.sum_proj(summary)[0])
        output = torch.cat((output, summary.unsqueeze(1)), dim=1)

        return output

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        model_encoder_weights = []
        adaptor_dict = {
            name: param
            for name, param in dict(self.named_parameters()).items()
            if not name.startswith("model_encoder")
        }
        for name, w in weights:
            if name.startswith("model_encoder"):
                model_encoder_weights.append((".".join(name.split(".")[1:]), w))
            else:
                param = adaptor_dict[name]
                with torch.no_grad():
                    default_weight_loader(param, w)

        self.model_encoder.load_weights(model_encoder_weights)
```