---
title: keye - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/keye/
source: sitemap
fetched_at: 2026-05-07T21:31:11.036843319-03:00
rendered_js: false
word_count: 349
summary: This document defines the BaseKeyeModule, a base class for implementing multimodal vision-language models in vLLM that supports image and video input processing and embedding.
tags:
    - vllm
    - multimodal
    - computer-vision
    - machine-learning
    - model-architecture
    - pytorch
category: reference
---

## BaseKeyeModule [¶](#vllm.model_executor.models.keye.BaseKeyeModule "Permanent link")

Bases: `Module`, `SupportsMultiModal`

Source code in `vllm/model_executor/models/keye.py`

```
classBaseKeyeModule(nn.Module, SupportsMultiModal):
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

    hf_to_vllm_mapper = WeightsMapper(
        orig_to_new_prefix={
            "lm_head.": "language_model.lm_head.",
            "model.": "language_model.model.",
        }
    )

    @classmethod
    defget_placeholder_str(cls, modality: str, i: int) -> str | None:
        if modality.startswith("image"):
            return "<|vision_start|><|image_pad|><|vision_end|>"
        if modality.startswith("video"):
            return "<|vision_start|><|video_pad|><|vision_end|>"

        raise ValueError("Only image or video modality is supported")

    def__init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
        super().__init__()
        config: PretrainedConfig = vllm_config.model_config.hf_config
        quant_config = vllm_config.quant_config

        self.config = config

        with self._mark_tower_model(vllm_config, {"image", "video"}):
            self.visual = KeyeSiglipVisionModel(
                config.vision_config,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "visual"),
            )
            self.mlp_AR = self._build_projector(
                config,
                config.vision_config,
                quant_config=quant_config,
                prefix=maybe_prefix(prefix, "mlp_AR"),
            )

        with self._mark_language_model(vllm_config):
            self.language_model = init_vllm_registered_model(
                vllm_config=vllm_config,
                prefix=maybe_prefix(prefix, "language_model"),
                architectures=["Qwen3ForCausalLM"],
            )

        self.make_empty_intermediate_tensors = (
            self.language_model.make_empty_intermediate_tensors
        )

    @abstractmethod
    def_build_projector(
        self,
        text_config: PretrainedConfig,
        vision_config: PretrainedConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> nn.Module:
        raise NotImplementedError("Need projector")

    def_process_image_input(self, image_input: Any) -> tuple[torch.Tensor, ...]:
        siglip_position_ids = list()
        image_grid_hws = list()
        sample_indices = list()
        cu_seqlens = [0]

        image_grid_thw = image_input["image_grid_thw"]
        assert image_grid_thw.ndim == 2

        for idx, thaw in enumerate(image_grid_thw):
            thw_tuple = tuple(thaw.detach().cpu().numpy().tolist())
            numel = np.prod(thw_tuple)
            image_grid_hws.append(thw_tuple)
            image_position_ids = torch.arange(numel) % np.prod(thw_tuple[1:])
            siglip_position_ids.append(image_position_ids)
            sample_indices.append(torch.full((numel,), idx, dtype=torch.int64))
            cu_seqlens.append(cu_seqlens[-1] + numel)

        if image_input["type"] == "image_embeds":
            raise ValueError(
                "Image embeddings are not supported for this processing path."
            )
        else:
            pixel_values = image_input["pixel_values"].type(self.visual.dtype)
            siglip_position_ids = torch.concat(siglip_position_ids, dim=0).to(
                pixel_values.device
            )
            cu_seqlens = torch.tensor(cu_seqlens, dtype=torch.int32).to(
                pixel_values.device
            )
            sample_indices = torch.concat(sample_indices, dim=0).to(pixel_values.device)

            image_embeds = self.visual(
                pixel_values=pixel_values,
                image_grid_thw=image_grid_hws,
                position_ids=siglip_position_ids,
                vision_return_embed_list=False,
                interpolate_pos_encoding=True,
                sample_indices=sample_indices,
                cu_seqlens=cu_seqlens,
                use_rope=True,
                window_size=-1,
            )
            image_embeds = tuple(self.mlp_AR(image_embeds, image_grid_thw))
            return image_embeds

    def_process_video_embeds(
        self,
        video_type: Literal["video_embeds", "pixel_values_videos"],
        video_grid_thw: list[torch.Tensor],
        pixel_values_videos: torch.Tensor | None = None,
    ) -> torch.Tensor | list[torch.Tensor]:
        siglip_position_ids = list()
        video_grid_hws = list()
        sample_indices = list()
        cu_seqlens = [0]

        assert video_grid_thw.ndim == 2
        for idx, sub_thw in enumerate(video_grid_thw):
            thw_tuple = tuple(sub_thw.detach().cpu().numpy().tolist())
            numel = np.prod(thw_tuple)

            video_grid_hws.append(thw_tuple)
            video_position_ids = torch.arange(numel) % np.prod(thw_tuple[1:])
            siglip_position_ids.append(video_position_ids)
            sample_indices.append(torch.full((numel,), idx, dtype=torch.int64))
            cu_seqlens.append(cu_seqlens[-1] + numel)

        if video_type == "video_embeds":
            raise ValueError(
                "Video embeddings are not supported for this processing path."
            )
        else:
            pixel_values_videos = pixel_values_videos.type(self.visual.dtype)
            siglip_position_ids = torch.concat(siglip_position_ids, dim=0).to(
                pixel_values_videos.device
            )
            cu_seqlens = torch.tensor(cu_seqlens, dtype=torch.int32).to(
                pixel_values_videos.device
            )
            sample_indices = torch.concat(sample_indices, dim=0).to(
                pixel_values_videos.device
            )

            video_embeds = self.visual(
                pixel_values=pixel_values_videos,
                image_grid_thw=video_grid_hws,
                position_ids=siglip_position_ids,
                vision_return_embed_list=True,
                interpolate_pos_encoding=True,
                sample_indices=sample_indices,
                cu_seqlens=cu_seqlens,
                use_rope=True,
                window_size=-1,
            )
            video_embeds = self.mlp_AR(video_embeds, video_grid_thw)
            return video_embeds

    def_parse_and_validate_multimodal_inputs(self, **kwargs: object) -> dict:
        modalities = {}

        for input_key in kwargs:
            if (
                input_key in ("pixel_values", "image_embeds")
                and "images" not in modalities
            ):
                modalities["images"] = self._parse_and_validate_image_input(**kwargs)
            if (
                input_key in ("pixel_values_videos", "video_embeds")
                and "videos" not in modalities
            ):
                modalities["videos"] = self._parse_and_validate_video_input(**kwargs)

        return modalities

    defembed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings | None:
        modalities = self._parse_and_validate_multimodal_inputs(**kwargs)
        if not modalities:
            return None

        multimodal_embeddings: tuple[torch.Tensor, ...] = ()

        for modality in modalities:
            if modality == "images":
                image_input = modalities["images"]
                image_embeddings = self._process_image_input(image_input)
                multimodal_embeddings += tuple(image_embeddings)
            if modality == "videos":
                video_input = modalities["videos"]
                video_embeddings = self._process_video_input(video_input)
                multimodal_embeddings += tuple(video_embeddings)
        return multimodal_embeddings

    defforward(
        self,
        input_ids: torch.Tensor | None,
        positions: torch.Tensor,
        intermediate_tensors: IntermediateTensors | None = None,
        inputs_embeds: torch.Tensor | None = None,
        **kwargs: object,
    ) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for Keye-VL.

        Args:
            input_ids: Flattened (concatenated) input_ids corresponding to a
                batch.
            positions: Flattened (concatenated) position ids corresponding to a
                batch.
                **NOTE**: If mrope is enabled (default setting for Qwen2-VL
                opensource models), the shape will be `(3, seq_len)`,
                otherwise it will be `(seq_len,)`.
            intermediate_tensors: Intermediate tensors from prior forward pass.
            inputs_embeds: Optional tensor of input embeddings.
        """
        if intermediate_tensors is not None:
            inputs_embeds = None

        hidden_states = self.language_model.model(
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
        return self.language_model.compute_logits(hidden_states)

    defload_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
        loader = AutoWeightsLoader(self)
        return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)

    defget_mm_mapping(self) -> MultiModelKeys:
"""Get the module prefix in multimodal models."""
        return MultiModelKeys.from_string_field(
            language_model="language_model",
            connector="mlp_AR.",
            tower_model="visual.",
        )
```

### forward [¶](#vllm.model_executor.models.keye.BaseKeyeModule.forward "Permanent link")

Run forward pass for Keye-VL.

Parameters:

Name Type Description Default `input_ids` `Tensor | None`

Flattened (concatenated) input\_ids corresponding to a batch.

*required* `positions` `Tensor`

Flattened (concatenated) position ids corresponding to a batch. **NOTE**: If mrope is enabled (default setting for Qwen2-VL opensource models), the shape will be `(3, seq_len)`, otherwise it will be `(seq_len,)`.

*required* `intermediate_tensors` `IntermediateTensors | None`

Intermediate tensors from prior forward pass.

`None` `inputs_embeds` `Tensor | None`

Optional tensor of input embeddings.

`None`

Source code in `vllm/model_executor/models/keye.py`

```
defforward(
    self,
    input_ids: torch.Tensor | None,
    positions: torch.Tensor,
    intermediate_tensors: IntermediateTensors | None = None,
    inputs_embeds: torch.Tensor | None = None,
    **kwargs: object,
) -> torch.Tensor | IntermediateTensors:
"""Run forward pass for Keye-VL.

    Args:
        input_ids: Flattened (concatenated) input_ids corresponding to a
            batch.
        positions: Flattened (concatenated) position ids corresponding to a
            batch.
            **NOTE**: If mrope is enabled (default setting for Qwen2-VL
            opensource models), the shape will be `(3, seq_len)`,
            otherwise it will be `(seq_len,)`.
        intermediate_tensors: Intermediate tensors from prior forward pass.
        inputs_embeds: Optional tensor of input embeddings.
    """
    if intermediate_tensors is not None:
        inputs_embeds = None

    hidden_states = self.language_model.model(
        input_ids=input_ids,
        positions=positions,
        intermediate_tensors=intermediate_tensors,
        inputs_embeds=inputs_embeds,
    )

    return hidden_states
```

### get\_mm\_mapping [¶](#vllm.model_executor.models.keye.BaseKeyeModule.get_mm_mapping "Permanent link")

```
get_mm_mapping() -> MultiModelKeys
```

Get the module prefix in multimodal models.

Source code in `vllm/model_executor/models/keye.py`

```
defget_mm_mapping(self) -> MultiModelKeys:
"""Get the module prefix in multimodal models."""
    return MultiModelKeys.from_string_field(
        language_model="language_model",
        connector="mlp_AR.",
        tower_model="visual.",
    )
```

## KeyeForConditionalGeneration [¶](#vllm.model_executor.models.keye.KeyeForConditionalGeneration "Permanent link")

Bases: `BaseKeyeModule`, `SupportsMultiModal`, `SupportsLoRA`, `SupportsPP`, `SupportsMRoPE`

Source code in `vllm/model_executor/models/keye.py`

```
@MULTIMODAL_REGISTRY.register_processor(
    KeyeMultiModalProcessor,
    info=KeyeProcessingInfo,
    dummy_inputs=KeyeDummyInputsBuilder,
)
classKeyeForConditionalGeneration(
    BaseKeyeModule, SupportsMultiModal, SupportsLoRA, SupportsPP, SupportsMRoPE
):
    def_build_projector(
        self,
        text_config: PretrainedConfig,
        vision_config: PretrainedConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ) -> nn.Module:
        return Projector(text_config, vision_config, quant_config, prefix)

    def_parse_and_validate_image_input(
        self, **kwargs: object
    ) -> KeyeImageInputs | None:
        pixel_values = kwargs.pop("pixel_values", None)
        image_embeds = kwargs.pop("image_embeds", None)
        image_grid_thw = kwargs.pop("image_grid_thw", None)

        if pixel_values is None and image_embeds is None:
            return None

        if pixel_values is not None:
            return KeyeImagePixelInputs(
                type="pixel_values",
                pixel_values=pixel_values,
                image_grid_thw=image_grid_thw,
            )

        if image_embeds is not None:
            return KeyeImageEmbeddingInputs(
                type="image_embeds",
                image_embeds=image_embeds,
                image_grid_thw=image_grid_thw,
            )

    def_parse_and_validate_video_input(
        self, **kwargs: object
    ) -> KeyeVideoInputs | None:
        pixel_values_videos = kwargs.pop("pixel_values_videos", None)
        video_embeds = kwargs.pop("video_embeds", None)
        video_grid_thw = kwargs.pop("video_grid_thw", None)

        if pixel_values_videos is None and video_embeds is None:
            return None

        if pixel_values_videos is not None:
            return KeyeVideoPixelInputs(
                type="pixel_values_videos",
                pixel_values_videos=pixel_values_videos,
                video_grid_thw=video_grid_thw,
            )

        if video_embeds is not None:
            return KeyeVideoEmbeddingInputs(
                type="video_embeds",
                video_embeds=video_embeds,
                video_grid_thw=video_grid_thw,
            )

    def_process_video_input(
        self, video_input: KeyeVideoInputs
    ) -> tuple[torch.Tensor, ...]:
        video_type = video_input["type"]
        video_grid_thw = video_input["video_grid_thw"]
        pixel_values_videos = video_input.get("pixel_values_videos", None)

        return tuple(
            self._process_video_embeds(video_type, video_grid_thw, pixel_values_videos)
        )

    @staticmethod
    def_split_video_grid_thw(
        grid_thw: torch.Tensor | list[list[int]] | list[int],
    ) -> list[list[int]]:
"""
        Split video grid_thw along the t dimension into per-frame rows.

        This preserves Keye's current M-RoPE behavior, where a video is emitted
        as consecutive frame-level multimodal blocks rather than a single block
        spanning the whole video.
        """
        if isinstance(grid_thw, list):
            if len(grid_thw) == 0:
                return []
            if isinstance(grid_thw[0], int):
                grid_thw = torch.tensor([grid_thw], dtype=torch.long)
            else:
                grid_thw = torch.tensor(grid_thw, dtype=torch.long)
        elif grid_thw.ndim == 1:
            grid_thw = grid_thw.unsqueeze(0)

        if grid_thw.numel() == 0:
            return []

        t, hw = grid_thw[:, 0], grid_thw[:, 1:]
        ones = torch.ones_like(hw[:, :1])
        out = torch.cat([ones, hw], dim=1).repeat_interleave(t, dim=0)
        return out.tolist()

    defiter_mm_grid_thw(
        self, mm_features: list[MultiModalFeatureSpec]
    ) -> Iterator[tuple[int, int, int, int]]:
        spatial_merge_size = self.config.vision_config.spatial_merge_size

        for mm_feature in sorted(mm_features, key=lambda f: f.mm_position.offset):
            if mm_feature.data is None:
                raise ValueError("M-RoPE calculation requires multimodal feature data")

            if mm_feature.modality == "image":
                grid_thw = mm_feature.data["image_grid_thw"].data
                if isinstance(grid_thw, torch.Tensor):
                    if grid_thw.ndim == 2:
                        assert grid_thw.shape[0] == 1
                        t, h, w = grid_thw[0].tolist()
                    else:
                        t, h, w = grid_thw.tolist()
                else:
                    if isinstance(grid_thw[0], list):
                        assert len(grid_thw) == 1
                        t, h, w = grid_thw[0]
                    else:
                        t, h, w = grid_thw

                yield (
                    mm_feature.mm_position.offset,
                    t,
                    h // spatial_merge_size,
                    w // spatial_merge_size,
                )
            elif mm_feature.modality == "video":
                current_offset = mm_feature.mm_position.offset
                for t, h, w in self._split_video_grid_thw(
                    mm_feature.data["video_grid_thw"].data
                ):
                    llm_grid_h = h // spatial_merge_size
                    llm_grid_w = w // spatial_merge_size
                    yield (current_offset, t, llm_grid_h, llm_grid_w)
                    current_offset += t * llm_grid_h * llm_grid_w
            else:
                raise ValueError(f"Unsupported modality: {mm_feature.modality}")

    defget_mrope_input_positions(
        self,
        input_tokens: list[int],
        mm_features: list[MultiModalFeatureSpec],
    ) -> tuple[torch.Tensor, int]:
        llm_pos_ids_list: list = []
        st = 0

        for (
            offset,
            llm_grid_t,
            llm_grid_h,
            llm_grid_w,
        ) in self.iter_mm_grid_thw(mm_features):
            text_len = offset - st

            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            llm_pos_ids_list.append(
                torch.arange(text_len).view(1, -1).expand(3, -1) + st_idx
            )

            t_index = (
                (
                    torch.arange(llm_grid_t)
                    .view(-1, 1)
                    .expand(-1, llm_grid_h * llm_grid_w)
                )
                .long()
                .flatten()
            )

            h_index = (
                torch.arange(llm_grid_h)
                .view(1, -1, 1)
                .expand(llm_grid_t, -1, llm_grid_w)
                .flatten()
            )
            w_index = (
                torch.arange(llm_grid_w)
                .view(1, 1, -1)
                .expand(llm_grid_t, llm_grid_h, -1)
                .flatten()
            )
            llm_pos_ids_list.append(
                torch.stack([t_index, h_index, w_index]) + text_len + st_idx
            )
            st = offset + llm_grid_t * llm_grid_h * llm_grid_w

        if st < len(input_tokens):
            st_idx = llm_pos_ids_list[-1].max() + 1 if len(llm_pos_ids_list) > 0 else 0
            text_len = len(input_tokens) - st
            llm_pos_ids_list.append(
                torch.arange(text_len).view(1, -1).expand(3, -1) + st_idx
            )

        llm_positions = torch.cat(llm_pos_ids_list, dim=1).reshape(3, -1)
        mrope_position_delta = (llm_positions.max() + 1 - len(input_tokens)).item()

        return llm_positions, mrope_position_delta
```

### \_split\_video\_grid\_thw `staticmethod` [¶](#vllm.model_executor.models.keye.KeyeForConditionalGeneration._split_video_grid_thw "Permanent link")

Split video grid\_thw along the t dimension into per-frame rows.

This preserves Keye's current M-RoPE behavior, where a video is emitted as consecutive frame-level multimodal blocks rather than a single block spanning the whole video.

Source code in `vllm/model_executor/models/keye.py`

```
@staticmethod
def_split_video_grid_thw(
    grid_thw: torch.Tensor | list[list[int]] | list[int],
) -> list[list[int]]:
"""
    Split video grid_thw along the t dimension into per-frame rows.

    This preserves Keye's current M-RoPE behavior, where a video is emitted
    as consecutive frame-level multimodal blocks rather than a single block
    spanning the whole video.
    """
    if isinstance(grid_thw, list):
        if len(grid_thw) == 0:
            return []
        if isinstance(grid_thw[0], int):
            grid_thw = torch.tensor([grid_thw], dtype=torch.long)
        else:
            grid_thw = torch.tensor(grid_thw, dtype=torch.long)
    elif grid_thw.ndim == 1:
        grid_thw = grid_thw.unsqueeze(0)

    if grid_thw.numel() == 0:
        return []

    t, hw = grid_thw[:, 0], grid_thw[:, 1:]
    ones = torch.ones_like(hw[:, :1])
    out = torch.cat([ones, hw], dim=1).repeat_interleave(t, dim=0)
    return out.tolist()
```

## KeyeImageEmbeddingInputs [¶](#vllm.model_executor.models.keye.KeyeImageEmbeddingInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- nf: Number of image features
- hs: Hidden size (must match the hidden size of language model backbone)
- ni: Number of images
- g: Grid dimensions (3 for t, h, w)

Source code in `vllm/model_executor/models/keye.py`

```
classKeyeImageEmbeddingInputs(TensorSchema):
"""
    Dimensions:
        - nf: Number of image features
        - hs: Hidden size (must match the hidden size of language model
          backbone)
        - ni: Number of images
        - g: Grid dimensions (3 for t, h, w)
    """

    type: Literal["image_embeds"]
    image_embeds: Annotated[torch.Tensor, TensorShape("nf", "hs")]
    image_grid_thw: Annotated[torch.Tensor, TensorShape("ni", 3)]
```

## KeyeImagePixelInputs [¶](#vllm.model_executor.models.keye.KeyeImagePixelInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bnp: Batch size * Number of patches
- c: Number of channels
- ps: Patch size
- ni: Number of images
- g: Grid dimensions (3 for t, h, w)

Source code in `vllm/model_executor/models/keye.py`

```
classKeyeImagePixelInputs(TensorSchema):
"""
    Dimensions:
        - bnp: Batch size * Number of patches
        - c: Number of channels
        - ps: Patch size
        - ni: Number of images
        - g: Grid dimensions (3 for t, h, w)
    """

    type: Literal["pixel_values"]
    pixel_values: Annotated[
        torch.Tensor, TensorShape("bnp", 3, "ps", "ps", dynamic_dims={"bnp"})
    ]
    image_grid_thw: Annotated[torch.Tensor, TensorShape("ni", 3)]
```

## KeyeSiglipAttention [¶](#vllm.model_executor.models.keye.KeyeSiglipAttention "Permanent link")

Bases: `Module`

Multi-headed attention from 'Attention Is All You Need' paper.

Source code in `vllm/model_executor/models/keye.py`

```
classKeyeSiglipAttention(nn.Module):
"""Multi-headed attention from 'Attention Is All You
    Need' paper."""

    def__init__(
        self,
        config: PretrainedConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.config = config

        hidden_size = config.hidden_size
        self.hidden_size = config.hidden_size
        use_data_parallel = is_vit_use_data_parallel()
        tp_size = 1 if use_data_parallel else get_tensor_model_parallel_world_size()
        self.total_num_heads = config.num_attention_heads
        assert self.total_num_heads % tp_size == 0
        self.num_heads = self.total_num_heads // tp_size
        self.total_num_kv_heads = config.num_attention_heads
        if self.total_num_kv_heads >= tp_size:
            assert self.total_num_kv_heads % tp_size == 0
        else:
            assert tp_size % self.total_num_kv_heads == 0
        self.num_kv_heads = max(1, self.total_num_kv_heads // tp_size)
        self.head_dim = config.hidden_size // self.total_num_heads
        self.q_size = self.num_heads * self.head_dim
        self.kv_size = self.num_kv_heads * self.head_dim
        self.scale = self.head_dim**-0.5

        self.qkv_proj = QKVParallelLinear(
            hidden_size,
            self.head_dim,
            self.total_num_heads,
            self.total_num_kv_heads,
            bias=True,
            quant_config=quant_config,
            prefix=f"{prefix}.qkv_proj",
        )
        self.out_proj = RowParallelLinear(
            input_size=hidden_size,
            output_size=hidden_size,
            quant_config=quant_config,
            prefix=f"{prefix}.out_proj",
        )

        self.attn = MMEncoderAttention(
            num_heads=self.num_heads,
            head_size=self.head_dim,
            scale=self.scale,
            num_kv_heads=self.num_kv_heads,
            prefix=f"{prefix}.attn",
        )

        self.apply_rotary_emb = ApplyRotaryEmb(
            enforce_enable=True,
            enable_fp32_compute=True,
        )

    defforward(
        self,
        hidden_states: torch.Tensor,
        attention_mask: torch.Tensor | None = None,
        output_attentions: bool | None = False,
        cu_seqlens: list[torch.Tensor] | None = None,
        rope_emb: tuple[torch.Tensor, torch.Tensor] | None = None,
    ) -> torch.Tensor:
        qkv, _ = self.qkv_proj(hidden_states)
        q, k, v = qkv.split(
            [self.q_size, self.kv_size, self.kv_size],
            dim=-1,
        )

        max_seqlen = (cu_seqlens[1:] - cu_seqlens[:-1]).max()

        if rope_emb is None:
            q = q.view(*q.shape[:-1], self.num_heads, self.head_dim)
            k = k.view(
                *k.shape[:-1],
                self.num_kv_heads,
                self.head_dim,
            )
            v = v.view(
                *v.shape[:-1],
                self.num_kv_heads,
                self.head_dim,
            )
        else:
            if cu_seqlens is None:
                raise ValueError("cu_seqlens cannot be None when rope_emb is not None.")
            cos, sin = rope_emb
            q = q.view(*q.shape[:-1], self.num_heads, self.head_dim)
            k = k.view(
                *k.shape[:-1],
                self.num_kv_heads,
                self.head_dim,
            )
            q, k = apply_rotary_pos_emb_flashatt(q, k, cos, sin, self.apply_rotary_emb)
            v = v.view(
                *v.shape[:-1],
                self.num_kv_heads,
                self.head_dim,
            )

        context_layer = self.attn(
            query=q,
            key=k,
            value=v,
            cu_seqlens=cu_seqlens,
            max_seqlen=max_seqlen,
        )
        context_layer = rearrange(context_layer, "b s h d -> b s (h d)")

        output, _ = self.out_proj(context_layer)
        return output
```

## KeyeVideoEmbeddingInputs [¶](#vllm.model_executor.models.keye.KeyeVideoEmbeddingInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- nf: Number of video features
- hs: Hidden size (must match the hidden size of language model backbone)
- nv: Number of videos
- g: Grid dimensions (3 for t, h, w)

Source code in `vllm/model_executor/models/keye.py`

```
classKeyeVideoEmbeddingInputs(TensorSchema):
"""
    Dimensions:
        - nf: Number of video features
        - hs: Hidden size (must match the hidden size of language model
          backbone)
        - nv: Number of videos
        - g: Grid dimensions (3 for t, h, w)
    """

    type: Literal["video_embeds"]
    video_embeds: Annotated[torch.Tensor, TensorShape("nf", "hs")]
    video_grid_thw: Annotated[torch.Tensor, TensorShape("nv", 3)]
```

## KeyeVideoPixelInputs [¶](#vllm.model_executor.models.keye.KeyeVideoPixelInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bnp: Batch size * Number of patches
- c: Number of channels
- ps: Patch size
- ni: Number of images
- g: Grid dimensions (3 for t, h, w)

Source code in `vllm/model_executor/models/keye.py`

```
classKeyeVideoPixelInputs(TensorSchema):
"""
    Dimensions:
        - bnp: Batch size * Number of patches
        - c: Number of channels
        - ps: Patch size
        - ni: Number of images
        - g: Grid dimensions (3 for t, h, w)
    """

    type: Literal["pixel_values_videos"]
    pixel_values_videos: Annotated[
        torch.Tensor, TensorShape("bnp", 3, "ps", "ps", dynamic_dims={"bnp"})
    ]
    video_grid_thw: Annotated[torch.Tensor, TensorShape("nv", 3)]
```