---
title: Oauth 2.0 Authentication | liteLLM
url: https://docs.litellm.ai/docs/proxy/oauth2
source: sitemap
fetched_at: 2026-01-21T19:53:07.623319261-03:00
rendered_js: false
word_count: 87
summary: This document provides instructions for configuring the LiteLLM Proxy to authenticate chat and embedding requests using OAuth2.0 tokens.
tags:
    - litellm-proxy
    - oauth2-authentication
    - security-configuration
    - token-validation
    - api-gateway
    - access-control
category: guide
---

Use this if you want to use an Oauth2.0 token to make `/chat`, `/embeddings` requests to the LiteLLM Proxy

## Usage[​](#usage "Direct link to Usage")

1. Set env vars:

```
export OAUTH_TOKEN_INFO_ENDPOINT="https://your-provider.com/token/info"
export OAUTH_USER_ID_FIELD_NAME="sub"
export OAUTH_USER_ROLE_FIELD_NAME="role"
export OAUTH_USER_TEAM_ID_FIELD_NAME="team_id"
```

- `OAUTH_TOKEN_INFO_ENDPOINT`: URL to validate OAuth tokens
- `OAUTH_USER_ID_FIELD_NAME`: Field in token info response containing user ID
- `OAUTH_USER_ROLE_FIELD_NAME`: Field in token info for user's role
- `OAUTH_USER_TEAM_ID_FIELD_NAME`: Field in token info for user's team ID

<!--THE END-->

2. Enable on litellm config.yaml

Set this on your config.yaml

```
model_list:
-model_name: gpt-4
litellm_params:
model: openai/fake
api_key: fake-key
api_base: https://exampleopenaiendpoint-production.up.railway.app/

general_settings:
master_key: sk-1234
enable_oauth2_auth:true
```

3. Use token in requests to LiteLLM

```
curl --location 'http://0.0.0.0:4000/chat/completions' \
    --header 'Content-Type: application/json' \
    --data '{
    "model": "gpt-3.5-turbo",
    "messages": [
        {
        "role": "user",
        "content": "what llm are you"
        }
    ]
}'
```

## Debugging[​](#debugging "Direct link to Debugging")

Start the LiteLLM Proxy with [`--detailed_debug` mode and you should see more verbose logs](https://docs.litellm.ai/docs/proxy/cli#detailed_debug)