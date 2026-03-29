---
title: User Onboarding Guide | liteLLM
url: https://docs.litellm.ai/docs/proxy/user_onboarding
source: sitemap
fetched_at: 2026-01-21T19:54:03.090766957-03:00
rendered_js: false
word_count: 205
summary: This document provides a comprehensive guide for administrators to onboard users and for end users to start using their API keys with a LiteLLM proxy instance. It covers user creation, permissions management, API key validation, and making initial LLM calls.
tags:
    - litellm-proxy
    - user-onboarding
    - api-key-management
    - user-management
    - access-control
    - llm-api
category: guide
---

A step-by-step guide to help admins onboard users to your LiteLLM proxy instance and help users get started with their API key.

* * *

## For Administrators[​](#for-administrators "Direct link to For Administrators")

### Step 1: Create a User Account[​](#step-1-create-a-user-account "Direct link to Step 1: Create a User Account")

You can create a user account via the Admin UI or using the API.

#### Admin UI[​](#admin-ui "Direct link to Admin UI")

- Go to the (`/ui` endpoint)
- Navigate to the Internal Users section
- Click "Add User" and fill in the required details

#### API[​](#api "Direct link to API")

```
curl -X POST http://localhost:4000/user/new \
  -H "Authorization: Bearer <admin-key>" \
  -H "Content-Type: application/json" \
  -d '{"user_email": "user@example.com"}'
```

* * *

### Step 2: Grant Access & Permissions[​](#step-2-grant-access--permissions "Direct link to Step 2: Grant Access & Permissions")

- Assign the user to a team (optional)
- Set budgets, rate limits, and allowed models as needed
- Generate an API key for the user (via UI or API)

#### **Generate API Key (API Example)**[​](#generate-api-key-api-example "Direct link to generate-api-key-api-example")

```
curl -X POST http://localhost:4000/key/generate \
  -H "Authorization: Bearer <admin-key>" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "<user-id>", "max_budget": 100}'
```

* * *

## For End Users[​](#for-end-users "Direct link to For End Users")

### Step 3: Validate Your API Key[​](#step-3-validate-your-api-key "Direct link to Step 3: Validate Your API Key")

Before making LLM calls, validate your key works by calling the `/v1/models` endpoint:

```
curl -X GET http://localhost:4000/v1/models \
  -H "Authorization: Bearer <your-api-key>"
```

- If your key is valid, you'll get a list of available models.
- If invalid, you'll get a 401 error.

* * *

### Step 4: Hello World - Make Your First LLM Call[​](#step-4-hello-world---make-your-first-llm-call "Direct link to Step 4: Hello World - Make Your First LLM Call")

```
curl -X POST http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer <your-api-key>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

* * *

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

- If you get a 401 error, check with your admin that your key is active and you have access to the requested model.
- Use the `/v1/models` endpoint to quickly check if your key is valid without consuming LLM tokens.

* * *

## See Also[​](#see-also "Direct link to See Also")

- [Proxy Quick Start](https://docs.litellm.ai/docs/proxy/quick_start)
- [User Management](https://docs.litellm.ai/docs/proxy/users)
- [Key Management](https://docs.litellm.ai/docs/proxy/key_management.md)