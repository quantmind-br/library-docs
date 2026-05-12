---
title: state - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/sample/logits_processor/state/
source: sitemap
fetched_at: 2026-05-07T21:41:26.495808658-03:00
rendered_js: false
word_count: 386
summary: The BatchUpdateBuilder class manages and tracks state transitions—specifically additions, removals, and movements—within a persistent batch of requests for logit processors.
tags:
    - batch-processing
    - logit-processor
    - state-management
    - vllm
    - data-structures
category: reference
---

## BatchUpdateBuilder [¶](#vllm.v1.sample.logits_processor.state.BatchUpdateBuilder "Permanent link")

Helps track persistent batch state changes and build a batch update data structure for logitsprocs Assumptions: * All information about requests removed from persistent batch during a step is aggregated in self.\_removed through calls to self.removed\_append() at the beginning of a step. This must happen before the first time that self.removed, self.pop\_removed() or self.peek\_removed() are invoked in a given step * After the first time that self.removed, self.pop\_removed() or self.peek\_removed() are read in a step, no new removals are registered using self.removed\_append() * Elements of self.\_removed are never directly modified, added or removed (i.e. modification is only via self.removed\_append() and self.pop\_removed()) Guarantees under above assumptions: * self.removed is always sorted in descending order * self.pop\_removed() and self.peek\_removed() both return the lowest removed request index in the current step

Source code in `vllm/v1/sample/logits_processor/state.py`

```
classBatchUpdateBuilder:
"""Helps track persistent batch state changes and build
    a batch update data structure for logitsprocs
    Assumptions:
    * All information about requests removed from persistent batch
      during a step is aggregated in self._removed through calls to
      self.removed_append() at the beginning of a step. This must happen
      before the first time that self.removed, self.pop_removed()
      or self.peek_removed() are invoked in a given step
    * After the first time that self.removed, self.pop_removed()
      or self.peek_removed() are read in a step, no new removals
      are registered using self.removed_append()
    * Elements of self._removed are never directly modified, added or
      removed (i.e. modification is only via self.removed_append() and
      self.pop_removed())
    Guarantees under above assumptions:
    * self.removed is always sorted in descending order
    * self.pop_removed() and self.peek_removed() both return
      the lowest removed request index in the current step
    """

    _removed: list[RemovedRequest]
    _is_removed_sorted: bool
    added: list[AddedRequest]
    moved: list[MovedRequest]

    def__init__(
        self,
        removed: list[RemovedRequest] | None = None,
        added: list[AddedRequest] | None = None,
        moved: list[MovedRequest] | None = None,
    ) -> None:
        self._removed = removed or []
        self.added = added or []
        self.moved = moved or []
        self._is_removed_sorted = False

        # Used to track changes in the pooling case
        # where we don't populate the added list.
        self.batch_changed = False

    def_ensure_removed_sorted(self) -> None:
"""Sort removed request indices in
        descending order.
        Idempotent after first call in a
        given step, until reset.
        """
        if not self._is_removed_sorted:
            self._removed.sort(reverse=True)
            self._is_removed_sorted = True

    @property
    defremoved(self) -> list[RemovedRequest]:
"""Removed request indices sorted in
        descending order"""
        self._ensure_removed_sorted()
        return self._removed

    defremoved_append(self, index: int) -> None:
"""Register the removal of a request from the persistent batch.

        Must not be called after the first time self.removed,
        self.pop_removed() or self.peek_removed() are invoked.

        Args:
          index: request index
        """
        if self._is_removed_sorted:
            raise RuntimeError(
                "Cannot register new removed request after self.removed has been read."
            )
        self._removed.append(index)
        self.batch_changed = True

    defhas_removed(self) -> bool:
        return bool(self._removed)

    defpeek_removed(self) -> int | None:
"""Return lowest removed request index"""
        if self.has_removed():
            self._ensure_removed_sorted()
            return self._removed[-1]
        return None

    defpop_removed(self) -> int | None:
"""Pop lowest removed request index"""
        if self.has_removed():
            self._ensure_removed_sorted()
            return self._removed.pop()
        return None

    defreset(self) -> bool:
"""Returns True if there were any changes to the batch."""
        self._is_removed_sorted = False
        self._removed.clear()
        self.added.clear()
        self.moved.clear()
        batch_changed = self.batch_changed
        self.batch_changed = False
        return batch_changed

    defget_and_reset(self, batch_size: int) -> BatchUpdate | None:
"""Generate a logitsprocs batch update data structure and reset
        internal batch update builder state.

        Args:
          batch_size: current persistent batch size

        Returns:
          Frozen logitsprocs batch update instance; `None` if no updates
        """
        # Reset removal-sorting logic
        self._is_removed_sorted = False
        self.batch_changed = False
        if not any((self._removed, self.moved, self.added)):
            # No update; short-circuit
            return None
        # Build batch state update
        batch_update = BatchUpdate(
            batch_size=batch_size,
            removed=self._removed,
            moved=self.moved,
            added=self.added,
        )
        self._removed = []
        self.moved = []
        self.added = []
        return batch_update
```

### removed `property` [¶](#vllm.v1.sample.logits_processor.state.BatchUpdateBuilder.removed "Permanent link")

```
removed: list[RemovedRequest]
```

Removed request indices sorted in descending order

### \_ensure\_removed\_sorted [¶](#vllm.v1.sample.logits_processor.state.BatchUpdateBuilder._ensure_removed_sorted "Permanent link")

```
_ensure_removed_sorted() -> None
```

Sort removed request indices in descending order. Idempotent after first call in a given step, until reset.

Source code in `vllm/v1/sample/logits_processor/state.py`

```
def_ensure_removed_sorted(self) -> None:
"""Sort removed request indices in
    descending order.
    Idempotent after first call in a
    given step, until reset.
    """
    if not self._is_removed_sorted:
        self._removed.sort(reverse=True)
        self._is_removed_sorted = True
```

### get\_and\_reset [¶](#vllm.v1.sample.logits_processor.state.BatchUpdateBuilder.get_and_reset "Permanent link")

Generate a logitsprocs batch update data structure and reset internal batch update builder state.

Parameters:

Name Type Description Default `batch_size` `int`

current persistent batch size

*required*

Returns:

Type Description `BatchUpdate | None`

Frozen logitsprocs batch update instance; `None` if no updates

Source code in `vllm/v1/sample/logits_processor/state.py`

```
defget_and_reset(self, batch_size: int) -> BatchUpdate | None:
"""Generate a logitsprocs batch update data structure and reset
    internal batch update builder state.

    Args:
      batch_size: current persistent batch size

    Returns:
      Frozen logitsprocs batch update instance; `None` if no updates
    """
    # Reset removal-sorting logic
    self._is_removed_sorted = False
    self.batch_changed = False
    if not any((self._removed, self.moved, self.added)):
        # No update; short-circuit
        return None
    # Build batch state update
    batch_update = BatchUpdate(
        batch_size=batch_size,
        removed=self._removed,
        moved=self.moved,
        added=self.added,
    )
    self._removed = []
    self.moved = []
    self.added = []
    return batch_update
```

### peek\_removed [¶](#vllm.v1.sample.logits_processor.state.BatchUpdateBuilder.peek_removed "Permanent link")

```
peek_removed() -> int | None
```

Return lowest removed request index

Source code in `vllm/v1/sample/logits_processor/state.py`

```
defpeek_removed(self) -> int | None:
"""Return lowest removed request index"""
    if self.has_removed():
        self._ensure_removed_sorted()
        return self._removed[-1]
    return None
```

### pop\_removed [¶](#vllm.v1.sample.logits_processor.state.BatchUpdateBuilder.pop_removed "Permanent link")

```
pop_removed() -> int | None
```

Pop lowest removed request index

Source code in `vllm/v1/sample/logits_processor/state.py`

```
defpop_removed(self) -> int | None:
"""Pop lowest removed request index"""
    if self.has_removed():
        self._ensure_removed_sorted()
        return self._removed.pop()
    return None
```

### removed\_append [¶](#vllm.v1.sample.logits_processor.state.BatchUpdateBuilder.removed_append "Permanent link")

```
removed_append(index: int) -> None
```

Register the removal of a request from the persistent batch.

Must not be called after the first time self.removed, self.pop\_removed() or self.peek\_removed() are invoked.

Parameters:

Name Type Description Default `index` `int`

request index

*required*

Source code in `vllm/v1/sample/logits_processor/state.py`

```
defremoved_append(self, index: int) -> None:
"""Register the removal of a request from the persistent batch.

    Must not be called after the first time self.removed,
    self.pop_removed() or self.peek_removed() are invoked.

    Args:
      index: request index
    """
    if self._is_removed_sorted:
        raise RuntimeError(
            "Cannot register new removed request after self.removed has been read."
        )
    self._removed.append(index)
    self.batch_changed = True
```

### reset [¶](#vllm.v1.sample.logits_processor.state.BatchUpdateBuilder.reset "Permanent link")

Returns True if there were any changes to the batch.

Source code in `vllm/v1/sample/logits_processor/state.py`

```
defreset(self) -> bool:
"""Returns True if there were any changes to the batch."""
    self._is_removed_sorted = False
    self._removed.clear()
    self.added.clear()
    self.moved.clear()
    batch_changed = self.batch_changed
    self.batch_changed = False
    return batch_changed
```

## LogitsProcessors [¶](#vllm.v1.sample.logits_processor.state.LogitsProcessors "Permanent link")

Encapsulates initialized logitsproc objects.

Source code in `vllm/v1/sample/logits_processor/state.py`

```
classLogitsProcessors:
"""Encapsulates initialized logitsproc objects."""

    def__init__(self, logitsprocs: Iterable["LogitsProcessor"] | None = None) -> None:
        self.argmax_invariant: list[LogitsProcessor] = []
        self.non_argmax_invariant: list[LogitsProcessor] = []
        if logitsprocs:
            for logitproc in logitsprocs:
                (
                    self.argmax_invariant
                    if logitproc.is_argmax_invariant()
                    else self.non_argmax_invariant
                ).append(logitproc)

    @property
    defall(self) -> Iterator["LogitsProcessor"]:
"""Iterator over all logits processors."""
        return chain(self.argmax_invariant, self.non_argmax_invariant)
```

### all `property` [¶](#vllm.v1.sample.logits_processor.state.LogitsProcessors.all "Permanent link")

Iterator over all logits processors.