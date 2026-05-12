---
title: Custom Chat Template - SGLang Documentation
url: https://docs.sglang.io/docs/references/custom_chat_template
source: sitemap
fetched_at: 2026-05-11T05:48:30.774751456-03:00
rendered_js: false
word_count: 156
summary: This document provides instructions on how to configure and override custom chat templates for the SGLang OpenAI-compatible API server using either JSON or Jinja formats.
tags:
    - sglang
    - chat-template
    - api-server
    - model-configuration
    - jinja
    - json-format
category: configuration
---

> ## Documentation Index
> 
> Fetch the complete documentation index at: [https://docs.sglang.io/llms.txt](https://docs.sglang.io/llms.txt)
> 
> Use this file to discover all available pages before exploring further.

**NOTE**: There are two chat template systems in SGLang project. This document is about setting a custom chat template for the OpenAI-compatible API server (defined at [conversation.py](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/conversation.py)). It is NOT related to the chat template used in the SGLang language frontend (defined at [chat\_template.py](https://github.com/sgl-project/sglang/blob/main/python/sglang/lang/chat_template.py)). By default, the server uses the chat template specified in the model tokenizer from Hugging Face. It should just work for most official models such as Llama-2/Llama-3. If needed, you can also override the chat template when launching the server:

```
python -m sglang.launch_server \
  --model-path meta-llama/Llama-2-7b-chat-hf \
  --port 30000 \
  --chat-template llama-2
```

If the chat template you are looking for is missing, you are welcome to contribute it or load it from a file.

## JSON Format

You can load the JSON format, which is defined by `conversation.py`.

```
{
  "name": "my_model",
  "system": "<|im_start|>system",
  "user": "<|im_start|>user",
  "assistant": "<|im_start|>assistant",
  "sep_style": "CHATML",
  "sep": "<|im_end|>",
  "stop_str": ["<|im_end|>", "<|im_start|>"]
}

python -m sglang.launch_server \
  --model-path meta-llama/Llama-2-7b-chat-hf \
  --port 30000 \
  --chat-template ./my_model_template.json
```

## Jinja Format

You can also use the [Jinja template format](https://huggingface.co/docs/transformers/main/en/chat_templating) as defined by Hugging Face Transformers.

```
python -m sglang.launch_server \
  --model-path meta-llama/Llama-2-7b-chat-hf \
  --port 30000 \
  --chat-template ./my_model_template.jinja
```