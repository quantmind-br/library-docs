---
title: Customer Usage | liteLLM
url: https://docs.litellm.ai/docs/proxy/customer_usage
source: sitemap
fetched_at: 2026-01-21T19:51:38.95731219-03:00
rendered_js: false
word_count: 411
summary: This document explains how to track and visualize end-user spend and usage metrics by associating API requests with customer IDs. It provides instructions for monitoring customer-level analytics, filtering logs, and managing billing within the platform's Admin UI.
tags:
    - customer-usage
    - spend-tracking
    - usage-analytics
    - billing
    - llm-monitoring
    - admin-ui
category: guide
---

Track and visualize end-user spend directly in the dashboard. Monitor customer-level usage analytics, spend logs, and activity metrics to understand how your customers are using your LLM services.

This feature is **available in v1.80.8-stable and above**.

## Overview[​](#overview "Direct link to Overview")

Customer Usage enables you to track spend and usage for individual customers (end users) by passing an ID in your API requests. This allows you to:

- Track spend per customer automatically
- View customer-level usage analytics in the Admin UI
- Filter spend logs and activity metrics by customer ID
- Set budgets and rate limits per customer
- Monitor customer usage patterns and trends

## How to Track Spend[​](#how-to-track-spend "Direct link to How to Track Spend")

Track customer spend by including a `user` field in your API requests or by passing a customer ID header. The customer ID will be automatically tracked and associated with all spend from that request.

- Request Body
- Request Header

### Using Request Body[​](#using-request-body "Direct link to Using Request Body")

Make a `/chat/completions` call with the `user` field containing your customer ID:

Track spend with customer ID in body

```
curl -X POST 'http://0.0.0.0:4000/chat/completions' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer sk-1234' \
  --data '{
    "model": "gpt-3.5-turbo",
    "user": "customer-123",
    "messages": [
      {
        "role": "user",
        "content": "What is the capital of France?"
      }
    ]
  }'
```

The customer ID will be automatically upserted into the database with the new spend. If the customer ID already exists, spend will be incremented.

### Example using OpenWebUI[​](#example-using-openwebui "Direct link to Example using OpenWebUI")

See the [Open WebUI tutorial](https://docs.litellm.ai/docs/tutorials/openweb_ui) for detailed instructions on connecting Open WebUI to LiteLLM and tracking customer usage.

## How to View Spend[​](#how-to-view-spend "Direct link to How to View Spend")

### View Spend in Admin UI[​](#view-spend-in-admin-ui "Direct link to View Spend in Admin UI")

Navigate to the Customer Usage tab in the Admin UI to view customer-level spend analytics:

#### 1. Access Customer Usage[​](#1-access-customer-usage "Direct link to 1. Access Customer Usage")

Go to the Usage page in the Admin UI (`PROXY_BASE_URL/ui/?login=success&page=new_usage`) and click on the **Customer Usage** tab.

#### 2. View Customer Analytics[​](#2-view-customer-analytics "Direct link to 2. View Customer Analytics")

The Customer Usage dashboard provides:

- **Total spend per customer**: View aggregated spend across all customers
- **Daily spend trends**: See how customer spend changes over time
- **Model usage breakdown**: Understand which models each customer uses
- **Activity metrics**: Track requests, tokens, and success rates per customer

#### 3. Filter by Customer[​](#3-filter-by-customer "Direct link to 3. Filter by Customer")

Use the customer filter dropdown to view spend for specific customers:

- Select one or more customer IDs from the dropdown
- View filtered analytics, spend logs, and activity metrics
- Compare spend across different customers

## Use Cases[​](#use-cases "Direct link to Use Cases")

### Customer Billing[​](#customer-billing "Direct link to Customer Billing")

Track spend per customer to accurately bill your end users:

- Monitor individual customer usage
- Generate invoices based on actual spend
- Set spending limits per customer

### Usage Analytics[​](#usage-analytics "Direct link to Usage Analytics")

Understand how different customers use your service:

- Identify high-value customers
- Analyze usage patterns
- Optimize resource allocation

* * *

## Related Features[​](#related-features "Direct link to Related Features")

- [Customers / End-User Budgets](https://docs.litellm.ai/docs/proxy/customers) - Set budgets and rate limits for customers
- [Cost Tracking](https://docs.litellm.ai/docs/proxy/cost_tracking) - Comprehensive cost tracking and analytics
- [Billing](https://docs.litellm.ai/docs/proxy/billing) - Bill customers based on their usage