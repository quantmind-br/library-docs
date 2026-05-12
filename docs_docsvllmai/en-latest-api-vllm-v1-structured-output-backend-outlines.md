---
title: backend_outlines - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/structured_output/backend_outlines/
source: sitemap
fetched_at: 2026-05-07T21:42:01.249626591-03:00
rendered_js: false
word_count: 115
summary: This document defines the OutlinesGrammar class and utility functions for managing structured output in vLLM by interfacing with the Outlines library to validate and enforce token sequences via finite state machines.
tags:
    - structured-output
    - vllm
    - fsm
    - token-constraints
    - grammar-parsing
    - regex-validation
category: reference
---

## OutlinesGrammar `dataclass` [¶](#vllm.v1.structured_output.backend_outlines.OutlinesGrammar "Permanent link")

Bases: `StructuredOutputGrammar`

Source code in `vllm/v1/structured_output/backend_outlines.py`

```
@dataclass
classOutlinesGrammar(StructuredOutputGrammar):
    vocab_size: int
    guide: oc.Guide = field(hash=False)
    num_processed_tokens: int = field(
        default_factory=lambda: 0, repr=False, hash=False, init=False
    )

    # outlines_core signals done on DFA accept; vLLM expects done after EOS.
    # We delay the finished flag by one step so EOS can still be emitted.
    _prev_finished: bool = field(default=False, init=False, repr=False, hash=False)

    defaccept_tokens(self, request_id: str, tokens: list[int]) -> bool:
"""Accepts a list of tokens and advances the FSM.

        Returns True if the FSM was advanced successfully.
        Returns False if the FSM failed to advance.
        """
        if self.guide.accepts_tokens(tokens):
            # Advance can fail when the next state reached after advancing with
            # the current tokens is a dead state. This is because Guide.accepts_tokens()
            # only checks whether the current tokens can be accepted,
            # whereas guide.advance() additionally checks the next state
            # after all tokens are accepted.
            # We need to be aware that the FSM must be prepared without dead states.
            for t in tokens:
                self.guide.advance(t)
                self.num_processed_tokens += 1
            return True
        return False

    defrollback(self, num_tokens: int) -> None:
        self.guide.rollback_state(num_tokens)
        self.num_processed_tokens -= num_tokens

    defvalidate_tokens(self, tokens: list[int]) -> list[int]:
        accepted: list[int] = []
        for tok in tokens:
            accepted.append(tok)
            if not self.guide.accepts_tokens(accepted):
                accepted.pop()
                break
        return accepted

    deffill_bitmask(self, bitmask: torch.Tensor, idx: int) -> None:
        mask = bitmask[idx]
        self.guide.write_mask_into(mask.data_ptr(), mask.numel(), mask.element_size())

    defis_terminated(self) -> bool:
        curr = self.guide.is_finished()
        prev = self._prev_finished
        self._prev_finished = curr
        return prev

    defreset(self):
        self.num_processed_tokens = 0
        self._prev_finished = False
        self.guide.reset()
```

### accept\_tokens [¶](#vllm.v1.structured_output.backend_outlines.OutlinesGrammar.accept_tokens "Permanent link")

Accepts a list of tokens and advances the FSM.

Returns True if the FSM was advanced successfully. Returns False if the FSM failed to advance.

Source code in `vllm/v1/structured_output/backend_outlines.py`

```
defaccept_tokens(self, request_id: str, tokens: list[int]) -> bool:
"""Accepts a list of tokens and advances the FSM.

    Returns True if the FSM was advanced successfully.
    Returns False if the FSM failed to advance.
    """
    if self.guide.accepts_tokens(tokens):
        # Advance can fail when the next state reached after advancing with
        # the current tokens is a dead state. This is because Guide.accepts_tokens()
        # only checks whether the current tokens can be accepted,
        # whereas guide.advance() additionally checks the next state
        # after all tokens are accepted.
        # We need to be aware that the FSM must be prepared without dead states.
        for t in tokens:
            self.guide.advance(t)
            self.num_processed_tokens += 1
        return True
    return False
```

## \_check\_unsupported [¶](#vllm.v1.structured_output.backend_outlines._check_unsupported "Permanent link")

```
_check_unsupported(parsed) -> None
```

Check for regex features unsupported by regex-automata

Source code in `vllm/v1/structured_output/backend_outlines.py`

```
def_check_unsupported(parsed) -> None:
"""Check for regex features unsupported by regex-automata"""
    tokens = parsed.data if hasattr(parsed, "data") else parsed
    for ttype, tval in tokens:
        # backreference
        if ttype in (sre_parse.GROUPREF, sre_parse.GROUPREF_EXISTS):
            raise ValueError("Backreferences are unsupported.")

        # look-around assertion
        elif ttype in (sre_constants.ASSERT, sre_constants.ASSERT_NOT):
            raise ValueError("Look-Around assertion are unsupported.")

        # unicode word boundaries
        elif ttype == sre_parse.AT:
            if tval in (sre_constants.AT_BOUNDARY, sre_constants.AT_NON_BOUNDARY):
                raise ValueError("Unicode word boundaries are unsupported.")

        elif ttype == sre_parse.BRANCH:
            # tval is (None, branches)
            for branch in tval[1]:
                _check_unsupported(branch)

        # tval is (min, max, subpattern)
        elif ttype == sre_parse.MAX_REPEAT:
            _check_unsupported(tval[2])
```

## \_prefix\_needs\_context [¶](#vllm.v1.structured_output.backend_outlines._prefix_needs_context "Permanent link")

```
_prefix_needs_context(parsed) -> bool
```

Return True if there's a look-around/anchor before any consumer.

Source code in `vllm/v1/structured_output/backend_outlines.py`

```
def_prefix_needs_context(parsed) -> bool:
"""Return True if there's a look-around/anchor before any consumer."""

    defsubpattern_consumes(parsed) -> bool:
"""Return True if subpattern can consume at least one character."""
        tokens = parsed.data if hasattr(parsed, "data") else parsed
        for ttype, tval in tokens:
            # literal, character class, or dot always consumes
            if ttype in (sre_parse.LITERAL, sre_parse.IN, sre_parse.ANY):
                return True
            # quantified subpattern: check inner pattern
            elif ttype == sre_parse.MAX_REPEAT:
                _, mx, sub = tval
                if mx != 0 and subpattern_consumes(sub):
                    return True
            # alternation: if any branch consumes, the whole does
            elif ttype == sre_parse.BRANCH:
                _, branches = tval
                if any(subpattern_consumes(br) for br in branches):
                    return True
            # grouped subpattern: recurse into its contents
            elif ttype == sre_parse.SUBPATTERN and subpattern_consumes(tval[3]):
                return True
        # No consumers, return False
        return False

    tokens = parsed.data if hasattr(parsed, "data") else parsed
    for ttype, tval in tokens:
        # Direct anchors or look-around
        if ttype == sre_parse.AT or ttype in (
            sre_constants.ASSERT,
            sre_constants.ASSERT_NOT,
        ):
            return True

        # Nested subpattern: check
        if ttype == sre_parse.SUBPATTERN:
            # tval: (group, add_flags, del_flags, subpattern)
            if _prefix_needs_context(tval[3]):
                return True
            if subpattern_consumes(tval[3]):
                return False

        # if any branch has a prefix anchor => True,
        # else if at least one branch consumes => prefix ends => False
        elif ttype == sre_parse.BRANCH:
            saw_consumer = False
            for br in tval[1]:
                if _prefix_needs_context(br):
                    return True
                if subpattern_consumes(br):
                    saw_consumer = True
            if saw_consumer:
                return False

        # Immediate consumer tokens
        elif ttype in (sre_parse.LITERAL, sre_parse.IN, sre_parse.ANY):
            return False

        # if subpattern has anchor => True, if it can consume => stop
        elif ttype == sre_parse.MAX_REPEAT:
            if _prefix_needs_context(tval[2]):
                return True
            if subpattern_consumes(tval[2]):
                return False

    return False
```

## validate\_regex\_is\_buildable [¶](#vllm.v1.structured_output.backend_outlines.validate_regex_is_buildable "Permanent link")

```
validate_regex_is_buildable(pattern: str) -> None
```

Validates that the input regex is not using unsupported features of the `regex-automata` crate (outlines\_core regex engine) and has a universal start state. definition of universal start state used can be found at: https://docs.rs/regex-automata/latest/regex\_automata/dfa/trait.Automaton.html#method.universal\_start\_state

Source code in `vllm/v1/structured_output/backend_outlines.py`

```
defvalidate_regex_is_buildable(pattern: str) -> None:
"""
    Validates that the input regex is not using unsupported features
    of the `regex-automata` crate (outlines_core regex engine) and has a
    universal start state.
    definition of universal start state used can be found at:
    https://docs.rs/regex-automata/latest/regex_automata/dfa/trait.Automaton.html#method.universal_start_state
    """
    try:
        parsed = sre_parse.parse(pattern)

    except sre_constants.error as e:
        raise ValueError(f"Error parsing regex: {e}") frome

    try:
        _check_unsupported(parsed)
    except ValueError as e:
        raise ValueError(
            f"Regex uses unsupported feature for structured outputs: {e}. "
            "Only basic matching constructs are supported—lookarounds, "
            "backreferences, and unicode boundaries are not."
        ) frome

    if _prefix_needs_context(parsed):
        raise ValueError(
            "Regex does not have a anchored universal start state"
            "This means that the Regex uses anchors (^) or look-arounds "
            "in a way which requires context before any token is matched."
            "structured outputs needs regexes that can match without needing "
            "that context. Try rewriting the pattern without using these "
            f"constructs. Pattern:\n{pattern}"
        )
```