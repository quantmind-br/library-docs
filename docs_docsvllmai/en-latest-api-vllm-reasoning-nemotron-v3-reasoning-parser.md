---
title: nemotron_v3_reasoning_parser - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/reasoning/nemotron_v3_reasoning_parser/
source: sitemap
fetched_at: 2026-05-07T21:35:09.480655015-03:00
rendered_js: false
word_count: 12
summary: This document defines a reasoning parser class for Nemotron V3 models that extends the DeepSeekR1 reasoning logic to handle specific chat template requirements.
tags:
    - vllm
    - nemotron-v3
    - reasoning-parser
    - natural-language-processing
    - model-output-parsing
category: reference
---

Bases: `DeepSeekR1ReasoningParser`

Reasoning parser for Nemotron V3 models.

Source code in `vllm/reasoning/nemotron_v3_reasoning_parser.py`

```
classNemotronV3ReasoningParser(DeepSeekR1ReasoningParser):
"""
    Reasoning parser for Nemotron V3 models.
    """

    defextract_reasoning(
        self, model_output: str, request: ChatCompletionRequest | ResponsesRequest
    ) -> tuple[str | None, str | None]:
        reasoning, final_content = super().extract_reasoning(model_output, request)
        chat_template_kwargs = getattr(request, "chat_template_kwargs", None)

        if (
            chat_template_kwargs
            and (
                chat_template_kwargs.get("enable_thinking") is False
                or chat_template_kwargs.get("force_nonempty_content") is True
            )
            and final_content is None
        ):
            reasoning, final_content = final_content, reasoning

        return reasoning, final_content
```