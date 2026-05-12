---
title: utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/utils/
source: sitemap
fetched_at: 2026-05-07T21:34:22.89407488-03:00
rendered_js: false
word_count: 601
summary: This document provides an API reference for multimodal utility functions in vLLM, covering media fetching, encoding, and tensor batching operations.
tags:
    - vllm
    - multimodal
    - media-processing
    - api-reference
    - data-encoding
    - tensor-handling
category: api
---

## argsort\_mm\_positions [¶](#vllm.multimodal.utils.argsort_mm_positions "Permanent link")

Given a `MultiModalPlaceholders`, output a sequence of keys to sort the dictionary by `offset` (starting index in the input sequence) in ascending order.

Returns:

Type Description `list[tuple[str, int]]`

A list of `(modality, idx)`, which can be used to access an item

`list[tuple[str, int]]`

by `mm_positions[modality][idx]`.

Source code in `vllm/multimodal/utils.py`

```
defargsort_mm_positions(
    mm_positions: MultiModalPlaceholders,
) -> list[tuple[str, int]]:
"""
    Given a `MultiModalPlaceholders`, output a sequence of keys to
    sort the dictionary by `offset` (starting index in the input sequence)
    in ascending order.

    Returns:
        A list of `(modality, idx)`, which can be used to access an item
        by `mm_positions[modality][idx]`.
    """
    flat_items = (
        (modality, idx, item)
        for modality, items in mm_positions.items()
        for idx, item in enumerate(items)
    )

    sorted_flat_items = sorted(flat_items, key=lambda x: x[2].offset)

    return [(modality, idx) for modality, idx, _ in sorted_flat_items]
```

## encode\_audio\_base64 [¶](#vllm.multimodal.utils.encode_audio_base64 "Permanent link")

```
encode_audio_base64(
    audio: ndarray,
    sampling_rate: int,
    *,
    format: str = "WAV",
) -> str
```

Encode audio as base64.

Source code in `vllm/multimodal/utils.py`

```
defencode_audio_base64(
    audio: np.ndarray,
    sampling_rate: int,
    *,
    format: str = "WAV",
) -> str:
"""Encode audio as base64."""
    audio_io = AudioMediaIO()
    return audio_io.encode_base64((audio, sampling_rate), audio_format=format)
```

## encode\_audio\_url [¶](#vllm.multimodal.utils.encode_audio_url "Permanent link")

```
encode_audio_url(
    audio: ndarray,
    sampling_rate: int,
    *,
    format: str = "WAV",
) -> str
```

Encode audio as a data URL.

Source code in `vllm/multimodal/utils.py`

```
defencode_audio_url(
    audio: np.ndarray,
    sampling_rate: int,
    *,
    format: str = "WAV",
) -> str:
"""Encode audio as a data URL."""
    audio_b64 = encode_audio_base64(audio, sampling_rate, format=format)
    mimetype = mimetypes.types_map.get("." + format.lower(), "audio")
    return f"data:{mimetype};base64,{audio_b64}"
```

## encode\_image\_base64 [¶](#vllm.multimodal.utils.encode_image_base64 "Permanent link")

```
encode_image_base64(
    image: Image,
    *,
    image_mode: str = "RGB",
    format: str = "PNG",
) -> str
```

Encode a pillow image to base64 format.

By default, the image is converted into RGB format before being encoded.

Source code in `vllm/multimodal/utils.py`

```
defencode_image_base64(
    image: Image.Image,
    *,
    image_mode: str = "RGB",
    format: str = "PNG",
) -> str:
"""
    Encode a pillow image to base64 format.

    By default, the image is converted into RGB format before being encoded.
    """
    image_io = ImageMediaIO(image_mode=image_mode)
    return image_io.encode_base64(image, image_format=format)
```

## encode\_image\_url [¶](#vllm.multimodal.utils.encode_image_url "Permanent link")

```
encode_image_url(
    image: Image,
    *,
    image_mode: str = "RGB",
    format: str = "PNG",
) -> str
```

Encode a pillow image as a data URL.

By default, the image is converted into RGB format before being encoded.

Source code in `vllm/multimodal/utils.py`

```
defencode_image_url(
    image: Image.Image,
    *,
    image_mode: str = "RGB",
    format: str = "PNG",
) -> str:
"""
    Encode a pillow image as a data URL.

    By default, the image is converted into RGB format before being encoded.
    """
    image_b64 = encode_image_base64(image, image_mode=image_mode, format=format)
    mimetype = mimetypes.types_map.get("." + format.lower(), "image")
    return f"data:{mimetype};base64,{image_b64}"
```

## fetch\_audio [¶](#vllm.multimodal.utils.fetch_audio "Permanent link")

Parameters:

Name Type Description Default `audio_url` `str`

URL of the audio file to fetch.

*required* `audio_io_kwargs` `dict[str, Any] | None`

Additional kwargs passed to handle audio IO.

`None`

Warning

This method has direct access to local files and is only intended to be called by user code. Never call this from the online server!

Source code in `vllm/multimodal/utils.py`

```
deffetch_audio(
    audio_url: str,
    audio_io_kwargs: dict[str, Any] | None = None,
) -> tuple[np.ndarray, int | float]:
"""
    Args:
        audio_url: URL of the audio file to fetch.
        audio_io_kwargs: Additional kwargs passed to handle audio IO.

    Warning:
        This method has direct access to local files and is only intended
        to be called by user code. Never call this from the online server!
    """
    media_io_kwargs = None if not audio_io_kwargs else {"audio": audio_io_kwargs}
    media_connector = MediaConnector(
        media_io_kwargs=media_io_kwargs,
        allowed_local_media_path="/",
    )
    return media_connector.fetch_audio(audio_url)
```

## fetch\_image [¶](#vllm.multimodal.utils.fetch_image "Permanent link")

Parameters:

Name Type Description Default `image_url` `str`

URL of the image file to fetch.

*required* `image_io_kwargs` `dict[str, Any] | None`

Additional kwargs passed to handle image IO.

`None`

Warning

This method has direct access to local files and is only intended to be called by user code. Never call this from the online server!

Source code in `vllm/multimodal/utils.py`

```
deffetch_image(
    image_url: str,
    image_io_kwargs: dict[str, Any] | None = None,
) -> Image.Image:
"""
    Args:
        image_url: URL of the image file to fetch.
        image_io_kwargs: Additional kwargs passed to handle image IO.

    Warning:
        This method has direct access to local files and is only intended
        to be called by user code. Never call this from the online server!
    """
    media_io_kwargs = None if not image_io_kwargs else {"image": image_io_kwargs}
    media_connector = MediaConnector(
        media_io_kwargs=media_io_kwargs,
        allowed_local_media_path="/",
    )
    return media_connector.fetch_image(image_url)
```

## fetch\_video [¶](#vllm.multimodal.utils.fetch_video "Permanent link")

Parameters:

Name Type Description Default `video_url` `str`

URL of the video file to fetch.

*required* `video_io_kwargs` `dict[str, Any] | None`

Additional kwargs passed to handle video IO.

`None`

Warning

This method has direct access to local files and is only intended to be called by user code. Never call this from the online server!

Source code in `vllm/multimodal/utils.py`

```
deffetch_video(
    video_url: str,
    video_io_kwargs: dict[str, Any] | None = None,
) -> tuple[npt.NDArray, dict[str, Any]]:
"""
    Args:
        video_url: URL of the video file to fetch.
        video_io_kwargs: Additional kwargs passed to handle video IO.

    Warning:
        This method has direct access to local files and is only intended
        to be called by user code. Never call this from the online server!
    """
    media_io_kwargs = None if not video_io_kwargs else {"video": video_io_kwargs}
    media_connector = MediaConnector(
        media_io_kwargs=media_io_kwargs,
        allowed_local_media_path="/",
    )
    return media_connector.fetch_video(video_url)
```

## group\_and\_batch\_mm\_items [¶](#vllm.multimodal.utils.group_and_batch_mm_items "Permanent link")

Group consecutive items (possibly from different requests) into batches.

Items must be split across groups if any of the following occurs, as the batch would otherwise be invalid: - They have different fields (e.g. mixed image and embedding inputs). - They have different values in `MultiModalSharedField`.

Parameters:

Name Type Description Default `items` `Sequence[MultiModalKwargsItem]`

List of `MultiModalKwargsItem`.

*required* `device` `Device`

The device to place the grouped tensors on.

`None` `pin_memory` `bool`

Whether to pin memory for faster host-to-device transfer.

`False`

Yields:

Type Description `Generator[tuple[int, BatchedTensorInputs]]`

A tuple `(num_items, grouped_kwargs)`, where:

`Generator[tuple[int, BatchedTensorInputs]]`

- `kwargs` is a dictionary of keyword arguments to pass to the model;

`Generator[tuple[int, BatchedTensorInputs]]`

- `num_items` is the corresponding number of items.

Source code in `vllm/multimodal/utils.py`

```
defgroup_and_batch_mm_items(
    items: Sequence[MultiModalKwargsItem],
    *,
    device: torch.types.Device = None,
    pin_memory: bool = False,
) -> Generator[tuple[int, BatchedTensorInputs]]:
"""
    Group consecutive items (possibly from different requests) into batches.

    Items must be split across groups if any of the following occurs,
    as the batch would otherwise be invalid:
    - They have different fields (e.g. mixed image and embedding inputs).
    - They have different values in `MultiModalSharedField`.

    Args:
        items: List of `MultiModalKwargsItem`.
        device: The device to place the grouped tensors on.
        pin_memory: Whether to pin memory for faster host-to-device transfer.

    Yields:
        A tuple `(num_items, grouped_kwargs)`, where:
        - `kwargs` is a dictionary of keyword arguments to pass to the model;
        - `num_items` is the corresponding number of items.
    """
    group_ids = [
        tuple(
            (key, _get_group_hash(elem))
            for key, elem in sorted(item.items(), key=lambda kv: kv[0])
        )
        for item in items
    ]
    group_sizes = [sum(1 for _ in group) for _, group in groupby(group_ids)]

    start_idx = 0
    for group_size in group_sizes:
        group_data = _batch_mm_items(
            items[start_idx : start_idx + group_size],
            device=device,
            pin_memory=pin_memory,
        )

        yield group_size, group_data

        start_idx += group_size

    assert start_idx == len(items)
```

## group\_and\_batch\_mm\_kwargs [¶](#vllm.multimodal.utils.group_and_batch_mm_kwargs "Permanent link")

Group consecutive items (possibly from different requests) into batches.

Items must be split across groups if any of the following occurs, as the batch would otherwise be invalid: - They have different fields (e.g. mixed image and embedding inputs). - They have different values in `MultiModalSharedField`.

To simplify the implementation of `embed_multimodal`, we add another restriction that the items in a batch must belong to the same modality.

Parameters:

Name Type Description Default `mm_kwargs` `list[tuple[str, MultiModalKwargsItem]]`

List of `(modality, item)`.

*required* `device` `Device`

The device to place the grouped tensors on.

`None` `pin_memory` `bool`

Whether to pin memory for faster host-to-device transfer.

`False`

Yields:

Type Description `str`

A tuple `(modality, num_items, grouped_kwargs)`, where:

`int`

- `modality` is the modality of the batch;

`BatchedTensorInputs`

- `kwargs` is a dictionary of keyword arguments to pass to the model;

`tuple[str, int, BatchedTensorInputs]`

- `num_items` is the corresponding number of items.

Source code in `vllm/multimodal/utils.py`

```
defgroup_and_batch_mm_kwargs(
    mm_kwargs: list[tuple[str, MultiModalKwargsItem]],
    *,
    device: torch.types.Device = None,
    pin_memory: bool = False,
) -> Generator[tuple[str, int, BatchedTensorInputs], None, None]:
"""
    Group consecutive items (possibly from different requests) into batches.

    Items must be split across groups if any of the following occurs,
    as the batch would otherwise be invalid:
    - They have different fields (e.g. mixed image and embedding inputs).
    - They have different values in `MultiModalSharedField`.

    To simplify the implementation of `embed_multimodal`, we add another
    restriction that the items in a batch must belong to the same modality.

    Args:
        mm_kwargs: List of `(modality, item)`.
        device: The device to place the grouped tensors on.
        pin_memory: Whether to pin memory for faster host-to-device transfer.

    Yields:
        A tuple `(modality, num_items, grouped_kwargs)`, where:
        - `modality` is the modality of the batch;
        - `kwargs` is a dictionary of keyword arguments to pass to the model;
        - `num_items` is the corresponding number of items.
    """
    for modality, group in groupby(mm_kwargs, key=lambda x: x[0]):
        items_lst = [item for _, item in group]

        for num_items, mm_kwargs_batch in group_and_batch_mm_items(
            items_lst,
            device=device,
            pin_memory=pin_memory,
        ):
            yield modality, num_items, mm_kwargs_batch
```