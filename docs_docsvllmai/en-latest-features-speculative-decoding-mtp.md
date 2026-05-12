---
title: MTP (Multi-Token Prediction) - vLLM
url: https://docs.vllm.ai/en/latest/features/speculative_decoding/mtp/
source: sitemap
fetched_at: 2026-05-07T21:14:40.020368726-03:00
rendered_js: false
word_count: 99
summary: This document explains how to utilize multi-token prediction (MTP) within vLLM for speculative decoding using models that natively support this feature without requiring an external draft model.
tags:
    - vllm
    - speculative-decoding
    - multi-token-prediction
    - inference-optimization
    - language-models
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/speculative_decoding/mtp.md "Edit this page")

MTP is a speculative decoding method where the target model includes native multi-token prediction capability. Unlike draft-model-based methods, you do not need to provide a separate draft model.

MTP is useful when:

- Your model natively supports MTP.
- You want model-based speculative decoding with minimal extra configuration.

## Offline Example[¶](#offline-example "Permanent link")

```
fromvllmimport LLM, SamplingParams

prompts = ["The future of AI is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(
    model="XiaomiMiMo/MiMo-7B-Base",
    tensor_parallel_size=1,
    speculative_config={
        "method": "mtp",
        "num_speculative_tokens": 1,
    },
)
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

## Online Example[¶](#online-example "Permanent link")

```
vllmserveXiaomiMiMo/MiMo-7B-Base\
--tensor-parallel-size1\
--speculative-config'{"method":"mtp","num_speculative_tokens":1}'
```

## Notes[¶](#notes "Permanent link")

- MTP only works for model families that support MTP in vLLM.
- `num_speculative_tokens` controls speculative depth. A small value like `1` is a good default to start with.
- If your model does not support MTP, use another method such as EAGLE or draft model speculation.