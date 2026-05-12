---
title: backend_xgrammar - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/structured_output/backend_xgrammar/
source: sitemap
fetched_at: 2026-05-07T21:42:03.309135043-03:00
rendered_js: false
word_count: 114
summary: This document defines the XgrammarGrammar class and related utility functions for managing structured output generation using the xgrammar backend within vLLM.
tags:
    - vllm
    - structured-output
    - xgrammar
    - fsm
    - token-validation
    - json-schema
    - grammar-parsing
category: reference
---

## XgrammarGrammar `dataclass` [¶](#vllm.v1.structured_output.backend_xgrammar.XgrammarGrammar "Permanent link")

Bases: `StructuredOutputGrammar`

Source code in `vllm/v1/structured_output/backend_xgrammar.py`

```
@dataclass
classXgrammarGrammar(StructuredOutputGrammar):
    # NOTE: This would be a generic-enough class for
    # supporting different backends, in the future.
    # For now, just xgrammar.
    #
    # https://xgrammar.mlc.ai/docs/api/python/index.html#xgrammar.GrammarMatcher.find_jump_forward_string
    # for jump-forward decoding

    vocab_size: int
    matcher: xgr.GrammarMatcher = field(hash=False)
    ctx: xgr.CompiledGrammar = field(hash=False)
    num_processed_tokens: int = field(
        default_factory=lambda: 0, repr=False, hash=False, init=False
    )
    _is_terminated: bool = field(default=False, repr=False, hash=False)

    defaccept_tokens(self, request_id: str, tokens: list[int]) -> bool:
"""Accepts a list of tokens and advances the FSM.

        Returns True if the FSM was advanced successfully.
        Returns False if the FSM failed to advance.
        """
        if self._is_terminated:
            return False
        for token in tokens:
            if not self.matcher.accept_token(token):
                logger.error(
                    "Failed to advance FSM for request %s "
                    "for tokens %s. Please file an issue.",
                    request_id,
                    token,
                )
                return False
            self.num_processed_tokens += 1
        self._is_terminated = self.matcher.is_terminated()
        return True

    defvalidate_tokens(self, tokens: list[int]) -> list[int]:
"""Checks if the list of tokens are accepted by the FSM in sequence.
        Will not advance the FSM.

        Returns the prefix list of tokens that are accepted by the FSM.
        """
        accepted_tokens = []
        for token in tokens:
            if self.matcher.accept_token(token):
                accepted_tokens.append(token)
            else:
                break
        if len(accepted_tokens) > 0:
            # Rollback the FSM to the initial state
            self.matcher.rollback(len(accepted_tokens))
        return accepted_tokens

    defrollback(self, num_tokens: int) -> None:
        self.matcher.rollback(num_tokens)
        self.num_processed_tokens -= num_tokens
        self._is_terminated = self.matcher.is_terminated()

    deffill_bitmask(self, bitmask: torch.Tensor, idx: int) -> None:
        self.matcher.fill_next_token_bitmask(bitmask, idx)

    defis_terminated(self) -> bool:
        return self._is_terminated

    defreset(self):
        self.num_processed_tokens = 0
        self.matcher.reset()
```

### accept\_tokens [¶](#vllm.v1.structured_output.backend_xgrammar.XgrammarGrammar.accept_tokens "Permanent link")

Accepts a list of tokens and advances the FSM.

Returns True if the FSM was advanced successfully. Returns False if the FSM failed to advance.

Source code in `vllm/v1/structured_output/backend_xgrammar.py`

```
defaccept_tokens(self, request_id: str, tokens: list[int]) -> bool:
"""Accepts a list of tokens and advances the FSM.

    Returns True if the FSM was advanced successfully.
    Returns False if the FSM failed to advance.
    """
    if self._is_terminated:
        return False
    for token in tokens:
        if not self.matcher.accept_token(token):
            logger.error(
                "Failed to advance FSM for request %s "
                "for tokens %s. Please file an issue.",
                request_id,
                token,
            )
            return False
        self.num_processed_tokens += 1
    self._is_terminated = self.matcher.is_terminated()
    return True
```

### validate\_tokens [¶](#vllm.v1.structured_output.backend_xgrammar.XgrammarGrammar.validate_tokens "Permanent link")

Checks if the list of tokens are accepted by the FSM in sequence. Will not advance the FSM.

Returns the prefix list of tokens that are accepted by the FSM.

Source code in `vllm/v1/structured_output/backend_xgrammar.py`

```
defvalidate_tokens(self, tokens: list[int]) -> list[int]:
"""Checks if the list of tokens are accepted by the FSM in sequence.
    Will not advance the FSM.

    Returns the prefix list of tokens that are accepted by the FSM.
    """
    accepted_tokens = []
    for token in tokens:
        if self.matcher.accept_token(token):
            accepted_tokens.append(token)
        else:
            break
    if len(accepted_tokens) > 0:
        # Rollback the FSM to the initial state
        self.matcher.rollback(len(accepted_tokens))
    return accepted_tokens
```

## has\_xgrammar\_unsupported\_json\_features [¶](#vllm.v1.structured_output.backend_xgrammar.has_xgrammar_unsupported_json_features "Permanent link")

```
has_xgrammar_unsupported_json_features(
    schema: dict[str, Any],
) -> bool
```

Check if JSON schema contains features unsupported by xgrammar.

Source code in `vllm/v1/structured_output/backend_xgrammar.py`

```
defhas_xgrammar_unsupported_json_features(schema: dict[str, Any]) -> bool:
"""Check if JSON schema contains features unsupported by xgrammar."""

    defcheck_object(obj: dict[str, Any]) -> bool:
        if not isinstance(obj, dict):
            return False

        # Check for numeric ranges
        if obj.get("type") in ("integer", "number") and ("multipleOf" in obj):
            return True

        # Check for array unsupported keywords
        if obj.get("type") == "array" and any(
            key in obj
            for key in ("uniqueItems", "contains", "minContains", "maxContains")
        ):
            return True

        # Unsupported keywords for strings
        if (
            obj.get("type") == "string"
            and "format" in obj
            and obj["format"] not in STRING_SUPPORTED_FORMATS
        ):
            return True

        # Unsupported keywords for objects
        if obj.get("type") == "object" and any(
            key in obj for key in ("patternProperties", "propertyNames")
        ):
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

## validate\_xgrammar\_grammar [¶](#vllm.v1.structured_output.backend_xgrammar.validate_xgrammar_grammar "Permanent link")

Validate that the request is supported by structured output.

Raises ValueError if the request is not supported.

Source code in `vllm/v1/structured_output/backend_xgrammar.py`

```
defvalidate_xgrammar_grammar(sampling_params: SamplingParams) -> None:
"""Validate that the request is supported by structured output.

    Raises ValueError if the request is not supported.
    """
    if sampling_params.structured_outputs is None:
        return

    so_params = sampling_params.structured_outputs

    if so_params.regex:
        try:
            xgr.Grammar.from_regex(so_params.regex)
        except Exception as err:
            raise ValueError(
                f"Failed to transform regex into a grammar: {err}"
            ) fromerr

    if so_params.choice:
        choice_grammar = choice_as_grammar(so_params.choice)
        try:
            xgr.Grammar.from_ebnf(choice_grammar)
        except Exception as err:
            raise ValueError(
                f"Failed to transform choices into a grammar: {err}"
            ) fromerr
        so_params.choice = None
        so_params.grammar = choice_grammar
        return

    if so_params.json:
        if isinstance(so_params.json, str):
            try:
                schema = json.loads(so_params.json)
            except json.JSONDecodeError as e:
                raise ValueError("Invalid JSON grammar specification.") frome
        else:
            schema = so_params.json

        if has_xgrammar_unsupported_json_features(schema):
            raise ValueError(
                "The provided JSON schema contains features not supported by xgrammar."
            )

        try:
            xgr.Grammar.from_json_schema(schema)
        except Exception as err:
            raise ValueError(
                f"Failed to transform json schema into a grammar: {err}"
            ) fromerr
        return

    if so_params.grammar:
        if grammar_is_likely_lark(so_params.grammar):
            # xgrammar supports EBNF grammars only
            try:
                so_params.grammar = convert_lark_to_ebnf(so_params.grammar)
            except ValueError as e:
                raise ValueError(
                    "Failed to convert the grammar from Lark to EBNF. "
                ) frome

        # Test parsing EBNF grammar, possibly already converted from Lark
        try:
            # parse the grammar, but we aren't compiling it.
            xgr.Grammar.from_ebnf(so_params.grammar)
        except Exception as e:
            raise ValueError("Invalid grammar specification.") frome
        return

    if so_params.structural_tag:
        try:
            s_tag = json.loads(so_params.structural_tag)

            # Using the deprecated method of compiling structural tag
            if "structures" in s_tag:
                tags = [
                    xgr.StructuralTagItem(
                        begin=s["begin"],
                        schema=json.dumps(s["schema"]),
                        end=s["end"],
                    )
                    for s in s_tag["structures"]
                ]
                xgr.Grammar.from_structural_tag(tags, s_tag["triggers"])
            else:
                xgr.Grammar.from_structural_tag(so_params.structural_tag)
        except Exception as e:
            raise ValueError("Invalid structural tag specification.") frome
```