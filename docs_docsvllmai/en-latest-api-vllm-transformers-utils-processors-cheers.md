---
title: cheers - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/cheers/
source: sitemap
fetched_at: 2026-05-07T21:37:48.221781908-03:00
rendered_js: false
word_count: 32
summary: This document defines the CheersProcessor class, which integrates a SigLIP image processor and a Qwen2 tokenizer to handle multimodal input processing within the vLLM framework.
tags:
    - multimodal-processing
    - vllm-framework
    - image-processing
    - tokenizer-integration
    - machine-learning
category: reference
---

## vllm.transformers\_utils.processors.cheers [¶](#vllm.transformers_utils.processors.cheers "Permanent link")

Cheers (UMM) processor for image and text inputs.

## CheersProcessor [¶](#vllm.transformers_utils.processors.cheers.CheersProcessor "Permanent link")

Bases: `ProcessorMixin`

Constructs a Cheers processor which wraps a SigLIP image processor and a Qwen2 tokenizer.

Source code in `vllm/transformers_utils/processors/cheers.py`

```
classCheersProcessor(ProcessorMixin):
"""
    Constructs a Cheers processor which wraps a
    SigLIP image processor and a Qwen2 tokenizer.
    """

    attributes = ["image_processor", "tokenizer"]
    image_processor_class = "AutoImageProcessor"
    tokenizer_class = "AutoTokenizer"

    def__call__(
        self,
        text: TextInput
        | PreTokenizedInput
        | list[TextInput]
        | list[PreTokenizedInput] = None,
        images: ImageInput = None,
        **kwargs: Unpack[CheersProcessorKwargs],
    ):
        output_kwargs = self._merge_kwargs(
            CheersProcessorKwargs,
            tokenizer_init_kwargs=self.tokenizer.init_kwargs,
            **kwargs,
        )

        if images is not None:
            importtorch

            if isinstance(images, (list, tuple)):
                all_pv = []
                all_ghw = []
                for img in images:
                    result = self.image_processor(img, **output_kwargs["images_kwargs"])
                    all_pv.append(result["pixel_values"])
                    if "grid_hws" in result:
                        all_ghw.append(result["grid_hws"])
                pixel_values = {
                    "pixel_values": torch.cat(all_pv, dim=0),
                }
                if all_ghw:
                    pixel_values["grid_hws"] = torch.cat(all_ghw, dim=0)
            else:
                pixel_values = self.image_processor(
                    images, **output_kwargs["images_kwargs"]
                )
        else:
            pixel_values = {}

        text_inputs = (
            self.tokenizer(text, **output_kwargs["text_kwargs"])
            if text is not None
            else {}
        )

        return BatchFeature(data={**pixel_values, **text_inputs})

    defbatch_decode(self, *args, **kwargs):
        return self.tokenizer.batch_decode(*args, **kwargs)

    defdecode(self, *args, **kwargs):
        return self.tokenizer.decode(*args, **kwargs)

    @property
    defmodel_input_names(self):
        tokenizer_input_names = self.tokenizer.model_input_names
        image_processor_input_names = self.image_processor.model_input_names
        return list(dict.fromkeys(tokenizer_input_names + image_processor_input_names))
```