---
title: aya_vision - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/aya_vision/
source: sitemap
fetched_at: 2026-05-07T21:29:05.186335693-03:00
rendered_js: false
word_count: 84
summary: This document defines the schema for image pixel inputs and processing logic for the AyaVision model, including methods for calculating patch requirements based on image size constraints.
tags:
    - aya-vision
    - vllm
    - image-processing
    - tensor-schema
    - patch-calculation
    - computer-vision
    - model-executor
category: reference
---

## AyaVisionImagePixelInputs [¶](#vllm.model_executor.models.aya_vision.AyaVisionImagePixelInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- np: The total number of patches over each image over each prompt in the batch
- c: Number of channels
- h: Height of each image patch
- w: Width of each image patch
- bn: Batch size * number of images

Source code in `vllm/model_executor/models/aya_vision.py`

```
classAyaVisionImagePixelInputs(TensorSchema):
"""
    Dimensions:
        - np: The total number of patches over each image over each prompt in
              the batch
        - c: Number of channels
        - h: Height of each image patch
        - w: Width of each image patch
        - bn: Batch size * number of images
    """

    type: Literal["pixel_values"]

    pixel_values: Annotated[
        torch.Tensor,
        TensorShape("np", 3, "h", "w"),
    ]

    num_patches: Annotated[
        torch.Tensor,
        TensorShape("bn"),
    ]
```

## AyaVisionProcessingInfo [¶](#vllm.model_executor.models.aya_vision.AyaVisionProcessingInfo "Permanent link")

Bases: `BaseProcessingInfo`

Source code in `vllm/model_executor/models/aya_vision.py`

```
classAyaVisionProcessingInfo(BaseProcessingInfo):
    defget_hf_config(self) -> AyaVisionConfig:
        return self.ctx.get_hf_config(AyaVisionConfig)

    defget_hf_processor(self, **kwargs: object) -> AyaVisionProcessor:
        return self.ctx.get_hf_processor(AyaVisionProcessor, **kwargs)

    defget_image_processor(self, **kwargs: object) -> GotOcr2ImageProcessor:
        return self.get_hf_processor(**kwargs).image_processor

    defget_supported_mm_limits(self) -> Mapping[str, int | None]:
        return {"image": None}

    defget_image_size_with_most_features(self) -> ImageSize:
        image_processor = self.get_image_processor()
        height = image_processor.size["height"]
        width = image_processor.size["width"]
        max_patches = image_processor.max_patches
        return ImageSize(height=height * max_patches, width=width * max_patches)

    defget_num_patches(
        self,
        *,
        image_width: int,
        image_height: int,
        size: dict,
        min_patches: int,
        max_patches: int,
    ) -> int:
"""
        Calculate the number of patches needed for a given image based on size
        constraints.  This method replicates and adjusts the logic from:
        transformers/models/got_ocr2/image_processing_got_ocr2
        """
        size = get_size_dict(size, default_to_square=False)
        num_columns, num_rows = get_optimal_tiled_canvas(
            (image_height, image_width),
            (size["height"], size["width"]),
            min_patches,
            max_patches,
        )
        num_blocks = num_columns * num_rows
        return num_blocks if num_blocks == 1 else num_blocks + 1
```

### get\_num\_patches [¶](#vllm.model_executor.models.aya_vision.AyaVisionProcessingInfo.get_num_patches "Permanent link")

```
get_num_patches(
    *,
    image_width: int,
    image_height: int,
    size: dict,
    min_patches: int,
    max_patches: int,
) -> int
```

Calculate the number of patches needed for a given image based on size constraints. This method replicates and adjusts the logic from: transformers/models/got\_ocr2/image\_processing\_got\_ocr2

Source code in `vllm/model_executor/models/aya_vision.py`

```
defget_num_patches(
    self,
    *,
    image_width: int,
    image_height: int,
    size: dict,
    min_patches: int,
    max_patches: int,
) -> int:
"""
    Calculate the number of patches needed for a given image based on size
    constraints.  This method replicates and adjusts the logic from:
    transformers/models/got_ocr2/image_processing_got_ocr2
    """
    size = get_size_dict(size, default_to_square=False)
    num_columns, num_rows = get_optimal_tiled_canvas(
        (image_height, image_width),
        (size["height"], size["width"]),
        min_patches,
        max_patches,
    )
    num_blocks = num_columns * num_rows
    return num_blocks if num_blocks == 1 else num_blocks + 1
```