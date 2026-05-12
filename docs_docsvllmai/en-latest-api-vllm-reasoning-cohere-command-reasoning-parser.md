---
title: cohere_command_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/cohere_command_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:34:54.911951623-03:00
rendered_js: false
word_count: 545
summary: This document defines data structures and helper utilities for normalizing tool definitions, structural tags, and JSON schema extraction within the vLLM Cohere reasoning parser.
tags:
    - vllm
    - cohere
    - json-schema
    - tool-definition
    - data-normalization
    - parser
category: reference
---

Bases: `TypedDict`

A tool definition normalized to the shape `collect_tool_schema` expects.

`parameters` is a JSON Schema object (possibly empty) describing the tool's call signature.

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
classCohereNormalizedTool(TypedDict):
"""A tool definition normalized to the shape ``collect_tool_schema`` expects.

    ``parameters`` is a JSON Schema object (possibly empty) describing the tool's
    call signature.
    """

    name: str
    parameters: dict[str, Any]
```

## CohereTagRegistry [¶](#vllm.reasoning.cohere_command_reasoning_parser.CohereTagRegistry "Permanent link")

Bases: `NamedTuple`

A single `structural_tag` begin("trigger")/end pair.

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
classCohereTagRegistry(NamedTuple):
"""A single ``structural_tag`` begin("trigger")/end pair."""

    trigger: str
    end: str
```

Bases: `NamedTuple`

The structural tags style for a given model architecture.

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
classCohereTagStyle(NamedTuple):
"""The structural tags style for a given model architecture."""

    json: CohereTagRegistry
    tools: CohereTagRegistry
```

True when `tools` contains at least one tool definition to convert.

`ResponsesRequest` defaults `tools` to `[]`; `ChatCompletionRequest` uses `None`. Both mean "no tools" here. Strings (e.g. a JSON blob) are treated as effective only when non-blank.

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
def_has_effective_tools(
    tools: str | list[Any] | None,
) -> TypeGuard[str | list[Any]]:
"""
    True when ``tools`` contains at least one tool definition to convert.

    ``ResponsesRequest`` defaults ``tools`` to ``[]``; ``ChatCompletionRequest``
    uses ``None``. Both mean "no tools" here. Strings (e.g. a JSON blob) are
    treated as effective only when non-blank.
    """
    if tools is None:
        return False
    if isinstance(tools, str):
        return bool(tools.strip())
    return len(tools) > 0
```

## \_maybe\_parse\_json\_dict [¶](#vllm.reasoning.cohere_command_reasoning_parser._maybe_parse_json_dict "Permanent link")

```
_maybe_parse_json_dict(value: Any) -> dict | None
```

If value is a JSON string, parse to dict; otherwise require dict.

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
def_maybe_parse_json_dict(value: Any) -> dict | None:
"""If value is a JSON string, parse to dict; otherwise require dict."""
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except (TypeError, json.JSONDecodeError):
            return None
        return parsed if isinstance(parsed, dict) else None
    return None
```

## \_schema\_dict\_from\_chat\_response\_format [¶](#vllm.reasoning.cohere_command_reasoning_parser._schema_dict_from_chat_response_format "Permanent link")

```
_schema_dict_from_chat_response_format(
    rf: AnyResponseFormat | dict | None,
) -> dict | None
```

JSON schema dict from Chat Completions `request.response_format` only.

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
def_schema_dict_from_chat_response_format(
    rf: AnyResponseFormat | dict | None,
) -> dict | None:
"""JSON schema dict from Chat Completions ``request.response_format`` only."""
    if rf is None:
        return None
    rf_type = _response_format_type(rf)
    if rf_type == "json_object":
        return {"type": "object"}
    if rf_type != "json_schema":
        return None
    js_wr = (
        rf.get("json_schema")
        if isinstance(rf, dict)
        else getattr(rf, "json_schema", None)
    )
    return _schema_from_json_schema_field(js_wr)
```

## \_schema\_dict\_from\_structured\_outputs [¶](#vllm.reasoning.cohere_command_reasoning_parser._schema_dict_from_structured_outputs "Permanent link")

Schema dict from `structured_outputs` (`json` / `json_object`).

Same unwrapping as `json_schema`. `json` is expected to be `str` or `dict` (enforced by `StructuredOutputsParams` / request models); other types raise `ValueError` only if a caller bypasses that validation.

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
def_schema_dict_from_structured_outputs(
    so: StructuredOutputsParams | None,
) -> dict | None:
"""Schema dict from ``structured_outputs`` (``json`` / ``json_object``).

    Same unwrapping as ``json_schema``. ``json`` is expected to be ``str`` or
    ``dict`` (enforced by ``StructuredOutputsParams`` / request models); other
    types raise ``ValueError`` only if a caller bypasses that validation.
    """
    if so is None:
        return None
    if so.json_object:
        return {"type": "object"}
    raw: Any = so.json
    if raw is None:
        return None

    if hasattr(raw, "model_dump"):
        out = _schema_from_json_schema_field(raw)
        if out is None:
            raise ValueError(
                "structured_outputs.json model has no extractable JSON Schema."
            )
        return out

    if isinstance(raw, str):
        if not raw.strip():
            raise ValueError("structured_outputs.json cannot be empty.")
        try:
            raw = json.loads(raw)
        except json.JSONDecodeError as e:
            raise ValueError("structured_outputs.json must be valid JSON.") frome
        if not isinstance(raw, dict):
            raise ValueError("structured_outputs.json must decode to a JSON object.")

    if isinstance(raw, Mapping):
        body = raw if isinstance(raw, dict) else dict(raw)
        return _schema_from_json_schema_field(body) or body

    raise ValueError(
        f"structured_outputs.json has unsupported type {type(raw).__name__}."
    )
```

## \_schema\_from\_json\_schema\_field [¶](#vllm.reasoning.cohere_command_reasoning_parser._schema_from_json_schema_field "Permanent link")

```
_schema_from_json_schema_field(js_wr: Any) -> dict | None
```

Extract the JSON Schema object from Chat Completions `json_schema` payload.

Accepts: - `JsonSchemaResponseFormat` (Pydantic) with `schema` / `json_schema` field - dict in OpenAI shape `{"name": ..., "schema": {...}}` - dict with `json_schema` key holding either the schema or a nested wrapper - dict that is already a JSON Schema document (some clients omit the wrapper) - JSON strings for any of the above

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
def_schema_from_json_schema_field(js_wr: Any) -> dict | None:
"""
    Extract the JSON Schema object from Chat Completions ``json_schema`` payload.

    Accepts:
    - ``JsonSchemaResponseFormat`` (Pydantic) with ``schema`` / ``json_schema`` field
    - dict in OpenAI shape ``{"name": ..., "schema": {...}}``
    - dict with ``json_schema`` key holding either the schema or a nested wrapper
    - dict that is already a JSON Schema document (some clients omit the wrapper)
    - JSON strings for any of the above
    """
    if js_wr is None:
        return None

    parsed_wr = _maybe_parse_json_dict(js_wr)
    if parsed_wr is not None:
        js_wr = parsed_wr

    if hasattr(js_wr, "model_dump"):
        for by_alias in (True, False):
            try:
                data = js_wr.model_dump(by_alias=by_alias, exclude_none=False)
            except TypeError:
                data = js_wr.model_dump(by_alias=by_alias)
            out = _unwrap_nested_schema(data.get("schema") or data.get("json_schema"))
            if out is not None:
                return out
        inner_attr = getattr(js_wr, "json_schema", None)
        return inner_attr if isinstance(inner_attr, dict) else None

    if isinstance(js_wr, dict):
        for key in ("schema", "json_schema"):
            out = _unwrap_nested_schema(js_wr.get(key))
            if out is not None:
                return out
        return js_wr

    return None
```

Build the list of `CohereNormalizedTool` dicts expected by `collect_tool_schema`.

Accepts: - JSON string - list of dicts with top-level `name` / `parameters` - list of Chat Completions-style `{"type": "function", "function": {...}}` - list of Pydantic models with `model_dump()`

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
def_tool_definitions_to_schema_list(
    tools: str | list[Any],
) -> list[CohereNormalizedTool]:
"""
    Build the list of ``CohereNormalizedTool`` dicts expected by
    ``collect_tool_schema``.

    Accepts:
    - JSON string
    - list of dicts with top-level ``name`` / ``parameters``
    - list of Chat Completions-style ``{"type": "function", "function": {...}}``
    - list of Pydantic models with ``model_dump()``
    """
    if isinstance(tools, str):
        try:
            parsed = json.loads(tools)
        except json.JSONDecodeError:
            return []
        if not isinstance(parsed, list):
            return []
    else:
        parsed = list(tools)

    out: list[CohereNormalizedTool] = []
    for raw in parsed:
        t = raw.model_dump() if hasattr(raw, "model_dump") else raw
        if not isinstance(t, dict):
            continue
        # Unwrap Chat Completions' ``{"type": "function", "function": {...}}``
        # shape; otherwise take the dict as-is.
        if t.get("type") == "function" and isinstance(t.get("function"), dict):
            t = t["function"]
        name = t.get("name")
        if not isinstance(name, str):
            continue
        params = t.get("parameters")
        out.append(
            CohereNormalizedTool(
                name=name,
                parameters=params if isinstance(params, dict) else {},
            )
        )
    return out
```

## \_unwrap\_nested\_schema [¶](#vllm.reasoning.cohere_command_reasoning_parser._unwrap_nested_schema "Permanent link")

```
_unwrap_nested_schema(candidate: Any) -> dict | None
```

Return `candidate` as a dict, unwrapping a nested `schema` if present.

Returns `None` if `candidate` is not (and cannot be parsed into) a dict.

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
def_unwrap_nested_schema(candidate: Any) -> dict | None:
"""Return ``candidate`` as a dict, unwrapping a nested ``schema`` if present.

    Returns ``None`` if ``candidate`` is not (and cannot be parsed into) a dict.
    """
    cand = _maybe_parse_json_dict(candidate)
    if not isinstance(cand, dict):
        return None
    nested = cand.get("schema")
    return nested if isinstance(nested, dict) else cand

collect_tool_schema(
    tool_schema: list[CohereNormalizedTool],
) -> str
```

Build an xgrammar EBNF grammar that matches a JSON array of tool calls.

The grammar shape is architecture-independent; callers are responsible for wrapping it in the correct structural tag (see `CohereTagStyle.tools`).

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
defcollect_tool_schema(tool_schema: list[CohereNormalizedTool]) -> str:
"""Build an xgrammar EBNF grammar that matches a JSON array of tool calls.

    The grammar shape is architecture-independent; callers are responsible for
    wrapping it in the correct structural tag (see ``CohereTagStyle.tools``).
    """
    tool_dictionary: dict[str, str] = {}
    for tool in tool_schema:
        tool_name = tool["name"]
        tool_parameters = json.dumps(tool["parameters"])
        json_schema = f"""{{
                        "type": "object",
                        "properties": {{
                            "tool_call_id": {{
                                "type": "string",
                                "pattern": "^[0-9]+$"
}},
                            "tool_name": {{
                                "type": "string",
                                "const": "{tool_name}"
}},
                            "parameters": {tool_parameters}
}}
}}"""
        tool_grammar = str(xgr.Grammar.from_json_schema(json_schema))
        for match in re.findall(r"\b(\w+)\s*::=", tool_grammar):
            tool_grammar = re.sub(
                rf"\b{re.escape(match)}\b", tool_name + match, tool_grammar
            )
        tool_dictionary[tool_name] = f"{tool_name} ::= {tool_name}root\n{tool_grammar}"
    # Emitted grammar shape:
    #   root  ::= tools
    #   tools ::= ws "[" ws tool ws ("," ws tool)* ws "]" ws
    #   ws    ::= (" " | "\t" | "\n")*
    #   tool  ::= <tool_a> | <tool_b> | ...         (one alternative per input)
    #   <tool_x>     ::= <tool_x>root               (per-tool xgrammar rules)
    #   <tool_x>root ::= ...                        (from xgr.Grammar.from_json_schema)
    tool_alternatives = "tool ::= " + " | ".join(tool_dictionary.keys())
    tool_rules = "\n    ".join(tool_dictionary.values())
    grammar = f"""root ::= tools
    tools ::= ws "[" ws tool ws ("," ws tool)*  ws "]" ws
    ws    ::= (" " | "\\t" | "\\n")*
{tool_alternatives}
{tool_rules}
    """
    return grammar

convert_schema_to_structural_tags(
    schema: dict | None = None,
    tools: str | list[Any] | None = None,
    model_architecture: str | None = None,
) -> str | None
```

Returns a response\_format string accepted by xgrammar's structural tag format. Uses the canonical shape: {"type": "structural\_tag", "format": {...}} with format.type "triggered\_tags" and tag content type "json\_schema" or "grammar".

Callers that are not on an engine path (e.g. the reasoning parser) must pass `model_architecture` explicitly.

Source code in `vllm/reasoning/cohere_command_reasoning_parser.py`

```
defconvert_schema_to_structural_tags(
    schema: dict | None = None,
    tools: str | list[Any] | None = None,
    model_architecture: str | None = None,
) -> str | None:
"""
    Returns a response_format string accepted by xgrammar's structural tag format.
    Uses the canonical shape: {"type": "structural_tag", "format": {...}} with
    format.type "triggered_tags" and tag content type "json_schema" or "grammar".

    Callers that are not on an engine path (e.g. the reasoning parser) must pass
    ``model_architecture`` explicitly.
    """
    if model_architecture is None or model_architecture not in MODEL_TO_TAG_STYLE:
        return None
    style = MODEL_TO_TAG_STYLE[model_architecture]

    tags: list[dict] = []

    def_add_tag(tag: CohereTagRegistry, content: dict) -> None:
        tags.append({"begin": tag.trigger, "content": content, "end": tag.end})

    if schema is not None:
        # Add the JSON-schema tag both for schema-only requests and for the
        # "tools plus JSON mode" case (North use case: follow the schema when
        # the model decides not to call any tool).
        _add_tag(style.json, {"type": "json_schema", "json_schema": schema})

    if _has_effective_tools(tools):
        # ``tools`` may be a JSON string (poseidon / RESPONSE_FORMAT_TOOL_DEFINITIONS)
        # or a list (Chat Completions ``request.tools`` as Pydantic models or dicts).
        tool_schema_list = _tool_definitions_to_schema_list(tools)
        if not tool_schema_list:
            raise ValueError(
                "No valid tool definitions could be parsed from the request for "
                "structural tag conversion."
            )
        tool_grammar = collect_tool_schema(tool_schema_list)
        _add_tag(style.tools, {"type": "grammar", "grammar": tool_grammar})

    if not tags:
        return None
    return json.dumps(
        {
            "type": "structural_tag",
            "format": {
                "type": "triggered_tags",
                "triggers": [t["begin"] for t in tags],
                "tags": tags,
            },
        }
    )
```