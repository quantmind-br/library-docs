---
title: v1.59.0
url: https://docs.litellm.ai/release_notes/v1.59.0
source: sitemap
fetched_at: 2026-01-21T19:43:18.465727271-03:00
rendered_js: false
word_count: 97
summary: This document explains how to enable and view message and response logs in the LiteLLM Admin UI by modifying the proxy configuration and database settings.
tags:
    - litellm
    - admin-ui
    - logging
    - proxy-configuration
    - database-schema
    - enterprise-features
category: configuration
---

info

Get a 7 day free trial for LiteLLM Enterprise [here](https://litellm.ai/#trial).

**no call needed**

## UI Improvements[​](#ui-improvements "Direct link to UI Improvements")

### \[Opt In] Admin UI - view messages / responses[​](#opt-in-admin-ui---view-messages--responses "Direct link to [Opt In] Admin UI - view messages / responses")

You can now view messages and response logs on Admin UI.

How to enable it - add `store_prompts_in_spend_logs: true` to your `proxy_config.yaml`

Once this flag is enabled, your `messages` and `responses` will be stored in the `LiteLLM_Spend_Logs` table.

```
general_settings:
store_prompts_in_spend_logs:true
```

## DB Schema Change[​](#db-schema-change "Direct link to DB Schema Change")

Added `messages` and `responses` to the `LiteLLM_Spend_Logs` table.

**By default this is not logged.** If you want `messages` and `responses` to be logged, you need to opt in with this setting

```
general_settings:
store_prompts_in_spend_logs:true
```