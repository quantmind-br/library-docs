---
title: ""
url: https://docs.sglang.io/_sources/basic_usage/glm45.md
source: crawler
fetched_at: 2026-02-04T08:48:37.104733446-03:00
rendered_js: false
word_count: 120
summary: This document provides instructions for serving GLM-4 series models using SGLang, including configurations for speculative decoding and implementing a thinking budget.
tags:
    - sglang
    - glm-4
    - speculative-decoding
    - model-serving
    - eagle-decoding
    - thinking-budget
    - llm-inference
category: tutorial
---

## Launch GLM-4.5 / GLM-4.6 / GLM-4.7 with SGLang

To serve GLM-4.5 / GLM-4.6 FP8 models on 8xH100/H200 GPUs:

```bash
python3 -m sglang.launch_server --model zai-org/GLM-4.6-FP8 --tp 8
```

### EAGLE Speculative Decoding

**Description**: SGLang has supported GLM-4.5 / GLM-4.6 models
with [EAGLE speculative decoding](https://docs.sglang.io/advanced_features/speculative_decoding.html#EAGLE-Decoding).

**Usage**:
Add arguments `--speculative-algorithm`, `--speculative-num-steps`, `--speculative-eagle-topk` and
`--speculative-num-draft-tokens` to enable this feature. For example:

``` bash
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

```{tip}
To enable the experimental overlap scheduler for EAGLE speculative decoding, set the environment variable `SGLANG_ENABLE_SPEC_V2=1`. This can improve performance by enabling overlap scheduling between draft and verification stages.
```

### Thinking Budget for GLM-4.5 / GLM-4.6
**Note**: For GLM-4.7, `--tool-call-parser` should be set to `glm47`, for GLM-4.5 and GLM-4.6, it should be set to `glm45`.

In SGLang, we can implement thinking budget with `CustomLogitProcessor`.

Launch a server with `--enable-custom-logit-processor` flag on.

Sample Request:

```python
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