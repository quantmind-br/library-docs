---
title: Structured Outputs - Fireworks AI Docs
url: https://docs.fireworks.ai/structured-responses/structured-response-formatting
source: sitemap
fetched_at: 2026-04-27T20:18:09.815356678-03:00
rendered_js: false
word_count: 278
summary: This document details how to enforce structured outputs from model responses in Fireworks, supporting both JSON mode (using predefined schemas or general JSON objects) and Grammar mode. It also explains the advanced feature of reasoning mode for inspecting model thought processes.
tags:
    - structured-output
    - json-mode
    - grammar-mode
    - pydantic
    - schema
    - reasoning
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Structured outputs ensure model responses conform to your specified format. Fireworks supports two methods: **JSON mode** (using JSON schemas) and **Grammar mode** (using custom BNF grammars).

## Quick Start

Force model output to conform to a [JSON schema](https://json-schema.org/):

```python
import os
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(
    api_key=os.environ.get("FIREWORKS_API_KEY"),
    base_url="https://api.fireworks.ai/inference/v1"
)

# Define your schema
class Result(BaseModel):
    winner: str

# Make the request
response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2p5",
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "Result",
            "schema": Result.model_json_schema()
        }
    },
    messages=[{
        "role": "user",
        "content": "Who won the US presidential election in 2012? Reply in JSON format."
    }]
)

print(response.choices[0].message.content)
# Output: {"winner": "Barack Obama"}
```

## Response Format Options

| Option | Description |
|---|---|
| `json_object` | Force any valid JSON output (no specific schema) |
| `json_schema` | Enforce a specific JSON schema (recommended) |

## JSON Schema Support

**Supported:**

- Types: `string`, `number`, `integer`, `boolean`, `object`, `array`, `null`
- Object constraints: `properties`, `required`
- Array constraints: `items`
- Nested schemas: `anyOf`, `$ref`

**Not yet supported:**

- `oneOf` composition
- Length/size constraints (`minLength`, `maxLength`, `minItems`, `maxItems`)
- Regular expressions (`pattern`)

## Reasoning Model JSON Mode

Some models support structured JSON outputs alongside their reasoning process. The [[094-tools-sdks-python-sdk|Fireworks Python SDK]] exposes reasoning via the `reasoning_content` field, keeping it separate from the JSON output in the `content` field.

```python
import json
from fireworks import Fireworks
from pydantic import BaseModel

client = Fireworks()

# Define the output schema
class QAResult(BaseModel):
    question: str
    answer: str

# Include the schema in the prompt to preserve reasoning
schema = QAResult.model_json_schema()

response = client.chat.completions.create(
    model="accounts/fireworks/models/kimi-k2p5",
    messages=[{
        "role": "user",
        "content": (
            "Who wrote 'Pride and Prejudice'?\n\n"
            f"Reply in JSON matching this schema:\n{json.dumps(schema, indent=2)}"
        )
    }],
    max_tokens=1000
)

# The Fireworks SDK separates reasoning into its own field
reasoning = response.choices[0].message.reasoning_content
content = response.choices[0].message.content

# Strip markdown code fences if the model wraps the JSON
json_str = content.strip()
if json_str.startswith("```"):
    json_str = json_str.split("\n", 1)[1].rsplit("```", 1)[0].strip()

# Parse into Pydantic model
qa_result = QAResult.model_validate_json(json_str)

if reasoning:
    print("Reasoning:", reasoning)
print("Result:", qa_result.model_dump_json(indent=2))
```

> [!tip] Reasoning mode use cases:
> - **Debugging**: Understanding why the model generated specific outputs
> - **Auditing**: Documenting the decision-making process
> - **Complex tasks**: Scenarios where the reasoning is as valuable as the final answer

See [[078-guides-reasoning]] for more on working with reasoning models.

## Grammar Mode

For advanced use cases where JSON isn't sufficient, use Grammar mode to constrain outputs using custom BNF grammars. Grammar mode is ideal for:

- **Classification tasks** – Limit output to a predefined list of options
- **Language-specific output** – Force output in specific languages or character sets
- **Custom formats** – Define arbitrary output structures beyond JSON

[Learn more about Grammar mode →](https://docs.fireworks.ai/structured-responses/structured-output-grammar-based)

See [[069-guides-function-calling]] for multi-turn capabilities and routing across multiple schemas.

#structured-output #json-mode #grammar-mode #pydantic
