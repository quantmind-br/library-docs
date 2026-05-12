---
title: Loading models with Run:ai Model Streamer
url: https://docs.vllm.ai/en/latest/models/extensions/runai_model_streamer/
source: sitemap
fetched_at: 2026-05-07T21:14:56.919621567-03:00
rendered_js: false
word_count: 398
summary: This document explains how to configure vLLM to load model weights from object storage and local files using the Run:ai Model Streamer library for efficient, concurrent tensor streaming to GPU memory.
tags:
    - vllm
    - runai-model-streamer
    - model-loading
    - cloud-storage
    - safetensors
    - distributed-training
category: configuration
---

[](https://github.com/vllm-project/vllm/edit/main/docs/models/extensions/runai_model_streamer.md "Edit this page")

Run:ai Model Streamer is a library to read tensors in concurrency, while streaming it to GPU memory. Further reading can be found in [Run:ai Model Streamer Documentation](https://github.com/run-ai/runai-model-streamer/blob/master/docs/README.md).

vLLM supports loading weights in Safetensors format using the Run:ai Model Streamer. You first need to install vLLM RunAI optional dependency:

To run it as an OpenAI-compatible server, add the `--load-format runai_streamer` flag:

```
vllmserve/home/meta-llama/Llama-3.2-3B-Instruct\
--load-formatrunai_streamer
```

To run model from AWS S3 object store run:

```
vllmserves3://core-llm/Llama-3-8b\
--load-formatrunai_streamer
```

To run model from Google Cloud Storage run:

```
vllmservegs://core-llm/Llama-3-8b\
--load-formatrunai_streamer
```

To run model from Azure Blob Storage run:

```
AZURE_STORAGE_ACCOUNT_NAME=<account>\
vllmserveaz://<container>/<model-path>\
--load-formatrunai_streamer
```

Authentication uses `DefaultAzureCredential`, which supports `az login`, managed identity, environment variables (`AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_CLIENT_SECRET`), and other methods.

To run model from a S3 compatible object store run:

```
RUNAI_STREAMER_S3_USE_VIRTUAL_ADDRESSING=0\
AWS_EC2_METADATA_DISABLED=true\
AWS_ENDPOINT_URL=https://storage.googleapis.com\
vllmserves3://core-llm/Llama-3-8b\
--load-formatrunai_streamer
```

## Tunable parameters[¶](#tunable-parameters "Permanent link")

You can tune parameters using `--model-loader-extra-config`:

You can tune `distributed` that controls whether distributed streaming should be used. This is currently only possible on CUDA and ROCM devices. This can significantly improve loading times from object storage or high-throughput network fileshares. You can read further about Distributed streaming [here](https://github.com/run-ai/runai-model-streamer/blob/master/docs/src/usage.md#distributed-streaming)

```
vllmserve/home/meta-llama/Llama-3.2-3B-Instruct\
--load-formatrunai_streamer\
--model-loader-extra-config'{"distributed":true}'
```

You can tune `concurrency` that controls the level of concurrency and number of OS threads reading tensors from the file to the CPU buffer. For reading from S3, it will be the number of client instances the host is opening to the S3 server.

```
vllmserve/home/meta-llama/Llama-3.2-3B-Instruct\
--load-formatrunai_streamer\
--model-loader-extra-config'{"concurrency":16}'
```

You can control the size of the CPU Memory buffer to which tensors are read from the file, and limit this size. You can read further about CPU buffer memory limiting [here](https://github.com/run-ai/runai-model-streamer/blob/master/docs/src/env-vars.md#runai_streamer_memory_limit).

```
vllmserve/home/meta-llama/Llama-3.2-3B-Instruct\
--load-formatrunai_streamer\
--model-loader-extra-config'{"memory_limit":5368709120}'
```

## Sharded Model Loading[¶](#sharded-model-loading "Permanent link")

vLLM also supports loading sharded models using Run:ai Model Streamer. This is particularly useful for large models that are split across multiple files. To use this feature, use the `--load-format runai_streamer_sharded` flag:

```
vllmserve/path/to/sharded/model--load-formatrunai_streamer_sharded
```

The sharded loader expects model files to follow the same naming pattern as the regular sharded state loader: `model-rank-{rank}-part-{part}.safetensors`. You can customize this pattern using the `pattern` parameter in `--model-loader-extra-config`:

```
vllmserve/path/to/sharded/model\
--load-formatrunai_streamer_sharded\
--model-loader-extra-config'{"pattern":"custom-model-rank-{rank}-part-{part}.safetensors"}'
```

To create sharded model files, you can use the script provided in [examples/features/sharded\_state/save\_sharded\_state\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/features/sharded_state/save_sharded_state_offline.py). This script demonstrates how to save a model in the sharded format that is compatible with the Run:ai Model Streamer sharded loader.

The sharded loader supports all the same tunable parameters as the regular Run:ai Model Streamer, including `concurrency` and `memory_limit`. These can be configured in the same way:

```
vllmserve/path/to/sharded/model\
--load-formatrunai_streamer_sharded\
--model-loader-extra-config'{"concurrency":16, "memory_limit":5368709120}'
```

Note

The sharded loader is particularly efficient for tensor or pipeline parallel models where each worker only needs to read its own shard rather than the entire checkpoint.