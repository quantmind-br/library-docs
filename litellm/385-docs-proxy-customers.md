---
title: Customers / End-User Budgets | liteLLM
url: https://docs.litellm.ai/docs/proxy/customers
source: sitemap
fetched_at: 2026-01-21T19:51:39.129595654-03:00
rendered_js: false
word_count: 281
summary: This guide explains how to track and manage LLM usage spend for customers using LiteLLM Proxy, including setting budget limits and pricing tiers.
tags:
    - litellm-proxy
    - spend-tracking
    - budget-management
    - rate-limiting
    - usage-quotas
    - customer-management
category: guide
---

Track spend, set budgets for your customers.

## Tracking Customer Spend[​](#tracking-customer-spend "Direct link to Tracking Customer Spend")

### 1. Make LLM API call w/ Customer ID[​](#1-make-llm-api-call-w-customer-id "Direct link to 1. Make LLM API call w/ Customer ID")

Make a /chat/completions call, pass 'user' - First call Works

Make request with customer ID

```
curl -X POST 'http://0.0.0.0:4000/chat/completions' \
        --header 'Content-Type: application/json' \
        --header 'Authorization: Bearer sk-1234' \ # 👈 YOUR PROXY KEY
        --data ' {
        "model": "azure-gpt-3.5",
        "user": "ishaan3", # 👈 CUSTOMER ID
        "messages": [
            {
            "role": "user",
            "content": "what time is it"
            }
        ]
        }'
```

The customer\_id will be upserted into the DB with the new spend.

If the customer\_id already exists, spend will be incremented.

### 2. Get Customer Spend[​](#2-get-customer-spend "Direct link to 2. Get Customer Spend")

- All-up spend
- Event Webhook

Call `/customer/info` to get a customer's all up spend

Get customer spend

```
curl -X GET 'http://0.0.0.0:4000/customer/info?end_user_id=ishaan3' \ # 👈 CUSTOMER ID
        -H 'Authorization: Bearer sk-1234' \ # 👈 YOUR PROXY KEY
```

Expected Response:

Response

```
{
"user_id":"ishaan3",
"blocked":false,
"alias":null,
"spend":0.001413,
"allowed_model_region":null,
"default_model":null,
"litellm_budget_table":null
}
```

## Setting Customer Budgets[​](#setting-customer-budgets "Direct link to Setting Customer Budgets")

Set customer budgets (e.g. monthly budgets, tpm/rpm limits) on LiteLLM Proxy

### Default Budget for All Customers[​](#default-budget-for-all-customers "Direct link to Default Budget for All Customers")

Apply budget limits to all customers without explicit budgets. This is useful for rate limiting and spending controls across all end users.

**Step 1: Create a default budget**

Create default budget

```
curl -X POST 'http://localhost:4000/budget/new' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
    "max_budget": 10,
    "rpm_limit": 2,
    "tpm_limit": 1000
}'
```

**Step 2: Configure the default budget ID**

config.yaml

```
litellm_settings:
max_end_user_budget_id:"budget_id_from_step_1"
```

**Step 3: Test it**

Make request with customer ID

```
curl -X POST 'http://localhost:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello"}],
    "user": "my-customer-id"
}'
```

The customer will be subject to the default budget limits (RPM, TPM, and $ budget). Customers with explicit budgets are unaffected.

### Quick Start[​](#quick-start "Direct link to Quick Start")

Create / Update a customer with budget

**Create New Customer w/ budget**

Create customer with budget

```
curl -X POST 'http://0.0.0.0:4000/customer/new'         
    -H 'Authorization: Bearer sk-1234'         
    -H 'Content-Type: application/json'         
    -d '{
        "user_id" : "my-customer-id",
        "max_budget": "0", # 👈 CAN BE FLOAT
    }'
```

**Test it!**

Test customer budget

```
curl -X POST 'http://localhost:4000/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-D '{
    "model": "mistral",
    "messages": [
        {
        "role": "user",
        "content": "What'\''s the weather like in Boston today?"
        }
    ],
    "user": "ishaan-jaff-48"
}
```

### Assign Pricing Tiers[​](#assign-pricing-tiers "Direct link to Assign Pricing Tiers")

Create and assign customers to pricing tiers.

#### 1. Create a budget[​](#1-create-a-budget "Direct link to 1. Create a budget")

- UI
- API

<!--THE END-->

- Go to the 'Budgets' tab on the UI.
- Click on '+ Create Budget'.
- Create your pricing tier (e.g. 'my-free-tier' with budget $4). This means each user on this pricing tier will have a max budget of $4.

#### 2. Assign Budget to Customer[​](#2-assign-budget-to-customer "Direct link to 2. Assign Budget to Customer")

In your application code, assign budget when creating a new customer.

Just use the `budget_id` used when creating the budget. In our example, this is `my-free-tier`.

Assign budget to customer

```
curl -X POST 'http://localhost:4000/customer/new' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-D '{
    "user_id": "my-customer-id",
    "budget_id": "my-free-tier" # 👈 KEY CHANGE
}
```

#### 3. Test it\![​](#3-test-it "Direct link to 3. Test it!")

- curl
- OpenAI

Test with curl

```
curl -X POST 'http://localhost:4000/customer/new' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer sk-1234' \
-D '{
    "user_id": "my-customer-id",
    "budget_id": "my-free-tier" # 👈 KEY CHANGE
}
```