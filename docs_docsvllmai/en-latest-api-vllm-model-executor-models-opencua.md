---
title: opencua - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/opencua/
source: sitemap
fetched_at: 2026-05-07T21:32:22.697725327-03:00
rendered_js: false
word_count: 44
summary: This document defines the processor and processing info classes for integrating the OpenCUA-7B multimodal model into the vLLM execution framework.
tags:
    - opencua
    - vllm
    - multimodal
    - processor
    - model-executor
    - huggingface
category: reference
---

Inference-only OpenCUA-7B model compatible with HuggingFace weights.

## OpenCUAMultiModalProcessor [¶](#vllm.model_executor.models.opencua.OpenCUAMultiModalProcessor "Permanent link")

Bases: `BaseMultiModalProcessor[OpenCUAProcessingInfo]`

Source code in `vllm/model_executor/models/opencua.py`

```
classOpenCUAMultiModalProcessor(BaseMultiModalProcessor[OpenCUAProcessingInfo]):
    def_get_mm_fields_config(
        self,
        hf_inputs: BatchFeature,
        hf_processor_mm_kwargs: Mapping[str, object],
    ) -> Mapping[str, MultiModalFieldConfig]:
        return _create_qwen2vl_field_factory(
            self.info.get_hf_config().vision_config.spatial_merge_size
        )(hf_inputs)

    def_hf_processor_applies_updates(
        self,
        prompt_text: str,
        mm_items: MultiModalDataItems,
        hf_processor_mm_kwargs: Mapping[str, object],
        tokenization_kwargs: Mapping[str, object],
    ) -> bool:
"""vLLM이 prompt 업데이트를 처리하도록 False 반환."""
        return False

    def_get_prompt_updates(
        self,
        mm_items: MultiModalDataItems,
        hf_processor_mm_kwargs: Mapping[str, Any],
        out_mm_kwargs: MultiModalKwargsItems,
    ) -> Sequence[PromptUpdate]:
        hf_processor = self.info.get_hf_processor(**hf_processor_mm_kwargs)
        image_processor = self.info.get_image_processor(**hf_processor_mm_kwargs)
        tokenizer = self.info.get_tokenizer()
        vocab = tokenizer.get_vocab()
        hf_config = self.info.get_hf_config()

        image_token_str = getattr(hf_processor, "image_token", "<|media_placeholder|>")
        image_token_id = vocab.get(
            image_token_str,
            getattr(hf_config, "media_placeholder_token_id", 151664),
        )

        merge_length = image_processor.merge_size**2

        defget_replacement_opencua(item_idx: int):
            out_item = out_mm_kwargs["image"][item_idx]
            grid_thw = out_item["image_grid_thw"].data
            assert isinstance(grid_thw, torch.Tensor)

            num_tokens = int(grid_thw.prod()) // merge_length
            return [image_token_id] * num_tokens

        return [
            PromptReplacement(
                modality="image",
                target=[image_token_id],
                replacement=get_replacement_opencua,
            )
        ]
```

### \_hf\_processor\_applies\_updates [¶](#vllm.model_executor.models.opencua.OpenCUAMultiModalProcessor._hf_processor_applies_updates "Permanent link")

vLLM이 prompt 업데이트를 처리하도록 False 반환.

Source code in `vllm/model_executor/models/opencua.py`

```
def_hf_processor_applies_updates(
    self,
    prompt_text: str,
    mm_items: MultiModalDataItems,
    hf_processor_mm_kwargs: Mapping[str, object],
    tokenization_kwargs: Mapping[str, object],
) -> bool:
"""vLLM이 prompt 업데이트를 처리하도록 False 반환."""
    return False
```

## OpenCUAProcessingInfo [¶](#vllm.model_executor.models.opencua.OpenCUAProcessingInfo "Permanent link")

Bases: `Qwen2VLProcessingInfo`

Source code in `vllm/model_executor/models/opencua.py`

```
classOpenCUAProcessingInfo(Qwen2VLProcessingInfo):
    defget_data_parser(self):
        return Qwen2VLMultiModalDataParser(
            self.get_hf_config().vision_config.spatial_merge_size,
            expected_hidden_size=self._get_expected_hidden_size(),
        )

    defget_hf_config(self):
        return self.ctx.get_hf_config()

    defget_supported_mm_limits(self) -> Mapping[str, int | None]:
        return {"image": None}

    defget_hf_processor(self, **kwargs: object):
"""Load OpenCUA processor."""
        tokenizer = self.get_tokenizer()
        vision_config = self.ctx.get_hf_image_processor_config()
        return OpenCUAProcessor(
            vision_config=vision_config,
            tokenizer=tokenizer,
            **kwargs,
        )
```

### get\_hf\_processor [¶](#vllm.model_executor.models.opencua.OpenCUAProcessingInfo.get_hf_processor "Permanent link")

```
get_hf_processor(**kwargs: object)
```

Load OpenCUA processor.

Source code in `vllm/model_executor/models/opencua.py`

```
defget_hf_processor(self, **kwargs: object):
"""Load OpenCUA processor."""
    tokenizer = self.get_tokenizer()
    vision_config = self.ctx.get_hf_image_processor_config()
    return OpenCUAProcessor(
        vision_config=vision_config,
        tokenizer=tokenizer,
        **kwargs,
    )
```