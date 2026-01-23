---
title: User Management Hierarchy | liteLLM
url: https://docs.litellm.ai/docs/proxy/user_management_heirarchy
source: sitemap
fetched_at: 2026-01-21T19:54:02.360586533-03:00
rendered_js: false
word_count: 59
summary: This document describes the hierarchical relationship between organizations, teams, users, and budgets in LiteLLM, including links to their respective management APIs.
tags:
    - litellm
    - user-hierarchy
    - organization-management
    - team-management
    - budget-tracking
    - access-control
category: concept
---

LiteLLM supports a hierarchy of users, teams, organizations, and budgets.

- Organizations can have multiple teams. [API Reference](https://litellm-api.up.railway.app/#/organization%20management)
- Teams can have multiple users. [API Reference](https://litellm-api.up.railway.app/#/team%20management)
- Users can have multiple keys, and be on multiple teams. [API Reference](https://litellm-api.up.railway.app/#/budget%20management)
- Keys can belong to either a team or a user. [API Reference](https://litellm-api.up.railway.app/#/end-user%20management)

info

See [Access Control](https://docs.litellm.ai/docs/proxy/access_control) for more details on roles and permissions.