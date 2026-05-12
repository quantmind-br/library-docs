---
title: kv_events - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/config/kv_events/
source: sitemap
fetched_at: 2026-05-07T21:16:57.98857193-03:00
rendered_js: false
word_count: 169
summary: This document defines the configuration parameters for the KV cache event publishing system, including settings for ZeroMQ endpoints, queue management, and event topic subscription.
tags:
    - kv-cache
    - event-publishing
    - configuration
    - zmq
    - performance-tuning
    - vllm
category: configuration
---

Configuration for KV event publishing.

Source code in `vllm/config/kv_events.py`

```
@config
classKVEventsConfig:
"""Configuration for KV event publishing."""

    enable_kv_cache_events: bool = False
"""If True, enable KV cache events for tracking block storage and removal.
    Events can be published externally by zmq using the event publisher config.
    """

    publisher: Literal["null", "zmq"] = None  # type: ignore[assignment]
"""The publisher to use for publishing kv events. Can be "null", "zmq".
    """

    endpoint: str = "tcp://*:5557"
"""The zmq endpoint to use for publishing kv events.
    """

    replay_endpoint: str | None = None
"""The zmq endpoint to use for replaying kv events.
    """

    buffer_steps: int = 10_000
"""The number of steps to cache for replay endpoint. Will only save
    events from the last N steps for the replay endpoint.
    """

    hwm: int = 100_000
"""The zmq high water mark for the event publisher. After queueing N events,
    events will start dropping if the consumer is not keeping up.
    """

    max_queue_size: int = 100_000
"""The maximum number of events to queue while waiting for publishing.
    """

    topic: str = ""
"""The topic to use for the event publisher. Consumers can subscribe to
    this topic to receive events.
    """

    def__post_init__(self):
        if self.publisher is None:
            self.publisher = "zmq" if self.enable_kv_cache_events else "null"
```

### buffer\_steps `class-attribute` `instance-attribute` [¶](#vllm.config.kv_events.KVEventsConfig.buffer_steps "Permanent link")

```
buffer_steps: int = 10000
```

The number of steps to cache for replay endpoint. Will only save events from the last N steps for the replay endpoint.

### enable\_kv\_cache\_events `class-attribute` `instance-attribute` [¶](#vllm.config.kv_events.KVEventsConfig.enable_kv_cache_events "Permanent link")

```
enable_kv_cache_events: bool = False
```

If True, enable KV cache events for tracking block storage and removal. Events can be published externally by zmq using the event publisher config.

### endpoint `class-attribute` `instance-attribute` [¶](#vllm.config.kv_events.KVEventsConfig.endpoint "Permanent link")

```
endpoint: str = 'tcp://*:5557'
```

The zmq endpoint to use for publishing kv events.

### hwm `class-attribute` `instance-attribute` [¶](#vllm.config.kv_events.KVEventsConfig.hwm "Permanent link")

The zmq high water mark for the event publisher. After queueing N events, events will start dropping if the consumer is not keeping up.

### max\_queue\_size `class-attribute` `instance-attribute` [¶](#vllm.config.kv_events.KVEventsConfig.max_queue_size "Permanent link")

```
max_queue_size: int = 100000
```

The maximum number of events to queue while waiting for publishing.

### publisher `class-attribute` `instance-attribute` [¶](#vllm.config.kv_events.KVEventsConfig.publisher "Permanent link")

```
publisher: Literal['null', 'zmq'] = None
```

The publisher to use for publishing kv events. Can be "null", "zmq".

### replay\_endpoint `class-attribute` `instance-attribute` [¶](#vllm.config.kv_events.KVEventsConfig.replay_endpoint "Permanent link")

```
replay_endpoint: str | None = None
```

The zmq endpoint to use for replaying kv events.

### topic `class-attribute` `instance-attribute` [¶](#vllm.config.kv_events.KVEventsConfig.topic "Permanent link")

The topic to use for the event publisher. Consumers can subscribe to this topic to receive events.