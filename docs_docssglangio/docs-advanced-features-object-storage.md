---
title: Loading Models from Object Storage - SGLang Documentation
url: https://docs.sglang.io/docs/advanced_features/object_storage
source: sitemap
fetched_at: 2026-05-11T05:49:25.436392399-03:00
rendered_js: false
word_count: 279
summary: This document explains how to configure SGLang to stream large language model weights directly from object storage providers like Amazon S3, Google Cloud Storage, and Azure Blob to optimize startup times and storage usage.
tags:
    - sglang
    - model-loading
    - object-storage
    - cloud-storage
    - weight-streaming
    - runai-streamer
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

SGLang supports direct loading of models from object storage (S3 and Google Cloud Storage) without requiring a full local download. This feature uses the `runai_streamer` load format to stream model weights directly from cloud storage, significantly reducing startup time and local storage requirements.

## Overview

When loading models from object storage, SGLang uses a two-phase approach:

1. **Metadata Download** (once, before process launch): Configuration files and tokenizer files are downloaded to a local cache
2. **Weight Streaming** (lazy, during model loading): Model weights are streamed directly from object storage as needed

## Supported Storage Backends

1. **Amazon S3**: `s3://bucket-name/path/to/model/`
2. **Google Cloud Storage**: `gs://bucket-name/path/to/model/`
3. **Azure Blob**: `az://some-azure-container/path/`
4. **S3 compatible**: `s3://bucket-name/path/to/model/`

## Quick Start

### Basic Usage

Simply provide an object storage URI as the model path:

```
# S3
python -m sglang.launch_server \
  --model-path s3://my-bucket/models/llama-3-8b/ \
  --load-format runai_streamer

# Google Cloud Storage
python -m sglang.launch_server \
  --model-path gs://my-bucket/models/llama-3-8b/ \
  --load-format runai_streamer
```

**Note**: The `--load-format runai_streamer` is automatically detected when using object storage URIs, so you can omit it:

```
python -m sglang.launch_server \
  --model-path s3://my-bucket/models/llama-3-8b/
```

### With Tensor Parallelism

```
python -m sglang.launch_server \
  --model-path gs://my-bucket/models/llama-70b/ \
  --tp 4 \
  --model-loader-extra-config '{"distributed": true}'
```

## Configuration

### Load Format

The `runai_streamer` load format is specifically designed for object storage, ssd and shared file systems

```
python -m sglang.launch_server \
  --model-path s3://bucket/model/ \
  --load-format runai_streamer
```

### Extended Configuration Parameters

Use `--model-loader-extra-config` to pass additional configuration as a JSON string:

```
python -m sglang.launch_server \
  --model-path s3://bucket/model/ \
  --model-loader-extra-config '{
    "distributed": true,
    "concurrency": 8,
    "memory_limit": 2147483648
  }'
```

#### Available Parameters

ParameterTypeDescriptionDefault`distributed`boolEnable distributed streaming for multi-GPU setups. Automatically set to `true` for object storage paths and cuda alike devices.Auto-detected`concurrency`intNumber of concurrent download streams. Higher values can improve throughput for large models.4`memory_limit`intMemory limit (in bytes) for the streaming buffer.System-dependent

## Performance Considerations

### Distributed Streaming

For multi-GPU setups, enable distributed streaming to parallelize weight loading between the processes:

```
python -m sglang.launch_server \
  --model-path s3://bucket/model/ \
  --tp 8 \
  --model-loader-extra-config '{"distributed": true}'
```

## Limitations

- **Supported Formats**: Currently only supports `.safetensors` weight format (recommended format)
- **Supported Device**: Distributed streaming is supported on cuda alike devices. Otherwise fallback to non distributed streaming

## See Also

- [Runai model streamer documentation](https://github.com/run-ai/runai-model-streamer)