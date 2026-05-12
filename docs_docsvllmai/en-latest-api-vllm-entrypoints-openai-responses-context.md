---
title: context - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/responses/context/
source: sitemap
fetched_at: 2026-05-07T21:20:29.27612479-03:00
rendered_js: false
word_count: 502
summary: The HarmonyContext class manages conversation state and tracks token usage metrics for multi-turn interactions involving tools in vLLM.
tags:
    - vllm
    - conversation-context
    - token-tracking
    - tool-calling
    - api-response
    - llm-metrics
category: reference
---

## HarmonyContext [¶](#vllm.entrypoints.openai.responses.context.HarmonyContext "Permanent link")

Bases: `ConversationContext`

Source code in `vllm/entrypoints/openai/responses/context.py`

```
classHarmonyContext(ConversationContext):
    def__init__(
        self,
        messages: list,
        available_tools: list[str],
    ):
        self._messages = messages
        self.finish_reason: str | None = None
        self.available_tools = available_tools
        self._tool_sessions: dict[str, ClientSession | Tool] = {}
        self.called_tools: set[str] = set()

        self.parser = get_streamable_parser_for_assistant()
        self.num_init_messages = len(messages)
        self.num_prompt_tokens = 0
        self.num_output_tokens = 0
        self.num_cached_tokens = 0
        self.num_reasoning_tokens = 0
        self.num_tool_output_tokens = 0

        # Turn tracking - replaces multiple individual tracking variables
        self.current_turn_metrics = TurnMetrics()
        # Track metrics for all turns
        self.all_turn_metrics: list[TurnMetrics] = []
        self.is_first_turn = True
        self.first_tok_of_message = True  # For streaming support
        self.kv_transfer_params: dict[str, Any] | None = None

    def_update_num_reasoning_tokens(self):
        channel = self.parser.current_channel
        if channel == "analysis":
            self.num_reasoning_tokens += 1
        elif channel == "commentary" and self.parser.current_recipient is not None:
            # Tool interactions (python/browser/container) are hidden.
            # Preambles (recipient=None) are visible user text.
            self.num_reasoning_tokens += 1

    defappend_output(self, output: RequestOutput) -> None:
        output_token_ids = output.outputs[0].token_ids
        self.parser = get_streamable_parser_for_assistant()
        for token_id in output_token_ids:
            self.parser.process(token_id)
            # Check if the current token is part of reasoning content
            self._update_num_reasoning_tokens()
        self._update_prefill_token_usage(output)
        self._update_decode_token_usage(output)
        if output.kv_transfer_params is not None:
            self.kv_transfer_params = output.kv_transfer_params
        # Append current turn to all turn list for next turn's calculations
        self.all_turn_metrics.append(self.current_turn_metrics.copy())
        self.current_turn_metrics.reset()
        # append_output is called only once before tool calling
        # in non-streaming case
        # so we can append all the parser messages to _messages
        output_msgs = self.parser.messages
        # The responses finish reason is set in the last message
        self.finish_reason = output.outputs[0].finish_reason
        self._messages.extend(output_msgs)

    defappend_tool_output(self, output: list[Message]) -> None:
        output_msgs = output
        self._messages.extend(output_msgs)

    def_update_prefill_token_usage(self, output: RequestOutput) -> None:
"""Update token usage statistics for the prefill phase of generation.

        The prefill phase processes the input prompt tokens. This method:
        1. Counts the prompt tokens for this turn
        2. Calculates tool output tokens for multi-turn conversations
        3. Updates cached token counts
        4. Tracks state for next turn calculations

        Tool output tokens are calculated as:
        current_prompt_tokens - last_turn_prompt_tokens -
        last_turn_output_tokens
        This represents tokens added between turns (typically tool responses).

        Args:
            output: The RequestOutput containing prompt token information
        """
        if output.prompt_token_ids is not None:
            this_turn_input_tokens = len(output.prompt_token_ids)
        else:
            this_turn_input_tokens = 0
            logger.error("RequestOutput appended contains no prompt_token_ids.")

        # Update current turn input tokens
        self.current_turn_metrics.input_tokens = this_turn_input_tokens
        self.num_prompt_tokens += this_turn_input_tokens

        # Calculate tool tokens (except on first turn)
        if self.is_first_turn:
            self.is_first_turn = False
        else:
            previous_turn = self.all_turn_metrics[-1]
            # start counting tool after first turn
            # tool tokens = this turn prefill - last turn prefill -
            # last turn decode
            this_turn_tool_tokens = (
                self.current_turn_metrics.input_tokens
                - previous_turn.input_tokens
                - previous_turn.output_tokens
            )

            # Handle negative tool token counts (shouldn't happen in normal
            # cases)
            if this_turn_tool_tokens < 0:
                logger.error(
                    "Negative tool output tokens calculated: %d "
                    "(current_input=%d, previous_input=%d, "
                    "previous_output=%d). Setting to 0.",
                    this_turn_tool_tokens,
                    self.current_turn_metrics.input_tokens,
                    previous_turn.input_tokens,
                    previous_turn.output_tokens,
                )
                this_turn_tool_tokens = 0

            self.num_tool_output_tokens += this_turn_tool_tokens
            self.current_turn_metrics.tool_output_tokens = this_turn_tool_tokens

        # Update cached tokens
        num_cached_token = output.num_cached_tokens
        if num_cached_token is not None:
            self.num_cached_tokens += num_cached_token
            self.current_turn_metrics.cached_input_tokens = num_cached_token

    def_update_decode_token_usage(self, output: RequestOutput) -> int:
"""Update token usage statistics for the decode phase of generation.

        The decode phase processes the generated output tokens. This method:
        1. Counts output tokens from all completion outputs
        2. Updates the total output token count
        3. Tracks tokens generated in the current turn

        In streaming mode, this is called for each token generated.
        In non-streaming mode, this is called once with all output tokens.

        Args:
            output: The RequestOutput containing generated token information

        Returns:
            int: Number of output tokens processed in this call
        """
        updated_output_token_count = 0
        if output.outputs:
            for completion_output in output.outputs:
                # only keep last round
                updated_output_token_count += len(completion_output.token_ids)
            self.num_output_tokens += updated_output_token_count
            self.current_turn_metrics.output_tokens += updated_output_token_count
        return updated_output_token_count

    @property
    defmessages(self) -> list:
        return self._messages

    defneed_builtin_tool_call(self) -> bool:
        last_msg = self.messages[-1]
        recipient = last_msg.recipient
        if recipient is None:
            return False
        if recipient.startswith("browser."):
            return "browser" in self.available_tools
        if recipient.startswith("python"):
            return "python" in self.available_tools
        if recipient.startswith("container."):
            return "container" in self.available_tools
        return False

    async defcall_tool(self) -> list[Message]:
        if not self.messages:
            return []
        last_msg = self.messages[-1]
        recipient = last_msg.recipient
        if recipient is not None:
            if recipient.startswith("browser."):
                return await self.call_search_tool(
                    self._tool_sessions["browser"], last_msg
                )
            elif recipient.startswith("python"):
                return await self.call_python_tool(
                    self._tool_sessions["python"], last_msg
                )
            elif recipient.startswith("container."):
                return await self.call_container_tool(
                    self._tool_sessions["container"], last_msg
                )
        raise ValueError("No tool call found")

    defrender_for_completion(self) -> list[int]:
        return render_for_completion(self.messages)

    async defcall_search_tool(
        self, tool_session: Union["ClientSession", Tool], last_msg: Message
    ) -> list[Message]:
        self.called_tools.add("browser")
        if isinstance(tool_session, Tool):
            return await tool_session.get_result(self)
        tool_name = last_msg.recipient.split(".")[1]
        if envs.VLLM_TOOL_JSON_ERROR_AUTOMATIC_RETRY:
            try:
                args = json.loads(last_msg.content[0].text)
            except json.JSONDecodeError as e:
                return _create_json_parse_error_messages(last_msg, e)
        else:
            args = json.loads(last_msg.content[0].text)
        result = await tool_session.call_tool(tool_name, args)
        result_str = result.content[0].text
        content = TextContent(text=result_str)
        author = Author(role=Role.TOOL, name=last_msg.recipient)
        return [
            Message(
                author=author,
                content=[content],
                recipient=Role.ASSISTANT,
                channel=last_msg.channel,
            )
        ]

    async defcall_python_tool(
        self, tool_session: Union["ClientSession", Tool], last_msg: Message
    ) -> list[Message]:
        self.called_tools.add("python")
        if isinstance(tool_session, Tool):
            return await tool_session.get_result(self)
        param = {
            "code": last_msg.content[0].text,
        }
        result = await tool_session.call_tool("python", param)
        result_str = result.content[0].text

        content = TextContent(text=result_str)
        author = Author(role=Role.TOOL, name="python")

        return [
            Message(
                author=author,
                content=[content],
                channel=last_msg.channel,
                recipient=Role.ASSISTANT,
            )
        ]

    async definit_tool_sessions(
        self,
        tool_server: ToolServer | None,
        exit_stack: AsyncExitStack,
        request_id: str,
        mcp_tools: dict[str, Mcp],
    ):
        if tool_server:
            for tool_name in self.available_tools:
                if tool_name not in self._tool_sessions:
                    tool_type = _map_tool_name_to_tool_type(tool_name)
                    headers = (
                        mcp_tools[tool_type].headers if tool_type in mcp_tools else None
                    )
                    tool_session = await exit_stack.enter_async_context(
                        tool_server.new_session(tool_name, request_id, headers)
                    )
                    self._tool_sessions[tool_name] = tool_session
                    exit_stack.push_async_exit(self.cleanup_session)

    async defcall_container_tool(
        self, tool_session: Union["ClientSession", Tool], last_msg: Message
    ) -> list[Message]:
"""
        Call container tool. Expect this to be run in a stateful docker
        with command line terminal.
        The official container tool would at least
        expect the following format:
        - for tool name: exec
            - args:
                {
                    "cmd":List[str] "command to execute",
                    "workdir":optional[str] "current working directory",
                    "env":optional[object/dict] "environment variables",
                    "session_name":optional[str] "session name",
                    "timeout":optional[int] "timeout in seconds",
                    "user":optional[str] "user name",
                }
        """
        self.called_tools.add("container")
        if isinstance(tool_session, Tool):
            return await tool_session.get_result(self)
        tool_name = last_msg.recipient.split(".")[1].split(" ")[0]
        if envs.VLLM_TOOL_JSON_ERROR_AUTOMATIC_RETRY:
            try:
                args = json.loads(last_msg.content[0].text)
            except json.JSONDecodeError as e:
                return _create_json_parse_error_messages(last_msg, e)
        else:
            args = json.loads(last_msg.content[0].text)
        result = await tool_session.call_tool(tool_name, args)
        result_str = result.content[0].text
        content = TextContent(text=result_str)
        author = Author(role=Role.TOOL, name=last_msg.recipient)
        return [
            Message(
                author=author,
                content=[content],
                recipient=Role.ASSISTANT,
                channel=last_msg.channel,
            )
        ]

    async defcleanup_session(self, *args, **kwargs) -> None:
"""Can be used as coro to used in __aexit__"""

        async defcleanup_tool_session(tool_session):
            if not isinstance(tool_session, Tool):
                logger.info(
                    "Cleaning up tool session for %s", tool_session._client_info
                )
                with contextlib.suppress(Exception):
                    await tool_session.call_tool("cleanup_session", {})

        await asyncio.gather(
            *(
                cleanup_tool_session(self._tool_sessions[tool])
                for tool in self.called_tools
            )
        )
```

### \_update\_decode\_token\_usage [¶](#vllm.entrypoints.openai.responses.context.HarmonyContext._update_decode_token_usage "Permanent link")

Update token usage statistics for the decode phase of generation.

The decode phase processes the generated output tokens. This method: 1. Counts output tokens from all completion outputs 2. Updates the total output token count 3. Tracks tokens generated in the current turn

In streaming mode, this is called for each token generated. In non-streaming mode, this is called once with all output tokens.

Parameters:

Name Type Description Default `output` `RequestOutput`

The RequestOutput containing generated token information

*required*

Returns:

Name Type Description `int` `int`

Number of output tokens processed in this call

Source code in `vllm/entrypoints/openai/responses/context.py`

```
def_update_decode_token_usage(self, output: RequestOutput) -> int:
"""Update token usage statistics for the decode phase of generation.

    The decode phase processes the generated output tokens. This method:
    1. Counts output tokens from all completion outputs
    2. Updates the total output token count
    3. Tracks tokens generated in the current turn

    In streaming mode, this is called for each token generated.
    In non-streaming mode, this is called once with all output tokens.

    Args:
        output: The RequestOutput containing generated token information

    Returns:
        int: Number of output tokens processed in this call
    """
    updated_output_token_count = 0
    if output.outputs:
        for completion_output in output.outputs:
            # only keep last round
            updated_output_token_count += len(completion_output.token_ids)
        self.num_output_tokens += updated_output_token_count
        self.current_turn_metrics.output_tokens += updated_output_token_count
    return updated_output_token_count
```

### \_update\_prefill\_token\_usage [¶](#vllm.entrypoints.openai.responses.context.HarmonyContext._update_prefill_token_usage "Permanent link")

Update token usage statistics for the prefill phase of generation.

The prefill phase processes the input prompt tokens. This method: 1. Counts the prompt tokens for this turn 2. Calculates tool output tokens for multi-turn conversations 3. Updates cached token counts 4. Tracks state for next turn calculations

Tool output tokens are calculated as: current\_prompt\_tokens - last\_turn\_prompt\_tokens - last\_turn\_output\_tokens This represents tokens added between turns (typically tool responses).

Parameters:

Name Type Description Default `output` `RequestOutput`

The RequestOutput containing prompt token information

*required*

Source code in `vllm/entrypoints/openai/responses/context.py`

```
def_update_prefill_token_usage(self, output: RequestOutput) -> None:
"""Update token usage statistics for the prefill phase of generation.

    The prefill phase processes the input prompt tokens. This method:
    1. Counts the prompt tokens for this turn
    2. Calculates tool output tokens for multi-turn conversations
    3. Updates cached token counts
    4. Tracks state for next turn calculations

    Tool output tokens are calculated as:
    current_prompt_tokens - last_turn_prompt_tokens -
    last_turn_output_tokens
    This represents tokens added between turns (typically tool responses).

    Args:
        output: The RequestOutput containing prompt token information
    """
    if output.prompt_token_ids is not None:
        this_turn_input_tokens = len(output.prompt_token_ids)
    else:
        this_turn_input_tokens = 0
        logger.error("RequestOutput appended contains no prompt_token_ids.")

    # Update current turn input tokens
    self.current_turn_metrics.input_tokens = this_turn_input_tokens
    self.num_prompt_tokens += this_turn_input_tokens

    # Calculate tool tokens (except on first turn)
    if self.is_first_turn:
        self.is_first_turn = False
    else:
        previous_turn = self.all_turn_metrics[-1]
        # start counting tool after first turn
        # tool tokens = this turn prefill - last turn prefill -
        # last turn decode
        this_turn_tool_tokens = (
            self.current_turn_metrics.input_tokens
            - previous_turn.input_tokens
            - previous_turn.output_tokens
        )

        # Handle negative tool token counts (shouldn't happen in normal
        # cases)
        if this_turn_tool_tokens < 0:
            logger.error(
                "Negative tool output tokens calculated: %d "
                "(current_input=%d, previous_input=%d, "
                "previous_output=%d). Setting to 0.",
                this_turn_tool_tokens,
                self.current_turn_metrics.input_tokens,
                previous_turn.input_tokens,
                previous_turn.output_tokens,
            )
            this_turn_tool_tokens = 0

        self.num_tool_output_tokens += this_turn_tool_tokens
        self.current_turn_metrics.tool_output_tokens = this_turn_tool_tokens

    # Update cached tokens
    num_cached_token = output.num_cached_tokens
    if num_cached_token is not None:
        self.num_cached_tokens += num_cached_token
        self.current_turn_metrics.cached_input_tokens = num_cached_token
```

### call\_container\_tool `async` [¶](#vllm.entrypoints.openai.responses.context.HarmonyContext.call_container_tool "Permanent link")

```
call_container_tool(
    tool_session: Union[ClientSession, Tool],
    last_msg: Message,
) -> list[Message]
```

Call container tool. Expect this to be run in a stateful docker with command line terminal. The official container tool would at least expect the following format: - for tool name: exec - args: { "cmd":List\[str] "command to execute", "workdir":optional\[str] "current working directory", "env":optional\[object/dict] "environment variables", "session\_name":optional\[str] "session name", "timeout":optional\[int] "timeout in seconds", "user":optional\[str] "user name", }

Source code in `vllm/entrypoints/openai/responses/context.py`

```
async defcall_container_tool(
    self, tool_session: Union["ClientSession", Tool], last_msg: Message
) -> list[Message]:
"""
    Call container tool. Expect this to be run in a stateful docker
    with command line terminal.
    The official container tool would at least
    expect the following format:
    - for tool name: exec
        - args:
            {
                "cmd":List[str] "command to execute",
                "workdir":optional[str] "current working directory",
                "env":optional[object/dict] "environment variables",
                "session_name":optional[str] "session name",
                "timeout":optional[int] "timeout in seconds",
                "user":optional[str] "user name",
            }
    """
    self.called_tools.add("container")
    if isinstance(tool_session, Tool):
        return await tool_session.get_result(self)
    tool_name = last_msg.recipient.split(".")[1].split(" ")[0]
    if envs.VLLM_TOOL_JSON_ERROR_AUTOMATIC_RETRY:
        try:
            args = json.loads(last_msg.content[0].text)
        except json.JSONDecodeError as e:
            return _create_json_parse_error_messages(last_msg, e)
    else:
        args = json.loads(last_msg.content[0].text)
    result = await tool_session.call_tool(tool_name, args)
    result_str = result.content[0].text
    content = TextContent(text=result_str)
    author = Author(role=Role.TOOL, name=last_msg.recipient)
    return [
        Message(
            author=author,
            content=[content],
            recipient=Role.ASSISTANT,
            channel=last_msg.channel,
        )
    ]
```

### cleanup\_session `async` [¶](#vllm.entrypoints.openai.responses.context.HarmonyContext.cleanup_session "Permanent link")

```
cleanup_session(*args, **kwargs) -> None
```

Can be used as coro to used in **aexit**

Source code in `vllm/entrypoints/openai/responses/context.py`

```
async defcleanup_session(self, *args, **kwargs) -> None:
"""Can be used as coro to used in __aexit__"""

    async defcleanup_tool_session(tool_session):
        if not isinstance(tool_session, Tool):
            logger.info(
                "Cleaning up tool session for %s", tool_session._client_info
            )
            with contextlib.suppress(Exception):
                await tool_session.call_tool("cleanup_session", {})

    await asyncio.gather(
        *(
            cleanup_tool_session(self._tool_sessions[tool])
            for tool in self.called_tools
        )
    )
```

## ParsableContext [¶](#vllm.entrypoints.openai.responses.context.ParsableContext "Permanent link")

Bases: `ConversationContext`

Source code in `vllm/entrypoints/openai/responses/context.py`

```
classParsableContext(ConversationContext):
    def__init__(
        self,
        *,
        response_messages: list[ResponseInputOutputItem],
        tokenizer: TokenizerLike,
        reasoning_parser_cls: type[ReasoningParser] | None,
        request: ResponsesRequest,
        available_tools: list[str] | None,
        tool_parser_cls: type[ToolParser] | None,
        chat_template: str | None,
        chat_template_content_format: ChatTemplateContentFormatOption,
    ):
        self.num_prompt_tokens = 0
        self.num_output_tokens = 0
        self.num_cached_tokens = 0
        self.num_reasoning_tokens = 0
        # not implemented yet for ParsableContext
        self.all_turn_metrics: list[TurnMetrics] = []

        if reasoning_parser_cls is None:
            raise ValueError("reasoning_parser_cls must be provided.")

        self.parser = get_responses_parser_for_simple_context(
            tokenizer=tokenizer,
            reasoning_parser_cls=reasoning_parser_cls,
            response_messages=response_messages,
            request=request,
            tool_parser_cls=tool_parser_cls,
            chat_template=chat_template,
            chat_template_content_format=chat_template_content_format,
        )
        self.tool_parser_cls = tool_parser_cls
        self.request = request

        self.available_tools = available_tools or []
        self._tool_sessions: dict[str, ClientSession | Tool] = {}
        self.called_tools: set[str] = set()

        self.tool_dicts = construct_tool_dicts(request.tools, request.tool_choice)
        self.chat_template = chat_template
        self.chat_template_content_format: Final = chat_template_content_format

        self.input_messages: list[ResponseRawMessageAndToken] = []
        self.output_messages: list[ResponseRawMessageAndToken] = []
        self._accumulated_token_ids: list[int] = []
        self.kv_transfer_params: dict[str, Any] | None = None

    defappend_output(self, output: RequestOutput) -> None:
        self.num_prompt_tokens = len(output.prompt_token_ids or [])
        self.num_cached_tokens = output.num_cached_tokens or 0
        self.num_output_tokens += len(output.outputs[0].token_ids or [])
        if output.kv_transfer_params is not None:
            self.kv_transfer_params = output.kv_transfer_params
        self.parser.process(output.outputs[0])
        output_token_ids = output.outputs[0].token_ids or []
        self._accumulated_token_ids.extend(output_token_ids)

        # only store if enable_response_messages is True, save memory
        if self.request.enable_response_messages:
            output_prompt = output.prompt or ""
            output_prompt_token_ids = output.prompt_token_ids or []
            if len(self.input_messages) == 0:
                self.input_messages.append(
                    ResponseRawMessageAndToken(
                        message=output_prompt,
                        tokens=output_prompt_token_ids,
                    )
                )
            else:
                self.output_messages.append(
                    ResponseRawMessageAndToken(
                        message=output_prompt,
                        tokens=output_prompt_token_ids,
                    )
                )
            self.output_messages.append(
                ResponseRawMessageAndToken(
                    message=output.outputs[0].text,
                    tokens=output.outputs[0].token_ids,
                )
            )

    defappend_tool_output(self, output: list[ResponseInputOutputItem]) -> None:
        self.parser.response_messages.extend(output)

    defneed_builtin_tool_call(self) -> bool:
"""Return true if the last message is a builtin tool call
        that the request has enabled."""
        last_message = self.parser.response_messages[-1]
        if last_message.type != "function_call":
            return False
        if last_message.name in ("code_interpreter", "python"):
            return "python" in self.available_tools
        if last_message.name == "web_search_preview":
            return "browser" in self.available_tools
        if last_message.name.startswith("container"):
            return "container" in self.available_tools
        return False

    async defcall_python_tool(
        self, tool_session: Union["ClientSession", Tool], last_msg: FunctionCall
    ) -> list[ResponseInputOutputItem]:
        self.called_tools.add("python")
        if isinstance(tool_session, Tool):
            return await tool_session.get_result_parsable_context(self)
        args = json.loads(last_msg.arguments)
        param = {
            "code": args["code"],
        }
        result = await tool_session.call_tool("python", param)
        result_str = result.content[0].text

        message = ResponseFunctionToolCallOutputItem(
            id=f"mcpo_{random_uuid()}",
            type="function_call_output",
            call_id=f"call_{random_uuid()}",
            output=result_str,
            status="completed",
        )

        return [message]

    async defcall_search_tool(
        self, tool_session: Union["ClientSession", Tool], last_msg: FunctionCall
    ) -> list[ResponseInputOutputItem]:
        self.called_tools.add("browser")
        if isinstance(tool_session, Tool):
            return await tool_session.get_result_parsable_context(self)
        if envs.VLLM_TOOL_JSON_ERROR_AUTOMATIC_RETRY:
            try:
                args = json.loads(last_msg.arguments)
            except json.JSONDecodeError as e:
                return _create_json_parse_error_messages(last_msg, e)
        else:
            args = json.loads(last_msg.arguments)
        result = await tool_session.call_tool("search", args)
        result_str = result.content[0].text

        message = ResponseFunctionToolCallOutputItem(
            id=f"fco_{random_uuid()}",
            type="function_call_output",
            call_id=f"call_{random_uuid()}",
            output=result_str,
            status="completed",
        )

        return [message]

    async defcall_container_tool(
        self, tool_session: Union["ClientSession", Tool], last_msg: Message
    ) -> list[Message]:
"""
        Call container tool. Expect this to be run in a stateful docker
        with command line terminal.
        The official container tool would at least
        expect the following format:
        - for tool name: exec
            - args:
                {
                    "cmd":List[str] "command to execute",
                    "workdir":optional[str] "current working directory",
                    "env":optional[object/dict] "environment variables",
                    "session_name":optional[str] "session name",
                    "timeout":optional[int] "timeout in seconds",
                    "user":optional[str] "user name",
                }
        """
        self.called_tools.add("container")
        if isinstance(tool_session, Tool):
            return await tool_session.get_result_parsable_context(self)
        # tool_name = last_msg.recipient.split(".")[1].split(" ")[0]
        if envs.VLLM_TOOL_JSON_ERROR_AUTOMATIC_RETRY:
            try:
                args = json.loads(last_msg.arguments)
            except json.JSONDecodeError as e:
                return _create_json_parse_error_messages(last_msg, e)
        else:
            args = json.loads(last_msg.arguments)
        result = await tool_session.call_tool("exec", args)
        result_str = result.content[0].text

        message = ResponseFunctionToolCallOutputItem(
            id=f"fco_{random_uuid()}",
            type="function_call_output",
            call_id=f"call_{random_uuid()}",
            output=result_str,
            status="completed",
        )

        return [message]

    async defcall_tool(self) -> list[ResponseInputOutputItem]:
        if not self.parser.response_messages:
            return []
        last_msg = self.parser.response_messages[-1]
        # change this to a mcp_ function call
        last_msg.id = f"{MCP_PREFIX}{random_uuid()}"
        self.parser.response_messages[-1] = last_msg
        if last_msg.name == "code_interpreter":
            return await self.call_python_tool(self._tool_sessions["python"], last_msg)
        elif last_msg.name == "web_search_preview":
            return await self.call_search_tool(self._tool_sessions["browser"], last_msg)
        elif last_msg.name.startswith("container"):
            return await self.call_container_tool(
                self._tool_sessions["container"], last_msg
            )
        return []

    defrender_for_completion(self):
        raise NotImplementedError("Should not be called.")

    async definit_tool_sessions(
        self,
        tool_server: ToolServer | None,
        exit_stack: AsyncExitStack,
        request_id: str,
        mcp_tools: dict[str, Mcp],
    ):
        if tool_server:
            for tool_name in self.available_tools:
                if tool_name in self._tool_sessions:
                    continue

                tool_type = _map_tool_name_to_tool_type(tool_name)
                headers = (
                    mcp_tools[tool_type].headers if tool_type in mcp_tools else None
                )
                tool_session = await exit_stack.enter_async_context(
                    tool_server.new_session(tool_name, request_id, headers)
                )
                self._tool_sessions[tool_name] = tool_session
                exit_stack.push_async_exit(self.cleanup_session)

    async defcleanup_session(self, *args, **kwargs) -> None:
"""Can be used as coro to used in __aexit__"""

        async defcleanup_tool_session(tool_session):
            if not isinstance(tool_session, Tool):
                logger.info(
                    "Cleaning up tool session for %s", tool_session._client_info
                )
                with contextlib.suppress(Exception):
                    await tool_session.call_tool("cleanup_session", {})

        await asyncio.gather(
            *(
                cleanup_tool_session(self._tool_sessions[tool])
                for tool in self.called_tools
            )
        )
```

### call\_container\_tool `async` [¶](#vllm.entrypoints.openai.responses.context.ParsableContext.call_container_tool "Permanent link")

```
call_container_tool(
    tool_session: Union[ClientSession, Tool],
    last_msg: Message,
) -> list[Message]
```

Call container tool. Expect this to be run in a stateful docker with command line terminal. The official container tool would at least expect the following format: - for tool name: exec - args: { "cmd":List\[str] "command to execute", "workdir":optional\[str] "current working directory", "env":optional\[object/dict] "environment variables", "session\_name":optional\[str] "session name", "timeout":optional\[int] "timeout in seconds", "user":optional\[str] "user name", }

Source code in `vllm/entrypoints/openai/responses/context.py`

```
async defcall_container_tool(
    self, tool_session: Union["ClientSession", Tool], last_msg: Message
) -> list[Message]:
"""
    Call container tool. Expect this to be run in a stateful docker
    with command line terminal.
    The official container tool would at least
    expect the following format:
    - for tool name: exec
        - args:
            {
                "cmd":List[str] "command to execute",
                "workdir":optional[str] "current working directory",
                "env":optional[object/dict] "environment variables",
                "session_name":optional[str] "session name",
                "timeout":optional[int] "timeout in seconds",
                "user":optional[str] "user name",
            }
    """
    self.called_tools.add("container")
    if isinstance(tool_session, Tool):
        return await tool_session.get_result_parsable_context(self)
    # tool_name = last_msg.recipient.split(".")[1].split(" ")[0]
    if envs.VLLM_TOOL_JSON_ERROR_AUTOMATIC_RETRY:
        try:
            args = json.loads(last_msg.arguments)
        except json.JSONDecodeError as e:
            return _create_json_parse_error_messages(last_msg, e)
    else:
        args = json.loads(last_msg.arguments)
    result = await tool_session.call_tool("exec", args)
    result_str = result.content[0].text

    message = ResponseFunctionToolCallOutputItem(
        id=f"fco_{random_uuid()}",
        type="function_call_output",
        call_id=f"call_{random_uuid()}",
        output=result_str,
        status="completed",
    )

    return [message]
```

### cleanup\_session `async` [¶](#vllm.entrypoints.openai.responses.context.ParsableContext.cleanup_session "Permanent link")

```
cleanup_session(*args, **kwargs) -> None
```

Can be used as coro to used in **aexit**

Source code in `vllm/entrypoints/openai/responses/context.py`

```
async defcleanup_session(self, *args, **kwargs) -> None:
"""Can be used as coro to used in __aexit__"""

    async defcleanup_tool_session(tool_session):
        if not isinstance(tool_session, Tool):
            logger.info(
                "Cleaning up tool session for %s", tool_session._client_info
            )
            with contextlib.suppress(Exception):
                await tool_session.call_tool("cleanup_session", {})

    await asyncio.gather(
        *(
            cleanup_tool_session(self._tool_sessions[tool])
            for tool in self.called_tools
        )
    )
```

### need\_builtin\_tool\_call [¶](#vllm.entrypoints.openai.responses.context.ParsableContext.need_builtin_tool_call "Permanent link")

```
need_builtin_tool_call() -> bool
```

Return true if the last message is a builtin tool call that the request has enabled.

Source code in `vllm/entrypoints/openai/responses/context.py`

```
defneed_builtin_tool_call(self) -> bool:
"""Return true if the last message is a builtin tool call
    that the request has enabled."""
    last_message = self.parser.response_messages[-1]
    if last_message.type != "function_call":
        return False
    if last_message.name in ("code_interpreter", "python"):
        return "python" in self.available_tools
    if last_message.name == "web_search_preview":
        return "browser" in self.available_tools
    if last_message.name.startswith("container"):
        return "container" in self.available_tools
    return False
```

## SimpleContext [¶](#vllm.entrypoints.openai.responses.context.SimpleContext "Permanent link")

Bases: `ConversationContext`

This is a context that cannot handle MCP tool calls

Source code in `vllm/entrypoints/openai/responses/context.py`

```
classSimpleContext(ConversationContext):
"""This is a context that cannot handle MCP tool calls"""

    def__init__(self):
        self.last_output = None

        # Accumulated final output for streaming mode
        self._accumulated_text: str = ""
        self._accumulated_token_ids: list[int] = []
        self._accumulated_logprobs: list = []

        self.num_prompt_tokens = 0
        self.num_output_tokens = 0
        self.num_cached_tokens = 0
        # todo num_reasoning_tokens is not implemented yet.
        self.num_reasoning_tokens = 0
        # not implemented yet for SimpleContext
        self.all_turn_metrics = []

        self.input_messages: list[ResponseRawMessageAndToken] = []
        self.kv_transfer_params: dict[str, Any] | None = None

    defappend_output(self, output) -> None:
        self.last_output = output
        if not isinstance(output, RequestOutput):
            raise ValueError("SimpleContext only supports RequestOutput.")
        self.num_prompt_tokens = len(output.prompt_token_ids or [])
        self.num_cached_tokens = output.num_cached_tokens or 0
        self.num_output_tokens += len(output.outputs[0].token_ids or [])
        if output.kv_transfer_params is not None:
            self.kv_transfer_params = output.kv_transfer_params

        # Accumulate text, token_ids, and logprobs for streaming mode
        delta_output = output.outputs[0]
        self._accumulated_text += delta_output.text
        self._accumulated_token_ids.extend(delta_output.token_ids)
        if delta_output.logprobs is not None:
            self._accumulated_logprobs.extend(delta_output.logprobs)

        if len(self.input_messages) == 0:
            output_prompt = output.prompt or ""
            output_prompt_token_ids = output.prompt_token_ids or []
            self.input_messages.append(
                ResponseRawMessageAndToken(
                    message=output_prompt,
                    tokens=output_prompt_token_ids,
                )
            )

    @property
    defoutput_messages(self) -> list[ResponseRawMessageAndToken]:
"""Return consolidated output as a single message.

        In streaming mode, text and tokens are accumulated across many deltas.
        This property returns them as a single entry rather than one per delta.
        """
        if not self._accumulated_text and not self._accumulated_token_ids:
            return []
        return [
            ResponseRawMessageAndToken(
                message=self._accumulated_text,
                tokens=list(self._accumulated_token_ids),
            )
        ]

    @property
    deffinal_output(self) -> RequestOutput | None:
"""Return the final output, with complete text/token_ids/logprobs."""
        if self.last_output is not None and self.last_output.outputs:
            assert isinstance(self.last_output, RequestOutput)
            final_output = copy.copy(self.last_output)
            # copy inner item to avoid modify last_output
            final_output.outputs = [replace(item) for item in self.last_output.outputs]
            final_output.outputs[0].text = self._accumulated_text
            final_output.outputs[0].token_ids = tuple(self._accumulated_token_ids)
            if self._accumulated_logprobs:
                final_output.outputs[0].logprobs = self._accumulated_logprobs
            return final_output
        return self.last_output

    defappend_tool_output(self, output) -> None:
        raise NotImplementedError("Should not be called.")

    defneed_builtin_tool_call(self) -> bool:
        return False

    async defcall_tool(self) -> list[Message]:
        raise NotImplementedError("Should not be called.")

    defrender_for_completion(self) -> list[int]:
        raise NotImplementedError("Should not be called.")

    async definit_tool_sessions(
        self,
        tool_server: ToolServer | None,
        exit_stack: AsyncExitStack,
        request_id: str,
        mcp_tools: dict[str, Mcp],
    ) -> None:
        pass

    async defcleanup_session(self) -> None:
        raise NotImplementedError("Should not be called.")
```

### final\_output `property` [¶](#vllm.entrypoints.openai.responses.context.SimpleContext.final_output "Permanent link")

Return the final output, with complete text/token\_ids/logprobs.

### output\_messages `property` [¶](#vllm.entrypoints.openai.responses.context.SimpleContext.output_messages "Permanent link")

Return consolidated output as a single message.

In streaming mode, text and tokens are accumulated across many deltas. This property returns them as a single entry rather than one per delta.

## TurnMetrics [¶](#vllm.entrypoints.openai.responses.context.TurnMetrics "Permanent link")

Tracks token and toolcall details for a single conversation turn.

Source code in `vllm/entrypoints/openai/responses/context.py`

```
classTurnMetrics:
"""Tracks token and toolcall details for a single conversation turn."""

    def__init__(
        self,
        input_tokens: int = 0,
        output_tokens: int = 0,
        cached_input_tokens: int = 0,
        tool_output_tokens: int = 0,
    ) -> None:
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.cached_input_tokens = cached_input_tokens
        self.tool_output_tokens = tool_output_tokens

    defreset(self) -> None:
"""Reset counters for a new turn."""
        self.input_tokens = 0
        self.output_tokens = 0
        self.cached_input_tokens = 0
        self.tool_output_tokens = 0

    defcopy(self) -> "TurnMetrics":
"""Create a copy of this turn's token counts."""
        return TurnMetrics(
            self.input_tokens,
            self.output_tokens,
            self.cached_input_tokens,
            self.tool_output_tokens,
        )
```

### copy [¶](#vllm.entrypoints.openai.responses.context.TurnMetrics.copy "Permanent link")

Create a copy of this turn's token counts.

Source code in `vllm/entrypoints/openai/responses/context.py`

```
defcopy(self) -> "TurnMetrics":
"""Create a copy of this turn's token counts."""
    return TurnMetrics(
        self.input_tokens,
        self.output_tokens,
        self.cached_input_tokens,
        self.tool_output_tokens,
    )
```

### reset [¶](#vllm.entrypoints.openai.responses.context.TurnMetrics.reset "Permanent link")

Reset counters for a new turn.

Source code in `vllm/entrypoints/openai/responses/context.py`

```
defreset(self) -> None:
"""Reset counters for a new turn."""
    self.input_tokens = 0
    self.output_tokens = 0
    self.cached_input_tokens = 0
    self.tool_output_tokens = 0
```

## \_create\_json\_parse\_error\_messages [¶](#vllm.entrypoints.openai.responses.context._create_json_parse_error_messages "Permanent link")

Creates an error message when json parse failed.

Source code in `vllm/entrypoints/openai/responses/context.py`

```
def_create_json_parse_error_messages(
    last_msg: Message, e: json.JSONDecodeError
) -> list[Message]:
"""
    Creates an error message when json parse failed.
    """
    error_msg = (
        f"Error parsing tool arguments as JSON: {str(e)}. "
        "Please ensure the tool call arguments are valid JSON and try again."
    )
    content = TextContent(text=error_msg)
    author = Author(role=Role.TOOL, name=last_msg.recipient)
    return [
        Message(
            author=author,
            content=[content],
            recipient=Role.ASSISTANT,
            channel=last_msg.channel,
        )
    ]
```