---
title: Embedding models - SGLang Documentation
url: https://docs.sglang.io/docs/supported-models/embedding_models
source: sitemap
fetched_at: 2026-05-11T05:51:22.038089168-03:00
rendered_js: false
word_count: 228
summary: This document outlines how to deploy and interact with embedding models using the SGLang framework, covering text, multimodal, and Matryoshka embedding configurations.
tags:
    - sglang
    - embeddings
    - model-serving
    - multimodal
    - matryoshka-embeddings
    - api-integration
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

SGLang provides robust support for embedding models by integrating efficient serving mechanisms with its flexible programming interface. This integration allows for streamlined handling of embedding tasks, facilitating faster and more accurate retrieval and semantic search operations. SGLang’s architecture enables better resource utilization and reduced latency in embedding model deployment.

## Quick Start

### Launch Server

```
python3 -m sglang.launch_server \
  --model-path Qwen/Qwen3-Embedding-4B \
  --is-embedding \
  --host 0.0.0.0 \
  --port 30000
```

### Client Request

```
import requests

url = "http://127.0.0.1:30000"

payload = {
    "model": "Qwen/Qwen3-Embedding-4B",
    "input": "What is the capital of France?",
    "encoding_format": "float"
}

response = requests.post(url + "/v1/embeddings", json=payload).json()
print("Embedding:", response["data"][0]["embedding"])
```

## Multimodal Embedding Example

For multimodal models like GME that support both text and images:

```
python3 -m sglang.launch_server \
  --model-path Alibaba-NLP/gme-Qwen2-VL-2B-Instruct \
  --is-embedding \
  --chat-template gme-qwen2-vl \
  --host 0.0.0.0 \
  --port 30000

import requests

url = "http://127.0.0.1:30000"

text_input = "Represent this image in embedding space."
image_path = "https://huggingface.co/datasets/liuhaotian/llava-bench-in-the-wild/resolve/main/images/023.jpg"

payload = {
    "model": "gme-qwen2-vl",
    "input": [
        {
            "text": text_input
        },
        {
            "image": image_path
        }
    ],
}

response = requests.post(url + "/v1/embeddings", json=payload).json()

print("Embeddings:", [x.get("embedding") for x in response.get("data", [])])
```

## Matryoshka Embedding Example

[Matryoshka Embeddings](https://sbert.net/examples/sentence_transformer/training/matryoshka/README.html#matryoshka-embeddings) or [Matryoshka Representation Learning (MRL)](https://arxiv.org/abs/2205.13147) is a technique used in training embedding models. It allows user to trade off between performance and cost.

### 1. Launch a Matryoshka‑capable model

If the model config already includes `matryoshka_dimensions` or `is_matryoshka` then no override is needed. Otherwise, you can use `--json-model-override-args` as below:

```
python3 -m sglang.launch_server \
    --model-path Qwen/Qwen3-Embedding-0.6B \
    --is-embedding \
    --host 0.0.0.0 \
    --port 30000 \
    --json-model-override-args '{"matryoshka_dimensions": [128, 256, 512, 1024, 1536]}'
```

1. Setting `"is_matryoshka": true` allows truncating to any dimension. Otherwise, the server will validate that the specified dimension in the request is one of `matryoshka_dimensions`.
2. Omitting `dimensions` in a request returns the full vector.

### 2. Make requests with different output dimensions

```
import requests

url = "http://127.0.0.1:30000"

# Request a truncated (Matryoshka) embedding by specifying a supported dimension.
payload = {
    "model": "Qwen/Qwen3-Embedding-0.6B",
    "input": "Explain diffusion models simply.",
    "dimensions": 512  # change to 128 / 1024 / omit for full size
}

response = requests.post(url + "/v1/embeddings", json=payload).json()
print("Embedding:", response["data"][0]["embedding"])
```

## Supported Models

Model FamilyExample ModelChat templateDescriptionE5 (Llama/Mistral based)`intfloat/e5-mistral-7b-instruct`N/AHigh-quality text embeddings based on Mistral/Llama architecturesGTE-Qwen2`Alibaba-NLP/gte-Qwen2-7B-instruct`N/AAlibaba’s text embedding model with multilingual supportQwen3-Embedding`Qwen/Qwen3-Embedding-4B`N/ALatest Qwen3-based text embedding model for semantic representationBGE`BAAI/bge-large-en-v1.5`N/ABAAI’s text embeddings (requires `attention-backend` triton/torch\_native)GME (Multimodal)`Alibaba-NLP/gme-Qwen2-VL-2B-Instruct``gme-qwen2-vl`Multimodal embedding for text and image cross-modal tasksCLIP`openai/clip-vit-large-patch14-336`N/AOpenAI’s CLIP for image and text embeddings