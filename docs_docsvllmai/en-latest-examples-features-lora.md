---
title: LoRA - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/lora/
source: sitemap
fetched_at: 2026-05-07T21:12:53.983828322-03:00
rendered_js: false
word_count: 104
summary: This document provides code examples demonstrating how to perform offline inference using LoRA adapters in conjunction with various quantization techniques and multi-adapter configurations within the vLLM engine.
tags:
    - lora
    - quantization
    - offline-inference
    - llm-fine-tuning
    - adapter-management
    - vllm
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/features/lora.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/lora](https://github.com/vllm-project/vllm/tree/main/examples/features/lora).

## LoRA With Quantization Offline[¶](#lora-with-quantization-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This example shows how to use LoRA with different quantization techniques
for offline inference.

Requires HuggingFace credentials for access.
"""

importgc

importtorch
fromhuggingface_hubimport snapshot_download

fromvllmimport EngineArgs, LLMEngine, RequestOutput, SamplingParams
fromvllm.lora.requestimport LoRARequest


defcreate_test_prompts(
    lora_path: str,
) -> list[tuple[str, SamplingParams, LoRARequest | None]]:
    return [
        # this is an example of using quantization without LoRA
        (
            "My name is",
            SamplingParams(temperature=0.0, logprobs=1, max_tokens=128),
            None,
        ),
        # the next three examples use quantization with LoRA
        (
            "my name is",
            SamplingParams(temperature=0.0, logprobs=1, max_tokens=128),
            LoRARequest("lora-test-1", 1, lora_path),
        ),
        (
            "The capital of USA is",
            SamplingParams(temperature=0.0, logprobs=1, max_tokens=128),
            LoRARequest("lora-test-2", 1, lora_path),
        ),
        (
            "The capital of France is",
            SamplingParams(temperature=0.0, logprobs=1, max_tokens=128),
            LoRARequest("lora-test-3", 1, lora_path),
        ),
    ]


defprocess_requests(
    engine: LLMEngine,
    test_prompts: list[tuple[str, SamplingParams, LoRARequest | None]],
):
"""Continuously process a list of prompts and handle the outputs."""
    request_id = 0

    while test_prompts or engine.has_unfinished_requests():
        if test_prompts:
            prompt, sampling_params, lora_request = test_prompts.pop(0)
            engine.add_request(
                str(request_id), prompt, sampling_params, lora_request=lora_request
            )
            request_id += 1

        request_outputs: list[RequestOutput] = engine.step()
        for request_output in request_outputs:
            if request_output.finished:
                print("----------------------------------------------------")
                print(f"Prompt: {request_output.prompt}")
                print(f"Output: {request_output.outputs[0].text}")


definitialize_engine(
    model: str, quantization: str, lora_repo: str | None
) -> LLMEngine:
"""Initialize the LLMEngine."""

    engine_args = EngineArgs(
        model=model,
        quantization=quantization,
        enable_lora=True,
        max_lora_rank=64,
        max_loras=4,
    )
    return LLMEngine.from_engine_args(engine_args)


defmain():
"""Main function that sets up and runs the prompt processing."""

    test_configs = [
        # QLoRA (https://arxiv.org/abs/2305.14314)
        {
            "name": "qlora_inference_example",
            "model": "huggyllama/llama-7b",
            "quantization": "bitsandbytes",
            "lora_repo": "timdettmers/qlora-flan-7b",
        },
        {
            "name": "AWQ_inference_with_lora_example",
            "model": "TheBloke/TinyLlama-1.1B-Chat-v0.3-AWQ",
            "quantization": "awq",
            "lora_repo": "jashing/tinyllama-colorist-lora",
        },
        {
            "name": "GPTQ_inference_with_lora_example",
            "model": "TheBloke/TinyLlama-1.1B-Chat-v0.3-GPTQ",
            "quantization": "gptq",
            "lora_repo": "jashing/tinyllama-colorist-lora",
        },
    ]

    for test_config in test_configs:
        print(f"~~~~~~~~~~~~~~~~ Running: {test_config['name']} ~~~~~~~~~~~~~~~~")
        engine = initialize_engine(
            test_config["model"], test_config["quantization"], test_config["lora_repo"]
        )
        lora_path = snapshot_download(repo_id=test_config["lora_repo"])
        test_prompts = create_test_prompts(lora_path)
        process_requests(engine, test_prompts)

        # Clean up the GPU memory for the next test
        del engine
        gc.collect()
        torch.accelerator.empty_cache()


if __name__ == "__main__":
    main()
```

## MultiLoRA Offline[¶](#multilora-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This example shows how to use the multi-LoRA functionality
for offline inference.

Requires HuggingFace credentials for access to Llama2.
"""

fromhuggingface_hubimport snapshot_download

fromvllmimport EngineArgs, LLMEngine, RequestOutput, SamplingParams
fromvllm.lora.requestimport LoRARequest


defcreate_test_prompts(
    lora_path: str,
) -> list[tuple[str, SamplingParams, LoRARequest | None]]:
"""Create a list of test prompts with their sampling parameters.

    2 requests for base model, 4 requests for the LoRA. We define 2
    different LoRA adapters (using the same model for demo purposes).
    Since we also set `max_loras=1`, the expectation is that the requests
    with the second LoRA adapter will be run after all requests with the
    first adapter have finished.
    """
    return [
        (
            "A robot may not injure a human being",
            SamplingParams(temperature=0.0, logprobs=1, max_tokens=128),
            None,
        ),
        (
            "To be or not to be,",
            SamplingParams(
                temperature=0.8, top_k=5, presence_penalty=0.2, max_tokens=128
            ),
            None,
        ),
        (
            "[user] Write a SQL query to answer the question based on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/user] [assistant]",  # noqa: E501
            SamplingParams(temperature=0.0, logprobs=1, max_tokens=128),
            LoRARequest("sql-lora", 1, lora_path),
        ),
        (
            "[user] Write a SQL query to answer the question based on the table schema.\n\n context: CREATE TABLE table_name_74 (icao VARCHAR, airport VARCHAR)\n\n question: Name the ICAO for lilongwe international airport [/user] [assistant]",  # noqa: E501
            SamplingParams(temperature=0.0, logprobs=1, max_tokens=128),
            LoRARequest("sql-lora2", 2, lora_path),
        ),
    ]


defprocess_requests(
    engine: LLMEngine,
    test_prompts: list[tuple[str, SamplingParams, LoRARequest | None]],
):
"""Continuously process a list of prompts and handle the outputs."""
    request_id = 0

    print("-" * 50)
    while test_prompts or engine.has_unfinished_requests():
        if test_prompts:
            prompt, sampling_params, lora_request = test_prompts.pop(0)
            engine.add_request(
                str(request_id), prompt, sampling_params, lora_request=lora_request
            )
            request_id += 1

        request_outputs: list[RequestOutput] = engine.step()

        for request_output in request_outputs:
            if request_output.finished:
                print(request_output)
                print("-" * 50)


definitialize_engine() -> LLMEngine:
"""Initialize the LLMEngine."""
    # max_loras: controls the number of LoRAs that can be used in the same
    #   batch. Larger numbers will cause higher memory usage, as each LoRA
    #   slot requires its own preallocated tensor.
    # max_lora_rank: controls the maximum supported rank of all LoRAs. Larger
    #   numbers will cause higher memory usage. If you know that all LoRAs will
    #   use the same rank, it is recommended to set this as low as possible.
    # max_cpu_loras: controls the size of the CPU LoRA cache.
    engine_args = EngineArgs(
        model="meta-llama/Llama-3.2-3B-Instruct",
        enable_lora=True,
        max_loras=1,
        max_lora_rank=8,
        max_cpu_loras=2,
        max_num_seqs=256,
    )
    return LLMEngine.from_engine_args(engine_args)


defmain():
"""Main function that sets up and runs the prompt processing."""
    engine = initialize_engine()
    lora_path = snapshot_download(repo_id="jeeejeee/llama32-3b-text2sql-spider")
    test_prompts = create_test_prompts(lora_path)
    process_requests(engine, test_prompts)


if __name__ == "__main__":
    main()
```