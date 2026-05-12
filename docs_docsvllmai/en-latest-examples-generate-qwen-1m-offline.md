---
title: Qwen 1M Offline - vLLM
url: https://docs.vllm.ai/en/latest/examples/generate/qwen_1m_offline/
source: sitemap
fetched_at: 2026-05-07T21:13:05.804204273-03:00
rendered_js: false
word_count: 6
summary: This document provides a code example demonstrating how to run offline inference with the Qwen2.5-1M model using the vLLM engine, specifically focusing on handling long-context prompts.
tags:
    - vllm
    - offline-inference
    - large-context-window
    - model-deployment
    - qwen
    - python
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/generate/qwen_1m_offline.md "Edit this page")

Source [https://github.com/vllm-project/vllm/blob/main/examples/generate/qwen\_1m\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/generate/qwen_1m_offline.py).

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
importos
fromurllib.requestimport urlopen

fromvllmimport LLM, SamplingParams

os.environ["VLLM_ALLOW_LONG_MAX_MODEL_LEN"] = "1"


defload_prompt() -> str:
    # Test cases with various lengths can be found at:
    #
    # https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/test-data/64k.txt
    # https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/test-data/200k.txt
    # https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/test-data/600k.txt
    # https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/test-data/1m.txt

    with urlopen(
        "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2.5-1M/test-data/600k.txt",
        timeout=5,
    ) as response:
        prompt = response.read().decode("utf-8")
    return prompt


# Processing the prompt.
defprocess_requests(llm: LLM, prompts: list[str]) -> None:
    # Create a sampling params object.
    sampling_params = SamplingParams(
        temperature=0.7,
        top_p=0.8,
        top_k=20,
        repetition_penalty=1.05,
        detokenize=True,
        max_tokens=256,
    )
    # Generate texts from the prompts.
    outputs = llm.generate(prompts, sampling_params)
    # Print the outputs.
    for output in outputs:
        prompt_token_ids = output.prompt_token_ids
        generated_text = output.outputs[0].text
        print(
            f"Prompt length: {len(prompt_token_ids)}, "
            f"Generated text: {generated_text!r}"
        )


# Create an LLM.
definitialize_engine() -> LLM:
    llm = LLM(
        model="Qwen/Qwen2.5-7B-Instruct-1M",
        max_model_len=1048576,
        tensor_parallel_size=4,
        enforce_eager=True,
        enable_chunked_prefill=True,
        max_num_batched_tokens=131072,
    )
    return llm


defmain():
    llm = initialize_engine()
    prompt = load_prompt()
    process_requests(llm, [prompt])


if __name__ == "__main__":
    main()
```