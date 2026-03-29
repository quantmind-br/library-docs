---
title: Model Access Groups | liteLLM
url: https://docs.litellm.ai/docs/proxy/model_access_groups
source: sitemap
fetched_at: 2026-01-21T19:52:58.629763295-03:00
rendered_js: false
word_count: 599
summary: This document explains how to organize multiple AI models into named groups to simplify access control and permission management for API keys and teams.
tags:
    - access-control
    - model-management
    - api-key-permissions
    - wildcard-matching
    - litellm-proxy
    - model-governance
category: guide
---

### Overview[​](#overview "Direct link to Overview")

Group multiple models under a single name, then grant keys or teams access to the entire group. Add or remove models from a group without updating individual keys.

Use cases:

- Separate production and development models
- Restrict expensive models to specific teams
- Organize models by provider or capability
- Control access to model families with wildcards (e.g., `openai/*`)

### How It Works[​](#how-it-works "Direct link to How It Works")

**Key Concept:** Group models together → Attach group to key → Key gets access to all models in group

**Step 1. Assign model, access group in config.yaml**

config.yaml

```
model_list:
-model_name: gpt-4
litellm_params:
model: openai/fake
api_key: fake-key
api_base: https://exampleopenaiendpoint-production.up.railway.app/
model_info:
access_groups:["beta-models"]# 👈 Model Access Group
-model_name: fireworks-llama-v3-70b-instruct
litellm_params:
model: fireworks_ai/accounts/fireworks/models/llama-v3-70b-instruct
api_key:"os.environ/FIREWORKS"
model_info:
access_groups:["beta-models"]# 👈 Model Access Group
```

- Key Access Groups
- Team Access Groups

**Create key with access group**

Create Key with Access Group

```
curl --location 'http://localhost:4000/key/generate' \
-H 'Authorization: Bearer <your-master-key>' \
-H 'Content-Type: application/json' \
-d '{"models": ["beta-models"], # 👈 Model Access Group
			"max_budget": 0,}'
```

Test Key

- Allowed Access
- Disallowed Access

Test Key - Allowed Access

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-<key-from-previous-step>" \
  -d '{
    "model": "gpt-4",
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'
```

### ✨ Control Access on Wildcard Models[​](#-control-access-on-wildcard-models "Direct link to ✨ Control Access on Wildcard Models")

Control access to all models with a specific prefix (e.g. `openai/*`).

Use this to also give users access to all models, except for a few that you don't want them to use (e.g. `openai/o1-*`).

info

Setting model access groups on wildcard models is an Enterprise feature.

See pricing [here](https://litellm.ai/#pricing)

Get a trial key [here](https://litellm.ai/#trial)

1. Setup config.yaml

config.yaml - Wildcard Models

```
model_list:
-model_name: openai/*
litellm_params:
model: openai/*
api_key: os.environ/OPENAI_API_KEY
model_info:
access_groups:["default-models"]
-model_name: openai/o1-*
litellm_params:
model: openai/o1-*
api_key: os.environ/OPENAI_API_KEY
model_info:
access_groups:["restricted-models"]
```

2. Generate a key with access to `default-models`

Generate Key for Wildcard Access Group

```
curl -L -X POST 'http://0.0.0.0:4000/key/generate' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{
    "models": ["default-models"],
}'
```

3. Test the key

<!--THE END-->

- Successful Request
- Rejected Request

Test Wildcard Access - Allowed

```
curl -i http://localhost:4000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-<key-from-previous-step>" \
  -d '{
    "model": "openai/gpt-4",
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'
```

## Managing Access Groups via API[​](#managing-access-groups-via-api "Direct link to Managing Access Groups via API")

Database Models Only

Access group management APIs only work with models stored in the database (added via `/model/new`).

Models defined in `config.yaml` cannot be managed through these APIs and must be configured directly in the config file.

Use the access group management endpoints to dynamically create, update, and delete access groups without restarting the proxy.

### Tutorial: Complete Access Group Workflow[​](#tutorial-complete-access-group-workflow "Direct link to Tutorial: Complete Access Group Workflow")

This tutorial shows how to create an access group, view its details, attach it to a key, and update the models in the group.

**Prerequisites:**

- Models must be added to the database first (not just in config.yaml)
- You need your master key for authorization

#### Step 1: Add Models to Database[​](#step-1-add-models-to-database "Direct link to Step 1: Add Models to Database")

First, add some models to the database:

Add Models to Database

```
# Add GPT-4 to database
curl -X POST 'http://localhost:4000/model/new' \
  -H 'Authorization: Bearer sk-1234' \
  -H 'Content-Type: application/json' \
  -d '{
    "model_name": "gpt-4",
    "litellm_params": {
      "model": "gpt-4",
      "api_key": "os.environ/OPENAI_API_KEY"
    }
  }'

# Add Claude to database
curl -X POST 'http://localhost:4000/model/new' \
  -H 'Authorization: Bearer sk-1234' \
  -H 'Content-Type: application/json' \
  -d '{
    "model_name": "claude-3-opus",
    "litellm_params": {
      "model": "claude-3-opus-20240229",
      "api_key": "os.environ/ANTHROPIC_API_KEY"
    }
  }'
```

#### Step 2: Create Access Group[​](#step-2-create-access-group "Direct link to Step 2: Create Access Group")

Create an access group containing multiple models:

Create Access Group

```
curl -X POST 'http://localhost:4000/access_group/new' \
  -H 'Authorization: Bearer sk-1234' \
  -H 'Content-Type: application/json' \
  -d '{
    "access_group": "production-models",
    "model_names": ["gpt-4", "claude-3-opus"]
  }'
```

**Response:**

Response

```
{
"access_group":"production-models",
"model_names":["gpt-4","claude-3-opus"],
"models_updated":2
}
```

#### Step 3: View Access Group Info[​](#step-3-view-access-group-info "Direct link to Step 3: View Access Group Info")

Check the access group details:

Get Access Group Info

```
curl -X GET 'http://localhost:4000/access_group/production-models/info' \
  -H 'Authorization: Bearer sk-1234'
```

**Response:**

Response

```
{
"access_group":"production-models",
"model_names":["gpt-4","claude-3-opus"],
"deployment_count":2
}
```

#### Step 4: Create Key with Access Group[​](#step-4-create-key-with-access-group "Direct link to Step 4: Create Key with Access Group")

Create an API key that can access all models in the group:

Create Key with Access Group

```
curl -X POST 'http://localhost:4000/key/generate' \
  -H 'Authorization: Bearer sk-1234' \
  -H 'Content-Type: application/json' \
  -d '{
    "models": ["production-models"],
    "max_budget": 100
  }'
```

**Response:**

Response

```
{
"key":"sk-...",
"models":["production-models"]
}
```

**Test the key:**

Test Key Access

```
# This succeeds - gpt-4 is in production-models
curl -X POST 'http://localhost:4000/v1/chat/completions' \
  -H 'Authorization: Bearer sk-...' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello"}]
  }'

# This succeeds - claude-3-opus is in production-models
curl -X POST 'http://localhost:4000/v1/chat/completions' \
  -H 'Authorization: Bearer sk-...' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "claude-3-opus",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

#### Step 5: Update Access Group[​](#step-5-update-access-group "Direct link to Step 5: Update Access Group")

Add or remove models from the access group:

Update Access Group

```
curl -X PUT 'http://localhost:4000/access_group/production-models/update' \
  -H 'Authorization: Bearer sk-1234' \
  -H 'Content-Type: application/json' \
  -d '{
    "model_names": ["gpt-4", "claude-3-opus", "gemini-pro"]
  }'
```

**Response:**

Response

```
{
"access_group":"production-models",
"model_names":["gpt-4","claude-3-opus","gemini-pro"],
"models_updated":3
}
```

The API key from Step 4 now automatically has access to `gemini-pro` without any changes to the key itself.

### API Reference - Access Group Management[​](#api-reference---access-group-management "Direct link to API Reference - Access Group Management")

For complete API documentation including all endpoints, parameters, and response schemas, see the [Access Group Management API Reference](https://litellm-api.up.railway.app/#/model%20management/create_model_group_access_group_new_post).

## Managing Access Groups via UI[​](#managing-access-groups-via-ui "Direct link to Managing Access Groups via UI")

You can also manage access groups through the LiteLLM Admin UI.

### Step 1: Add Model to Access Group[​](#step-1-add-model-to-access-group "Direct link to Step 1: Add Model to Access Group")

When adding a model to the database, assign it to an access group using the "Model Access Group" field:

![Add Model with Access Group](https://docs.litellm.ai/assets/images/add_model_access-29a26dc3efb36af7e77eae7983cf3532.png)

In this example, `gpt-4` is added to the `production-models` access group.

### Step 2: Create Key with Access Group[​](#step-2-create-key-with-access-group "Direct link to Step 2: Create Key with Access Group")

When creating an API key, specify the access group in the "Models" field:

![Create Key with Access Group](https://docs.litellm.ai/assets/images/add_model_key-d0614f9fd52a8c70a6f3b1b4389d4283.png)

The key will have access to all models in the `production-models` group.

### Step 3: Test the Key[​](#step-3-test-the-key "Direct link to Step 3: Test the Key")

Use the generated key to make requests:

Test Key with Access Group

```
# This succeeds - gpt-4 is in production-models
curl -X POST 'http://localhost:4000/v1/chat/completions' \
  -H 'Authorization: Bearer sk-...' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

**Response:**

Success Response

```
{
"id":"chatcmpl-...",
"object":"chat.completion",
"created":1234567890,
"model":"gpt-4",
"choices":[
{
"index":0,
"message":{
"role":"assistant",
"content":"Hello! How can I help you today?"
},
"finish_reason":"stop"
}
]
}
```

If you try to access a model not in the access group, the request will be rejected:

Test Rejected Request

```
# This fails - gpt-4o is not in production-models
curl -X POST 'http://localhost:4000/v1/chat/completions' \
  -H 'Authorization: Bearer sk-...' \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

**Response:**

Error Response

```
{
"error":{
"message":"Invalid model for key",
"type":"invalid_request_error"
}
}
```