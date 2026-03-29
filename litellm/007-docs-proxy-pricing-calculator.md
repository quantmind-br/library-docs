---
title: Pricing Calculator (Cost Estimation) | liteLLM
url: https://docs.litellm.ai/docs/proxy/pricing_calculator
source: sitemap
fetched_at: 2026-01-21T19:53:14.79622245-03:00
rendered_js: false
word_count: 205
summary: This document provides a step-by-step walkthrough for using the Pricing Calculator in the LiteLLM UI to forecast model costs based on token usage and request volume.
tags:
    - litellm
    - cost-estimation
    - llm-pricing
    - token-usage
    - budget-planning
    - litellm-dashboard
category: tutorial
---

Estimate LLM costs based on expected token usage and request volume. This tool helps developers and platform teams forecast spending before deploying models to production.

This walkthrough shows how to estimate LLM costs using the Pricing Calculator in the LiteLLM UI.

From the LiteLLM dashboard, click on **Settings** in the left sidebar.

Click on **Cost Tracking** to access the cost configuration options.

Click on **Pricing Calculator** to expand the calculator panel. This section allows you to estimate LLM costs based on expected token usage and request volume.

Click the **Model** dropdown to select the model you want to estimate costs for.

Choose a model from the list. The models shown are the ones configured on your LiteLLM proxy.

Enter the expected **Input Tokens (per request)** - this is the average number of tokens in your prompts.

Enter the expected **Output Tokens (per request)** - this is the average number of tokens in model responses.

Enter your expected request volume. You can specify **Requests per Day** and/or **Requests per Month**.

For example, enter `10000000` for 10 million requests per month.

The calculator automatically updates as you change values. View the cost breakdown including:

Click the **Export** button to download your cost estimate. You can export as:

```
{
"model":"gpt-4",
"input_tokens":1000,
"output_tokens":500,
"num_requests_per_day":1000,
"num_requests_per_month":30000,
"cost_per_request":0.045,
"input_cost_per_request":0.03,
"output_cost_per_request":0.015,
"margin_cost_per_request":0.0,
"daily_cost":45.0,
"daily_input_cost":30.0,
"daily_output_cost":15.0,
"daily_margin_cost":0.0,
"monthly_cost":1350.0,
"monthly_input_cost":900.0,
"monthly_output_cost":450.0,
"monthly_margin_cost":0.0,
"input_cost_per_token":3e-05,
"output_cost_per_token":6e-05,
"provider":"openai"
}
```