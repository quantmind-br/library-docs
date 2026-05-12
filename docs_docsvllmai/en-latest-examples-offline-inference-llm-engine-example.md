---
title: LLM Engine Example - vLLM
url: https://docs.vllm.ai/en/latest/examples/offline_inference/llm_engine_example/
source: sitemap
fetched_at: 2026-05-07T21:13:12.96766528-03:00
rendered_js: false
word_count: 98
summary: This document demonstrates how to utilize the LLMEngine class for executing offline inference tasks with customized sampling parameters in the vLLM framework.
tags:
    - vllm
    - offline-inference
    - llm-engine
    - python-framework
    - sampling-parameters
    - machine-learning
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/offline_inference/llm_engine_example.md "Edit this page")

Source [https://github.com/vllm-project/vllm/blob/main/examples/offline\_inference/llm\_engine\_example.py](https://github.com/vllm-project/vllm/blob/main/examples/offline_inference/llm_engine_example.py).

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This file demonstrates using the `LLMEngine`
for processing prompts with various sampling parameters.
"""

importargparse

fromvllmimport EngineArgs, LLMEngine, RequestOutput, SamplingParams
fromvllm.utils.argparse_utilsimport FlexibleArgumentParser


defcreate_test_prompts() -> list[tuple[str, SamplingParams]]:
"""Create a list of test prompts with their sampling parameters."""
    return [
        (
            "A robot may not injure a human being",
            SamplingParams(temperature=0.0, logprobs=1, prompt_logprobs=1),
        ),
        (
            "To be or not to be,",
            SamplingParams(temperature=0.8, top_k=5, presence_penalty=0.2),
        ),
        (
            "What is the meaning of life?",
            SamplingParams(n=2, temperature=0.8, top_p=0.95, frequency_penalty=0.1),
        ),
    ]


defprocess_requests(engine: LLMEngine, test_prompts: list[tuple[str, SamplingParams]]):
"""Continuously process a list of prompts and handle the outputs."""
    request_id = 0

    print("-" * 50)
    while test_prompts or engine.has_unfinished_requests():
        if test_prompts:
            prompt, sampling_params = test_prompts.pop(0)
            engine.add_request(str(request_id), prompt, sampling_params)
            request_id += 1

        request_outputs: list[RequestOutput] = engine.step()

        for request_output in request_outputs:
            if request_output.finished:
                print(request_output)
                print("-" * 50)


definitialize_engine(args: argparse.Namespace) -> LLMEngine:
"""Initialize the LLMEngine from the command line arguments."""
    engine_args = EngineArgs.from_cli_args(args)
    return LLMEngine.from_engine_args(engine_args)


defparse_args():
    parser = FlexibleArgumentParser(
        description="Demo on using the LLMEngine class directly"
    )
    parser = EngineArgs.add_cli_args(parser)
    return parser.parse_args()


defmain(args: argparse.Namespace):
"""Main function that sets up and runs the prompt processing."""
    engine = initialize_engine(args)
    test_prompts = create_test_prompts()
    process_requests(engine, test_prompts)


if __name__ == "__main__":
    args = parse_args()
    main(args)
```