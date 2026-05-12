---
title: inputs - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/inputs/
source: sitemap
fetched_at: 2026-05-07T21:34:20.057109001-03:00
rendered_js: false
word_count: 20
summary: This document defines the ProcessorInputs dataclass used to manage multimodal input arguments, including prompt data, modality-specific items, and hashing logic for processing configurations.
tags:
    - vllm
    - multimodal
    - data-processing
    - python-dataclass
    - input-handling
    - hashing
category: reference
---

## vllm.multimodal.processing.inputs [¶](#vllm.multimodal.processing.inputs "Permanent link")

## ProcessorInputs `dataclass` [¶](#vllm.multimodal.processing.inputs.ProcessorInputs "Permanent link")

Represents the keyword arguments to [`vllm.multimodal.processing.BaseMultiModalProcessor.apply`](https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/#vllm.multimodal.processing.BaseMultiModalProcessor.apply "            apply").

Source code in `vllm/multimodal/processing/inputs.py`

```
@dataclass
classProcessorInputs:
"""
    Represents the keyword arguments to
    [`vllm.multimodal.processing.BaseMultiModalProcessor.apply`][].
    """

    prompt: str | list[int]
    mm_data_items: MultiModalDataItems
    mm_uuid_items: MultiModalUUIDItems | None = None
    hf_processor_mm_kwargs: Mapping[str, object] = field(default_factory=dict)
    tokenization_kwargs: Mapping[str, object] = field(default_factory=dict)

    defget_mm_hashes(self, model_id: str) -> MultiModalHashes:
        mm_data_items = self.mm_data_items
        mm_uuid_items = self.mm_uuid_items or {}
        hf_processor_mm_kwargs = self.hf_processor_mm_kwargs

        mm_hashes = dict[str, list[str]]()
        hasher = MultiModalHasher

        for modality, data_items in mm_data_items.items():
            if modality in mm_uuid_items:
                uuid_items = mm_uuid_items[modality]

                # For None entries, compute a hash; otherwise, use provided ID.
                hashes: list[str] = []
                for i, item in enumerate(data_items.get_all_items_for_hash()):
                    uuid_item = uuid_items[i]

                    # NOTE: Even if a uuid_item is provided, we still compute a hash
                    # if `hf_processor_mm_kwargs` is provided.
                    # This is because the processed multimodal inputs can be different
                    # depending on the processor kwargs.
                    if uuid_item is None or hf_processor_mm_kwargs:
                        # NOTE: use provided hash string to hash with kwargs
                        # if available for better performance.
                        item = uuid_item if uuid_item is not None else item
                        hashes.append(
                            hasher.hash_kwargs(
                                model_id=model_id,
                                **{modality: item},
                                **hf_processor_mm_kwargs,
                            )
                        )
                    else:
                        hashes.append(uuid_item)

                mm_hashes[modality] = hashes
            else:
                mm_hashes[modality] = [
                    hasher.hash_kwargs(
                        model_id=model_id,
                        **{modality: item},
                        **hf_processor_mm_kwargs,
                    )
                    for item in data_items
                ]

        return mm_hashes
```