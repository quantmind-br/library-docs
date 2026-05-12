---
title: base - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/assets/base/
source: sitemap
fetched_at: 2026-05-07T21:15:38.838074382-03:00
rendered_js: false
word_count: 53
summary: This module provides utility functions for managing local asset caching and downloading public assets from an S3 bucket within the vLLM ecosystem.
tags:
    - asset-management
    - caching
    - s3-download
    - vllm-assets
    - python-api
category: api
---

## vllm.assets.base [¶](#vllm.assets.base "Permanent link")

## get\_cache\_dir [¶](#vllm.assets.base.get_cache_dir "Permanent link")

Get the path to the cache for storing downloaded assets.

Source code in `vllm/assets/base.py`

```
defget_cache_dir() -> Path:
"""Get the path to the cache for storing downloaded assets."""
    path = Path(envs.VLLM_ASSETS_CACHE)
    path.mkdir(parents=True, exist_ok=True)

    return path
```

## get\_vllm\_public\_assets `cached` [¶](#vllm.assets.base.get_vllm_public_assets "Permanent link")

```
get_vllm_public_assets(
    filename: str, s3_prefix: str | None = None
) -> Path
```

Download an asset file from `s3://vllm-public-assets` and return the path to the downloaded file.

Source code in `vllm/assets/base.py`

```
@lru_cache
defget_vllm_public_assets(filename: str, s3_prefix: str | None = None) -> Path:
"""
    Download an asset file from `s3://vllm-public-assets`
    and return the path to the downloaded file.
    """
    asset_directory = get_cache_dir() / "vllm_public_assets"
    asset_directory.mkdir(parents=True, exist_ok=True)

    asset_path = asset_directory / filename
    if not asset_path.exists():
        if s3_prefix is not None:
            filename = s3_prefix + "/" + filename
        global_http_connection.download_file(
            f"{VLLM_S3_BUCKET_URL}/{filename}",
            asset_path,
            timeout=envs.VLLM_IMAGE_FETCH_TIMEOUT,
        )

    return asset_path
```