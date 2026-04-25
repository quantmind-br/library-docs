---
title: Structured Response
url: https://lmstudio.ai/docs/python/llm-prediction/structured-response
source: sitemap
fetched_at: 2026-04-07T21:31:06.938115266-03:00
rendered_js: false
word_count: 201
summary: 'This document explains two primary methods for enforcing a structured output format from an LLM: using a class-based schema definition, ideally with libraries like Pydantic, or by providing a direct JSON schema.'
tags:
    - llm-response
    - schema-enforcement
    - pydantic
    - json-schema
    - structured-output
category: guide
---

You can enforce a particular response format from an LLM by providing a JSON schema to the `.respond()` method. This guarantees that the model's output conforms to the schema you provide.

The JSON schema can either be provided directly, or by providing an object that implements the `lmstudio.ModelSchema` protocol, such as `pydantic.BaseModel` or `lmstudio.BaseModel`.

The `lmstudio.ModelSchema` protocol is defined as follows:

```

@runtime_checkable
class ModelSchema(Protocol):
    """Protocol for classes that provide a JSON schema for their model."""

    @classmethod
    def model_json_schema(cls) → DictSchema:
        """Return a JSON schema dict describing this model."""
        ...

```

When a schema is provided, the prediction result's `parsed` field will contain a string-keyed dictionary that conforms to the given schema (for unstructured results, this field is a string field containing the same value as `content`).

## Enforce Using a Class Based Schema Definition[](#enforce-using-a-class-based-schema-definition "Link to 'Enforce Using a Class Based Schema Definition'")

If you wish the model to generate JSON that satisfies a given schema, it is recommended to provide a class based schema definition using a library such as [`pydantic`](https://docs.pydantic.dev/) or [`msgspec`](https://jcristharif.com/msgspec/).

Pydantic models natively implement the `lmstudio.ModelSchema` protocol, while `lmstudio.BaseModel` is a `msgspec.Struct` subclass that implements `.model_json_schema()` appropriately.

#### Define a Class Based Schema

#### Generate a Structured Response

## Enforce Using a JSON Schema[](#enforce-using-a-json-schema "Link to 'Enforce Using a JSON Schema'")

You can also enforce a structured response using a JSON schema.

#### Define a JSON Schema

```

# A JSON schema for a book
schema = {
  "type": "object",
  "properties": {
    "title": { "type": "string" },
    "author": { "type": "string" },
    "year": { "type": "integer" },
  },
  "required": ["title", "author", "year"],
}
```

#### Generate a Structured Response