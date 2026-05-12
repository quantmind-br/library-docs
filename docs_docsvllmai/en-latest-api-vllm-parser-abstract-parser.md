---
title: abstract_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/parser/abstract_parser/
source: sitemap
fetched_at: 2026-05-07T21:34:26.911257242-03:00
rendered_js: false
word_count: 5
summary: The DelegatingParser class provides a base implementation for combining separate reasoning and tool parsing logic to process complex model outputs and tool calls.
tags:
    - parser-pattern
    - delegation
    - tool-calling
    - reasoning-extraction
    - model-response
    - python-class
category: concept
---

```
classDelegatingParser(Parser):
"""
    A Parser implementation that delegates to separate ReasoningParser and
    ToolParser instances.

    This is the recommended base class for creating model-specific parsers
    that combine existing reasoning and tool parser implementations.
    Subclasses should set `self._reasoning_parser` and `self._tool_parser`
    in their `__init__` method.

    If either parser is None, the corresponding methods will return default
    values (no reasoning extraction, no tool calls).
    """

    defextract_reasoning(
        self,
        model_output: str,
        request: ChatCompletionRequest | ResponsesRequest,
    ) -> tuple[str | None, str | None]:
        if self._reasoning_parser is None:
            return None, model_output
        return self._reasoning_parser.extract_reasoning(model_output, request)

    defextract_response_outputs(
        self,
        *,
        model_output: str,
        model_output_token_ids: Sequence[int],
        request: ResponsesRequest,
        enable_auto_tools: bool = False,
        tool_call_id_type: str = "random",
        logprobs: list[Logprob] | None = None,
    ) -> list[ResponseOutputItem]:
        # First extract reasoning
        reasoning, content = self.extract_reasoning(model_output, request)

        # Then parse tool calls from the content
        tool_calls, content = self._parse_tool_calls(
            request=request,
            content=content,
            enable_auto_tools=enable_auto_tools,
        )

        # Build output items
        outputs: list[ResponseOutputItem] = []

        # Add reasoning item if present
        if reasoning:
            reasoning_item = ResponseReasoningItem(
                id=f"rs_{random_uuid()}",
                summary=[],
                type="reasoning",
                content=[
                    ResponseReasoningTextContent(text=reasoning, type="reasoning_text")
                ],
                status=None,  # NOTE: Only the last output item has status.
            )
            outputs.append(reasoning_item)

        # Add message item if there's content
        if content:
            res_text_part = ResponseOutputText(
                text=content,
                annotations=[],
                type="output_text",
                logprobs=logprobs,
            )
            message_item = ResponseOutputMessage(
                id=f"msg_{random_uuid()}",
                content=[res_text_part],
                role="assistant",
                status="completed",
                type="message",
            )
            outputs.append(message_item)

        if tool_calls:
            # We use a simple counter for history_tool_call_count because
            # we don't track the history of tool calls in the Responses API yet.
            # This means that the tool call index will start from 0 for each
            # request.
            for history_tool_call_cnt, tool_call in enumerate(tool_calls):
                tool_call_item = ResponseFunctionToolCall(
                    id=f"fc_{random_uuid()}",
                    call_id=tool_call.id
                    if tool_call.id
                    else make_tool_call_id(
                        id_type=tool_call_id_type,
                        func_name=tool_call.name,
                        idx=history_tool_call_cnt,
                    ),
                    type="function_call",
                    status="completed",
                    name=tool_call.name,
                    arguments=tool_call.arguments,
                )
                outputs.append(tool_call_item)

        return outputs

    def_get_function_name(
        self, request: ChatCompletionRequest | ResponsesRequest
    ) -> str:
        if request.tool_choice and isinstance(request.tool_choice, ToolChoiceFunction):
            return request.tool_choice.name
        if request.tool_choice and isinstance(
            request.tool_choice, ChatCompletionNamedToolChoiceParam
        ):
            return request.tool_choice.function.name
        raise ValueError("Invalid tool_choice for function name extraction.")

    def_parse_tool_calls(
        self,
        request: ResponsesRequest,
        content: str | None,
        enable_auto_tools: bool,
    ) -> tuple[list[FunctionCall], str | None]:
"""
        TODO(qandrew): merge _parse_tool_calls_from_content
        for ChatCompletions into this function
        Parse tool calls from content based on request tool_choice settings.

        Returns:
            A tuple of (function_calls, remaining_content) if tool calls
            were parsed
        """
        function_calls: list[FunctionCall] = []

        if request.tool_choice and isinstance(
            request.tool_choice,
            (ToolChoiceFunction, ChatCompletionNamedToolChoiceParam),
        ):
            # Forced Function Call
            if content is None:
                return [], None
            function_calls.append(
                FunctionCall(name=self._get_function_name(request), arguments=content)
            )
            return function_calls, None  # Clear content since tool is called.

        if request.tool_choice == "required":
            # Required tool calls - parse JSON
            tool_calls = []
            with contextlib.suppress(ValidationError):
                content = content or ""
                tool_calls = TypeAdapter(list[FunctionDefinition]).validate_json(
                    content
                )
            for tool_call in tool_calls:
                function_calls.append(
                    FunctionCall(
                        name=tool_call.name,
                        arguments=json.dumps(tool_call.parameters, ensure_ascii=False),
                    )
                )
            return function_calls, None  # Clear content since tool is called.

        if (
            self._tool_parser is not None
            and enable_auto_tools
            and (request.tool_choice == "auto" or request.tool_choice is None)
        ):
            # Automatic Tool Call Parsing
            tool_call_info = self._tool_parser.extract_tool_calls(
                content if content is not None else "",
                request=request,  # type: ignore
            )
            if tool_call_info is not None and tool_call_info.tools_called:
                function_calls.extend(
                    FunctionCall(
                        id=tool_call.id,
                        name=tool_call.function.name,
                        arguments=tool_call.function.arguments,
                    )
                    for tool_call in tool_call_info.tool_calls
                )
                remaining_content = tool_call_info.content
                if remaining_content and remaining_content.strip() == "":
                    remaining_content = None
                return function_calls, remaining_content

        # No tool calls
        return [], content

    defadjust_request(
        self, request: ChatCompletionRequest | ResponsesRequest
    ) -> ChatCompletionRequest | ResponsesRequest:
        if self._reasoning_parser is not None:
            request = self._reasoning_parser.adjust_request(request)
        if self._tool_parser is not None:
            request = self._tool_parser.adjust_request(request)
        return request

    defextract_reasoning_streaming(
        self,
        previous_text: str,
        current_text: str,
        delta_text: str,
        previous_token_ids: Sequence[int],
        current_token_ids: Sequence[int],
        delta_token_ids: Sequence[int],
    ) -> DeltaMessage | None:
        if self._reasoning_parser is None:
            return DeltaMessage(content=delta_text)
        return self._reasoning_parser.extract_reasoning_streaming(
            previous_text,
            current_text,
            delta_text,
            previous_token_ids,
            current_token_ids,
            delta_token_ids,
        )

    defextract_tool_calls(
        self,
        model_output: str,
        request: ChatCompletionRequest,
    ) -> ExtractedToolCallInformation:
        if self._tool_parser is None:
            return ExtractedToolCallInformation(
                tools_called=False, tool_calls=[], content=model_output
            )
        return self._tool_parser.extract_tool_calls(model_output, request)

    defextract_tool_calls_streaming(
        self,
        previous_text: str,
        current_text: str,
        delta_text: str,
        previous_token_ids: Sequence[int],
        current_token_ids: Sequence[int],
        delta_token_ids: Sequence[int],
        request: ChatCompletionRequest,
    ) -> DeltaMessage | None:
        if self._tool_parser is None:
            return None
        return self._tool_parser.extract_tool_calls_streaming(
            previous_text,
            current_text,
            delta_text,
            previous_token_ids,
            current_token_ids,
            delta_token_ids,
            request,
        )

    def_extract_tool_calls_streaming(
        self,
        previous_text: str,
        current_text: str,
        delta_text: str,
        previous_token_ids: Sequence[int],
        current_token_ids: Sequence[int],
        delta_token_ids: Sequence[int],
        request: ChatCompletionRequest | ResponsesRequest,
        # The following parameters are used for "required" tool choice parsing and are
        # tracked in StreamState for streaming parsing.
        tool_call_idx: int | None = None,
        tool_call_id_type: str = "random",
        function_name_returned: bool = False,
    ) -> tuple[DeltaMessage | None, bool]:
        assert self._tool_parser is not None
        supports_required_and_named = self._tool_parser.supports_required_and_named
        if (
            supports_required_and_named
            and request.tool_choice
            and isinstance(
                request.tool_choice,
                (ToolChoiceFunction, ChatCompletionNamedToolChoiceParam),
            )
        ):
            delta_message, function_name_returned = extract_named_tool_call_streaming(
                delta_text=delta_text,
                function_name=self._get_function_name(request),
                function_name_returned=function_name_returned,
                tool_call_idx=tool_call_idx,
                tool_call_id_type=tool_call_id_type,
                tokenizer=self.model_tokenizer,
            )
            return delta_message, function_name_returned

        if supports_required_and_named and request.tool_choice == "required":
            delta_message, function_name_returned = (
                extract_required_tool_call_streaming(
                    previous_text=previous_text,
                    current_text=current_text,
                    delta_text=delta_text,
                    function_name_returned=function_name_returned,
                    tool_call_idx=tool_call_idx,
                    tool_call_id_type=tool_call_id_type,
                )
            )
            return delta_message, function_name_returned
        return self.extract_tool_calls_streaming(
            previous_text,
            current_text,
            delta_text,
            previous_token_ids,
            current_token_ids,
            delta_token_ids,
            request,  # type: ignore[arg-type]
        ), False

    defis_reasoning_end(self, input_ids: list[int]) -> bool:
        if self._reasoning_parser is None:
            return False
        return self._reasoning_parser.is_reasoning_end(input_ids)

    defextract_content_ids(self, input_ids: list[int]) -> list[int]:
        if self._reasoning_parser is None:
            return input_ids
        return self._reasoning_parser.extract_content_ids(input_ids)

    def_in_reasoning_phase(self, state: StreamState) -> bool:
        if self._reasoning_parser is None:
            return False
        return not state.reasoning_ended

    def_in_tool_call_phase(self, state: StreamState) -> bool:
        if self._tool_parser is None:
            return False
        return state.reasoning_ended

    defparse_delta(
        self,
        delta_text: str,
        delta_token_ids: list[int],
        request: ChatCompletionRequest | ResponsesRequest,
        prompt_token_ids: list[int] | None = None,
    ) -> DeltaMessage | None:
        state = self._stream_state

        if not state.prompt_reasoning_checked and prompt_token_ids is not None:
            state.prompt_reasoning_checked = True
            if self._reasoning_parser is None or self.is_reasoning_end(
                prompt_token_ids
            ):
                state.reasoning_ended = True

        current_text = state.previous_text + delta_text
        current_token_ids = state.previous_token_ids + delta_token_ids
        delta_message: DeltaMessage | None = None

        # Reasoning extraction
        if self._in_reasoning_phase(state):
            delta_message = self.extract_reasoning_streaming(
                previous_text=state.previous_text,
                current_text=current_text,
                delta_text=delta_text,
                previous_token_ids=state.previous_token_ids,
                current_token_ids=current_token_ids,
                delta_token_ids=delta_token_ids,
            )
            # Hand off remaining content to tool parser
            if self._tool_parser and self.is_reasoning_end(delta_token_ids):
                state.reasoning_ended = True
                current_token_ids = self.extract_content_ids(delta_token_ids)
                if delta_message and delta_message.content:
                    current_text = delta_message.content
                    delta_message.content = None
                else:
                    current_text = ""

        # Tool call extraction
        if self._in_tool_call_phase(state):
            if not state.tool_call_text_started:
                state.tool_call_text_started = True
                state.previous_text = ""
                state.previous_token_ids = []
                delta_text = current_text
                delta_token_ids = current_token_ids

            delta_message, state.function_name_returned = (
                self._extract_tool_calls_streaming(
                    previous_text=state.previous_text,
                    current_text=current_text,
                    delta_text=delta_text,
                    previous_token_ids=state.previous_token_ids,
                    current_token_ids=current_token_ids,
                    delta_token_ids=delta_token_ids,
                    request=request,  # type: ignore[arg-type]
                    tool_call_idx=state.history_tool_call_cnt,
                    tool_call_id_type=state.tool_call_id_type,
                    function_name_returned=state.function_name_returned,
                )
            )
            if (
                delta_message
                and delta_message.tool_calls
                and delta_message.tool_calls[0].id is not None
            ):
                state.history_tool_call_cnt += 1

        # No phase active: pass through as content
        if (
            delta_message is None
            and not self._in_reasoning_phase(state)
            and not self._in_tool_call_phase(state)
        ):
            delta_message = DeltaMessage(content=delta_text)

        state.previous_text = current_text
        state.previous_token_ids = current_token_ids
        return delta_message
```