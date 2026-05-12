---
title: molmo2 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/molmo2/
source: sitemap
fetched_at: 2026-05-07T21:32:05.948260088-03:00
rendered_js: false
word_count: 612
summary: This document provides the technical class definitions and structural configuration for the Molmo2 multimodal language model components within the vLLM framework.
tags:
    - vllm
    - molmo2
    - multimodal
    - deep-learning
    - attention-mechanism
    - neural-networks
    - tensor-parallelism
category: reference
---

## AdapterConfig `dataclass` [¶](#vllm.model_executor.models.molmo2.AdapterConfig "Permanent link")

Config for a vit-llm adapter

Source code in `vllm/model_executor/models/molmo2.py`

```
@dataclass
classAdapterConfig:
"""Config for a vit-llm adapter"""

    vit_layers: tuple[int, int] = (-3, -9)
    pooling_attention_mask: bool = False
    hidden_size: int = 1152
    num_attention_heads: int = 16
    num_key_value_heads: int = 16
    head_dim: int = 72
    hidden_act: str = "silu"
    intermediate_size: int = 18944
    text_hidden_size: int = 3584
```

## ImagePoolingAttention [¶](#vllm.model_executor.models.molmo2.ImagePoolingAttention "Permanent link")

Bases: `Module`

Multi-head attention used for image pooling

Source code in `vllm/model_executor/models/molmo2.py`

```
classImagePoolingAttention(nn.Module):
"""Multi-head attention used for image pooling"""

    def__init__(
        self,
        input_dim: int,
        hidden_size: int,
        num_heads: int,
        num_key_value_heads: int,
        head_dim: int,
        use_bias: bool = True,
        use_pytorch_sdpa: bool = False,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()

        self.input_dim = input_dim
        self.hidden_size = hidden_size
        self.total_num_heads = num_heads
        tp_size = get_tensor_model_parallel_world_size()

        assert self.hidden_size % self.total_num_heads == 0
        assert self.total_num_heads % tp_size == 0

        self.num_heads = self.total_num_heads // tp_size
        self.head_dim = head_dim

        assert self.head_dim == self.hidden_size // self.total_num_heads

        self.total_num_kv_heads = num_key_value_heads
        if self.total_num_kv_heads >= tp_size:
            assert self.total_num_kv_heads % tp_size == 0
        else:
            assert tp_size % self.total_num_kv_heads == 0

        self.num_kv_heads = max(1, self.total_num_kv_heads // tp_size)

        self.kv_size = self.num_kv_heads * self.head_dim

        self.q_proj = ColumnParallelLinear(
            self.input_dim,
            self.total_num_heads * self.head_dim,
            bias=use_bias,
            quant_config=quant_config,
            prefix=f"{prefix}.q_proj",
        )
        self.merged_kv = MergedColumnParallelLinear(
            self.input_dim,
            [self.total_num_kv_heads * self.head_dim] * 2,
            bias=use_bias,
            quant_config=quant_config,
            prefix=f"{prefix}.merged_kv",
        )
        self.o_proj = RowParallelLinear(
            self.total_num_heads * self.head_dim,
            self.hidden_size,
            bias=use_bias,
            quant_config=quant_config,
            prefix=f"{prefix}.o_proj",
        )
        self.scale = self.head_dim**-0.5
        self.use_pytorch_sdpa = use_pytorch_sdpa
        if use_pytorch_sdpa:
            self.attn = None
        else:
            self.attn = MMEncoderAttention(
                self.num_heads,
                self.head_dim,
                self.scale,
                num_kv_heads=self.num_kv_heads,
                prefix=f"{prefix}.attn",
            )

    defforward_sdpa(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        attn_mask: torch.Tensor | None = None,
    ) -> torch.Tensor:
        bsz, q_len, _ = query.size()
        kv_len = key.size(1)

        query = query.view(bsz, q_len, self.num_heads, self.head_dim)
        key = key.view(bsz, kv_len, self.num_kv_heads, self.head_dim)
        value = value.view(bsz, kv_len, self.num_kv_heads, self.head_dim)

        query, key, value = (x.transpose(1, 2) for x in (query, key, value))

        out = F.scaled_dot_product_attention(
            query,
            key,
            value,
            attn_mask=attn_mask,
            is_causal=False,
            enable_gqa=self.num_heads > self.num_kv_heads,
        ).transpose(1, 2)

        return out.reshape(bsz, q_len, -1)

    defforward(
        self,
        inputs_q: torch.Tensor,
        inputs_kv: torch.Tensor,
        attn_mask: torch.Tensor | None = None,
    ) -> torch.Tensor:
        xq, _ = self.q_proj(inputs_q)
        kv, _ = self.merged_kv(inputs_kv)
        xk, xv = kv.split([self.kv_size, self.kv_size], dim=-1)

        if self.use_pytorch_sdpa:
            output = self.forward_sdpa(xq, xk, xv, attn_mask)
        else:
            output = self.attn(xq, xk, xv)

        output, _ = self.o_proj(output)

        return output
```

## ImageProjectorMLP [¶](#vllm.model_executor.models.molmo2.ImageProjectorMLP "Permanent link")

Bases: `Module`

MLP used for the image projector

Source code in `vllm/model_executor/models/molmo2.py`

```
classImageProjectorMLP(nn.Module):
"""MLP used for the image projector"""

    def__init__(
        self,
        input_dim: int,
        hidden_dim: int,
        output_dim: int,
        hidden_act: str,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()

        self.merged_linear = MergedColumnParallelLinear(
            input_dim,
            [hidden_dim] * 2,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.merged_linear",
        )
        # Activation function.
        assert hidden_act == "silu"
        self.act_fn = SiluAndMul()

        # Feed-forward output projection.
        self.down_proj = RowParallelLinear(
            hidden_dim,
            output_dim,
            bias=False,
            quant_config=quant_config,
            prefix=f"{prefix}.down_proj",
        )

    defforward(self, x: torch.Tensor) -> torch.Tensor:
        x, _ = self.merged_linear(x)
        x = self.act_fn(x)
        x, _ = self.down_proj(x)
        return x
```

## LanguageModelMLP [¶](#vllm.model_executor.models.molmo2.LanguageModelMLP "Permanent link")

Bases: `Module`

Molmo2's LLM mlp.

Source code in `vllm/model_executor/models/molmo2.py`

```
classLanguageModelMLP(nn.Module):
"""Molmo2's LLM mlp."""

    def__init__(
        self,
        input_dim: int,
        intermediate_size: int,
        hidden_act: str,
        quant_config: QuantizationConfig | None = None,
    ) -> None:
        super().__init__()

        self.up_gate_proj = MergedColumnParallelLinear(
            input_dim,
            [intermediate_size] * 2,
            bias=False,
            quant_config=quant_config,
        )
        # Activation function.
        assert hidden_act == "silu"
        self.act_fn = MulAndSilu()
        # Feed-forward output projection.
        self.down_proj = RowParallelLinear(
            intermediate_size,
            input_dim,
            bias=False,
            quant_config=quant_config,
        )

    defforward(
        self,
        x: torch.Tensor,
    ) -> torch.Tensor:
        up_gate, _ = self.up_gate_proj(x)
        x = self.act_fn(up_gate)
        x, _ = self.down_proj(x)
        return x
```

## Molmo2Attention [¶](#vllm.model_executor.models.molmo2.Molmo2Attention "Permanent link")

Bases: `Module`

Molmo2's LLM Attention.

Source code in `vllm/model_executor/models/molmo2.py`

```
classMolmo2Attention(nn.Module):
"""Molmo2's LLM Attention."""

    def__init__(
        self,
        config: TextConfig,
        rope_parameters: dict[str, Any],
        cache_config: CacheConfig | None = None,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        self.hidden_size = config.hidden_size
        self.tp_size = get_tensor_model_parallel_world_size()
        self.total_num_heads = config.num_attention_heads

        assert self.hidden_size % self.total_num_heads == 0
        assert self.total_num_heads % self.tp_size == 0

        self.num_heads = self.total_num_heads // self.tp_size
        self.total_num_kv_heads = config.num_key_value_heads
        if self.total_num_kv_heads >= self.tp_size:
            assert self.total_num_kv_heads % self.tp_size == 0
        else:
            assert self.tp_size % self.total_num_kv_heads == 0
        self.num_kv_heads = max(1, self.total_num_kv_heads // self.tp_size)
        self.head_dim = config.head_dim

        self.q_size = self.num_heads * self.head_dim
        self.kv_size = self.num_kv_heads * self.head_dim
        self.max_position_embeddings = config.max_position_embeddings
        self.rope_theta = config.rope_theta

        # Attention input projection. Projects x -> (q, k, v)
        self.qkv_proj = QKVParallelLinear(
            self.hidden_size,
            self.head_dim,
            self.total_num_heads,
            self.total_num_kv_heads,
            bias=config.qkv_bias,
            quant_config=quant_config,
        )

        self.tp_rank: int | None = None
        self.k_norm: nn.Module | None = None
        self.q_norm: nn.Module | None = None
        self.qk_norm_type: str | None = None
        if config.use_qk_norm:
            k_norm_size = (
                self.head_dim
                if config.qk_norm_type == "qwen3"
                else self.total_num_kv_heads * self.head_dim
            )
            self.tp_rank = get_tensor_model_parallel_rank()
            self.k_norm = RMSNorm(k_norm_size, eps=config.layer_norm_eps)
            q_norm_size = (
                self.head_dim
                if config.qk_norm_type == "qwen3"
                else self.total_num_heads * self.head_dim
            )
            self.q_norm = RMSNorm(q_norm_size, eps=config.layer_norm_eps)
            self.qk_norm_type = config.qk_norm_type
        # Rotary embeddings. Rope scaling is only applied on full attention layers.
        layer_idx = extract_layer_index(prefix)
        if (
            config.rope_scaling_layers is not None
            and layer_idx not in config.rope_scaling_layers
        ):
            rope_theta = rope_parameters["rope_theta"]
            rope_parameters = {"rope_type": "default", "rope_theta": rope_theta}
        self.rotary_emb = get_rope(
            self.head_dim,
            max_position=self.max_position_embeddings,
            rope_parameters=rope_parameters,
        )
        self.scaling = self.head_dim**-0.5
        self.attn = Attention(
            self.num_heads,
            self.head_dim,
            self.scaling,
            num_kv_heads=self.num_kv_heads,
            cache_config=cache_config,
            quant_config=quant_config,
            prefix=f"{prefix}.attn",
        )

        # Attention output projection.
        self.o_proj = RowParallelLinear(
            self.total_num_heads * self.head_dim,
            self.hidden_size,
            bias=False,
            quant_config=quant_config,
        )

    def_apply_qk_norm(
        self,
        q: torch.Tensor,
        k: torch.Tensor,
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
        **kwargs: object,
    ) -> torch.Tensor:
        qkv, _ = self.qkv_proj(hidden_states)
        q, k, v = qkv.split([self.q_size, self.kv_size, self.kv_size], dim=-1)
        if (
            self.q_norm is not None
            and self.k_norm is not None
            and self.qk_norm_type == "olmo"
        ):
            q, k = self._apply_qk_norm(q, k)
        elif self.q_norm is not None and self.k_norm is not None:
            q_by_head = q.view(
                *q.shape[:-1],
                q.shape[-1] // self.head_dim,
                self.head_dim,
            )
            q_by_head = self.q_norm(q_by_head)
            q = q_by_head.view(q.shape)
            k_by_head = k.view(
                *k.shape[:-1],
                k.shape[-1] // self.head_dim,
                self.head_dim,
            )
            k_by_head = self.k_norm(k_by_head)
            k = k_by_head.view(k.shape)
        q, k = self.rotary_emb(positions, q, k)
        attn_output = self.attn(q, k, v)

        output, _ = self.o_proj(attn_output)
        return output
```

## Molmo2ForConditionalGeneration [¶](#vllm.model_executor.models.molmo2.Molmo2ForConditionalGeneration "Permanent link")

Bases: `Module`, `SupportsMultiModal`, `SupportsPP`, `SupportsLoRA`, `SupportsQuant`

Source code in `vllm/model_executor/models/molmo2.py`

```
@MULTIMODAL_REGISTRY.register_processor(
    Molmo2MultiModalProcessor,
    info=Molmo2ProcessingInfo,
    dummy_inputs=Molmo2DummyInputsBuilder,
)
classMolmo2ForConditionalGeneration(
    nn.Module, SupportsMultiModal, SupportsPP, SupportsLoRA, SupportsQuant
):
    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_substr={
            # vision backbone mapping
            "image_pooling_2d.wq": "image_pooling_2d.q_proj",
            "image_pooling_2d.wk": "image_pooling_2d.k_proj",
            "image_pooling_2d.wv": "image_pooling_2d.v_proj",
            "image_pooling_2d.wo": "image_pooling_2d.o_proj",
            "image_projector.w1": "image_projector.gate_proj",
            "image_projector.w3": "image_projector.up_proj",
            "image_projector.w2": "image_projector.down_proj",
            # language backbone mapping
            "att_proj": "qkv_proj",
            "attn_out": "o_proj",
            "q_norm": "q_norm",
            "k_norm": "k_norm",
            "ff_proj": "up_gate_proj",
            "ff_out": "down_proj",
            "attn_norm": "input_layernorm",
            "ff_norm": "post_attention_layernorm",
        },
        orig_to_new_prefix={
            # vision backbone mapping
            "model.vision_backbone.": "vision_backbone.",
            # language backbone mapping
            "model.transformer.blocks.": "model.layers.",
            "model.transformer.ln_f.": "model.norm.",
        },
    )

    packed_modules_mapping = {
        "qkv_proj": ["qkv_proj"],
        "up_gate_proj": ["up_gate_proj"],  # language model
        "merged_qkv": ["wq", "wk", "wv"],  # vision backbone
        "merged_kv": ["k_proj", "v_proj"],  # image_pooling_2d
        "merged_linear": ["gate_proj", "up_proj"],  # image_projector
    }

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return IMAGE_PROMPT
        if modality.startswith("video"):
            return VIDEO_PROMPT

        raise ValueError("Only image or video modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config
        multimodal_config = vllm_config.model_config.multimodal_config
        self.config = config
        self.multimodal_config = multimodal_config

        kwargs = {}
        for field in fields(VitConfig):
            kwargs[field.name] = getattr(config.vit_config, field.name)
        vit_config = VitConfig(**kwargs)

        kwargs = {}
        for field in fields(AdapterConfig):
            kwargs[field.name] = getattr(config.adapter_config, field.name)
        adapter_config = AdapterConfig(**kwargs)

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.vision_backbone = Molmo2VisionBackbone(
                vit_config,
                adapter_config,
                quant_config,
                prefix=maybe_prefix(prefix, "vision_backbone"),
            )

        with self._mark_language_model(vllm_config):
            self.model = Molmo2TextModel(
                vllm_config=vllm_config,
                prefix=maybe_prefix(prefix, "model"),
            )

        self.img_patch_id = config.image_patch_id

        if hasattr(config, "text_config"):
            hf_text_config = config.text_config
        else:
            hf_text_config = config.llm_config

        self.lm_head = ParallelLMHead(
            hf_text_config.vocab_size,
            hf_text_config.hidden_size,
            quant_config=quant_config,
        )
        self.logits_processor = LogitsProcessor(hf_text_config.vocab_size)

        self.make_empty_intermediate_tensors = (
            self.model.make_empty_intermediate_tensors
        )

    @property
    defdtype(self):
        return next(self.parameters()).dtype

    def_parse_and_validate_image_input(
        self,
        **kwargs: object,
    ) -> Molmo2ImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        if pixel_values is None:
            return None

        token_pooling = kwargs.pop("image_token_pooling", None)
        num_pooled_patches = kwargs.pop("image_num_pooled_patches", None)
        num_patches = kwargs.pop("image_num_patches", None)
        image_tokens = kwargs.pop("image_tokens", None)
        num_image_tokens = kwargs.pop("num_image_tokens", None)

        accum_patches = [0] + num_patches.cumsum(dim=0)[:-1].tolist()
        patch_offset = 0
        new_token_pooling = token_pooling.clone()
        for i, n in enumerate(num_pooled_patches):
            cur_slice = token_pooling[patch_offset : patch_offset + n]
            index_offset = int(accum_patches[i])
            new_token_pooling[patch_offset : patch_offset + n] = torch.where(
                cur_slice >= 0,
                cur_slice + index_offset,
                cur_slice,
            )
            patch_offset += n

        return Molmo2ImageInputs(
            pixel_values=pixel_values,
            token_pooling=new_token_pooling,
            num_pooled_patches=num_pooled_patches,
            image_tokens=image_tokens,
            num_image_tokens=num_image_tokens,
        )

    def_parse_and_validate_video_input(
        self,
        **kwargs: object,
    ) -> Molmo2VideoInputs | None:
        pixel_values_videos = kwargs.pop("pixel_values_videos", None)
        if pixel_values_videos is None:
            return None

        token_pooling = kwargs.pop("video_token_pooling", None)
        num_pooled_patches = kwargs.pop("video_num_pooled_patches", None)
        num_patches = kwargs.pop("video_num_patches", None)
        video_tokens = kwargs.pop("video_tokens", None)
        num_video_tokens = kwargs.pop("num_video_tokens", None)

        accum_patches = [0] + num_patches.cumsum(dim=0)[:-1].tolist()
        patch_offset = 0
        new_token_pooling = token_pooling.clone()
        for i, n in enumerate(num_pooled_patches):
            cur_slice = token_pooling[patch_offset : patch_offset + n]
            index_offset = int(accum_patches[i])
            new_token_pooling[patch_offset : patch_offset + n] = torch.where(
                cur_slice >= 0,
                cur_slice + index_offset,
                cur_slice,
            )
            patch_offset += n

        return Molmo2VideoInputs(
            pixel_values_videos=pixel_values_videos,
            token_pooling=new_token_pooling,
            num_pooled_patches=num_pooled_patches,
            video_tokens=video_tokens,
            num_video_tokens=num_video_tokens,
        )

    def_parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
        modalities = {}

        for input_key in kwargs:
            if input_key in ("pixel_values",) and "images" not in modalities:
                modalities["images"] = self._parse_and_validate_image_input(**kwargs)
            if input_key in ("pixel_values_videos",) and "videos" not in modalities:
                modalities["videos"] = self._parse_and_validate_video_input(**kwargs)
        return modalities

    def_process_image_input(
        self,
        image_input: Molmo2ImageInputs,
    ) -> tuple[torch.Tensor, ...]:
        pixel_values = image_input["pixel_values"]
        token_pooling = image_input["token_pooling"]
        num_pooled_patches = image_input["num_pooled_patches"]
        image_tokens = image_input["image_tokens"]
        num_image_tokens = image_input["num_image_tokens"]

        image_features_flat = self.vision_backbone(
            images=pixel_values.unsqueeze(0),
            token_pooling=token_pooling.unsqueeze(0),
        )

        assert len(image_features_flat) == num_pooled_patches.sum()
        image_features_list = image_features_flat.split(
            num_pooled_patches.tolist(), dim=0
        )
        image_tokens_list = image_tokens.split(num_image_tokens.tolist(), dim=0)
        out = []
        for image_features_i, image_tokens_i in zip(
            image_features_list, image_tokens_list
        ):
            out_features = self.get_language_model().embed_input_ids(image_tokens_i)
            is_image_patch = image_tokens_i == self.img_patch_id
            out_features[is_image_patch] = image_features_i
            out.append(out_features)
        return tuple(out)

    def_process_video_input(
        self,
        video_input: Molmo2VideoInputs,
    ) -> tuple[torch.Tensor, ...]:
        pixel_values_videos = video_input["pixel_values_videos"]
        token_pooling = video_input["token_pooling"]
        num_pooled_patches = video_input["num_pooled_patches"]
        video_tokens = video_input["video_tokens"]
        num_video_tokens = video_input["num_video_tokens"]

        image_features_flat = self.vision_backbone(
            images=pixel_values_videos.unsqueeze(0),
            token_pooling=token_pooling.unsqueeze(0),
        )

        assert len(image_features_flat) == num_pooled_patches.sum()
        image_features_list = image_features_flat.split(
            num_pooled_patches.tolist(), dim=0
        )
        video_tokens_list = video_tokens.split(num_video_tokens.tolist(), dim=0)
        out = []
        for image_features_i, video_tokens_i in zip(
            image_features_list, video_tokens_list
        ):
            out_features = self.get_language_model().embed_input_ids(video_tokens_i)
            is_image_patch = video_tokens_i == self.img_patch_id
            out_features[is_image_patch] = image_features_i
            out.append(out_features)
        return tuple(out)

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
        modalities = self._parse_and_validate_multimodal_inputs(**kwargs)
        if not modalities:
            return []

        multimodal_embeddings: tuple[torch.Tensor, ...] = ()

        for modality in modalities:
            if modality == "images":
                image_input = modalities["images"]
                image_embeddings = self._process_image_input(image_input)
                multimodal_embeddings += image_embeddings
            if modality == "videos":
                video_input = modalities["videos"]
                video_embeddings = self._process_video_input(video_input)
                multimodal_embeddings += video_embeddings

        return multimodal_embeddings

    defembed_input_ids(
        self,
        input_ids: torch.Tensor,
        multimodal_embeddings: MultiModalEmbeddings | None = None,
        *,
        is_multimodal: torch.Tensor | None = None,
    ) -> torch.Tensor:
        inputs_embeds = self._embed_text_input_ids(
            input_ids,
            self.get_language_model().embed_input_ids,
            is_multimodal=is_multimodal,
        )

        if multimodal_embeddings is None or len(multimodal_embeddings) == 0:
            return inputs_embeds

        if is_multimodal is None:
            raise ValueError(
                "`embed_input_ids` now requires `is_multimodal` arg, "
                "please update your model runner according to "
                "https://github.com/vllm-project/vllm/pull/16229."
            )

        inputs_embeds = _merge_multimodal_embeddings(
            inputs_embeds=inputs_embeds,
            multimodal_embeddings=multimodal_embeddings,
            is_multimodal=is_multimodal,
        )
        return inputs_embeds

    defforward(
        self,
        input_ids: torch.LongTensor,
        positions: torch.LongTensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor:
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.model(
            input_ids,
            positions,
            intermediate_tensors,
            inputs_embeds=inputs_embeds,
            **kwargs,
        )

        return hidden_states

    defcompute_logits(self, hidden_states: torch.Tensor) -> torch.Tensor:
        logits = self.logits_processor(self.lm_head, hidden_states)
        return logits

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]):
        loader = AutoWeightsLoader(self)
        weights = _get_weights_with_merged_embedding(weights)
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)

    defget_mm_mapping(self) -> MultiModelKeys:
"""
        Get the module prefix in multimodal models
        """
        return MultiModelKeys.from_string_field(
            language_model="model",
            connector="vision_backbone.image_projector",
            tower_model="vision_backbone",
        )
```

### get\_mm\_mapping [¶](#vllm.model_executor.models.molmo2.Molmo2ForConditionalGeneration.get_mm_mapping "Permanent link")

```
get_mm_mapping() -> MultiModelKeys
```

Get the module prefix in multimodal models

Source code in `vllm/model_executor/models/molmo2.py`

```
defget_mm_mapping(self) -> MultiModelKeys:
"""
    Get the module prefix in multimodal models
    """
    return MultiModelKeys.from_string_field(
        language_model="model",
        connector="vision_backbone.image_projector",
        tower_model="vision_backbone",
    )
```

## Molmo2ImageInputs [¶](#vllm.model_executor.models.molmo2.Molmo2ImageInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- nc: The total number of crops (dynamic)
- np: The total number of patches per crop
- cps: Number of channels * patch\_size * patch\_size
- npp: Number of pooled patches (dynamic)
- pp: pooling\_size * pooling\_size
- ni: Number of images
- nt: Number of image tokens (dynamic)

Source code in `vllm/model_executor/models/molmo2.py`

```
classMolmo2ImageInputs(TensorSchema):
"""
    Dimensions:
        - nc: The total number of crops (dynamic)
        - np: The total number of patches per crop
        - cps: Number of channels * patch_size * patch_size
        - npp: Number of pooled patches (dynamic)
        - pp: pooling_size * pooling_size
        - ni: Number of images
        - nt: Number of image tokens (dynamic)
    """

    pixel_values: Annotated[torch.Tensor, TensorShape("nc", "np", "cps")]

    token_pooling: Annotated[torch.Tensor, TensorShape("npp", "pp")]
"""
    An index tensor that maps image features to their corresponding
    patch tokens before pooling.
    """

    num_pooled_patches: Annotated[torch.Tensor, TensorShape("ni")]

    image_tokens: Annotated[torch.BoolTensor, TensorShape("nt")]

    num_image_tokens: Annotated[torch.Tensor, TensorShape("ni")]
```

### token\_pooling `instance-attribute` [¶](#vllm.model_executor.models.molmo2.Molmo2ImageInputs.token_pooling "Permanent link")

An index tensor that maps image features to their corresponding patch tokens before pooling.

## Molmo2VideoInputs [¶](#vllm.model_executor.models.molmo2.Molmo2VideoInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- nc: The total number of frames (dynamic)
- np: The total number of patches per frame
- cps: Number of channels * patch\_size * patch\_size
- npp: Number of pooled patches (dynamic)
- pp: pooling\_size * pooling\_size
- nv: Number of videos
- nt: Number of video tokens (dynamic)

Source code in `vllm/model_executor/models/molmo2.py`

```
classMolmo2VideoInputs(TensorSchema):
"""
    Dimensions:
        - nc: The total number of frames (dynamic)
        - np: The total number of patches per frame
        - cps: Number of channels * patch_size * patch_size
        - npp: Number of pooled patches (dynamic)
        - pp: pooling_size * pooling_size
        - nv: Number of videos
        - nt: Number of video tokens (dynamic)
    """

    pixel_values_videos: Annotated[torch.Tensor, TensorShape("nc", "np", "cps")]

    token_pooling: Annotated[torch.Tensor, TensorShape("npp", "pp")]
"""
    An index tensor that maps image features to their corresponding
    patch tokens before pooling.
    """

    num_pooled_patches: Annotated[torch.Tensor, TensorShape("nv")]

    video_tokens: Annotated[torch.BoolTensor, TensorShape("nt")]

    num_video_tokens: Annotated[torch.Tensor, TensorShape("nv")]
```

### token\_pooling `instance-attribute` [¶](#vllm.model_executor.models.molmo2.Molmo2VideoInputs.token_pooling "Permanent link")

An index tensor that maps image features to their corresponding patch tokens before pooling.

## Molmo2VisionBackbone [¶](#vllm.model_executor.models.molmo2.Molmo2VisionBackbone "Permanent link")

Bases: `Module`, `SupportsQuant`

Source code in `vllm/model_executor/models/molmo2.py`

```
classMolmo2VisionBackbone(nn.Module, SupportsQuant):
    packed_modules_mapping = {
        "merged_qkv": ["wq", "wk", "wv"],  # vision backbone
        "merged_kv": ["k_proj", "v_proj"],  # image_pooling_2d
        "merged_linear": ["gate_proj", "up_proj"],
    }

    def__init__(
        self,
        vit_config: VitConfig,
        adapter_config: AdapterConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        self.vit_config = vit_config
        self.adapter_config = adapter_config

        self.vit_layers = []
        for layer in adapter_config.vit_layers:
            if layer >= 0:
                self.vit_layers.append(layer)
            else:
                self.vit_layers.append(layer + vit_config.num_hidden_layers)

        last_layer_needed = max(self.vit_layers) + 1
        if last_layer_needed < vit_config.num_hidden_layers:
            vit_config.num_hidden_layers = last_layer_needed
        self.image_vit = Molmo2VisionTransformer(
            vit_config,
            quant_config,
            prefix=f"{prefix}.image_vit",
        )

        self.num_prefix_tokens: int = self.image_vit.num_prefix_tokens

        pool_dim = vit_config.hidden_size * len(adapter_config.vit_layers)
        self.image_pooling_2d = ImagePoolingAttention(
            input_dim=pool_dim,
            hidden_size=adapter_config.hidden_size,
            num_heads=adapter_config.num_attention_heads,
            num_key_value_heads=adapter_config.num_key_value_heads,
            head_dim=adapter_config.head_dim,
            use_pytorch_sdpa=adapter_config.pooling_attention_mask,
            quant_config=quant_config,
            prefix=f"{prefix}.image_pooling_2d",
        )
        self.image_projector = ImageProjectorMLP(
            input_dim=adapter_config.hidden_size,
            hidden_dim=adapter_config.intermediate_size,
            output_dim=adapter_config.text_hidden_size,
            hidden_act=adapter_config.hidden_act,
            quant_config=quant_config,
            prefix=f"{prefix}.image_projector",
        )

    @property
    defdtype(self) -> torch.dtype:
        return self.image_vit.patch_embedding.weight.dtype

    @property
    defdevice(self) -> torch.device:
        return self.image_vit.patch_embedding.weight.device

    defencode_image(self, images: torch.Tensor) -> torch.Tensor:
"""
        : param images: (batch_size, num_crops, num_patch, n_pixels)
        """
        B, T, N, D = images.shape
        images = images.view(B * T, N, D)
        image_features = self.image_vit(images)

        features = []
        for layer in self.vit_layers:
            features.append(image_features[layer])
        image_features = torch.cat(features, dim=-1)

        if self.num_prefix_tokens > 0:
            image_features = image_features[:, 1:]
        image_features = image_features.view(B, T, N, -1)
        return image_features

    defforward(
        self,
        images: torch.Tensor,
        token_pooling: torch.Tensor,
    ) -> torch.Tensor:
        # image_features shape:
        # (batch_size, num_crops(=num_image), num_patch, nximage_emb_dim)
        batch_size, num_image = images.shape[:2]
        images = images.to(device=self.device, dtype=self.dtype)
        image_features = self.encode_image(images)

        dim = image_features.shape[-1]
        valid = token_pooling >= 0
        valid_token = torch.any(valid, -1)

        # Use `token_pooling` to arange the features for image pooling
        batch_idx = torch.arange(
            token_pooling.shape[0],
            dtype=torch.long,
            device=token_pooling.device,
        )
        batch_idx = torch.tile(
            batch_idx.view(batch_size, 1, 1),
            [1, token_pooling.shape[1], token_pooling.shape[2]],
        )

        # Now [batch, num_features, num_pooled_patches, dim]
        to_pool = image_features.reshape(batch_size, -1, dim)[
            batch_idx, torch.clip(token_pooling, 0)
        ]
        to_pool = to_pool * valid.to(self.dtype)[:, :, :, None]
        to_pool = to_pool.reshape([-1, token_pooling.shape[-1], dim])
        if self.adapter_config.pooling_attention_mask:
            attn_mask = valid.reshape([-1, 1, 1, valid.shape[-1]])
            denom = valid.view(-1, to_pool.shape[-2]).float().sum(-1)
            denom = torch.where(denom == 0, 1, denom)
            query = to_pool.sum(-2, keepdim=True) / denom[:, None, None].to(
                to_pool.dtype
            )
        else:
            attn_mask = None
            query = to_pool.mean(-2, keepdim=True)

        pooled_features = self.image_pooling_2d(query, to_pool, attn_mask=attn_mask)
        pooled_features = pooled_features.reshape(
            [batch_size, -1, pooled_features.shape[-1]]
        )

        # MLP layer to map the feature.
        pooled_features = self.image_projector(pooled_features)
        return pooled_features.view(-1, pooled_features.shape[-1])[
            valid_token.flatten()
        ]

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        stacked_params_mapping = [
            # (param_name, shard_name, shard_id)
            ("merged_qkv", "wq", "q"),
            ("merged_qkv", "wk", "k"),
            ("merged_qkv", "wv", "v"),
            ("merged_kv", "k_proj", 0),
            ("merged_kv", "v_proj", 1),
            ("merged_linear", "gate_proj", 0),
            ("merged_linear", "up_proj", 1),
        ]
        params_dict = dict(self.named_parameters())
        loaded_params: set[str] = set()

        for name, loaded_weight in weights:
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
            else:
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

### encode\_image [¶](#vllm.model_executor.models.molmo2.Molmo2VisionBackbone.encode_image "Permanent link")

: param images: (batch\_size, num\_crops, num\_patch, n\_pixels)

Source code in `vllm/model_executor/models/molmo2.py`

```
defencode_image(self, images: torch.Tensor) -> torch.Tensor:
"""
    : param images: (batch_size, num_crops, num_patch, n_pixels)
    """
    B, T, N, D = images.shape
    images = images.view(B * T, N, D)
    image_features = self.image_vit(images)

    features = []
    for layer in self.vit_layers:
        features.append(image_features[layer])
    image_features = torch.cat(features, dim=-1)

    if self.num_prefix_tokens > 0:
        image_features = image_features[:, 1:]
    image_features = image_features.view(B, T, N, -1)
    return image_features
```

## Molmo2VisionBlock [¶](#vllm.model_executor.models.molmo2.Molmo2VisionBlock "Permanent link")

Bases: `Module`

Residual attention block used in Vision Transformer.

Source code in `vllm/model_executor/models/molmo2.py`

```
classMolmo2VisionBlock(nn.Module):
"""Residual attention block used in Vision Transformer."""

    def__init__(
        self,
        config: VitConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        self.attention = ViTMultiHeadDotProductAttention(
            hidden_size=config.hidden_size,
            num_heads=config.num_attention_heads,
            num_key_value_heads=config.num_key_value_heads,
            head_dim=config.head_dim,
            quant_config=quant_config,
            prefix=f"{prefix}.attention",
        )
        self.feed_forward = ViTMLP(
            dim=config.hidden_size,
            hidden_dim=config.intermediate_size,
            hidden_act=config.hidden_act,
            quant_config=quant_config,
            prefix=f"{prefix}.feed_forward",
        )
        self.attention_norm = nn.LayerNorm(
            config.hidden_size,
            eps=config.layer_norm_eps,
        )
        self.ffn_norm = nn.LayerNorm(
            config.hidden_size,
            eps=config.layer_norm_eps,
        )

    defforward(self, x: torch.Tensor) -> torch.Tensor:
        x = x + self.attention(self.attention_norm(x))
        x = x + self.feed_forward(self.ffn_norm(x))
        return x
```

## Molmo2VisionBlockCollection [¶](#vllm.model_executor.models.molmo2.Molmo2VisionBlockCollection "Permanent link")

Bases: `Module`

Collection of residual attention blocks used in Vision Transformer.

Source code in `vllm/model_executor/models/molmo2.py`

```
classMolmo2VisionBlockCollection(nn.Module):
"""Collection of residual attention blocks used in Vision Transformer."""

    def__init__(
        self,
        config: VitConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        self.resblocks = nn.ModuleList(
            [
                Molmo2VisionBlock(
                    config,
                    quant_config,
                    prefix=f"{prefix}.resblocks.{layer_idx}",
                )
                for layer_idx in range(config.num_hidden_layers)
            ]
        )

    defforward(self, x: torch.Tensor) -> list[torch.Tensor]:
        hidden_states = []
        for r in self.resblocks:
            x = r(x)
            hidden_states.append(x)
        return hidden_states
```

## Molmo2VisionTransformer [¶](#vllm.model_executor.models.molmo2.Molmo2VisionTransformer "Permanent link")

Bases: `Module`

Vision Transformer used in Vision Backbone.

Source code in `vllm/model_executor/models/molmo2.py`

```
classMolmo2VisionTransformer(nn.Module):
"""Vision Transformer used in Vision Backbone."""

    def__init__(
        self,
        config: VitConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        scale = config.hidden_size**-0.5
        self.num_prefix_tokens: int = 0  # no class embeddings
        self.patch_num = config.image_num_patch
        self.positional_embedding = nn.Parameter(
            torch.randn(config.image_num_pos, config.hidden_size) * scale,
        )
        image_patch_size = config.image_patch_size
        self.patch_embedding = nn.Linear(
            image_patch_size * image_patch_size * 3,
            config.hidden_size,
            bias=True,
        )
        self.transformer = Molmo2VisionBlockCollection(
            config,
            quant_config,
            prefix=f"{prefix}.transformer",
        )

    defadd_pos_emb(self, x: torch.Tensor, patch_num: int) -> torch.Tensor:
        pos_emb = self.positional_embedding

        pos_emb = pos_emb.reshape(
            (
                int(math.sqrt(pos_emb.shape[0])),
                int(math.sqrt(pos_emb.shape[0])),
                pos_emb.shape[1],
            )
        )

        (patch_num_0, patch_num_1) = patch_num

        if pos_emb.shape[0] != patch_num_0 or pos_emb.shape[1] != patch_num_1:
            # from https://github.com/facebookresearch/mae/blob/main/util/pos_embed.py
            pos_emb = pos_emb.unsqueeze(0).permute(0, 3, 1, 2)
            pos_emb = F.interpolate(
                pos_emb,
                size=(patch_num_0, patch_num_1),
                mode="bicubic",
                align_corners=False,
                antialias=True,
            )
            pos_emb = pos_emb.permute(0, 2, 3, 1).squeeze(0)

        pos_emb = pos_emb.reshape(-1, pos_emb.shape[-1])
        x = x + pos_emb[None, :, :].to(x.dtype)
        return x

    defforward(
        self,
        x: torch.Tensor,
        patch_num: int | None = None,
    ) -> list[torch.Tensor]:
"""
        : param x: (batch_size, num_patch, n_pixels)
        """
        if patch_num is None:
            patch_num = self.patch_num

        x = self.patch_embedding(x)

        x = self.add_pos_emb(x, patch_num)

        hidden_states = self.transformer(x)
        return hidden_states
```

### forward [¶](#vllm.model_executor.models.molmo2.Molmo2VisionTransformer.forward "Permanent link")

: param x: (batch\_size, num\_patch, n\_pixels)

Source code in `vllm/model_executor/models/molmo2.py`

```
defforward(
    self,
    x: torch.Tensor,
    patch_num: int | None = None,
) -> list[torch.Tensor]:
"""
    : param x: (batch_size, num_patch, n_pixels)
    """
    if patch_num is None:
        patch_num = self.patch_num

    x = self.patch_embedding(x)

    x = self.add_pos_emb(x, patch_num)

    hidden_states = self.transformer(x)
    return hidden_states
```

## TextConfig `dataclass` [¶](#vllm.model_executor.models.molmo2.TextConfig "Permanent link")

Configuration for a text model transformer

Source code in `vllm/model_executor/models/molmo2.py`

```
@dataclass
classTextConfig:
"""Configuration for a text model transformer"""

    hidden_size: int = 3584
"""
    The hidden size of the model.
    """

    num_attention_heads: int = 28
"""
    The number of self-attention heads.
    """

    num_key_value_heads: int = 4
"""
    The number of heads to use for keys and values.
    """

    head_dim: int = 128
"""
    The head dimensionality for the attention mechanism.
    """

    vocab_size: int = 152064
"""Vocabulary size of the model."""

    additional_vocab_size: int = 128
"""Number of additional tokens to have the input embeddings for"""

    qkv_bias: bool = True
"""
    Do QKV projection a bias
    """

    num_hidden_layers: int = 48
"""
    The number of layers/blocks.
    """

    intermediate_size: int = 18944
"""
    The hidden size for the MLP.
    """

    hidden_act: str = "silu"
"""
    The activation function to use within the MLP layers.
    """

    max_position_embeddings: int = 4096
"""
    Max positional embeddings to use in RoPE cache
    """

    rope_theta: float = 1000000.0
"""
    RoPE theta parameter.
    """

    use_qk_norm: bool = False
"""
    Apply layer norm to the keys and queries within the attention mechanism.
    This can help stabilize training.
    """

    qk_norm_type: str = "olmo"
"""
    The type of layer norm to use for the keys and queries.
    Can be "olmo" or "qwen3".
    """

    layer_norm_eps: float = 1e-6
"""
    epsilon for layer norms
    """

    norm_after: bool = False
"""Apply layer norm before and after the attention and MLP blocks."""

    rope_scaling_layers: tuple[int, ...] | None = None
"""
    RoPE scaling layers.
    """
```

### additional\_vocab\_size `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.additional_vocab_size "Permanent link")

```
additional_vocab_size: int = 128
```

Number of additional tokens to have the input embeddings for

### head\_dim `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.head_dim "Permanent link")

The head dimensionality for the attention mechanism.

### hidden\_act `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.hidden_act "Permanent link")

The activation function to use within the MLP layers.

### hidden\_size `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.hidden_size "Permanent link")

The hidden size of the model.

### intermediate\_size `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.intermediate_size "Permanent link")

```
intermediate_size: int = 18944
```

The hidden size for the MLP.

### layer\_norm\_eps `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.layer_norm_eps "Permanent link")

```
layer_norm_eps: float = 1e-06
```

epsilon for layer norms

### max\_position\_embeddings `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.max_position_embeddings "Permanent link")

```
max_position_embeddings: int = 4096
```

Max positional embeddings to use in RoPE cache

### norm\_after `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.norm_after "Permanent link")

Apply layer norm before and after the attention and MLP blocks.

### num\_attention\_heads `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.num_attention_heads "Permanent link")

```
num_attention_heads: int = 28
```

The number of self-attention heads.

### num\_hidden\_layers `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.num_hidden_layers "Permanent link")

```
num_hidden_layers: int = 48
```

The number of layers/blocks.

### num\_key\_value\_heads `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.num_key_value_heads "Permanent link")

```
num_key_value_heads: int = 4
```

The number of heads to use for keys and values.

### qk\_norm\_type `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.qk_norm_type "Permanent link")

```
qk_norm_type: str = 'olmo'
```

The type of layer norm to use for the keys and queries. Can be "olmo" or "qwen3".

### qkv\_bias `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.qkv_bias "Permanent link")

Do QKV projection a bias

### rope\_scaling\_layers `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.rope_scaling_layers "Permanent link")

```
rope_scaling_layers: tuple[int, ...] | None = None
```

RoPE scaling layers.

### rope\_theta `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.rope_theta "Permanent link")

```
rope_theta: float = 1000000.0
```

RoPE theta parameter.

### use\_qk\_norm `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.use_qk_norm "Permanent link")

```
use_qk_norm: bool = False
```

Apply layer norm to the keys and queries within the attention mechanism. This can help stabilize training.

### vocab\_size `class-attribute` `instance-attribute` [¶](#vllm.model_executor.models.molmo2.TextConfig.vocab_size "Permanent link")

Vocabulary size of the model.

## ViTMLP [¶](#vllm.model_executor.models.molmo2.ViTMLP "Permanent link")

Bases: `Module`

MLP used in Vision Transformer.

Source code in `vllm/model_executor/models/molmo2.py`

```
classViTMLP(nn.Module):
"""MLP used in Vision Transformer."""

    def__init__(
        self,
        dim: int,
        hidden_dim: int,
        hidden_act: str,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()
        self.w1 = ColumnParallelLinear(
            dim,
            hidden_dim,
            bias=True,
            quant_config=quant_config,
            prefix=f"{prefix}.w1",
        )
        # Activation function.
        self.act = get_act_fn(hidden_act)
        self.w2 = RowParallelLinear(
            hidden_dim,
            dim,
            bias=True,
            quant_config=quant_config,
            prefix=f"{prefix}.w2",
        )

    defforward(self, x: torch.Tensor) -> torch.Tensor:
        x, _ = self.w1(x)
        x = self.act(x)
        x, _ = self.w2(x)
        return x
```

## ViTMultiHeadDotProductAttention [¶](#vllm.model_executor.models.molmo2.ViTMultiHeadDotProductAttention "Permanent link")

Bases: `Module`

Multi-head attention used in Vision Transformer.

Source code in `vllm/model_executor/models/molmo2.py`

```
classViTMultiHeadDotProductAttention(nn.Module):
"""Multi-head attention used in Vision Transformer."""

    def__init__(
        self,
        hidden_size: int,
        num_heads: int,
        num_key_value_heads: int,
        head_dim: int,
        use_bias: bool = True,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> None:
        super().__init__()

        self.hidden_size = hidden_size
        self.total_num_heads = num_heads
        tp_size = get_tensor_model_parallel_world_size()

        assert self.hidden_size % self.total_num_heads == 0
        assert self.total_num_heads % tp_size == 0

        self.num_heads = self.total_num_heads // tp_size
        self.head_dim = head_dim

        assert self.head_dim == self.hidden_size // self.total_num_heads

        self.total_num_kv_heads = num_key_value_heads
        if self.total_num_kv_heads >= tp_size:
            assert self.total_num_kv_heads % tp_size == 0
        else:
            assert tp_size % self.total_num_kv_heads == 0

        self.num_kv_heads = max(1, self.total_num_kv_heads // tp_size)

        self.q_size = self.num_heads * self.head_dim
        self.kv_size = self.num_kv_heads * self.head_dim

        self.merged_qkv = QKVParallelLinear(
            self.hidden_size,
            self.head_dim,
            self.total_num_heads,
            self.total_num_kv_heads,
            bias=use_bias,
            quant_config=quant_config,
            prefix=f"{prefix}.merged_qkv",
        )
        self.wo = RowParallelLinear(
            self.total_num_heads * self.head_dim,
            self.hidden_size,
            bias=use_bias,
            quant_config=quant_config,
            prefix=f"{prefix}.wo",
        )
        self.scale = self.head_dim**-0.5
        self.attn = MMEncoderAttention(
            self.num_heads,
            self.head_dim,
            self.scale,
            num_kv_heads=self.num_kv_heads,
            prefix=f"{prefix}.attn",
        )

    defforward(self, inputs: torch.Tensor) -> torch.Tensor:
        qkv, _ = self.merged_qkv(inputs)
        xq, xk, xv = qkv.split([self.q_size, self.kv_size, self.kv_size], dim=-1)

        output = self.attn(xq, xk, xv)

        output, _ = self.wo(output)

        return output
```

## VitConfig `dataclass` [¶](#vllm.model_executor.models.molmo2.VitConfig "Permanent link")

Config for a vision transformer

Source code in `vllm/model_executor/models/molmo2.py`

```
@dataclass
classVitConfig:
"""Config for a vision transformer"""

    hidden_size: int = 1152
    intermediate_size: int = 4304
    num_hidden_layers: int = 27
    num_attention_heads: int = 16
    num_key_value_heads: int = 16
    head_dim: int = 72
    hidden_act: str = "gelu_pytorch_tanh"
    layer_norm_eps: float = 1e-6
    image_default_input_size: tuple[int, int] = (378, 378)
    image_patch_size: int = 14
    image_num_pos: int = 577

    def__post_init__(self):
        self.image_default_input_size = tuple(self.image_default_input_size)  # type: ignore[assignment]

    @property
    defimage_num_patch(self):
        h, w = self.image_default_input_size
        return h // self.image_patch_size, w // self.image_patch_size
```

## get\_candidate\_target\_fps [¶](#vllm.model_executor.models.molmo2.get_candidate_target_fps "Permanent link")

Return the subset of `video_fps` factors that remain multiples of `sampling_fps`.

Examples:

```
>>> get_candidate_target_fps(video_fps=6, sampling_fps=2)
[2, 6]
>>> get_candidate_target_fps(video_fps=5, sampling_fps=1)
[1, 5]
>>> get_candidate_target_fps(video_fps=2, sampling_fps=2)
[2]
>>> get_candidate_target_fps(video_fps=5, sampling_fps=2)
Traceback (most recent call last):
...
ValueError: sampling_fps=2 must divide video_fps=5 to produce
    consistent frame steps.
```

Source code in `vllm/model_executor/models/molmo2.py`

```
defget_candidate_target_fps(
    video_fps: int | float,
    sampling_fps: int | float,
    max_fps: int | float = _MAX_VIDEO_FPS,
) -> list[float]:
"""
    Return the subset of `video_fps` factors that remain multiples
    of `sampling_fps`.

    Examples:
        >>> get_candidate_target_fps(video_fps=6, sampling_fps=2)
        [2, 6]
        >>> get_candidate_target_fps(video_fps=5, sampling_fps=1)
        [1, 5]
        >>> get_candidate_target_fps(video_fps=2, sampling_fps=2)
        [2]
        >>> get_candidate_target_fps(video_fps=5, sampling_fps=2)
        Traceback (most recent call last):
            ...
        ValueError: sampling_fps=2 must divide video_fps=5 to produce
            consistent frame steps.
    """
    video_fps = int(video_fps)
    sampling_fps = int(sampling_fps)
    max_fps = int(max_fps)

    if sampling_fps is None:
        raise ValueError("sampling_fps must be provided")
    if video_fps <= 0 or sampling_fps <= 0:
        raise ValueError(
            "video_fps and sampling_fps must be positive "
            f"(got {video_fps}, {sampling_fps})"
        )
    if video_fps % sampling_fps != 0:
        raise ValueError(
            f"sampling_fps={sampling_fps} must divide video_fps={video_fps}."
        )

    candidates = []
    for candidate in range(sampling_fps, video_fps + 1, sampling_fps):
        if candidate > max_fps:
            break
        if video_fps % candidate == 0:
            candidates.append(float(candidate))

    return candidates
```

## get\_target\_fps [¶](#vllm.model_executor.models.molmo2.get_target_fps "Permanent link")

```
get_target_fps(
    video_fps: float,
    max_frames: int,
    total_frames: int,
    frame_sample_mode: str,
    candidate_target_fps: list[float],
) -> float | None
```

Get the target fps that best spans the video and has the most frames sampled

Source code in `vllm/model_executor/models/molmo2.py`

```
defget_target_fps(
    video_fps: float,
    max_frames: int,
    total_frames: int,
    frame_sample_mode: str,
    candidate_target_fps: list[float],
) -> float | None:
"""
    Get the target fps that best spans the video and has the most frames sampled
    """
    num_frames_sampled = 0
    selected_target_fps = None
    for target_fps in candidate_target_fps:
        step_size = max(int(video_fps / target_fps), 1)
        num_frames_sampled_at_fps = int(total_frames / step_size)
        if num_frames_sampled == 0:
            if (
                "uniform" in frame_sample_mode
                and num_frames_sampled_at_fps > max_frames
            ):
                break
            selected_target_fps = target_fps
            num_frames_sampled = num_frames_sampled_at_fps

        else:
            # the candidate sampling fps increases so frame count can't decrease
            assert num_frames_sampled <= num_frames_sampled_at_fps
            if num_frames_sampled_at_fps > max_frames:
                # choose the sampling fps that spans the video
                continue

            elif num_frames_sampled_at_fps > num_frames_sampled:
                # both are less than max_frames; choose the one with higher
                # density of frames sampled
                selected_target_fps = target_fps
                num_frames_sampled = num_frames_sampled_at_fps
    return selected_target_fps
```