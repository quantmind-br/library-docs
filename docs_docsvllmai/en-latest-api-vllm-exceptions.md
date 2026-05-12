---
title: exceptions - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/exceptions/
source: sitemap
fetched_at: 2026-05-07T21:21:55.077307032-03:00
rendered_js: false
word_count: 110
summary: This document defines the custom exception classes used within the vLLM library for handling errors related to missing resources and request validation failures.
tags:
    - vllm
    - exception-handling
    - error-reporting
    - python-exceptions
    - software-development
category: reference
---

Custom exceptions for vLLM.

## LoRAAdapterNotFoundError [¶](#vllm.exceptions.LoRAAdapterNotFoundError "Permanent link")

Bases: `VLLMNotFoundError`

Exception raised when a LoRA adapter is not found.

This exception is thrown when a requested LoRA adapter does not exist in the system.

Attributes:

Name Type Description `message` `str`

The error message string describing the exception

Source code in `vllm/exceptions.py`

```
classLoRAAdapterNotFoundError(VLLMNotFoundError):
"""Exception raised when a LoRA adapter is not found.

    This exception is thrown when a requested LoRA adapter does not exist
    in the system.

    Attributes:
        message: The error message string describing the exception
    """

    message: str

    def__init__(
        self,
        lora_name: str,
        lora_path: str,
    ) -> None:
        message = f"Loading lora {lora_name} failed: No adapter found for {lora_path}"
        self.message = message

    def__str__(self):
        return self.message
```

## VLLMNotFoundError [¶](#vllm.exceptions.VLLMNotFoundError "Permanent link")

Bases: `Exception`

vLLM-specific NotFoundError

Source code in `vllm/exceptions.py`

```
classVLLMNotFoundError(Exception):
"""vLLM-specific NotFoundError"""

    pass
```

## VLLMValidationError [¶](#vllm.exceptions.VLLMValidationError "Permanent link")

Bases: `ValueError`

vLLM-specific validation error for request validation failures.

Parameters:

Name Type Description Default `message` `str`

The error message describing the validation failure.

*required* `parameter` `str | None`

Optional parameter name that failed validation.

`None` `value` `Any`

Optional value that was rejected during validation.

`None`

Source code in `vllm/exceptions.py`

```
classVLLMValidationError(ValueError):
"""vLLM-specific validation error for request validation failures.

    Args:
        message: The error message describing the validation failure.
        parameter: Optional parameter name that failed validation.
        value: Optional value that was rejected during validation.
    """

    def__init__(
        self,
        message: str,
        *,
        parameter: str | None = None,
        value: Any = None,
    ) -> None:
        super().__init__(message)
        self.parameter = parameter
        self.value = value

    def__str__(self):
        base = super().__str__()
        extras = []
        if self.parameter is not None:
            extras.append(f"parameter={self.parameter}")
        if self.value is not None:
            extras.append(f"value={self.value}")
        return f"{base} ({', '.join(extras)})" if extras else base
```