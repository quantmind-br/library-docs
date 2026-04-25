---
title: List your models
url: https://lmstudio.ai/docs/developer/rest/list
source: sitemap
fetched_at: 2026-04-07T21:30:19.954331332-03:00
rendered_js: false
word_count: 294
summary: This document details the structure and expected response fields when accessing the GET /api/v1/models endpoint, which lists all available language and embedding models.
tags:
    - api-endpoint
    - model-listing
    - response-schema
    - llm-models
    - embedding-models
category: reference
---

`GET /api/v1/models`

This endpoint has no request parameters.

* * *

**Response fields**

models : array

List of available models (both LLMs and embedding models).

type : "llm" | "embedding"

Type of model.

publisher : string

Model publisher name.

key : string

Unique identifier for the model.

display\_name : string

Human-readable model name.

architecture (optional) : string | null

Model architecture (e.g., "llama", "mistral"). Absent for embedding models.

quantization : object | null

Quantization information for the model.

name : string | null

Quantization method name.

bits\_per\_weight : number | null

Bits per weight for the quantization.

size\_bytes : number

Size of the model in bytes.

params\_string : string | null

Human-readable parameter count (e.g., "7B", "13B").

loaded\_instances : array

List of currently loaded instances of this model.

id : string

Unique identifier for the loaded model instance.

config : object

Configuration for the loaded instance.

context\_length : number

The maximum context length for the model in number of tokens.

eval\_batch\_size (optional) : number

Number of input tokens to process together in a single batch during evaluation. Absent for embedding models.

flash\_attention (optional) : boolean

Whether Flash Attention is enabled for optimized attention computation. Absent for embedding models.

num\_experts (optional) : number

Number of experts for MoE (Mixture of Experts) models. Absent for embedding models.

offload\_kv\_cache\_to\_gpu (optional) : boolean

Whether KV cache is offloaded to GPU memory. Absent for embedding models.

max\_context\_length : number

Maximum context length supported by the model in number of tokens.

format : "gguf" | "mlx" | null

Model file format.

capabilities (optional) : object

Model capabilities. Absent for embedding models.

vision : boolean

Whether the model supports vision/image inputs.

trained\_for\_tool\_use : boolean

Whether the model was trained for tool/function calling.

description (optional) : string | null

Model description. Absent for embedding models.