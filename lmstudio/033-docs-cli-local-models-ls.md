---
title: '`lms ls`'
url: https://lmstudio.ai/docs/cli/local-models/ls
source: sitemap
fetched_at: 2026-04-07T21:28:31.724264883-03:00
rendered_js: false
word_count: 156
summary: This document explains the usage of the `lms ls` command, detailing how it lists downloaded models along with various filtering options like model type and output format.
tags:
    - command-line
    - list-models
    - llm
    - embedding-models
    - flags
    - ls
category: reference
---

The `lms ls` command displays a list of all models downloaded to your machine, including their size, architecture, and parameters.

### Flags[](#flags)

--llm (optional) : flag

Show only LLMs. When not set, all models are shown

--embedding (optional) : flag

Show only embedding models

--json (optional) : flag

Output the list in JSON format

--detailed (optional) : flag

Show detailed information about each model

## List all models[](#list-all-models "Link to 'List all models'")

Show all downloaded models:


Example output:

```

You have 47 models, taking up 160.78 GB of disk space.

LLMs (Large Language Models)                       PARAMS      ARCHITECTURE           SIZE
lmstudio-community/meta-llama-3.1-8b-instruct          8B         Llama            4.92 GB
hugging-quants/llama-3.2-1b-instruct                   1B         Llama            1.32 GB
mistral-7b-instruct-v0.3                                         Mistral           4.08 GB
zeta                                                   7B         Qwen2            4.09 GB

... (abbreviated in this example) ...

Embedding Models                                   PARAMS      ARCHITECTURE           SIZE
text-embedding-nomic-embed-text-v1.5@q4_k_m                     Nomic BERT        84.11 MB
text-embedding-bge-small-en-v1.5                     33M           BERT           24.81 MB
```

### Filter by model type[](#filter-by-model-type)

List only LLM models:


List only embedding models:


### Additional output formats[](#additional-output-formats)

Get detailed information about models:


Output in JSON format:


## Operate on a remote LM Studio instance[](#operate-on-a-remote-lm-studio-instance "Link to 'Operate on a remote LM Studio instance'")

`lms ls` supports the `--host` flag to connect to a remote LM Studio instance:


For this to work, the remote LM Studio instance must be running and accessible from your local machine, e.g. be accessible on the same subnet.