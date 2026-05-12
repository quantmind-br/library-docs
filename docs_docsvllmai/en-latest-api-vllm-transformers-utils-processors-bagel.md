---
title: bagel - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/transformers_utils/processors/bagel/
source: sitemap
fetched_at: 2026-05-07T21:37:47.275117172-03:00
rendered_js: false
word_count: 78
summary: The BagelProcessor class integrates a SigLIP image processor and a Qwen2 tokenizer to facilitate the preparation of multimodal input data for machine learning models.
tags:
    - bagel-processor
    - multimodal-input
    - image-processing
    - qwen2-tokenizer
    - data-preprocessing
    - vllm-utils
category: api
---

BAGEL processor for image and text inputs.

## BagelProcessor [¶](#vllm.transformers_utils.processors.bagel.BagelProcessor "Permanent link")

Bases: `ProcessorMixin`

Constructs a BAGEL processor which wraps a SigLIP image processor and a Qwen2 tokenizer.

Source code in `vllm/transformers_utils/processors/bagel.py`

```
classBagelProcessor(ProcessorMixin):
"""
    Constructs a BAGEL processor which wraps a
    SigLIP image processor and a Qwen2 tokenizer.
    """

    attributes = ["image_processor", "tokenizer"]
    image_processor_class = "SiglipImageProcessor"
    tokenizer_class = "AutoTokenizer"

    def__call__(
        self,
        text: TextInput
        | PreTokenizedInput
        | list[TextInput]
        | list[PreTokenizedInput] = None,
        images: ImageInput = None,
        **kwargs: Unpack[BagelProcessorKwargs],
    ):
"""
        Main method to prepare for the model one or several sequences(s) and image(s).
        """
        output_kwargs = self._merge_kwargs(
            BagelProcessorKwargs,
            tokenizer_init_kwargs=self.tokenizer.init_kwargs,
            **kwargs,
        )

        if images is not None:
            # Process images with the image processor
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
"""
        This method forwards all its arguments to Qwen2TokenizerFast's batch_decode.
        """
        return self.tokenizer.batch_decode(*args, **kwargs)

    defdecode(self, *args, **kwargs):
"""
        This method forwards all its arguments to Qwen2TokenizerFast's decode.
        """
        return self.tokenizer.decode(*args, **kwargs)

    @property
    defmodel_input_names(self):
        tokenizer_input_names = self.tokenizer.model_input_names
        image_processor_input_names = self.image_processor.model_input_names
        return list(dict.fromkeys(tokenizer_input_names + image_processor_input_names))
```

### \_\_call\__ [¶](#vllm.transformers_utils.processors.bagel.BagelProcessor.__call__ "Permanent link")

```
__call__(
    text: TextInput
    | PreTokenizedInput
    | list[TextInput]
    | list[PreTokenizedInput] = None,
    images: ImageInput = None,
    **kwargs: Unpack[BagelProcessorKwargs],
)
```

Main method to prepare for the model one or several sequences(s) and image(s).

Source code in `vllm/transformers_utils/processors/bagel.py`

```
def__call__(
    self,
    text: TextInput
    | PreTokenizedInput
    | list[TextInput]
    | list[PreTokenizedInput] = None,
    images: ImageInput = None,
    **kwargs: Unpack[BagelProcessorKwargs],
):
"""
    Main method to prepare for the model one or several sequences(s) and image(s).
    """
    output_kwargs = self._merge_kwargs(
        BagelProcessorKwargs,
        tokenizer_init_kwargs=self.tokenizer.init_kwargs,
        **kwargs,
    )

    if images is not None:
        # Process images with the image processor
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
```

### batch\_decode [¶](#vllm.transformers_utils.processors.bagel.BagelProcessor.batch_decode "Permanent link")

```
batch_decode(*args, **kwargs)
```

This method forwards all its arguments to Qwen2TokenizerFast's batch\_decode.

Source code in `vllm/transformers_utils/processors/bagel.py`

```
defbatch_decode(self, *args, **kwargs):
"""
    This method forwards all its arguments to Qwen2TokenizerFast's batch_decode.
    """
    return self.tokenizer.batch_decode(*args, **kwargs)
```

### decode [¶](#vllm.transformers_utils.processors.bagel.BagelProcessor.decode "Permanent link")

This method forwards all its arguments to Qwen2TokenizerFast's decode.

Source code in `vllm/transformers_utils/processors/bagel.py`

```
defdecode(self, *args, **kwargs):
"""
    This method forwards all its arguments to Qwen2TokenizerFast's decode.
    """
    return self.tokenizer.decode(*args, **kwargs)
```