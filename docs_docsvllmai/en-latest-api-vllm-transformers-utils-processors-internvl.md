---
title: internvl - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/internvl/
source: sitemap
fetched_at: 2026-05-07T21:38:00.210208062-03:00
rendered_js: false
word_count: 0
summary: This class provides a custom processor for the InternVL model, handling the tokenization of text, images, and video inputs, including the injection of specific special tokens required for multimodal processing.
tags:
    - internvl
    - multimodal
    - processor
    - hugging-face
    - image-processing
    - video-processing
    - tokenizer
category: api
---

```
classInternVLProcessor(ProcessorMixin):
"""
    This model doesn't define its own HF processor,
    so we implement our own one here.

    The code to insert image tokens is based on:
    https://huggingface.co/OpenGVLab/InternVL2-1B/blob/main/modeling_internvl_chat.py#L252

    Code for video processing is adapted from video example:
    https://huggingface.co/OpenGVLab/InternVL3-1B#inference-with-transformers
    """

    attributes = ["image_processor", "tokenizer", "video_processor"]

    def__init__(
        self,
        image_processor: InternVLImageProcessor,
        tokenizer: HfTokenizer,
        video_processor: InternVLVideoProcessor | None = None,
        *,
        image_seq_length: int,
        start_image_token: str = "<img>",
        end_image_token: str = "</img>",
        ctx_image_token: str = "<IMG_CONTEXT>",
        ctx_video_token: str | None = None,
    ) -> None:
        self.image_processor = image_processor
        self.tokenizer = tokenizer
        self.video_processor = video_processor

        self.image_seq_length = image_seq_length
        self.start_image_token = start_image_token
        self.end_image_token = end_image_token
        self.ctx_image_token = ctx_image_token
        self.ctx_video_token = ctx_video_token

        self.start_image_token_id = tokenizer.convert_tokens_to_ids(start_image_token)
        self.end_image_token_id = tokenizer.convert_tokens_to_ids(end_image_token)
        self.ctx_image_token_id = tokenizer.convert_tokens_to_ids(ctx_image_token)
        self.ctx_video_token_id = (
            None
            if ctx_video_token is None
            else tokenizer.convert_tokens_to_ids(ctx_video_token)
        )

    defresolve_target_ratios(
        self,
        *,
        min_dynamic_patch: int | None = None,
        max_dynamic_patch: int | None = None,
        dynamic_image_size: bool | None = None,
        use_thumbnail: bool | None = None,
    ) -> list[tuple[int, int]]:
        min_num, max_num = self.image_processor.resolve_min_max_num(
            min_dynamic_patch=min_dynamic_patch,
            max_dynamic_patch=max_dynamic_patch,
            dynamic_image_size=dynamic_image_size,
            use_thumbnail=use_thumbnail,
        )

        return get_internvl_target_ratios(min_num, max_num)

    defget_num_image_tokens(
        self,
        *,
        image_width: int,
        image_height: int,
    ) -> int:
        image_processor = self.image_processor
        target_ratios = self.resolve_target_ratios(
            use_thumbnail=False,  # Applied in calculate_targets
        )

        num_patches, _, _ = calculate_internvl_targets(
            orig_width=image_width,
            orig_height=image_height,
            image_size=image_processor.image_size,
            target_ratios=target_ratios,
            use_thumbnail=image_processor.use_thumbnail,
        )

        return num_patches * self.image_seq_length

    defget_image_repl(
        self,
        num_patches: int | None,
        num_features: int | None = None,
    ) -> PromptUpdateDetails[str]:
        if num_patches is None:
            assert num_features is not None
        else:
            num_features = num_patches * self.image_seq_length

        repl_features = self.ctx_image_token * num_features
        repl_full = self.start_image_token + repl_features + self.end_image_token

        return PromptUpdateDetails.select_text(repl_full, self.ctx_image_token)

    defget_video_repl(self, num_patches: int) -> PromptUpdateDetails[str]:
        assert self.ctx_video_token is not None

        repl_features = self.ctx_video_token * self.image_seq_length
        repl_features_with_sep = (
            self.start_image_token + repl_features + self.end_image_token
        )
        # num_patches is equal to num_frames
        repl_full = "".join(
            [f"Frame{i+1}: {repl_features_with_sep}" for i in range(num_patches)]
        )

        return PromptUpdateDetails.select_text(repl_full, self.ctx_video_token)

    def__call__(
        self,
        text: str | list[str] | None = None,
        images: Image.Image | list[Image.Image] | None = None,
        videos: npt.NDArray | list[npt.NDArray] | None = None,
        *,
        min_dynamic_patch: int | None = None,
        max_dynamic_patch: int | None = None,
        dynamic_image_size: bool | None = None,
        return_tensors: str | TensorType | None = None,
        **kwargs,
    ) -> BatchFeature:
        if images is not None:
            image_inputs = self.image_processor(
                images=images,
                min_dynamic_patch=min_dynamic_patch,
                max_dynamic_patch=max_dynamic_patch,
                dynamic_image_size=dynamic_image_size,
                return_tensors=return_tensors,
            )
            image_num_patches = image_inputs["image_num_patches"]
        else:
            image_inputs = {}
            image_num_patches = []

        if videos is not None:
            if self.video_processor is None:
                raise ValueError("This model does not support video inputs")

            video_inputs = self.video_processor(
                videos=videos,
                return_tensors=return_tensors,
            )
            video_num_patches = video_inputs["video_num_patches"]
        else:
            video_inputs = {}
            video_num_patches = []

        if text is not None:
            if not isinstance(text, list):
                text = [text]

            if image_inputs:
                image_token = "<image>"
                image_index = 0
                processed_text = list[str]()
                replace_strings = list[str]()

                for prompt in text:
                    new_prompt = prompt

                    while image_token in new_prompt:
                        new_prompt = new_prompt.replace(image_token, "<placeholder>", 1)
                        image_repl = self.get_image_repl(image_num_patches[image_index])
                        replace_strings.append(image_repl.full)
                        image_index += 1

                    while "<placeholder>" in new_prompt:
                        replace_str = replace_strings.pop(0)
                        new_prompt = new_prompt.replace("<placeholder>", replace_str, 1)

                    processed_text.append(new_prompt)

                text = processed_text

            if video_inputs:
                video_token = "<video>"
                video_index = 0
                processed_text = list[str]()
                replace_strings = list[str]()

                assert video_token is not None

                for prompt in text:
                    new_prompt = prompt

                    while video_token in new_prompt:
                        new_prompt = new_prompt.replace(video_token, "<placeholder>", 1)
                        video_repl = self.get_video_repl(video_num_patches[video_index])
                        replace_strings.append(video_repl.full)
                        video_index += 1

                    while "<placeholder>" in new_prompt:
                        replace_str = replace_strings.pop(0)
                        new_prompt = new_prompt.replace("<placeholder>", replace_str, 1)

                    processed_text.append(new_prompt)

                text = processed_text

            text_inputs = self.tokenizer(text, return_tensors=return_tensors)
        else:
            text_inputs = {}

        return BatchFeature(
            data={**text_inputs, **image_inputs, **video_inputs},
            tensor_type=return_tensors,
        )
```