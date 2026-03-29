---
title: Multimodal Language Models — SGLang
url: https://docs.sglang.io/supported_models/multimodal_language_models.html
source: crawler
fetched_at: 2026-02-04T08:47:00.641895168-03:00
rendered_js: false
word_count: 283
summary: This document explains how to deploy and configure multimodal language models in SGLang, covering server setup, video input integration, and performance optimization flags.
tags:
    - multimodal-models
    - sglang
    - vlm
    - video-inference
    - inference-optimization
    - server-configuration
category: guide
---

## Contents

## Multimodal Language Models[#](#multimodal-language-models "Link to this heading")

These models accept multi-modal inputs (e.g., images and text) and generate text output. They augment language models with multimodal encoders.

## Example launch Command[#](#example-launch-command "Link to this heading")

```
python3-msglang.launch_server\
--model-pathmeta-llama/Llama-3.2-11B-Vision-Instruct\ # example HF/local path
--host0.0.0.0\
--port30000\
```

## Supported models[#](#supported-models "Link to this heading")

Below the supported models are summarized in a table.

If you are unsure if a specific architecture is implemented, you can search for it via GitHub. For example, to search for `Qwen2_5_VLForConditionalGeneration`, use the expression:

```
repo:sgl-project/sglang path:/^python\/sglang\/srt\/models\// Qwen2_5_VLForConditionalGeneration
```

in the GitHub search bar.

## Video Input Support[#](#video-input-support "Link to this heading")

SGLang supports video input for Vision-Language Models (VLMs), enabling temporal reasoning tasks such as video question answering, captioning, and holistic scene understanding. Video clips are decoded, key frames are sampled, and the resulting tensors are batched together with the text prompt, allowing multimodal inference to integrate visual and linguistic context.

Use `sgl.video(path, num_frames)` when building prompts to attach clips from your SGLang programs.

Example OpenAI-compatible request that sends a video clip:

```
importrequests

url = "http://localhost:30000/v1/chat/completions"

data = {
    "model": "Qwen/Qwen3-VL-30B-A3B-Instruct",
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

## Usage Notes[#](#usage-notes "Link to this heading")

### Performance Optimization[#](#performance-optimization "Link to this heading")

For multimodal models, you can use the `--keep-mm-feature-on-device` flag to optimize for latency at the cost of increased GPU memory usage:

- **Default behavior**: Multimodal feature tensors are moved to CPU after processing to save GPU memory
- **With `--keep-mm-feature-on-device`** : Feature tensors remain on GPU, reducing device-to-host copy overhead and improving latency, but consuming more GPU memory

Use this flag when you have sufficient GPU memory and want to minimize latency for multimodal inference.

### Multimodal Inputs Limitation[#](#multimodal-inputs-limitation "Link to this heading")

- **Use `--mm-process-config '{"image":{"max_pixels":1048576},"video":{"fps":3,"max_pixels":602112,"max_frames":60}}'`** : To set `image`, `video`, and `audio` input limits.

This can reduce GPU memory usage, improve inference speed, and help to avoid OOM, but may impact model performance, thus set a proper value based on your specific use case. Currently, only `qwen_vl` supports this config. Please refer to [qwen\_vl processor](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/multimodal/processors/qwen_vl.py) for understanding the meaning of each parameter.