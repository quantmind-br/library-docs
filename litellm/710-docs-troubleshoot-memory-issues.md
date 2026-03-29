---
title: Memory Issue Classification & Reproduction | liteLLM
url: https://docs.litellm.ai/docs/troubleshoot/memory_issues
source: sitemap
fetched_at: 2026-01-21T19:54:57.579784046-03:00
rendered_js: false
word_count: 245
summary: This document outlines a structured approach for identifying, reproducing, and reporting memory issues such as leaks and OOM events in LiteLLM.
tags:
    - litellm
    - memory-management
    - troubleshooting
    - oom-events
    - debugging
    - performance-monitoring
category: guide
---

## 1. Classify the Memory Issue[​](#1-classify-the-memory-issue "Direct link to 1. Classify the Memory Issue")

Select the option(s) that best describe the memory behavior observed:

- Memory scales with traffic (RPS-driven)
- Memory increases without a traffic increase
- Memory increases after a LiteLLM upgrade
- Memory leak (memory continuously grows over time)
- Out of Memory (OOM) events or pod restarts

* * *

## 2. Can you reproduce the issue?[​](#2-can-you-reproduce-the-issue "Direct link to 2. Can you reproduce the issue?")

Before escalating, verify whether the memory or OOM issue can be reproduced in a test environment that mirrors your production deployment.

If reproducible, provide **detailed reproduction steps** along with any relevant requests, workloads, or configuration used.  
For guidance on the type of information we’re looking for, see the [LiteLLM Troubleshooting Guide](https://docs.litellm.ai/docs/troubleshoot).

* * *

## 3. Issue Cannot Be Reproduced[​](#3-issue-cannot-be-reproduced "Direct link to 3. Issue Cannot Be Reproduced")

If the memory or OOM issue cannot be reproduced in a test environment that mirrors production, please provide:

1. **Information from Sections 1 and 2**
   
   - Memory/issue classification (Section 1)
   - Reproduction attempts and environment details (Section 2)
2. **Additional context** to help investigate:
   
   - **Workload:** A realistic sample of requests processed before and during the spike, including any recent configuration changes.
   - **Metrics:** Memory usage, CPU usage, P50/P99 latency, and any pod restarts or OOM events. Please include **screenshots** of the metrics whenever possible.
   - **Logs / Alerts:** Any relevant logs or alerts captured **before and during the spike**, including OOM errors or stack traces if available.

> Providing this information allows the team to analyze patterns, correlate memory spikes or OOMs with traffic or configuration, and attempt to reproduce the issue internally. Without it, our engineers will not have enough information to investigate the problem.