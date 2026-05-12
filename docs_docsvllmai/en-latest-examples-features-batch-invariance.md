---
title: Batch Invariance - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/batch_invariance/
source: sitemap
fetched_at: 2026-05-07T21:12:48.723942701-03:00
rendered_js: false
word_count: 8
summary: This document demonstrates how to configure vLLM environments to ensure deterministic and reproducible model outputs regardless of scheduling variations.
tags:
    - vllm
    - reproducibility
    - batch-invariance
    - deterministic-inference
    - model-serving
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/features/batch_invariance.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/batch\_invariance](https://github.com/vllm-project/vllm/tree/main/examples/features/batch_invariance).

## Reproducibility Offline[¶](#reproducibility-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
Demonstrates how to achieve reproducibility in vLLM.

Main article: https://docs.vllm.ai/en/latest/usage/reproducibility.html
"""

importos
importrandom

fromvllmimport LLM, SamplingParams

# Either:
## Turn off multiprocessing to make the scheduling deterministic, or
os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0"
## Enable batch invariance to get consistent results regardless of scheduling.
os.environ["VLLM_BATCH_INVARIANT"] = "1"

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)


defmain():
    llm = LLM(model="facebook/opt-125m")
    outputs = llm.generate(prompts, sampling_params)
    print("-" * 50)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
        print("-" * 50)

    # Try generating random numbers outside vLLM
    # The same number is output across runs, meaning that the random state
    # in the user code has been updated by vLLM
    print(random.randint(0, 100))


if __name__ == "__main__":
    main()
```