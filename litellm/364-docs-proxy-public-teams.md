---
title: '[BETA] Public Teams | liteLLM'
url: https://docs.litellm.ai/docs/proxy/public_teams
source: sitemap
fetched_at: 2026-01-21T19:53:23.200152963-03:00
rendered_js: false
word_count: 25
summary: This guide explains how to configure LiteLLM to expose specific teams to users for selection during the signup or SSO onboarding process.
tags:
    - litellm
    - team-management
    - user-signup
    - sso-integration
    - access-control
category: guide
---

Expose available teams to your users to join on signup.

## Quick Start[​](#quick-start "Direct link to Quick Start")

1. Create a team on LiteLLM

```
curl -X POST '<PROXY_BASE_URL>/team/new' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <MASTER_KEY>' \
-d '{"name": "My Team", "team_id": "team_id_1"}'
```

2. Expose the team to your users

```
litellm_settings:
default_internal_user_params:
available_teams:["team_id_1"]# 👈 Make team available to new SSO users
```

3. Test it!

```
curl -L -X POST 'http://0.0.0.0:4000/team/member_add' \
-H 'Authorization: Bearer sk-<USER_KEY>' \
-H 'Content-Type: application/json' \
--data-raw '{
    "team_id": "team_id_1", 
    "member": [{"role": "user", "user_id": "my-test-user"}]
}'
```