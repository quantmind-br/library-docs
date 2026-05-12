---
title: metrics - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/metrics/
source: sitemap
fetched_at: 2026-05-07T21:18:29.036157449-03:00
rendered_js: false
word_count: 263
summary: This document describes the classes and methods used for collecting, aggregating, and exporting KV transfer metrics, including support for logging and Prometheus integration.
tags:
    - kv-transfer
    - metrics
    - prometheus
    - logging
    - telemetry
    - distributed-systems
category: api
---

## KVConnectorLogging [¶](#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorLogging "Permanent link")

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`

```
classKVConnectorLogging:
    def__init__(self, kv_transfer_config: KVTransferConfig | None):
        # Instantiate the connector's stats class.
        if kv_transfer_config and kv_transfer_config.kv_connector:
            self.connector_cls = KVConnectorFactory.get_connector_class(
                kv_transfer_config
            )
        self.reset()

    defreset(self):
        self.transfer_stats_accumulator: KVConnectorStats | None = None

    defobserve(self, transfer_stats_data: dict[str, Any]):
        # Should not be called when a KVConnector is not configured.
        assert self.connector_cls is not None
        # Called periodically when connector syncs with the scheduler.
        # Note that this is not the same as the logging interval.
        # We expect transfer_stats_data to be aggregated across all workers and
        # consist of observations from a single connector or a MultiConnector.
        transfer_stats = self.connector_cls.build_kv_connector_stats(
            transfer_stats_data
        )
        if transfer_stats is None:
            logger.warning_once(
                "The connector %s is collecting stats but "
                "does not implement the "
                "`build_kv_connector_stats` method. "
                "Stats will not be logged.",
                self.connector_cls,
            )
            return

        if self.transfer_stats_accumulator is None:
            self.transfer_stats_accumulator = transfer_stats
        else:
            # Accumulate last interval stats.
            self.transfer_stats_accumulator = self.transfer_stats_accumulator.aggregate(
                transfer_stats
            )

    deflog(self, log_fn=logger.info):
"""Log transfer metrics periodically, similar to throughput logging"""
        if (
            self.transfer_stats_accumulator
            and not self.transfer_stats_accumulator.is_empty()
        ):
            # Produce a single cumulative stats object for the last time
            # interval from the recorded observations.
            xfer_metrics = self.transfer_stats_accumulator.reduce()
            xfer_metrics_str = ", ".join(f"{k}={v}" for k, v in xfer_metrics.items())
            log_fn("KV Transfer metrics: %s", xfer_metrics_str)

            # Reset metrics for next interval
            self.reset()
```

### log [¶](#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorLogging.log "Permanent link")

Log transfer metrics periodically, similar to throughput logging

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`

```
deflog(self, log_fn=logger.info):
"""Log transfer metrics periodically, similar to throughput logging"""
    if (
        self.transfer_stats_accumulator
        and not self.transfer_stats_accumulator.is_empty()
    ):
        # Produce a single cumulative stats object for the last time
        # interval from the recorded observations.
        xfer_metrics = self.transfer_stats_accumulator.reduce()
        xfer_metrics_str = ", ".join(f"{k}={v}" for k, v in xfer_metrics.items())
        log_fn("KV Transfer metrics: %s", xfer_metrics_str)

        # Reset metrics for next interval
        self.reset()
```

## KVConnectorProm [¶](#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorProm "Permanent link")

Support for registering per-connector Prometheus metrics, and recording transfer statistics to those metrics. Uses KVConnectorBase.build\_prom\_metrics().

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`

```
classKVConnectorProm:
"""
    Support for registering per-connector Prometheus metrics, and
    recording transfer statistics to those metrics. Uses
    KVConnectorBase.build_prom_metrics().
    """

    _gauge_cls = Gauge
    _counter_cls = Counter
    _histogram_cls = Histogram

    def__init__(
        self,
        vllm_config: VllmConfig,
        labelnames: list[str],
        per_engine_labelvalues: dict[int, list[object]],
    ):
        self.prom_metrics: KVConnectorPromMetrics | None = None
        kv_transfer_config = vllm_config.kv_transfer_config
        if kv_transfer_config and kv_transfer_config.kv_connector:
            connector_cls = KVConnectorFactory.get_connector_class(kv_transfer_config)
            metric_types = {
                Gauge: self._gauge_cls,
                Counter: self._counter_cls,
                Histogram: self._histogram_cls,
            }
            self.prom_metrics = connector_cls.build_prom_metrics(
                vllm_config,
                metric_types,
                labelnames,
                per_engine_labelvalues,
            )

    defobserve(self, transfer_stats_data: dict[str, Any], engine_idx: int = 0):
        if self.prom_metrics is None:
            return
        self.prom_metrics.observe(transfer_stats_data, engine_idx)
```

## KVConnectorPromMetrics [¶](#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorPromMetrics "Permanent link")

A base class for per-connector Prometheus metric registration and recording.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`

```
classKVConnectorPromMetrics:
"""
    A base class for per-connector Prometheus metric registration
    and recording.
    """

    def__init__(
        self,
        vllm_config: VllmConfig,
        metric_types: dict[type[PromMetric], type[PromMetricT]],
        labelnames: list[str],
        per_engine_labelvalues: dict[int, list[object]],
    ):
        self._kv_transfer_config = vllm_config.kv_transfer_config
        self._gauge_cls = metric_types[Gauge]
        self._counter_cls = metric_types[Counter]
        self._histogram_cls = metric_types[Histogram]
        self._labelnames = labelnames
        self.per_engine_labelvalues = per_engine_labelvalues

    defobserve(self, transfer_stats_data: dict[str, Any], engine_idx: int = 0):
"""
        Record the supplied transfer statistics to Prometheus metrics. These
        statistics are engine-specific, and should be recorded to a metric
        with the appropriate 'engine' label. These metric instances can be
        created using the create_metric_per_engine() helper method.
        """
        raise NotImplementedError
```

### observe [¶](#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorPromMetrics.observe "Permanent link")

```
observe(
    transfer_stats_data: dict[str, Any], engine_idx: int = 0
)
```

Record the supplied transfer statistics to Prometheus metrics. These statistics are engine-specific, and should be recorded to a metric with the appropriate 'engine' label. These metric instances can be created using the create\_metric\_per\_engine() helper method.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`

```
defobserve(self, transfer_stats_data: dict[str, Any], engine_idx: int = 0):
"""
    Record the supplied transfer statistics to Prometheus metrics. These
    statistics are engine-specific, and should be recorded to a metric
    with the appropriate 'engine' label. These metric instances can be
    created using the create_metric_per_engine() helper method.
    """
    raise NotImplementedError
```

## KVConnectorStats `dataclass` [¶](#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats "Permanent link")

Base class for KV Connector Stats, a container for transfer performance metrics or otherwise important telemetry from the connector. All sub-classes need to be serializable as stats are sent from worker to logger process.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`

```
@dataclass
classKVConnectorStats:
"""
    Base class for KV Connector Stats, a container for transfer performance
    metrics or otherwise important telemetry from the connector.
    All sub-classes need to be serializable as stats are sent from worker to
    logger process.
    """

    data: dict[str, Any] = field(default_factory=dict)

    defreset(self):
"""Reset the stats, clear the state."""
        raise NotImplementedError

    defaggregate(self, other: "KVConnectorStats") -> "KVConnectorStats":
"""
        Aggregate stats with another `KVConnectorStats` object.
        """
        raise NotImplementedError

    defreduce(self) -> dict[str, int | float]:
"""
        Reduce the observations collected during a time interval to one or
        more representative values (eg avg/median/sum of the series).
        This is meant to be called by the logger to produce a summary of the
        stats for the last time interval.
        """
        raise NotImplementedError

    defis_empty(self) -> bool:
"""Return True if the stats are empty."""
        raise NotImplementedError
```

### aggregate [¶](#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.aggregate "Permanent link")

```
aggregate(other: KVConnectorStats) -> KVConnectorStats
```

Aggregate stats with another `KVConnectorStats` object.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`

```
defaggregate(self, other: "KVConnectorStats") -> "KVConnectorStats":
"""
    Aggregate stats with another `KVConnectorStats` object.
    """
    raise NotImplementedError
```

### is\_empty [¶](#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.is_empty "Permanent link")

Return True if the stats are empty.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`

```
defis_empty(self) -> bool:
"""Return True if the stats are empty."""
    raise NotImplementedError
```

### reduce [¶](#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.reduce "Permanent link")

Reduce the observations collected during a time interval to one or more representative values (eg avg/median/sum of the series). This is meant to be called by the logger to produce a summary of the stats for the last time interval.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`

```
defreduce(self) -> dict[str, int | float]:
"""
    Reduce the observations collected during a time interval to one or
    more representative values (eg avg/median/sum of the series).
    This is meant to be called by the logger to produce a summary of the
    stats for the last time interval.
    """
    raise NotImplementedError
```

### reset [¶](#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.reset "Permanent link")

Reset the stats, clear the state.

Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`

```
defreset(self):
"""Reset the stats, clear the state."""
    raise NotImplementedError
```