---
title: Unsloth Dynamic GGUFs on Aider Polyglot
url: https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs/unsloth-dynamic-ggufs-on-aider-polyglot.md
source: llms
fetched_at: 2026-04-27T18:15:05.953846858-03:00
rendered_js: false
word_count: 1430
summary: This document details how Unsloth's Dynamic GGUFs enable extreme quantization of large language models, such as DeepSeek-V3.1, down to 1-bit or 3-bit while maintaining high performance. It showcases superior results against SOTA models using the Aider Polyglot benchmark across reasoning and non-reasoning tasks.
tags:
    - unsloth
    - dynamic-ggufs
    - llm-quantization
    - deepseek-v31
    - aider-polyglot
    - model-performance
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Unsloth Dynamic GGUFs on Aider Polyglot

Unsloth Dynamic GGUFs quantize [DeepSeek-V3.1](https://unsloth.ai/docs/models/tutorials/deepseek-v3.1-how-to-run-locally) (671B) to **1-bit** or **3-bit** while outperforming GPT-4.5, GPT-4.1 (Apr 2025), and Claude-4-Opus (May 2025). Previous results on [[115-basics-unsloth-dynamic-2.0-ggufs|Dynamic GGUFs]] showed superiority on 5-shot MMLU and KL Divergence; this page covers independent third-party evaluation via the **Aider Polyglot** benchmark.

### Key results

- **1-bit** Dynamic GGUF: DeepSeek-V3.1 671GB -> 192GB (-75%), no-thinking mode outperforms GPT-4.1, GPT-4.5, DeepSeek-V3-0324
- **3-bit** Dynamic GGUF (thinking): outperforms Claude-4-Opus-20250514 (thinking)
- **5-bit** Dynamic GGUF (non-thinking): matches Claude-4-Opus-20250514 (non-thinking)
- Consistently outperforms non-Unsloth Dynamic imatrix GGUFs
- Other non-Unsloth 1-bit/2-bit quantizations and standard 1-bit without selective layer quantization either failed to load or produced gibberish/looping outputs

**Why Aider Polyglot?** One of the most comprehensive measures of LLM coding, instruction-following, and autonomous change application — one of the hardest real-world benchmarks.

> [!tip] Unsloth actively fixes critical bugs in major models. Collaborations with [Qwen3](https://www.reddit.com/r/LocalLLaMA/comments/1kaodxu/qwen3_unsloth_dynamic_ggufs_128k_context_bug_fixes/), [Meta (Llama 4)](https://github.com/ggml-org/llama.cpp/pull/12889), [Mistral (Devstral)](https://app.gitbook.com/o/HpyELzcNe0topgVLGCZY/s/xhOjnexMCB3dmuQFQ2Zq/~/changes/618/basics/tutorials-how-to-fine-tune-and-run-llms/devstral-how-to-run-and-fine-tune), [Google (Gemma 1-3)](https://news.ycombinator.com/item?id=39691146), [Microsoft (Phi-3/4)](https://simonwillison.net/2025/Jan/11/phi-4-bug-fixes) contribute essential accuracy fixes.

## Unsloth Dynamic Quantization

> [!tip] Dynamic 1-bit: important layers in 8 or 16 bits, unimportant layers in 1-6 bits.

Nov 2024: [4-bit Dynamic](https://unsloth.ai/blog/dynamic-4bit) Quants showed QLoRA fine-tuning accuracy restoration via selective layer quantization. Applied to [DeepSeek-R1](https://unsloth.ai/docs/models/tutorials/deepseek-r1-how-to-run-locally)'s architecture — some layers at 1-bit, important layers at 6/8-bit. This became the de facto method for MoE quantization.

Paired with [imatrix calibration dataset](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) for chat/coding performance, enabling extreme compression without catastrophic quality loss.

Example: naive 4-bit quantization of Qwen2-VL-2B-Instruct causes it to misidentify a train as a coastal scene. Selective quantization preserves visual understanding.

Dynamic benchmarks for Gemma 3 and Llama 4 Scout: see [[115-basics-unsloth-dynamic-2.0-ggufs]].

### Benchmark setup

DeepSeek-V3.1 experiments compared Unsloth Dynamic GGUFs against:

- Full-precision unquantized LLMs (GPT 4.5, 4.1, Claude-4-Opus, DeepSeek-V3-0324)
- Other dynamic imatrix V3.1 GGUFs
- Semi-dynamic (partial selective layer quantization) imatrix V3.1 GGUFs for ablation

Experiments conducted by [David Sluys](https://www.linkedin.com/in/david-sluys-231348208/) (neolithic5452 on [Aider Discord](https://discord.com/channels/1131200896827654144/1408293692074360914)). Tests run ~3x and averaged; Pass-2 accuracy reported.

<details>
<summary>Reasoning model Aider benchmarks</summary>

| Model | Accuracy |
| --- | --- |
| GPT-5 | 86.7 |
| Gemini 2.5 Pro (June) | 83.1 |
| o3 | 76.9 |
| DeepSeek V3.1 | 76.1 |
| **(3 bit) DeepSeek V3.1 Unsloth** | **75.6** |
| Claude-4-Opus (May) | 72 |
| o4-mini (High) | 72 |
| DeepSeek R1 0528 | 71.4 |
| **(2 bit) DeepSeek V3.1 Unsloth** | **66.7** |
| Claude-3.7-Sonnet (Feb) | 64.9 |
| **(1 bit) DeepSeek V3.1 Unsloth** | **57.8** |
| DeepSeek R1 | 56.9 |

</details>

<details>
<summary>Non Reasoning model Aider benchmarks</summary>

| Model | Accuracy |
| --- | --- |
| DeepSeek V3.1 | 71.6 |
| Claude-4-Opus (May) | 70.7 |
| **(5 bit) DeepSeek V3.1 Unsloth** | **70.7** |
| **(4 bit) DeepSeek V3.1 Unsloth** | **69.7** |
| **(3 bit) DeepSeek V3.1 Unsloth** | **68.4** |
| **(2 bit) DeepSeek V3.1 Unsloth** | **65.8** |
| Qwen3 235B A22B | 59.6 |
| Kimi K2 | 59.1 |
| **(1 bit) DeepSeek V3.1 Unsloth** | **55.7** |
| DeepSeek V3-0324 | 55.1 |
| GPT-4.1 (April, 2025) | 52.4 |
| ChatGPT 4o (March, 2025) | 45.3 |
| GPT-4.5 | 44.9 |

</details>

Non-reasoning trend: dynamic 5-bit = 70.7%, dynamic 1-bit = 55.7%. 3-bit and 4-bit offer best size/accuracy tradeoff.

## Comparison to other quants

Compared against other community dynamic imatrix GGUFs on Aider Polyglot. Fair comparison methodology:

1. Select similar-sized files and bit types per Unsloth quant
2. Use fixed chat template if community quant fails — some community quants error with `{"code":500,"message":"split method must have between 1 and 1 positional arguments..."}`, fixed by Unsloth chat template

<details>
<summary>Raw numerical data — other quants comparison</summary>

| Quant | Quant Size (GB) | Unsloth Accuracy % | Comparison Accuracy % |
| --- | --- | --- | --- |
| IQ2_XXS | 164 | | 43.6 |
| TQ1_0 | 170 | 50.7 | |
| IQ1_M | 206 | 55.7 | |
| IQ2_M | 215 | | 56.6 |
| IQ2_XXS | 225 | 61.2 | |
| IQ2_M | 235 | 64.3 | |
| Q2_K_L | 239 | | 64.0 |
| Q2_K_XL | 255 | 65.8 | |
| IQ3_XXS | 268 | 65.6 | 65.6 |
| IQ3_XXS | 279 | 66.8 | |
| Q3_K_S | 293 | | 65.2 |
| Q3_K_XL | 300 | 68.4 | |
| IQ4_XS | 357 | 69.2 | |
| IQ4_XS | 360 | | 66.3 |
| Q4_K_XL | 387 | 69.7 | |
| Q4_K_M | 405 | 69.7 | |
| Q4_K_M | 409 | | 67.7 |
| Q5_K_M | 478 | | 68.9 |
| Q5_K_XL | 484 | 70.7 | |

</details>

### Dynamic quantization ablations

Ablations confirm calibration dataset and dynamic methodology work. Trick: quantize important layers to higher bits (e.g., 8-bit), unimportant to lower bits (e.g., 2-bit).

Test: leave specific tensors at 4-bit (semi-dynamic) vs 8-bit (Unsloth). Increasing quant size by ~100MB (<0.1%) dramatically improves accuracy.

> [!tip] `attn_k_b` and other tensors in DeepSeek V3.1 are highly sensitive to quantization — keep in higher precision to retain accuracy.

### Chat Template Bug Fixes

Lower-bit quants failed to enclose thinking tokens properly. llama.cpp's minja (simplified jinja) rejects positional arguments in `.split`. Fix applied:

```
{%- set content = content.split("🧠", 1)[1] -%}
```

changed to:

```
{%- set splitted = content.split("🧠") -%}
{%- set content = splitted[1:] | join("🧠") -%}
```

Fixed chat template: [HuggingFace](https://huggingface.co/unsloth/DeepSeek-V3.1-GGUF?chat_template=default\&format=true) | [raw jinja](https://huggingface.co/unsloth/DeepSeek-V3.1/raw/main/chat_template.jinja)

### Pass Rate 1

Aider standard is Pass Rate 2. Pass Rate 1 shows dynamic quants outperform community quants at same size, especially below 2-bit and above 4-bit. 3-bit and 4-bit perform similarly well.

## Run DeepSeek V3.1 Dynamic quants

See [[116-models-tutorials-deepseek-r1-how-to-run-locally-deepseek-r1-dynamic-1.58-bit|DeepSeek V3.1 guide]] or use llama.cpp directly:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-quantize llama-cli llama-gguf-split llama-mtmd-cli llama-server
cp llama.cpp/build/bin/llama-* llama.cpp
```

```bash
export LLAMA_CACHE="unsloth/DeepSeek-V3.1-GGUF"
./llama.cpp/llama-cli \
    -hf unsloth/DeepSeek-V3.1-GGUF:Q2_K_XL \
    --jinja \
    --n-gpu-layers 99 \
    --temp 0.6 \
    --top_p 0.95 \
    --min_p 0.01 \
    --ctx-size 8192 \
    --seed 3407 \
    -ot ".ffn_.*_exps.=CPU"
```

Optimal temperature, chat template, and other parameters are pre-configured.

---

# Agent Instructions: Querying This Documentation

If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter:

```
GET https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs/unsloth-dynamic-ggufs-on-aider-polyglot.md?ask=<question>
```

The question should be specific, self-contained, and written in natural language.
The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.

#quantization #gguf #deepseek-v31 #aider-benchmark #dynamic-quantization
