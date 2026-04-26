---
title: Custom | Mistral Docs
url: https://docs.mistral.ai/studio-api/conversations/structured-output/custom
source: sitemap
fetched_at: 2026-04-26T04:12:38.898406094-03:00
rendered_js: false
word_count: 187
summary: Enforce specific JSON output formats using Pydantic, Zod, or JSON schemas for consistent response structures.
tags:
    - structured-outputs
    - json-schema
    - pydantic
    - zod
    - model-configuration
    - api-integration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Custom Structured Outputs

Ensure the model provides responses in a specific JSON format by supplying a clear JSON schema.

## Define Structure

### Pydantic

```python
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    year: int
    genres: list[str]
```

### Zod

```typescript
import { z } from "zod";

const BookSchema = z.object({
    title: z.string(),
    author: z.string(),
    year: z.number(),
    genres: z.array(z.string())
});
```

### JSON Schema

```python
book_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "year": {"type": "integer"},
        "genres": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["title", "author", "year"]
}
```

## Use with API

```python
response = client.chat(
    model="mistral-large-latest",
    messages=[{"role": "user", "content": "Return info about the book '1984'"}],
    response_format=Book  # Pydantic model
)
```

## Output Types

| Type | Description |
|------|-------------|
| `schema_constrained` | Raw structured JSON output enforced by schema |

## System Prompt Prepending

When using this method, Mistral automatically prepends guidance to the system prompt:

```
Follow the following schema exactly:
{"type": "json_schema", ...}
```

> [!tip] Add more explanations and iterate on your system prompt to clarify expected schema and behavior.

## Example Response

```python
# Input: "Return info about the book '1984'"

# Output:
{
    "title": "1984",
    "author": "George Orwell",
    "year": 1949,
    "genres": ["dystopian", "political fiction"]
}
```

#structured-outputs #json-schema #pydantic #zod #model-configuration #api-integration
