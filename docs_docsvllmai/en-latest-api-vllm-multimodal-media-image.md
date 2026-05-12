---
title: image - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/media/image/
source: sitemap
fetched_at: 2026-05-07T21:34:14.080751719-03:00
rendered_js: false
word_count: 90
summary: This document defines classes for processing and converting image data and embeddings within the vLLM multimodal framework, providing mechanisms for loading from bytes, files, and base64 strings.
tags:
    - multimodal
    - image-processing
    - tensor-loading
    - media-io
    - vllm
    - data-conversion
category: reference
---

Bases: `MediaIO[Tensor]`

Image embedding MediaIO implementation.

Configuration values can be user-provided either by --media-io-kwargs or by the runtime API field "media\_io\_kwargs". Ensure proper validation and error handling.

Source code in `vllm/multimodal/media/image.py`

```
classImageEmbeddingMediaIO(MediaIO[torch.Tensor]):
"""Image embedding MediaIO implementation.

    Configuration values can be user-provided either by --media-io-kwargs or
    by the runtime API field "media_io_kwargs". Ensure proper validation and
    error handling.
    """

    def__init__(self) -> None:
        super().__init__()

    def_load_pickled_torch(self, data: bytes) -> torch.Tensor:
        buffer = BytesIO(data)
        # Enable sparse tensor integrity checks to prevent out-of-bounds
        # writes from maliciously crafted tensors
        with torch.sparse.check_sparse_tensor_invariants():
            tensor = torch.load(buffer, weights_only=True)
            return tensor.to_dense()

    def_load_numpy(self, data: bytes) -> torch.Tensor:
        with BytesIO(data) as buffer:
            return torch.from_numpy(np.load(buffer))

    defload_bytes(self, data: bytes) -> torch.Tensor:
        if data[:6] == MAGIC_NUMPY_PREFIX:
            return self._load_numpy(data)

        return self._load_pickled_torch(data)

    defload_base64(self, media_type: str, data: str) -> torch.Tensor:
        return self.load_bytes(pybase64.b64decode(data, validate=True))

    defload_file(self, filepath: Path) -> torch.Tensor:
        if filepath.suffix == ".npy":
            return torch.from_numpy(np.load(filepath))

        with torch.sparse.check_sparse_tensor_invariants():
            tensor = torch.load(filepath, weights_only=True)
            return tensor.to_dense()

    defencode_base64(self, media: torch.Tensor) -> str:
        return tensor2base64(media)
```

Bases: `MediaIO[Image]`

Configuration values can be user-provided either by --media-io-kwargs or by the runtime API field "media\_io\_kwargs". Ensure proper validation and error handling.

Source code in `vllm/multimodal/media/image.py`

```
classImageMediaIO(MediaIO[Image.Image]):
"""Configuration values can be user-provided either by --media-io-kwargs or
    by the runtime API field "media_io_kwargs". Ensure proper validation and
    error handling.
    """

    def__init__(self, image_mode: str = "RGB", **kwargs) -> None:
        super().__init__()

        self.image_mode = image_mode
        # `kwargs` contains custom arguments from
        # --media-io-kwargs for this modality, merged with
        # per-request runtime media_io_kwargs via merge_kwargs().
        # They can be passed to the underlying
        # media loaders (e.g. custom implementations)
        # for flexible control.
        self.kwargs = kwargs

        # Extract RGBA background color from kwargs if provided
        # Default to white background for backward compatibility
        rgba_bg = kwargs.get("rgba_background_color", (255, 255, 255))
        # Convert list to tuple for consistency
        if isinstance(rgba_bg, list):
            rgba_bg = tuple(rgba_bg)

        # Validate rgba_background_color format
        if not (
            isinstance(rgba_bg, tuple)
            and len(rgba_bg) == 3
            and all(isinstance(c, int) and 0 <= c <= 255 for c in rgba_bg)
        ):
            raise ValueError(
                "rgba_background_color must be a list or tuple of 3 integers "
                "in the range [0, 255]."
            )
        self.rgba_background_color = rgba_bg

    def_convert_image_mode(
        self, image: Image.Image | MediaWithBytes[Image.Image]
    ) -> Image.Image:
"""Convert image mode with custom background color."""
        if isinstance(image, MediaWithBytes):
            image = image.media
        if image.mode == self.image_mode:
            return image
        elif image.mode == "RGBA" and self.image_mode == "RGB":
            return rgba_to_rgb(image, self.rgba_background_color)
        else:
            return convert_image_mode(image, self.image_mode)

    defload_bytes(self, data: bytes) -> MediaWithBytes[Image.Image]:
        try:
            image = Image.open(BytesIO(data))
            image.load()
            image = self._convert_image_mode(image)
        except (OSError, Image.UnidentifiedImageError) as e:
            raise ValueError(f"Failed to load image: {e}") frome
        return MediaWithBytes(image, data)

    defload_base64(self, media_type: str, data: str) -> MediaWithBytes[Image.Image]:
        return self.load_bytes(pybase64.b64decode(data, validate=True))

    defload_file(self, filepath: Path) -> MediaWithBytes[Image.Image]:
        return self.load_bytes(filepath.read_bytes())

    defencode_base64(
        self,
        media: Image.Image,
        *,
        image_format: str = "PNG",
    ) -> str:
        image = media

        with BytesIO() as buffer:
            image = self._convert_image_mode(image)
            image.save(buffer, image_format)
            data = buffer.getvalue()

        return pybase64.b64encode(data).decode("utf-8")
```

### \_convert\_image\_mode [¶](#vllm.multimodal.media.image.ImageMediaIO._convert_image_mode "Permanent link")

Convert image mode with custom background color.

Source code in `vllm/multimodal/media/image.py`

```
def_convert_image_mode(
    self, image: Image.Image | MediaWithBytes[Image.Image]
) -> Image.Image:
"""Convert image mode with custom background color."""
    if isinstance(image, MediaWithBytes):
        image = image.media
    if image.mode == self.image_mode:
        return image
    elif image.mode == "RGBA" and self.image_mode == "RGB":
        return rgba_to_rgb(image, self.rgba_background_color)
    else:
        return convert_image_mode(image, self.image_mode)
```