---
title: hunyuan_vl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/hunyuan_vl/
source: sitemap
fetched_at: 2026-05-07T21:37:58.146934188-03:00
rendered_js: false
word_count: 7
summary: This document provides a Python function that divides an image tensor into smaller patches and further subdivides those patches into smaller regions for computer vision preprocessing.
tags:
    - image-processing
    - tensor-manipulation
    - pytorch
    - computer-vision
    - patch-splitting
    - feature-extraction
category: reference
---

```
defsplit_image_into_patch_blocks(
    pixel_values: torch.Tensor,  # shape: [batch_size, 3, H, W]
    patch_size: int = 16,  # e.g. 16
    adaptor_patch_div: int = 4,  # e.g. 4 --> each patch_size is cut into 4x4 small regions, i.e. patch_size // 4 # noqa: E501
) -> torch.Tensor:
"""
    Split the input image tensor (supporting batch) into large patches of size `patch_size`,
    and then further divide each large patch into smaller regions of size
    (patch_size // adaptor_patch_div) x (patch_size // adaptor_patch_div).
    Each small region is extracted as a tensor of shape [3, patch_size, patch_size].
    The final output contains all such small region tensors.

    Args:
        pixel_values: Input image tensor of shape [batch_size, 3, H, W].
        patch_size: Size of the large patch, e.g., 16.
        adaptor_patch_div: Each large patch is divided into
                          (patch_size // adaptor_patch_div) x (patch_size // adaptor_patch_div)
                          smaller regions.

    Returns:
        patches: A tensor of shape [N, 3, patch_size, patch_size],
                 where N = batch_size * (H // patch_size) * (W // patch_size) * (patch_size // adaptor_patch_div)^2.
                 Each element in the batch corresponds to one small image region.
    """  # noqa: E501
    batch_size, channels, height, width = pixel_values.shape
    assert channels == 3, "Pixel values must have 3 channels in dim=1"
    assert height % patch_size == 0 and width % patch_size == 0, (
        "H and W must be divisible by patch_size"
    )

    patch_height_num = height // patch_size
    patch_width_num = width // patch_size

    # Reshape to [B, 3, ph, ps, pw, ps]
    img = pixel_values.reshape(
        batch_size, 3, patch_height_num, patch_size, patch_width_num, patch_size
    )

    # Further split each psxps patch into (ps//aps)x(ps//aps) small regions
    img = img.reshape(
        batch_size,
        3,
        patch_height_num,
        patch_size // adaptor_patch_div,  # ps // aps
        adaptor_patch_div,
        patch_width_num,
        patch_size // adaptor_patch_div,  # ps // aps
        adaptor_patch_div,
    )

    # Permute to group the small regions: [B, ph, pw, ps//aps, ps//aps, 3, aps, aps]
    img = img.permute(0, 2, 5, 3, 6, 1, 4, 7)

    # Reshape into [B * ph * pw * (ps//aps)^2, 3, patch_size, patch_size]
    patches = img.reshape(-1, 3, patch_size, patch_size)

    return patches
```