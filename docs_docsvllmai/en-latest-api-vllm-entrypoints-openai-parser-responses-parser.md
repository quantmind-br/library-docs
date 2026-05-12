---
title: responses_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/parser/responses_parser/
source: sitemap
fetched_at: 2026-05-07T21:20:16.938469133-03:00
rendered_js: false
word_count: 0
summary: This document defines a parser class responsible for processing completion tokens into structured response items, incorporating support for reasoning extraction and tool call handling.
tags:
    - token-parsing
    - reasoning-extraction
    - tool-call-handling
    - completion-tokens
    - response-processing
    - structured-output
category: reference
---

```
classResponsesParser:
"""Incremental parser over completion tokens with reasoning support."""

    def__init__(
        self,
        *,
        tokenizer: TokenizerLike,
        reasoning_parser_cls: type[ReasoningParser],
        response_messages: list[ResponseInputOutputItem],
        request: ResponsesRequest,
        tool_parser_cls: type[ToolParser] | None,
        chat_template: str | None,
        chat_template_content_format: ChatTemplateContentFormatOption,
    ):
        self.response_messages: list[ResponseInputOutputItem] = (
            # TODO: initial messages may not be properly typed
            response_messages
        )
        self.num_init_messages = len(response_messages)
        self.tokenizer = tokenizer
        self.request = request

        self.reasoning_parser_instance = reasoning_parser_cls(
            tokenizer,
            chat_template_kwargs=_effective_chat_template_kwargs(
                request,
                chat_template=chat_template,
                chat_template_content_format=chat_template_content_format,
            ),
        )
        self.tool_parser_instance = None
        if tool_parser_cls is not None:
            self.tool_parser_instance = tool_parser_cls(tokenizer, request.tools)

        # Store the last finish_reason to determine response status
        self.finish_reason: str | None = None

    defprocess(self, output: CompletionOutput) -> "ResponsesParser":
        # Store the finish_reason from the output
        self.finish_reason = output.finish_reason

        reasoning, content = self.reasoning_parser_instance.extract_reasoning(
            output.text, request=self.request
        )
        if reasoning:
            self.response_messages.append(
                ResponseReasoningItem(
                    type="reasoning",
                    id=f"rs_{random_uuid()}",
                    summary=[],
                    content=[
                        Content(
                            type="reasoning_text",
                            text=reasoning,
                        )
                    ],
                )
            )

        function_calls: list[ResponseFunctionToolCall] = []
        if self.tool_parser_instance is not None:
            tool_call_info = self.tool_parser_instance.extract_tool_calls(
                content if content is not None else "",
                request=self.request,  # type: ignore
            )
            if tool_call_info is not None and tool_call_info.tools_called:
                # extract_tool_calls() returns a list of tool calls.
                function_calls.extend(
                    ResponseFunctionToolCall(
                        id=f"fc_{random_uuid()}",
                        call_id=f"call_{random_uuid()}",
                        type="function_call",
                        status="completed",
                        name=tool_call.function.name,
                        arguments=tool_call.function.arguments,
                    )
                    for tool_call in tool_call_info.tool_calls
                )
                content = tool_call_info.content
                if content and content.strip() == "":
                    content = None

        if content:
            self.response_messages.append(
                ResponseOutputMessage(
                    type="message",
                    id=f"msg_{random_uuid()}",
                    status="completed",
                    role="assistant",
                    content=[
                        ResponseOutputText(
                            annotations=[],  # TODO
                            type="output_text",
                            text=content,
                            logprobs=None,  # TODO
                        )
                    ],
                )
            )
        if len(function_calls) > 0:
            self.response_messages.extend(function_calls)

        return self

    defmake_response_output_items_from_parsable_context(
        self,
    ) -> list[ResponseOutputItem]:
"""Given a list of sentences, construct ResponseOutput Items."""
        response_messages = self.response_messages[self.num_init_messages :]
        output_messages: list[ResponseOutputItem] = []
        for message in response_messages:
            if not isinstance(message, ResponseFunctionToolCallOutputItem):
                output_messages.append(message)
            else:
                if len(output_messages) == 0:
                    raise ValueError(
                        "Cannot have a FunctionToolCallOutput before FunctionToolCall."
                    )
                if isinstance(output_messages[-1], ResponseFunctionToolCall):
                    mcp_message = McpCall(
                        id=f"{MCP_PREFIX}{random_uuid()}",
                        arguments=output_messages[-1].arguments,
                        name=output_messages[-1].name,
                        server_label=output_messages[
                            -1
                        ].name,  # TODO: store the server label
                        type="mcp_call",
                        status="completed",
                        output=message.output,
                        # TODO: support error output
                    )
                    output_messages[-1] = mcp_message

        return output_messages
```