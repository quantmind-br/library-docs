---
title: image - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/assets/image/
source: sitemap
fetched_at: 2026-05-07T21:15:39.75638129-03:00
rendered_js: false
word_count: 0
summary: This document defines a Python dataclass used for managing and retrieving image assets from S3 storage, including methods for handling file paths, loading images, and accessing embeddings.
tags:
    - python
    - dataclass
    - image-processing
    - s3-storage
    - asset-management
    - embedding-loading
category: reference
---

```
@dataclass(frozen=True)
classImageAsset:
    name: ImageAssetName

    defget_path(self, ext: str) -> Path:
"""
        Return s3 path for given image.
        """
        return get_vllm_public_assets(
            filename=f"{self.name}.{ext}", s3_prefix=VLM_IMAGES_DIR
        )

    @property
    defpil_image(self) -> Image.Image:
        return self.pil_image_ext(ext="jpg")

    defpil_image_ext(self, ext: str) -> Image.Image:
        image_path = self.get_path(ext=ext)
        return Image.open(image_path)

    @property
    defimage_embeds(self) -> torch.Tensor:
"""
        Image embeddings, only used for testing purposes with llava 1.5.
        """
        image_path = self.get_path("pt")
        return torch.load(image_path, map_location="cpu", weights_only=True)

    defread_bytes(self, ext: str) -> bytes:
        p = Path(self.get_path(ext))
        return p.read_bytes()
```