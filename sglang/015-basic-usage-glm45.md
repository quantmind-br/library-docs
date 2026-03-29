---
title: Launch GLM-4.5 / GLM-4.6 / GLM-4.7 with SGLang — SGLang
url: https://docs.sglang.io/basic_usage/glm45.html
source: crawler
fetched_at: 2026-02-04T08:47:38.170159267-03:00
rendered_js: false
word_count: 119
summary: This document explains how to deploy GLM-4.x models using SGLang, including instructions for EAGLE speculative decoding and implementing thinking budget configurations.
tags:
    - sglang
    - glm-4
    - speculative-decoding
    - eagle-decoding
    - llm-serving
    - model-inference
category: guide
---

## Launch GLM-4.5 / GLM-4.6 / GLM-4.7 with SGLang[#](#launch-glm-4-5-glm-4-6-glm-4-7-with-sglang "Link to this heading")

To serve GLM-4.5 / GLM-4.6 FP8 models on 8xH100/H200 GPUs:

```
python3-msglang.launch_server--modelzai-org/GLM-4.6-FP8--tp8
```

## EAGLE Speculative Decoding[#](#eagle-speculative-decoding "Link to this heading")

**Description**: SGLang has supported GLM-4.5 / GLM-4.6 models with [EAGLE speculative decoding](https://docs.sglang.io/advanced_features/speculative_decoding.html#EAGLE-Decoding).

**Usage**: Add arguments `--speculative-algorithm`, `--speculative-num-steps`, `--speculative-eagle-topk` and `--speculative-num-draft-tokens` to enable this feature. For example:

```
python3-msglang.launch_server\
--model-pathzai-org/GLM-4.6-FP8\
--tp-size8\
--tool-call-parserglm45\
--reasoning-parserglm45\
--speculative-algorithmEAGLE\
--speculative-num-steps3\
--speculative-eagle-topk1\
--speculative-num-draft-tokens4\
--mem-fraction-static0.9\
--served-model-nameglm-4.6-fp8\
--enable-custom-logit-processor
```

Tip

To enable the experimental overlap scheduler for EAGLE speculative decoding, set the environment variable `SGLANG_ENABLE_SPEC_V2=1`. This can improve performance by enabling overlap scheduling between draft and verification stages.

## Thinking Budget for GLM-4.5 / GLM-4.6[#](#thinking-budget-for-glm-4-5-glm-4-6 "Link to this heading")

**Note**: For GLM-4.7, `--tool-call-parser` should be set to `glm47`, for GLM-4.5 and GLM-4.6, it should be set to `glm45`.

In SGLang, we can implement thinking budget with `CustomLogitProcessor`.

Launch a server with `--enable-custom-logit-processor` flag on.

Sample Request:

```
importopenai
fromrich.prettyimport pprint
fromsglang.srt.sampling.custom_logit_processorimport Glm4MoeThinkingBudgetLogitProcessor


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