---
title: LTX2 & LTX2.3 - SGLang Documentation
url: https://docs.sglang.io/cookbook/diffusion/LTX/LTX2 & LTX2.3
source: sitemap
fetched_at: 2026-05-11T05:49:57.271731428-03:00
rendered_js: false
word_count: 748
summary: This document provides instructions for deploying and invoking Lightricks LTX video generation models using SGLang, covering pipeline configuration, hardware-specific optimization, and inference patterns.
tags:
    - sglang
    - ltx-2
    - video-generation
    - model-deployment
    - diffusion
    - multi-gpu
    - inference
category: configuration
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## 1. Model Introduction

[LTX-2](https://huggingface.co/Lightricks/LTX-2) and [LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3) are video generation models from Lightricks. SGLang Diffusion supports the LTX series through native one-stage and two-stage pipelines for text-to-video and image-conditioned video generation. Use `Lightricks/LTX-2` or `Lightricks/LTX-2.3` as `--model-path`. For two-stage generation, SGLang uses the spatial upsampler and distilled LoRA components from the model snapshot by default. LTX-2.3 also supports the HQ two-stage variant.

## 2. SGLang-diffusion Installation

Install SGLang with diffusion dependencies:

```
uv pip install "sglang[diffusion]" --prerelease=allow
```

For platform-specific setup, see the [SGLang Diffusion installation guide](https://docs.sglang.io/docs/sglang-diffusion/installation).

## 3. Model Deployment

This section provides deployment configurations optimized for different LTX pipelines and hardware targets.

### 3.1 Basic Configuration

The LTX series supports one-stage and two-stage pipelines. LTX-2.3 also supports the HQ two-stage pipeline. The recommended launch configuration depends on whether the target GPU can keep both two-stage DiTs resident. **Interactive Command Generator**: Use the configuration selector below to generate a deployment command. The default selection targets a single NVIDIA H200 with `resident` two-stage mode. For multi-GPU serving, start from the 2-GPU or 4-GPU presets and only change parallelism if you need more memory headroom.

Deployment Target

1x H200resident2 GPUsCFG parallel4 GPUsTP2 + CFGStandard CUDASnapshot modeOfficial MatchOriginal switching

Pipeline

Two StageTwo Stage HQHigh QualityOne Stage

Select LoRA Model

transitionvaliantcat/LTX-2.3-Transition-LORA

Run this Command:

```
sglang serve \
  --model-path Lightricks/LTX-2.3 \
  --pipeline-class-name LTX2TwoStagePipeline \
  --ltx2-two-stage-device-mode resident \
  --port 30000
```

### 3.2 Configuration Tips

Choose the pipeline class based on the quality and latency target:

Use casePipeline classNotesOne-stage generation`LTX2Pipeline`Fastest LTX native path. Supports T2V and TI2V.Two-stage generation`LTX2TwoStagePipeline`Uses a base stage and a refinement stage. Supported by LTX-2 and LTX-2.3.Two-stage High Quality (HQ) generation`LTX2TwoStageHQPipeline`LTX-2.3 HQ path; defaults to 1920x1088 unless you override `--width` and `--height`.

Feature compatibility:

Pipeline classT2VTI2V (`--image-path`)LoRA (`--lora-path`)Notes`LTX2Pipeline`YesYesYesOne-stage path. Cannot be combined with HQ because HQ is a separate two-stage pipeline class.`LTX2TwoStagePipeline`YesYesYesStandard two-stage path for LTX-2 and LTX-2.3.`LTX2TwoStageHQPipeline`YesYesYesHigh Quality two-stage path for LTX-2.3. Use this instead of `LTX2Pipeline`; it is not a one-stage mode flag.

For two-stage pipelines, `--ltx2-two-stage-device-mode` controls transformer residency:

ModeWhen to use it`snapshot`Recommended default. Balances latency and VRAM.`resident`Best latency on high-VRAM GPUs because both DiTs can stay resident.`original`Closest to the original two-stage switching semantics.

Other deployment flags:

- `--lora-path`: Preload a community LoRA adapter.
- `--lora-weight-name`: Select the exact safetensors file when the LoRA repository contains multiple weight files.

### 3.3 Fast multi-GPU presets

For latency-oriented LTX serving, prefer CFG parallel over sequence parallelism. CFG parallel splits guidance branches across GPUs, while SP/Ulysses is mainly a memory/long-sequence tool for LTX.

TargetRecommended server flagsNotesLTX-2.3, 1 high-VRAM GPU`--ltx2-two-stage-device-mode resident`Fastest two-stage setup when both DiTs fit.LTX-2.3, 1 standard GPU`--ltx2-two-stage-device-mode snapshot`Lower VRAM than `resident`; use this when H100-class memory is tight.LTX-2, 2 GPUs`--num-gpus 2 --enable-cfg-parallel`Fastest verified 2-GPU setup; keep `--dit-layerwise-offload` disabled unless memory is tight.LTX-2.3, 2 GPUs`--num-gpus 2 --enable-cfg-parallel --ltx2-two-stage-device-mode resident`Fastest common 2-GPU setup.LTX-2.3, 4 GPUs`--num-gpus 4 --tp-size 2 --enable-cfg-parallel --ltx2-two-stage-device-mode resident`Fastest common 4-GPU layout: TP2 inside each CFG branch.Official comparison`--ltx2-two-stage-device-mode original`Use this only when matching the original LTX-2.3 stage-switch semantics matters.

Use `--enable-cfg-parallel` for degree-2 CFG parallel. Use `--cfg-parallel-size` only when you explicitly need a different CFG branch count. If `resident` exceeds available VRAM, keep the same parallelism preset and switch only the device mode to `snapshot`. On high-VRAM GPUs, add `--text-encoder-cpu-offload false` if text encoding latency matters and you have enough memory.

#### 3.3.1 Two GPUs

```
sglang serve \
  --model-path Lightricks/LTX-2.3 \
  --pipeline-class-name LTX2TwoStagePipeline \
  --num-gpus 2 \
  --enable-cfg-parallel \
  --ltx2-two-stage-device-mode resident
```

#### 3.3.2 Four GPUs

```
sglang serve \
  --model-path Lightricks/LTX-2.3 \
  --pipeline-class-name LTX2TwoStagePipeline \
  --num-gpus 4 \
  --tp-size 2 \
  --enable-cfg-parallel \
  --ltx2-two-stage-device-mode resident
```

## 4. Model Invocation

### 4.1 Basic Usage

The examples below spell out the current SGLang sampling defaults for reproducibility:

Model pathDefault outputDefault framesDefault steps`Lightricks/LTX-2`768x51212140`Lightricks/LTX-2.3`768x51212130`Lightricks/LTX-2.3` with `LTX2TwoStageHQPipeline`1920x108812115

#### 4.1.1 LTX-2 one-stage text-to-video

```
sglang generate \
  --model-path Lightricks/LTX-2 \
  --pipeline-class-name LTX2Pipeline \
  --prompt "A quiet coastal town at sunrise, fishing boats moving slowly through golden mist, cinematic camera movement" \
  --save-output
```

#### 4.1.2 LTX-2.3 one-stage text-to-video

```
sglang generate \
  --model-path Lightricks/LTX-2.3 \
  --pipeline-class-name LTX2Pipeline \
  --prompt "A quiet coastal town at sunrise, fishing boats moving slowly through golden mist, cinematic camera movement" \
  --save-output
```

#### 4.1.3 LTX-2 two-stage text-to-video

```
sglang generate \
  --model-path Lightricks/LTX-2 \
  --pipeline-class-name LTX2TwoStagePipeline \
  --prompt "A handheld shot follows a red tram crossing a rainy city square at night, reflections on the pavement, cinematic lighting" \
  --save-output
```

#### 4.1.4 LTX-2.3 two-stage text-to-video

```
sglang generate \
  --model-path Lightricks/LTX-2.3 \
  --pipeline-class-name LTX2TwoStagePipeline \
  --prompt "A handheld shot follows a red tram crossing a rainy city square at night, reflections on the pavement, cinematic lighting" \
  --save-output
```

#### 4.1.5 LTX-2.3 HQ text-to-video

```
sglang generate \
  --model-path Lightricks/LTX-2.3 \
  --pipeline-class-name LTX2TwoStageHQPipeline \
  --prompt "A wide cinematic shot of alpine clouds rolling over a mountain ridge, soft morning light, slow aerial camera movement" \
  --save-output
```

#### 4.1.6 Image-to-video with one reference image

Pass one image to `--image-path` for image-conditioned generation:

```
sglang generate \
  --model-path Lightricks/LTX-2.3 \
  --pipeline-class-name LTX2TwoStagePipeline \
  --image-path ./inputs/start.png \
  --prompt "The camera slowly pushes forward as the subject turns toward warm window light, subtle natural motion, cinematic" \
  --save-output
```

#### 4.1.7 First-to-last-frame transition with two reference images

Pass two images to `--image-path` for transition-style TI2V. The first image is used as the starting condition and the second image is used as the ending condition.

```
sglang generate \
  --model-path Lightricks/LTX-2.3 \
  --pipeline-class-name LTX2TwoStagePipeline \
  --image-path ./inputs/start.png ./inputs/end.png \
  --prompt "A smooth cinematic transition from the first scene into the final scene, dynamic camera motion, motion blur, zhuanchang" \
  --save-output
```

### 4.2 Advanced Usage

Use `--lora-path` to load a LoRA adapter. If the Hugging Face repo contains multiple safetensors files, use `--lora-weight-name` to select the exact file. `--lora-scale` maps to the standard LoRA merge scale and defaults to `1.0`. The following example uses [`valiantcat/LTX-2.3-Transition-LORA`](https://huggingface.co/valiantcat/LTX-2.3-Transition-LORA):

```
sglang generate \
  --model-path Lightricks/LTX-2.3 \
  --pipeline-class-name LTX2TwoStagePipeline \
  --lora-path valiantcat/LTX-2.3-Transition-LORA \
  --lora-weight-name ltx2.3-transition.safetensors \
  --prompt "A low-angle tracking shot moves through a foggy forest road. The camera rises above the treetops and transitions into a clear view of a snowy mountain peak under bright sunlight, zhuanchang" \
  --save-output
```

You can combine the Transition LoRA with two reference images:

```
sglang generate \
  --model-path Lightricks/LTX-2.3 \
  --pipeline-class-name LTX2TwoStagePipeline \
  --image-path ./inputs/start.png ./inputs/end.png \
  --lora-path valiantcat/LTX-2.3-Transition-LORA \
  --lora-weight-name ltx2.3-transition.safetensors \
  --prompt "A fast cinematic transition from the first image to the second image, whip-pan motion, atmospheric lighting, zhuanchang" \
  --save-output
```

## 5. Practical Tips

- Use `--pipeline-class-name LTX2TwoStagePipeline` as the default LTX two-stage quality path.
- Use `--pipeline-class-name LTX2TwoStageHQPipeline` when you want the HQ path and have enough VRAM for larger outputs.
- Use `--ltx2-two-stage-device-mode resident` on high-VRAM GPUs if latency matters more than memory usage.
- Use `--ltx2-two-stage-device-mode original` when comparing against official two-stage behavior.
- Keep `--width` and `--height` aligned with the target model resolution; for LTX models, these are output video dimensions.