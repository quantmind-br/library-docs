---
title: bee - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/bee/
source: sitemap
fetched_at: 2026-05-07T21:29:11.130143906-03:00
rendered_js: false
word_count: 21
summary: This document defines the BeeProcessingInfo class, which provides logic for calculating unpadded feature counts in vision models by adjusting for aspect ratios and patch constraints.
tags:
    - vllm
    - model-executor
    - vision-processing
    - feature-extraction
    - aspect-ratio
    - patch-calculation
category: reference
---

## BeeProcessingInfo [¶](#vllm.model_executor.models.bee.BeeProcessingInfo "Permanent link")

Bases: `LlavaNextProcessingInfo`

Source code in `vllm/model_executor/models/bee.py`

```
classBeeProcessingInfo(LlavaNextProcessingInfo):
    defget_hf_config(self):
        return self.ctx.get_hf_config()

    defget_hf_processor(self, **kwargs: object):
        return self.ctx.get_hf_processor(**kwargs)

    def_get_num_unpadded_features(
        self,
        *,
        original_height: int,
        original_width: int,
        npatches: int,
        num_patch_height: int,
        num_patch_width: int,
    ) -> tuple[int, int]:
"""Override to use correct max_num_patches from vision_aspect_ratio."""
        importmath

        current_height = npatches * num_patch_height
        current_width = npatches * num_patch_width

        aspect_ratio = original_width / original_height
        current_aspect_ratio = current_width / current_height

        if aspect_ratio > current_aspect_ratio:
            new_height = int(
                round(original_height * (current_width / original_width), 7)
            )
            padding = (current_height - new_height) // 2
            current_height = current_height - (2 * padding)
        else:
            new_width = int(
                round(original_width * (current_height / original_height), 7)
            )
            padding = (current_width - new_width) // 2
            current_width = current_width - (2 * padding)

        unpadded_features = current_height * current_width
        newline_features = current_height

        # Get max_num_patches from vision_aspect_ratio config
        hf_config = self.get_hf_config()
        vision_aspect_ratio = getattr(hf_config, "vision_aspect_ratio", "anyres_max_9")
        max_num_patches = int(vision_aspect_ratio.replace("anyres_max_", ""))

        ratio = math.sqrt(
            current_height * current_width / (max_num_patches * npatches**2)
        )
        if ratio > 1.1:
            height_factor = int(current_height // ratio)
            width_factor = int(current_width // ratio)
            unpadded_features = height_factor * width_factor
            newline_features = height_factor

        return (unpadded_features, newline_features)
```

### \_get\_num\_unpadded\_features [¶](#vllm.model_executor.models.bee.BeeProcessingInfo._get_num_unpadded_features "Permanent link")

```
_get_num_unpadded_features(
    *,
    original_height: int,
    original_width: int,
    npatches: int,
    num_patch_height: int,
    num_patch_width: int,
) -> tuple[int, int]
```

Override to use correct max\_num\_patches from vision\_aspect\_ratio.

Source code in `vllm/model_executor/models/bee.py`

```
def_get_num_unpadded_features(
    self,
    *,
    original_height: int,
    original_width: int,
    npatches: int,
    num_patch_height: int,
    num_patch_width: int,
) -> tuple[int, int]:
"""Override to use correct max_num_patches from vision_aspect_ratio."""
    importmath

    current_height = npatches * num_patch_height
    current_width = npatches * num_patch_width

    aspect_ratio = original_width / original_height
    current_aspect_ratio = current_width / current_height

    if aspect_ratio > current_aspect_ratio:
        new_height = int(
            round(original_height * (current_width / original_width), 7)
        )
        padding = (current_height - new_height) // 2
        current_height = current_height - (2 * padding)
    else:
        new_width = int(
            round(original_width * (current_height / original_height), 7)
        )
        padding = (current_width - new_width) // 2
        current_width = current_width - (2 * padding)

    unpadded_features = current_height * current_width
    newline_features = current_height

    # Get max_num_patches from vision_aspect_ratio config
    hf_config = self.get_hf_config()
    vision_aspect_ratio = getattr(hf_config, "vision_aspect_ratio", "anyres_max_9")
    max_num_patches = int(vision_aspect_ratio.replace("anyres_max_", ""))

    ratio = math.sqrt(
        current_height * current_width / (max_num_patches * npatches**2)
    )
    if ratio > 1.1:
        height_factor = int(current_height // ratio)
        width_factor = int(current_width // ratio)
        unpadded_features = height_factor * width_factor
        newline_features = height_factor

    return (unpadded_features, newline_features)
```