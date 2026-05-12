---
title: Draft Models - vLLM
url: https://docs.vllm.ai/en/latest/features/speculative_decoding/draft_model/
source: sitemap
fetched_at: 2026-05-07T21:14:37.408308492-03:00
rendered_js: false
word_count: 95
summary: This document explains how to implement speculative decoding in vLLM using a draft model for both offline inference and online serving.
tags:
    - vllm
    - speculative-decoding
    - draft-model
    - offline-inference
    - model-serving
    - llm-optimization
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/speculative_decoding/draft_model.md "Edit this page")

The following code configures vLLM in an offline mode to use speculative decoding with a draft model, speculating 5 tokens at a time.

```
fromvllmimport LLM, SamplingParams

prompts = ["The future of AI is"]
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

llm = LLM(
    model="Qwen/Qwen3-8B",
    tensor_parallel_size=1,
    speculative_config={
        "model": "Qwen/Qwen3-0.6B",
        "num_speculative_tokens": 5,
        "method": "draft_model",
    },
)
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")
```

To perform the equivalent launch in online mode, use the following server-side code:

```
vllmserveQwen/Qwen3-4B-Thinking-2507\
--host0.0.0.0\
--port8000\
--seed42\
-tp1\
--max-model-len2048\
--gpu-memory-utilization0.8\
--speculative-config'{"model": "Qwen/Qwen3-0.6B", "num_speculative_tokens": 5, "method": "draft_model"}'
```

The code used to request as completions as a client remains unchanged:

Code

```
fromopenaiimport OpenAI

# Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8000/v1"

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=openai_api_key,
    base_url=openai_api_base,
)

models = client.models.list()
model = models.data[0].id

# Completion API
stream = False
completion = client.completions.create(
    model=model,
    prompt="The future of AI is",
    echo=False,
    n=1,
    stream=stream,
)

print("Completion results:")
if stream:
    for c in completion:
        print(c)
else:
    print(completion)
```

Warning

Note: Please use `--speculative-config` to set all configurations related to speculative decoding. The previous method of specifying the model through `--speculative-model` and adding related parameters such as `--num-speculative-tokens` separately has been deprecated. For supported keys and examples, see the [`--speculative-config` schema](https://docs.vllm.ai/en/latest/features/speculative_decoding/#--speculative-config-schema).