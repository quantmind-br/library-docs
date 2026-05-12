---
title: pixtral - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/pixtral/
source: sitemap
fetched_at: 2026-05-07T21:38:11.082335641-03:00
rendered_js: false
word_count: 18
summary: This class provides a Hugging Face-compatible interface for the Mistral Common image encoder, enabling standard image processing workflows within the vLLM framework.
tags:
    - vllm
    - image-processing
    - hugging-face
    - multimodal
    - pixtral
    - mistral-common
category: api
---

## vllm.transformers\_utils.processors.pixtral [¶](#vllm.transformers_utils.processors.pixtral "Permanent link")

## MistralCommonImageProcessor [¶](#vllm.transformers_utils.processors.pixtral.MistralCommonImageProcessor "Permanent link")

Provide a HF-compatible interface for `mistral_common.tokens.tokenizers.multimodal.ImageEncoder`.

Source code in `vllm/transformers_utils/processors/pixtral.py`

```
classMistralCommonImageProcessor:
"""
    Provide a HF-compatible interface for
    `mistral_common.tokens.tokenizers.multimodal.ImageEncoder`.
    """

    def__init__(self, mm_encoder: ImageEncoder) -> None:
        self.mm_encoder = mm_encoder

    def__call__(
        self,
        images: ImageInput,
        return_tensors: str | TensorType | None = None,
        **kwargs,
    ) -> BatchFeature:
        images_lst = [images] if not isinstance(images, list) else images

        images_processed = list[torch.Tensor]()

        for image in images_lst:
            image_inputs = self.mm_encoder(ImageChunk(image=image))
            image_processed = torch.tensor(image_inputs.image)

            images_processed.append(image_processed)

        return BatchFeature({"images": images_processed}, tensor_type=return_tensors)

    defget_number_of_image_patches(
        self,
        height: int,
        width: int,
    ) -> tuple[int, int, int]:
        image = Image.new("RGB", (width, height))
        ncols, nrows = self.mm_encoder._image_to_num_tokens(image)
        return ncols * nrows, nrows, ncols
```