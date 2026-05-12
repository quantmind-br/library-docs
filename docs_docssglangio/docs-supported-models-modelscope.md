---
title: Use Models From ModelScope - SGLang Documentation
url: https://docs.sglang.io/docs/supported-models/modelscope
source: sitemap
fetched_at: 2026-05-11T05:48:04.183903346-03:00
rendered_js: false
word_count: 70
summary: This document provides instructions on how to configure and run SGLang servers using models hosted on ModelScope.
tags:
    - sglang
    - modelscope
    - server-configuration
    - environment-variables
    - docker
    - llm-deployment
category: configuration
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

To use a model from [ModelScope](https://www.modelscope.cn), set the environment variable `SGLANG_USE_MODELSCOPE`.

```
export SGLANG_USE_MODELSCOPE=true
```

We take [Qwen2-7B-Instruct](https://www.modelscope.cn/models/qwen/qwen2-7b-instruct) as an example. Launch the Server:

```
python -m sglang.launch_server --model-path qwen/Qwen2-7B-Instruct --port 30000
```

Or start it by docker:

```
docker run --gpus all \
    -p 30000:30000 \
    -v ~/.cache/modelscope:/root/.cache/modelscope \
    --env "SGLANG_USE_MODELSCOPE=true" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server --model-path Qwen/Qwen2.5-7B-Instruct --host 0.0.0.0 --port 30000
```

Note that modelscope uses a different cache directory than huggingface. You may need to set it manually to avoid running out of disk space.