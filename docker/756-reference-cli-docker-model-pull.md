---
title: docker model pull
url: https://docs.docker.com/reference/cli/docker/model/pull/
source: llms
fetched_at: 2026-01-24T14:38:26.641587271-03:00
rendered_js: false
word_count: 119
summary: This document provides instructions and reference details for using the docker model pull command to download AI models from Docker Hub or Hugging Face.
tags:
    - docker-cli
    - model-management
    - machine-learning
    - huggingface
    - docker-hub
    - gguf-models
category: reference
---

DescriptionPull a model from Docker Hub or HuggingFace to your local environmentUsage`docker model pull MODEL`

## [Description](#description)

Pull a model to your local environment. Downloaded models also appear in the Docker Desktop Dashboard.

## [Options](#options)

OptionDefaultDescription`--ignore-runtime-memory-check`Do not block pull if estimated runtime memory for model exceeds system resources.

## [Examples](#examples)

### [Pulling a model from Docker Hub](#pulling-a-model-from-docker-hub)

```
docker model pull ai/smollm2
```

### [Pulling from HuggingFace](#pulling-from-huggingface)

You can pull GGUF models directly from [Hugging Face](https://huggingface.co/models?library=gguf).

**Note about quantization:** If no tag is specified, the command tries to pull the `Q4_K_M` version of the model. If `Q4_K_M` doesn't exist, the command pulls the first GGUF found in the **Files** view of the model on HuggingFace. To specify the quantization, provide it as a tag, for example: `docker model pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:Q4_K_S`

```
docker model pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF
```