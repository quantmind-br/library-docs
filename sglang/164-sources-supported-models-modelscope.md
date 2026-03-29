---
title: Use Models From ModelScope
url: https://docs.sglang.io/_sources/supported_models/modelscope.md
source: crawler
fetched_at: 2026-02-04T08:48:42.260649363-03:00
rendered_js: false
word_count: 53
summary: This document explains how to configure SGLANG to use models from ModelScope by setting the SGLANG_USE_MODELSCOPE environment variable and provides server launch examples.
tags:
    - modelscope
    - sglang
    - environment-variables
    - docker
    - deployment
    - llm-serving
category: guide
---

# Use Models From ModelScope

To use a model from [ModelScope](https://www.modelscope.cn), set the environment variable `SGLANG_USE_MODELSCOPE`.

```bash
export SGLANG_USE_MODELSCOPE=true
```

We take [Qwen2-7B-Instruct](https://www.modelscope.cn/models/qwen/qwen2-7b-instruct) as an example.

Launch the Server:
```bash
python -m sglang.launch_server --model-path qwen/Qwen2-7B-Instruct --port 30000
```

Or start it by docker:

```bash
docker run --gpus all \
    -p 30000:30000 \
    -v ~/.cache/modelscope:/root/.cache/modelscope \
    --env "SGLANG_USE_MODELSCOPE=true" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server --model-path Qwen/Qwen2.5-7B-Instruct --host 0.0.0.0 --port 30000
```

Note that modelscope uses a different cache directory than huggingface. You may need to set it manually to avoid running out of disk space.