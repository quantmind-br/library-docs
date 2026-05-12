---
title: streaming_events - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/responses/streaming_events/
source: sitemap
fetched_at: 2026-05-07T21:20:33.222785743-03:00
rendered_js: false
word_count: 676
summary: This document describes the streaming event builder architecture for the OpenAI Responses API, utilizing a state machine to manage transitions between content, reasoning, and tool-call states during SSE stream generation.
tags:
    - streaming-events
    - sse
    - state-machine
    - openai-api
    - vllm
    - event-processing
category: concept
---

Streaming SSE event builders for the Responses API.

Pure functions that translate streaming state + delta data into OpenAI Response API SSE events. Used by the streaming event processors in serving.py.

The file is organized as

1. StreamingState dataclass + utility helpers
2. Shared leaf helpers — delta events (take plain strings, no context)
3. Shared leaf helpers — done events (take plain strings, no context)
4. Harmony-specific dispatchers (route ctx/previous\_item → leaf helpers)
5. Harmony-specific tool lifecycle helpers

## SimpleStreamingEventProcessor [¶](#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor "Permanent link")

State-machine processor for the simple (non-Harmony) streaming path.

Core flow

1. Resolve the target state from the delta\_message (CONTENT / REASONING / TOOL\_CALL).
2. If the target state differs from the current one, close\_current() then open() the new state.
3. emit\_delta() produces the incremental events for the state.

State lifecycle

open() -&gt; repeated emit\_delta() -&gt; close\_current()

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
classSimpleStreamingEventProcessor:
"""
    State-machine processor for the simple (non-Harmony) streaming path.

    Core flow:
      1. Resolve the target state from the delta_message
         (CONTENT / REASONING / TOOL_CALL).
      2. If the target state differs from the current one,
         close_current() then open() the new state.
      3. emit_delta() produces the incremental events for the state.

    State lifecycle:
      open()  ->  repeated emit_delta()  ->  close_current()
    """

    _STATE_HANDLERS: ClassVar[dict[_StateType, _StateHandlers]] = {
        _StateType.CONTENT: _StateHandlers(
            emit_simple_content_open,
            emit_simple_content_delta,
            emit_simple_content_done,
        ),
        _StateType.REASONING: _StateHandlers(
            emit_simple_reasoning_open,
            emit_simple_reasoning_delta,
            emit_simple_reasoning_done,
        ),
        _StateType.TOOL_CALL: _StateHandlers(
            emit_simple_tool_call_open,
            emit_simple_tool_call_delta,
            emit_simple_tool_call_done,
        ),
    }

    def__init__(self, state: SimpleStreamingState | None = None) -> None:
        self.state = state or SimpleStreamingState()

    defresolve_target_state(
        self, delta_message: DeltaMessage
    ) -> tuple[_StateType, Any]:
"""
        Decide which state the next delta belongs to.

        Priority: TOOL_CALL > REASONING > CONTENT, fallback to NONE.
        For TOOL_CALL the first tool_call object is also returned so
        callers can detect a switch between consecutive tools.
        """
        if (
            delta_message.tool_calls
            and delta_message.tool_calls[0].function is not None
        ):
            return _StateType.TOOL_CALL, delta_message.tool_calls[0]
        if delta_message.reasoning is not None:
            return _StateType.REASONING, None
        if delta_message.content:
            return _StateType.CONTENT, None
        return _StateType.NONE, None

    defneeds_transition(self, target_state: _StateType, tool_call: Any) -> bool:
"""
        Return True when we must close the current state and open a new one.

        Two cases trigger a transition:
          1. The target state differs from the current state
             (e.g. CONTENT -> TOOL_CALL).
          2. We are already in TOOL_CALL but the next tool_call has a
             different index (multiple consecutive tool calls).
        """
        if self.state.current_state != target_state:
            return True
        return (
            target_state == _StateType.TOOL_CALL
            and tool_call is not None
            and self.state.tool_call_index is not None
            and tool_call.index is not None
            and self.state.tool_call_index != tool_call.index
        )

    defclose_current(self) -> list[StreamingResponsesResponse]:
"""Close the current state and emit its 'done' event sequence."""
        handlers = self._STATE_HANDLERS.get(self.state.current_state)
        if handlers is None:
            return []
        return handlers.done_fn(self.state)

    defopen(
        self, target_state: _StateType, tool_call: Any = None
    ) -> list[StreamingResponsesResponse]:
"""Open a new state and emit its 'added' / 'open' event sequence."""
        handlers = self._STATE_HANDLERS[target_state]
        if target_state == _StateType.TOOL_CALL:
            assert tool_call is not None
            return handlers.open_fn(
                self.state, tool_call.function.name, tool_call.index
            )
        return handlers.open_fn(self.state)

    defemit_delta(
        self,
        delta_message: DeltaMessage,
        output: CompletionOutput,
        get_logprobs: Callable[
            [CompletionOutput], list[response_text_delta_event.Logprob]
        ]
        | None = None,
    ) -> list[StreamingResponsesResponse]:
"""
        Emit incremental events for the current state from the delta.

        Special case: when already in REASONING and the same delta also
        carries content, we emit the reasoning delta, close reasoning,
        open content, and then emit the content delta.
        """
        handlers = self._STATE_HANDLERS[self.state.current_state]
        events: list[StreamingResponsesResponse] = []

        # Special case: reasoning -> content inside a single delta.
        if (
            self.state.current_state == _StateType.REASONING
            and delta_message.reasoning is not None
            and delta_message.content is not None
        ):
            events.extend(handlers.delta_fn(self.state, delta_message.reasoning))
            events.extend(self.close_current())
            events.extend(self.open(_StateType.CONTENT))
            content_handlers = self._STATE_HANDLERS[_StateType.CONTENT]
            logprobs = get_logprobs(output) if get_logprobs else []
            events.extend(
                content_handlers.delta_fn(self.state, delta_message.content, logprobs)
            )
            return events

        if self.state.current_state == _StateType.TOOL_CALL:
            assert delta_message.tool_calls is not None
            tool_call_function = delta_message.tool_calls[0].function
            assert tool_call_function is not None
            if tool_call_function.arguments:
                return handlers.delta_fn(self.state, tool_call_function.arguments)
            return []
        elif self.state.current_state == _StateType.REASONING:
            assert delta_message.reasoning is not None
            return handlers.delta_fn(self.state, delta_message.reasoning)
        elif self.state.current_state == _StateType.CONTENT:
            assert delta_message.content is not None
            logprobs = get_logprobs(output) if get_logprobs else []
            return handlers.delta_fn(self.state, delta_message.content, logprobs)
        return []
```

### close\_current [¶](#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.close_current "Permanent link")

```
close_current() -> list[StreamingResponsesResponse]
```

Close the current state and emit its 'done' event sequence.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defclose_current(self) -> list[StreamingResponsesResponse]:
"""Close the current state and emit its 'done' event sequence."""
    handlers = self._STATE_HANDLERS.get(self.state.current_state)
    if handlers is None:
        return []
    return handlers.done_fn(self.state)
```

### emit\_delta [¶](#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.emit_delta "Permanent link")

Emit incremental events for the current state from the delta.

Special case: when already in REASONING and the same delta also carries content, we emit the reasoning delta, close reasoning, open content, and then emit the content delta.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_delta(
    self,
    delta_message: DeltaMessage,
    output: CompletionOutput,
    get_logprobs: Callable[
        [CompletionOutput], list[response_text_delta_event.Logprob]
    ]
    | None = None,
) -> list[StreamingResponsesResponse]:
"""
    Emit incremental events for the current state from the delta.

    Special case: when already in REASONING and the same delta also
    carries content, we emit the reasoning delta, close reasoning,
    open content, and then emit the content delta.
    """
    handlers = self._STATE_HANDLERS[self.state.current_state]
    events: list[StreamingResponsesResponse] = []

    # Special case: reasoning -> content inside a single delta.
    if (
        self.state.current_state == _StateType.REASONING
        and delta_message.reasoning is not None
        and delta_message.content is not None
    ):
        events.extend(handlers.delta_fn(self.state, delta_message.reasoning))
        events.extend(self.close_current())
        events.extend(self.open(_StateType.CONTENT))
        content_handlers = self._STATE_HANDLERS[_StateType.CONTENT]
        logprobs = get_logprobs(output) if get_logprobs else []
        events.extend(
            content_handlers.delta_fn(self.state, delta_message.content, logprobs)
        )
        return events

    if self.state.current_state == _StateType.TOOL_CALL:
        assert delta_message.tool_calls is not None
        tool_call_function = delta_message.tool_calls[0].function
        assert tool_call_function is not None
        if tool_call_function.arguments:
            return handlers.delta_fn(self.state, tool_call_function.arguments)
        return []
    elif self.state.current_state == _StateType.REASONING:
        assert delta_message.reasoning is not None
        return handlers.delta_fn(self.state, delta_message.reasoning)
    elif self.state.current_state == _StateType.CONTENT:
        assert delta_message.content is not None
        logprobs = get_logprobs(output) if get_logprobs else []
        return handlers.delta_fn(self.state, delta_message.content, logprobs)
    return []
```

### needs\_transition [¶](#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.needs_transition "Permanent link")

```
needs_transition(
    target_state: _StateType, tool_call: Any
) -> bool
```

Return True when we must close the current state and open a new one.

Two cases trigger a transition

1. The target state differs from the current state (e.g. CONTENT -&gt; TOOL\_CALL).
2. We are already in TOOL\_CALL but the next tool\_call has a different index (multiple consecutive tool calls).

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defneeds_transition(self, target_state: _StateType, tool_call: Any) -> bool:
"""
    Return True when we must close the current state and open a new one.

    Two cases trigger a transition:
      1. The target state differs from the current state
         (e.g. CONTENT -> TOOL_CALL).
      2. We are already in TOOL_CALL but the next tool_call has a
         different index (multiple consecutive tool calls).
    """
    if self.state.current_state != target_state:
        return True
    return (
        target_state == _StateType.TOOL_CALL
        and tool_call is not None
        and self.state.tool_call_index is not None
        and tool_call.index is not None
        and self.state.tool_call_index != tool_call.index
    )
```

### open [¶](#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.open "Permanent link")

```
open(
    target_state: _StateType, tool_call: Any = None
) -> list[StreamingResponsesResponse]
```

Open a new state and emit its 'added' / 'open' event sequence.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defopen(
    self, target_state: _StateType, tool_call: Any = None
) -> list[StreamingResponsesResponse]:
"""Open a new state and emit its 'added' / 'open' event sequence."""
    handlers = self._STATE_HANDLERS[target_state]
    if target_state == _StateType.TOOL_CALL:
        assert tool_call is not None
        return handlers.open_fn(
            self.state, tool_call.function.name, tool_call.index
        )
    return handlers.open_fn(self.state)
```

### resolve\_target\_state [¶](#vllm.entrypoints.openai.responses.streaming_events.SimpleStreamingEventProcessor.resolve_target_state "Permanent link")

```
resolve_target_state(
    delta_message: DeltaMessage,
) -> tuple[_StateType, Any]
```

Decide which state the next delta belongs to.

Priority: TOOL\_CALL &gt; REASONING &gt; CONTENT, fallback to NONE. For TOOL\_CALL the first tool\_call object is also returned so callers can detect a switch between consecutive tools.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defresolve_target_state(
    self, delta_message: DeltaMessage
) -> tuple[_StateType, Any]:
"""
    Decide which state the next delta belongs to.

    Priority: TOOL_CALL > REASONING > CONTENT, fallback to NONE.
    For TOOL_CALL the first tool_call object is also returned so
    callers can detect a switch between consecutive tools.
    """
    if (
        delta_message.tool_calls
        and delta_message.tool_calls[0].function is not None
    ):
        return _StateType.TOOL_CALL, delta_message.tool_calls[0]
    if delta_message.reasoning is not None:
        return _StateType.REASONING, None
    if delta_message.content:
        return _StateType.CONTENT, None
    return _StateType.NONE, None
```

## StreamingState `dataclass` [¶](#vllm.entrypoints.openai.responses.streaming_events.StreamingState "Permanent link")

Mutable state for streaming event processing.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
@dataclass
classStreamingState:
"""Mutable state for streaming event processing."""

    current_content_index: int = -1
    current_output_index: int = 0
    current_item_id: str = ""
    current_call_id: str = ""
    sent_output_item_added: bool = False
    is_first_function_call_delta: bool = False

    defreset_for_new_item(self) -> None:
"""Reset state when expecting a new output item."""
        self.current_output_index += 1
        self.sent_output_item_added = False
        self.is_first_function_call_delta = False
        self.current_call_id = ""
```

### reset\_for\_new\_item [¶](#vllm.entrypoints.openai.responses.streaming_events.StreamingState.reset_for_new_item "Permanent link")

```
reset_for_new_item() -> None
```

Reset state when expecting a new output item.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defreset_for_new_item(self) -> None:
"""Reset state when expecting a new output item."""
    self.current_output_index += 1
    self.sent_output_item_added = False
    self.is_first_function_call_delta = False
    self.current_call_id = ""
```

## \_StateHandlers [¶](#vllm.entrypoints.openai.responses.streaming_events._StateHandlers "Permanent link")

Bases: `NamedTuple`

Tuple for each state: open(start), delta(chunk), done(finish).

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
class_StateHandlers(NamedTuple):
"""Tuple for each state: open(start), delta(chunk), done(finish)."""

    open_fn: Callable[..., list[StreamingResponsesResponse]]
    delta_fn: Callable[..., list[StreamingResponsesResponse]]
    done_fn: Callable[..., list[StreamingResponsesResponse]]
```

## \_resolve\_mcp\_name\_label [¶](#vllm.entrypoints.openai.responses.streaming_events._resolve_mcp_name_label "Permanent link")

Resolve MCP tool name and server label from a recipient string.

- `mcp.*` recipients: strip prefix, use the bare name as both name and server\_label.
- Everything else: use the recipient as the name and look up the server\_label in TOOL\_NAME\_TO\_MCP\_SERVER\_LABEL.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
def_resolve_mcp_name_label(recipient: str) -> tuple[str, str]:
"""Resolve MCP tool name and server label from a recipient string.

    - ``mcp.*`` recipients: strip prefix, use the bare name as both
      name and server_label.
    - Everything else: use the recipient as the name and look up the
      server_label in TOOL_NAME_TO_MCP_SERVER_LABEL.
    """
    if recipient.startswith("mcp."):
        name = recipient[len("mcp.") :]
        return name, name
    return recipient, TOOL_NAME_TO_MCP_SERVER_LABEL.get(recipient, recipient)
```

## emit\_browser\_tool\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_browser_tool_events "Permanent link")

```
emit_browser_tool_events(
    previous_item: Message, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit events for browser tool calls (web search).

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_browser_tool_events(
    previous_item: HarmonyMessage,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events for browser tool calls (web search)."""
    function_name = previous_item.recipient[len("browser.") :]
    parsed_args = json.loads(previous_item.content[0].text)
    action = None

    if function_name == "search":
        action = response_function_web_search.ActionSearch(
            type="search",
            query=parsed_args["query"],
        )
    elif function_name == "open":
        action = response_function_web_search.ActionOpenPage(
            type="open_page",
            # TODO: translate to url
            url=f"cursor:{parsed_args.get('cursor','')}",
        )
    elif function_name == "find":
        action = response_function_web_search.ActionFind(
            type="find",
            pattern=parsed_args["pattern"],
            # TODO: translate to url
            url=f"cursor:{parsed_args.get('cursor','')}",
        )
    else:
        raise ValueError(f"Unknown function name: {function_name}")

    state.current_item_id = f"tool_{random_uuid()}"
    events: list[StreamingResponsesResponse] = []
    events.append(
        ResponseOutputItemAddedEvent(
            type="response.output_item.added",
            sequence_number=-1,
            output_index=state.current_output_index,
            item=response_function_web_search.ResponseFunctionWebSearch(
                # TODO: generate a unique id for web search call
                type="web_search_call",
                id=state.current_item_id,
                action=action,
                status="in_progress",
            ),
        )
    )
    events.append(
        ResponseWebSearchCallInProgressEvent(
            type="response.web_search_call.in_progress",
            sequence_number=-1,
            output_index=state.current_output_index,
            item_id=state.current_item_id,
        )
    )
    events.append(
        ResponseWebSearchCallSearchingEvent(
            type="response.web_search_call.searching",
            sequence_number=-1,
            output_index=state.current_output_index,
            item_id=state.current_item_id,
        )
    )
    # enqueue
    events.append(
        ResponseWebSearchCallCompletedEvent(
            type="response.web_search_call.completed",
            sequence_number=-1,
            output_index=state.current_output_index,
            item_id=state.current_item_id,
        )
    )
    events.append(
        ResponseOutputItemDoneEvent(
            type="response.output_item.done",
            sequence_number=-1,
            output_index=state.current_output_index,
            item=ResponseFunctionWebSearch(
                type="web_search_call",
                id=state.current_item_id,
                action=action,
                status="completed",
            ),
        )
    )
    return events
```

## emit\_code\_interpreter\_completion\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_code_interpreter_completion_events "Permanent link")

```
emit_code_interpreter_completion_events(
    previous_item: Message, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit events when code interpreter completes.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_code_interpreter_completion_events(
    previous_item: HarmonyMessage,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events when code interpreter completes."""
    events: list[StreamingResponsesResponse] = []
    events.append(
        ResponseCodeInterpreterCallCodeDoneEvent(
            type="response.code_interpreter_call_code.done",
            sequence_number=-1,
            output_index=state.current_output_index,
            item_id=state.current_item_id,
            code=previous_item.content[0].text,
        )
    )
    events.append(
        ResponseCodeInterpreterCallInterpretingEvent(
            type="response.code_interpreter_call.interpreting",
            sequence_number=-1,
            output_index=state.current_output_index,
            item_id=state.current_item_id,
        )
    )
    events.append(
        ResponseCodeInterpreterCallCompletedEvent(
            type="response.code_interpreter_call.completed",
            sequence_number=-1,
            output_index=state.current_output_index,
            item_id=state.current_item_id,
        )
    )
    events.append(
        ResponseOutputItemDoneEvent(
            type="response.output_item.done",
            sequence_number=-1,
            output_index=state.current_output_index,
            item=ResponseCodeInterpreterToolCallParam(
                type="code_interpreter_call",
                id=state.current_item_id,
                code=previous_item.content[0].text,
                container_id="auto",
                outputs=[],
                status="completed",
            ),
        )
    )
    return events
```

## emit\_code\_interpreter\_delta\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_code_interpreter_delta_events "Permanent link")

```
emit_code_interpreter_delta_events(
    delta: str, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit events for code interpreter delta streaming.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_code_interpreter_delta_events(
    delta: str,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events for code interpreter delta streaming."""
    events: list[StreamingResponsesResponse] = []
    if not state.sent_output_item_added:
        state.sent_output_item_added = True
        state.current_item_id = f"tool_{random_uuid()}"
        events.append(
            ResponseOutputItemAddedEvent(
                type="response.output_item.added",
                sequence_number=-1,
                output_index=state.current_output_index,
                item=ResponseCodeInterpreterToolCallParam(
                    type="code_interpreter_call",
                    id=state.current_item_id,
                    code=None,
                    container_id="auto",
                    outputs=None,
                    status="in_progress",
                ),
            )
        )
        events.append(
            ResponseCodeInterpreterCallInProgressEvent(
                type="response.code_interpreter_call.in_progress",
                sequence_number=-1,
                output_index=state.current_output_index,
                item_id=state.current_item_id,
            )
        )
    events.append(
        ResponseCodeInterpreterCallCodeDeltaEvent(
            type="response.code_interpreter_call_code.delta",
            sequence_number=-1,
            output_index=state.current_output_index,
            item_id=state.current_item_id,
            delta=delta,
        )
    )
    return events
```

## emit\_content\_delta\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_content_delta_events "Permanent link")

```
emit_content_delta_events(
    ctx: StreamingHarmonyContext, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit events for content delta streaming based on channel type.

This is a Harmony-specific dispatcher that extracts values from the Harmony context and delegates to shared leaf helpers.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_content_delta_events(
    ctx: StreamingHarmonyContext,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events for content delta streaming based on channel type.

    This is a Harmony-specific dispatcher that extracts values from the
    Harmony context and delegates to shared leaf helpers.
    """
    delta = ctx.last_content_delta
    if not delta:
        return []

    channel = ctx.parser.current_channel
    recipient = ctx.parser.current_recipient

    if channel in ("final", "commentary") and recipient is None:
        # Preambles (commentary with no recipient) and final messages
        # are both user-visible text.
        return emit_text_delta_events(delta, state)
    elif channel == "analysis" and recipient is None:
        return emit_reasoning_delta_events(delta, state)
    # built-in tools will be triggered on the analysis channel
    # However, occasionally built-in tools will
    # still be output to commentary.
    elif channel in ("commentary", "analysis") and recipient is not None:
        if recipient.startswith("functions."):
            function_name = recipient[len("functions.") :]
            return emit_function_call_delta_events(delta, function_name, state)
        elif recipient == "python":
            return emit_code_interpreter_delta_events(delta, state)
        elif recipient.startswith("mcp.") or is_mcp_tool_by_namespace(recipient):
            return emit_mcp_delta_events(delta, state, recipient)

    return []
```

## emit\_function\_call\_delta\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_function_call_delta_events "Permanent link")

```
emit_function_call_delta_events(
    delta: str, function_name: str, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit events for function call argument deltas.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_function_call_delta_events(
    delta: str,
    function_name: str,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events for function call argument deltas."""
    events: list[StreamingResponsesResponse] = []
    if state.is_first_function_call_delta is False:
        state.is_first_function_call_delta = True
        state.current_item_id = f"fc_{random_uuid()}"
        state.current_call_id = f"call_{random_uuid()}"
        tool_call_item = ResponseFunctionToolCall(
            name=function_name,
            type="function_call",
            id=state.current_item_id,
            call_id=state.current_call_id,
            arguments="",
            status="in_progress",
        )
        events.append(
            ResponseOutputItemAddedEvent(
                type="response.output_item.added",
                sequence_number=-1,
                output_index=state.current_output_index,
                item=tool_call_item,
            )
        )
    # Always emit the delta (including on first call)
    events.append(
        ResponseFunctionCallArgumentsDeltaEvent(
            item_id=state.current_item_id,
            delta=delta,
            output_index=state.current_output_index,
            sequence_number=-1,
            type="response.function_call_arguments.delta",
        )
    )
    return events
```

## emit\_function\_call\_done\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_function_call_done_events "Permanent link")

```
emit_function_call_done_events(
    function_name: str,
    arguments: str,
    state: StreamingState,
) -> list[StreamingResponsesResponse]
```

Emit events when a function call completes.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_function_call_done_events(
    function_name: str,
    arguments: str,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events when a function call completes."""
    events: list[StreamingResponsesResponse] = []
    events.append(
        ResponseFunctionCallArgumentsDoneEvent(
            type="response.function_call_arguments.done",
            arguments=arguments,
            name=function_name,
            item_id=state.current_item_id,
            output_index=state.current_output_index,
            sequence_number=-1,
        )
    )
    function_call_item = ResponseFunctionToolCall(
        type="function_call",
        arguments=arguments,
        name=function_name,
        item_id=state.current_item_id,
        output_index=state.current_output_index,
        sequence_number=-1,
        call_id=state.current_call_id,
        status="completed",
    )
    events.append(
        ResponseOutputItemDoneEvent(
            type="response.output_item.done",
            sequence_number=-1,
            output_index=state.current_output_index,
            item=function_call_item,
        )
    )
    return events
```

## emit\_mcp\_completion\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_mcp_completion_events "Permanent link")

```
emit_mcp_completion_events(
    recipient: str, arguments: str, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit events when an MCP tool call completes.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_mcp_completion_events(
    recipient: str,
    arguments: str,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events when an MCP tool call completes."""
    name, server_label = _resolve_mcp_name_label(recipient)
    events: list[StreamingResponsesResponse] = []
    events.append(
        ResponseMcpCallArgumentsDoneEvent(
            type="response.mcp_call_arguments.done",
            arguments=arguments,
            name=name,
            item_id=state.current_item_id,
            output_index=state.current_output_index,
            sequence_number=-1,
        )
    )
    events.append(
        ResponseMcpCallCompletedEvent(
            type="response.mcp_call.completed",
            sequence_number=-1,
            output_index=state.current_output_index,
            item_id=state.current_item_id,
        )
    )
    events.append(
        ResponseOutputItemDoneEvent(
            type="response.output_item.done",
            sequence_number=-1,
            output_index=state.current_output_index,
            item=McpCall(
                type="mcp_call",
                arguments=arguments,
                name=name,
                id=state.current_item_id,
                server_label=server_label,
                status="completed",
            ),
        )
    )
    return events
```

## emit\_mcp\_delta\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_mcp_delta_events "Permanent link")

```
emit_mcp_delta_events(
    delta: str, state: StreamingState, recipient: str
) -> list[StreamingResponsesResponse]
```

Emit events for MCP tool delta streaming.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_mcp_delta_events(
    delta: str,
    state: StreamingState,
    recipient: str,
) -> list[StreamingResponsesResponse]:
"""Emit events for MCP tool delta streaming."""
    name, server_label = _resolve_mcp_name_label(recipient)
    events: list[StreamingResponsesResponse] = []
    if not state.sent_output_item_added:
        state.sent_output_item_added = True
        state.current_item_id = f"mcp_{random_uuid()}"
        events.append(
            ResponseOutputItemAddedEvent(
                type="response.output_item.added",
                sequence_number=-1,
                output_index=state.current_output_index,
                item=McpCall(
                    type="mcp_call",
                    id=state.current_item_id,
                    name=name,
                    arguments="",
                    server_label=server_label,
                    status="in_progress",
                ),
            )
        )
        events.append(
            ResponseMcpCallInProgressEvent(
                type="response.mcp_call.in_progress",
                sequence_number=-1,
                output_index=state.current_output_index,
                item_id=state.current_item_id,
            )
        )
    events.append(
        ResponseMcpCallArgumentsDeltaEvent(
            type="response.mcp_call_arguments.delta",
            sequence_number=-1,
            output_index=state.current_output_index,
            item_id=state.current_item_id,
            delta=delta,
        )
    )
    return events
```

## emit\_previous\_item\_done\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_previous_item_done_events "Permanent link")

```
emit_previous_item_done_events(
    previous_item: Message, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit done events for the previous item when expecting a new start.

This is a Harmony-specific dispatcher that extracts values from the Harmony parser's message object and delegates to shared leaf helpers.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_previous_item_done_events(
    previous_item: HarmonyMessage,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit done events for the previous item when expecting a new start.

    This is a Harmony-specific dispatcher that extracts values from the
    Harmony parser's message object and delegates to shared leaf helpers.
    """
    text = previous_item.content[0].text
    if previous_item.recipient is not None:
        # Deal with tool call
        if previous_item.recipient.startswith("functions."):
            function_name = previous_item.recipient[len("functions.") :]
            return emit_function_call_done_events(function_name, text, state)
        elif previous_item.recipient == "python":
            return emit_code_interpreter_completion_events(previous_item, state)
        elif (
            is_mcp_tool_by_namespace(previous_item.recipient)
            and state.current_item_id is not None
            and state.current_item_id.startswith("mcp_")
        ):
            return emit_mcp_completion_events(previous_item.recipient, text, state)
    elif previous_item.channel == "analysis":
        return emit_reasoning_done_events(text, state)
    elif previous_item.channel in ("commentary", "final"):
        # Preambles (commentary with no recipient) and final messages
        # are both user-visible text.
        return emit_text_output_done_events(text, state)
    return []
```

## emit\_reasoning\_delta\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_reasoning_delta_events "Permanent link")

```
emit_reasoning_delta_events(
    delta: str, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit events for reasoning text delta streaming.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_reasoning_delta_events(
    delta: str,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events for reasoning text delta streaming."""
    events: list[StreamingResponsesResponse] = []
    if not state.sent_output_item_added:
        state.sent_output_item_added = True
        state.current_item_id = f"msg_{random_uuid()}"
        events.append(
            ResponseOutputItemAddedEvent(
                type="response.output_item.added",
                sequence_number=-1,
                output_index=state.current_output_index,
                item=ResponseReasoningItem(
                    type="reasoning",
                    id=state.current_item_id,
                    summary=[],
                    status="in_progress",
                ),
            )
        )
        state.current_content_index += 1
        events.append(
            ResponseReasoningPartAddedEvent(
                type="response.reasoning_part.added",
                sequence_number=-1,
                output_index=state.current_output_index,
                item_id=state.current_item_id,
                content_index=state.current_content_index,
                part=ResponseReasoningTextContent(
                    text="",
                    type="reasoning_text",
                ),
            )
        )
    events.append(
        ResponseReasoningTextDeltaEvent(
            type="response.reasoning_text.delta",
            item_id=state.current_item_id,
            output_index=state.current_output_index,
            content_index=state.current_content_index,
            delta=delta,
            sequence_number=-1,
        )
    )
    return events
```

## emit\_reasoning\_done\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_reasoning_done_events "Permanent link")

```
emit_reasoning_done_events(
    text: str, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit events when a reasoning (analysis) item completes.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_reasoning_done_events(
    text: str,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events when a reasoning (analysis) item completes."""
    content = ResponseReasoningTextContent(
        text=text,
        type="reasoning_text",
    )
    reasoning_item = ResponseReasoningItem(
        type="reasoning",
        content=[content],
        status="completed",
        id=state.current_item_id,
        summary=[],
    )
    events: list[StreamingResponsesResponse] = []
    events.append(
        ResponseReasoningTextDoneEvent(
            type="response.reasoning_text.done",
            item_id=state.current_item_id,
            sequence_number=-1,
            output_index=state.current_output_index,
            content_index=state.current_content_index,
            text=text,
        )
    )
    events.append(
        ResponseReasoningPartDoneEvent(
            type="response.reasoning_part.done",
            sequence_number=-1,
            item_id=state.current_item_id,
            output_index=state.current_output_index,
            content_index=state.current_content_index,
            part=content,
        )
    )
    events.append(
        ResponseOutputItemDoneEvent(
            type="response.output_item.done",
            sequence_number=-1,
            output_index=state.current_output_index,
            item=reasoning_item,
        )
    )
    return events
```

## emit\_text\_delta\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_text_delta_events "Permanent link")

```
emit_text_delta_events(
    delta: str, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit events for text content delta streaming.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_text_delta_events(
    delta: str,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events for text content delta streaming."""
    events: list[StreamingResponsesResponse] = []
    if not state.sent_output_item_added:
        state.sent_output_item_added = True
        state.current_item_id = f"msg_{random_uuid()}"
        events.append(
            ResponseOutputItemAddedEvent(
                type="response.output_item.added",
                sequence_number=-1,
                output_index=state.current_output_index,
                item=ResponseOutputMessage(
                    id=state.current_item_id,
                    type="message",
                    role="assistant",
                    content=[],
                    status="in_progress",
                ),
            )
        )
        state.current_content_index += 1
        events.append(
            ResponseContentPartAddedEvent(
                type="response.content_part.added",
                sequence_number=-1,
                output_index=state.current_output_index,
                item_id=state.current_item_id,
                content_index=state.current_content_index,
                part=ResponseOutputText(
                    type="output_text",
                    text="",
                    annotations=[],
                    logprobs=[],
                ),
            )
        )
    events.append(
        ResponseTextDeltaEvent(
            type="response.output_text.delta",
            sequence_number=-1,
            content_index=state.current_content_index,
            output_index=state.current_output_index,
            item_id=state.current_item_id,
            delta=delta,
            # TODO, use logprobs from ctx.last_request_output
            logprobs=[],
        )
    )
    return events
```

## emit\_text\_output\_done\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_text_output_done_events "Permanent link")

```
emit_text_output_done_events(
    text: str, state: StreamingState
) -> list[StreamingResponsesResponse]
```

Emit events when a final text output item completes.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_text_output_done_events(
    text: str,
    state: StreamingState,
) -> list[StreamingResponsesResponse]:
"""Emit events when a final text output item completes."""
    text_content = ResponseOutputText(
        type="output_text",
        text=text,
        annotations=[],
    )
    events: list[StreamingResponsesResponse] = []
    events.append(
        ResponseTextDoneEvent(
            type="response.output_text.done",
            sequence_number=-1,
            output_index=state.current_output_index,
            content_index=state.current_content_index,
            text=text,
            logprobs=[],
            item_id=state.current_item_id,
        )
    )
    events.append(
        ResponseContentPartDoneEvent(
            type="response.content_part.done",
            sequence_number=-1,
            item_id=state.current_item_id,
            output_index=state.current_output_index,
            content_index=state.current_content_index,
            part=text_content,
        )
    )
    events.append(
        ResponseOutputItemDoneEvent(
            type="response.output_item.done",
            sequence_number=-1,
            output_index=state.current_output_index,
            item=ResponseOutputMessage(
                id=state.current_item_id,
                type="message",
                role="assistant",
                content=[text_content],
                status="completed",
            ),
        )
    )
    return events
```

## emit\_tool\_action\_events [¶](#vllm.entrypoints.openai.responses.streaming_events.emit_tool_action_events "Permanent link")

```
emit_tool_action_events(
    ctx: StreamingHarmonyContext,
    state: StreamingState,
    tool_server: ToolServer | None,
) -> list[StreamingResponsesResponse]
```

Emit events for tool action turn.

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defemit_tool_action_events(
    ctx: StreamingHarmonyContext,
    state: StreamingState,
    tool_server: ToolServer | None,
) -> list[StreamingResponsesResponse]:
"""Emit events for tool action turn."""
    if not ctx.is_assistant_action_turn() or len(ctx.parser.messages) == 0:
        return []

    events: list[StreamingResponsesResponse] = []
    previous_item = ctx.parser.messages[-1]

    # Handle browser tool
    if (
        tool_server is not None
        and tool_server.has_tool("browser")
        and previous_item.recipient is not None
        and previous_item.recipient.startswith("browser.")
    ):
        events.extend(emit_browser_tool_events(previous_item, state))

    # Handle tool completion
    if (
        tool_server is not None
        and previous_item.recipient is not None
        and state.current_item_id is not None
        and state.sent_output_item_added
    ):
        recipient = previous_item.recipient
        if recipient == "python":
            events.extend(emit_code_interpreter_completion_events(previous_item, state))
        elif recipient.startswith("mcp.") or is_mcp_tool_by_namespace(recipient):
            events.extend(
                emit_mcp_completion_events(
                    recipient, previous_item.content[0].text, state
                )
            )

    return events
```

## is\_mcp\_tool\_by\_namespace [¶](#vllm.entrypoints.openai.responses.streaming_events.is_mcp_tool_by_namespace "Permanent link")

```
is_mcp_tool_by_namespace(recipient: str | None) -> bool
```

Determine if a tool call is an MCP tool based on recipient prefix.

- Tools starting with "functions." are function calls
- Everything else is an MCP tool

Source code in `vllm/entrypoints/openai/responses/streaming_events.py`

```
defis_mcp_tool_by_namespace(recipient: str | None) -> bool:
"""
    Determine if a tool call is an MCP tool based on recipient prefix.

    - Tools starting with "functions." are function calls
    - Everything else is an MCP tool
    """
    if recipient is None:
        return False

    # Function calls have "functions." prefix
    # Everything else is an MCP tool
    return not recipient.startswith("functions.")
```