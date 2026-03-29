---
title: DP for Multi-Modal Encoder in SGLang — SGLang
url: https://docs.sglang.io/advanced_features/dp_for_multi_modal_encoder.html
source: crawler
fetched_at: 2026-02-04T08:46:55.995531426-03:00
rendered_js: false
word_count: 201
summary: This document explains the rationale and benefits of using data parallelism for multi-modal encoders in SGLang and provides instructions for enabling this feature.
tags:
    - sglang
    - data-parallelism
    - multi-modal-encoder
    - vlm
    - vision-transformer
    - performance-optimization
category: configuration
---

## DP for Multi-Modal Encoder in SGLang[#](#dp-for-multi-modal-encoder-in-sglang "Link to this heading")

A typical VLM architecture involves two main components: an multi-modal encoder and a text decoder.

Most VLMs utilize a Vision Transformer (ViT) as their multi-modal encoder, it is responsible for processing visual data, extracting features (objects, colors, textures, etc.), and transforming them into a format that can be understood by the model.

The text deocoder is based on LLM. It processes textual data and generates output based on the encoded visual features.

However, since the size of ViT is very small compared to language decoders, there is relatively little gain from TP. On the other hand, TP incurs significant communication overhead because of all-reduce being performed after every layer.

Placing the ViT in data parallel while keeping the LLM in tensor parallel consistently lowers TTFT and boosts end-to-end throughput. In this hybrid layout, the vision front-end becomes parallel and lightweight, while scarce interconnect bandwidth and collective ops are reserved for the LLM.

Data parallelism replicates the entire model across multiple GPU sets and processes different batches of requests in parallel.

## Command Example[#](#command-example "Link to this heading")

You can enable batch-level DP by setting `mm-enable-dp-encoder`, for example:

```
python3 -m sglang.launch_server \
    --model-path Qwen/Qwen2.5-VL-7B-Instruct \
    --tp 2 \
    --mm-enable-dp-encoder
```

## Known supported models[#](#known-supported-models "Link to this heading")

- Qwen2.5-VL ([sgl-project/sglang#13126](https://github.com/sgl-project/sglang/pull/13126))
- Qwen3-VL ([sgl-project/sglang#13724](https://github.com/sgl-project/sglang/pull/13724))
- InternVL ([sgl-project/sglang#13925](https://github.com/sgl-project/sglang/pull/13925))
- GLM-4.5V & GLM-4.6V ([sgl-project/sglang#14097](https://github.com/sgl-project/sglang/pull/14097))