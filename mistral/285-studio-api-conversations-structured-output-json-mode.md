---
title: JSON Mode | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/structured-output/json_mode
source: sitemap
fetched_at: 2026-04-26T04:12:41.268329135-03:00
rendered_js: false
word_count: 94
summary: Enable JSON mode in the Mistral API to ensure model outputs are consistently returned as valid JSON objects.
tags:
    - json-mode
    - api-configuration
    - response-formatting
    - mistral-api
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# JSON Mode

Set `response_format` to `{"type": "json_object"}` to ensure the model always returns valid JSON.

> [!tip] Still recommend explicitly asking for JSON in your prompt and specifying the format.

## Usage

```python
response = client.chat(
    model="mistral-large-latest",
    messages=[
        {"role": "system", "content": "You always return valid JSON."},
        {"role": "user", "content": "Return a JSON object with fields 'name' (string) and 'age' (number)"}
    ],
    response_format={"type": "json_object"}
)
```

## Output

```json
{
    "content": "{\"name\": \"Alice\", \"age\": 30}"
}
```

The `content` field is a stringified JSON object.

## Example

```python
# Request
response = client.chat(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "Return user's info as JSON with name and age fields"}],
    response_format={"type": "json_object"}
)

# Response content will be a JSON string like: '{"name": "John", "age": 25}'
result = json.loads(response.choices[0].message.content)
```

> [!warning] JSON mode does not guarantee adherence to a specific schema. For stricter format enforcement, use [Custom Structured Outputs](https://docs.mistral.ai/studio-api/conversations/structured-output/custom).

#json-mode #api-configuration #response-formatting #mistral-api
