---
title: nemotron_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/nemotron_vl/
source: sitemap
fetched_at: 2026-05-07T21:38:07.225883173-03:00
rendered_js: false
word_count: 94
summary: This document defines the processor classes and transformation utilities required to handle image inputs for Llama-3.1-Nemotron-Nano-VL models within the vLLM framework.
tags:
    - vllm
    - processor
    - vision-language
    - nemotron
    - image-processing
    - siglip
category: reference
---

## LlamaNemotronNanoVLProcessor [¶](#vllm.transformers_utils.processors.nemotron_vl.LlamaNemotronNanoVLProcessor "Permanent link")

Bases: `InternVLProcessor`

This model doesn't define its own HF processor, so we implement our own one here.

The image processor is given by: https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/image\_processing.py

Source code in `vllm/transformers_utils/processors/nemotron_vl.py`

```
classLlamaNemotronNanoVLProcessor(InternVLProcessor):
"""
    This model doesn't define its own HF processor,
    so we implement our own one here.

    The image processor is given by:
    https://huggingface.co/nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1/blob/main/image_processing.py
    """

    def__init__(
        self,
        image_processor: LlamaNemotronNanoVLImageProcessor,
        tokenizer: HfTokenizer,
        *,
        image_seq_length: int,
        start_image_token: str = "<img>",
        end_image_token: str = "</img>",
        ctx_image_token: str = "<image>",
    ) -> None:
        super().__init__(
            image_processor=image_processor,
            tokenizer=tokenizer,
            image_seq_length=image_seq_length,
            start_image_token=start_image_token,
            end_image_token=end_image_token,
            ctx_image_token=ctx_image_token,
        )

    defget_num_image_tokens(
        self,
        *,
        image_width: int,
        image_height: int,
    ) -> int:
        image_processor = self.image_processor
        target_ratios = self.resolve_target_ratios(
            use_thumbnail=False,  # Applied in calculate_targets
        )

        num_patches, _, _ = calculate_nemotron_vl_targets(
            orig_width=image_width,
            orig_height=image_height,
            image_size=image_processor.image_size,
            target_ratios=target_ratios,
            use_thumbnail=image_processor.use_thumbnail,
        )

        return num_patches * self.image_seq_length
```

## LlamaNemotronVLEmbedProcessor [¶](#vllm.transformers_utils.processors.nemotron_vl.LlamaNemotronVLEmbedProcessor "Permanent link")

Bases: `InternVLProcessor`

Processor for LlamaNemotronVL embedding model.

Inherits from NemotronVLProcessor and specializes it for embedding tasks: - Uses SigLIP transform with normalization instead of base transform - Uses different image context token ( vs []())

Source code in `vllm/transformers_utils/processors/nemotron_vl.py`

```
classLlamaNemotronVLEmbedProcessor(InternVLProcessor):
"""
    Processor for LlamaNemotronVL embedding model.

    Inherits from NemotronVLProcessor and specializes it for embedding tasks:
    - Uses SigLIP transform with normalization instead of base transform
    - Uses different image context token (<IMG_CONTEXT> vs <image>)
    """

    def__init__(
        self,
        image_processor: LlamaNemotronVLEmbedImageProcessor,
        tokenizer: HfTokenizer,
        *,
        image_seq_length: int,
        start_image_token: str = "<img>",
        end_image_token: str = "</img>",
        ctx_image_token: str = "<IMG_CONTEXT>",
    ) -> None:
        super().__init__(
            image_processor=image_processor,
            tokenizer=tokenizer,
            image_seq_length=image_seq_length,
            start_image_token=start_image_token,
            end_image_token=end_image_token,
            ctx_image_token=ctx_image_token,
        )

        self.image_processor: LlamaNemotronVLEmbedImageProcessor

    defget_num_image_tokens(
        self,
        *,
        image_width: int,
        image_height: int,
    ) -> int:
        image_processor = self.image_processor
        target_ratios = self.resolve_target_ratios(
            use_thumbnail=False,  # Applied in calculate_targets
        )

        num_patches, _, _ = calculate_nemotron_vl_targets(
            orig_width=image_width,
            orig_height=image_height,
            image_size=image_processor.image_size,
            target_ratios=target_ratios,
            use_thumbnail=image_processor.use_thumbnail,
        )

        return num_patches * self.image_seq_length
```

## build\_siglip\_transform [¶](#vllm.transformers_utils.processors.nemotron_vl.build_siglip_transform "Permanent link")

```
build_siglip_transform(input_size: int)
```

Build transform for SigLIP vision encoder with normalization.

Extends the base transform from nemotron\_vl with SigLIP-specific normalization.

Source code in `vllm/transformers_utils/processors/nemotron_vl.py`

```
defbuild_siglip_transform(input_size: int):
"""Build transform for SigLIP vision encoder with normalization.

    Extends the base transform from nemotron_vl with SigLIP-specific normalization.
    """
    return T.Compose(
        [
            build_transform(input_size=input_size),
            T.Normalize(mean=SIGLIP_MEAN, std=SIGLIP_STD),
        ]
    )
```