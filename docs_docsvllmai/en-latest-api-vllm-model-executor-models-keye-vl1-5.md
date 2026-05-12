---
title: keye_vl1_5 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/keye_vl1_5/
source: sitemap
fetched_at: 2026-05-07T21:31:12.186721349-03:00
rendered_js: false
word_count: 264
summary: This document defines the data structures and utility functions used for processing image and video input tensors for the KeyeVL1.5 model architecture.
tags:
    - keye-vl1-5
    - vllm
    - tensor-schema
    - multimodal
    - image-processing
    - video-processing
    - deep-learning
category: reference
---

## KeyeVL1\_5ImageEmbeddingInputs [¶](#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5ImageEmbeddingInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- nf: Number of image features
- hs: Hidden size (must match the hidden size of language model backbone)
- ni: Number of images
- g: Grid dimensions (3 for t, h, w)

Source code in `vllm/model_executor/models/keye_vl1_5.py`

```
classKeyeVL1_5ImageEmbeddingInputs(TensorSchema):
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

## KeyeVL1\_5ImagePixelInputs [¶](#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5ImagePixelInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bnp: Batch size * Number of patches
- c: Number of channels
- ps: Patch size
- ni: Number of images
- g: Grid dimensions (3 for t, h, w)

Source code in `vllm/model_executor/models/keye_vl1_5.py`

```
classKeyeVL1_5ImagePixelInputs(TensorSchema):
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

## KeyeVL1\_5VideoEmbeddingInputs [¶](#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5VideoEmbeddingInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- nf: Number of video features
- hs: Hidden size (must match the hidden size of language model backbone)
- nv: Number of videos
- g: Grid dimensions (3 for t, h, w)

Source code in `vllm/model_executor/models/keye_vl1_5.py`

```
classKeyeVL1_5VideoEmbeddingInputs(TensorSchema):
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
    num_frames: torch.Tensor
```

## KeyeVL1\_5VideoPixelInputs [¶](#vllm.model_executor.models.keye_vl1_5.KeyeVL1_5VideoPixelInputs "Permanent link")

Bases: `TensorSchema`

Dimensions

- bnp: Batch size * Number of patches
- c: Number of channels
- ps: Patch size
- ni: Number of images
- g: Grid dimensions (3 for t, h, w)

Source code in `vllm/model_executor/models/keye_vl1_5.py`

```
classKeyeVL1_5VideoPixelInputs(TensorSchema):
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

    num_frames: torch.Tensor
```

## get\_num\_patches [¶](#vllm.model_executor.models.keye_vl1_5.get_num_patches "Permanent link")

Return num\_patches per video.

Parameters:

Name Type Description Default `grid_thw` `Tensor`

Tensor with shape \[N, 3] containing temporal, height, width dimensions

*required* `num_frames` `list[int] | Tensor`

List or tensor indicating the number of frames per video

*required*

Returns:

Type Description `list[int]`

List of ints representing the number of patches for each video

Examples:

```
>>> # Suppose there are 2 videos with a total of 3 grids
>>> grid_thw = torch.tensor(
...     [
...         [2, 2, 2],  # grid 0: 2*2*2=8 patches
...         [2, 2, 2],  # grid 1: 2*2*2=8 patches
...         [1, 1, 1],
...     ]
... )  # grid 2: 1*1*1=1 patches
>>> num_frames = [2, 1]  # The first video contains 2 grids,
                           the second contains 1 grid.
>>> get_num_patches(grid_thw, num_frames)
tensor([16, 1])  # Total patches for first video: 8+8=16,
                   second video: 1.
```

Source code in `vllm/model_executor/models/keye_vl1_5.py`

```
defget_num_patches(
    grid_thw: torch.Tensor, num_frames: list[int] | torch.Tensor
) -> list[int]:
"""
    Return num_patches per video.

    Args:
        grid_thw: Tensor with shape [N, 3] containing temporal, height, width
            dimensions
        num_frames: List or tensor indicating the number of frames per video

    Returns:
        List of ints representing the number of patches for each video

    Examples:
        >>> # Suppose there are 2 videos with a total of 3 grids
        >>> grid_thw = torch.tensor(
        ...     [
        ...         [2, 2, 2],  # grid 0: 2*2*2=8 patches
        ...         [2, 2, 2],  # grid 1: 2*2*2=8 patches
        ...         [1, 1, 1],
        ...     ]
        ... )  # grid 2: 1*1*1=1 patches
        >>> num_frames = [2, 1]  # The first video contains 2 grids,
                                   the second contains 1 grid.
        >>> get_num_patches(grid_thw, num_frames)
        tensor([16, 1])  # Total patches for first video: 8+8=16,
                           second video: 1.
    """

    assert len(grid_thw.shape) == 2
    if isinstance(num_frames, torch.Tensor):
        num_frames = num_frames.clone().tolist()

    num_grids_per_frame = grid_thw.prod(dim=1)
    start_idx_per_video = [0, *itertools.accumulate(num_frames)]
    num_patches = [
        num_grids_per_frame[start_idx_per_video[i] : start_idx_per_video[i + 1]].sum()
        for i in range(len(num_frames))
    ]
    return (
        torch.stack(num_patches)
        if num_patches
        else torch.zeros(0, dtype=grid_thw.dtype, device=grid_thw.device)
    )
```

## split\_thw [¶](#vllm.model_executor.models.keye_vl1_5.split_thw "Permanent link")

Split grid\_thw in t dimension.

Parameters:

Name Type Description Default `grid_thw` `Tensor`

\[N, 3] tensor of \[t, h, w]

*required*

Returns:

Type Description `Tensor`

\[Σt, 3] tensor where each row is \[1, h, w]

Example:

> > > grid\_thw = torch.tensor(\[\[2, 3, 4], \[1, 5, 6]]) split\_thw(grid\_thw) tensor(\[\[1, 3, 4], \[1, 3, 4], \[1, 5, 6]])

Source code in `vllm/model_executor/models/keye_vl1_5.py`

```
defsplit_thw(grid_thw: torch.Tensor) -> torch.Tensor:
"""
    Split grid_thw in t dimension.

    Args:
        grid_thw: [N, 3] tensor of [t, h, w]

    Returns:
        [Σt, 3] tensor where each row is [1, h, w]

    Example:
    >>> grid_thw = torch.tensor([[2, 3, 4], [1, 5, 6]])
    >>> split_thw(grid_thw)
    tensor([[1, 3, 4],
           [1, 3, 4],
           [1, 5, 6]])
    """
    t = grid_thw[:, 0]
    h_w = grid_thw[:, 1:]
    ones = torch.ones_like(h_w[:, :1])
    return torch.cat([ones, h_w], dim=1).repeat_interleave(t, dim=0)
```