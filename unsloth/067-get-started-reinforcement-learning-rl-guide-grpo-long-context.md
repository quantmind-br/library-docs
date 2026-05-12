---
title: Reinforcement Learning GRPO with 7x Longer Context
url: https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/grpo-long-context.md
source: llms
fetched_at: 2026-04-27T18:13:09.419472865-03:00
rendered_js: false
word_count: 1680
summary: This document introduces new batching algorithms for Reinforcement Learning (RL) within Unsloth that significantly extend the supported context length—up to 7x longer—without sacrificing accuracy or speed. The enhancements achieve this through techniques like flattened sequence chunking and offloading log softmax activations, enabling massive context training on modern GPUs.
tags:
    - reinforcement-learning
    - long-context
    - grpo
    - batching-algorithms
    - memory-efficiency
    - unsloth
category: guide
optimized: true
optimized_at: 2026-04-27T21:40:00Z
---

# Reinforcement Learning GRPO with 7x Longer Context

New batching algorithms enable ~**7x longer context** (up to 12x) RL training with no accuracy or speed degradation vs. FA3/kernels/chunked-loss setups.

- gpt-oss QLoRA: **380K context** on single 192GB B200
- [Qwen3](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune#fine-tuning-qwen3-with-unsloth)-8B GRPO: **110K context** on 80GB H100 via [vLLM](#vllm-for-rl) + QLoRA; **65K** for [gpt-oss](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/gpt-oss-reinforcement-learning) BF16 LoRA
- 24GB VRAM: gpt-oss 20K context; [Qwen3-VL](https://unsloth.ai/docs/models/tutorials/qwen3-how-to-run-and-fine-tune/qwen3-vl-how-to-run-and-fine-tune)-8B QLoRA 32K
- All models (Llama, Gemma, etc.) auto-support longer contexts

Memory unlocked via:

- Dynamic [flattened sequence chunking](#flattened-sequence-length-chunking) — avoids materializing massive logit tensors
- [Offloading log softmax](#offloading-activations-for-log-softmax) activations — prevents silent memory growth

> [!info] Combinable features
> 1. [[068-get-started-reinforcement-learning-rl-guide-memory-efficient-rl|Weight-sharing]] with [vLLM](https://github.com/vllm-project/vllm) and Standby Feature
> 2. [Flex Attention](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/long-context-gpt-oss-training) for long context gpt-oss + [[103-blog-500k-context-length-fine-tuning|500K context fine-tuning]]
> 3. Float8 in [[066-get-started-reinforcement-learning-rl-guide-fp8-reinforcement-learning|FP8 RL]] + async gradient checkpointing and more

## Getting Started

Use any existing [GRPO notebooks](https://unsloth.ai/docs/unsloth-notebooks#grpo-reasoning-rl-notebooks) (or update Unsloth):

- [**gpt-oss-20b**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) — GSPO
- [**Qwen3-VL-8B**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision-GRPO.ipynb) — Vision RL
- [Qwen3-8B - **FP8**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_8B_FP8_GRPO.ipynb) — L4 GPU

- **Hardware** — NVIDIA H100 or equivalent for optimal VRAM utilization
- **Config** — align `batch_size` and `gradient_accumulation_steps` with compute resources

> [!tip] Update Unsloth
> ```
> pip install --upgrade --no-cache-dir unsloth unsloth_zoo
> ```

Benchmarks compare BF16 GRPO to Hugging Face with all optimizations (all kernels, FA3, chunked loss). Both plots below (without [standby](https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/memory-efficient-rl)) run with `batch_size = 4`, `gradient_accumulation_steps=2`.

## Flattened Sequence Length Chunking

Unsloth previously reduced RL memory by avoiding full logits materialization via batch-dimension chunking. VRAM to materialize logits:

$$\text{Logit Memory (GB)} = \frac{\text{batch size} \times\text{context length} \times \text{vocab dim}}{1024^3}$$

Example: `batch_size=4`, `context_length=8192`, `vocab_dim=128,000` ≈ **3.3 GB VRAM**.

Via [long-context-gpt-oss-training](https://unsloth.ai/docs/models/gpt-oss-how-to-run-and-fine-tune/long-context-gpt-oss-training) fused loss approach processes one batch sample at a time:

$$\text{Logit Memory (GB)} = \frac{\text{context length} \times \text{vocab dim}}{1024^3}$$

Same config drops to ~**0.83 GB**.

This update extends chunking across the **sequence dimension** — flattens batch and sequence dimensions, processes in smaller chunks via configurable multiplier. Same example with multiplier `max(4, context_length // 4096)`:

$$\text{Logit Memory (GB)} = \frac{\frac{\text{context length}}{\text{multiplier}} \times \text{vocab dim}}{1024^3}$$

Now only **0.207 GB VRAM** for logits.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fy1TkzxySrNAeeSWJSVLU%2Funsloth_vs_trl_gpt_oss.png?alt=media&#x26;token=0303423d-1454-4410-8be8-7d6110ac1df0" alt="" width="375"><figcaption><p>Figure 1: gpt-oss BF16 GRPO LoRA (Unsloth vs. HF with all optimizations on)</p></figcaption></figure> <figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FmfKhenN0TGRDlMcuxob6%2Fqwen38b%20long%20context%20grpo.png?alt=media&#x26;token=22883f90-5bf0-4478-91a9-6a191c920f12" alt="" width="375"><figcaption><p>Figure 2: Qwen3-8B QLoRA GRPO LoRA (Unsloth vs. HF with all optimizations on)</p></figcaption></figure>

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FWFTbejdIn3T6E6yHgF1Z%2FCode_Generated_Image%20(2).png?alt=media&#x26;token=790a1ee4-2814-4b29-afcb-bb9ffd1eb729" alt="" width="375"><figcaption><p>Figure 3: gpt-oss-20b (H100) Unsloth new vs. old</p></figcaption></figure> <figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2Fi4QipufoavtPKyeRU0Vv%2FCode_Generated_Image%20(3).png?alt=media&#x26;token=226c5a3c-a0a4-458d-a0df-8c84523b04b5" alt="" width="375"><figcaption><p>Figure 4: Qwen3-8B (H100) Unsloth new vs. old</p></figcaption></figure> <figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FkSIh1DIWvKGemnNHowPs%2FCode_Generated_Image_4.png?alt=media&#x26;token=0a3dfe85-ae8c-4280-bc0a-6c1f1523c90e" alt="" width="375"><figcaption><p>Figure 5: gpt-oss-20b (H100)</p></figcaption></figure> <figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FRP1RPiOeIYOt82L1Ifkc%2FCode_Generated_Image_5.png?alt=media&#x26;token=4ce06b0f-2464-41fd-8795-e5bf0dbf4327" alt="" width="375"><figcaption><p>Figure 6: Qwen3-8B (B200)</p></figcaption></figure>

The compiled `chunked_hidden_states_selective_log_softmax` now chunks across both batch and sequence dimensions. Logits tensor `[batch_size, context_length, vocab_dim]` is always chunked across batch; sequence chunking controlled via `unsloth_logit_chunk_multiplier` in GRPO config (defaults to `max(4, context_length // 4096)`). `input_ids_chunk[0]` = size of hidden states mini batches in optimization 2.

```python
logprobs_chunk = chunked_hidden_states_selective_log_softmax(
    new_hidden_states_chunk,
    lm_head,
    completion_ids,
    chunks=input_ids_chunk.shape[0]*multiplier,
    logit_scale_multiply=logit_scale_multiply,
    logit_scale_divide=logit_scale_divide,
    logit_softcapping=logit_softcapping,
    temperature=temperature,
)
```

1. Uses `torch.compile` with custom compile options to reduce VRAM and increase speed
2. All chunked logits upcasted in float32 to preserve accuracy
3. Supports logit softcapping, temperature scaling, and all other features

## Hidden States Chunking

At longer context lengths, hidden states become a significant memory contributor (`hidden_states_dim=4096`):

$$\text{Hidden States Memory (GB)} = \frac{\text{batch size} \times\text{context length} \times \text{hidden states dim}}{1024^3}$$

`batch_size=8`, `context_length=64000` ≈ **2 GB**. Optional batch-dimension chunking divides by batch size → **0.244 GB**:

$$\text{Hidden States Memory (GB)} = \frac{\text{context length} \times \text{hidden states dim}}{1024^3}$$

Automatically tunes hidden state batching (like [[103-blog-500k-context-length-fine-tuning|cross entropy loss in 500K context release]]). Control via `unsloth_grpo_mini_batch` — increasing beyond optimal may slightly change speed (usually faster).

GPT-OSS run (`context_length=8192, batch_size=4, gradient_accumulation_steps=2`) with `unsloth_grpo_mini_batch=1` and `unsloth_logit_chunk_multiplier=4`: **~5 GB VRAM reduction** with little/no speed degradation.

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FYZsgoKpZKyJKrNmbvehR%2FCode_Generated_Image%20(4).png?alt=media&#x26;token=5d3c0605-9ed8-4d4a-a722-a85132510222" alt="" width="375"><figcaption></figcaption></figure>

> [!tip] Effective batch size
> Figures 3 and 4 use max effective batch size = 8 (`batch_size × gradient_accumulation_steps` = `4 × 2`). See [[113-get-started-reinforcement-learning-rl-guide-advanced-rl-documentation|advanced RL documentation]] for deeper explanation.

## Offloading Activations for Log Softmax

When tiling across batch dimension for hidden states, activations were not offloaded after fused logits/logprobs computation. Since logits are computed one batch at a time (`hidden_states[i] @ lm_head`), existing activation offloading/gradient checkpointing logic (designed for model forward pass) did not apply.

Fix: explicit offloading outside model's forward pass:

```python
class Unsloth_Offloaded_Log_Softmax(torch.autograd.Function):
    def forward(...):
        with torch.no_grad():
            output = chunked_hidden_states_selective_log_softmax(hidden_states, lm_head, ...)
        return output
    def backward(ctx, grad_output):
        hidden_states = ctx.saved_hidden_states
        hidden_states.requires_grad_(True)
        with torch.enable_grad():
            output = chunked_hidden_states_selective_log_softmax(hidden_states, lm_head, ...)
        torch.autograd.backward(output, grad_output)
        return ...
```

> [!tip] Activation offloading caveat
> Only effective when chunking across batch dimension (`unsloth_grpo_mini_batch > 1`). If all hidden states materialized at once (`unsloth_grpo_mini_batch = 1`), backward pass uses same GPU memory regardless — offloading adds slight slowdown with no memory benefit.

## Configuring Parameters

If `unsloth_grpo_mini_batch` and `unsloth_logit_chunk_multiplier` are unset, Unsloth **auto-tunes** based on available VRAM and context length.

```python
training_args = GRPOConfig(
    ...
    unsloth_grpo_mini_batch = 3
    unsloth_logit_chunk_multiplier = 2
    ...
)
```

<figure><img src="https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2F2OmZA297HzG3CdRzi3X5%2FLogit%20Chunking%20(1).png?alt=media&#x26;token=b953a62b-fefa-43f2-a9ce-108675b8735f" alt="" width="375"><figcaption></figcaption></figure>

- **3 matrices** = overall larger batch / `unsloth_grpo_mini_batch` (black brackets)
- **Rows per matrix** = context length chunked by `unsloth_logit_chunk_multiplier` (red brackets)

## vLLM for RL

Inference/generation is the main RL bottleneck. [vLLM](https://github.com/vllm-project/vllm) accelerates generation up to **11x** vs. normal generation. vLLM has been a core component of most RL frameworks including Unsloth since GRPO was popularized.

Notebooks for longer context RL:

- [**gpt-oss-20b**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/gpt-oss-\(20B\)-GRPO.ipynb) — GSPO
- [**Qwen3-VL-8B**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_\(8B\)-Vision-GRPO.ipynb) — Vision RL
- [Qwen3-8B - **FP8**](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_8B_FP8_GRPO.ipynb) — L4 GPU

---

# Agent Instructions: Querying This Documentation

If you need additional information not on this page, query dynamically via HTTP GET on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/grpo-long-context.md?ask=<question>
```

The question should be specific, self-contained, and in natural language. The response contains a direct answer with relevant excerpts and sources.

#reinforcement-learning #long-context #grpo #memory-efficiency
