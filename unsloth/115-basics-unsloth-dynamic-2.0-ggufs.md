---
title: Unsloth Dynamic 2.0 GGUFs
url: https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs.md
source: llms
fetched_at: 2026-04-27T18:15:04.440467982-03:00
rendered_js: false
word_count: 2103
summary: Major quantization enhancements preserving model accuracy while reducing file size. Covers dynamic layer selection, benchmarks across Gemma 4 and Qwen3.6.
tags:
    - unsloth-ggufs
    - dynamic-quantization
    - llm-optimization
    - benchmark-results
    - model-performance
    - llama-cpp
    - accuracy-preservation
category: reference
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Unsloth Dynamic 2.0 GGUFs

[Unsloth](https://github.com/unslothai/unsloth) Dynamic v2.0 quantization — major upgrade outperforming leading quantization methods on [Aider Polyglot](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs/unsloth-dynamic-ggufs-on-aider-polyglot), 5-shot MMLU, and KL Divergence. Run + fine-tune quantized LLMs while preserving accuracy on most inference engines (llama.cpp, [[102-new-studio-start|Unsloth Studio]], etc.).

**Updates:**

- **Apr 20, 2026** — New GGUF Benchmarks for [Qwen3.6](https://unsloth.ai/docs/models/qwen3.6#unsloth-gguf-benchmarks) and [Gemma 4](https://unsloth.ai/docs/models/gemma-4#unsloth-gguf-benchmarks)
- **Feb 27, 2026** — [Qwen3.5](https://unsloth.ai/docs/models/qwen3.5/gguf-benchmarks) benchmarks, fixed tool-calling chat template issues, benchmarked every GGUF on perplexity & KL Divergence
- **Sept 10, 2025** — Aider Polyglot results: Dynamic 3-bit DeepSeek V3.1 GGUF scores **75.6%**, surpassing many full-precision SOTA LLMs. [Read more.](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs/unsloth-dynamic-ggufs-on-aider-polyglot)

> [!tip] Unsloth Dynamic GGUFs can now be run in [[102-new-studio-start|Unsloth Studio]].

**Key advantage**: Unsloth actively fixes bugs in major models, collaborating with [Qwen3](https://www.reddit.com/r/LocalLLaMA/comments/1kaodxu/qwen3_unsloth_dynamic_ggufs_128k_context_bug_fixes/), [Meta (Llama 4)](https://github.com/ggml-org/llama.cpp/pull/12889), [Mistral (Devstral)](https://app.gitbook.com/o/HpyELzcNe0topgVLGCZY/s/xhOjnexMCB3dmuQFQ2Zq/~/changes/618/basics/tutorials-how-to-fine-tune-and-run-llms/devstral-how-to-run-and-fine-tune), [Google (Gemma 1-3)](https://news.ycombinator.com/item?id=39671146), [Microsoft (Phi-3/4)](https://simonwillison.net/2025/Jan/11/phi-4-bug-fixes).

External benchmarks by Benjamin Marie (LiveCodeBench v6, MMLU Pro, etc.) confirm Unsloth GGUFs outperform non-Unsloth quants at ~8GB smaller.

## What's New in Dynamic v2.0

- **Revamped Layer Selection** — dynamically adjusts quantization type of every possible layer; combinations differ per layer and model (GGUFs + safetensors)
- **New calibration dataset** — >1.5M tokens (model-dependent), high-quality hand-curated and cleaned data for chat performance
- **All models supported** — v2.0 works on MoE and non-MoE architectures (previous Dynamic only worked for MoE)
- **Model-specific quants** — each model uses a custom-tailored scheme (e.g., Gemma 3 layers differ significantly from Llama 4)
- **Additional formats** — Q4_NL, Q5.1, Q5.0, Q4.1, Q4.0 for Apple Silicon / ARM efficiency

All future GGUF uploads use Dynamic 2.0. Internal evaluation framework built to match official reported 5-shot MMLU scores for apples-to-apples comparisons vs full-precision, QAT, and standard imatrix GGUF quants.

## Why KL Divergence

[Accuracy is Not All You Need](https://arxiv.org/pdf/2407.09141) shows pruning/quantization can change incorrect answers to correct ("flips") without decreasing MMLU. KL Divergence correlates with flips, making it a better metric for measuring how close a quant stays to the original model.

> [!info] **KL Divergence** is one of the gold standards for reporting quantization errors per the paper. **Perplexity is incorrect** — output token values can cancel out. Use KLD or harder benchmarks like [[075-basics-unsloth-dynamic-2.0-ggufs-unsloth-dynamic-ggufs-on-aider-polyglot|Aider Polyglot]].

Goal: reduce mean KL Divergence while increasing disk space as little as possible.

## Calibration Dataset Overfitting

Most frameworks use Wikipedia test sets for perplexity/KLD, causing quants calibrated on similar data to overfit. Unsloth uses [Calibration_v3](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8) and [Calibration_v5](https://gist.github.com/tristandruyen/9e207a95c7d75ddf37525d353e00659c/) for fair testing.

> [!danger] Instruct models have unique chat templates — text-only calibration datasets are **not effective** for instruct models (base models yes). Most imatrix GGUFs are calibrated with these issues, inflating KLD scores on Wikipedia benchmarks.

For fair evaluation, Unsloth benchmarks KLD using the same standard Wikipedia datasets as baselines, not its own chat-optimized calibration dataset.

## MMLU Replication

Replicating MMLU 5-shot was problematic — could not replicate results for Llama 3.1 (8B) Instruct, Gemma 3 (12B), and others due to subtle implementation issues. Llama 3.1 (8B) should get ~68.2%; incorrect implementations yield as low as **35%**.

- Llama 3.1 (8B) Instruct: naive implementation gets 67.8%. Llama **tokenizes `"A"` and `" A"` (space-prefixed) as different token IDs**. Considering both: 68.2% (+0.4%)
- Llama 3 per Eleuther AI's [LLM Harness](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/lm_eval/tasks/llama3/instruct/mmlu/_continuation_template_yaml) appends **"The best answer is"** per original MMLU benchmarks
- Unsloth built custom MMLU implementation from scratch, investigating [github.com/hendrycks/test](https://github.com/hendrycks/test) directly, verified across multiple models vs reported numbers

## Gemma 3 QAT Replication and Benchmarks

Gemma team released two QAT versions:

1. **Q4_0 GGUF** — quantizes all layers via `w = q * block_scale` (32 weights per block), see [llama.cpp wiki](https://github.com/ggml-org/llama.cpp/wiki/Tensor-Encoding-Schemes)
2. **int4 version** — presumably [TorchAO int4 style](https://github.com/pytorch/ao/blob/main/torchao/quantization/README.md)

**12B Q4_0 QAT gets 67.07%** vs full bfloat16 12B at 67.15% on 5-shot MMLU.

| Metric | 1B | 4B | 12B | 27B |
| --- | --- | --- | --- | --- |
| MMLU 5 shot | 26.12% | 55.13% | **67.07% (67.15% BF16)** | **70.64% (71.5% BF16)** |
| Disk Space | 0.93GB | 2.94GB | **7.52GB** | 16.05GB |
| **Efficiency*** | 1.20 | 10.26 | **5.59** | 2.84 |

**Efficiency metric:**

```
Efficiency = (MMLU 5 shot score - 25) / Disk Space GB
```

> [!warning] 25 is subtracted because MMLU has 4 choices (A/B/C/D); random guessing = 25% accuracy, which would yield misleading efficiency for trivially small models.

### KL Divergence vs Base Model (Gemma 3)

Closer to 0 = better (identical to full precision).

| Quant | Baseline KLD | GB | New KLD | GB |
| --- | --- | --- | --- | --- |
| IQ1_S | 1.035688 | 5.83 | 0.972932 | 6.06 |
| IQ1_M | 0.832252 | 6.33 | 0.800049 | 6.51 |
| IQ2_XXS | 0.535764 | 7.16 | 0.521039 | 7.31 |
| IQ2_M | 0.26554 | 8.84 | 0.258192 | 8.96 |
| Q2_K_XL | 0.229671 | 9.78 | 0.220937 | 9.95 |
| Q3_K_XL | 0.087845 | 12.51 | 0.080617 | 12.76 |
| Q4_K_XL | 0.024916 | 15.41 | 0.023701 | 15.64 |

Dynamic 2-bit Q2_K_XL reduces KLD ~7.5% with small disk increase.

### Gemma 3 (27B) MMLU Benchmarks

Dynamic 4-bit is **2GB smaller with +1% extra accuracy vs QAT**. 2-bit Q2_K_XL leads on efficiency.

| Quant | Unsloth | Unsloth + QAT | Disk Size | Efficiency |
| --- | --- | --- | --- | --- |
| IQ1_M | 48.10 | 47.23 | 6.51 | 3.42 |
| IQ2_XXS | 59.20 | 56.57 | 7.31 | 4.32 |
| IQ2_M | 66.47 | 64.47 | 8.96 | 4.40 |
| Q2_K_XL | 68.70 | 67.77 | 9.95 | 4.30 |
| Q3_K_XL | 70.87 | 69.50 | 12.76 | 3.49 |
| **Q4_K_XL** | **71.47** | **71.07** | **15.64** | **2.94** |
| **Google QAT** | | **70.64** | **17.2** | **2.65** |

<details>

<summary>Full Gemma 3 (27B) QAT Benchmarks</summary>

| Model | Unsloth | Unsloth + QAT | Disk Size | Efficiency |
| --- | --- | --- | --- | --- |
| IQ1_S | 41.87 | 43.37 | 6.06 | 3.03 |
| IQ1_M | 48.10 | 47.23 | 6.51 | 3.42 |
| IQ2_XXS | 59.20 | 56.57 | 7.31 | 4.32 |
| IQ2_M | 66.47 | 64.47 | 8.96 | 4.40 |
| Q2_K | 68.50 | 67.60 | 9.78 | 4.35 |
| Q2_K_XL | 68.70 | 67.77 | 9.95 | 4.30 |
| IQ3_XXS | 68.27 | 67.07 | 10.07 | 4.18 |
| Q3_K_M | 70.70 | 69.77 | 12.51 | 3.58 |
| Q3_K_XL | 70.87 | 69.50 | 12.76 | 3.49 |
| Q4_K_M | 71.23 | 71.00 | 15.41 | 2.98 |
| **Q4_K_XL** | **71.47** | **71.07** | **15.64** | **2.94** |
| Q5_K_M | 71.77 | 71.23 | 17.95 | 2.58 |
| Q6_K | 71.87 | 71.60 | 20.64 | 2.26 |
| Q8_0 | 71.60 | 71.53 | 26.74 | 1.74 |
| **Google QAT** | | **70.64** | **17.2** | **2.65** |

</details>

## Llama 4 Bug Fixes

Unsloth fixed several Llama 4 bugs:

- **RoPE Scaling** — Llama 4 Scout changed config in official repo; resolved in [llama.cpp](https://github.com/ggml-org/llama.cpp/pull/12889)
- **QK Norm epsilon** — Scout and Maverick should use 1e-05 from config, not 1e-06. Fixed in [llama.cpp](https://github.com/ggml-org/llama.cpp/pull/12889) and [transformers](https://github.com/huggingface/transformers/pull/37418)
- **QK Norm head sharing** — should not be shared across all heads. Independently fixed by Llama 4 team and [vLLM](https://github.com/vllm-project/vllm/pull/16311); MMLU Pro increased from 68.58% to 71.53%
- [Wolfram Ravenwolf](https://x.com/WolframRvnwlf/status/1909735579564331016) showed Unsloth GGUFs via llama.cpp attain much higher accuracy than third-party inference providers

### Running Llama 4 Scout

Clone and build llama.cpp:

```bash
apt-get update
apt-get install pciutils build-essential cmake curl libcurl4-openssl-dev -y
git clone https://github.com/ggml-org/llama.cpp
cmake llama.cpp -B llama.cpp/build \
    -DBUILD_SHARED_LIBS=OFF -DGGML_CUDA=ON -DLLAMA_CURL=ON
cmake --build llama.cpp/build --config Release -j --clean-first --target llama-cli llama-gguf-split
cp llama.cpp/build/bin/llama-* llama.cpp
```

Download Dynamic v2.0 quant:

```python
# !pip install huggingface_hub hf_transfer
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id = "unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF",
    local_dir = "unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF",
    allow_patterns = ["*IQ2_XXS*"],
)
```

Run inference:

```bash
./llama.cpp/llama-cli \
    --model unsloth/Llama-4-Scout-17B-16E-Instruct-GGUF/Llama-4-Scout-17B-16E-Instruct-UD-IQ2_XXS.gguf \
    --threads 32 \
    --ctx-size 16384 \
    --n-gpu-layers 99 \
    -ot ".ffn_.*_exps.=CPU" \
    --seed 3407 \
    --prio 3 \
    --temp 0.6 \
    --min-p 0.01 \
    --top-p 0.9 \
    -no-cnv \
    --prompt "<|header_start|>user<|header_end|>\n\nCreate a Flappy Bird game.<|eot|><|header_start|>assistant<|header_end|>\n\n"
```

> [!success] Read more on running Llama 4: <https://docs.unsloth.ai/basics/tutorial-how-to-run-and-fine-tune-llama-4>

#unsloth #gguf #quantization #dynamic-2.0 #llama #gemma #benchmarks
