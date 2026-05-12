---
title: Batch Invariance - vLLM
url: https://docs.vllm.ai/en/latest/features/batch_invariance/
source: sitemap
fetched_at: 2026-05-07T21:14:05.414245349-03:00
rendered_js: false
word_count: 383
summary: This document explains how to enable batch invariance in vLLM to ensure deterministic, reproducible model inference outputs regardless of batch size or request ordering.
tags:
    - vllm
    - deterministic-inference
    - batch-invariance
    - reproducibility
    - gpu-computing
    - model-debugging
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/batch_invariance.md "Edit this page")

Note

Batch invariance is currently in beta. Some features are still under active development. Track progress and planned improvements at [Issue #27433](https://github.com/vllm-project/vllm/issues/27433)

This document shows how to enable batch invariance in vLLM. Batch invariance ensures that the output of a model is deterministic and independent of the batch size or the order of requests in a batch.

## Motivation[¶](#motivation "Permanent link")

Batch invariance is crucial for several use cases:

- **Framework debugging**: Deterministic outputs make it easier to debug issues in the inference framework, as the same input will always produce the same output regardless of batching.
- **Model debugging**: Helps identify issues in model implementations by ensuring consistent behavior across different batch configurations.
- **Reinforcement Learning (RL)**: RL training often requires deterministic rollouts for reproducibility and stable training.
- **Large-scale inference systems**: Systems that use vLLM as a component benefit from deterministic behavior for testing, validation, and consistency guarantees.

## Hardware Requirements[¶](#hardware-requirements "Permanent link")

Batch invariance currently requires NVIDIA GPUs with compute capability 9.0 or higher:

- **H-series**: H100, H200
- **B-series**: B100, B200

## Enabling Batch Invariance[¶](#enabling-batch-invariance "Permanent link")

Batch invariance can be enabled by setting the `VLLM_BATCH_INVARIANT` environment variable to `1`:

```
exportVLLM_BATCH_INVARIANT=1
```

### Online Inference (Server Mode)[¶](#online-inference-server-mode "Permanent link")

To start a vLLM server with batch invariance enabled:

```
VLLM_BATCH_INVARIANT=1vllmservemeta-llama/Llama-3.1-8B-Instruct
```

Then use the OpenAI-compatible client:

```
fromopenaiimport OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1",
)

# These requests will produce deterministic outputs
# regardless of batch size or order
response = client.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    prompt="The future of AI is",
    max_tokens=100,
    temperature=0.7,
    seed=42,
)

print(response.choices[0].text)
```

### Offline Inference[¶](#offline-inference "Permanent link")

For offline batch inference with batch invariance:

```
importos
os.environ["VLLM_BATCH_INVARIANT"] = "1"

fromvllmimport LLM, SamplingParams

prompts = [
    "The future of AI is",
    "Machine learning enables",
    "Deep learning models can",
]

sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.95,
    max_tokens=100,
    seed=42,
)

llm = LLM(
    model="meta-llama/Llama-3.1-8B-Instruct",
    tensor_parallel_size=1,
)

# Outputs will be deterministic regardless of batch size
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}")
    print(f"Generated: {generated_text!r}\n")
```

## Tested Models[¶](#tested-models "Permanent link")

Batch invariance has been tested and verified on the following models:

- **DeepSeek series**: `deepseek-ai/DeepSeek-V3`, `deepseek-ai/DeepSeek-V3-0324`, `deepseek-ai/DeepSeek-R1`, `deepseek-ai/DeepSeek-V3.1`
- **Qwen3 (Dense)**: `Qwen/Qwen3-1.7B`, `Qwen/Qwen3-8B`, `Qwen/Qwen3-4B-AWQ`, `Qwen/Qwen3-8B-AWQ`
- **Qwen3 (MoE)**: `Qwen/Qwen3-30B-A3B`, `Qwen/Qwen3-Next-80B-A3B-Instruct`, `Qwen/Qwen3-30B-A3B-Thinking-2507-FP8`
- **Qwen2.5**: `Qwen/Qwen2.5-0.5B-Instruct`, `Qwen/Qwen2.5-1.5B-Instruct`, `Qwen/Qwen2.5-3B-Instruct`, `Qwen/Qwen2.5-7B-Instruct`, `Qwen/Qwen2.5-14B-Instruct`, `Qwen/Qwen2.5-32B-Instruct`
- **Llama 3**: `meta-llama/Llama-3.1-8B-Instruct`, `meta-llama/Llama-3.2-1B-Instruct`
- **GPT-OSS**: `openai/gpt-oss-20b`, `openai/gpt-oss-120b`
- **Mistral**: `mistralai/Mistral-7B-v0.3`

Other models may also work, but these have been explicitly validated. If you encounter issues with a specific model, please report them on the [GitHub issue tracker](https://github.com/vllm-project/vllm/issues/new/choose).

## Implementation Details[¶](#implementation-details "Permanent link")

When batch invariance is enabled, vLLM:

1. Uses deterministic kernel implementations for attention and other operations
2. Ensures consistent numerical behavior across different batch sizes
3. Disables certain optimizations that may introduce non-determinism (such as custom all-reduce operations in tensor parallel mode)

Note

Enabling batch invariance may impact performance compared to the default non-deterministic mode. This trade-off is intentional to guarantee reproducibility.

## Future Improvements[¶](#future-improvements "Permanent link")

The batch invariance feature is under active development. Planned improvements include:

- Support for additional GPU architectures
- Expanded model coverage
- Performance optimizations
- Additional testing and validation

For the latest status and to contribute ideas, see the [tracking issue](https://github.com/vllm-project/vllm/issues/27433).