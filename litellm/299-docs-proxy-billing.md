---
title: Billing | liteLLM
url: https://docs.litellm.ai/docs/proxy/billing
source: sitemap
fetched_at: 2026-01-21T19:51:15.633104605-03:00
rendered_js: false
word_count: 158
summary: This document provides instructions for integrating LiteLLM with Lago to enable usage-based billing for internal teams and external customers.
tags:
    - litellm
    - lago
    - usage-based-billing
    - cost-tracking
    - api-proxy
    - billing-integration
category: tutorial
---

Bill internal teams, external customers for their usage

**🚨 Requirements**

- [Setup Lago](https://docs.getlago.com/guide/self-hosted/docker#run-the-app), for usage-based billing. We recommend following [their Stripe tutorial](https://docs.getlago.com/templates/per-transaction/stripe#step-1-create-billable-metrics-for-transaction)

Steps:

- Connect the proxy to Lago
- Set the id you want to bill for (customers, internal users, teams)
- Start!

## Quick Start[​](#quick-start "Direct link to Quick Start")

Bill internal teams for their usage

### 1. Connect proxy to Lago[​](#1-connect-proxy-to-lago "Direct link to 1. Connect proxy to Lago")

Set 'lago' as a callback on your proxy config.yaml

```
model_list:
-model_name: fake-openai-endpoint
litellm_params:
model: openai/fake
api_key: fake-key
api_base: https://exampleopenaiendpoint-production.up.railway.app/

litellm_settings:
callbacks:["lago"]# 👈 KEY CHANGE

general_settings:
master_key: sk-1234
```

Add your Lago keys to the environment

```
export LAGO_API_BASE="http://localhost:3000" # self-host - https://docs.getlago.com/guide/self-hosted/docker#run-the-app
export LAGO_API_KEY="3e29d607-de54-49aa-a019-ecf585729070" # Get key - https://docs.getlago.com/guide/self-hosted/docker#find-your-api-key
export LAGO_API_EVENT_CODE="openai_tokens" # name of lago billing code
export LAGO_API_CHARGE_BY="team_id" # 👈 Charges 'team_id' attached to proxy key
```

Start proxy

```
litellm --config /path/to/config.yaml
```

### 2. Create Key for Internal Team[​](#2-create-key-for-internal-team "Direct link to 2. Create Key for Internal Team")

```
curl 'http://0.0.0.0:4000/key/generate' \
--header 'Authorization: Bearer sk-1234' \
--header 'Content-Type: application/json' \
--data-raw '{"team_id": "my-unique-id"}' # 👈 Internal Team's ID
```

Response Object:

```
{
  "key": "sk-tXL0wt5-lOOVK9sfY2UacA",
}
```

### 3. Start billing\![​](#3-start-billing "Direct link to 3. Start billing!")

- Curl
- OpenAI Python SDK
- Langchain

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer sk-tXL0wt5-lOOVK9sfY2UacA' \ # 👈 Team's Key
--data ' {
      "model": "fake-openai-endpoint",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ],
    }
'
```

**See Results on Lago**

## Advanced - Lago Logging object[​](#advanced---lago-logging-object "Direct link to Advanced - Lago Logging object")

This is what LiteLLM will log to Lagos

```
{
    "event": {
      "transaction_id": "<generated_unique_id>",
      "external_customer_id": <selected_id>, # either 'end_user_id', 'user_id', or 'team_id'. Default 'end_user_id'. 
      "code": os.getenv("LAGO_API_EVENT_CODE"), 
      "properties": {
          "input_tokens": <number>,
          "output_tokens": <number>,
          "model": <string>,
          "response_cost": <number>, # 👈 LITELLM CALCULATED RESPONSE COST - https://github.com/BerriAI/litellm/blob/d43f75150a65f91f60dc2c0c9462ce3ffc713c1f/litellm/utils.py#L1473
      }
    }
}
```

## Advanced - Bill Customers, Internal Users[​](#advanced---bill-customers-internal-users "Direct link to Advanced - Bill Customers, Internal Users")

For:

- Customers (id passed via 'user' param in /chat/completion call) = 'end\_user\_id'
- Internal Users (id set when [creating keys](https://docs.litellm.ai/docs/proxy/virtual_keys#advanced---spend-tracking)) = 'user\_id'
- Teams (id set when [creating keys](https://docs.litellm.ai/docs/proxy/virtual_keys#advanced---spend-tracking)) = 'team\_id'

<!--THE END-->

- Customer Billing
- Internal User Billing

<!--THE END-->

1. Set 'LAGO\_API\_CHARGE\_BY' to 'end\_user\_id'

```
export LAGO_API_CHARGE_BY="end_user_id"
```

2. Test it!

<!--THE END-->

- Curl
- OpenAI Python SDK
- Langchain

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
--header 'Content-Type: application/json' \
--data ' {
      "model": "gpt-4o",
      "messages": [
        {
          "role": "user",
          "content": "what llm are you"
        }
      ],
      "user": "my_customer_id" # 👈 whatever your customer id is
    }
'
```