---
title: preprocess - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/inputs/preprocess/
source: sitemap
fetched_at: 2026-05-07T21:22:00.147415305-03:00
rendered_js: false
word_count: 0
summary: This document defines the InputPreprocessor class, which transforms various input prompt formats into model-ready engine inputs by handling tokenization, multi-modal data processing, and encoder-decoder configurations.
tags:
    - input-preprocessing
    - tokenization
    - multi-modal
    - encoder-decoder
    - vllm
    - data-processing
category: reference
---

```
classInputPreprocessor:
    def__init__(
        self,
        vllm_config: VllmConfig,
        renderer: BaseRenderer | None = None,
        mm_registry: MultiModalRegistry = MULTIMODAL_REGISTRY,
    ) -> None:
        super().__init__()

        self.model_config = vllm_config.model_config
        self.renderer = renderer or renderer_from_config(vllm_config)
        self.mm_registry = mm_registry

    @property
    deftokenizer(self) -> TokenizerLike | None:
        return self.renderer.tokenizer

    defget_tokenizer(self) -> TokenizerLike:
        return self.renderer.get_tokenizer()

    def_tokenize_prompt(
        self,
        prompt: str,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> list[int]:
"""
        Apply the model's tokenizer to a text prompt, returning the
        corresponding token IDs.
        """
        renderer = self.renderer

        tok_params = renderer.default_cmpl_tok_params.with_kwargs(
            **(tokenization_kwargs or {})
        )

        tok_prompt = renderer._tokenize_singleton_prompt(
            TextPrompt(prompt=prompt),
            tok_params,
        )

        return tok_prompt["prompt_token_ids"]

    def_process_multimodal(
        self,
        prompt: str | list[int],
        mm_data: MultiModalDataDict,
        mm_processor_kwargs: Mapping[str, object] | None = None,
        tokenization_kwargs: dict[str, Any] | None = None,
        *,
        mm_uuids: MultiModalUUIDDict | None = None,
    ) -> MultiModalInput:
"""
        Apply the model's multi-modal processor to a multi-modal prompt,
        returning the corresponding token IDs and metadata.
        """
        return self.renderer._process_multimodal(
            prompt,
            mm_data,
            mm_uuids=mm_uuids,
            mm_processor_kwargs=mm_processor_kwargs,
            tokenization_kwargs=tokenization_kwargs,
        )

    def_process_embeds(
        self,
        parsed_content: EmbedsPrompt,
    ) -> EmbedsInput:
        return self.renderer._process_embeds(parsed_content)

    def_truncate_inputs(
        self, inputs: list[int], tokenization_kwargs: dict[str, Any] | None = None
    ) -> list[int]:
        renderer = self.renderer

        tok_params = renderer.default_cmpl_tok_params.with_kwargs(
            **(tokenization_kwargs or {})
        )

        tok_prompt = renderer._tokenize_singleton_prompt(
            TokensPrompt(prompt_token_ids=inputs),
            tok_params,
        )

        return tok_prompt["prompt_token_ids"]

    def_process_tokens(
        self,
        parsed_content: TokensPrompt,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> TokensInput | MultiModalInput:
        prompt_token_ids = self._truncate_inputs(
            parsed_content["prompt_token_ids"], tokenization_kwargs
        )

        inputs: TokensInput | MultiModalInput
        if multi_modal_data := parsed_content.get("multi_modal_data"):
            inputs = self._process_multimodal(
                prompt_token_ids,
                multi_modal_data,
                parsed_content.get("mm_processor_kwargs"),
                tokenization_kwargs=tokenization_kwargs,
                mm_uuids=parsed_content.get("multi_modal_uuids"),
            )
        else:
            inputs = tokens_input(prompt_token_ids)

        if prompt_text := parsed_content.get("prompt"):
            inputs["prompt"] = prompt_text
        if cache_salt := parsed_content.get("cache_salt"):
            inputs["cache_salt"] = cache_salt

        return inputs

    def_process_text(
        self,
        parsed_content: TextPrompt,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> TokensInput | MultiModalInput:
        prompt_text = parsed_content["prompt"]

        inputs: TokensInput | MultiModalInput
        if multi_modal_data := parsed_content.get("multi_modal_data"):
            inputs = self._process_multimodal(
                prompt_text,
                multi_modal_data,
                parsed_content.get("mm_processor_kwargs") or {},
                tokenization_kwargs=tokenization_kwargs,
            )
        else:
            prompt_token_ids = self._tokenize_prompt(
                prompt_text,
                tokenization_kwargs=tokenization_kwargs,
            )
            inputs = tokens_input(prompt_token_ids)

        inputs["prompt"] = prompt_text

        if cache_salt := parsed_content.get("cache_salt"):
            inputs["cache_salt"] = cache_salt

        return inputs

    @overload
    def_prompt_to_llm_inputs(
        self,
        prompt: EncoderDictPrompt,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> EncoderInput: ...

    @overload
    def_prompt_to_llm_inputs(  # type: ignore[misc]
        self,
        prompt: DecoderDictPrompt,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> DecoderEngineInput: ...

    @overload
    def_prompt_to_llm_inputs(  # type: ignore[misc]
        self,
        prompt: DecoderOnlyDictPrompt,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> DecoderOnlyEngineInput: ...

    def_prompt_to_llm_inputs(
        self,
        prompt: SingletonDictPrompt,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> SingletonInput:
        if "prompt_embeds" in prompt:
            return self._process_embeds(prompt)  # type: ignore[arg-type]

        if "prompt_token_ids" in prompt:
            return self._process_tokens(prompt)  # type: ignore[arg-type]

        if "prompt" in prompt:
            return self._process_text(
                prompt,  # type: ignore[arg-type]
                tokenization_kwargs=tokenization_kwargs,
            )

        assert_never(prompt)  # type: ignore[arg-type]

    def_process_encoder_decoder_prompt(
        self,
        prompt: EncoderDecoderDictPrompt,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> EncoderDecoderInput:
        encoder_prompt = prompt["encoder_prompt"]
        decoder_prompt = prompt["decoder_prompt"]

        skip_decoder_start_token = False
        if self.renderer.mm_processor is not None:
            fromvllm.multimodal.processingimport EncDecMultiModalProcessor

            if isinstance(self.renderer.mm_processor, EncDecMultiModalProcessor):
                skip_decoder_start_token = (
                    self.renderer.mm_processor.skip_decoder_start_token
                )

        return build_enc_dec_input(
            encoder_input=self._prompt_to_llm_inputs(
                encoder_prompt,
                tokenization_kwargs=tokenization_kwargs,
            ),
            decoder_input=(
                None
                if decoder_prompt is None
                else self._prompt_to_llm_inputs(
                    decoder_prompt,
                    tokenization_kwargs=tokenization_kwargs,
                )
            ),
            decoder_start_token_id=self.renderer.get_dec_start_token_id(),
            skip_decoder_start_token=skip_decoder_start_token,
        )

    def_process_decoder_only_prompt(
        self,
        prompt: DecoderOnlyDictPrompt,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> DecoderOnlyEngineInput:
        return self._prompt_to_llm_inputs(
            prompt,
            tokenization_kwargs=tokenization_kwargs,
        )

    defpreprocess(
        self,
        prompt: PromptType,
        tokenization_kwargs: dict[str, Any] | None = None,
    ) -> EngineInput:
"""Preprocess the input prompt."""
        if self.model_config.is_encoder_decoder:
            # Encoder-decoder model requires special mapping of
            # input prompts to encoder & decoder.
            return self._process_encoder_decoder_prompt(
                parse_enc_dec_prompt(prompt),
                tokenization_kwargs,
            )

        return self._process_decoder_only_prompt(
            parse_dec_only_prompt(prompt),
            tokenization_kwargs=tokenization_kwargs,
        )
```