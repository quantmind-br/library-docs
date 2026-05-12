---
title: Launch GLM-4.5 / GLM-4.6 / GLM-4.7 with SGLang - SGLang Documentation
url: https://docs.sglang.io/docs/basic_usage/glm45
source: sitemap
fetched_at: 2026-05-11T05:49:05.048694844-03:00
rendered_js: false
word_count: 103
summary: This document provides instructions for serving GLM-4.5 and GLM-4.6 models using SGLang, including configurations for EAGLE speculative decoding and custom thinking budget logic.
tags:
    - sglang
    - llm-serving
    - glm-4
    - speculative-decoding
    - eagle
    - model-optimization
category: guide
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

To serve GLM-4.5 / GLM-4.6 FP8 models on 8xH100/H200 GPUs:

```
python3 -m sglang.launch_server --model zai-org/GLM-4.6-FP8 --tp 8
```

### EAGLE Speculative Decoding

**Description**: SGLang has supported GLM-4.5 / GLM-4.6 models with [EAGLE speculative decoding](https://docs.sglang.io/docs/advanced_features/speculative_decoding#EAGLE-Decoding). **Usage**: Add arguments `--speculative-algorithm`, `--speculative-num-steps`, `--speculative-eagle-topk` and `--speculative-num-draft-tokens` to enable this feature. For example:

```
python3 -m sglang.launch_server \
  --model-path zai-org/GLM-4.6-FP8 \
  --tp-size 8 \
  --tool-call-parser glm45  \
  --reasoning-parser glm45  \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 3  \
  --speculative-eagle-topk 1  \
  --speculative-num-draft-tokens 4 \
  --mem-fraction-static 0.9 \
  --served-model-name glm-4.6-fp8 \
  --enable-custom-logit-processor
```

### Thinking Budget for GLM-4.5 / GLM-4.6

**Note**: For GLM-4.7, `--tool-call-parser` should be set to `glm47`, for GLM-4.5 and GLM-4.6, it should be set to `glm45`. In SGLang, we can implement thinking budget with `CustomLogitProcessor`. Launch a server with `--enable-custom-logit-processor` flag on. Sample Request:

```
import openai
from rich.pretty import pprint
from sglang.srt.sampling.custom_logit_processor import Glm4MoeThinkingBudgetLogitProcessor


client = openai.Client(base_url="http://127.0.0.1:30000/v1", api_key="*")
response = client.chat.completions.create(
    model="zai-org/GLM-4.6",
    messages=[
        {
            "role": "user",
            "content": "Question: Is Paris the Capital of France?",
        }
    ],
    max_tokens=1024,
    extra_body={
        "custom_logit_processor": Glm4MoeThinkingBudgetLogitProcessor().to_str(),
        "custom_params": {
            "thinking_budget": 512,
        },
    },
)
pprint(response)
```