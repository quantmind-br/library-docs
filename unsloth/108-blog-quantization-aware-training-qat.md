---
title: Quantization-Aware Training (QAT)
url: https://unsloth.ai/docs/blog/quantization-aware-training-qat.md
source: llms
fetched_at: 2026-04-27T18:15:21.614896601-03:00
rendered_js: false
word_count: 901
summary: This document details Quantization-Aware Training (QAT) within Unsloth, explaining how it improves model accuracy over standard Post-Training Quantization (PTQ). It covers techniques for training smarter quantization schemes and provides guidance on exporting these QAT models using TorchAO for various deployment targets.
tags:
    - quantization-aware
    - qat
    - pytorch-unsloth
    - model-training
    - low-bit
    - torchao
category: tutorial
optimized: true
optimized_at: 2026-04-27T21:15:00Z
---

# Quantization-Aware Training (QAT)

Trainable quantization in Unsloth (with PyTorch/TorchAO) recovers up to **70% of lost accuracy** vs naive 4-bit PTQ, achieving **1-3%** benchmark improvements (GPQA, MMLU Pro). No extra inference overhead -- same disk/memory as normal quantization.

[Qwen3 (4B) QAT notebook](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_\(4B\)_Instruct-QAT.ipynb)

## Quantization Background

**Post-training quantization (PTQ)** -- naive approach:
1. Find `max(abs(W))`
2. Compute `a = 127/max(abs(W))` (int8 max range)
3. Quantize: `qW = int8(round(W * a))`
4. Dequantize: `float16(qW) / a`

PTQ reduces storage/inference cost but degrades accuracy at 4-bit or lower. Alternatives: [[115-basics-unsloth-dynamic-2.0-ggufs|dynamic GGUF quants]] (calibration-based) or **trainable/learnable quantization (QAT)**.

## QAT Results

- Gemma3-4B on GPQA: recovers **66.9%** of lost accuracy, +1.0% raw improvement
- Gemma3-12B on BBH: recovers **45.5%**, +2.1% raw improvement

## How QAT Works

QAT "fake quantizes" weights (and optionally activations) during training -- rounding to quantized values while staying in high-precision dtype (e.g. bfloat16), then immediately dequantizing. TorchAO:

1. Inserts fake quantize operations into linear layers (enables training a more accurate quantization representation)
2. Transforms fake quantize to actual quantize/dequantize after training for inference

## QAT + LoRA Fine-tuning

Combine both: reduce storage/compute during training while mitigating quantization degradation. Supported `qat_scheme` values: `fp8-int4`, `fp8-fp8`, `int8-int4`, `int4`.

```python
from unsloth import FastLanguageModel
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Qwen3-4B-Instruct-2507",
    max_seq_length = 2048,
    load_in_16bit = True,
)
model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 32,

    # We support fp8-int4, fp8-fp8, int8-int4, int4
    qat_scheme = "int4",
)
```

## Exporting QAT Models

### Prepare for conversion

```python
from torchao.quantization import quantize_
from torchao.quantization.qat import QATConfig
quantize_(model, QATConfig(step = "convert"))
```

### Save with TorchAO

```python
# Use the exact same config as QAT (convenient function)
model.save_pretrained_torchao(
    model, "tokenizer",
    torchao_config = model._torchao_config.base_config,
)

# Int4 QAT
from torchao.quantization import Int4WeightOnlyConfig
model.save_pretrained_torchao(
    model, "tokenizer",
    torchao_config = Int4WeightOnlyConfig(),
)

# Int8 QAT
from torchao.quantization import Int8DynamicActivationInt8WeightConfig
model.save_pretrained_torchao(
    model, "tokenizer",
    torchao_config = Int8DynamicActivationInt8WeightConfig(),
)
```

Deploy in vLLM, Unsloth, or other inference systems.

## Quantizing Without Training (PTQ)

```python
# Float8 example
from torchao.quantization import PerRow
from torchao.quantization import Float8DynamicActivationFloat8WeightConfig
torchao_config = Float8DynamicActivationFloat8WeightConfig(granularity = PerRow())
model.save_pretrained_torchao(torchao_config = torchao_config)
```

## ExecuTorch -- Mobile Deployment

Fine-tune in Unsloth, export to [ExecuTorch](https://github.com/pytorch/executorch) for on-device inference. Example: [Qwen3-4B-int8-int4-unsloth on HuggingFace](https://huggingface.co/metascroy/Qwen3-4B-int8-int4-unsloth). More workflows coming soon.

## Installation

```bash
pip install --upgrade --no-cache-dir --force-reinstall unsloth unsloth_zoo
pip install torchao==0.14.0 fbgemm-gpu-genai==1.3.0
```

## Acknowledgements

PyTorch/TorchAO team: Andrew Or, Jerry Zhang, Supriya Rao, Scott Roy, Mergen Nachin. Also the ExecuTorch team.

#quantization #qat #torchao #unsloth #low-bit
