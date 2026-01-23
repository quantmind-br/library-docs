---
title: CPU Issue Classification & Reproduction | liteLLM
url: https://docs.litellm.ai/docs/troubleshoot/cpu_issues
source: sitemap
fetched_at: 2026-01-21T19:54:57.159848014-03:00
rendered_js: false
word_count: 209
summary: This document provides a framework for identifying, reproducing, and reporting CPU performance issues in LiteLLM, ensuring developers provide the necessary context for technical support.
tags:
    - litellm
    - cpu-usage
    - performance-troubleshooting
    - debugging-guide
    - issue-reporting
    - system-monitoring
category: guide
---

## 1. Classify the CPU Issue[​](#1-classify-the-cpu-issue "Direct link to 1. Classify the CPU Issue")

Select the options that best describes the CPU behavior observed.

- CPU scales with traffic (RPS-driven)
- CPU increases without a traffic increase
- CPU increases after a LiteLLM upgrade

## 2. Can you reproduce the issue?[​](#2-can-you-reproduce-the-issue "Direct link to 2. Can you reproduce the issue?")

Before escalating, verify whether the CPU issue can be reproduced in a test environment that mirrors your production setup.

If reproducible, provide **detailed reproduction steps** along with any relevant requests or configuration used.  
For guidance on the type of information we're looking for, see the [LiteLLM Troubleshooting Guide](https://docs.litellm.ai/docs/troubleshoot).

## 3. Issue Cannot Be Reproduced[​](#3-issue-cannot-be-reproduced "Direct link to 3. Issue Cannot Be Reproduced")

If the CPU issue cannot be reproduced in a test environment that mirrors your production setup, please provide:

1. **Information from Section 1 and 2**
   
   - CPU classification (Section 1)
   - Reproduction attempts and environment details (Section 2)
2. **Additional context** to help investigate:
   
   - **Workload:** A realistic sample of requests processed before and during the spike, including any recent configuration changes.
   - **Metrics:** CPU usage, P50/P99 latency, memory usage. Please include **screenshots** of the metrics whenever possible.
   - **Logs / Alerts:** Any relevant logs or alerts captured **before and during the spike**.

> Providing this information allows the team to analyze patterns, correlate spikes with traffic or configuration, and attempt to reproduce the issue internally. Without it, our engineers won't have enough information to look into the problem.