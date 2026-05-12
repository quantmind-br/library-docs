---
title: parse - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/parse/
source: sitemap
fetched_at: 2026-05-07T21:34:16.151289965-03:00
rendered_js: false
word_count: 13
summary: The MultiModalDataParser class handles the ingestion, validation, and preprocessing of multimodal data including audio, video, images, and vision chunks for model inference.
tags:
    - multimodal-data
    - data-parsing
    - vllm
    - audio-resampling
    - model-inference
    - data-normalization
category: api
---

```
classMultiModalDataParser:
"""
    Parses [`MultiModalDataDict`][vllm.inputs.MultiModalDataDict]
    into [`MultiModalDataItems`][vllm.multimodal.parse.MultiModalDataItems].

    Args:
        target_sr (float, optional): Enables automatic resampling of audio
            items to the model's expected sampling rate.
        target_channels (int, optional): Target number of audio channels.
            If provided, normalizes audio to this many channels (e.g., 1 for mono).
            If None, audio channels are passed through unchanged.
        expected_hidden_size (int, optional): Expected hidden dimension for
            embedding inputs. If provided, validates that user-supplied
            embeddings have the correct hidden size to prevent crashes
            during model inference.
    """

    def__init__(
        self,
        *,
        target_sr: float | None = None,
        target_channels: int | None = None,
        audio_resample_method: Literal["pyav", "scipy"] = "pyav",
        video_needs_metadata: bool = False,
        expected_hidden_size: int | None = None,
    ) -> None:
        super().__init__()

        self.audio_resampler = AudioResampler(
            target_sr=target_sr,
            method=audio_resample_method,
        )
        self.target_channels = target_channels
        self.video_needs_metadata = video_needs_metadata
        self.expected_hidden_size = expected_hidden_size

    @classmethod
    defis_embeddings(
        cls, data: object
    ) -> TypeGuard[torch.Tensor | list[torch.Tensor]]:
        if isinstance(data, torch.Tensor):
            return data.ndim == 3
        if is_list_of(data, torch.Tensor) and len(data) > 0:
            return data[0].ndim == 2  # type: ignore[index]

        return False

    def_get_audio_with_sr(
        self,
        audio: AudioItem,
    ) -> tuple[np.ndarray, float | None]:
        if isinstance(audio, tuple):
            return audio
        if isinstance(audio, list):
            return np.array(audio), None
        if isinstance(audio, np.ndarray):
            return audio, None
        if isinstance(audio, torch.Tensor):
            return audio.numpy(), None

        assert_never(audio)

    def_get_video_with_metadata(
        self,
        video: VideoItem,
    ) -> tuple[np.ndarray, dict[str, Any] | None]:
        if isinstance(video, tuple):
            return video
        if isinstance(video, list):
            return np.array(video), None
        if isinstance(video, np.ndarray):
            return video, None
        if isinstance(video, torch.Tensor):
            return video.numpy(), None

        assert_never(video)

    def_parse_audio_data(
        self,
        data: ModalityData[AudioItem],
    ) -> ModalityDataItems[Any, Any] | None:
        if data is None:
            return None

        if self.is_embeddings(data):
            return AudioEmbeddingItems(data, self.expected_hidden_size)

        data_items: list[AudioItem]
        if (
            (is_list_of(data, float) and len(data) > 0)
            or (isinstance(data, (np.ndarray, torch.Tensor)) and data.ndim == 1)
            or isinstance(data, tuple)
        ):
            data_items = [data]
        elif isinstance(data, (np.ndarray, torch.Tensor)):
            data_items = [elem for elem in data]
        else:
            data_items = data  # type: ignore[assignment]

        new_audios = list[np.ndarray]()
        for data_item in data_items:
            audio, orig_sr = self._get_audio_with_sr(data_item)
            if orig_sr is None:
                new_audio = audio
            else:
                new_audio = self.audio_resampler.resample(audio, orig_sr=orig_sr)

            # Apply channel normalization if target_channels is set
            if self.target_channels is not None:
                spec = AudioSpec(target_channels=self.target_channels)
                new_audio = normalize_audio(new_audio, spec)

            new_audios.append(new_audio)

        return AudioProcessorItems(new_audios)

    def_parse_image_data(
        self,
        data: ModalityData[ImageItem],
    ) -> ModalityDataItems[Any, Any] | None:
        if data is None:
            return None

        if self.is_embeddings(data):
            return ImageEmbeddingItems(data, self.expected_hidden_size)

        if isinstance(data, (PILImage.Image, MediaWithBytes)) or (
            isinstance(data, (np.ndarray, torch.Tensor)) and data.ndim == 3
        ):
            data_items = [data]
        elif isinstance(data, (np.ndarray, torch.Tensor)):
            data_items = [elem for elem in data]
        else:
            data_items = data

        return ImageProcessorItems(data_items)

    def_parse_video_data(
        self,
        data: ModalityData[VideoItem],
    ) -> ModalityDataItems[Any, Any] | None:
        if data is None:
            return None

        if self.is_embeddings(data):
            return VideoEmbeddingItems(data, self.expected_hidden_size)

        data_items: list[VideoItem]
        if (is_list_of(data, PILImage.Image) and len(data) > 0) or (
            isinstance(data, (np.ndarray, torch.Tensor)) and data.ndim == 4
        ):
            data_items = [data]
        elif isinstance(data, (np.ndarray, torch.Tensor)):
            data_items = [elem for elem in data]
        elif isinstance(data, tuple) and len(data) == 2:
            data_items = [data]
        else:
            data_items = data  # type: ignore[assignment]

        new_videos = list[tuple[np.ndarray, dict[str, Any] | None]]()
        metadata_lst: list[dict[str, Any] | None] = []
        for data_item in data_items:
            video, metadata = self._get_video_with_metadata(data_item)
            if self.video_needs_metadata:
                if metadata is None:
                    raise ValueError(
                        "Video metadata is required but not found in mm input. "
                        "Please check your video input in `multi_modal_data`"
                    )
                new_videos.append((video, metadata))
                metadata_lst.append(metadata)
            else:
                new_videos.append(video)

        if not self.video_needs_metadata:
            metadata = None

        return VideoProcessorItems(new_videos, metadata=metadata_lst)

    def_parse_vision_chunk_data(
        self,
        data: ModalityData[Any],
    ) -> ModalityDataItems[Any, Any] | None:
"""Parse vision chunk data (unified image and video chunks)."""
        if data is None:
            return None

        if self.is_embeddings(data):
            raise ValueError("Do not support embedding data for vision_chunk right now")

        if isinstance(data, dict):
            data = [data]

        return VisionChunkProcessorItems(data)

    def_get_subparsers(self) -> Mapping[str, ModalityDataParser]:
        return {
            "audio": self._parse_audio_data,
            "image": self._parse_image_data,
            "video": self._parse_video_data,
            "vision_chunk": self._parse_vision_chunk_data,
        }

    defparse_mm_data(self, mm_data: MultiModalDataDict) -> MultiModalDataItems:
        subparsers = self._get_subparsers()

        mm_items = MultiModalDataItems()
        for k, v in mm_data.items():
            if k not in subparsers:
                raise ValueError(f"Unsupported modality: {k}")

            # ignore empty embedding data
            if (parsed_data := subparsers[k](v)) is not None:
                mm_items[k] = parsed_data

        return mm_items
```