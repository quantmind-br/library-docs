---
title: hf - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/renderers/hf/
source: sitemap
fetched_at: 2026-05-07T21:35:22.0759638-03:00
rendered_js: false
word_count: 29
summary: This class implements a Hugging Face-based renderer responsible for processing chat messages, applying tokenization, and integrating multimodal data and prompt embeddings for inference engines.
tags:
    - hugging-face
    - multimodal
    - renderer
    - tokenization
    - chat-template
    - prompt-embeddings
category: api
---

```
classHfRenderer(BaseRenderer[HfTokenizer]):
    def__init__(
        self,
        config: VllmConfig,
        tokenizer: HfTokenizer | None,
    ) -> None:
        # Ensure the og tokenizer is never modified by maybe_make_thread_pool
        tokenizer = copy.copy(tokenizer)
        if (
            # Skip for mock configs and tokenizers
            getattr(config.model_config, "enable_prompt_embeds", False)
            and isinstance(tokenizer, HfTokenizer)
        ):
            _ensure_prompt_embeds_placeholder_token(tokenizer)
        super().__init__(config, tokenizer)

        self.use_unified_vision_chunk = getattr(
            config.model_config.hf_config, "use_unified_vision_chunk", False
        )

        self._apply_chat_template_async = make_async(
            safe_apply_chat_template, executor=self._executor
        )

        if self.tokenizer is not None:
            maybe_make_thread_pool(
                self.tokenizer, config.model_config.renderer_num_workers + 1
            )

    defrender_messages(
        self,
        messages: list[ChatCompletionMessageParam],
        params: ChatParams,
    ) -> tuple[list[ConversationMessage], DictPrompt]:
        model_config = self.model_config
        tokenizer = self.get_tokenizer()

        prompt_embeds_placeholder_token_id: int | None = None
        if model_config.enable_prompt_embeds:
            prompt_embeds_placeholder_token_id = (
                _ensure_prompt_embeds_placeholder_token(tokenizer)
            )

        conversation, mm_data, mm_uuids = parse_chat_messages(
            messages,
            model_config,
            content_format=resolve_chat_template_content_format(
                chat_template=params.chat_template,
                tools=params.chat_template_kwargs.get("tools"),
                given_format=params.chat_template_content_format,
                tokenizer=tokenizer,
                model_config=model_config,
            ),
            media_io_kwargs=params.media_io_kwargs,
            mm_processor_kwargs=params.mm_processor_kwargs,
        )

        # prompt_embeds tensors are carried by the tracker through mm_data,
        # but they must NOT be fed to the MM processor (which would reject
        # the unknown key). Extract them here.
        prompt_embeds_tensors: list[torch.Tensor] | None = None
        if mm_data is not None and "prompt_embeds" in mm_data:
            prompt_embeds_tensors = list(
                cast(Sequence[torch.Tensor], mm_data["prompt_embeds"])
            )
            mm_data = {k: v for k, v in mm_data.items() if k != "prompt_embeds"}
            if not mm_data:
                mm_data = None

        chat_template_kwargs = params.get_apply_chat_template_kwargs()
        if prompt_embeds_tensors:
            # prompt_embeds post-processing requires prompt_token_ids.
            if chat_template_kwargs.get("tokenize") is False:
                logger.warning_once(_TOKENIZE_OVERRIDE_WARNING)
            chat_template_kwargs["tokenize"] = True

        prompt_raw = safe_apply_chat_template(
            model_config,
            tokenizer,
            conversation,
            **chat_template_kwargs,
        )

        # NOTE: use_unified_vision_chunk is currently specific to Kimi-K2.5
        # model which uses unified vision chunks for both images and videos.
        if (
            self.use_unified_vision_chunk
            and mm_uuids is not None
            and mm_data is not None
        ):
            mm_uuids = rebuild_mm_uuids_from_mm_data(mm_uuids, mm_data)

            # get video placeholder, replace it with runtime video-chunk prompts
            video_placeholder = getattr(
                model_config.hf_config, "video_placeholder", None
            )
            prompt_raw = cast(
                list[int],
                replace_vision_chunk_video_placeholder(
                    prompt_raw,
                    mm_data,
                    video_placeholder,
                ),
            )

        prompt = parse_dec_only_prompt(prompt_raw)

        # When `prompt_embeds` is mixed with other modality data,
        # `_process_tokens` runs `_process_multimodal` first (expanding
        # `<|AUDIO|>` / `<|IMAGE|>` placeholders) and then
        # `_apply_prompt_embeds_to_engine_input` augments the result.
        # Stash the tensors and placeholder ID for that override to consume.
        if prompt_embeds_tensors and mm_data:
            assert prompt_embeds_placeholder_token_id is not None
            cast(dict, prompt)["_prompt_embeds"] = (
                prompt_embeds_tensors,
                prompt_embeds_placeholder_token_id,
            )
            if params.mm_processor_kwargs:
                cast(dict, prompt)["mm_processor_kwargs"] = params.mm_processor_kwargs
        elif prompt_embeds_tensors:
            # Pure mode: no other MM data, mutate prompt to EmbedsPrompt shape.
            assert prompt_embeds_placeholder_token_id is not None
            self._apply_prompt_embeds_to_prompt(
                prompt,
                prompt_embeds_tensors,
                prompt_embeds_placeholder_token_id,
            )

        if mm_data is not None:
            prompt["multi_modal_data"] = mm_data
        if mm_uuids is not None:
            prompt["multi_modal_uuids"] = mm_uuids

        return conversation, prompt

    async defrender_messages_async(
        self,
        messages: list[ChatCompletionMessageParam],
        params: ChatParams,
    ) -> tuple[list[ConversationMessage], DictPrompt]:
        model_config = self.model_config
        tokenizer = self.get_tokenizer()

        prompt_embeds_placeholder_token_id: int | None = None
        if model_config.enable_prompt_embeds:
            prompt_embeds_placeholder_token_id = (
                _ensure_prompt_embeds_placeholder_token(tokenizer)
            )

        conversation, mm_data, mm_uuids = await parse_chat_messages_async(
            messages,
            model_config,
            content_format=resolve_chat_template_content_format(
                chat_template=params.chat_template,
                tools=params.chat_template_kwargs.get("tools"),
                given_format=params.chat_template_content_format,
                tokenizer=tokenizer,
                model_config=model_config,
            ),
            media_io_kwargs=params.media_io_kwargs,
            mm_processor_kwargs=params.mm_processor_kwargs,
        )

        prompt_embeds_tensors: list[torch.Tensor] | None = None
        if mm_data is not None and "prompt_embeds" in mm_data:
            prompt_embeds_tensors = list(
                cast(Sequence[torch.Tensor], mm_data["prompt_embeds"])
            )
            mm_data = {k: v for k, v in mm_data.items() if k != "prompt_embeds"}
            if not mm_data:
                mm_data = None

        chat_template_kwargs = params.get_apply_chat_template_kwargs()
        if prompt_embeds_tensors:
            # prompt_embeds post-processing requires prompt_token_ids.
            if chat_template_kwargs.get("tokenize") is False:
                logger.warning_once(_TOKENIZE_OVERRIDE_WARNING)
            chat_template_kwargs["tokenize"] = True

        prompt_raw = await self._apply_chat_template_async(
            model_config,
            tokenizer,
            conversation,
            **chat_template_kwargs,
        )

        # NOTE: use_unified_vision_chunk is currently specific to Kimi-K2.5
        # model which uses unified vision chunks for both images and videos.
        if (
            self.use_unified_vision_chunk
            and mm_uuids is not None
            and mm_data is not None
        ):
            # get video placeholder, replace it with runtime video-chunk prompts
            video_placeholder = getattr(
                model_config.hf_config, "video_placeholder", None
            )
            prompt_raw = cast(
                list[int],
                replace_vision_chunk_video_placeholder(
                    prompt_raw,
                    mm_data,
                    video_placeholder,
                ),
            )

        prompt = parse_dec_only_prompt(prompt_raw)

        # See `render_messages` for the rationale.
        if prompt_embeds_tensors and mm_data:
            assert prompt_embeds_placeholder_token_id is not None
            cast(dict, prompt)["_prompt_embeds"] = (
                prompt_embeds_tensors,
                prompt_embeds_placeholder_token_id,
            )
            if params.mm_processor_kwargs:
                cast(dict, prompt)["mm_processor_kwargs"] = params.mm_processor_kwargs
        elif prompt_embeds_tensors:
            assert prompt_embeds_placeholder_token_id is not None
            self._apply_prompt_embeds_to_prompt(
                prompt,
                prompt_embeds_tensors,
                prompt_embeds_placeholder_token_id,
            )

        if mm_data is not None:
            prompt["multi_modal_data"] = mm_data
        if mm_uuids is not None:
            prompt["multi_modal_uuids"] = mm_uuids

        return conversation, prompt

    @override
    def_process_tokens(
        self,
        prompt: TokensPrompt,
        *,
        skip_mm_cache: bool = False,
    ) -> TokensInput | MultiModalInput:
"""Pre-expand `prompt_embeds` sentinels before delegating to the MM
        processor, then attach `prompt_embeds` modality data to the result.

        Mixed mode only: the `_prompt_embeds` stash is set by
        `render_messages` when `prompt_embeds` co-exist with other MM data
        (images, audio, …).  We expand each 1-token sentinel to an N-token
        span *before* calling `super()._process_tokens()` so the MM
        processor records all placeholder offsets in the final (post-expansion)
        coordinate space, no offset shifting needed afterwards.
        """
        prompt_embeds_info = cast(dict, prompt).pop("_prompt_embeds", None)
        if prompt_embeds_info is not None:
            tensors, placeholder_token_id = prompt_embeds_info
            mm_updates = _build_prompt_embeds_updates(tensors, placeholder_token_id)
            cast(dict, prompt)["prompt_token_ids"] = _expand_prompt_embeds_placeholders(
                list(prompt["prompt_token_ids"]), mm_updates
            )
        engine_input = super()._process_tokens(prompt, skip_mm_cache=skip_mm_cache)
        if prompt_embeds_info is not None:
            tensors, _ = prompt_embeds_info
            self._apply_prompt_embeds_to_engine_input(
                cast(MultiModalInput, engine_input),
                tensors,
                mm_updates,
            )
        return engine_input

    @override
    async def_process_tokens_async(
        self,
        prompt: TokensPrompt,
        *,
        skip_mm_cache: bool = False,
    ) -> TokensInput | MultiModalInput:
"""Async equivalent of `_process_tokens`."""
        prompt_embeds_info = cast(dict, prompt).pop("_prompt_embeds", None)
        if prompt_embeds_info is not None:
            tensors, placeholder_token_id = prompt_embeds_info
            mm_updates = _build_prompt_embeds_updates(tensors, placeholder_token_id)
            cast(dict, prompt)["prompt_token_ids"] = _expand_prompt_embeds_placeholders(
                list(prompt["prompt_token_ids"]), mm_updates
            )
        engine_input = await super()._process_tokens_async(
            prompt, skip_mm_cache=skip_mm_cache
        )
        if prompt_embeds_info is not None:
            tensors, _ = prompt_embeds_info
            self._apply_prompt_embeds_to_engine_input(
                cast(MultiModalInput, engine_input),
                tensors,
                mm_updates,
            )
        return engine_input

    @staticmethod
    def_apply_prompt_embeds_to_prompt(
        prompt: DictPrompt,
        prompt_embeds_tensors: list[torch.Tensor],
        placeholder_token_id: int,
    ) -> None:
"""Mutate `prompt` from `TokensPrompt` to `EmbedsPrompt` shape.

        Pure `prompt_embeds` path only (no other MM modalities).  Expands
        each `<prompt_embeds>` sentinel token into an N-token span and builds
        the full-length `prompt_embeds` tensor + `prompt_is_token_ids` mask
        that the engine's `enable_prompt_embeds` worker branch consumes.
        """
        token_ids = cast(list[int] | None, prompt.get("prompt_token_ids"))
        if token_ids is None:
            raise RuntimeError(_MISSING_PROMPT_TOKEN_IDS_ERROR)

        embeds_orig_positions: list[int] = [
            i for i, tok in enumerate(token_ids) if tok == placeholder_token_id
        ]
        if len(embeds_orig_positions) != len(prompt_embeds_tensors):
            raise ValueError(
                f"Expected {len(prompt_embeds_tensors)} prompt_embeds "
                f"placeholder tokens in the rendered prompt, found "
                f"{len(embeds_orig_positions)}."
            )

        mm_updates = _build_prompt_embeds_updates(
            prompt_embeds_tensors, placeholder_token_id
        )
        expanded = _expand_prompt_embeds_placeholders(token_ids, mm_updates)
        positions = _build_prompt_embeds_positions(
            expanded, len(prompt_embeds_tensors), mm_updates
        )

        embeds_prompt = cast(EmbedsPrompt, prompt)
        embeds_prompt["prompt_token_ids"] = expanded
        full_embeds, is_token_ids_mask = _build_mixed_prompt_embeds(
            expanded, prompt_embeds_tensors, positions
        )
        embeds_prompt["prompt_embeds"] = full_embeds
        embeds_prompt["prompt_is_token_ids"] = is_token_ids_mask

    @staticmethod
    def_apply_prompt_embeds_to_engine_input(
        engine_input: MultiModalInput,
        prompt_embeds_tensors: list[torch.Tensor],
        mm_updates: MultiModalPromptUpdates,
    ) -> None:
"""Augment `engine_input` in-place with a `prompt_embeds` modality.

        Mixed mode: called after `_process_multimodal` has already run on the
        pre-expanded token IDs (expansion was done in `_process_tokens` before
        calling `super()`).  Locates the already-expanded `prompt_embeds` spans
        and adds `prompt_embeds` entries to `mm_kwargs`, `mm_hashes`, and
        `mm_placeholders`.
        """
        # token_ids already contain the pre-expanded N-token spans.
        token_ids = list(engine_input["prompt_token_ids"])

        positions = _build_prompt_embeds_positions(
            token_ids, len(prompt_embeds_tensors), mm_updates
        )

        pe_kwargs_items: list[MultiModalKwargsItem] = []
        pe_hashes: list[str] = []
        pe_placeholders: list[PlaceholderRange] = []
        for tensor, (start, length) in zip(
            prompt_embeds_tensors, positions, strict=True
        ):
            pe_kwargs_items.append(
                MultiModalKwargsItem(
                    {
                        "embedding": MultiModalFieldElem(
                            data=tensor,
                            field=MultiModalSharedField(batch_size=1),
                        )
                    }
                )
            )
            pe_hashes.append(MultiModalHasher.hash_kwargs(prompt_embeds=tensor))
            # `is_embed=None` matches the existing image_embeds-style
            # "no encoder, just splice the tensor directly" semantics.
            pe_placeholders.append(
                PlaceholderRange(offset=start, length=length, is_embed=None)
            )

        cast(
            MultiModalKwargsItems[MultiModalKwargsItem | None],
            engine_input["mm_kwargs"],
        )["prompt_embeds"] = pe_kwargs_items
        engine_input["mm_hashes"] = {
            **engine_input["mm_hashes"],
            "prompt_embeds": pe_hashes,
        }
        cast(dict, engine_input["mm_placeholders"])["prompt_embeds"] = pe_placeholders
```