---
title: request_queue - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/core/sched/request_queue/
source: sitemap
fetched_at: 2026-05-07T21:40:25.433777226-03:00
rendered_js: false
word_count: 815
summary: This document provides the API reference for request queue implementations, including first-come-first-served and priority-based queuing mechanisms used for task scheduling.
tags:
    - api-reference
    - request-queue
    - scheduling
    - vllm
    - python-classes
category: api
---

## FCFSRequestQueue [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue "Permanent link")

Bases: `deque[Request]`, `RequestQueue`

A first-come-first-served queue that supports deque operations.

Source code in `vllm/v1/core/sched/request_queue.py`

```
classFCFSRequestQueue(deque[Request], RequestQueue):
"""A first-come-first-served queue that supports deque operations."""

    defadd_request(self, request: Request) -> None:
"""Add a request to the queue according to FCFS policy."""
        self.append(request)

    defpop_request(self) -> Request:
"""Pop a request from the queue according to FCFS policy."""
        return self.popleft()

    defpeek_request(self) -> Request:
"""Peek at the next request in the queue without removing it."""
        if not self:
            raise IndexError("peek from an empty queue")
        return self[0]

    defprepend_request(self, request: Request) -> None:
"""Prepend a request to the front of the queue."""
        self.appendleft(request)

    defprepend_requests(self, requests: RequestQueue) -> None:
"""Prepend all requests from another queue to the front of this
        queue.

        Note: The requests will be prepended in reverse order of their
        appearance in the `requests` queue.
        """
        self.extendleft(requests)

    defremove_request(self, request: Request) -> None:
"""Remove a specific request from the queue."""
        self.remove(request)

    defremove_requests(self, requests: Iterable[Request]) -> None:
"""Remove multiple specific requests from the queue."""
        requests_to_remove = set(requests)
        filtered_requests = [req for req in self if req not in requests_to_remove]
        # deque does not support in-place filtering, so we need to clear
        # and extend
        self.clear()
        self.extend(filtered_requests)

    def__bool__(self) -> bool:
"""Check if queue has any requests."""
        return len(self) > 0

    def__len__(self) -> int:
"""Get number of requests in queue."""
        return super().__len__()

    def__iter__(self) -> Iterator[Request]:
"""Iterate over the queue according to FCFS policy."""
        return super().__iter__()
```

### \_\_bool\__ [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue.__bool__ "Permanent link")

Check if queue has any requests.

Source code in `vllm/v1/core/sched/request_queue.py`

```
def__bool__(self) -> bool:
"""Check if queue has any requests."""
    return len(self) > 0
```

### \_\_iter\__ [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue.__iter__ "Permanent link")

Iterate over the queue according to FCFS policy.

Source code in `vllm/v1/core/sched/request_queue.py`

```
def__iter__(self) -> Iterator[Request]:
"""Iterate over the queue according to FCFS policy."""
    return super().__iter__()
```

### \_\_len\__ [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue.__len__ "Permanent link")

Get number of requests in queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
def__len__(self) -> int:
"""Get number of requests in queue."""
    return super().__len__()
```

### add\_request [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue.add_request "Permanent link")

```
add_request(request: Request) -> None
```

Add a request to the queue according to FCFS policy.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defadd_request(self, request: Request) -> None:
"""Add a request to the queue according to FCFS policy."""
    self.append(request)
```

### peek\_request [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue.peek_request "Permanent link")

Peek at the next request in the queue without removing it.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defpeek_request(self) -> Request:
"""Peek at the next request in the queue without removing it."""
    if not self:
        raise IndexError("peek from an empty queue")
    return self[0]
```

### pop\_request [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue.pop_request "Permanent link")

Pop a request from the queue according to FCFS policy.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defpop_request(self) -> Request:
"""Pop a request from the queue according to FCFS policy."""
    return self.popleft()
```

### prepend\_request [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue.prepend_request "Permanent link")

```
prepend_request(request: Request) -> None
```

Prepend a request to the front of the queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defprepend_request(self, request: Request) -> None:
"""Prepend a request to the front of the queue."""
    self.appendleft(request)
```

### prepend\_requests [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue.prepend_requests "Permanent link")

```
prepend_requests(requests: RequestQueue) -> None
```

Prepend all requests from another queue to the front of this queue.

Note: The requests will be prepended in reverse order of their appearance in the `requests` queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defprepend_requests(self, requests: RequestQueue) -> None:
"""Prepend all requests from another queue to the front of this
    queue.

    Note: The requests will be prepended in reverse order of their
    appearance in the `requests` queue.
    """
    self.extendleft(requests)
```

### remove\_request [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue.remove_request "Permanent link")

```
remove_request(request: Request) -> None
```

Remove a specific request from the queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defremove_request(self, request: Request) -> None:
"""Remove a specific request from the queue."""
    self.remove(request)
```

### remove\_requests [¶](#vllm.v1.core.sched.request_queue.FCFSRequestQueue.remove_requests "Permanent link")

Remove multiple specific requests from the queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defremove_requests(self, requests: Iterable[Request]) -> None:
"""Remove multiple specific requests from the queue."""
    requests_to_remove = set(requests)
    filtered_requests = [req for req in self if req not in requests_to_remove]
    # deque does not support in-place filtering, so we need to clear
    # and extend
    self.clear()
    self.extend(filtered_requests)
```

## PriorityRequestQueue [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue "Permanent link")

Bases: `RequestQueue`

A priority queue that supports heap operations.

Respects the ordering defined in the Request class, where requests with a smaller value of `priority` are processed first. If multiple requests have the same priority, the one with the earlier `arrival_time` is processed first.

Source code in `vllm/v1/core/sched/request_queue.py`

```
classPriorityRequestQueue(RequestQueue):
"""
    A priority queue that supports heap operations.

    Respects the ordering defined in the Request class, where
    requests with a smaller value of `priority` are processed first.
    If multiple requests have the same priority, the one with the earlier
    `arrival_time` is processed first.
    """

    def__init__(self) -> None:
        self._heap: list[Request] = []

    defadd_request(self, request: Request) -> None:
"""Add a request to the queue according to priority policy."""
        heapq.heappush(self._heap, request)

    defpop_request(self) -> Request:
"""Pop a request from the queue according to priority policy."""
        if not self._heap:
            raise IndexError("pop from empty heap")
        return heapq.heappop(self._heap)

    defpeek_request(self) -> Request:
"""Peek at the next request in the queue without removing it."""
        if not self._heap:
            raise IndexError("peek from empty heap")
        return self._heap[0]

    defprepend_request(self, request: Request) -> None:
"""Add a request to the queue according to priority policy.

        Note: In a priority queue, there is no concept of prepending to the
        front. Requests are ordered by (priority, arrival_time)."""
        self.add_request(request)

    defprepend_requests(self, requests: RequestQueue) -> None:
"""Add all requests from another queue according to priority policy.

        Note: In a priority queue, there is no concept of prepending to the
        front. Requests are ordered by (priority, arrival_time)."""
        for request in requests:
            self.add_request(request)

    defremove_request(self, request: Request) -> None:
"""Remove a specific request from the queue."""
        self._heap.remove(request)
        heapq.heapify(self._heap)

    defremove_requests(self, requests: Iterable[Request]) -> None:
"""Remove multiple specific requests from the queue."""
        requests_to_remove = requests if isinstance(requests, set) else set(requests)
        self._heap = [r for r in self._heap if r not in requests_to_remove]
        heapq.heapify(self._heap)

    def__bool__(self) -> bool:
"""Check if queue has any requests."""
        return bool(self._heap)

    def__len__(self) -> int:
"""Get number of requests in queue."""
        return len(self._heap)

    def__iter__(self) -> Iterator[Request]:
"""Iterate over the queue according to priority policy."""
        heap_copy = self._heap[:]
        while heap_copy:
            yield heapq.heappop(heap_copy)
```

### \_\_bool\__ [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue.__bool__ "Permanent link")

Check if queue has any requests.

Source code in `vllm/v1/core/sched/request_queue.py`

```
def__bool__(self) -> bool:
"""Check if queue has any requests."""
    return bool(self._heap)
```

### \_\_iter\__ [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue.__iter__ "Permanent link")

Iterate over the queue according to priority policy.

Source code in `vllm/v1/core/sched/request_queue.py`

```
def__iter__(self) -> Iterator[Request]:
"""Iterate over the queue according to priority policy."""
    heap_copy = self._heap[:]
    while heap_copy:
        yield heapq.heappop(heap_copy)
```

### \_\_len\__ [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue.__len__ "Permanent link")

Get number of requests in queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
def__len__(self) -> int:
"""Get number of requests in queue."""
    return len(self._heap)
```

### add\_request [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue.add_request "Permanent link")

```
add_request(request: Request) -> None
```

Add a request to the queue according to priority policy.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defadd_request(self, request: Request) -> None:
"""Add a request to the queue according to priority policy."""
    heapq.heappush(self._heap, request)
```

### peek\_request [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue.peek_request "Permanent link")

Peek at the next request in the queue without removing it.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defpeek_request(self) -> Request:
"""Peek at the next request in the queue without removing it."""
    if not self._heap:
        raise IndexError("peek from empty heap")
    return self._heap[0]
```

### pop\_request [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue.pop_request "Permanent link")

Pop a request from the queue according to priority policy.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defpop_request(self) -> Request:
"""Pop a request from the queue according to priority policy."""
    if not self._heap:
        raise IndexError("pop from empty heap")
    return heapq.heappop(self._heap)
```

### prepend\_request [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue.prepend_request "Permanent link")

```
prepend_request(request: Request) -> None
```

Add a request to the queue according to priority policy.

Note: In a priority queue, there is no concept of prepending to the front. Requests are ordered by (priority, arrival\_time).

Source code in `vllm/v1/core/sched/request_queue.py`

```
defprepend_request(self, request: Request) -> None:
"""Add a request to the queue according to priority policy.

    Note: In a priority queue, there is no concept of prepending to the
    front. Requests are ordered by (priority, arrival_time)."""
    self.add_request(request)
```

### prepend\_requests [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue.prepend_requests "Permanent link")

```
prepend_requests(requests: RequestQueue) -> None
```

Add all requests from another queue according to priority policy.

Note: In a priority queue, there is no concept of prepending to the front. Requests are ordered by (priority, arrival\_time).

Source code in `vllm/v1/core/sched/request_queue.py`

```
defprepend_requests(self, requests: RequestQueue) -> None:
"""Add all requests from another queue according to priority policy.

    Note: In a priority queue, there is no concept of prepending to the
    front. Requests are ordered by (priority, arrival_time)."""
    for request in requests:
        self.add_request(request)
```

### remove\_request [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue.remove_request "Permanent link")

```
remove_request(request: Request) -> None
```

Remove a specific request from the queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defremove_request(self, request: Request) -> None:
"""Remove a specific request from the queue."""
    self._heap.remove(request)
    heapq.heapify(self._heap)
```

### remove\_requests [¶](#vllm.v1.core.sched.request_queue.PriorityRequestQueue.remove_requests "Permanent link")

Remove multiple specific requests from the queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defremove_requests(self, requests: Iterable[Request]) -> None:
"""Remove multiple specific requests from the queue."""
    requests_to_remove = requests if isinstance(requests, set) else set(requests)
    self._heap = [r for r in self._heap if r not in requests_to_remove]
    heapq.heapify(self._heap)
```

## RequestQueue [¶](#vllm.v1.core.sched.request_queue.RequestQueue "Permanent link")

Bases: `ABC`

Abstract base class for request queues.

Source code in `vllm/v1/core/sched/request_queue.py`

```
classRequestQueue(ABC):
"""Abstract base class for request queues."""

    @abstractmethod
    defadd_request(self, request: Request) -> None:
"""Add a request to the queue according to the policy."""
        pass

    @abstractmethod
    defpop_request(self) -> Request:
"""Pop a request from the queue according to the policy."""
        pass

    @abstractmethod
    defpeek_request(self) -> Request:
"""Peek at the request at the front of the queue without removing it."""
        pass

    @abstractmethod
    defprepend_request(self, request: Request) -> None:
"""Prepend a request to the front of the queue."""
        pass

    @abstractmethod
    defprepend_requests(self, requests: "RequestQueue") -> None:
"""Prepend all requests from another queue to the front of this
        queue."""
        pass

    @abstractmethod
    defremove_request(self, request: Request) -> None:
"""Remove a specific request from the queue."""
        pass

    @abstractmethod
    defremove_requests(self, requests: Iterable[Request]) -> None:
"""Remove multiple specific requests from the queue."""
        pass

    @abstractmethod
    def__bool__(self) -> bool:
"""Check if queue has any requests."""
        pass

    @abstractmethod
    def__len__(self) -> int:
"""Get number of requests in queue."""
        pass

    @abstractmethod
    def__iter__(self) -> Iterator[Request]:
"""Iterate over the queue according to the policy."""
        pass
```

### \_\_bool\__ `abstractmethod` [¶](#vllm.v1.core.sched.request_queue.RequestQueue.__bool__ "Permanent link")

Check if queue has any requests.

Source code in `vllm/v1/core/sched/request_queue.py`

```
@abstractmethod
def__bool__(self) -> bool:
"""Check if queue has any requests."""
    pass
```

### \_\_iter\__ `abstractmethod` [¶](#vllm.v1.core.sched.request_queue.RequestQueue.__iter__ "Permanent link")

Iterate over the queue according to the policy.

Source code in `vllm/v1/core/sched/request_queue.py`

```
@abstractmethod
def__iter__(self) -> Iterator[Request]:
"""Iterate over the queue according to the policy."""
    pass
```

### \_\_len\__ `abstractmethod` [¶](#vllm.v1.core.sched.request_queue.RequestQueue.__len__ "Permanent link")

Get number of requests in queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
@abstractmethod
def__len__(self) -> int:
"""Get number of requests in queue."""
    pass
```

### add\_request `abstractmethod` [¶](#vllm.v1.core.sched.request_queue.RequestQueue.add_request "Permanent link")

```
add_request(request: Request) -> None
```

Add a request to the queue according to the policy.

Source code in `vllm/v1/core/sched/request_queue.py`

```
@abstractmethod
defadd_request(self, request: Request) -> None:
"""Add a request to the queue according to the policy."""
    pass
```

### peek\_request `abstractmethod` [¶](#vllm.v1.core.sched.request_queue.RequestQueue.peek_request "Permanent link")

Peek at the request at the front of the queue without removing it.

Source code in `vllm/v1/core/sched/request_queue.py`

```
@abstractmethod
defpeek_request(self) -> Request:
"""Peek at the request at the front of the queue without removing it."""
    pass
```

### pop\_request `abstractmethod` [¶](#vllm.v1.core.sched.request_queue.RequestQueue.pop_request "Permanent link")

Pop a request from the queue according to the policy.

Source code in `vllm/v1/core/sched/request_queue.py`

```
@abstractmethod
defpop_request(self) -> Request:
"""Pop a request from the queue according to the policy."""
    pass
```

### prepend\_request `abstractmethod` [¶](#vllm.v1.core.sched.request_queue.RequestQueue.prepend_request "Permanent link")

```
prepend_request(request: Request) -> None
```

Prepend a request to the front of the queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
@abstractmethod
defprepend_request(self, request: Request) -> None:
"""Prepend a request to the front of the queue."""
    pass
```

### prepend\_requests `abstractmethod` [¶](#vllm.v1.core.sched.request_queue.RequestQueue.prepend_requests "Permanent link")

```
prepend_requests(requests: RequestQueue) -> None
```

Prepend all requests from another queue to the front of this queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
@abstractmethod
defprepend_requests(self, requests: "RequestQueue") -> None:
"""Prepend all requests from another queue to the front of this
    queue."""
    pass
```

### remove\_request `abstractmethod` [¶](#vllm.v1.core.sched.request_queue.RequestQueue.remove_request "Permanent link")

```
remove_request(request: Request) -> None
```

Remove a specific request from the queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
@abstractmethod
defremove_request(self, request: Request) -> None:
"""Remove a specific request from the queue."""
    pass
```

### remove\_requests `abstractmethod` [¶](#vllm.v1.core.sched.request_queue.RequestQueue.remove_requests "Permanent link")

Remove multiple specific requests from the queue.

Source code in `vllm/v1/core/sched/request_queue.py`

```
@abstractmethod
defremove_requests(self, requests: Iterable[Request]) -> None:
"""Remove multiple specific requests from the queue."""
    pass
```

## SchedulingPolicy [¶](#vllm.v1.core.sched.request_queue.SchedulingPolicy "Permanent link")

Bases: `Enum`

Enum for scheduling policies.

Source code in `vllm/v1/core/sched/request_queue.py`

```
classSchedulingPolicy(Enum):
"""Enum for scheduling policies."""

    FCFS = "fcfs"
    PRIORITY = "priority"
```

## create\_request\_queue [¶](#vllm.v1.core.sched.request_queue.create_request_queue "Permanent link")

```
create_request_queue(
    policy: SchedulingPolicy,
) -> RequestQueue
```

Create request queue based on scheduling policy.

Source code in `vllm/v1/core/sched/request_queue.py`

```
defcreate_request_queue(policy: SchedulingPolicy) -> RequestQueue:
"""Create request queue based on scheduling policy."""
    if policy == SchedulingPolicy.PRIORITY:
        return PriorityRequestQueue()
    elif policy == SchedulingPolicy.FCFS:
        return FCFSRequestQueue()
    else:
        raise ValueError(f"Unknown scheduling policy: {policy}")
```