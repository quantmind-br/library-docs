---
title: Benchmarks | liteLLM
url: https://docs.litellm.ai/docs/benchmarks
source: sitemap
fetched_at: 2026-01-21T19:44:10.973725075-03:00
rendered_js: false
word_count: 480
summary: This document provides performance benchmarks for the LiteLLM Proxy Server, offering infrastructure scaling recommendations and comparisons against other tools like Portkey. It details latency metrics, hardware requirements for PostgreSQL and Redis, and methods for measuring proxy overhead during load testing.
tags:
    - litellm-proxy
    - benchmarks
    - performance-metrics
    - infrastructure-scaling
    - api-gateway
    - load-testing
    - redis-optimization
category: reference
---

Benchmarks for LiteLLM Gateway (Proxy Server) tested against a fake OpenAI endpoint.

Use this config for testing:

```
model_list:
-model_name:"fake-openai-endpoint"
litellm_params:
model: openai/any
api_base: https://your-fake-openai-endpoint.com/chat/completions
api_key:"test"
```

### 2 Instance LiteLLM Proxy[​](#2-instance-litellm-proxy "Direct link to 2 Instance LiteLLM Proxy")

In these tests the baseline latency characteristics are measured against a fake-openai-endpoint.

#### Performance Metrics[​](#performance-metrics "Direct link to Performance Metrics")

**Type****Name****Median (ms)****95%ile (ms)****99%ile (ms)****Average (ms)****Current RPS**POST/chat/completions2006301200262.461035.7CustomLiteLLM Overhead Duration (ms)12294314.741035.7Aggregated100430930138.62071.4

### 4 Instances[​](#4-instances "Direct link to 4 Instances")

**Type****Name****Median (ms)****95%ile (ms)****99%ile (ms)****Average (ms)****Current RPS**POST/chat/completions100150240111.731170CustomLiteLLM Overhead Duration (ms)28133.321170Aggregated7713018057.532340

#### Key Findings[​](#key-findings "Direct link to Key Findings")

- Doubling from 2 to 4 LiteLLM instances halves median latency: 200 ms → 100 ms.
- High-percentile latencies drop significantly: P95 630 ms → 150 ms, P99 1,200 ms → 240 ms.
- Setting workers equal to CPU count gives optimal performance.

## Machine Spec used for testing[​](#machine-spec-used-for-testing "Direct link to Machine Spec used for testing")

Each machine deploying LiteLLM had the following specs:

- 4 CPU
- 8GB RAM

## Configuration[​](#configuration "Direct link to Configuration")

- Database: PostgreSQL
- Redis: Not used

## Infrastructure Recommendations[​](#infrastructure-recommendations "Direct link to Infrastructure Recommendations")

Recommended specifications based on benchmark results and industry standards for API gateway deployments.

### PostgreSQL[​](#postgresql "Direct link to PostgreSQL")

Required for authentication, key management, and usage tracking.

WorkloadCPURAMStorageConnections1-2K RPS4-8 cores16GB200GB SSD (3000+ IOPS)100-2002-5K RPS8 cores16-32GB500GB SSD (5000+ IOPS)200-5005K+ RPS16+ cores32-64GB1TB+ SSD (10000+ IOPS)500+

**Configuration:** Set `proxy_batch_write_at: 60` to batch writes and reduce DB load. Total connections = pool limit × instances.

### Redis (Recommended)[​](#redis-recommended "Direct link to Redis (Recommended)")

Redis was not used in these benchmarks but provides significant production benefits: 60-80% reduced DB load.

WorkloadCPURAM1-2K RPS2-4 cores8GB2-5K RPS4 cores16GB5K+ RPS8+ cores32GB+

**Requirements:** Redis 7.0+, AOF persistence enabled, `allkeys-lru` eviction policy.

**Configuration:**

```
router_settings:
redis_host: os.environ/REDIS_HOST
redis_port: os.environ/REDIS_PORT
redis_password: os.environ/REDIS_PASSWORD

litellm_settings:
cache:True
cache_params:
type: redis
host: os.environ/REDIS_HOST
port: os.environ/REDIS_PORT
password: os.environ/REDIS_PASSWORD
```

tip

Use `redis_host`, `redis_port`, and `redis_password` instead of `redis_url` for ~80 RPS better performance.

**Scaling:** DB connections scale linearly with instances. Consider PostgreSQL read replicas beyond 5K RPS.

See [Production Configuration](https://docs.litellm.ai/docs/proxy/prod) for detailed best practices.

## Locust Settings[​](#locust-settings "Direct link to Locust Settings")

- 1000 Users
- 500 user Ramp Up

## How to measure LiteLLM Overhead[​](#how-to-measure-litellm-overhead "Direct link to How to measure LiteLLM Overhead")

All responses from litellm will include the `x-litellm-overhead-duration-ms` header, this is the latency overhead in milliseconds added by LiteLLM Proxy.

If you want to measure this on locust you can use the following code:

Locust Code for measuring LiteLLM Overhead

```
import os
import uuid
from locust import HttpUser, task, between, events

# Custom metric to track LiteLLM overhead duration
overhead_durations =[]

@events.request.add_listener
defon_request(request_type, name, response_time, response_length, response, context, exception, start_time, url,**kwargs):
if response andhasattr(response,'headers'):
        overhead_duration = response.headers.get('x-litellm-overhead-duration-ms')
if overhead_duration:
try:
                duration_ms =float(overhead_duration)
                overhead_durations.append(duration_ms)
# Report as custom metric
                events.request.fire(
                    request_type="Custom",
                    name="LiteLLM Overhead Duration (ms)",
                    response_time=duration_ms,
                    response_length=0,
)
except(ValueError, TypeError):
pass

classMyUser(HttpUser):
    wait_time = between(0.5,1)# Random wait time between requests

defon_start(self):
        self.api_key = os.getenv('API_KEY','sk-1234567890')
        self.client.headers.update({'Authorization':f'Bearer {self.api_key}'})

@task
deflitellm_completion(self):
# no cache hits with this
        payload ={
"model":"db-openai-endpoint",
"messages":[{"role":"user","content":f"{uuid.uuid4()} This is a test there will be no cache hits and we'll fill up the context"*150}],
"user":"my-new-end-user-1"
}
        response = self.client.post("chat/completions", json=payload)

if response.status_code !=200:
# log the errors in error.txt
withopen("error.txt","a")as error_log:
                error_log.write(response.text +"\n")
```

## LiteLLM vs Portkey Performance Comparison[​](#litellm-vs-portkey-performance-comparison "Direct link to LiteLLM vs Portkey Performance Comparison")

**Test Configuration**: 4 CPUs, 8 GB RAM per instance | Load: 1k concurrent users, 500 ramp-up **Versions:** Portkey **v1.14.0** | LiteLLM **v1.79.1-stable**  
**Test Duration:** 5 minutes

### Multi-Instance (4×) Performance[​](#multi-instance-4-performance "Direct link to Multi-Instance (4×) Performance")

MetricPortkey (no DB)LiteLLM (with DB)Comment**Total Requests**293,796312,405LiteLLM higher**Failed Requests**00Same**Median Latency**100 ms100 msSame**p95 Latency**230 ms150 msLiteLLM lower**p99 Latency**500 ms240 msLiteLLM lower**Average Latency**123 ms111 msLiteLLM lower**Current RPS**1,170.91,170Same

*Lower is better for latency metrics; higher is better for requests and RPS.*

### Technical Insights[​](#technical-insights "Direct link to Technical Insights")

**Portkey**

**Pros**

- Low memory footprint
- Stable latency with minimal spikes

**Cons**

- CPU utilization capped around ~40%, indicating underutilization of available compute resources
- Experienced three I/O timeout outages

**LiteLLM**

**Pros**

- Fully utilizes available CPU capacity
- Strong connection handling and low latency after initial warm-up spikes

**Cons**

- High memory usage during initialization and per request

## Logging Callbacks[​](#logging-callbacks "Direct link to Logging Callbacks")

### [GCS Bucket Logging](https://docs.litellm.ai/docs/observability/gcs_bucket_integration)[​](#gcs-bucket-logging "Direct link to gcs-bucket-logging")

Using GCS Bucket has **no impact on latency, RPS compared to Basic Litellm Proxy**

MetricBasic Litellm ProxyLiteLLM Proxy with GCS Bucket LoggingRPS1133.21137.3Median Latency (ms)140138

### [LangSmith logging](https://docs.litellm.ai/docs/proxy/logging)[​](#langsmith-logging "Direct link to langsmith-logging")

Using LangSmith has **no impact on latency, RPS compared to Basic Litellm Proxy**

MetricBasic Litellm ProxyLiteLLM Proxy with LangSmithRPS1133.21135Median Latency (ms)140132