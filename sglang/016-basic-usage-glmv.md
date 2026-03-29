---
title: 4.6V / GLM-4.5V Usage — SGLang
url: https://docs.sglang.io/basic_usage/glmv.html
source: crawler
fetched_at: 2026-02-04T08:47:38.545586975-03:00
rendered_js: false
word_count: 327
summary: This document provides instructions for deploying and optimizing GLM-4.6V and GLM-4.5V multimodal models using the SGLang server, including launch configurations for different hardware and API request examples for images and video.
tags:
    - glm-4-6v
    - sglang
    - multimodal-models
    - model-deployment
    - gpu-optimization
    - fp8-quantization
    - video-inference
category: guide
---

## Contents

## GLM-4.6V / GLM-4.5V Usage[#](#glm-4-6v-glm-4-5v-usage "Link to this heading")

## Launch commands for SGLang[#](#launch-commands-for-sglang "Link to this heading")

Below are suggested launch commands tailored for different hardware / precision modes

### FP8 (quantised) mode[#](#fp8-quantised-mode "Link to this heading")

For high memory-efficiency and latency optimized deployments (e.g., on H100, H200) where FP8 checkpoint is supported:

```
python3-msglang.launch_server\
--model-pathzai-org/GLM-4.6V-FP8\
--tp2\
--ep2\
--host0.0.0.0\
--port30000\
--keep-mm-feature-on-device
```

### Non-FP8 (BF16 / full precision) mode[#](#non-fp8-bf16-full-precision-mode "Link to this heading")

For deployments on A100/H100 where BF16 is used (or FP8 snapshot not used):

```
python3-msglang.launch_server\
--model-pathzai-org/GLM-4.6V\
--tp4\
--ep4\
--host0.0.0.0\
--port30000
```

## Hardware-specific notes / recommendations[#](#hardware-specific-notes-recommendations "Link to this heading")

- On H100 with FP8: Use the FP8 checkpoint for best memory efficiency.
- On A100 / H100 with BF16 (non-FP8): It’s recommended to use `--mm-max-concurrent-calls` to control parallel throughput and GPU memory usage during image/video inference.
- On H200 & B200: The model can be run “out of the box”, supporting full context length plus concurrent image + video processing.

## Sending Image/Video Requests[#](#sending-image-video-requests "Link to this heading")

### Image input:[#](#image-input "Link to this heading")

```
importrequests

url = f"http://localhost:30000/v1/chat/completions"

data = {
    "model": "zai-org/GLM-4.6V",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://github.com/sgl-project/sglang/blob/main/examples/assets/example_image.png?raw=true"
                    },
                },
            ],
        }
    ],
    "max_tokens": 300,
}

response = requests.post(url, json=data)
print(response.text)
```

### Video Input:[#](#video-input "Link to this heading")

```
importrequests

url = f"http://localhost:30000/v1/chat/completions"

data = {
    "model": "zai-org/GLM-4.6V",
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s happening in this video?"},
                {
                    "type": "video_url",
                    "video_url": {
                        "url": "https://github.com/sgl-project/sgl-test-files/raw/refs/heads/main/videos/jobs_presenting_ipod.mp4"
                    },
                },
            ],
        }
    ],
    "max_tokens": 300,
}

response = requests.post(url, json=data)
print(response.text)
```

## Important Server Parameters and Flags[#](#important-server-parameters-and-flags "Link to this heading")

When launching the model server for **multimodal support**, you can use the following command-line arguments to fine-tune performance and behavior:

- `--mm-attention-backend`: Specify multimodal attention backend. Eg. `fa3`(Flash Attention 3)
- `--mm-max-concurrent-calls <value>`: Specifies the **maximum number of concurrent asynchronous multimodal data processing calls** allowed on the server. Use this to control parallel throughput and GPU memory usage during image/video inference.
- `--mm-per-request-timeout <seconds>`: Defines the **timeout duration (in seconds)** for each multimodal request. If a request exceeds this time limit (e.g., for very large video inputs), it will be automatically terminated.
- `--keep-mm-feature-on-device`: Instructs the server to **retain multimodal feature tensors on the GPU** after processing. This avoids device-to-host (D2H) memory copies and improves performance for repeated or high-frequency inference workloads.
- `--mm-enable-dp-encoder`: Placing the ViT in data parallel while keeping the LLM in tensor parallel consistently lowers TTFT and boosts end-to-end throughput.
- `SGLANG_USE_CUDA_IPC_TRANSPORT=1`: Shared memory pool based CUDA IPC for multi-modal data transport. For significantly improving e2e latency.

### Example usage with the above optimizations:[#](#example-usage-with-the-above-optimizations "Link to this heading")

```
SGLANG_USE_CUDA_IPC_TRANSPORT=1\
SGLANG_VLM_CACHE_SIZE_MB=0\
python-msglang.launch_server\
--model-pathzai-org/GLM-4.6V\
--host0.0.0.0\
--port30000\
--trust-remote-code\
--tp-size8\
--enable-cache-report\
--log-levelinfo\
--max-running-requests64\
--mem-fraction-static0.65\
--chunked-prefill-size8192\
--attention-backendfa3\
--mm-attention-backendfa3\
--mm-enable-dp-encoder\
--enable-metrics
```

### Thinking Budget for GLM-4.5V / GLM-4.6V[#](#thinking-budget-for-glm-4-5v-glm-4-6v "Link to this heading")

In SGLang, we can implement thinking budget with `CustomLogitProcessor`.

Launch a server with `--enable-custom-logit-processor` flag on. and using `Glm4MoeThinkingBudgetLogitProcessor` in the request likes `GLM-4.6` example in [glm45.md](https://docs.sglang.io/basic_usage/glm45.html).