---
title: Adaptive Load Balancing
url: https://docs.getbifrost.ai/enterprise/adaptive-load-balancing.md
source: llms
fetched_at: 2026-01-21T19:43:19.232901329-03:00
rendered_js: false
word_count: 686
summary: This document explains the technical implementation of adaptive load balancing, detailing how real-time metrics like error rates and latency are used to dynamically optimize traffic distribution across providers and keys.
tags:
    - load-balancing
    - traffic-management
    - performance-optimization
    - health-monitoring
    - circuit-breaker
    - adaptive-routing
category: concept
---

# Adaptive Load Balancing

> Advanced load balancing algorithms with predictive scaling, health monitoring, and performance optimization for enterprise-grade traffic distribution.

<Info>
  **Looking for comprehensive provider routing documentation?**

  For a detailed guide covering how adaptive load balancing works with governance routing, the two-level architecture (provider + key selection), Model Catalog integration, and example scenarios, see the [**Provider Routing Guide**](/providers/provider-routing).

  This page focuses on the technical implementation and performance characteristics of adaptive load balancing.
</Info>

## Overview

**Adaptive Load Balancing** in Bifrost Enterprise automatically optimizes traffic distribution across providers and keys based on real-time performance metrics. The system operates at **two levels** - provider selection (direction) and key selection (route) - continuously monitoring error rates, latency, and throughput to dynamically adjust weights, ensuring optimal performance and reliability.

### Key Features

| Feature                              | Description                                                                    |
| ------------------------------------ | ------------------------------------------------------------------------------ |
| **Dynamic Weight Adjustment**        | Automatically adjusts key weights based on performance metrics                 |
| **Real-time Performance Monitoring** | Tracks error rates, latency, and success rates per model-key combination       |
| **Cross-Node Synchronization**       | Gossip protocol ensures consistent weight information across all cluster nodes |
| **Circuit Breaker Integration**      | Temporarily removes poorly performing keys from rotation                       |
| **Fast Recovery**                    | Momentum-based scoring helps routes recover quickly after transient failures   |

<Tip>
  **Zero-overhead design**: All route selection logic adds less than **10 microseconds** to hot path latency. Weight calculations happen asynchronously every 5 seconds, so request routing uses pre-computed weights with minimal overhead.
</Tip>

***

## Architecture

The load balancing system operates at two levels:

* **Direction-level** (provider + model): Decides which provider to use for a given model
* **Route-level** (provider + model + key): Decides which API key to use within a provider

This two-tier approach enables both macro-level provider selection and micro-level key optimization.

```mermaid  theme={null}
graph TB
    Request["Incoming Request<br/>model: gpt-4"]

    subgraph DirectionSelection["Direction Selection"]
        DS["Provider Selector<br/>Score-based selection"]
        DP1["OpenAI<br/>score: 0.92"]
        DP2["Azure<br/>score: 0.85"]
        DP3["Anthropic<br/>score: 0.78"]
    end

    subgraph RouteSelection["Route Selection"]
        RS["Key Selector<br/>Weighted random"]
        K1["Key 1<br/>weight: 850"]
        K2["Key 2<br/>weight: 620"]
        K3["Key 3<br/>weight: 45"]
    end

    subgraph Tracker["Metrics Tracker"]
        T["Real-time Metrics<br/>5-second recomputation"]
        M1["Error Rate"]
        M2["Latency Score"]
        M3["Utilization"]
    end

    Request --> DS
    DS --> DP1 & DP2 & DP3
    DP1 --> RS
    RS --> K1 & K2 & K3
    K1 --> Response["API Response"]
    Response --> T
    T --> M1 & M2 & M3
    M1 & M2 & M3 -.->|"Update Weights"| DS & RS
```

***

## How Weight Calculation Works

Every 5 seconds, the system recalculates weights for all routes based on four factors:

| Factor                | Weight   | Purpose                                         |
| --------------------- | -------- | ----------------------------------------------- |
| **Error Penalty**     | 50%      | Penalizes routes with high error rates          |
| **Latency Score**     | 20%      | Penalizes routes with abnormally slow responses |
| **Utilization Score** | 5%       | Prevents overloading high-performing routes     |
| **Momentum Bias**     | Additive | Rewards routes that are recovering well         |

The system combines these into a single score, then converts it to a weight between 1 and 1000. Lower penalties mean higher weights, which means more traffic.

$$
Score = (P_{error} \times 0.5) + (P_{latency} \times 0.2) + (P_{util} \times 0.05) - M_{momentum}
$$

$$
Weight = W_{min} + (1 - Score) \times (W_{max} - W_{min})
$$

```mermaid  theme={null}
flowchart LR
    subgraph Inputs["Raw Metrics"]
        E["Error Rate"]
        L["Latency"]
        U["Utilization"]
        M["Momentum"]
    end

    subgraph Scoring["Score Computation"]
        EP["Error Penalty<br/>50% weight"]
        LP["Latency Score<br/>20% weight"]
        US["Utilization Score<br/>5% weight"]
        MS["Momentum Bias"]
    end

    subgraph Output["Final Weight"]
        NS["Normalized Score"]
        FW["Route Weight<br/>1 - 1000"]
    end

    E --> EP
    L --> LP
    U --> US
    M --> MS
    EP & LP & US --> NS
    MS --> NS
    NS --> FW
```

***

## Key Capabilities

1. **Automatic Route Health Management**: Routes automatically transition between 4 states (Healthy, Degraded, Failed, Recovering) based on error rates and latency. No manual intervention required when a route fails or recovers.

2. **Fair Traffic Distribution**: The system prevents any single route from being overloaded while still favoring better performers. Low-weight routes always get minimum traffic to prove recovery.

3. **Real-time Dashboard**: Provides visibility into weight distribution, performance metrics (error rates, latency), state transitions, and actual vs expected traffic per route.

<Frame>
  <img src="https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-load-balancing.png?fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=ebca4e200b7528b855dd931d673dca5c" alt="Adaptive Load Balancing Dashboard" data-og-width="3492" width="3492" data-og-height="2358" height="2358" data-path="media/ui-load-balancing.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-load-balancing.png?w=280&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=d1206292f0afb18b47602c519d6667ea 280w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-load-balancing.png?w=560&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=4e98ab4f7aedba288c275a0b84a51d2c 560w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-load-balancing.png?w=840&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=3c25fae863ff8a7633519c6e11c05eb0 840w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-load-balancing.png?w=1100&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=97ba36be0e339b42e2fdf539c61f55b4 1100w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-load-balancing.png?w=1650&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=a2a650fa3a301eb1d4d65a04bdf3edb6 1650w, https://mintcdn.com/bifrost/_ilYf7u7HJP58LQG/media/ui-load-balancing.png?w=2500&fit=max&auto=format&n=_ilYf7u7HJP58LQG&q=85&s=538656bf13dd862b2be43e34b8707098 2500w" />
</Frame>

4. **Multi-Factor Scoring**: Routes are scored using 4 components - Error Penalty (50% weight, time-decayed), Latency Score (token-aware via MV-TACOS algorithm), Utilization Score (fair-share balancing), and Momentum (accelerates recovery after failures).

5. **Smart Key Selection**: Uses weighted random selection with jitter (5% band) and 25% exploration probability to probe potentially recovered routes, rather than always picking the best route.

6. **Performance Thresholds**: Specific triggers drive state transitions —> 2% error rate triggers Degraded, >5% error rate or TPM hit triggers Failed, \<2% error with 50%+ expected traffic triggers Healthy.

<Tip>
  The system is designed to be self-healing: it penalizes failing routes quickly, but also enables fast recovery (90% penalty reduction in 30 seconds) once issues are fixed.
</Tip>

***

## Next Steps

<Steps>
  <Step title="Enable Adaptive Load Balancing">
    Contact your Bifrost Enterprise representative to enable adaptive load balancing for your deployment
  </Step>

  <Step title="Monitor Weight Distribution">
    Use the dashboard to observe how weights adapt to real traffic patterns
  </Step>

  <Step title="Analyze Performance">
    Review route state transitions and weight adjustments to understand system behavior
  </Step>
</Steps>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt