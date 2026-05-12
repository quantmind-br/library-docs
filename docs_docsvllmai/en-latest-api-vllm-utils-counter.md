---
title: counter - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/counter/
source: sitemap
fetched_at: 2026-05-07T21:38:32.109027051-03:00
rendered_js: false
word_count: 59
summary: This document provides the technical specification and implementation details for the AtomicCounter class, which ensures thread-safe integer increment and decrement operations.
tags:
    - python
    - threading
    - concurrency
    - atomic-operations
    - utility-class
    - synchronization
category: reference
---

## AtomicCounter [¶](#vllm.utils.counter.AtomicCounter "Permanent link")

An atomic, thread-safe counter

Source code in `vllm/utils/counter.py`

```
classAtomicCounter:
"""An atomic, thread-safe counter"""

    def__init__(self, initial: int = 0) -> None:
"""Initialize a new atomic counter to given initial value"""
        super().__init__()

        self._value = initial
        self._lock = threading.Lock()

    @property
    defvalue(self) -> int:
        return self._value

    definc(self, num: int = 1) -> int:
"""Atomically increment the counter by num and return the new value"""
        with self._lock:
            self._value += num
            return self._value

    defdec(self, num: int = 1) -> int:
"""Atomically decrement the counter by num and return the new value"""
        with self._lock:
            self._value -= num
            return self._value
```

### \_\_init\__ [¶](#vllm.utils.counter.AtomicCounter.__init__ "Permanent link")

```
__init__(initial: int = 0) -> None
```

Initialize a new atomic counter to given initial value

Source code in `vllm/utils/counter.py`

```
def__init__(self, initial: int = 0) -> None:
"""Initialize a new atomic counter to given initial value"""
    super().__init__()

    self._value = initial
    self._lock = threading.Lock()
```

### dec [¶](#vllm.utils.counter.AtomicCounter.dec "Permanent link")

Atomically decrement the counter by num and return the new value

Source code in `vllm/utils/counter.py`

```
defdec(self, num: int = 1) -> int:
"""Atomically decrement the counter by num and return the new value"""
    with self._lock:
        self._value -= num
        return self._value
```

### inc [¶](#vllm.utils.counter.AtomicCounter.inc "Permanent link")

Atomically increment the counter by num and return the new value

Source code in `vllm/utils/counter.py`

```
definc(self, num: int = 1) -> int:
"""Atomically increment the counter by num and return the new value"""
    with self._lock:
        self._value += num
        return self._value
```