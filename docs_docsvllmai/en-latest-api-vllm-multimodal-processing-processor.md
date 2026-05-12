---
title: processor - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/multimodal/processing/processor/
source: sitemap
fetched_at: 2026-05-07T21:34:21.773639497-03:00
rendered_js: false
word_count: 41
summary: This document defines the BaseMultiModalProcessor abstract base class, which provides a framework for integrating and processing multi-modal inputs within the vLLM architecture.
tags:
    - vllm
    - multi-modal
    - python
    - abstract-base-class
    - hugging-face
    - data-processing
category: concept
---

```
classBaseMultiModalProcessor(ABC, Generic[_I]):
"""
    Abstract base class to process multi-modal inputs to be used in vLLM.

    Not to be confused with `transformers.ProcessorMixin`.
    """

    def__init__(
        self,
        info: _I,
        dummy_inputs: "BaseDummyInputsBuilder[_I]",
        *,
        cache: BaseMultiModalProcessorCache | None = None,
    ) -> None:
        super().__init__()

        self.info = info
        self.dummy_inputs = dummy_inputs
        self.cache = cache

        self.data_parser = self.info.get_data_parser()

    def__call__(
        self,
        prompt: str,
        mm_items: MultiModalDataItems,
        mm_uuid_items: MultiModalUUIDItems | None = None,
        hf_processor_mm_kwargs: Mapping[str, object] | None = None,
    ) -> MultiModalInput:
        processor_inputs = ProcessorInputs(
            prompt,
            mm_items,
            mm_uuid_items,
            hf_processor_mm_kwargs=hf_processor_mm_kwargs or {},
        )

        return self.apply(processor_inputs, TimingContext(enabled=False))

    @abstractmethod
    def_get_mm_fields_config(
        self,
        hf_inputs: BatchFeature,
        hf_processor_mm_kwargs: Mapping[str, object],
    ) -> Mapping[str, MultiModalFieldConfig]:
"""Given the HF-processed data, output the metadata of each field."""
        raise NotImplementedError

    @abstractmethod
    def_get_prompt_updates(
        self,
        mm_items: MultiModalDataItems,
        hf_processor_mm_kwargs: Mapping[str, object],
        out_mm_kwargs: MultiModalKwargsItems,
    ) -> Sequence[PromptUpdate]:
"""
        Given the original multi-modal items for this modality
        and HF-processed data, output the updates to perform.

        The information returned by this method is used to update token inputs
        which bypass the HF processor. It is also used to update the output of
        HF processor if the HF process does not apply prompt updates to text
        inputs.

        Moreover, this information is critical to determine the token positions
        in order to construct
        [`PlaceholderRange`][vllm.multimodal.inputs.PlaceholderRange]
        for each multi-modal item.
        """
        raise NotImplementedError

    def_bind_and_group_updates(
        self,
        prompt_updates: Sequence[PromptUpdate],
        mm_item_counts: Mapping[str, int],
    ) -> MultiModalPromptUpdates:
        return {
            modality: [
                [update.resolve(item_idx) for update in updates]
                for item_idx in range(mm_item_counts.get(modality, 0))
            ]
            for modality, updates in full_groupby_modality(prompt_updates)
        }

    def_get_mm_prompt_updates(
        self,
        mm_items: MultiModalDataItems,
        hf_processor_mm_kwargs: Mapping[str, object],
        out_mm_kwargs: MultiModalKwargsItems,
    ) -> MultiModalPromptUpdates:
        unbound_prompt_updates = self._get_prompt_updates(
            mm_items=mm_items,
            hf_processor_mm_kwargs=hf_processor_mm_kwargs,
            out_mm_kwargs=out_mm_kwargs,
        )

        mm_prompt_updates = self._bind_and_group_updates(
            unbound_prompt_updates,
            mm_items.get_all_counts(),
        )

        return mm_prompt_updates

    def_find_mm_placeholders(
        self,
        new_token_ids: list[int],
        mm_prompt_updates: MultiModalPromptUpdates,
    ) -> Mapping[str, list[PlaceholderFeaturesInfo]]:
        tokenizer = self.info.get_tokenizer()

        return find_mm_placeholders(new_token_ids, mm_prompt_updates, tokenizer)

    def_get_hf_mm_data(
        self,
        mm_items: MultiModalDataItems,
    ) -> tuple[Mapping[str, object], Mapping[str, object]]:
"""Extract processor and passthrough data from multi-modal items."""
        processor_data = dict[str, object]()
        passthrough_data = dict[str, object]()

        for items in mm_items.values():
            processor_data.update(items.get_processor_data())
            passthrough_data.update(items.get_passthrough_data())

        return processor_data, passthrough_data

    def_call_hf_processor(
        self,
        prompt: str,
        # Not to be confused with `mm_data` in `self.apply`.
        # This refers to the data to be passed to HF processor.
        mm_data: Mapping[str, object],
        mm_kwargs: Mapping[str, object],
        tok_kwargs: Mapping[str, object],
    ) -> BatchFeature:
"""
        Call the HF processor on the prompt text and
        associated multi-modal data.
        """
        return self.info.ctx.call_hf_processor(
            self.info.get_hf_processor(**mm_kwargs),
            dict(text=prompt, **mm_data),
            dict(**mm_kwargs, **tok_kwargs),
        )

    def_hf_processor_applies_updates(
        self,
        prompt_text: str,
        mm_items: MultiModalDataItems,
        hf_processor_mm_kwargs: Mapping[str, object],
        tokenization_kwargs: Mapping[str, object],
    ) -> bool:
"""
        Return whether the HF processor applies prompt updates.

        For most HF processors, this should be `True` when multi-modal
        data items are passed, but `False` when multi-modal embeddings
        are passed.
        """
        return not any(
            isinstance(items, (EmbeddingItems, DictEmbeddingItems))
            for items in mm_items.values()
        )

    def_apply_hf_processor_text_mm(
        self,
        prompt_text: str,
        mm_items: MultiModalDataItems,
        hf_processor_mm_kwargs: Mapping[str, object],
        tokenization_kwargs: Mapping[str, object],
    ) -> tuple[list[int], BatchFeature, bool]:
"""
        Apply the HF processor on the prompt text and multi-modal data
        together.

        In addition, return whether prompt updates have been applied.
        """
        valid_mm_items = mm_items.select(
            {k for k, c in mm_items.get_all_counts().items() if c > 0}
        )
        processor_data, passthrough_data = self._get_hf_mm_data(valid_mm_items)

        processed_data = self._call_hf_processor(
            prompt=prompt_text,
            mm_data=processor_data,
            mm_kwargs=hf_processor_mm_kwargs,
            tok_kwargs=tokenization_kwargs,
        )
        processed_data.update(passthrough_data)

        input_ids = processed_data.pop("input_ids")
        if not isinstance(input_ids, list):
            input_ids = input_ids.tolist()

        (prompt_ids,) = input_ids

        is_update_applied = self._hf_processor_applies_updates(
            prompt_text=prompt_text,
            mm_items=mm_items,
            hf_processor_mm_kwargs=hf_processor_mm_kwargs,
            tokenization_kwargs=tokenization_kwargs,
        )

        return prompt_ids, processed_data, is_update_applied

    def_apply_hf_processor_text_only(
        self,
        prompt_text: str,
        tokenization_kwargs: Mapping[str, object],
    ) -> list[int]:
"""
        Apply the HF processor on the prompt text only.

        Since HF processor requires that text and multi-modal items
        correspond to each other, we create dummy multi-modal items
        to go along with the text.
        """
        prompt_ids, _, _ = self._apply_hf_processor_text_mm(
            prompt_text=prompt_text,
            mm_items=MultiModalDataItems({}),
            hf_processor_mm_kwargs={},
            tokenization_kwargs=tokenization_kwargs,
        )

        return prompt_ids

    def_apply_hf_processor_tokens_only(
        self,
        prompt_tokens: list[int],
    ) -> list[int]:
"""
        Apply the HF processor on the prompt tokens only.

        Most HF processors accept prompt text but not prompt tokens.
        If the HF processor adds or removes tokens that are not related to
        multi-modal data, you should override this method so it is consistent
        with the output of
        [`_apply_hf_processor_text_only`][vllm.multimodal.processing.BaseMultiModalProcessor._apply_hf_processor_text_only]
        on the
        corresponding text.
        """
        return prompt_tokens

    def_apply_hf_processor_mm_only(
        self,
        mm_items: MultiModalDataItems,
        hf_processor_mm_kwargs: Mapping[str, object],
        tokenization_kwargs: Mapping[str, object],
    ) -> BatchFeature:
"""
        Apply the HF processor on the multi-modal data only.

        Since HF processor requires that text and multi-modal items
        correspond to each other, we generate dummy text using
        [`DummyInputsBuilder`][vllm.multimodal.processing.BaseDummyInputsBuilder]
        to go along with the multi-modal data.
        """
        # Custom logic based on text inputs
        if type(self)._call_hf_processor != BaseMultiModalProcessor._call_hf_processor:
            mm_counts = mm_items.get_all_counts()

            _, mm_processed_data, _ = self._apply_hf_processor_text_mm(
                prompt_text=self.dummy_inputs.get_dummy_text(mm_counts),
                mm_items=mm_items,
                hf_processor_mm_kwargs=hf_processor_mm_kwargs,
                tokenization_kwargs=tokenization_kwargs,
            )

            return mm_processed_data

        valid_mm_items = mm_items.select(
            {k for k, c in mm_items.get_all_counts().items() if c > 0}
        )
        processor_data, passthrough_data = self._get_hf_mm_data(valid_mm_items)

        processed_data = self.info.ctx.call_hf_processor(
            partial(
                call_hf_processor_mm_only,
                self.info.get_hf_processor(**hf_processor_mm_kwargs),
            ),
            processor_data,
            dict(**hf_processor_mm_kwargs, **tokenization_kwargs),
        )
        processed_data.update(passthrough_data)

        return processed_data

    def_apply_hf_processor_main(
        self,
        prompt: str | list[int],
        mm_items: MultiModalDataItems,
        hf_processor_mm_kwargs: Mapping[str, object],
        tokenization_kwargs: Mapping[str, object],
        *,
        enable_hf_prompt_update: bool,
    ) -> tuple[list[int], BatchFeature, bool]:
"""
        Apply the HF processor on the prompt text and multi-modal data.

        In addition, return whether prompt updates have been applied
        (for most HF processors, this should be `True`).

        Note:
            If `enable_hf_prompt_update=False`, we use HF processor
            to perform prompt updates if available; HF processor requires
            that the prompt corresponds to multi-modal items.
        """
        if isinstance(prompt, str):
            if enable_hf_prompt_update:
                return self._apply_hf_processor_text_mm(
                    prompt_text=prompt,
                    mm_items=mm_items,
                    hf_processor_mm_kwargs=hf_processor_mm_kwargs,
                    tokenization_kwargs=tokenization_kwargs,
                )

            prompt_ids = self._apply_hf_processor_text_only(prompt, tokenization_kwargs)
        else:
            prompt_ids = self._apply_hf_processor_tokens_only(prompt)

        mm_processed_data = self._apply_hf_processor_mm_only(
            mm_items=mm_items,
            hf_processor_mm_kwargs=hf_processor_mm_kwargs,
            tokenization_kwargs=tokenization_kwargs,
        )

        return prompt_ids, mm_processed_data, False

    def_get_cache_missing_items(
        self,
        cache: BaseMultiModalProcessorCache,
        mm_data_items: MultiModalDataItems,
        mm_hashes: MultiModalHashes,
    ) -> tuple[MultiModalIsCached, MultiModalDataItems]:
        mm_is_cached = {
            modality: cache.is_cached(hashes) for modality, hashes in mm_hashes.items()
        }

        mm_missing_idxs = {
            modality: [
                idx
                for idx, item_is_cached in enumerate(items_is_cached)
                if not item_is_cached
            ]
            for modality, items_is_cached in mm_is_cached.items()
        }

        mm_missing_data = {}
        for modality, idxs in mm_missing_idxs.items():
            missing_modality_data = []
            for idx in idxs:
                data = mm_data_items[modality][idx]
                if data is None:
                    raise ValueError(
                        f"Cache miss for {modality} at index {idx} "
                        f"but data is not provided."
                    )
                else:
                    missing_modality_data.append(data)
            mm_missing_data[modality] = missing_modality_data

        mm_missing_items = self.info.parse_mm_data(mm_missing_data, validate=False)

        return mm_is_cached, mm_missing_items

    def_recompute_cached_prompt_update(
        self,
        cached_update: ResolvedPromptUpdate,
        new_item_idx: int,
    ) -> ResolvedPromptUpdate:
"""
        Override this if other attributes of `ResolvedPromptUpdate`
        also need to be recomputed after retrieving from the cache.
        """
        return replace(cached_update, item_idx=new_item_idx)

    def_merge_mm_kwargs(
        self,
        cache: BaseMultiModalProcessorCache,
        mm_hashes: MultiModalHashes,
        mm_is_cached: MultiModalIsCached,
        mm_missing_kwargs: MultiModalKwargsItems,
        mm_missing_prompt_updates: MultiModalPromptUpdates,
    ) -> tuple[MultiModalKwargsOptionalItems, MultiModalPromptUpdates]:
        # Need to touch all mm hashes before update to avoid hash in updated
        # list evict during update
        for hashes in mm_hashes.values():
            for item_hash in hashes:
                cache.touch_sender_cache_item(item_hash)

        mm_missing_next_idx = defaultdict[str, int](lambda: 0)

        merged_kwargs = defaultdict[str, list[MultiModalKwargsItem | None]](list)
        merged_prompt_updates = defaultdict[str, list[Sequence[ResolvedPromptUpdate]]](
            list
        )
        for modality, hashes in mm_hashes.items():
            missing_kwargs = mm_missing_kwargs.get(modality, [])
            missing_prompt_updates = mm_missing_prompt_updates.get(modality, [])

            for item_idx, item_hash in enumerate(hashes):
                if not mm_is_cached[modality][item_idx]:
                    missing_next_idx = mm_missing_next_idx[modality]
                    missing_kwargs_item = missing_kwargs[missing_next_idx]
                    missing_updates_item = missing_prompt_updates[missing_next_idx]

                    mm_missing_next_idx[modality] += 1

                    item = missing_kwargs_item, missing_updates_item
                else:
                    item = None

                kwargs, updates = cache.get_and_update_item(item, item_hash)

                merged_kwargs[modality].append(kwargs)
                merged_prompt_updates[modality].append(
                    [
                        self._recompute_cached_prompt_update(update, item_idx)
                        for update in updates
                    ]
                )

        mm_kwargs = MultiModalKwargsItems(merged_kwargs)
        mm_prompt_updates = dict(merged_prompt_updates)

        return mm_kwargs, mm_prompt_updates

    def_apply_hf_processor(
        self,
        inputs: ProcessorInputs,
        timing_ctx: TimingContext,
    ) -> tuple[list[int], MultiModalProcessingInfo, bool]:
        with timing_ctx.record("apply_hf_processor"):
            (
                prompt_ids,
                mm_processed_data,
                is_update_applied,
            ) = self._apply_hf_processor_main(
                prompt=inputs.prompt,
                mm_items=inputs.mm_data_items,
                hf_processor_mm_kwargs=inputs.hf_processor_mm_kwargs,
                tokenization_kwargs=inputs.tokenization_kwargs,
                enable_hf_prompt_update=True,
            )

        mm_kwargs = MultiModalKwargsItems.from_hf_inputs(
            mm_processed_data,
            self._get_mm_fields_config(
                mm_processed_data, inputs.hf_processor_mm_kwargs
            ),
        )

        # Use overrides if provided; fallback to data-dependent hashing.
        with timing_ctx.record("get_mm_hashes"):
            mm_hashes = inputs.get_mm_hashes(self.info.model_id)

        mm_prompt_updates = self._get_mm_prompt_updates(
            inputs.mm_data_items,
            inputs.hf_processor_mm_kwargs,
            mm_kwargs,
        )

        mm_info = MultiModalProcessingInfo(
            kwargs=mm_kwargs,
            hashes=mm_hashes,
            prompt_updates=mm_prompt_updates,
        )

        return prompt_ids, mm_info, is_update_applied

    def_cached_apply_hf_processor(
        self,
        inputs: ProcessorInputs,
        timing_ctx: TimingContext,
    ) -> tuple[list[int], MultiModalProcessingInfo, bool]:
"""
        Apply the HF processor on the full prompt text,
        caching the results and reusing cached results.
        """
        cache = self.cache

        _, passthrough_data = self._get_hf_mm_data(inputs.mm_data_items)
        if cache is None or passthrough_data:
            return self._apply_hf_processor(inputs, timing_ctx)

        with timing_ctx.record("get_mm_hashes"):
            mm_hashes = inputs.get_mm_hashes(self.info.model_id)

        with timing_ctx.record("get_cache_missing_items"):
            mm_is_cached, mm_missing_data_items = self._get_cache_missing_items(
                cache=cache,
                mm_data_items=inputs.mm_data_items,
                mm_hashes=mm_hashes,
            )

        # NOTE: `prompt` does not correspond to `mm_missing_data_items`,
        # so we can't apply prompt updates until the new multimodal
        # items are combined with the cached multimodal items
        with timing_ctx.record("apply_hf_processor"):
            (
                prompt_ids,
                mm_missing_processed_data,
                is_update_applied,
            ) = self._apply_hf_processor_main(
                prompt=inputs.prompt,
                mm_items=mm_missing_data_items,
                hf_processor_mm_kwargs=inputs.hf_processor_mm_kwargs,
                tokenization_kwargs=inputs.tokenization_kwargs,
                enable_hf_prompt_update=False,
            )

        mm_missing_kwargs = MultiModalKwargsItems.from_hf_inputs(
            mm_missing_processed_data,
            self._get_mm_fields_config(
                mm_missing_processed_data, inputs.hf_processor_mm_kwargs
            ),
        )

        mm_missing_prompt_updates = self._get_mm_prompt_updates(
            mm_missing_data_items,
            inputs.hf_processor_mm_kwargs,
            mm_missing_kwargs,
        )

        with timing_ctx.record("merge_mm_kwargs"):
            mm_kwargs, mm_prompt_updates = self._merge_mm_kwargs(
                cache,
                mm_hashes=mm_hashes,
                mm_is_cached=mm_is_cached,
                mm_missing_kwargs=mm_missing_kwargs,
                mm_missing_prompt_updates=mm_missing_prompt_updates,
            )

        mm_info = MultiModalProcessingInfo(
            kwargs=mm_kwargs,
            hashes=mm_hashes,
            prompt_updates=mm_prompt_updates,
        )

        return prompt_ids, mm_info, is_update_applied

    def_apply_token_matches(
        self,
        prompt: list[int],
        mm_prompt_updates: MultiModalPromptUpdates,
    ) -> tuple[list[int], MultiModalPromptUpdatesApplyResult]:
        tokenizer = self.info.get_tokenizer()
        return apply_token_matches(prompt, mm_prompt_updates, tokenizer)

    def_apply_text_matches(
        self,
        prompt: str,
        mm_prompt_updates: MultiModalPromptUpdates,
    ) -> tuple[str, MultiModalPromptUpdatesApplyResult]:
        tokenizer = self.info.get_tokenizer()
        return apply_text_matches(prompt, mm_prompt_updates, tokenizer)

    def_apply_prompt_updates(
        self,
        token_ids: list[int],
        mm_prompt_updates: MultiModalPromptUpdates,
    ) -> tuple[list[int], Mapping[str, list[PlaceholderFeaturesInfo]]]:
"""Apply multi-modal prompt updates to token IDs."""
        tokenizer = self.info.get_tokenizer()

        new_token_ids, match_result = self._apply_token_matches(
            token_ids,
            mm_prompt_updates,
        )

        # If the search text does not represent a special token,
        # it may have different token IDs in the prompt, because
        # the tokens may go across the boundaries of the search text.
        # ----
        # e.g. when searching for "foo" in "food", if "food" itself makes
        # up a token, then the token ID of "foo" will not appear at all
        # ----
        # Since it is inefficient to search for all possible tokenizations
        # of the search text in the prompt, we instead perform string-based
        # updates on the decoded token IDs, then encode them back.
        if not all(
            all(update_idx is not None for update_idx in update_idxs)
            for update_idxs in match_result.values()
        ):
            new_text, match_result = self._apply_text_matches(
                _seq2text(tokenizer, token_ids, use_cache=False),
                mm_prompt_updates,
            )

            new_token_ids = _seq2tokens(tokenizer, new_text, use_cache=False)

        matched_updates = defaultdict[str, list[Sequence[ResolvedPromptUpdate]]](list)
        for modality, update_idxs in match_result.items():
            for item_idx, update_idx in enumerate(update_idxs):
                assert update_idx is not None, (
                    "Failed to apply prompt replacement for "
                    f"mm_items[{modality!r}][{item_idx}]"
                )

                matched_updates[modality].append(
                    [mm_prompt_updates[modality][item_idx][update_idx]]
                )

        placeholders = self._find_mm_placeholders(
            new_token_ids,
            dict(matched_updates),
        )

        return new_token_ids, placeholders

    def_validate_mm_kwargs(
        self,
        mm_kwargs: MultiModalKwargsOptionalItems,
        mm_item_counts: Mapping[str, int],
    ) -> None:
        for modality, item_count in mm_item_counts.items():
            items = mm_kwargs.get(modality, [])

            if len(items) != item_count:
                raise RuntimeError(
                    f"Expected there to be {item_count}{modality} items in "
                    f"keyword arguments corresponding to {item_count} "
                    f"{modality} data items, but only found {len(items)}! "
                    "There is likely a problem with your "
                    "implementation of merged multi-modal processor for this "
                    "model (usually arising from an inconsistency between "
                    "`_call_hf_processor` and `_get_mm_fields_config`)."
                )

    def_validate_mm_updates(
        self,
        mm_updates: MultiModalPromptUpdates,
        mm_item_counts: Mapping[str, int],
    ) -> None:
        for modality, item_count in mm_item_counts.items():
            placeholders = mm_updates.get(modality, [])

            if len(placeholders) != item_count:
                raise RuntimeError(
                    f"Expected there to be {item_count} prompt updates "
                    f"corresponding to {item_count}{modality} items, but "
                    f"instead found {len(placeholders)} prompt updates! "
                    "This is likely because you forgot to include input "
                    "placeholder tokens (e.g., `<image>`, `<|image_pad|>`) "
                    "in the prompt. If the model has a chat template, make "
                    "sure you have applied it before calling `LLM.generate`."
                )

    def_validate_mm_placeholders(
        self,
        mm_placeholders: Mapping[str, list[PlaceholderFeaturesInfo]],
        mm_item_counts: Mapping[str, int],
    ) -> None:
        for modality, item_count in mm_item_counts.items():
            placeholders = mm_placeholders.get(modality, [])

            if len(placeholders) != item_count:
                raise RuntimeError(
                    f"Expected there to be {item_count} prompt placeholders "
                    f"corresponding to {item_count}{modality} items, but "
                    f"instead found {len(placeholders)} prompt placeholders! "
                    "Make sure the implementation of `_call_hf_processor` and "
                    "`_get_mm_fields_config` are consistent with each other."
                )

    def_maybe_apply_prompt_updates(
        self,
        mm_items: MultiModalDataItems,
        prompt_ids: list[int],
        mm_kwargs: MultiModalKwargsOptionalItems,
        mm_prompt_updates: MultiModalPromptUpdates,
        is_update_applied: bool,
    ) -> tuple[list[int], Mapping[str, list[PlaceholderFeaturesInfo]]]:
        mm_item_counts = mm_items.get_all_counts()
        self._validate_mm_kwargs(mm_kwargs, mm_item_counts)
        self._validate_mm_updates(mm_prompt_updates, mm_item_counts)

        if is_update_applied:
            mm_placeholders = self._find_mm_placeholders(
                prompt_ids,
                mm_prompt_updates,
            )
            self._validate_mm_placeholders(mm_placeholders, mm_item_counts)
        else:
            prompt_ids, mm_placeholders = self._apply_prompt_updates(
                prompt_ids,
                mm_prompt_updates,
            )
            self._validate_mm_placeholders(mm_placeholders, mm_item_counts)

        return prompt_ids, mm_placeholders

    defapply(
        self,
        inputs: ProcessorInputs,
        timing_ctx: TimingContext,
    ) -> MultiModalInput:
"""
        Process multi-modal inputs to be used in vLLM.

        The main steps are:

        1. Apply HF Processor on prompt text and multi-modal data together,
           outputting token IDs and processed tensors.
        2. Find and update sequences in the token IDs with placeholder tokens.
           The number of placeholder tokens equals the feature size of the
           multi-modal data outputted by the multi-modal encoder.
        3. Extract information about the placeholder tokens from the
           processed token IDs.
        """
        (
            prompt_ids,
            mm_info,
            is_update_applied,
        ) = self._cached_apply_hf_processor(inputs, timing_ctx)

        # NOTE: tokenization_kwargs are not required to init processor
        with timing_ctx.record("apply_prompt_updates"):
            prompt_ids, mm_placeholders = self._maybe_apply_prompt_updates(
                mm_items=inputs.mm_data_items,
                prompt_ids=prompt_ids,
                mm_kwargs=mm_info.kwargs,
                mm_prompt_updates=mm_info.prompt_updates,
                is_update_applied=is_update_applied,
            )

        mm_placeholder_ranges = {
            modality: [item.to_range() for item in placeholders]
            for modality, placeholders in mm_placeholders.items()
        }

        return mm_input(
            prompt_token_ids=prompt_ids,
            mm_kwargs=mm_info.kwargs,
            mm_hashes=mm_info.hashes,
            mm_placeholders=mm_placeholder_ranges,
        )
```