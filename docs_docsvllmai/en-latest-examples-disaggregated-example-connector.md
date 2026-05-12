---
title: Disaggregated Prefill V1 - vLLM
url: https://docs.vllm.ai/en/latest/examples/disaggregated/example_connector/
source: sitemap
fetched_at: 2026-05-07T21:12:41.888849075-03:00
rendered_js: false
word_count: 91
summary: This document provides an example of implementing disaggregated prefill and decoding in vLLM by transferring KV state between separate execution instances using a connector.
tags:
    - vllm
    - disaggregated-prefill
    - kv-cache
    - offline-inference
    - llm-serving
    - model-performance
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/disaggregated/example_connector.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/example\_connector](https://github.com/vllm-project/vllm/tree/main/examples/disaggregated/example_connector).

This example contains scripts that demonstrate disaggregated prefill in the offline setting of vLLM.

## Files[¶](#files "Permanent link")

- `run.sh` - A helper script that will run `prefill_example.py` and `decode_example.py` sequentially.
  
  - Make sure you are in the `examples/disaggregated/example_connector` directory before running `run.sh`.
- `prefill_example.py` - A script which performs prefill only, saving the KV state to the `local_storage` directory and the prompts to `output.txt`.
- `decode_example.py` - A script which performs decode only, loading the KV state from the `local_storage` directory and the prompts from `output.txt`.

## Example materials[¶](#example-materials "Permanent link")

decode\_example.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromvllmimport LLM, SamplingParams
fromvllm.configimport KVTransferConfig


defread_prompts():
"""Read prompts from output.txt"""
    prompts = []
    try:
        with open("output.txt") as f:
            for line in f:
                prompts.append(line.strip())
        print(f"Loaded {len(prompts)} prompts from output.txt")
        return prompts
    except FileNotFoundError:
        print("Error: output.txt file not found")
        exit(-1)


defmain():
    prompts = read_prompts()
    sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=10)

    llm = LLM(
        model="meta-llama/Llama-3.2-1B-Instruct",
        enforce_eager=True,
        gpu_memory_utilization=0.8,
        max_num_batched_tokens=64,
        max_num_seqs=16,
        kv_transfer_config=KVTransferConfig(
            kv_connector="ExampleConnector",
            kv_role="kv_both",
            kv_connector_extra_config={"shared_storage_path": "local_storage"},
        ),
    )  # , max_model_len=2048, max_num_batched_tokens=2048)

    # 1ST generation (prefill instance)
    outputs = llm.generate(prompts, sampling_params)

    print("-" * 30)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
        print("-" * 30)


if __name__ == "__main__":
    main()
```

prefill\_example.py

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromvllmimport LLM, SamplingParams
fromvllm.configimport KVTransferConfig


defread_prompts():
    context = "Hi " * 1000
    context2 = "Hey " * 500
    return [
        context + "Hello, my name is",
        context + "The capital of France is",
        context2 + "Your name is",
        context2 + "The capital of China is",
    ]


defmain():
    prompts = read_prompts()

    sampling_params = SamplingParams(temperature=0, top_p=0.95, max_tokens=1)

    llm = LLM(
        model="meta-llama/Llama-3.2-1B-Instruct",
        enforce_eager=True,
        gpu_memory_utilization=0.8,
        kv_transfer_config=KVTransferConfig(
            kv_connector="ExampleConnector",
            kv_role="kv_both",
            kv_connector_extra_config={"shared_storage_path": "local_storage"},
        ),
    )  # , max_model_len=2048, max_num_batched_tokens=2048)

    # 1ST generation (prefill instance)
    outputs = llm.generate(
        prompts,
        sampling_params,
    )

    new_prompts = []
    print("-" * 30)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        new_prompts.append(prompt + generated_text)
        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
        print("-" * 30)

    # Write new_prompts to output.txt
    with open("output.txt", "w") as f:
        for prompt in new_prompts:
            f.write(prompt + "\n")
    print(f"Saved {len(new_prompts)} prompts to output.txt")


if __name__ == "__main__":
    main()
```

run.sh

```
rm-rflocal_storage/

if[-f"output.txt"];then
rmoutput.txt
fi

# The directory of current script
SCRIPT_DIR=$(dirname"$(readlink-f"$0")")

VLLM_ENABLE_V1_MULTIPROCESSING=0CUDA_VISIBLE_DEVICES=0python3"$SCRIPT_DIR/prefill_example.py"
VLLM_ENABLE_V1_MULTIPROCESSING=0CUDA_VISIBLE_DEVICES=0python3"$SCRIPT_DIR/decode_example.py"
```