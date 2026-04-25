---
title: '`lms ps`'
url: https://lmstudio.ai/docs/cli/local-models/ps
source: sitemap
fetched_at: 2026-04-07T21:28:29.703735138-03:00
rendered_js: false
word_count: 91
summary: This document explains how the `lms ps` command can display detailed information about all locally loaded models or connect to and query a remote LM Studio instance.
tags:
    - command-line
    - model-management
    - loaded-models
    - remote-connection
    - llm-studio
category: reference
---

The `lms ps` command displays information about all models currently loaded in memory.

## List loaded models[](#list-loaded-models "Link to 'List loaded models'")

Show all currently loaded models:


Example output:

```

   LOADED MODELS

Identifier: unsloth/deepseek-r1-distill-qwen-1.5b
  • Type:  LLM
  • Path: unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf
  • Size: 1.12 GB
  • Architecture: Qwen2
```

### JSON output[](#json-output)

Get the list in machine-readable format:


## Operate on a remote LM Studio instance[](#operate-on-a-remote-lm-studio-instance "Link to 'Operate on a remote LM Studio instance'")

`lms ps` supports the `--host` flag to connect to a remote LM Studio instance:


For this to work, the remote LM Studio instance must be running and accessible from your local machine, e.g. be accessible on the same subnet.