---
title: Prompt Embedding Inputs - vLLM
url: https://docs.vllm.ai/en/latest/features/prompt_embeds/
source: sitemap
fetched_at: 2026-05-07T21:14:16.072031514-03:00
rendered_js: false
word_count: 478
summary: This document explains how to provide custom prompt embeddings directly to vLLM for both offline inference and online serving via OpenAI-compatible APIs.
tags:
    - vllm
    - prompt-embeddings
    - offline-inference
    - online-serving
    - multimodal
    - openai-api
    - tensor-processing
category: guide
---

[](https://github.com/vllm-project/vllm/edit/main/docs/features/prompt_embeds.md "Edit this page")

This page teaches you how to pass prompt embedding inputs to vLLM.

## What are prompt embeddings?[¶](#what-are-prompt-embeddings "Permanent link")

The traditional flow of text data for a Large Language Model goes from text to token ids (via a tokenizer) then from token ids to prompt embeddings. For a traditional decoder-only model (such as meta-llama/Llama-3.1-8B-Instruct), this step of converting token ids to prompt embeddings happens via a look-up from a learned embedding matrix, but the model is not limited to processing only the embeddings corresponding to its token vocabulary.

## Offline Inference[¶](#offline-inference "Permanent link")

To input multi-modal data, follow this schema in [vllm.inputs.EmbedsPrompt](https://docs.vllm.ai/en/latest/api/vllm/inputs/#vllm.inputs.EmbedsPrompt "            EmbedsPrompt"):

- `prompt_embeds`: A torch tensor representing a sequence of prompt/token embeddings. This has the shape (sequence\_length, hidden\_size), where sequence length is the number of tokens embeddings and hidden\_size is the hidden size (embedding size) of the model.

### Hugging Face Transformers Inputs[¶](#hugging-face-transformers-inputs "Permanent link")

You can pass prompt embeddings from Hugging Face Transformers models to the `'prompt_embeds'` field of the prompt embedding dictionary, as shown in the following examples:

[examples/features/prompt\_embed/prompt\_embed\_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/features/prompt_embed/prompt_embed_offline.py)

## Online Serving[¶](#online-serving "Permanent link")

Our OpenAI-compatible server accepts prompt embeddings inputs via both the [Completions API](https://platform.openai.com/docs/api-reference/completions) and the [Chat Completions API](https://platform.openai.com/docs/api-reference/chat). Both are enabled by the `--enable-prompt-embeds` flag in `vllm serve`.

### Completions API[¶](#completions-api "Permanent link")

Prompt embeddings inputs are added via a `'prompt_embeds'` key in the JSON request body.

When a mixture of `'prompt_embeds'` and `'prompt'` inputs are provided in a single request, the prompt embeds are always returned first.

Prompt embeddings are passed in as base64 encoded torch tensors.

The Completions endpoint does **not** apply a chat template to `prompt_embeds`. If the model assumes some chat template, the caller is responsible for producing embeddings for the full, already-templated prompt: apply the chat template, then embed the resulting token IDs. Anything the model would normally need (system prompt, role markers, generation prompt, etc.) must already be baked into the embedded tokens.

### Chat Completions API[¶](#chat-completions-api "Permanent link")

Prompt embeddings can be included as content parts in chat messages, interleaved with text:

```
{
"messages":[
{
"role":"system",
"content":[
{"type":"text","text":"You are a helpful assistant."},
{"type":"prompt_embeds","data":"<base64_encoded_tensor>"}
]
},
{
"role":"user",
"content":[
{"type":"prompt_embeds","data":"<base64_encoded_tensor>"},
{"type":"text","text":"Summarize the above."}
]
}
]
}
```

Each `prompt_embeds` content part contains a `data` field with a base64-encoded `torch.Tensor` of shape `(num_tokens, hidden_size)`. Multiple `prompt_embeds` parts can appear in any message, in any position relative to text parts. The server expands each part into the correct number of placeholder tokens during chat template rendering, then splices the pre-computed embeddings into the model's input at the corresponding positions.

Unlike the Completions API, a `prompt_embeds` content part should encode **only** the content, not a templated conversation. The server wraps the chat template around the embedded content at request time, the same way it would for a plain text `content` string. Embedding a full templated conversation here would double-apply the template and produce incorrect inputs to the model.

Warning

The vLLM engine may crash if incorrect shape of embeddings is passed. Only enable this flag for trusted users!

### Transformers Inputs via OpenAI Client[¶](#transformers-inputs-via-openai-client "Permanent link")

First, launch the OpenAI-compatible server:

```
vllmservemeta-llama/Llama-3.2-1B-Instruct--runnergenerate\
--max-model-len4096--enable-prompt-embeds
```

Then, you can use the OpenAI client as follows:

[examples/features/prompt\_embed/prompt\_embed\_inference\_with\_openai\_client.py](https://github.com/vllm-project/vllm/blob/main/examples/features/prompt_embed/prompt_embed_inference_with_openai_client.py)