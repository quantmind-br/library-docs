---
title: cache - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/utils/cache/
source: sitemap
fetched_at: 2026-05-07T21:38:30.412762648-03:00
rendered_js: false
word_count: 31
summary: This document defines a custom LRU cache implementation that extends standard cache functionality to include item pinning, usage statistics tracking, and granular control over eviction processes.
tags:
    - python
    - lru-cache
    - data-structures
    - memory-management
    - cache-policy
    - object-oriented-programming
category: reference
---

```
classLRUCache(cachetools.LRUCache[_K, _V]):
    def__init__(self, capacity: float, getsizeof: Callable[[_V], float] | None = None):
        super().__init__(capacity, getsizeof)

        self.pinned_items = set[_K]()

        self._hits = 0
        self._total = 0
        self._last_info = CacheInfo(hits=0, total=0)

    def__getitem__(self, key: _K, *, update_info: bool = True) -> _V:
        value = super().__getitem__(key)

        if update_info:
            self._hits += 1
            self._total += 1

        return value

    def__delitem__(self, key: _K) -> None:
        run_on_remove = key in self
        value = self.__getitem__(key, update_info=False)  # type: ignore[call-arg]
        super().__delitem__(key)
        if key in self.pinned_items:
            # Todo: add warning to inform that del pinned item
            self._unpin(key)
        if run_on_remove:
            self._on_remove(key, value)

    @property
    defcache(self) -> Mapping[_K, _V]:
"""Return the internal cache dictionary in order (read-only)."""
        return _MappingOrderCacheView(
            self._Cache__data,  # type: ignore
            self.order,
        )

    @property
    deforder(self) -> Mapping[_K, None]:
"""Return the internal order dictionary (read-only)."""
        return MappingProxyType(self._LRUCache__order)  # type: ignore

    @property
    defcapacity(self) -> float:
        return self.maxsize

    @property
    defusage(self) -> float:
        if self.maxsize == 0:
            return 0

        return self.currsize / self.maxsize

    defstat(self, *, delta: bool = False) -> CacheInfo:
"""
        Gets the cumulative number of hits and queries against this cache.

        If `delta=True`, instead gets these statistics
        since the last call that also passed `delta=True`.
        """
        info = CacheInfo(hits=self._hits, total=self._total)

        if delta:
            info_delta = info - self._last_info
            self._last_info = info
            info = info_delta

        return info

    deftouch(self, key: _K) -> None:
        try:
            self._LRUCache__order.move_to_end(key)  # type: ignore
        except KeyError:
            self._LRUCache__order[key] = None  # type: ignore

    @overload
    defget(self, key: _K, /) -> _V | None: ...

    @overload
    defget(self, key: _K, /, default: _V | _T) -> _V | _T: ...

    defget(self, key: _K, /, default: _V | _T | None = None) -> _V | _T | None:
        value: _V | _T | None
        if key in self:
            value = self.__getitem__(key, update_info=False)  # type: ignore[call-arg]

            self._hits += 1
        else:
            value = default

        self._total += 1
        return value

    @overload
    defpop(self, key: _K) -> _V: ...

    @overload
    defpop(self, key: _K, default: _V | _T) -> _V | _T: ...

    defpop(self, key: _K, default: _V | _T | None = None) -> _V | _T | None:
        value: _V | _T | None
        if key not in self:
            return default

        value = self.__getitem__(key, update_info=False)  # type: ignore[call-arg]
        self.__delitem__(key)
        return value

    defput(self, key: _K, value: _V) -> None:
        self.__setitem__(key, value)

    defpin(self, key: _K) -> None:
"""
        Pins a key in the cache preventing it from being
        evicted in the LRU order.
        """
        if key not in self:
            raise ValueError(f"Cannot pin key: {key} not in cache.")
        self.pinned_items.add(key)

    def_unpin(self, key: _K) -> None:
"""
        Unpins a key in the cache allowing it to be
        evicted in the LRU order.
        """
        self.pinned_items.remove(key)

    def_on_remove(self, key: _K, value: _V | None) -> None:
        pass

    defremove_oldest(self, *, remove_pinned: bool = False) -> None:
        if len(self) == 0:
            return

        self.popitem(remove_pinned=remove_pinned)

    def_remove_old_if_needed(self) -> None:
        while self.currsize > self.capacity:
            self.remove_oldest()

    defpopitem(self, remove_pinned: bool = False):
"""Remove and return the `(key, value)` pair least recently used."""
        if not remove_pinned:
            # pop the oldest item in the cache that is not pinned
            lru_key = next(
                (key for key in self.order if key not in self.pinned_items),
                ALL_PINNED_SENTINEL,
            )
            if lru_key is ALL_PINNED_SENTINEL:
                raise RuntimeError(
                    "All items are pinned, cannot remove oldest from the cache."
                )
        else:
            lru_key = next(iter(self.order))
        value = self.pop(cast(_K, lru_key))
        return (lru_key, value)

    defclear(self) -> None:
        while len(self) > 0:
            self.remove_oldest(remove_pinned=True)

        self._hits = 0
        self._total = 0
        self._last_info = CacheInfo(hits=0, total=0)
```