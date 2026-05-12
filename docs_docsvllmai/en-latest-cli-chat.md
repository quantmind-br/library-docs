---
title: vllm chat - vLLM
url: https://docs.vllm.ai/en/latest/cli/chat/
source: sitemap
fetched_at: 2026-05-07T21:10:56.53731976-03:00
rendered_js: false
word_count: 123
summary: This document lists the command-line arguments available for the vLLM chat interface used to interact with OpenAI-compatible RESTful API servers.
tags:
    - vllm
    - cli-reference
    - openai-compatible-api
    - chat-interface
    - command-line-arguments
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/cli/chat.md "Edit this page")

## Arguments[¶](#arguments "Permanent link")

#### `--url`[¶](#-url "Permanent link")

url of the running OpenAI-Compatible RESTful API server

Default: `http://localhost:8000/v1`

#### `--model-name`[¶](#-model-name "Permanent link")

The model name used in prompt completion, default to the first model in list models API call.

#### `--api-key`[¶](#-api-key "Permanent link")

API key for OpenAI services. If provided, this api key will overwrite the api key obtained through environment variables. It is important to note that this option only applies to the OpenAI-compatible API endpoints and NOT other endpoints that may be present in the server. See the security guide in the vLLM docs for more details.

#### `--system-prompt`[¶](#-system-prompt "Permanent link")

The system prompt to be added to the chat template, used for models that support system prompts.

#### `-q`, `--quick`[¶](#-q-quick "Permanent link")

Send a single prompt as MESSAGE and print the response, then exit.