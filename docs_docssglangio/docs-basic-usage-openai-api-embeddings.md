---
title: OpenAI APIs - Embedding - SGLang Documentation
url: https://docs.sglang.io/docs/basic_usage/openai_api_embeddings
source: sitemap
fetched_at: 2026-05-11T05:49:02.451380858-03:00
rendered_js: false
word_count: 124
summary: This document provides instructions on how to use SGLang's OpenAI-compatible embedding APIs, including server configuration and request patterns using cURL, Python requests, and the OpenAI client.
tags:
    - sglang
    - embeddings
    - openai-api
    - local-llm
    - server-configuration
    - text-embeddings
    - input-ids
category: tutorial
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

SGLang provides OpenAI-compatible APIs to enable a smooth transition from OpenAI services to self-hosted local models. A complete reference for the API is available in the [OpenAI API Reference](https://platform.openai.com/docs/guides/embeddings). This tutorial covers the embedding APIs for embedding models. For a list of the supported models see the [corresponding overview page](https://docs.sglang.io/docs/supported-models)

## Launch A Server

Launch the server in your terminal and wait for it to initialize. Remember to add `--is-embedding` to the command.

```
from sglang.test.doc_patch import launch_server_cmd
from sglang.utils import wait_for_server, print_highlight, terminate_process

embedding_process, port = launch_server_cmd(
    """
python3 -m sglang.launch_server --model-path Alibaba-NLP/gte-Qwen2-1.5B-instruct \
    --host 0.0.0.0 --is-embedding --log-level warning
"""
)

wait_for_server(f"http://localhost:{port}")
```

## Using cURL

```
import subprocess, json

text = "Once upon a time"

curl_text = f"""curl -s http://localhost:{port}/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{{"model": "Alibaba-NLP/gte-Qwen2-1.5B-instruct", "input": "{text}"}}'"""

result = subprocess.check_output(curl_text, shell=True)

print(result)

text_embedding = json.loads(result)["data"][0]["embedding"]

print_highlight(f"Text embedding (first 10): {text_embedding[:10]}")
```

## Using Python Requests

```
import requests

text = "Once upon a time"

response = requests.post(
    f"http://localhost:{port}/v1/embeddings",
    json={"model": "Alibaba-NLP/gte-Qwen2-1.5B-instruct", "input": text},
)

text_embedding = response.json()["data"][0]["embedding"]

print_highlight(f"Text embedding (first 10): {text_embedding[:10]}")
```

## Using OpenAI Python Client

```
import openai

client = openai.Client(base_url=f"http://127.0.0.1:{port}/v1", api_key="None")

# Text embedding example
response = client.embeddings.create(
    model="Alibaba-NLP/gte-Qwen2-1.5B-instruct",
    input=text,
)

embedding = response.data[0].embedding[:10]
print_highlight(f"Text embedding (first 10): {embedding}")
```

## Using Input IDs

SGLang also supports `input_ids` as input to get the embedding.

```
import json
import os
from transformers import AutoTokenizer

os.environ["TOKENIZERS_PARALLELISM"] = "false"

tokenizer = AutoTokenizer.from_pretrained("Alibaba-NLP/gte-Qwen2-1.5B-instruct")
input_ids = tokenizer.encode(text)

curl_ids = f"""curl -s http://localhost:{port}/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{{"model": "Alibaba-NLP/gte-Qwen2-1.5B-instruct", "input": {json.dumps(input_ids)}}}'"""

input_ids_embedding = json.loads(subprocess.check_output(curl_ids, shell=True))["data"][
    0
]["embedding"]

print_highlight(f"Input IDs embedding (first 10): {input_ids_embedding[:10]}")

terminate_process(embedding_process)
```

## Multi-Modal Embedding Model

Please refer to [Multi-Modal Embedding Model](https://docs.sglang.io/docs/supported-models)