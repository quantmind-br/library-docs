---
title: reasoning - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/reasoning/
source: sitemap
fetched_at: 2026-05-07T21:17:11.937344282-03:00
rendered_js: false
word_count: 301
summary: This document defines the ReasoningConfig class, which manages the start and end delimiters for reasoning blocks in models and provides methods to automatically initialize corresponding token IDs.
tags:
    - vllm
    - reasoning-models
    - configuration
    - tokenization
    - model-config
category: configuration
---

Configuration for reasoning models.

Set `reasoning_start_str` and `reasoning_end_str` to the strings that delimit the reasoning block (e.g. `"<think>"` and `"</think>"`). The corresponding token IDs are derived automatically via `initialize_token_ids` and are not intended to be set directly.

Source code in `vllm/config/reasoning.py`

```
@config
classReasoningConfig:
"""Configuration for reasoning models.

    Set `reasoning_start_str` and `reasoning_end_str` to the strings that delimit
    the reasoning block (e.g. `"<think>"` and `"</think>"`).  The
    corresponding token IDs are derived automatically via
    `initialize_token_ids` and are not intended to be set directly.
    """

    reasoning_parser: str = ""
"""The name of the ReasoningParser to use for this model."""
    reasoning_start_str: str = ""
"""String that indicates the start of reasoning."""
    reasoning_end_str: str = ""
"""String that indicates the end of reasoning content."""

    _reasoning_start_token_ids: list[int] | None = field(
        default=None, init=False, repr=False
    )
"""Private backing field for `reasoning_start_token_ids`. Set by
    `initialize_token_ids`. Not intended to be configured directly."""
    _reasoning_end_token_ids: list[int] | None = field(
        default=None, init=False, repr=False
    )
"""Private backing field for `reasoning_end_token_ids`. Set by
    `initialize_token_ids`. Not intended to be configured directly."""

    _enabled: bool = field(default=False, init=False, repr=False)
"""Private field indicating whether reasoning token IDs have been initialized.
    Set to True by `initialize_token_ids` once token IDs are initialized."""

    @property
    defenabled(self) -> bool:
"""Returns True if reasoning is enabled (i.e. if token IDs have been
        initialized), False otherwise."""
        return self._enabled

    @property
    defreasoning_start_token_ids(self) -> list[int] | None:
"""Token IDs derived from `reasoning_start_str`. Set automatically by
        `initialize_token_ids`. Not intended to be configured directly."""
        return self._reasoning_start_token_ids

    @property
    defreasoning_end_token_ids(self) -> list[int] | None:
"""Token IDs derived from `reasoning_end_str`. Set automatically by
        `initialize_token_ids`. Not intended to be configured directly."""
        return self._reasoning_end_token_ids

    definitialize_token_ids(self, model_config: ModelConfig) -> None:
"""Initialize reasoning token IDs from strings using the tokenizer."""
        if (
            self._reasoning_start_token_ids is not None
            and self._reasoning_end_token_ids is not None
        ):
            self._enabled = True
            return  # Already initialized

        tokenizer = cached_tokenizer_from_config(model_config=model_config)
        reasoning_start_str = self.reasoning_start_str
        reasoning_end_str = self.reasoning_end_str
        if self.reasoning_parser is not None and (
            not reasoning_start_str or not reasoning_end_str
        ):
            parser_cls = ReasoningParserManager.get_reasoning_parser(
                self.reasoning_parser
            )
            reasoning_parser = parser_cls(tokenizer)
            start_token = reasoning_parser.reasoning_start_str
            if start_token and not reasoning_start_str:
                reasoning_start_str = start_token

            end_token = reasoning_parser.reasoning_end_str
            if end_token and not reasoning_end_str:
                reasoning_end_str = end_token

        if not reasoning_start_str or not reasoning_end_str:
            # If we don't have valid strings to tokenize,
            # we can't initialize the token IDs.
            return
        self._reasoning_start_token_ids = tokenizer.encode(
            reasoning_start_str, add_special_tokens=False
        )
        self._reasoning_end_token_ids = tokenizer.encode(
            reasoning_end_str, add_special_tokens=False
        )

        if not self._reasoning_start_token_ids or not self._reasoning_end_token_ids:
            raise ValueError(
                f"ReasoningConfig: failed to tokenize reasoning strings: "
                f"reasoning_start_str='{self.reasoning_start_str}', "
                f"reasoning_end_str='{self.reasoning_end_str}'. "
                "Ensure the strings are valid tokens in the model's vocabulary."
            )
        self._enabled = True
```

### \_enabled `class-attribute` `instance-attribute` [¶](#vllm.config.reasoning.ReasoningConfig._enabled "Permanent link")

```
_enabled: bool = field(
    default=False, init=False, repr=False
)
```

Private field indicating whether reasoning token IDs have been initialized. Set to True by `initialize_token_ids` once token IDs are initialized.

### \_reasoning\_end\_token\_ids `class-attribute` `instance-attribute` [¶](#vllm.config.reasoning.ReasoningConfig._reasoning_end_token_ids "Permanent link")

```
_reasoning_end_token_ids: list[int] | None = field(
    default=None, init=False, repr=False
)
```

Private backing field for `reasoning_end_token_ids`. Set by `initialize_token_ids`. Not intended to be configured directly.

### \_reasoning\_start\_token\_ids `class-attribute` `instance-attribute` [¶](#vllm.config.reasoning.ReasoningConfig._reasoning_start_token_ids "Permanent link")

```
_reasoning_start_token_ids: list[int] | None = field(
    default=None, init=False, repr=False
)
```

Private backing field for `reasoning_start_token_ids`. Set by `initialize_token_ids`. Not intended to be configured directly.

### enabled `property` [¶](#vllm.config.reasoning.ReasoningConfig.enabled "Permanent link")

Returns True if reasoning is enabled (i.e. if token IDs have been initialized), False otherwise.

### reasoning\_end\_str `class-attribute` `instance-attribute` [¶](#vllm.config.reasoning.ReasoningConfig.reasoning_end_str "Permanent link")

```
reasoning_end_str: str = ''
```

String that indicates the end of reasoning content.

### reasoning\_end\_token\_ids `property` [¶](#vllm.config.reasoning.ReasoningConfig.reasoning_end_token_ids "Permanent link")

```
reasoning_end_token_ids: list[int] | None
```

Token IDs derived from `reasoning_end_str`. Set automatically by `initialize_token_ids`. Not intended to be configured directly.

### reasoning\_parser `class-attribute` `instance-attribute` [¶](#vllm.config.reasoning.ReasoningConfig.reasoning_parser "Permanent link")

```
reasoning_parser: str = ''
```

The name of the ReasoningParser to use for this model.

### reasoning\_start\_str `class-attribute` `instance-attribute` [¶](#vllm.config.reasoning.ReasoningConfig.reasoning_start_str "Permanent link")

```
reasoning_start_str: str = ''
```

String that indicates the start of reasoning.

### reasoning\_start\_token\_ids `property` [¶](#vllm.config.reasoning.ReasoningConfig.reasoning_start_token_ids "Permanent link")

```
reasoning_start_token_ids: list[int] | None
```

Token IDs derived from `reasoning_start_str`. Set automatically by `initialize_token_ids`. Not intended to be configured directly.

### initialize\_token\_ids [¶](#vllm.config.reasoning.ReasoningConfig.initialize_token_ids "Permanent link")

```
initialize_token_ids(model_config: ModelConfig) -> None
```

Initialize reasoning token IDs from strings using the tokenizer.

Source code in `vllm/config/reasoning.py`

```
definitialize_token_ids(self, model_config: ModelConfig) -> None:
"""Initialize reasoning token IDs from strings using the tokenizer."""
    if (
        self._reasoning_start_token_ids is not None
        and self._reasoning_end_token_ids is not None
    ):
        self._enabled = True
        return  # Already initialized

    tokenizer = cached_tokenizer_from_config(model_config=model_config)
    reasoning_start_str = self.reasoning_start_str
    reasoning_end_str = self.reasoning_end_str
    if self.reasoning_parser is not None and (
        not reasoning_start_str or not reasoning_end_str
    ):
        parser_cls = ReasoningParserManager.get_reasoning_parser(
            self.reasoning_parser
        )
        reasoning_parser = parser_cls(tokenizer)
        start_token = reasoning_parser.reasoning_start_str
        if start_token and not reasoning_start_str:
            reasoning_start_str = start_token

        end_token = reasoning_parser.reasoning_end_str
        if end_token and not reasoning_end_str:
            reasoning_end_str = end_token

    if not reasoning_start_str or not reasoning_end_str:
        # If we don't have valid strings to tokenize,
        # we can't initialize the token IDs.
        return
    self._reasoning_start_token_ids = tokenizer.encode(
        reasoning_start_str, add_special_tokens=False
    )
    self._reasoning_end_token_ids = tokenizer.encode(
        reasoning_end_str, add_special_tokens=False
    )

    if not self._reasoning_start_token_ids or not self._reasoning_end_token_ids:
        raise ValueError(
            f"ReasoningConfig: failed to tokenize reasoning strings: "
            f"reasoning_start_str='{self.reasoning_start_str}', "
            f"reasoning_end_str='{self.reasoning_end_str}'. "
            "Ensure the strings are valid tokens in the model's vocabulary."
        )
    self._enabled = True
```