---
title: Context Extension - vLLM
url: https://docs.vllm.ai/en/latest/examples/features/context_extension/
source: sitemap
fetched_at: 2026-05-07T21:12:49.83695492-03:00
rendered_js: false
word_count: 9
summary: This document provides an example script demonstrating how to extend the context length of a language model using the YARN method within the vLLM framework.
tags:
    - vllm
    - context-extension
    - yarn-method
    - rope-parameters
    - model-configuration
    - nlp
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/features/context_extension.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/features/context\_extension](https://github.com/vllm-project/vllm/tree/main/examples/features/context_extension).

## Context Extension Offline[¶](#context-extension-offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project
"""
This script demonstrates how to extend the context length
of a Qwen model using the YARN method (rope_parameters)
and run a simple chat example.

Usage:
    python examples/features/context_extension/context_extension_offline.py
"""

fromvllmimport LLM, RequestOutput, SamplingParams


defcreate_llm():
    rope_theta = 1000000
    original_max_position_embeddings = 32768
    factor = 4.0

    # Use yarn to extend context
    hf_overrides = {
        "rope_parameters": {
            "rope_theta": rope_theta,
            "rope_type": "yarn",
            "factor": factor,
            "original_max_position_embeddings": original_max_position_embeddings,
        },
        "max_model_len": int(original_max_position_embeddings * factor),
    }

    llm = LLM(model="Qwen/Qwen3-0.6B", hf_overrides=hf_overrides)
    return llm


defrun_llm_chat(llm):
    sampling_params = SamplingParams(
        temperature=0.8,
        top_p=0.95,
        max_tokens=128,
    )

    conversation = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hello! How can I assist you today?"},
    ]
    outputs = llm.chat(conversation, sampling_params, use_tqdm=False)
    return outputs, [
        conversation,
    ]


defprint_outputs(outputs: list[RequestOutput], conversations: list):
    print("\nGenerated Outputs:\n" + "-" * 80)
    for i, output in enumerate(outputs):
        prompt = conversations[i]
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}\n")
        print(f"Generated text: {generated_text!r}")
        print("-" * 80)


defmain():
    llm = create_llm()
    outputs, conversations = run_llm_chat(llm)
    print_outputs(outputs, conversations)


if __name__ == "__main__":
    main()
```