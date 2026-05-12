---
title: kimi_k25 - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/kimi_k25/
source: sitemap
fetched_at: 2026-05-07T21:38:03.124183778-03:00
rendered_js: false
word_count: 122
summary: This document defines the KimiK25Processor class, which manages multimodal data processing by combining text tokenization with image and video chunk pre-processing for input into a model.
tags:
    - multimodal-processing
    - transformer-utils
    - image-processing
    - tokenization
    - vllm-framework
    - data-preprocessing
category: reference
---

Bases: `ProcessorMixin`

Source code in `vllm/transformers_utils/processors/kimi_k25.py`

```
classKimiK25Processor(ProcessorMixin):
    attributes = ["image_processor", "tokenizer"]

    def__init__(
        self,
        image_processor: BaseImageProcessor,
        tokenizer: HfTokenizer,
        media_token_id: int,
    ) -> None:
        self.image_processor = image_processor
        self.tokenizer = tokenizer

        self.media_token_id = media_token_id

    def__call__(
        self,
        text: str | list[str] | None = None,
        vision_chunks: list[VisionChunk] | None = None,
        return_tensors: str | TensorType | None = None,
        **kwargs,
    ) -> BatchFeature:
"""
        Args:
            text: The text to be field to the model.
            vision_chunks: List of `VisionChunk` items to be processed.
                For image: `VisionChunkImage` with
                  `type='image', image=PIL.Image`
                For video_chunk: `VisionChunkVideo` with
                  `type='video_chunk', video_chunk=list[PIL.Image]`
        Returns:
            [`BatchFeature`]: A [`BatchFeature`] with the following fields:

            - **input_ids** -- list of token ids to be fed to a model.
            - **pixel_values** -- Pixel values to be fed to a model.
              Returned when `vision_chunks` is not `None`.
            - **grid_thws** -- list of image 3D grid in LLM.
              Returned when `vision_chunks` is not `None`.
        """
        if vision_chunks is not None:
            mm_inputs = self.image_processor.preprocess(
                vision_chunks,
                return_tensors=return_tensors,
            )
        else:
            mm_inputs = {}

        if text is not None:
            if not isinstance(text, list):
                text = [text]

            text_inputs = self.tokenizer(text)

            # Note: Modify in-place
            input_ids: list[list[int]] = text_inputs["input_ids"]  # type: ignore

            if vision_chunks is not None:
                num_tokens_per_chunk = [
                    self.image_processor.media_tokens_calculator(chunk)
                    for chunk in vision_chunks
                ]

                for i in range(len(input_ids)):
                    new_input_ids = []
                    for token in input_ids[i]:
                        if token == self.media_token_id:
                            new_input_ids.extend(
                                [self.media_token_id] * num_tokens_per_chunk.pop(0)
                            )
                        else:
                            new_input_ids.append(token)

                    input_ids[i] = new_input_ids
        else:
            text_inputs = {}

        return BatchFeature(
            data={**text_inputs, **mm_inputs},
            tensor_type=return_tensors,
        )
```

### \_\_call\__ [¶](#vllm.transformers_utils.processors.kimi_k25.KimiK25Processor.__call__ "Permanent link")

```
__call__(
    text: str | list[str] | None = None,
    vision_chunks: list[VisionChunk] | None = None,
    return_tensors: str | TensorType | None = None,
    **kwargs,
) -> BatchFeature
```

Parameters:

Name Type Description Default `text` `str | list[str] | None`

The text to be field to the model.

`None` `vision_chunks` `list[VisionChunk] | None`

List of `VisionChunk` items to be processed. For image: `VisionChunkImage` with `type='image', image=PIL.Image` For video\_chunk: `VisionChunkVideo` with `type='video_chunk', video_chunk=list[PIL.Image]`

`None`

Returns: \[`BatchFeature`]: A \[`BatchFeature`] with the following fields:

```
- **input_ids** -- list of token ids to be fed to a model.
- **pixel_values** -- Pixel values to be fed to a model.
  Returned when `vision_chunks` is not `None`.
- **grid_thws** -- list of image 3D grid in LLM.
  Returned when `vision_chunks` is not `None`.
```

Source code in `vllm/transformers_utils/processors/kimi_k25.py`

```
def__call__(
    self,
    text: str | list[str] | None = None,
    vision_chunks: list[VisionChunk] | None = None,
    return_tensors: str | TensorType | None = None,
    **kwargs,
) -> BatchFeature:
"""
    Args:
        text: The text to be field to the model.
        vision_chunks: List of `VisionChunk` items to be processed.
            For image: `VisionChunkImage` with
              `type='image', image=PIL.Image`
            For video_chunk: `VisionChunkVideo` with
              `type='video_chunk', video_chunk=list[PIL.Image]`
    Returns:
        [`BatchFeature`]: A [`BatchFeature`] with the following fields:

        - **input_ids** -- list of token ids to be fed to a model.
        - **pixel_values** -- Pixel values to be fed to a model.
          Returned when `vision_chunks` is not `None`.
        - **grid_thws** -- list of image 3D grid in LLM.
          Returned when `vision_chunks` is not `None`.
    """
    if vision_chunks is not None:
        mm_inputs = self.image_processor.preprocess(
            vision_chunks,
            return_tensors=return_tensors,
        )
    else:
        mm_inputs = {}

    if text is not None:
        if not isinstance(text, list):
            text = [text]

        text_inputs = self.tokenizer(text)

        # Note: Modify in-place
        input_ids: list[list[int]] = text_inputs["input_ids"]  # type: ignore

        if vision_chunks is not None:
            num_tokens_per_chunk = [
                self.image_processor.media_tokens_calculator(chunk)
                for chunk in vision_chunks
            ]

            for i in range(len(input_ids)):
                new_input_ids = []
                for token in input_ids[i]:
                    if token == self.media_token_id:
                        new_input_ids.extend(
                            [self.media_token_id] * num_tokens_per_chunk.pop(0)
                        )
                    else:
                        new_input_ids.append(token)

                input_ids[i] = new_input_ids
    else:
        text_inputs = {}

    return BatchFeature(
        data={**text_inputs, **mm_inputs},
        tensor_type=return_tensors,
    )
```