---
title: v1.57.7
url: https://docs.litellm.ai/release_notes/v1.57.7
source: sitemap
fetched_at: 2026-01-21T19:43:15.435152843-03:00
rendered_js: false
word_count: 207
summary: This document details recent updates to LiteLLM, including improvements to Langfuse prompt management, team and organization UI features, Hashicorp Vault support, and custom Prometheus metrics.
tags:
    - litellm
    - langfuse
    - team-management
    - hashicorp-vault
    - prometheus-metrics
    - prompt-management
    - secret-management
category: other
---

`langfuse`, `management endpoints`, `ui`, `prometheus`, `secret management`

## Langfuse Prompt Management[​](#langfuse-prompt-management "Direct link to Langfuse Prompt Management")

Langfuse Prompt Management is being labelled as BETA. This allows us to iterate quickly on the feedback we're receiving, and making the status clearer to users. We expect to make this feature to be stable by next month (February 2025).

Changes:

- Include the client message in the LLM API Request. (Previously only the prompt template was sent, and the client message was ignored).
- Log the prompt template in the logged request (e.g. to s3/langfuse).
- Log the 'prompt\_id' and 'prompt\_variables' in the logged request (e.g. to s3/langfuse).

[Start Here](https://docs.litellm.ai/docs/proxy/prompt_management)

## Team/Organization Management + UI Improvements[​](#teamorganization-management--ui-improvements "Direct link to Team/Organization Management + UI Improvements")

Managing teams and organizations on the UI is now easier.

Changes:

- Support for editing user role within team on UI.
- Support updating team member role to admin via api - `/team/member_update`
- Show team admins all keys for their team.
- Add organizations with budgets
- Assign teams to orgs on the UI
- Auto-assign SSO users to teams

[Start Here](https://docs.litellm.ai/docs/proxy/self_serve)

## Hashicorp Vault Support[​](#hashicorp-vault-support "Direct link to Hashicorp Vault Support")

We now support writing LiteLLM Virtual API keys to Hashicorp Vault.

[Start Here](https://docs.litellm.ai/docs/proxy/vault)

## Custom Prometheus Metrics[​](#custom-prometheus-metrics "Direct link to Custom Prometheus Metrics")

Define custom prometheus metrics, and track usage/latency/no. of requests against them

This allows for more fine-grained tracking - e.g. on prompt template passed in request metadata

[Start Here](https://docs.litellm.ai/docs/proxy/prometheus#beta-custom-metrics)