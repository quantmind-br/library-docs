---
title: EPD Disaggregation — SGLang
url: https://docs.sglang.io/advanced_features/epd_disaggregation.html
source: crawler
fetched_at: 2026-02-04T08:46:51.725649168-03:00
rendered_js: false
word_count: 230
summary: This document introduces Encoder-Prefill-Decode (EPD) disaggregation in SGLang and explains how to configure standalone servers for each stage of Vision-Language Model inference.
tags:
    - sglang
    - vlm-inference
    - epd-disaggregation
    - vision-language-models
    - model-serving
    - distributed-inference
category: guide
---

## Contents

## EPD Disaggregation[#](#epd-disaggregation "Link to this heading")

## Why and What is EPD Disaggregation?[#](#why-and-what-is-epd-disaggregation "Link to this heading")

In modern Vision-Language Model (VLM) inference, request execution naturally decomposes into three distinct stages: Encoder, Prefill, and Decode. The Encoder stage performs vision preprocessing and ViT-based image encoding, which is highly compute-intensive but only required during request initialization. The Prefill stage processes the full multimodal input sequence to initialize the language model’s Key-Value (KV) cache, while the Decode stage is dominated by memory bandwidth and KV cache access for autoregressive token generation.

Existing deployments typically colocate these stages within a unified execution engine, or at best apply Prefill–Decode (PD) disaggregation. However, such designs still tightly couple vision encoding with language prefill, leading to inefficient resource utilization, limited scalability for image-heavy workloads, and suboptimal scheduling under load.

To address these challenges, we introduce Encoder–Prefill–Decode (EPD) Disaggregation in SGLang. EPD further separates vision encoding from language processing, enabling independent horizontal scaling of encoder servers, improved load balancing for multimodal requests, and seamless integration with existing PD disaggregation to form a fully decoupled three-tier inference architecture.

### Usage[#](#usage "Link to this heading")

You can launch a language-only model using `--language-only`, or an encoder-only model using `--encoder-only`. When launching a language-only model, you must additionally specify the encoder service endpoints via `--encoder-urls`.

We support multiple encoder transfer backends, including zmq\_to\_scheduler, zmq\_to\_tokenizer, and mooncake (the default is zmq\_to\_scheduler). The backend can be selected using `--encoder-transfer-backend`.

#### Qwen VL[#](#qwen-vl "Link to this heading")

- EP Disaggregation

```
# encoder 0
python-msglang.launch_server\
--model-pathQwen/Qwen3-VL-8B-Instruct\
--encoder-only\
--encoder-transfer-backendzmq_to_scheduler\
--port30000
# encoder 1
python-msglang.launch_server\
--model-pathQwen/Qwen3-VL-8B-Instruct\
--encoder-only\
--encoder-transfer-backendzmq_to_scheduler\
--port30001
# language-only server
python-msglang.launch_server\
--model-pathQwen/Qwen3-VL-8B-Instruct\
--language-only\
--encoder-urlshttp://127.0.0.1:30000http://127.0.0.1:30001\
--encoder-transfer-backendzmq_to_scheduler\
--port30002
```

- EPD Disaggregation

```
# encoder 0
python-msglang.launch_server\
--model-pathQwen/Qwen3-VL-8B-Instruct\
--encoder-only\
--encoder-transfer-backendzmq_to_scheduler\
--port30000
# encoder 1
python-msglang.launch_server\
--model-pathQwen/Qwen3-VL-8B-Instruct\
--encoder-only\
--encoder-transfer-backendzmq_to_scheduler\
--port30001
# prefill 0
python-msglang.launch_server\
--model-pathQwen/Qwen3-VL-8B-Instruct\
--disaggregation-modeprefill\
--language-only\
--encoder-urlshttp://127.0.0.1:30000http://127.0.0.1:30001\
--encoder-transfer-backendzmq_to_scheduler\
--port30002
# decode 0
python-msglang.launch_server\
--model-pathQwen/Qwen3-VL-8B-Instruct\
--disaggregation-modedecode\
--port30003
# router
python-msglang_router.launch_router\
--pd-disaggregation\
--prefillhttp://$PREFILL_HOST:30002\
--decodehttp://$DECODE_HOST:30003\
--port8000
```