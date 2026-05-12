---
title: dummy_inputs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/dummy_inputs/
source: sitemap
fetched_at: 2026-05-07T21:34:18.978931049-03:00
rendered_js: false
word_count: 8
summary: This abstract base class provides a framework for generating synthetic input data and processor inputs required to profile and test multi-modal machine learning models.
tags:
    - python
    - multi-modal
    - data-generation
    - abstract-base-class
    - model-profiling
    - machine-learning
category: reference
---

```
classBaseDummyInputsBuilder(ABC, Generic[_I]):
"""
    Abstract base class that constructs the dummy data to profile
    multi-modal models.
    """

    def__init__(self, info: _I) -> None:
        super().__init__()

        self.info = info

    @abstractmethod
    defget_dummy_text(self, mm_counts: Mapping[str, int]) -> str:
"""
        Build the text input corresponding to `mm_counts`.
        """
        raise NotImplementedError

    @abstractmethod
    defget_dummy_mm_data(
        self,
        seq_len: int,
        mm_counts: Mapping[str, int],
        mm_options: Mapping[str, BaseDummyOptions],
    ) -> MultiModalDataDict:
"""
        Build the multimodal input which, after processing, results in
        the maximum possible number of placeholder tokens.

        Args:
            seq_len: Sequence length
            mm_counts: Count of items per modality
            mm_options: Configurable options per modality (optional).
                       If None, use model defaults for backward compatibility.
                       If provided, models can use these to customize dummy
                       data generation.
        """
        raise NotImplementedError

    defget_dummy_processor_inputs(
        self,
        seq_len: int,
        mm_counts: Mapping[str, int],
        mm_options: Mapping[str, BaseDummyOptions],
    ) -> ProcessorInputs:
"""
        Build the input which, after processing, results in
        the maximum possible number of placeholder tokens.

        Args:
            seq_len: Sequence length
            mm_counts: Count of items per modality
            mm_options: Configurable options per modality (optional)
        """
        dummy_text = self.get_dummy_text(mm_counts)
        dummy_mm_data = self.get_dummy_mm_data(seq_len, mm_counts, mm_options)
        dummy_mm_items = self.info.parse_mm_data(dummy_mm_data, validate=False)

        tokenization_kwargs = {"truncation": False}

        return ProcessorInputs(
            prompt=dummy_text,
            mm_data_items=dummy_mm_items,
            tokenization_kwargs=tokenization_kwargs,
        )

    def_get_dummy_audios(
        self,
        *,
        length: int,
        num_audios: int,
        overrides: AudioDummyOptions | None = None,
    ) -> list[npt.NDArray]:
        if num_audios == 0:
            return []
        if overrides and overrides.length:
            if overrides.length > length:
                logger.warning(
                    "audio.length override (%d) exceeds model's "
                    "maximum length (%d), will be ignored",
                    overrides.length,
                    length,
                )
            length = min(length, overrides.length)
        audio = np.zeros((length,))
        return [audio] * num_audios

    def_get_dummy_images(
        self,
        *,
        width: int,
        height: int,
        num_images: int,
        overrides: ImageDummyOptions | None = None,
    ) -> list[Image.Image]:
        if num_images == 0:
            return []
        if overrides:
            if overrides.width:
                if overrides.width > width:
                    logger.warning(
                        "image.width override (%d) exceeds model's "
                        "maximum width (%d), will be ignored",
                        overrides.width,
                        width,
                    )
                width = min(width, overrides.width)
            if overrides.height:
                if overrides.height > height:
                    logger.warning(
                        "image.height override (%d) exceeds model's "
                        "maximum height (%d), will be ignored",
                        overrides.height,
                        height,
                    )
                height = min(height, overrides.height)
        image = Image.new("RGB", (width, height), color=255)
        return [image] * num_images

    def_get_dummy_videos(
        self,
        *,
        width: int,
        height: int,
        num_frames: int,
        num_videos: int,
        overrides: VideoDummyOptions | None = None,
    ) -> list[npt.NDArray]:
        if num_videos == 0:
            return []
        if overrides:
            if overrides.num_frames:
                if overrides.num_frames > num_frames:
                    logger.warning(
                        "video.num_frames override (%d) exceeds model's "
                        "maximum number of frames (%d), will be ignored",
                        overrides.num_frames,
                        num_frames,
                    )
                num_frames = min(num_frames, overrides.num_frames)
            if overrides.width:
                if overrides.width > width:
                    logger.warning(
                        "video.width override (%d) exceeds model's "
                        "maximum width (%d), will be ignored",
                        overrides.width,
                        width,
                    )
                width = min(width, overrides.width)
            if overrides.height:
                if overrides.height > height:
                    logger.warning(
                        "video.height override (%d) exceeds model's "
                        "maximum height (%d), will be ignored",
                        overrides.height,
                        height,
                    )
                height = min(height, overrides.height)
        video = np.full((num_frames, width, height, 3), 255, dtype=np.uint8)
        return [video] * num_videos
```