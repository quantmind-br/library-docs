---
title: Evaluations · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/evaluations/index.md
source: llms
fetched_at: 2026-01-24T15:07:23.260556369-03:00
rendered_js: false
word_count: 168
summary: This document introduces AI Gateway's Evaluations feature, which allows developers to analyze and optimize their AI application's performance, cost, and accuracy using log datasets.
tags:
    - ai-gateway
    - evaluations
    - performance-monitoring
    - cost-optimization
    - data-analysis
    - human-feedback
category: concept
---

Understanding your application's performance is essential for optimization. Developers often have different priorities, and finding the optimal solution involves balancing key factors such as cost, latency, and accuracy. Some prioritize low-latency responses, while others focus on accuracy or cost-efficiency.

AI Gateway's Evaluations provide the data needed to make informed decisions on how to optimize your AI application. Whether it is adjusting the model, provider, or prompt, this feature delivers insights into key metrics around performance, speed, and cost. It empowers developers to better understand their application's behavior, ensuring improved accuracy, reliability, and customer satisfaction.

Evaluations use datasets which are collections of logs stored for analysis. You can create datasets by applying filters in the Logs tab, which help narrow down specific logs for evaluation.

Our first step toward comprehensive AI evaluations starts with human feedback (currently in open beta). We will continue to build and expand AI Gateway with additional evaluators.

[Learn how to set up an evaluation](https://developers.cloudflare.com/ai-gateway/evaluations/set-up-evaluations/) including creating datasets, selecting evaluators, and running the evaluation process.