---
title: io_processor - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/base/io_processor/
source: sitemap
fetched_at: 2026-05-07T21:20:47.230103531-03:00
rendered_js: false
word_count: 0
summary: This document defines the ClassPoolingIOProcessor class, which manages the preprocessing and postprocessing of pooling requests for both online serving and offline batch operations within the vLLM framework.
tags:
    - pooling-processor
    - request-handling
    - data-preprocessing
    - chat-template
    - vllm-framework
    - offline-processing
category: reference
---

```
classPoolingIOProcessor:
"""Processor for handling preprocessing & postprocessing ops for pooling requests.

    This class manages both online (serving) and offline (batch) processing of pooling
    requests, handling chat and completion formats.
    """

    name: str

    def__init__(
        self,
        vllm_config: VllmConfig,
        renderer: BaseRenderer,
        chat_template_config: ChatTemplateConfig,
    ):
        self.vllm_config = vllm_config
        self.model_config = vllm_config.model_config
        self.renderer = renderer

        self.chat_template = chat_template_config.chat_template
        self.chat_template_content_format: Final = (
            chat_template_config.chat_template_content_format
        )
        self.trust_request_chat_template = (
            chat_template_config.trust_request_chat_template
        )

    #######################################
    # online APIs

    defcreate_pooling_params(self, request):
        return request.to_pooling_params()

    defpre_process_online(self, ctx: PoolingServeContext):
        request = ctx.request

        if isinstance(request, PoolingChatLikeRequest):
            self._validate_chat_template(
                request_chat_template=request.chat_template,
                chat_template_kwargs=request.chat_template_kwargs,
                trust_request_chat_template=self.trust_request_chat_template,
            )
            _, engine_inputs = self._preprocess_chat_online(
                request,
                request.messages,
                default_template=self.chat_template,
                default_template_content_format=self.chat_template_content_format,
                default_template_kwargs=None,
            )
        elif isinstance(request, PoolingCompletionLikeRequest):
            engine_inputs = self._preprocess_cmpl_online(
                request,
                prompt_input=request.input,
                prompt_embeds=None,
            )
        else:
            raise ValueError(f"Invalid {self.name} request type")

        ctx.engine_inputs = engine_inputs

    defpost_process_online(
        self,
        ctx: PoolingServeContext,
    ):
        pass

    #######################################
    # offline APIs

    defpre_process_offline(self, ctx: OfflineInputsContext) -> Sequence[EngineInput]:
        assert not isinstance(ctx.prompts, ScoringData) and not (
            isinstance(ctx.prompts, dict) and "data" in ctx.prompts
        )

        prompts_seq = prompt_to_seq(ctx.prompts)
        tok_params = self.renderer.default_cmpl_tok_params.with_kwargs(
            **(ctx.tokenization_kwargs or {})
        )
        return self._preprocess_cmpl_offline(prompts=prompts_seq, tok_params=tok_params)

    defpost_process_offline(
        self,
        ctx: OfflineOutputsContext,
    ) -> list[PoolingRequestOutput]:
        return ctx.outputs

    #######################################
    # helpers

    def_preprocess_cmpl_online(
        self,
        request: RendererRequest,
        prompt_input: str | list[str] | list[int] | list[list[int]] | None,
        prompt_embeds: bytes | list[bytes] | None,
    ) -> list[EngineInput]:
        renderer = self.renderer
        model_config = self.model_config

        prompts = list[SingletonPrompt | bytes]()
        if prompt_embeds is not None:  # embeds take higher priority
            prompts.extend(prompt_to_seq(prompt_embeds))
        if prompt_input is not None:
            prompts.extend(prompt_to_seq(prompt_input))

        parsed_prompts = [
            (
                prompt
                if isinstance(prompt, bytes)
                else parse_model_prompt(model_config, prompt)
            )
            for prompt in prompts
        ]
        tok_params = request.build_tok_params(model_config)

        return renderer.render_cmpl(
            parsed_prompts,
            tok_params,
            prompt_extras={
                k: v
                for k in ("mm_processor_kwargs", "cache_salt")
                if (v := getattr(request, k, None)) is not None
            },
        )

    def_preprocess_chat_online(
        self,
        request: RendererChatRequest,
        messages: list[ChatCompletionMessageParam],
        default_template: str | None,
        default_template_content_format: ChatTemplateContentFormatOption,
        default_template_kwargs: dict[str, Any] | None,
        tool_dicts: list[dict[str, Any]] | None = None,
        tool_parser: type[ToolParser] | None = None,
    ) -> tuple[list[ConversationMessage], list[EngineInput]]:
        renderer = self.renderer

        default_template_kwargs = merge_kwargs(
            default_template_kwargs,
            dict(
                tools=tool_dicts,
                tokenize=is_mistral_tokenizer(renderer.tokenizer),
            ),
        )

        mm_config = self.model_config.multimodal_config

        tok_params = request.build_tok_params(self.model_config)
        chat_params = request.build_chat_params(
            default_template, default_template_content_format
        ).with_defaults(
            default_template_kwargs,
            default_media_io_kwargs=(mm_config.media_io_kwargs if mm_config else None),
        )

        (conversation,), (engine_input,) = renderer.render_chat(
            [messages],
            chat_params,
            tok_params,
            prompt_extras={
                k: v
                for k in ("mm_processor_kwargs", "cache_salt")
                if (v := getattr(request, k, None)) is not None
            },
        )

        return conversation, [engine_input]

    def_preprocess_cmpl_offline(
        self,
        prompts: PromptType | Sequence[PromptType],
        tok_params: TokenizeParams,
        prompt_extras: dict[str, Any] | None = None,
    ) -> Sequence[EngineInput]:
        prompts = prompt_to_seq(prompts)
        parsed_prompts = [
            (
                prompt
                if isinstance(prompt, bytes)
                else parse_model_prompt(self.model_config, prompt)
            )
            for prompt in prompts
        ]

        return self.renderer.render_cmpl(
            parsed_prompts, tok_params, prompt_extras=prompt_extras
        )

    def_validate_chat_template(
        self,
        request_chat_template: str | None,
        chat_template_kwargs: dict[str, Any] | None,
        trust_request_chat_template: bool,
    ):
        if not trust_request_chat_template and (
            request_chat_template is not None
            or (
                chat_template_kwargs
                and chat_template_kwargs.get("chat_template") is not None
            )
        ):
            raise ValueError(
                "Chat template is passed with request, but "
                "--trust-request-chat-template is not set. "
                "Refused request with untrusted chat template."
            )
        return None

    def_params_to_seq(
        self,
        params: PoolingParams | Sequence[PoolingParams],
        num_requests: int,
    ) -> Sequence[PoolingParams]:
        if isinstance(params, Sequence):
            if len(params) != num_requests:
                raise ValueError(
                    f"The lengths of prompts ({num_requests}) "
                    f"and params ({len(params)}) must be the same."
                )

            return params

        return [params] * num_requests
```