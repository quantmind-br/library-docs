---
title: vllm complete - vLLM
url: https://docs.vllm.ai/en/latest/cli/complete/
source: sitemap
fetched_at: 2026-05-07T21:10:56.623275845-03:00
rendered_js: false
word_count: 114
summary: This document lists the command-line arguments available for the vLLM completion interface when interacting with an OpenAI-compatible RESTful API server.
tags:
    - cli-reference
    - vllm
    - api-integration
    - command-line-interface
    - openai-compatible
category: reference
---

[](https://github.com/vllm-project/vllm/edit/main/docs/cli/complete.md "Edit this page")

## Arguments[¶](#arguments "Permanent link")

#### `--url`[¶](#-url "Permanent link")

url of the running OpenAI-Compatible RESTful API server

Default: `http://localhost:8000/v1`

#### `--model-name`[¶](#-model-name "Permanent link")

The model name used in prompt completion, default to the first model in list models API call.

#### `--api-key`[¶](#-api-key "Permanent link")

API key for OpenAI services. If provided, this api key will overwrite the api key obtained through environment variables. It is important to note that this option only applies to the OpenAI-compatible API endpoints and NOT other endpoints that may be present in the server. See the security guide in the vLLM docs for more details.

#### `--max-tokens`[¶](#-max-tokens "Permanent link")

Maximum number of tokens to generate per output sequence.

#### `-q`, `--quick`[¶](#-q-quick "Permanent link")

Send a single prompt and print the completion output, then exit.