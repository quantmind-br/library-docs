---
title: Metrics - vLLM
url: https://docs.vllm.ai/en/latest/examples/observability/metrics/
source: sitemap
fetched_at: 2026-05-07T21:13:08.750837325-03:00
rendered_js: false
word_count: 7
summary: This document demonstrates how to extract and monitor operational metrics from the vLLM library during offline inference tasks.
tags:
    - vllm
    - observability
    - metrics-monitoring
    - offline-inference
    - performance-tracking
category: tutorial
---

[](https://github.com/vllm-project/vllm/edit/main/docs/examples/observability/metrics.md "Edit this page")

Source [https://github.com/vllm-project/vllm/tree/main/examples/observability/metrics](https://github.com/vllm-project/vllm/tree/main/examples/observability/metrics).

## Offline[¶](#offline "Permanent link")

```
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

fromvllmimport LLM, SamplingParams
fromvllm.v1.metrics.readerimport Counter, Gauge, Histogram, Vector

# Sample prompts.
prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]
# Create a sampling params object.
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)


defmain():
    # Create an LLM.
    llm = LLM(model="facebook/opt-125m", disable_log_stats=False)

    # Generate texts from the prompts.
    outputs = llm.generate(prompts, sampling_params)

    # Print the outputs.
    print("-" * 50)
    for output in outputs:
        prompt = output.prompt
        generated_text = output.outputs[0].text
        print(f"Prompt: {prompt!r}\nGenerated text: {generated_text!r}")
        print("-" * 50)

    # Dump all metrics
    for metric in llm.get_metrics():
        if isinstance(metric, Gauge):
            print(f"{metric.name} (gauge) = {metric.value}")
        elif isinstance(metric, Counter):
            print(f"{metric.name} (counter) = {metric.value}")
        elif isinstance(metric, Vector):
            print(f"{metric.name} (vector) = {metric.values}")
        elif isinstance(metric, Histogram):
            print(f"{metric.name} (histogram)")
            print(f"    sum = {metric.sum}")
            print(f"    count = {metric.count}")
            for bucket_le, value in metric.buckets.items():
                print(f"    {bucket_le} = {value}")


if __name__ == "__main__":
    main()
```