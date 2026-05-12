---
title: ovis2_5 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/ovis2_5/
source: sitemap
fetched_at: 2026-05-07T21:32:28.919039622-03:00
rendered_js: false
word_count: 111
summary: This document provides the technical reference for the Ovis 2.5 multimodal model implementation in vLLM, detailing its tensor schemas for image and video patches, visual processor logic, and visual tokenizer integration.
tags:
    - ovis-2-5
    - multimodal-models
    - vllm
    - tensor-schema
    - visual-tokenizer
    - pytorch
category: reference
---

PyTorch Ovis model.

## Ovis2\_5ImagePatchInputs [¶](#vllm.model_executor.models.ovis2_5.Ovis2_5ImagePatchInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bnp: Batch size * number of images * number of patches
- patch\_size: patch\_size\_x * patch\_size\_y * num\_channels
- patch\_indicators: Batch size * (number of patches + 1)
- bn: Batch size * number of images

Source code in `vllm/model_executor/models/ovis2_5.py`

```
classOvis2_5ImagePatchInputs(TensorSchema):
"""
    Dimensions:
        - bnp: Batch size * number of images * number of patches
        - patch_size: patch_size_x * patch_size_y * num_channels
        - patch_indicators: Batch size * (number of patches + 1)
        - bn: Batch size * number of images
    """

    type: Literal["image_patches"]
    flat_data: Annotated[torch.Tensor, TensorShape("bnp", "patch_size")]
    indicator_tokens: Annotated[torch.Tensor, TensorShape("patch_indicators")]
    patches_per_item: Annotated[list[int], TensorShape("bn")]
    grids: Annotated[torch.Tensor, TensorShape("bn", 3)]
```

## Ovis2\_5MultiModalProcessor [¶](#vllm.model_executor.models.ovis2_5.Ovis2_5MultiModalProcessor "Permanent link")

Bases: `BaseMultiModalProcessor[Ovis2_5ProcessingInfo]`

Source code in `vllm/model_executor/models/ovis2_5.py`

```
classOvis2_5MultiModalProcessor(BaseMultiModalProcessor[Ovis2_5ProcessingInfo]):
    defvisual_indicators_to_visual_tokens(
        self,
        visual_indicators: list[int],
    ) -> list[int]:
"""
        Filter image indicators placeholders and convert them to corresponding
        tokens in visual tokenizer.
        """
        hf_config = self.info.get_hf_config()
        vte_vocab_size = hf_config.visual_vocab_size
        return [
            vte_vocab_size - len(INDICATOR_IDS) + (x - INDICATOR_IDS[0])
            for x in visual_indicators
            if x >= INDICATOR_IDS[0]
        ]

    def_call_hf_processor(
        self,
        prompt: str,
        mm_data: Mapping[str, object],
        mm_kwargs: Mapping[str, object],
        tok_kwargs: Mapping[str, object],
    ) -> BatchFeature:
        if not mm_data:
            # Avoid warning from HF logger for text-only input
            tokenizer = self.info.get_tokenizer()
            prompt_ids = tokenizer.encode(prompt, add_special_tokens=False)
            return BatchFeature(dict(input_ids=[prompt_ids]), tensor_type="pt")

        processed_outputs = super()._call_hf_processor(
            prompt=prompt,
            mm_data=mm_data,
            mm_kwargs=mm_kwargs,
            tok_kwargs=tok_kwargs,
        )
        hf_processor = self.info.get_hf_processor()

        if "videos" in mm_data:
            visual_indicators = [
                hf_processor.construct_visual_indicators((1, 1, 1), True)
                for grid in processed_outputs["video_grids"]
            ]
            indicator_tokens = [
                self.visual_indicators_to_visual_tokens(indicator)
                for indicator in visual_indicators
            ]
            processed_outputs["video_indicator_tokens"] = torch.tensor(indicator_tokens)
        if "images" in mm_data:
            visual_indicators = [
                hf_processor.construct_visual_indicators((1, 1, 1), False)
                for grid in processed_outputs["grids"]
            ]
            indicator_tokens = [
                self.visual_indicators_to_visual_tokens(indicator)
                for indicator in visual_indicators
            ]

            processed_outputs["indicator_tokens"] = torch.tensor(indicator_tokens)
        return processed_outputs

    def_apply_hf_processor_tokens_only(
        self,
        prompt_tokens: list[int],
    ) -> list[int]:
        return prompt_tokens

    def_get_mm_fields_config(
        self,
        hf_inputs: BatchFeature,
        hf_processor_mm_kwargs: Mapping[str, object],
    ) -> Mapping[str, MultiModalFieldConfig]:
        return dict(
            pixel_values=MultiModalFieldConfig.batched("image"),
            grids=MultiModalFieldConfig.batched("image"),
            indicator_tokens=MultiModalFieldConfig.batched("image"),
            video_pixel_values=MultiModalFieldConfig.batched("video"),
            video_indicator_tokens=MultiModalFieldConfig.batched("video"),
            video_grids=MultiModalFieldConfig.batched("video"),
        )

    def_get_prompt_updates(
        self,
        mm_items: MultiModalDataItems,
        hf_processor_mm_kwargs: Mapping[str, object],
        out_mm_kwargs: MultiModalKwargsItems,
    ) -> list[PromptReplacement]:
        tokenizer = self.info.get_tokenizer()
        vocab = tokenizer.get_vocab()

        placeholder = {
            "image": vocab[IMAGE_TOKEN],
            "video": vocab[VIDEO_TOKEN],
        }

        defget_replacement_ovis(item_idx, modality: str):
            if modality == "image":
                out_item = out_mm_kwargs["image"][item_idx]
                grid = out_item["grids"].data
            elif modality == "video":
                out_item = out_mm_kwargs["video"][item_idx]
                grid = out_item["video_grids"].data
            hf_processor = self.info.get_hf_processor()
            return hf_processor.construct_visual_placeholders(
                grid[0],
            )

        return [
            PromptReplacement(
                modality=modality,
                target=[placeholder[modality]],
                replacement=partial(get_replacement_ovis, modality=modality),
            )
            for modality in ("image", "video")
        ]
```

### visual\_indicators\_to\_visual\_tokens [¶](#vllm.model_executor.models.ovis2_5.Ovis2_5MultiModalProcessor.visual_indicators_to_visual_tokens "Permanent link")

```
visual_indicators_to_visual_tokens(
    visual_indicators: list[int],
) -> list[int]
```

Filter image indicators placeholders and convert them to corresponding tokens in visual tokenizer.

Source code in `vllm/model_executor/models/ovis2_5.py`

```
defvisual_indicators_to_visual_tokens(
    self,
    visual_indicators: list[int],
) -> list[int]:
"""
    Filter image indicators placeholders and convert them to corresponding
    tokens in visual tokenizer.
    """
    hf_config = self.info.get_hf_config()
    vte_vocab_size = hf_config.visual_vocab_size
    return [
        vte_vocab_size - len(INDICATOR_IDS) + (x - INDICATOR_IDS[0])
        for x in visual_indicators
        if x >= INDICATOR_IDS[0]
    ]
```

## Ovis2\_5VideoPatchInputs [¶](#vllm.model_executor.models.ovis2_5.Ovis2_5VideoPatchInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bnp: Batch size * number of videos * number of patches
- patch\_size: patch\_size\_x * patch\_size\_y * num\_channels
- patch\_indicators: Batch size * (number of patches + 1)
- bn: Batch size * number of videos

Source code in `vllm/model_executor/models/ovis2_5.py`

```
classOvis2_5VideoPatchInputs(TensorSchema):
"""
    Dimensions:
        - bnp: Batch size * number of videos * number of patches
        - patch_size: patch_size_x * patch_size_y * num_channels
        - patch_indicators: Batch size * (number of patches + 1)
        - bn: Batch size * number of videos
    """

    type: Literal["video_patches"]
    flat_data: Annotated[torch.Tensor, TensorShape("bnp", "patch_size")]
    indicator_tokens: Annotated[torch.Tensor, TensorShape("patch_indicators")]
    patches_per_item: Annotated[list[int], TensorShape("bn")]
    grids: Annotated[torch.Tensor, TensorShape("bn", 3)]
```

## VisualTokenizer [¶](#vllm.model_executor.models.ovis2_5.VisualTokenizer "Permanent link")

Bases: `Module`

VIT

Source code in `vllm/model_executor/models/ovis2_5.py`

```
classVisualTokenizer(torch.nn.Module):
"""
    VIT
    """

    def__init__(
        self,
        config: PretrainedConfig,
        visual_vocab_size: int,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        super().__init__()
        self.config = config
        self.vit = self._init_backbone(
            config=config,
            quant_config=quant_config,
            prefix=f"{prefix}.vit",
        )
        # reserved tokens for INDICATOR_IDS
        head_dim = visual_vocab_size - len(INDICATOR_IDS)
        self.head = torch.nn.Sequential(
            ReplicatedLinear(
                self.config.hidden_size * self.config.hidden_stride**2,
                head_dim,
                bias=False,
                return_bias=False,
            ),
            torch.nn.LayerNorm(head_dim),
        )

    def_init_backbone(
        self,
        config: PretrainedConfig,
        quant_config: QuantizationConfig | None = None,
        prefix: str = "",
    ):
        model_type = config.model_type
        if model_type == "siglip2_navit":
            return Siglip2NavitModel(
                config=config,
                quant_config=quant_config,
                prefix=prefix,
            )
        raise ValueError(f"Unsupported visual tokenizer model_type: {model_type}")

    @property
    defdtype(self) -> torch.dtype:
        return next(self.head.parameters()).dtype

    @property
    defdevice(self) -> torch.device:
        return next(self.head.parameters()).device

    deftokenize(self, logits: torch.Tensor) -> torch.Tensor:
        tokens = torch.softmax(logits, dim=-1, dtype=torch.float32).to(logits.dtype)
        return tokens

    defencode(
        self, pixel_values: torch.Tensor, grid_thws: torch.Tensor
    ) -> torch.Tensor:
        features = self.vit(pixel_values, grid_thws)
        # refer to qwen2.5-vl patchmerger
        seq_len, _ = features.shape
        features = features.reshape(seq_len // (self.config.hidden_stride**2), -1)

        return features

    defforward(
        self, pixel_values: torch.Tensor, grid_thws: torch.Tensor
    ) -> torch.Tensor:
        features = self.encode(pixel_values, grid_thws)
        logits = self.head(features)
        tokens = self.tokenize(logits)
        # tokens' shape is [#Token, VocabSize-4],
        # so padding with [#Token, 4], after which,
        # tokens' shape should become [#Token, VocabSize];
        tokens = torch.nn.functional.pad(
            tokens,
            (0, len(INDICATOR_IDS)),
            mode="constant",
            value=0,
        )
        return tokens
```