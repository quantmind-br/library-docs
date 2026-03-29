---
title: Custom Chat Template — SGLang
url: https://docs.sglang.io/references/custom_chat_template.html
source: crawler
fetched_at: 2026-02-04T08:47:19.735715195-03:00
rendered_js: false
word_count: 138
summary: Explains how to configure and override custom chat templates for the SGLang OpenAI-compatible API server using command-line arguments, JSON files, or Jinja templates.
tags:
    - sglang
    - chat-template
    - openai-api
    - llm-serving
    - jinja-template
    - configuration
category: configuration
---

## Custom Chat Template[#](#custom-chat-template "Link to this heading")

**NOTE**: There are two chat template systems in SGLang project. This document is about setting a custom chat template for the OpenAI-compatible API server (defined at [conversation.py](https://github.com/sgl-project/sglang/blob/main/python/sglang/srt/conversation.py)). It is NOT related to the chat template used in the SGLang language frontend (defined at [chat\_template.py](https://github.com/sgl-project/sglang/blob/main/python/sglang/lang/chat_template.py)).

By default, the server uses the chat template specified in the model tokenizer from Hugging Face. It should just work for most official models such as Llama-2/Llama-3.

If needed, you can also override the chat template when launching the server:

```
python-msglang.launch_server\
--model-pathmeta-llama/Llama-2-7b-chat-hf\
--port30000\
--chat-templatellama-2
```

If the chat template you are looking for is missing, you are welcome to contribute it or load it from a file.

## JSON Format[#](#json-format "Link to this heading")

You can load the JSON format, which is defined by `conversation.py`.

```
{
"name":"my_model",
"system":"<|im_start|>system",
"user":"<|im_start|>user",
"assistant":"<|im_start|>assistant",
"sep_style":"CHATML",
"sep":"<|im_end|>",
"stop_str":["<|im_end|>","<|im_start|>"]
}
```

```
python-msglang.launch_server\
--model-pathmeta-llama/Llama-2-7b-chat-hf\
--port30000\
--chat-template./my_model_template.json
```

## Jinja Format[#](#jinja-format "Link to this heading")

You can also use the [Jinja template format](https://huggingface.co/docs/transformers/main/en/chat_templating) as defined by Hugging Face Transformers.

```
python-msglang.launch_server\
--model-pathmeta-llama/Llama-2-7b-chat-hf\
--port30000\
--chat-template./my_model_template.jinja
```