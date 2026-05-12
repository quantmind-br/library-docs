---
title: eplb - vLLM
url: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/
source: sitemap
fetched_at: 2026-05-07T21:17:54.668647193-03:00
rendered_js: false
word_count: 50
summary: This document provides an overview of the modules composing the Expert Parallelism Load Balancer (EPLB) system, including its communication, state management, and rebalancing utilities.
tags:
    - expert-parallelism
    - load-balancer
    - distributed-systems
    - system-architecture
    - eplb
category: reference
---

Expert parallelism load balancer (EPLB).

Modules:

Name Description `async_worker`

The async worker that transfers experts in the background.

`eplb_communicator`

EPLB communicator implementations and factory.

`eplb_state`

Expert parallelism load balancer (EPLB) metrics and states.

`eplb_utils`

Utility functions for EPLB (Expert Parallel Load Balancing).

`policy` `rebalance_execute`

The actual execution of the rearrangement.