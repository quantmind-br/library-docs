---
title: reader - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/v1/metrics/reader/
source: sitemap
fetched_at: 2026-05-07T21:41:14.301809338-03:00
rendered_js: false
word_count: 240
summary: This document defines the data structures for Prometheus-compatible metrics and the API for retrieving in-memory metric snapshots from the vLLM system.
tags:
    - prometheus-metrics
    - data-structures
    - metrics-collection
    - vllm-monitoring
    - python-dataclasses
category: reference
---

## Counter `dataclass` [¶](#vllm.v1.metrics.reader.Counter "Permanent link")

Bases: `Metric`

A monotonically increasing integer counter.

Source code in `vllm/v1/metrics/reader.py`

```
@dataclass
classCounter(Metric):
"""A monotonically increasing integer counter."""

    value: int
```

## Gauge `dataclass` [¶](#vllm.v1.metrics.reader.Gauge "Permanent link")

Bases: `Metric`

A numerical value that can go up or down.

Source code in `vllm/v1/metrics/reader.py`

```
@dataclass
classGauge(Metric):
"""A numerical value that can go up or down."""

    value: float
```

## Histogram `dataclass` [¶](#vllm.v1.metrics.reader.Histogram "Permanent link")

Bases: `Metric`

Observations recorded in configurable buckets.

Buckets are represented by a dictionary. The key is the upper limit of the bucket, and the value is the observed count in that bucket. A '+Inf' key always exists.

The count property is the total count across all buckets, identical to the count of the '+Inf' bucket.

The sum property is the total sum of all observed values.

Source code in `vllm/v1/metrics/reader.py`

```
@dataclass
classHistogram(Metric):
"""Observations recorded in configurable buckets.

    Buckets are represented by a dictionary. The key is
    the upper limit of the bucket, and the value is the
    observed count in that bucket. A '+Inf' key always
    exists.

    The count property is the total count across all
    buckets, identical to the count of the '+Inf' bucket.

    The sum property is the total sum of all observed
    values.
    """

    count: int
    sum: float
    buckets: dict[str, int]
```

## Metric `dataclass` [¶](#vllm.v1.metrics.reader.Metric "Permanent link")

A base class for prometheus metrics.

Each metric may be associated with key=value labels, and in some cases a single vLLM instance may have multiple metrics with the same name but different sets of labels.

Source code in `vllm/v1/metrics/reader.py`

```
@dataclass
classMetric:
"""A base class for prometheus metrics.

    Each metric may be associated with key=value labels, and
    in some cases a single vLLM instance may have multiple
    metrics with the same name but different sets of labels.
    """

    name: str
    labels: dict[str, str]
```

## Vector `dataclass` [¶](#vllm.v1.metrics.reader.Vector "Permanent link")

Bases: `Metric`

An ordered array of integer counters.

This type - which doesn't exist in Prometheus - models one very specific metric, vllm:spec\_decode\_num\_accepted\_tokens\_per\_pos.

Source code in `vllm/v1/metrics/reader.py`

```
@dataclass
classVector(Metric):
"""An ordered array of integer counters.

    This type - which doesn't exist in Prometheus - models one very
    specific metric, vllm:spec_decode_num_accepted_tokens_per_pos.
    """

    values: list[int]
```

## get\_metrics\_snapshot [¶](#vllm.v1.metrics.reader.get_metrics_snapshot "Permanent link")

```
get_metrics_snapshot() -> list[Metric]
```

An API for accessing in-memory Prometheus metrics.

Example

> > > for metric in llm.get\_metrics(): ... if isinstance(metric, Counter): ... print(f"{metric} = {metric.value}") ... elif isinstance(metric, Gauge): ... print(f"{metric} = {metric.value}") ... elif isinstance(metric, Histogram): ... print(f"{metric}") ... print(f" sum = {metric.sum}") ... print(f" count = {metric.count}") ... for bucket\_le, value in metrics.buckets.items(): ... print(f" {bucket\_le} = {value}")

Source code in `vllm/v1/metrics/reader.py`

```
defget_metrics_snapshot() -> list[Metric]:
"""An API for accessing in-memory Prometheus metrics.

    Example:
        >>> for metric in llm.get_metrics():
        ...     if isinstance(metric, Counter):
        ...         print(f"{metric} = {metric.value}")
        ...     elif isinstance(metric, Gauge):
        ...         print(f"{metric} = {metric.value}")
        ...     elif isinstance(metric, Histogram):
        ...         print(f"{metric}")
        ...         print(f"    sum = {metric.sum}")
        ...         print(f"    count = {metric.count}")
        ...         for bucket_le, value in metrics.buckets.items():
        ...             print(f"    {bucket_le} = {value}")
    """
    collected: list[Metric] = []
    for metric in REGISTRY.collect():
        if not metric.name.startswith("vllm:"):
            continue
        if metric.type == "gauge":
            samples = _get_samples(metric)
            for s in samples:
                collected.append(
                    Gauge(name=metric.name, labels=s.labels, value=s.value)
                )
        elif metric.type == "counter":
            samples = _get_samples(metric, "_total")
            if metric.name == "vllm:spec_decode_num_accepted_tokens_per_pos":
                #
                # Ugly vllm:num_accepted_tokens_per_pos special case.
                #
                # This metric is a vector of counters - for each spec
                # decoding token position, we observe the number of
                # accepted tokens using a Counter labeled with 'position'.
                # We convert these into a vector of integer values.
                #
                for labels, values in _digest_num_accepted_by_pos_samples(samples):
                    collected.append(
                        Vector(name=metric.name, labels=labels, values=values)
                    )
            else:
                for s in samples:
                    collected.append(
                        Counter(name=metric.name, labels=s.labels, value=int(s.value))
                    )

        elif metric.type == "histogram":
            #
            # A histogram has a number of '_bucket' samples where
            # the 'le' label represents the upper limit of the bucket.
            # We convert these bucketized values into a dict of values
            # indexed by the value of the 'le' label. The 'le=+Inf'
            # label is a special case, catching all values observed.
            #
            bucket_samples = _get_samples(metric, "_bucket")
            count_samples = _get_samples(metric, "_count")
            sum_samples = _get_samples(metric, "_sum")
            for labels, buckets, count_value, sum_value in _digest_histogram(
                bucket_samples, count_samples, sum_samples
            ):
                collected.append(
                    Histogram(
                        name=metric.name,
                        labels=labels,
                        buckets=buckets,
                        count=count_value,
                        sum=sum_value,
                    )
                )
        else:
            raise AssertionError(f"Unknown metric type {metric.type}")

    return collected
```