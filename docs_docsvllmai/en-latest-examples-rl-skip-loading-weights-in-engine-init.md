---
title: Skip Loading Weights In Engine Init
url: https://docs.vllm.ai/en/latest/examples/rl/skip_loading_weights_in_engine_init/
source: sitemap
fetched_at: 2026-05-07T21:13:50.832900543-03:00
rendered_js: false
word_count: 45
summary: This document demonstrates how to initialize the vLLM engine using dummy weights to save time and subsequently reload actual model weights at runtime using collective RPC calls.
tags:
    - vllm
    - weight-loading
    - engine-initialization
    - dummy-weights
    - model-deployment
    - rpc-calls
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/rl/skip_loading_weights_in_engine_init.md "Edit this page")

Source [https://github.com/vllm-project/vllm/blob/main/examples/rl/skip\_loading\_weights\_in\_engine\_init.py](https://github.com/vllm-project/vllm/blob/main/examples/rl/skip_loading_weights_in_engine_init.py).

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromvllmimport LLM, RequestOutput, SamplingParams

# Sample prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)


defprint_prompts_and_outputs(outputs: list[RequestOutput]) -> None:
    print("-" * 60)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt:    {prompt!r}")
        print(f"Output:    {generated_text!r}")
        print("-" * 60)


defmain():
    # Create an LLM without loading real weights
    llm = LLM(
        model="Qwen/Qwen3-0.6B",
        load_format="dummy",
        enforce_eager=True,
        tensor_parallel_size=4,
    )
    outputs = llm.generate(prompts, sampling_params)
    print("\nOutputs do not make sense:")
    print_prompts_and_outputs(outputs)

    # Update load format from `dummy` to `auto`
    llm.collective_rpc(
        "update_config", args=({"load_config": {"load_format": "auto"}},)
    )
    # Now reload real weights inplace
    llm.collective_rpc("reload_weights")

    # Check outputs make sense
    outputs = llm.generate(prompts, sampling_params)
    print("\nOutputs make sense after loading real weights:")
    print_prompts_and_outputs(outputs)


if __name__ == "__main__":
    main()
```