---
title: GLM-OCR - SGLang Documentation
url: https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-OCR
source: sitemap
fetched_at: 2026-05-11T05:50:35.894420132-03:00
rendered_js: false
word_count: 512
summary: This document provides an overview, deployment instructions, and usage guidance for the GLM-OCR multimodal model, optimized for document understanding and table extraction using SGLang.
tags:
    - glm-ocr
    - ocr
    - multimodal-model
    - sglang
    - document-understanding
    - speculative-decoding
    - model-deployment
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

## 1. Model Introduction

[GLM-OCR](https://huggingface.co/zai-org/GLM-OCR) is a multimodal OCR model for complex document understanding, built on the GLM-V encoder–decoder architecture. It introduces Multi-Token Prediction (MTP) loss and stable full-task reinforcement learning to improve training efficiency, recognition accuracy, and generalization. The model integrates the CogViT visual encoder pre-trained on large-scale image–text data, a lightweight cross-modal connector with efficient token downsampling, and a GLM-0.5B language decoder. Combined with a two-stage pipeline of layout analysis and parallel recognition based on PP-DocLayout-V3, GLM-OCR delivers robust and high-quality OCR performance across diverse document layouts. **Hardware Support:** NVIDIA B200/H100/H200 **Key Features:**

- **State-of-the-Art Performance**: Achieves 94.62 on OmniDocBench V1.5, ranking #1, and delivers SOTA results across major document understanding benchmarks, including formula recognition, table recognition, and information extraction.
- **Optimized for Real-World Scenarios**: Specifically optimized for practical business cases, maintaining stable and accurate performance on complex tables, code documents, seals, and other challenging layouts.
- **Efficient Inference**: With only 0.9B parameters, GLM-OCR supports deployment via vLLM and SGLang, significantly reducing inference latency and compute cost—well suited for high-concurrency and edge deployments.
- **Easy to Use**: Fully open-sourced with a complete SDK and inference toolchain, enabling one-line invocation and seamless integration into existing systems.

For more details, please refer to the [official GLM-OCR model card](https://huggingface.co/zai-org/GLM-OCR).

## 2. SGLang Installation

SGLang offers multiple installation methods. You can choose the most suitable installation method based on your hardware platform and requirements. Please refer to the [official SGLang installation guide](https://docs.sglang.io/docs/get-started/install) for installation instructions.

## 3. Model Deployment

This section provides deployment configurations optimized for different hardware platforms and use cases.

### 3.1 Basic Configuration

**Interactive Command Generator**: Use the configuration selector below to automatically generate the appropriate deployment command for your hardware platform and deployment options. You can optionally enable MTP (Multi-Token Prediction) for faster inference using EAGLE speculative decoding.

Hardware Platform

H100H200B200

Deployment Strategy

MTPMulti-token Prediction

Run this Command:

```
SGLANG_USE_CUDA_IPC_TRANSPORT=1 python -m sglang.launch_server \
  --model zai-org/GLM-OCR \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 4
```

### 3.2 Configuration Tips

- **CUDA IPC Transport**: The `SGLANG_USE_CUDA_IPC_TRANSPORT=1` environment variable enables CUDA IPC for transferring multimodal features, which significantly improves TTFT.
- **MTP (Multi-Token Prediction)**: Enable MTP to use EAGLE speculative decoding for faster inference. This feature predicts multiple tokens at once to reduce latency.
- **Memory Management**: For memory-constrained environments, you may need to adjust `--mem-fraction-static` and/or `--max-running-requests`.

## 4. Model Invocation

### 4.1 Basic Usage

For basic API usage and request examples, please refer to:

- [SGLang Basic Usage Guide](https://docs.sglang.io/docs/basic_usage/send_request)
- [SGLang OpenAI Vision API Guide](https://docs.sglang.io/docs/basic_usage/openai_api_vision)

### 4.2 Advanced Usage

#### 4.2.1 OCR Image Processing

GLM-OCR supports OCR tasks on various document types. Here’s a basic example:

```
import time
from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:30000/v1",
    timeout=3600
)

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://ofasys-multimodal-wlcb-3-toshanghai.oss-accelerate.aliyuncs.com/wpf272043/keepme/image/receipt.png"
                }
            },
            {
                "type": "text",
                "text": "Please extract all text from this image."
            }
        ]
    }
]

start = time.time()
response = client.chat.completions.create(
    model="zai-org/GLM-OCR",
    messages=messages,
    max_tokens=2048
)
print(f"Response costs: {time.time() - start:.2f}s")
print(f"Generated text: {response.choices[0].message.content}")
```

**Example Output:**

```
Response costs: 2.29s
Generated text: CINNAMON SUGAR
1 x 17,000 17,000

SUB TOTAL 17,000

GRAND TOTAL 17,000

CASH IDR 20,000

CHANGE DUE 3,000

```

#### 4.2.2 Complex Document Processing

GLM-OCR excels at processing complex documents including:

- **Tables**: Accurate extraction of tabular data with structure preservation
- **Formulas**: Mathematical formula recognition
- **Code Documents**: Source code extraction from screenshots
- **Seals and Stamps**: Recognition of seals and stamps in documents
- **Multi-layout Documents**: Mixed content with text, images, and tables

```
import time
from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:30000/v1",
    timeout=3600
)

# Example: Processing a document with tables
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": "YOUR_DOCUMENT_IMAGE_URL"
                }
            },
            {
                "type": "text",
                "text": "Please extract the table content from this document and format it as markdown."
            }
        ]
    }
]

response = client.chat.completions.create(
    model="zai-org/GLM-OCR",
    messages=messages,
    max_tokens=4096
)
print(response.choices[0].message.content)
```

## 5. Benchmark

### 5.1 Accuracy Benchmark

Document model accuracy on standard benchmarks:

#### 5.1.1 OCRBench Benchmark

- Benchmark Command

```
python3 -m lmms_eval \
  --model openai_compatible \
  --model_args "model_version=zai-org/GLM-OCR" \
  --tasks ocrbench \
  --batch_size 128 \
  --log_samples \
  --log_samples_suffix "openai_compatible" \
  --output_path ./logs
```

- Test Result

TasksVersionFiltern-shotMetricValueStderrocrbenchYamlnone0ocrbench\_accuracy↑0.806N/A

#### 5.1.2 OmniDocBench V1.5

GLM-OCR achieves **94.62** on OmniDocBench V1.5, ranking #1 among all models, demonstrating state-of-the-art performance across major document understanding benchmarks.