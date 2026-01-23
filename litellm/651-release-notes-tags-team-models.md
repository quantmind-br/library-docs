---
title: One post tagged with "team models" | liteLLM
url: https://docs.litellm.ai/release_notes/tags/team-models
source: sitemap
fetched_at: 2026-01-21T19:42:10.164959701-03:00
rendered_js: false
word_count: 81
summary: This document outlines updates to LiteLLM v1.65.0 that restrict model creation to admins and expand management capabilities for team-specific models via the API.
tags:
    - litellm
    - api-updates
    - access-control
    - model-management
    - team-administration
    - v1-65-0
category: api
---

v1.65.0 updates the `/model/new` endpoint to prevent non-team admins from creating team models.

This means that only proxy admins or team admins can create team models.

## Additional Changes[​](#additional-changes "Direct link to Additional Changes")

- Allows team admins to call `/model/update` to update team models.
- Allows team admins to call `/model/delete` to delete team models.
- Introduces new `user_models_only` param to `/v2/model/info` - only return models added by this user.

These changes enable team admins to add and manage models for their team on the LiteLLM UI + API.