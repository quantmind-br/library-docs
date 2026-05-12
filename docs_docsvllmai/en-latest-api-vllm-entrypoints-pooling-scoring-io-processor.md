---
title: io_processor - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/pooling/scoring/io_processor/
source: sitemap
fetched_at: 2026-05-07T21:21:09.872235001-03:00
rendered_js: false
word_count: 0
summary: This document defines the ClassScoringIOProcessor class, which manages input validation, token limit enforcement, and text truncation for scoring tasks in a model inference pipeline.
tags:
    - python-class
    - data-validation
    - token-truncation
    - model-inference
    - input-processing
    - scoring-tasks
category: reference
---

```
classScoringIOProcessor(PoolingIOProcessor):
    name: str
    pooling_task: PoolingTask

    def__init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.tokenizer = self.renderer.get_tokenizer()
        self.architecture = self.model_config.architecture
        self.is_multimodal_model = self.model_config.is_multimodal_model
        self.pad_token_id = self.tokenizer.pad_token_id

    defcreate_pooling_params(self, request):
        return request.to_pooling_params(self.pooling_task)

    def_validate_token_limit(self, value: int, name: str) -> None:
        if value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
        if value >= self.model_config.max_model_len:
            raise ValueError(
                f"{name} ({value}) must be less "
                f"than max_model_len ({self.model_config.max_model_len})."
            )

    def_get_token_limits(
        self,
        request: ScoringRequest | None = None,
        pooling_params: PoolingParams | None = None,
    ) -> tuple[int, int]:
"""Extract and validate token limits from request or pooling_params."""
        if request is not None:
            max_tokens_per_query = getattr(request, "max_tokens_per_query", 0)
            max_tokens_per_doc = getattr(request, "max_tokens_per_doc", 0)
        else:
            extra = (
                (pooling_params.extra_kwargs or {})
                if pooling_params is not None
                else {}
            )
            max_tokens_per_query = extra.get("max_tokens_per_query", 0)
            max_tokens_per_doc = extra.get("max_tokens_per_doc", 0)

        if max_tokens_per_query != 0:
            self._validate_token_limit(max_tokens_per_query, "max_tokens_per_query")
        if max_tokens_per_doc != 0:
            self._validate_token_limit(max_tokens_per_doc, "max_tokens_per_doc")
        return max_tokens_per_query, max_tokens_per_doc

    def_truncate_scoring_data(
        self,
        scoring_data: ScoringData,
        max_tokens_per_query: int = 0,
        max_tokens_per_doc: int = 0,
    ) -> ScoringData:
"""Truncate query/document texts to token limits."""
        data_1 = scoring_data.data_1
        data_2 = scoring_data.data_2
        if max_tokens_per_query > 0:
            data_1 = [
                truncate_text_to_tokens(d, self.tokenizer, max_tokens_per_query)
                if isinstance(d, str)
                else d
                for d in data_1
            ]
        if max_tokens_per_doc > 0:
            data_2 = [
                truncate_text_to_tokens(d, self.tokenizer, max_tokens_per_doc)
                if isinstance(d, str)
                else d
                for d in data_2
            ]
        return ScoringData(data_1=data_1, data_2=data_2)

    defvalid_inputs(
        self,
        data_1: ScoreInput | list[ScoreInput],
        data_2: ScoreInput | list[ScoreInput],
    ) -> ScoringData:
        scoring_data = validate_score_input(
            data_1,
            data_2,
            is_multimodal_model=self.is_multimodal_model,
            architecture=self.architecture,
        )
        return scoring_data
```