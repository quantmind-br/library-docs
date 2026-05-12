---
title: structural_tag_registry - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/tool_parsers/structural_tag_registry/
source: sitemap
fetched_at: 2026-05-07T21:36:31.938737324-03:00
rendered_js: false
word_count: 0
summary: This code implements a structural tag builder for the DeepSeek V4 model, defining how tool calls and reasoning triggers are formatted as XML-based structural tokens.
tags:
    - deepseek-v4
    - structural-tags
    - tool-calling
    - xml-formatting
    - function-calling
    - model-integration
category: api
---

```
@register_model_structural_tag("deepseek_v4")
defget_deepseek_v4_structural_tag(
    tools: list[ChatCompletionToolsParam],
    tool_choice: SimplifiedToolChoice,
    reasoning: bool,
) -> StructuralTag:
"""Build DeepSeek V4 structural tags."""

    invoke_begin_prefix = '<｜DSML｜invoke name="'
    invoke_begin_suffix = '">\n'
    invoke_end = "</｜DSML｜invoke>\n"
    tool_calls_prefix = "\n\n"
    function_calls_begin = "<｜DSML｜tool_calls>\n"
    function_calls_end = "</｜DSML｜tool_calls>"
    function_calls_trigger = "<｜DSML｜tool_calls>"
    think_tag_end = "</think>"
    think_exclude_tokens = ["<think>", "</think>"]
    xml_style = "deepseek_xml"

    if tool_choice == "auto":
        tags = []
        for tool in tools:
            function = tool.function
            parameters = _get_function_parameters(function)
            tags.append(
                TagFormat(
                    begin=invoke_begin_prefix + function.name + invoke_begin_suffix,
                    content=JSONSchemaFormat(
                        json_schema=parameters,
                        style=xml_style,
                    ),
                    end=invoke_end,
                )
            )

        if tags:
            function_calling_tags = TagsWithSeparatorFormat(
                tags=tags,
                separator="\n",
                at_least_one=True,
            )
            suffix_tag = TriggeredTagsFormat(
                triggers=[function_calls_trigger],
                tags=[
                    TagFormat(
                        begin=function_calls_begin,
                        content=function_calling_tags,
                        end=function_calls_end,
                    )
                ],
                excludes=think_exclude_tokens,
            )
        else:
            suffix_tag = AnyTextFormat(excludes=think_exclude_tokens)

    elif tool_choice == "forced":
        if not tools:
            raise ValueError("Forced tool choice must resolve to exactly one tool.")
        function = tools[0].function
        suffix_tag = SequenceFormat(
            elements=[
                ConstStringFormat(value=tool_calls_prefix + function_calls_begin),
                TagFormat(
                    begin=invoke_begin_prefix + function.name + invoke_begin_suffix,
                    content=JSONSchemaFormat(
                        json_schema=_get_function_parameters(function),
                        style=xml_style,
                    ),
                    end=invoke_end,
                ),
                ConstStringFormat(value=function_calls_end),
            ]
        )

    elif tool_choice == "required":
        tags = []
        for tool in tools:
            function = tool.function
            parameters = _get_function_parameters(function)
            tags.append(
                TagFormat(
                    begin=invoke_begin_prefix + function.name + invoke_begin_suffix,
                    content=JSONSchemaFormat(
                        json_schema=parameters,
                        style=xml_style,
                    ),
                    end=invoke_end,
                )
            )
        assert len(tags) > 0
        suffix_tag = SequenceFormat(
            elements=[
                ConstStringFormat(value=tool_calls_prefix + function_calls_begin),
                TagsWithSeparatorFormat(
                    tags=tags,
                    separator="\n",
                    at_least_one=True,
                ),
                ConstStringFormat(value=function_calls_end),
            ]
        )

    if not reasoning:
        return StructuralTag(format=suffix_tag)

    prefix_tag = TagFormat(begin="", content=AnyTextFormat(), end=think_tag_end)
    return StructuralTag(format=SequenceFormat(elements=[prefix_tag, suffix_tag]))
```