---
title: Prompt Caching | liteLLM
url: https://docs.litellm.ai/docs/completion/prompt_caching
source: sitemap
fetched_at: 2026-01-21T19:44:40.533560043-03:00
rendered_js: false
word_count: 285
summary: This document explains how LiteLLM supports and implements prompt caching across various providers including OpenAI, Anthropic, and DeepSeek.
tags:
    - litellm
    - prompt-caching
    - openai
    - anthropic
    - deepseek
    - cost-management
category: guide
---

For the supported providers, LiteLLM follows the OpenAI prompt caching usage object format:

Note: OpenAI caching is only available for prompts containing 1024 tokens or more

Anthropic charges for cache writes.

Specify the content to cache with `"cache_control": {"type": "ephemeral"}`.

If you pass that in for any other llm provider, it will be ignored.

Works the same as OpenAI.

```
from litellm import completion 
import litellm
import os 

os.environ["DEEPSEEK_API_KEY"]=""

litellm.set_verbose =True# 👈 SEE RAW REQUEST

model_name ="deepseek/deepseek-chat"
messages_1 =[
{
"role":"system",
"content":"You are a history expert. The user will provide a series of questions, and your answers should be concise and start with `Answer:`",
},
{
"role":"user",
"content":"In what year did Qin Shi Huang unify the six states?",
},
{"role":"assistant","content":"Answer: 221 BC"},
{"role":"user","content":"Who was the founder of the Han Dynasty?"},
{"role":"assistant","content":"Answer: Liu Bang"},
{"role":"user","content":"Who was the last emperor of the Tang Dynasty?"},
{"role":"assistant","content":"Answer: Li Zhu"},
{
"role":"user",
"content":"Who was the founding emperor of the Ming Dynasty?",
},
{"role":"assistant","content":"Answer: Zhu Yuanzhang"},
{
"role":"user",
"content":"Who was the founding emperor of the Qing Dynasty?",
},
]

message_2 =[
{
"role":"system",
"content":"You are a history expert. The user will provide a series of questions, and your answers should be concise and start with `Answer:`",
},
{
"role":"user",
"content":"In what year did Qin Shi Huang unify the six states?",
},
{"role":"assistant","content":"Answer: 221 BC"},
{"role":"user","content":"Who was the founder of the Han Dynasty?"},
{"role":"assistant","content":"Answer: Liu Bang"},
{"role":"user","content":"Who was the last emperor of the Tang Dynasty?"},
{"role":"assistant","content":"Answer: Li Zhu"},
{
"role":"user",
"content":"Who was the founding emperor of the Ming Dynasty?",
},
{"role":"assistant","content":"Answer: Zhu Yuanzhang"},
{"role":"user","content":"When did the Shang Dynasty fall?"},
]

response_1 = litellm.completion(model=model_name, messages=messages_1)
response_2 = litellm.completion(model=model_name, messages=message_2)

# Add any assertions here to check the response
print(response_2.usage)
```

Cost cache-hit prompt tokens can differ from cache-miss prompt tokens.

```
cost = completion_cost(completion_response=response, model=model)
```