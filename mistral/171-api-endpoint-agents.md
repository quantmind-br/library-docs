---
title: Agents
url: https://docs.mistral.ai/api/endpoint/agents
source: sitemap
fetched_at: 2026-04-26T04:01:14.662630746-03:00
rendered_js: false
word_count: 436
summary: API specification for the agent completion endpoint, used to generate model responses based on specific agent configurations.
tags:
    - api-reference
    - chat-completion
    - agent-configuration
    - request-parameters
    - rest-api
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## POST /v1/agents/completions

Generate completions using a configured agent.

### Parameters

| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `agent_id` | string | - | **Required.** ID of the agent to use |
| `frequency_penalty` | number | `0` | Penalizes token repetition based on frequency |
| `max_tokens` | integer | - | Maximum tokens (prompt + max_tokens cannot exceed context length) |
| `messages` | array | - | Prompt as list of dict with role and content |
| `n` | integer | - | Completions per request |
| `parallel_tool_calls` | boolean | `true` | Enable parallel function calling |
| `prediction` | Prediction\|null | - | Expected completion for optimization |
| `presence_penalty` | number | `0` | Penalizes repetition to increase variety |
| `prompt_mode` | object | - | High-level intent for system prompt |
| `random_seed` | integer\|null | - | Seed for deterministic sampling |
| `reasoning_effort` | "high"\|"none" | - | Reasoning effort level |
| `response_format` | ResponseFormat\|null | - | Output format |
| `stop` | string\|array | - | Stop token(s) |
| `stream` | boolean | `false` | Stream partial progress |
| `tool_choice` | ToolChoice\|"auto"\|"none"\|"any"\|"required" | - | Tool selection mode |
| `tools` | array | - | List of tools the model may call |

### Code Examples

```typescript
import{Mistral}from"@mistralai/mistralai";
const mistral = new Mistral({ apiKey: "MISTRAL_API_KEY" });

async function run() {
  const result = await mistral.agents.complete({
    messages: [{ content: "Who is the best French painter?", role: "user" }],
    agentId: "<id>",
  });
  console.log(result);
}
run();
```

```python
from mistralai.client import Mistral
import os

with Mistral(api_key=os.getenv("MISTRAL_API_KEY","")) as mistral:
    res = mistral.agents.complete(
        messages=[{"role": "user", "content": "Who is the best French painter?"}],
        agent_id="<id>",
        stream=False,
        response_format={"type": "text"}
    )
    print(res)
```

```bash
curl https://api.mistral.ai/v1/agents/completions \
  -X POST \
  -H 'Authorization: Bearer YOUR_APIKEY_HERE' \
  -H 'Content-Type: application/json' \
  -d '{"agent_id": "ipsum eiusmod", "messages": [{"content": "consequat do"}]}'
```

### Response Example

```json
{
  "id": "cf79f7daaee244b1a0ae5c7b1444424a",
  "object": "chat.completion",
  "model": "mistral-medium-latest",
  "usage": {
    "prompt_tokens": 24,
    "completion_tokens": 27,
    "total_tokens": 51,
    "prompt_audio_seconds": {}
  },
  "created": 1759500534,
  "choices": [{
    "index": 0,
    "message": {
      "content": "Arrr, the scallywag Claude Monet be the finest French painter...",
      "tool_calls": null,
      "prefix": false,
      "role": "assistant"
    },
    "finish_reason": "stop"
  }]
}
```

#agent-configuration #chat-completion #rest-api
