---
title: Cerebras
url: https://docs.getbifrost.ai/providers/supported-providers/cerebras.md
source: llms
fetched_at: 2026-01-21T19:44:28.680894131-03:00
rendered_js: false
word_count: 558
summary: This document outlines the integration of the Cerebras API into an OpenAI-compatible framework, detailing supported features like chat completions, streaming, and tool calling alongside specific parameter mappings.
tags:
    - cerebras
    - openai-compatibility
    - chat-completions
    - streaming
    - tool-calling
    - api-integration
    - text-completions
category: reference
---

# Cerebras

> Cerebras API conversion guide - OpenAI-compatible format, full feature support, streaming, tool calling, and parameter handling

## Overview

Cerebras is a **fully OpenAI-compatible provider** leveraging the complete set of OpenAI API features. Bifrost delegates all functionality to the OpenAI provider implementation with standard parameter filtering. Key characteristics:

* **Complete OpenAI compatibility** - All chat, text, and streaming features supported
* **Full tool calling** - Function definitions and parallel tool execution
* **Streaming support** - Server-Sent Events with token usage tracking
* **Parameter preservation** - Passes through all standard OpenAI parameters
* **Responses API** - Full support with format conversion

### Supported Operations

| Operation            | Non-Streaming | Streaming | Endpoint               |
| -------------------- | ------------- | --------- | ---------------------- |
| Chat Completions     | ✅             | ✅         | `/v1/chat/completions` |
| Responses API        | ✅             | ✅         | `/v1/chat/completions` |
| Text Completions     | ✅             | ✅         | `/v1/completions`      |
| List Models          | ✅             | -         | `/v1/models`           |
| Embeddings           | ❌             | ❌         | -                      |
| Image Generation     | ❌             | ❌         | -                      |
| Speech (TTS)         | ❌             | ❌         | -                      |
| Transcriptions (STT) | ❌             | ❌         | -                      |
| Files                | ❌             | ❌         | -                      |
| Batch                | ❌             | ❌         | -                      |

<Note>
  **Unsupported Operations** (❌): Embeddings, Image Generation, Speech, Transcriptions, Files, and Batch are not supported by the upstream Cerebras API. These return `UnsupportedOperationError`.
</Note>

***

# 1. Chat Completions

## Request Parameters

Cerebras supports all standard OpenAI chat completion parameters. For full parameter reference and behavior, see [OpenAI Chat Completions](/providers/supported-providers/openai#1-chat-completions).

### Filtered Parameters

Removed for Cerebras compatibility:

* `prompt_cache_key` - Not supported
* `verbosity` - Anthropic-specific
* `store` - Not supported
* `service_tier` - OpenAI-specific

### Reasoning Parameter

Cerebras delegates to OpenAI via `ToOpenAIChatRequest`, so reasoning parameters are transformed: `reasoning.effort` values (e.g., `minimal` → `low`) are mapped per the OpenAI-compatible providers convention, and `reasoning.max_tokens` is cleared/omitted (removed during conversion).

Cerebras supports all standard OpenAI message types, tools, responses, and streaming formats. For details on message handling, tool conversion, responses, and streaming, refer to [OpenAI Chat Completions](/providers/supported-providers/openai#1-chat-completions).

***

# 2. Responses API

Bifrost converts Responses API format to Chat Completions internally, then converts response back:

```
BifrostResponsesRequest
  → ToChatRequest()
  → ChatCompletion
  → ToBifrostResponsesResponse()
```

Same parameter support as Chat Completions with response format differences (output items instead of message content).

***

# 3. Text Completions

Cerebras supports legacy text completion API:

| Parameter     | Mapping        |
| ------------- | -------------- |
| `prompt`      | Sent as-is     |
| `max_tokens`  | max\_tokens    |
| `temperature` | temperature    |
| `top_p`       | top\_p         |
| `stop`        | stop sequences |

Response returns `choices[].text` with completion text.

***

# 4. Text Completions Streaming

Streaming text completions use same SSE format as chat streaming.

***

# 5. List Models

Lists available models from Cerebras with capabilities and context length information.

***

## Unsupported Features

| Feature           | Reason                      |
| ----------------- | --------------------------- |
| Embedding         | Not offered by Cerebras API |
| Image Generation  | Not offered by Cerebras API |
| Speech/TTS        | Not offered by Cerebras API |
| Transcription/STT | Not offered by Cerebras API |
| Batch Operations  | Not offered by Cerebras API |
| File Management   | Not offered by Cerebras API |

***

## Caveats

<Accordion title="User Field Size Limit">
  **Severity**: Low
  **Behavior**: User field > 64 characters is silently dropped
  **Impact**: Longer user identifiers are lost
  **Code**: SanitizeUserField enforces 64-char max
</Accordion>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt