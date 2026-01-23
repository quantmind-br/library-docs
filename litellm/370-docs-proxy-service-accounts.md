---
title: '[Beta] Service Accounts | liteLLM'
url: https://docs.litellm.ai/docs/proxy/service_accounts
source: sitemap
fetched_at: 2026-01-21T19:53:36.43630751-03:00
rendered_js: false
word_count: 107
summary: This document explains how to create and manage service account keys for production projects to ensure key persistence and apply team-based usage limits. It provides instructions for generating keys via API, configuring specific settings, and enforcing request parameters.
tags:
    - service-account
    - api-key-management
    - litellm-proxy
    - access-control
    - authentication
    - team-limits
category: guide
---

Use this if you want to create Virtual Keys that are not owned by a specific user but instead created for production projects

Why use a service account key?

- Prevent key from being deleted when user is deleted.
- Apply team limits, not team member limits to key.

## Usage[​](#usage "Direct link to Usage")

Use the `/key/service-account/generate` endpoint to generate a service account key.

```
curl -L -X POST 'http://localhost:4000/key/service-account/generate' \
-H 'Authorization: Bearer sk-1234' \
-H 'Content-Type: application/json' \
-d '{
    "team_id": "my-unique-team"
}'
```

## Example - require `user` param for all service account requests[​](#example---require-user-param-for-all-service-account-requests "Direct link to example---require-user-param-for-all-service-account-requests")

### 1. Set settings for Service Accounts[​](#1-set-settings-for-service-accounts "Direct link to 1. Set settings for Service Accounts")

Set `service_account_settings` if you want to create settings that only apply to service account keys

```
general_settings:
service_account_settings:
enforced_params:["user"]# this means the "user" param is enforced for all requests made through any service account keys
```

### 2. Create Service Account Key on LiteLLM Proxy Admin UI[​](#2-create-service-account-key-on-litellm-proxy-admin-ui "Direct link to 2. Create Service Account Key on LiteLLM Proxy Admin UI")

### 3. Test Service Account Key[​](#3-test-service-account-key "Direct link to 3. Test Service Account Key")

- Unsuccessful call
- Successful call

```
curl --location 'http://localhost:4000/chat/completions' \
    --header 'Authorization: Bearer <sk-your-service-account>' \
    --header 'Content-Type: application/json' \
    --data '{
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": "hello"
        }
    ]
}'
```

Expected Response

```
{
"error":{
"message":"BadRequest please pass param=user in request body. This is a required param for service account",
"type":"bad_request_error",
"param":"user",
"code":"400"
}
}
```