---
title: backend_guidance - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/structured_output/backend_guidance/
source: sitemap
fetched_at: 2026-05-07T21:41:59.128449779-03:00
rendered_js: false
word_count: 91
summary: This document defines the GuidanceGrammar class and utility functions for managing structured output constraints within the vLLM framework using the llguidance library.
tags:
    - vllm
    - structured-output
    - llguidance
    - token-parsing
    - json-schema
    - grammar-enforcement
category: reference
---

## GuidanceGrammar `dataclass` [¶](#vllm.v1.structured_output.backend_guidance.GuidanceGrammar "Permanent link")

Bases: `StructuredOutputGrammar`

Source code in `vllm/v1/structured_output/backend_guidance.py`

```
@dataclass
classGuidanceGrammar(StructuredOutputGrammar):
    ll_matcher: llguidance.LLMatcher
    ll_tokenizer: llguidance.LLTokenizer
    vocab_size: int
    printed_error: bool = False
    terminated: bool = False
    rollback_lag: int = 0

    defcheck_error(self):
        if not self.printed_error:
            err = self.ll_matcher.get_error()
            if err:
                self.printed_error = True
                logger.warning("LLMatcher error: %s", err)

    defaccept_tokens(self, request_id: str, tokens: list[int]) -> bool:
"""Accepts a list of tokens and advances the parser.

        Returns True if the parser was advanced successfully.
        Returns False if the parser failed to advance.
        """

        if self.ll_tokenizer.eos_token in tokens:
            if self.ll_matcher.is_stopped() and not self.terminated:
                self.rollback_lag = 1
            self.terminated = True

        if self.ll_matcher.is_stopped():
            return True

        # TODO - Add jump decoding support in the future:
        # self.ll_matcher.compute_ff_bytes() - this should always work
        # self.ll_matcher.compute_ff_tokens() - this only works for
        #   "canonical" tokenizers
        # For conversion between the two, see
        # https://github.com/guidance-ai/llguidance/blob/main/docs/fast_forward.md

        r = self.ll_matcher.consume_tokens(tokens)

        self.check_error()

        return r

    defvalidate_tokens(self, tokens: list[int]) -> list[int]:
"""Checks if the list of tokens are accepted by the parser in sequence.
        Will not advance the parser.

        Returns the prefix list of tokens that are accepted by the parser.
        """
        if len(tokens) == 0:
            return []
        if self.ll_matcher.is_stopped():
            return []

        num_tokens = self.ll_matcher.validate_tokens(tokens)

        self.check_error()

        return tokens[:num_tokens]

    defrollback(self, num_tokens: int) -> None:
        if num_tokens > 0:
            self.ll_matcher.rollback(num_tokens - self.rollback_lag)
            self.terminated = False
            self.rollback_lag = 0
            self.check_error()

    deffill_bitmask(self, bitmask: torch.Tensor, idx: int) -> None:
        # this will automatically return [EOS] mask if the matcher is stopped
        # or otherwise in an error state
        llguidance_torch.fill_next_token_bitmask(self.ll_matcher, bitmask, idx)
        self.check_error()

    defis_terminated(self) -> bool:
        return self.terminated

    defreset(self):
        # This method may be not needed anymore? TODO
        self.ll_matcher.reset()
```

### accept\_tokens [¶](#vllm.v1.structured_output.backend_guidance.GuidanceGrammar.accept_tokens "Permanent link")

Accepts a list of tokens and advances the parser.

Returns True if the parser was advanced successfully. Returns False if the parser failed to advance.

Source code in `vllm/v1/structured_output/backend_guidance.py`

```
defaccept_tokens(self, request_id: str, tokens: list[int]) -> bool:
"""Accepts a list of tokens and advances the parser.

    Returns True if the parser was advanced successfully.
    Returns False if the parser failed to advance.
    """

    if self.ll_tokenizer.eos_token in tokens:
        if self.ll_matcher.is_stopped() and not self.terminated:
            self.rollback_lag = 1
        self.terminated = True

    if self.ll_matcher.is_stopped():
        return True

    # TODO - Add jump decoding support in the future:
    # self.ll_matcher.compute_ff_bytes() - this should always work
    # self.ll_matcher.compute_ff_tokens() - this only works for
    #   "canonical" tokenizers
    # For conversion between the two, see
    # https://github.com/guidance-ai/llguidance/blob/main/docs/fast_forward.md

    r = self.ll_matcher.consume_tokens(tokens)

    self.check_error()

    return r
```

### validate\_tokens [¶](#vllm.v1.structured_output.backend_guidance.GuidanceGrammar.validate_tokens "Permanent link")

Checks if the list of tokens are accepted by the parser in sequence. Will not advance the parser.

Returns the prefix list of tokens that are accepted by the parser.

Source code in `vllm/v1/structured_output/backend_guidance.py`

```
defvalidate_tokens(self, tokens: list[int]) -> list[int]:
"""Checks if the list of tokens are accepted by the parser in sequence.
    Will not advance the parser.

    Returns the prefix list of tokens that are accepted by the parser.
    """
    if len(tokens) == 0:
        return []
    if self.ll_matcher.is_stopped():
        return []

    num_tokens = self.ll_matcher.validate_tokens(tokens)

    self.check_error()

    return tokens[:num_tokens]
```

## has\_guidance\_unsupported\_json\_features [¶](#vllm.v1.structured_output.backend_guidance.has_guidance_unsupported_json_features "Permanent link")

```
has_guidance_unsupported_json_features(
    schema: dict[str, Any],
) -> bool
```

Check if JSON schema contains features unsupported by guidance/llguidance.

Source code in `vllm/v1/structured_output/backend_guidance.py`

```
defhas_guidance_unsupported_json_features(schema: dict[str, Any]) -> bool:
"""Check if JSON schema contains features unsupported by guidance/llguidance."""

    defcheck_object(obj: dict[str, Any]) -> bool:
        if not isinstance(obj, dict):
            return False

        # patternProperties is not supported by llguidance
        if "patternProperties" in obj:
            return True

        # Recursively check all nested objects and arrays
        for value in obj.values():
            if isinstance(value, dict):
                if check_object(value):
                    return True
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict) and check_object(item):
                        return True

        return False

    return check_object(schema)
```