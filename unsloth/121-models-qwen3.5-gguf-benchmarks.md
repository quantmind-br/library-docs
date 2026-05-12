---
title: Qwen3.5 GGUF Benchmarks
url: https://unsloth.ai/docs/models/qwen3.5/gguf-benchmarks.md
source: llms
fetched_at: 2026-04-27T18:13:36.908173441-03:00
rendered_js: false
word_count: 1533
summary: This document details the benchmarks, improvements, and technical findings regarding Qwen3.5 models quantized into GGUF format by Unsloth. It covers updates like better quantization algorithms using 'imatrix' data and analyzes how different tensor types respond to various bit-width quantizations.
tags:
    - qwen3-5
    - gguf-benchmarks
    - quantization-analysis
    - unsloth-dynamic
    - imatrix
    - model-performance
category: reference
optimized: true
optimized_at: 2026-04-27T21:30:00Z
---

# Qwen3.5 GGUF Benchmarks

Unsloth Dynamic quants: SOTA on nearly all bits. 150+ KL Divergence benchmarks, 9TB of GGUFs. Fixed tool-calling chat template issue (affects all quant uploaders/types).

> [!tip] **Mar 5 2026 Update**: Redownload Qwen3.5-**35B**, **27B**, **122B**, **397B**. Improved quantization algorithm + new imatrix data. Better chat, coding, long context, tool-calling. New benchmarks for Qwen3.5-122B-A10B and 35-A3B.

Inference guide: [[021-models-qwen3.5|Qwen3.5 - How to Run Locally]]

99.9% KL Divergence shows SOTA on Pareto Frontier for [[115-basics-unsloth-dynamic-2.0-ggufs|Unsloth Dynamic]] `Q4_K_XL`, `IQ3_XXS` etc.

## Key Findings

- Imatrix reduces KLD & PPL at 5-10% slower inference cost.
- Quantizing `ssm_out` (Mamba) and `ffn_down_exps` is not recommended.
- **Retiring MXFP4** from all GGUF quants: Q2_K_XL, Q3_K_XL, Q4_K_XL (except pure MXFP4_MOE).

| [Qwen3.5-35B-A3B](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-GGUF) | [Qwen3.5-27B](https://huggingface.co/unsloth/Qwen3.5-27B-GGUF) | [Qwen3.5-122B-A10B](https://huggingface.co/unsloth/Qwen3.5-122B-A10B-GGUF) | [Qwen3.5-397B-A17B](https://huggingface.co/unsloth/Qwen3.5-397B-A17B-GGUF) |
| --- | --- | --- | --- |

## 1) Tensor sensitivity to quantization

9TB of research artifacts available at [Experiments page](https://huggingface.co/unsloth/Qwen3.5-35B-A3B-Experiments-GGUF) (KLD metrics, 121 configs).

- **Best to quantize**: `ffn_up_exps`, `ffn_gate_exps` — OK at 3bit. `ffn_down_exps` slightly more sensitive.
- **Worst to quantize**: `ssm_out` dramatically increases KLD with minuscule disk savings. **Quantizing `attn_*` is especially sensitive** for hybrid architectures — keep in higher precision.
- **3bit is the sweet spot** for `ffn_*` layers (iq3_xxs). 2 bits cause more degradation.

**MXFP4 is worse than Q4_K** on many tensors (`attn_gate`, `attn_q`, `ssm_beta`, `ssm_alpha`). Q4_K uses 4.5 bits/weight vs MXFP4's 4.25 — Q4_K is the better choice.

## 2) Imatrix effectiveness

Imatrix weights quantization correctly. Reduces 99.9% KLD significantly, especially at lower bits. Works across all quants/bit widths.

**Tradeoff**: I-quants (iq3_xxs, iq2_s etc) are 5-10% slower but more efficient.

| Type | pp512 (~) | tg128 (~) |
| --- | --- | --- |
| mxfp4 | 1978.69 | 90.67 |
| q4_k | 1976.44 | 90.38 |
| q3_k | 1972.61 | 91.36 |
| q6_k | 1964.55 | 90.50 |
| q2_k | 1964.20 | 90.77 |
| q8_0 | 1964.17 | 90.33 |
| q5_k | 1947.74 | 90.72 |
| iq3_xxs | 2030.94 | 85.68 |
| iq2_xxs | 1997.64 | 85.79 |
| iq3_s | 1990.12 | 84.37 |
| iq2_xs | 1967.85 | 85.19 |
| iq2_s | 1952.50 | 85.04 |

## 3) Perplexity & KLD can be misleading

Highly influenced by calibration. Most GGUFs evaluated on Wiki-test with 512 context windows — results shift if imatrix calibration includes Wikipedia-like data. Unsloth GGUFs may show higher perplexity because imatrix uses long-context chat and tool-calling examples instead.

[Benjamin Marie's MiniMax-M2.5 analysis](https://x.com/bnjmn_marie/status/2027043753484021810): Unsloth Dynamic IQ2_XXS outperforms AesSedai IQ3_S on real-world evals (LiveCodeBench v6, MMLU Pro) despite being 11GB smaller. Yet AesSedai's PPL/KLD suggest opposite (PPL: 0.3552 vs 0.2441; KLD: 9.0338 vs 8.2849 — lower is better).

Lower PPL/KLD does not necessarily mean better real-world performance. Going forward, Unsloth publishes both as community reference.

## 4) March 5 2026 Update — reduced Maximum KLD

Enhanced quantization for Qwen3.5 MoEs to reduce Maximum KLD directly (useful for massive outliers where 99.9% percentile may not capture).

| Quant | Old GB | New GB | Old Max KLD | New Max KLD |
| --- | --- | --- | --- | --- |
| UD-Q2_K_XL | 12.0 | ***11.3*** | 8.237 | ***8.155*** |
| UD-Q3_K_XL | 16.1 | ***15.5*** | 5.505 | ***5.146*** |
| UD-Q4_K_XL | ***19.2*** | 20.7 (+7.8%) | 5.894 | ***2.877 (-51%)*** |
| UD-Q5_K_XL | ***23.2*** | 24.6 (+6%) | 5.536 | ***3.210 (-42%)*** |

## Full Benchmarks

| Quantizer | Quant Level | Disk (GB) | PPL | KLD 99.9% | Mean KLD |
| --- | --- | --- | --- | --- | --- |
| AesSedai | IQ3_S | 12.65 | 6.9152 | 1.8669 | 0.0613 |
| AesSedai | IQ4_XS | 16.4 | 6.6447 | 0.8067 | 0.0235 |
| AesSedai | Q4_K_M | 20.62 | 6.5665 | 0.3171 | 0.0096 |
| AesSedai | Q5_K_M | 24.45 | 6.5356 | 0.21 | 0.0058 |
| Ubergarm | Q4_0 | 19.79 | 6.5784 | 0.4829 | 0.0142 |
| Unsloth | IQ2_XXS | 9.09 | 7.716 | 4.2221 | 0.1846 |
| Unsloth | Q2_K_XL | 12.04 | 7.0438 | 2.9092 | 0.097 |
| Unsloth | IQ3_XXS | 13.12 | 6.7829 | 1.5296 | 0.0501 |
| Unsloth | IQ3_S | 14.13 | 6.7715 | 1.4193 | 0.0457 |
| Unsloth | Q3_K_M | 15.54 | 6.732 | 0.9726 | 0.0324 |
| Unsloth | Q3_K_XL | 16.06 | 6.7245 | 0.9539 | 0.0308 |
| Unsloth | MXFP4_MOE | 18.17 | 6.6 | 0.7789 | 0.0272 |
| Unsloth | Q4_K_M | 18.49 | 6.6053 | 0.5478 | 0.0192 |
| Unsloth | Q4_K_L | 18.82 | 6.5905 | 0.4828 | 0.015 |
| Unsloth | Q4_K_XL | 19.17 | 6.5918 | 0.4097 | 0.0137 |
| Unsloth | Q5_K_XL | 23.22 | 6.5489 | 0.236 | 0.0069 |
| Unsloth | Q6_K_S | 26.56 | 6.5456 | 0.2226 | 0.0065 |
| Unsloth | Q6_K_XL | 28.22 | 6.5392 | 0.1437 | 0.0041 |
| Unsloth | Q8_K_XL | 36.04 | 6.5352 | 0.1033 | 0.0026 |
| bartowski | Qwen_IQ2_XXS | 8.15 | 9.3427 | 6.0607 | 0.3457 |
| bartowski | Qwen_Q2_K_L | 11.98 | 7.5504 | 3.8095 | 0.1559 |
| bartowski | Qwen_IQ3_XXS | 12.94 | 7.0938 | 2.1563 | 0.0851 |
| bartowski | Qwen_Q3_K_M | 14.95 | 6.772 | 1.7779 | 0.0585 |
| bartowski | Qwen_Q3_K_XL | 15.97 | 6.8245 | 1.7516 | 0.0627 |
| bartowski | Qwen_IQ4_XS | 17.42 | 6.6234 | 0.7265 | 0.0234 |
| bartowski | Qwen_Q4_K_M | 19.77[^1] | 6.6097 | 0.5771 | 0.0182 |
| bartowski | Qwen_Q5_K_M | 23.11 | 6.5828 | 0.3549 | 0.0106 |
| noctrex | MXFP4_MOE_BF16 | 20.55 | 6.5948 | 0.7939 | 0.0248 |
| noctrex | MXFP4_MOE_F16 | 20.55 | 6.5937 | 0.7614 | 0.0247 |

[^1]: Bartowski's Q4_K_M is 1GB bigger than Unsloth's

#qwen3.5 #gguf #quantization #benchmarks #imatrix #unsloth-dynamic
