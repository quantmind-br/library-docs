---
title: Chat
url: https://docs.mistral.ai/api/endpoint/chat
source: sitemap
fetched_at: 2026-04-26T04:02:03.147222827-03:00
rendered_js: false
word_count: 622
summary: API specification for the chat completions endpoint, including configuration options for model behavior, streaming, and tool usage.
tags:
    - api-reference
    - chat-completions
    - llm-parameters
    - rest-api
    - inference-configuration
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## POST /v1/chat/completions

Generate chat completions with configurable parameters.

### Parameters

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `frequency_penalty` | number | `0` | Penalizes token repetition based on frequency |
| `guardrails` | array | null | Guardrail configurations |
| `max_tokens` | integer | - | Maximum tokens (prompt + max_tokens cannot exceed context length) |
| `messages` | array | - | Prompt as list of dict with role and content |
| `n` | integer | - | Completions per request (input tokens billed once) |
| `parallel_tool_calls` | boolean | `true` | Enable parallel function calling |
| `prediction` | Prediction\|null | - | Expected completion for optimization |
| `presence_penalty` | number | `0` | Penalizes repetition to increase variety |
| `prompt_mode` | object | - | High-level intent for system prompt |
| `random_seed` | integer\|null | - | Seed for deterministic sampling |
| `reasoning_effort` | "high"\|"none" | - | Reasoning effort level |
| `response_format` | ResponseFormat\|null | - | Output format (text, JSON object, JSON schema) |
| `safe_prompt` | boolean | `false` | Inject safety prompt |
| `stop` | string\|array | - | Stop token(s) |
| `stream` | boolean | `false` | Stream partial progress |
| `temperature` | number | - | Sampling temperature (0.0-0.7 recommended) |
| `tool_choice` | ToolChoice\|"auto"\|"none"\|"any"\|"required" | - | Tool selection mode |
| `top_p` | number | `1` | Nucleus sampling threshold |
| `model` | string | - | Model identifier |

### Response Formats

- `200 (application/json)` — Full completion
- `200 (text/event-stream)` — Streaming tokens

### Code Examples

```typescript
import{Mistral}from"@mistralai/mistralai";
const mistral = new Mistral({ apiKey: "MISTRAL_API_KEY" });

async function run() {
  const result = await mistral.chat.complete({
    model: "mistral-small-latest",
    messages: [{ content: "Who is the best French painter?", role: "user" }],
  });
  console.log(result);
}
run();
```

```python
from mistralai import Mistral
import os

with Mistral(api_key=os.getenv("MISTRAL_API_KEY","")) as mistral:
    res = mistral.chat.complete(
        model="mistral-small-latest",
        messages=[{"content": "Who is the best French painter?", "role": "user"}],
        stream=False
    )
    print(res)
```

```bash
curl https://api.mistral.ai/v1/chat/completions \
  -X POST \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
  -H 'Content-Type: application/json' \
  -d '{"messages": [{"content": "ipsum eiusmod"}], "model": "mistral-large-latest"}'
```

### Response Example

```json
{
  "choices": [{"finish_reason": "stop", "index": "0", "message": {}}],
  "created": "1702256327",
  "id": "cmpl-e5cc70bb28c444948073e77776eb30ef",
  "model": "mistral-small-latest",
  "object": "chat.completion",
  "usage": {}
}
```

#chat-completions #llm-parameters #rest-api
