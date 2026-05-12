---
title: backend_types - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/structured_output/backend_types/
source: sitemap
fetched_at: 2026-05-07T21:42:02.537260221-03:00
rendered_js: false
word_count: 365
summary: This document defines the abstract base classes StructuredOutputBackend and StructuredOutputGrammar, which provide the interface for engine-level and request-level handling of constrained, structured output generation in vLLM.
tags:
    - vllm
    - structured-output
    - grammar-compilation
    - token-bitmask
    - abstract-base-class
    - inference-engine
category: reference
---

## StructuredOutputBackend `dataclass` [¶](#vllm.v1.structured_output.backend_types.StructuredOutputBackend "Permanent link")

Bases: `ABC`

Engine-level backend for structured output requests.

Source code in `vllm/v1/structured_output/backend_types.py`

```
@dataclass
classStructuredOutputBackend(ABC):
"""Engine-level backend for structured output requests."""

    vllm_config: VllmConfig
    tokenizer: TokenizerLike
    vocab_size: int

    @abstractmethod
    defcompile_grammar(
        self, request_type: StructuredOutputOptions, grammar_spec: str
    ) -> StructuredOutputGrammar:
"""
        Compiles a grammar specification into a structured output grammar.

        Args:
            request_type (StructuredOutputOptions): The type of structured
                output request.
            grammar_spec (str): The grammar specification to compile.

        Returns:
            StructuredOutputGrammar: The compiled structured output grammar.
        """

    @abstractmethod
    defallocate_token_bitmask(self, max_num_seqs: int) -> "torch.Tensor":
"""
        Allocates a token bitmask for the specified maximum number of sequences.

        Args:
            max_num_seqs (int): The maximum number of sequences for which
                to allocate the bitmask.
        """

    @abstractmethod
    defdestroy(self):
"""
        Backend-specific cleanup.
        """
```

### allocate\_token\_bitmask `abstractmethod` [¶](#vllm.v1.structured_output.backend_types.StructuredOutputBackend.allocate_token_bitmask "Permanent link")

```
allocate_token_bitmask(max_num_seqs: int) -> Tensor
```

Allocates a token bitmask for the specified maximum number of sequences.

Parameters:

Name Type Description Default `max_num_seqs` `int`

The maximum number of sequences for which to allocate the bitmask.

*required*

Source code in `vllm/v1/structured_output/backend_types.py`

```
@abstractmethod
defallocate_token_bitmask(self, max_num_seqs: int) -> "torch.Tensor":
"""
    Allocates a token bitmask for the specified maximum number of sequences.

    Args:
        max_num_seqs (int): The maximum number of sequences for which
            to allocate the bitmask.
    """
```

### compile\_grammar `abstractmethod` [¶](#vllm.v1.structured_output.backend_types.StructuredOutputBackend.compile_grammar "Permanent link")

```
compile_grammar(
    request_type: StructuredOutputOptions, grammar_spec: str
) -> StructuredOutputGrammar
```

Compiles a grammar specification into a structured output grammar.

Parameters:

Name Type Description Default `request_type` `StructuredOutputOptions`

The type of structured output request.

*required* `grammar_spec` `str`

The grammar specification to compile.

*required*

Returns:

Name Type Description `StructuredOutputGrammar` `StructuredOutputGrammar`

The compiled structured output grammar.

Source code in `vllm/v1/structured_output/backend_types.py`

```
@abstractmethod
defcompile_grammar(
    self, request_type: StructuredOutputOptions, grammar_spec: str
) -> StructuredOutputGrammar:
"""
    Compiles a grammar specification into a structured output grammar.

    Args:
        request_type (StructuredOutputOptions): The type of structured
            output request.
        grammar_spec (str): The grammar specification to compile.

    Returns:
        StructuredOutputGrammar: The compiled structured output grammar.
    """
```

### destroy `abstractmethod` [¶](#vllm.v1.structured_output.backend_types.StructuredOutputBackend.destroy "Permanent link")

Backend-specific cleanup.

Source code in `vllm/v1/structured_output/backend_types.py`

```
@abstractmethod
defdestroy(self):
"""
    Backend-specific cleanup.
    """
```

## StructuredOutputGrammar [¶](#vllm.v1.structured_output.backend_types.StructuredOutputGrammar "Permanent link")

Bases: `ABC`

Request-level backend for structured output requests.

Source code in `vllm/v1/structured_output/backend_types.py`

```
classStructuredOutputGrammar(ABC):
"""Request-level backend for structured output requests."""

    @abstractmethod
    defaccept_tokens(self, request_id: str, tokens: list[int]) -> bool:
"""
        Determines whether the provided tokens are accepted for the
        given request.

        Args:
            request_id (str): The unique identifier for the request.
            tokens (list[int]): A list of token IDs to evaluate.

        Returns:
            bool: True if the tokens are accepted, False otherwise.
        """

    @abstractmethod
    defvalidate_tokens(self, tokens: list[int]) -> list[int]:
"""
        Validates the provided tokens against the grammar.
        Will not advance the FSM.

        Args:
            tokens (list[int]): A list of token IDs to validate.

        Returns:
            list[int]: A list of accepted token IDs. Will be a prefix
                of the input tokens, and empty if none are accepted.
        """

    @abstractmethod
    defrollback(self, num_tokens: int) -> None:
"""
        Rolls back the state of the grammar by a specified number of tokens.
        Will also revert counters for the number of processed tokens.

        Args:
            num_tokens (int): The number of tokens to roll back.
        """

    @abstractmethod
    deffill_bitmask(self, bitmask: "torch.Tensor", batch_index: int) -> None:
"""
        Fills the bitmask for a specific batch index.

        Args:
            bitmask (torch.Tensor): The bitmask to fill
            batch_index (int): The index in the bitmask to fill
        """

    @abstractmethod
    defis_terminated(self) -> bool:
"""
        Checks whether the structured output process has terminated.

        Returns:
            bool: True if the process is terminated, False otherwise.
        """

    @abstractmethod
    defreset(self):
"""
        Resets the state of the structured output grammar.
        """
```

### accept\_tokens `abstractmethod` [¶](#vllm.v1.structured_output.backend_types.StructuredOutputGrammar.accept_tokens "Permanent link")

Determines whether the provided tokens are accepted for the given request.

Parameters:

Name Type Description Default `request_id` `str`

The unique identifier for the request.

*required* `tokens` `list[int]`

A list of token IDs to evaluate.

*required*

Returns:

Name Type Description `bool` `bool`

True if the tokens are accepted, False otherwise.

Source code in `vllm/v1/structured_output/backend_types.py`

```
@abstractmethod
defaccept_tokens(self, request_id: str, tokens: list[int]) -> bool:
"""
    Determines whether the provided tokens are accepted for the
    given request.

    Args:
        request_id (str): The unique identifier for the request.
        tokens (list[int]): A list of token IDs to evaluate.

    Returns:
        bool: True if the tokens are accepted, False otherwise.
    """
```

### fill\_bitmask `abstractmethod` [¶](#vllm.v1.structured_output.backend_types.StructuredOutputGrammar.fill_bitmask "Permanent link")

```
fill_bitmask(bitmask: Tensor, batch_index: int) -> None
```

Fills the bitmask for a specific batch index.

Parameters:

Name Type Description Default `bitmask` `Tensor`

The bitmask to fill

*required* `batch_index` `int`

The index in the bitmask to fill

*required*

Source code in `vllm/v1/structured_output/backend_types.py`

```
@abstractmethod
deffill_bitmask(self, bitmask: "torch.Tensor", batch_index: int) -> None:
"""
    Fills the bitmask for a specific batch index.

    Args:
        bitmask (torch.Tensor): The bitmask to fill
        batch_index (int): The index in the bitmask to fill
    """
```

### is\_terminated `abstractmethod` [¶](#vllm.v1.structured_output.backend_types.StructuredOutputGrammar.is_terminated "Permanent link")

Checks whether the structured output process has terminated.

Returns:

Name Type Description `bool` `bool`

True if the process is terminated, False otherwise.

Source code in `vllm/v1/structured_output/backend_types.py`

```
@abstractmethod
defis_terminated(self) -> bool:
"""
    Checks whether the structured output process has terminated.

    Returns:
        bool: True if the process is terminated, False otherwise.
    """
```

### reset `abstractmethod` [¶](#vllm.v1.structured_output.backend_types.StructuredOutputGrammar.reset "Permanent link")

Resets the state of the structured output grammar.

Source code in `vllm/v1/structured_output/backend_types.py`

```
@abstractmethod
defreset(self):
"""
    Resets the state of the structured output grammar.
    """
```

### rollback `abstractmethod` [¶](#vllm.v1.structured_output.backend_types.StructuredOutputGrammar.rollback "Permanent link")

```
rollback(num_tokens: int) -> None
```

Rolls back the state of the grammar by a specified number of tokens. Will also revert counters for the number of processed tokens.

Parameters:

Name Type Description Default `num_tokens` `int`

The number of tokens to roll back.

*required*

Source code in `vllm/v1/structured_output/backend_types.py`

```
@abstractmethod
defrollback(self, num_tokens: int) -> None:
"""
    Rolls back the state of the grammar by a specified number of tokens.
    Will also revert counters for the number of processed tokens.

    Args:
        num_tokens (int): The number of tokens to roll back.
    """
```

### validate\_tokens `abstractmethod` [¶](#vllm.v1.structured_output.backend_types.StructuredOutputGrammar.validate_tokens "Permanent link")

Validates the provided tokens against the grammar. Will not advance the FSM.

Parameters:

Name Type Description Default `tokens` `list[int]`

A list of token IDs to validate.

*required*

Returns:

Type Description `list[int]`

list\[int]: A list of accepted token IDs. Will be a prefix of the input tokens, and empty if none are accepted.

Source code in `vllm/v1/structured_output/backend_types.py`

```
@abstractmethod
defvalidate_tokens(self, tokens: list[int]) -> list[int]:
"""
    Validates the provided tokens against the grammar.
    Will not advance the FSM.

    Args:
        tokens (list[int]): A list of token IDs to validate.

    Returns:
        list[int]: A list of accepted token IDs. Will be a prefix
            of the input tokens, and empty if none are accepted.
    """
```