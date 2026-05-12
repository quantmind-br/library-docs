---
title: math_utils - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/math_utils/
source: sitemap
fetched_at: 2026-05-07T21:38:42.273602148-03:00
rendered_js: false
word_count: 72
summary: This document provides a technical reference for mathematical utility functions used in the vLLM library, specifically covering division, rounding, and bitwise operations.
tags:
    - math-utils
    - vllm
    - bitwise-operations
    - integer-arithmetic
    - ceiling-division
category: reference
---

Math utility functions for vLLM.

## cdiv [¶](#vllm.utils.math_utils.cdiv "Permanent link")

Ceiling division.

Source code in `vllm/utils/math_utils.py`

```
defcdiv(a: int, b: int) -> int:
"""Ceiling division."""
    return -(a // -b)
```

## largest\_power\_of\_2\_divisor [¶](#vllm.utils.math_utils.largest_power_of_2_divisor "Permanent link")

```
largest_power_of_2_divisor(n: int) -> int
```

Return the largest power-of-2 that divides *n* (isolate lowest set bit).

Source code in `vllm/utils/math_utils.py`

```
deflargest_power_of_2_divisor(n: int) -> int:
"""Return the largest power-of-2 that divides *n* (isolate lowest set bit)."""
    return n & (-n)
```

## next\_power\_of\_2 [¶](#vllm.utils.math_utils.next_power_of_2 "Permanent link")

```
next_power_of_2(n: int) -> int
```

The next power of 2 (inclusive)

Source code in `vllm/utils/math_utils.py`

```
defnext_power_of_2(n: int) -> int:
"""The next power of 2 (inclusive)"""
    return 1 if n < 1 else 1 << (n - 1).bit_length()
```

## round\_down [¶](#vllm.utils.math_utils.round_down "Permanent link")

Round down x to the nearest multiple of y.

Source code in `vllm/utils/math_utils.py`

```
defround_down(x: int, y: int) -> int:
"""Round down x to the nearest multiple of y."""
    return (x // y) * y
```

## round\_up [¶](#vllm.utils.math_utils.round_up "Permanent link")

Round up x to the nearest multiple of y.

Source code in `vllm/utils/math_utils.py`

```
defround_up(x: int, y: int) -> int:
"""Round up x to the nearest multiple of y."""
    return ((x + y - 1) // y) * y
```