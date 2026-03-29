---
title: Use Models From ModelScope — SGLang
url: https://docs.sglang.io/supported_models/modelscope.html
source: crawler
fetched_at: 2026-02-04T08:47:09.480426021-03:00
rendered_js: false
word_count: 53
summary: This document explains how to configure and launch an SGLang server using models from the ModelScope platform by setting specific environment variables and using Docker or Python commands.
tags:
    - sglang
    - modelscope
    - model-deployment
    - docker-configuration
    - environment-variables
    - large-language-models
category: guide
---

## Use Models From ModelScope[#](#use-models-from-modelscope "Link to this heading")

To use a model from [ModelScope](https://www.modelscope.cn), set the environment variable `SGLANG_USE_MODELSCOPE`.

```
exportSGLANG_USE_MODELSCOPE=true
```

We take [Qwen2-7B-Instruct](https://www.modelscope.cn/models/qwen/qwen2-7b-instruct) as an example.

Launch the Server:

```
python-msglang.launch_server--model-pathqwen/Qwen2-7B-Instruct--port30000
```

Or start it by docker:

```
dockerrun--gpusall\
-p30000:30000\
-v~/.cache/modelscope:/root/.cache/modelscope\
--env"SGLANG_USE_MODELSCOPE=true"\
--ipc=host\
lmsysorg/sglang:latest\
python3-msglang.launch_server--model-pathQwen/Qwen2.5-7B-Instruct--host0.0.0.0--port30000
```

Note that modelscope uses a different cache directory than huggingface. You may need to set it manually to avoid running out of disk space.