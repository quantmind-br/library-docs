---
title: video - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/assets/video/
source: sitemap
fetched_at: 2026-05-07T21:15:40.666711205-03:00
rendered_js: false
word_count: 45
summary: This document defines the VideoAsset dataclass and supporting utility functions used for downloading, processing, and extracting audio or visual frames from video assets in the vLLM library.
tags:
    - vllm
    - video-processing
    - dataclass
    - asset-management
    - multimodal-input
category: reference
---

## vllm.assets.video [¶](#vllm.assets.video "Permanent link")

## VideoAsset `dataclass` [¶](#vllm.assets.video.VideoAsset "Permanent link")

Source code in `vllm/assets/video.py`

```
@dataclass(frozen=True)
classVideoAsset:
    name: VideoAssetName
    num_frames: int = -1

    _NAME_TO_FILE: ClassVar[dict[VideoAssetName, str]] = {
        "baby_reading": "sample_demo_1.mp4",
    }

    @property
    deffilename(self) -> str:
        return self._NAME_TO_FILE[self.name]

    @property
    defvideo_path(self) -> str:
        return download_video_asset(self.filename)

    @property
    defpil_images(self) -> list[Image.Image]:
        ret = video_to_pil_images_list(self.video_path, self.num_frames)
        return ret

    @property
    defnp_ndarrays(self) -> npt.NDArray:
        ret = video_to_ndarrays(self.video_path, self.num_frames)
        return ret

    @property
    defmetadata(self) -> dict[str, Any]:
        ret = video_get_metadata(self.video_path, self.num_frames)
        return ret

    defget_audio(self, sampling_rate: float | None = None) -> npt.NDArray:
"""
        Read audio data from the video asset, used in Qwen2.5-Omni examples.

        See also: examples/offline_inference/qwen2_5_omni/only_thinker.py
        """
        return load_audio_pyav(self.video_path, sr=sampling_rate)[0]
```

### get\_audio [¶](#vllm.assets.video.VideoAsset.get_audio "Permanent link")

Read audio data from the video asset, used in Qwen2.5-Omni examples.

See also: examples/offline\_inference/qwen2\_5\_omni/only\_thinker.py

Source code in `vllm/assets/video.py`

```
defget_audio(self, sampling_rate: float | None = None) -> npt.NDArray:
"""
    Read audio data from the video asset, used in Qwen2.5-Omni examples.

    See also: examples/offline_inference/qwen2_5_omni/only_thinker.py
    """
    return load_audio_pyav(self.video_path, sr=sampling_rate)[0]
```

## download\_video\_asset `cached` [¶](#vllm.assets.video.download_video_asset "Permanent link")

```
download_video_asset(filename: str) -> str
```

Download and open an image from huggingface repo: raushan-testing-hf/videos-test

Source code in `vllm/assets/video.py`

```
@lru_cache
defdownload_video_asset(filename: str) -> str:
"""
    Download and open an image from huggingface
    repo: raushan-testing-hf/videos-test
    """
    video_directory = get_cache_dir() / "video-example-data"
    video_directory.mkdir(parents=True, exist_ok=True)

    video_path = video_directory / filename
    video_path_str = str(video_path)
    if not video_path.exists():
        video_path_str = hf_hub_download(
            repo_id="raushan-testing-hf/videos-test",
            filename=filename,
            repo_type="dataset",
            cache_dir=video_directory,
        )
    return video_path_str
```