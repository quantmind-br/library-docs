---
title: v1.65.0 - Team Model Add - update
url: https://docs.litellm.ai/release_notes/v1.65.0
source: sitemap
fetched_at: 2026-01-21T19:43:28.687966123-03:00
rendered_js: false
word_count: 81
summary: This document details updates to model management endpoints in version 1.65.0, focusing on expanded permissions for team admins to create, update, and delete models via the API and UI.
tags:
    - litellm
    - model-management
    - access-control
    - api-updates
    - permissions
    - team-administration
category: api
---

v1.65.0 updates the `/model/new` endpoint to prevent non-team admins from creating team models.

This means that only proxy admins or team admins can create team models.

## Additional Changes[​](#additional-changes "Direct link to Additional Changes")

- Allows team admins to call `/model/update` to update team models.
- Allows team admins to call `/model/delete` to delete team models.
- Introduces new `user_models_only` param to `/v2/model/info` - only return models added by this user.

These changes enable team admins to add and manage models for their team on the LiteLLM UI + API.