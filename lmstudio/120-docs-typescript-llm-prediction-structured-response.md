---
title: Structured Response
url: https://lmstudio.ai/docs/typescript/llm-prediction/structured-response
source: sitemap
fetched_at: 2026-04-07T21:31:48.789919288-03:00
rendered_js: false
word_count: 254
summary: This document explains methods for forcing a language model to generate responses conforming to a specific structure, detailing the use of both Zod and standard JSON schemas.
tags:
    - structured-output
    - zod-schema
    - json-schema
    - llm-control
    - response-formatting
category: guide
---

You can enforce a particular response format from an LLM by providing a schema (JSON or `zod`) to the `.respond()` method. This guarantees that the model's output conforms to the schema you provide.

## Enforce Using a `zod` Schema[](#enforce-using-a-zod-schema "Link to 'Enforce Using a ,[object Object], Schema'")

If you wish the model to generate JSON that satisfies a given schema, it is recommended to provide the schema using [`zod`](https://zod.dev/). When a `zod` schema is provided, the prediction result will contain an extra field `parsed`, which contains parsed, validated, and typed result.

#### Define a `zod` Schema

```

import { z } from "zod";

// A zod schema for a book
const bookSchema = z.object({
  title: z.string(),
  author: z.string(),
  year: z.number().int(),
});
```

#### Generate a Structured Response

## Enforce Using a JSON Schema[](#enforce-using-a-json-schema "Link to 'Enforce Using a JSON Schema'")

You can also enforce a structured response using a JSON schema.

#### Define a JSON Schema

```

// A JSON schema for a book
const schema = {
  type: "object",
  properties: {
    title: { type: "string" },
    author: { type: "string" },
    year: { type: "integer" },
  },
  required: ["title", "author", "year"],
};
```

#### Generate a Structured Response

Structured generation works by constraining the model to only generate tokens that conform to the provided schema. This ensures valid output in normal cases, but comes with two important limitations:

- Models (especially smaller ones) may occasionally get stuck in an unclosed structure (like an open bracket), when they "forget" they are in such structure and cannot stop due to schema requirements. Thus, it is recommended to always include a `maxTokens` parameter to prevent infinite generation.
- Schema compliance is only guaranteed for complete, successful generations. If generation is interrupted (by cancellation, reaching the `maxTokens` limit, or other reasons), the output will likely violate the schema. With `zod` schema input, this will raise an error; with JSON schema, you'll receive an invalid string that doesn't satisfy schema.