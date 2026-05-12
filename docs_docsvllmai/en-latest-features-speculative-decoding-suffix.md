---
title: Suffix Decoding - vLLM
url: https://docs.vllm.ai/en/latest/features/speculative_decoding/suffix/
source: sitemap
fetched_at: 2026-05-07T21:14:44.18035405-03:00
rendered_js: false
word_count: 164
summary: This document explains how to configure vLLM to utilize Suffix Decoding for speculative token generation, detailing its mechanism, benefits for repetitive tasks, and implementation requirements.
tags:
    - vllm
    - speculative-decoding
    - suffix-decoding
    - llm-inference
    - performance-optimization
    - arctic-inference
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/speculative_decoding/suffix.md "Edit this page")

The following code configures vLLM to use speculative decoding where proposals are generated using Suffix Decoding ([technical report](https://arxiv.org/abs/2411.04975)).

Like n-gram, Suffix Decoding can generate draft tokens by pattern-matching using the last `n` generated tokens. Unlike n-gram, Suffix Decoding (1) can pattern-match against both the prompt and previous generations, (2) uses frequency counts to propose the most likely continuations, and (3) speculates an adaptive number of tokens for each request at each iteration to get better acceptance rates.

Suffix Decoding can achieve better performance for tasks with high repetition, such as code-editing, agentic loops (e.g. self-reflection, self-consistency), and RL rollouts.

Install Arctic Inference

Suffix Decoding requires [Arctic Inference](https://github.com/snowflakedb/ArcticInference). You can install it with `pip install arctic-inference`.

Suffix Decoding Speculative Tokens

Suffix Decoding will speculate a dynamic number of tokens for each request at each decoding step, so the `num_speculative_tokens` configuration specifies the *maximum* number of speculative tokens. It is suggested to use a high number such as `16` or `32` (default).

```
fromvllmimport LLM, SamplingParams

prompts = ["The future of AI is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(
    model="Qwen/Qwen3-8B",
    tensor_parallel_size=1,
    speculative_config={
        "method": "suffix",
        "num_speculative_tokens": 32,
    },
)
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```