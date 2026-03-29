---
title: Document - DSPy
url: https://dspy.ai/api/experimental/Document/
source: sitemap
fetched_at: 2026-01-23T08:01:40.541290738-03:00
rendered_js: false
word_count: 489
summary: Defines the experimental Document class in DSPy, which facilitates providing structured text content and metadata for citation-enabled language model interactions.
tags:
    - dspy
    - citations
    - document-class
    - experimental-feature
    - metadata
category: api
---

Bases: `Type`

A document type for providing content that can be cited by language models.

This type represents documents that can be passed to language models for citation-enabled responses, particularly useful with Anthropic's Citations API. Documents include the content and metadata that helps the LM understand and reference the source material.

Attributes:

Name Type Description `data` `str`

The text content of the document

`title` `str | None`

Optional title for the document (used in citations)

`media_type` `Literal['text/plain', 'application/pdf']`

MIME type of the document content (defaults to "text/plain")

`context` `str | None`

Optional context information about the document

Example

```
importdspy
fromdspy.signaturesimport Signature
fromdspy.experimentalimport Document, Citations

classAnswerWithSources(Signature):
'''Answer questions using provided documents with citations.'''
    documents: list[Document] = dspy.InputField()
    question: str = dspy.InputField()
    answer: str = dspy.OutputField()
    citations: Citations = dspy.OutputField()

# Create documents
docs = [
    Document(
        data="The Earth orbits the Sun in an elliptical path.",
        title="Basic Astronomy Facts"
    ),
    Document(
        data="Water boils at 100°C at standard atmospheric pressure.",
        title="Physics Fundamentals",
    )
]

# Use with a citation-supporting model
lm = dspy.LM("anthropic/claude-opus-4-1-20250805")
predictor = dspy.Predict(AnswerWithSources)
result = predictor(documents=docs, question="What temperature does water boil?", lm=lm)
print(result.citations)
```

### Functions[¶](#dspy.experimental.Document-functions "Permanent link")

#### `adapt_to_native_lm_feature(signature: type[Signature], field_name: str, lm: LM, lm_kwargs: dict[str, Any]) -> type[Signature]` `classmethod` [¶](#dspy.experimental.Document.adapt_to_native_lm_feature "Permanent link")

Adapt the custom type to the native LM feature if possible.

When the LM and configuration supports the related native LM feature, e.g., native tool calling, native reasoning, etc., we adapt the signature and `lm_kwargs` to enable the native LM feature.

Parameters:

Name Type Description Default `signature` `type[Signature]`

The DSPy signature for the LM call.

*required* `field_name` `str`

The name of the field in the signature to adapt to the native LM feature.

*required* `lm` `LM`

The LM instance.

*required* `lm_kwargs` `dict[str, Any]`

The keyword arguments for the LM call, subject to in-place updates if adaptation if required.

*required*

Returns:

Type Description `type[Signature]`

The adapted signature. If the custom type is not natively supported by the LM, return the original

`type[Signature]`

signature.

Source code in `dspy/adapters/types/base_type.py`

```
@classmethod
defadapt_to_native_lm_feature(
    cls,
    signature: type["Signature"],
    field_name: str,
    lm: "LM",
    lm_kwargs: dict[str, Any],
) -> type["Signature"]:
"""Adapt the custom type to the native LM feature if possible.

    When the LM and configuration supports the related native LM feature, e.g., native tool calling, native
    reasoning, etc., we adapt the signature and `lm_kwargs` to enable the native LM feature.

    Args:
        signature: The DSPy signature for the LM call.
        field_name: The name of the field in the signature to adapt to the native LM feature.
        lm: The LM instance.
        lm_kwargs: The keyword arguments for the LM call, subject to in-place updates if adaptation if required.

    Returns:
        The adapted signature. If the custom type is not natively supported by the LM, return the original
        signature.
    """
    return signature
```

#### `description() -> str` `classmethod` [¶](#dspy.experimental.Document.description "Permanent link")

Description of the document type for use in prompts.

Source code in `dspy/adapters/types/document.py`

```
@classmethod
defdescription(cls) -> str:
"""Description of the document type for use in prompts."""
    return (
        "A document containing text content that can be referenced and cited. "
        "Include the full text content and optionally a title for proper referencing."
    )
```

Extract all custom types from the annotation.

This is used to extract all custom types from the annotation of a field, while the annotation can have arbitrary level of nesting. For example, we detect `Tool` is in `list[dict[str, Tool]]`.

Source code in `dspy/adapters/types/base_type.py`

```
@classmethod
defextract_custom_type_from_annotation(cls, annotation):
"""Extract all custom types from the annotation.

    This is used to extract all custom types from the annotation of a field, while the annotation can
    have arbitrary level of nesting. For example, we detect `Tool` is in `list[dict[str, Tool]]`.
    """
    # Direct match. Nested type like `list[dict[str, Event]]` passes `isinstance(annotation, type)` in python 3.10
    # while fails in python 3.11. To accommodate users using python 3.10, we need to capture the error and ignore it.
    try:
        if isinstance(annotation, type) and issubclass(annotation, cls):
            return [annotation]
    except TypeError:
        pass

    origin = get_origin(annotation)
    if origin is None:
        return []

    result = []
    # Recurse into all type args
    for arg in get_args(annotation):
        result.extend(cls.extract_custom_type_from_annotation(arg))

    return result
```

#### `format() -> list[dict[str, Any]]` [¶](#dspy.experimental.Document.format "Permanent link")

Format document for LM consumption.

Returns:

Type Description `list[dict[str, Any]]`

A list containing the document block in the format expected by citation-enabled language models.

Source code in `dspy/adapters/types/document.py`

```
defformat(self) -> list[dict[str, Any]]:
"""Format document for LM consumption.

    Returns:
        A list containing the document block in the format expected by citation-enabled language models.
    """
    document_block = {
        "type": "document",
        "source": {
            "type": "text",
            "media_type": self.media_type,
            "data": self.data
        },
        "citations": {"enabled": True}
    }

    if self.title:
        document_block["title"] = self.title

    if self.context:
        document_block["context"] = self.context

    return [document_block]
```

#### `is_streamable() -> bool` `classmethod` [¶](#dspy.experimental.Document.is_streamable "Permanent link")

Whether the custom type is streamable.

Source code in `dspy/adapters/types/base_type.py`

```
@classmethod
defis_streamable(cls) -> bool:
"""Whether the custom type is streamable."""
    return False
```

#### `parse_lm_response(response: str | dict[str, Any]) -> Optional[Type]` `classmethod` [¶](#dspy.experimental.Document.parse_lm_response "Permanent link")

Parse a LM response into the custom type.

Parameters:

Name Type Description Default `response` `str | dict[str, Any]`

A LM response.

*required*

Returns:

Type Description `Optional[Type]`

A custom type object.

Source code in `dspy/adapters/types/base_type.py`

```
@classmethod
defparse_lm_response(cls, response: str | dict[str, Any]) -> Optional["Type"]:
"""Parse a LM response into the custom type.

    Args:
        response: A LM response.

    Returns:
        A custom type object.
    """
    return None
```

#### `parse_stream_chunk(chunk: ModelResponseStream) -> Optional[Type]` `classmethod` [¶](#dspy.experimental.Document.parse_stream_chunk "Permanent link")

Parse a stream chunk into the custom type.

Parameters:

Name Type Description Default `chunk` `ModelResponseStream`

A stream chunk.

*required*

Returns:

Type Description `Optional[Type]`

A custom type object or None if the chunk is not for this custom type.

Source code in `dspy/adapters/types/base_type.py`

```
@classmethod
defparse_stream_chunk(cls, chunk: ModelResponseStream) -> Optional["Type"]:
"""
    Parse a stream chunk into the custom type.

    Args:
        chunk: A stream chunk.

    Returns:
        A custom type object or None if the chunk is not for this custom type.
    """
    return None
```

#### `serialize_model()` [¶](#dspy.experimental.Document.serialize_model "Permanent link")

Source code in `dspy/adapters/types/base_type.py`

```
@pydantic.model_serializer()
defserialize_model(self):
    formatted = self.format()
    if isinstance(formatted, list):
        return (
            f"{CUSTOM_TYPE_START_IDENTIFIER}{json.dumps(formatted,ensure_ascii=False)}{CUSTOM_TYPE_END_IDENTIFIER}"
        )
    return formatted
```

#### `validate_input(data: Any)` `classmethod` [¶](#dspy.experimental.Document.validate_input "Permanent link")

Source code in `dspy/adapters/types/document.py`

```
@pydantic.model_validator(mode="before")
@classmethod
defvalidate_input(cls, data: Any):
    if isinstance(data, cls):
        return data

    # Handle case where data is just a string (data only)
    if isinstance(data, str):
        return {"data": data}

    # Handle case where data is a dict
    elif isinstance(data, dict):
        return data

    raise ValueError(f"Received invalid value for `Document`: {data}")
```