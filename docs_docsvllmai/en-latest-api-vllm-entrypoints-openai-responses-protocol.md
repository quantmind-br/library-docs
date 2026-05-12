---
title: protocol - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/responses/protocol/
source: sitemap
fetched_at: 2026-05-07T21:20:31.066938538-03:00
rendered_js: false
word_count: 21
summary: This document defines the ClassResponsesRequest model, which encapsulates the parameters for handling AI inference requests, including configuration for sampling, token management, and specific request metadata.
tags:
    - api-model
    - inference-parameters
    - data-schema
    - request-handling
    - python-pydantic
category: reference
---

```
classResponsesRequest(OpenAIBaseModel):
    # Ordered by official OpenAI API documentation
    # https://platform.openai.com/docs/api-reference/responses/create
    background: bool | None = False
    include: (
        list[
            Literal[
                "code_interpreter_call.outputs",
                "computer_call_output.output.image_url",
                "file_search_call.results",
                "message.input_image.image_url",
                "message.output_text.logprobs",
                "reasoning.encrypted_content",
            ],
        ]
        | None
    ) = None
    input: str | list[ResponseInputOutputItem]
    instructions: str | None = None
    max_output_tokens: int | None = None
    max_tool_calls: int | None = None
    metadata: Metadata | None = None
    model: str | None = None
    logit_bias: dict[str, float] | None = None
    parallel_tool_calls: bool | None = True
    previous_response_id: str | None = None
    prompt: ResponsePrompt | None = None
    reasoning: Reasoning | None = None
    service_tier: Literal["auto", "default", "flex", "scale", "priority"] = "auto"
    store: bool | None = True
    stream: bool | None = False
    temperature: float | None = None
    text: ResponseTextConfig | None = None
    tool_choice: ToolChoice = "auto"
    tools: list[Tool] = Field(default_factory=list)
    top_logprobs: int | None = 0
    top_p: float | None = None
    top_k: int | None = None
    truncation: Literal["auto", "disabled"] | None = "disabled"
    user: str | None = None
    skip_special_tokens: bool = True
    include_stop_str_in_output: bool = False
    presence_penalty: float | None = Field(
        default=None,
        ge=-2.0,
        le=2.0,
        description=(
            "The presence penalty that was used to penalize new tokens based on "
            "whether they appear in the text so far."
        ),
    )
    frequency_penalty: float | None = Field(
        default=None,
        ge=-2.0,
        le=2.0,
        description=(
            "The frequency penalty that was used to penalize new tokens based on "
            "their frequency in the text so far."
        ),
    )
    prompt_cache_key: str | None = Field(
        default=None,
        description=(
            "A key that was used to read from or write to the prompt cache."
            "Note: This field has not been implemented yet "
            "and vLLM will ignore it."
        ),
    )

    # --8<-- [start:responses-extra-params]
    request_id: str = Field(
        default_factory=lambda: f"resp_{random_uuid()}",
        description=(
            "The request_id related to this request. If the caller does "
            "not set it, a random_uuid will be generated. This id is used "
            "through out the inference process and return in response."
        ),
    )
    media_io_kwargs: dict[str, dict[str, Any]] | None = Field(
        default=None,
        description=(
            "Additional kwargs to pass to the media IO connectors, "
            "keyed by modality. Merged with engine-level media_io_kwargs."
        ),
    )
    mm_processor_kwargs: dict[str, Any] | None = Field(
        default=None,
        description=("Additional kwargs to pass to the HF processor."),
    )
    priority: int = Field(
        default=0,
        ge=_INT64_MIN,
        le=_INT64_MAX,
        description=(
            "The priority of the request (lower means earlier handling; "
            "default: 0). Any priority other than 0 will raise an error "
            "if the served model does not use priority scheduling."
        ),
    )
    cache_salt: str | None = Field(
        default=None,
        description=(
            "If specified, the prefix cache will be salted with the provided "
            "string to prevent an attacker to guess prompts in multi-user "
            "environments. The salt should be random, protected from "
            "access by 3rd parties, and long enough to be "
            "unpredictable (e.g., 43 characters base64-encoded, corresponding "
            "to 256 bit)."
        ),
    )

    enable_response_messages: bool = Field(
        default=False,
        description=(
            "Dictates whether or not to return messages as part of the "
            "response object. Currently only supported for non-background."
        ),
    )
    # similar to input_messages / output_messages in ResponsesResponse
    # we take in previous_input_messages (ie in harmony format)
    # this cannot be used in conjunction with previous_response_id
    # TODO: consider supporting non harmony messages as well
    previous_input_messages: list[OpenAIHarmonyMessage | dict] | None = None
    structured_outputs: StructuredOutputsParams | None = Field(
        default=None,
        description="Additional kwargs for structured outputs",
    )

    repetition_penalty: float | None = None
    seed: int | None = Field(None, ge=_INT64_MIN, le=_INT64_MAX)
    stop: str | list[str] | None = []
    ignore_eos: bool = False
    vllm_xargs: dict[str, str | int | float | list[str | int | float]] | None = Field(
        default=None,
        description=(
            "Additional request parameters with (list of) string or "
            "numeric values, used by custom extensions."
        ),
    )
    kv_transfer_params: dict[str, Any] | None = Field(
        default=None,
        description="KVTransfer parameters used for disaggregated serving.",
    )
    # --8<-- [end:responses-extra-params]

    defbuild_chat_params(
        self,
        default_template: str | None,
        default_template_content_format: ChatTemplateContentFormatOption,
    ) -> ChatParams:
        from.utilsimport should_continue_final_message

        # Check if we should continue the final message (partial completion)
        # This enables Anthropic-style partial message completion where the
        # user provides an incomplete assistant message to continue from.
        continue_final = should_continue_final_message(self.input)

        reasoning = self.reasoning

        return ChatParams(
            chat_template=default_template,
            chat_template_content_format=default_template_content_format,
            chat_template_kwargs=merge_kwargs(  # To remove unset values
                {},
                dict(
                    add_generation_prompt=not continue_final,
                    continue_final_message=continue_final,
                    reasoning_effort=None if reasoning is None else reasoning.effort,
                ),
            ),
            media_io_kwargs=self.media_io_kwargs,
        )

    defbuild_tok_params(self, model_config: ModelConfig) -> TokenizeParams:
        return TokenizeParams(
            max_total_tokens=model_config.max_model_len,
            max_output_tokens=self.max_output_tokens or 0,
            truncate_prompt_tokens=-1 if self.truncation != "disabled" else None,
            max_total_tokens_param="max_model_len",
            max_output_tokens_param="max_output_tokens",
        )

    _DEFAULT_SAMPLING_PARAMS = {
        "temperature": 1.0,
        "top_p": 1.0,
        "top_k": 0,
    }

    defto_sampling_params(
        self,
        default_max_tokens: int,
        default_sampling_params: dict | None = None,
    ) -> SamplingParams:
        if self.max_output_tokens is None:
            max_tokens = default_max_tokens
        else:
            max_tokens = min(self.max_output_tokens, default_max_tokens)

        default_sampling_params = default_sampling_params or {}
        if (temperature := self.temperature) is None:
            temperature = default_sampling_params.get(
                "temperature", self._DEFAULT_SAMPLING_PARAMS["temperature"]
            )
        if (top_p := self.top_p) is None:
            top_p = default_sampling_params.get(
                "top_p", self._DEFAULT_SAMPLING_PARAMS["top_p"]
            )
        if (top_k := self.top_k) is None:
            top_k = default_sampling_params.get(
                "top_k", self._DEFAULT_SAMPLING_PARAMS["top_k"]
            )

        if (repetition_penalty := self.repetition_penalty) is None:
            repetition_penalty = default_sampling_params.get("repetition_penalty", 1.0)

        if (presence_penalty := self.presence_penalty) is None:
            presence_penalty = default_sampling_params.get("presence_penalty", 0.0)

        if (frequency_penalty := self.frequency_penalty) is None:
            frequency_penalty = default_sampling_params.get("frequency_penalty", 0.0)

        stop_token_ids = default_sampling_params.get("stop_token_ids")

        # Structured output
        structured_outputs = self.structured_outputs

        # Also check text.format for OpenAI-style json_schema
        if self.text is not None and self.text.format is not None:
            if structured_outputs is not None:
                raise VLLMValidationError(
                    "Cannot specify both structured_outputs and text.format",
                    parameter="structured_outputs",
                )
            response_format = self.text.format
            if (
                response_format.type == "json_schema"
                and response_format.schema_ is not None
            ):
                structured_outputs = StructuredOutputsParams(
                    json=response_format.schema_  # type: ignore[call-arg]
                    # --follow-imports skip hides the class definition but also hides
                    # multiple third party conflicts, so best of both evils
                )

        stop = self.stop if self.stop else []
        if isinstance(stop, str):
            stop = [stop]

        extra_args: dict[str, Any] = self.vllm_xargs if self.vllm_xargs else {}
        if self.kv_transfer_params:
            extra_args["kv_transfer_params"] = self.kv_transfer_params

        return SamplingParams.from_optional(
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            max_tokens=max_tokens,
            logprobs=self.top_logprobs if self.is_include_output_logprobs() else None,
            stop_token_ids=stop_token_ids,
            stop=stop,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            repetition_penalty=repetition_penalty,
            seed=self.seed,
            ignore_eos=self.ignore_eos,
            output_kind=(
                RequestOutputKind.DELTA if self.stream else RequestOutputKind.FINAL_ONLY
            ),
            structured_outputs=structured_outputs,
            logit_bias=self.logit_bias,
            extra_args=extra_args,
            skip_clone=True,  # Created fresh per request, safe to skip clone
            skip_special_tokens=self.skip_special_tokens,
            include_stop_str_in_output=self.include_stop_str_in_output,
        )

    defis_include_output_logprobs(self) -> bool:
"""Check if the request includes output logprobs."""
        if self.include is None:
            return False
        return (
            isinstance(self.include, list)
            and "message.output_text.logprobs" in self.include
        )

    @model_validator(mode="before")
    @classmethod
    defvalidate_background(cls, data):
        if not data.get("background"):
            return data
        if not data.get("store", True):
            raise VLLMValidationError(
                "background can only be used when `store` is true",
                parameter="background",
            )
        return data

    @model_validator(mode="before")
    @classmethod
    defvalidate_prompt(cls, data):
        if data.get("prompt") is not None:
            raise VLLMValidationError(
                "prompt template is not supported", parameter="prompt"
            )
        return data

    @model_validator(mode="before")
    @classmethod
    defcheck_cache_salt_support(cls, data):
        if data.get("cache_salt") is not None and (
            not isinstance(data["cache_salt"], str) or not data["cache_salt"]
        ):
            raise VLLMValidationError(
                "Parameter 'cache_salt' must be a non-empty string if provided.",
                parameter="cache_salt",
            )
        return data

    @model_validator(mode="before")
    @classmethod
    definput_item_parsing(cls, data):
"""Parse input items that are missing required fields or that Pydantic
        cannot disambiguate in a Union of TypedDict / BaseModel types.

        Specifically handles:
        - function_call -> ResponseFunctionToolCall
        - reasoning     -> ResponseReasoningItem (auto-generates id)
        - message(role=assistant) -> ResponseOutputMessage (auto-generates
          id/status and annotations)

        Invalid structures are left for Pydantic to reject.
        """
        input_data = data.get("input")

        # Early return for None, strings, or bytes
        if input_data is None or isinstance(input_data, (str, bytes)):
            return data

        # Convert iterators (like ValidatorIterator) to list
        if not isinstance(input_data, list):
            try:
                input_data = list(input_data)
            except TypeError:
                # Not iterable, leave as-is for Pydantic to handle
                return data

        processed_input = []
        for item in input_data:
            if not isinstance(item, dict):
                processed_input.append(item)
                continue

            item_type = item.get("type")

            if item_type == "function_call":
                try:
                    processed_input.append(ResponseFunctionToolCall(**item))
                except ValidationError:
                    logger.debug(
                        "Failed to parse function_call to ResponseFunctionToolCall, "
                        "leaving for Pydantic validation"
                    )
                    processed_input.append(item)

            elif item_type == "reasoning":
                if "id" not in item:
                    item = {**item, "id": f"rs_{random_uuid()}"}
                try:
                    processed_input.append(ResponseReasoningItem(**item))
                except ValidationError:
                    logger.debug(
                        "Failed to parse reasoning to ResponseReasoningItem, "
                        "leaving for Pydantic validation"
                    )
                    processed_input.append(item)

            elif item_type == "message" and item.get("role") == "assistant":
                item = dict(item)
                if "id" not in item:
                    item["id"] = f"msg_{random_uuid()}"
                if "status" not in item:
                    item["status"] = "completed"
                # ResponseOutputText requires annotations
                if isinstance(item.get("content"), list):
                    new_content = []
                    for c in item["content"]:
                        if (
                            isinstance(c, dict)
                            and c.get("type") == "output_text"
                            and "annotations" not in c
                        ):
                            c = {**c, "annotations": []}
                        new_content.append(c)
                    item["content"] = new_content
                try:
                    processed_input.append(ResponseOutputMessage(**item))
                except ValidationError:
                    logger.debug(
                        "Failed to parse assistant message to ResponseOutputMessage, "
                        "leaving for Pydantic validation"
                    )
                    processed_input.append(item)

            else:
                processed_input.append(item)

        data["input"] = processed_input
        return data

    @model_validator(mode="before")
    @classmethod
    defcheck_tool_usage(cls, data):
        if not isinstance(data, dict):
            return data

        tools = data.get("tools")
        tool_choice = data.get("tool_choice", "auto")
        has_tools = tools is not None and len(tools) > 0
        is_named_tool_choice = (
            isinstance(tool_choice, dict) and tool_choice.get("type") == "function"
        )

        if not has_tools:
            if tool_choice in ("auto", "none"):
                data["tool_choice"] = "none"
            elif tool_choice == "required":
                raise VLLMValidationError(
                    "Tool choice 'required' must be specified with 'tools' parameter.",
                    parameter="tool_choice",
                )
            elif is_named_tool_choice:
                raise VLLMValidationError(
                    "Tool choice 'function' not found in 'tools' parameter.",
                    parameter="tool_choice",
                )
        elif is_named_tool_choice and tools is not None:
            tool_name = tool_choice.get("name")
            tool_names = {
                t.get("name") if isinstance(t, dict) else getattr(t, "name", None)
                for t in tools
            }
            if not tool_name or tool_name not in tool_names:
                raise VLLMValidationError(
                    "Tool choice 'function' not found in 'tools' parameter.",
                    parameter="tool_choice",
                )

        return data
```