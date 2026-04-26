---
title: Admin API | Mistral Docs
url: https://docs.mistral.ai/admin/security-access/admin-api
source: sitemap
fetched_at: 2026-04-26T04:00:56.725215576-03:00
rendered_js: false
word_count: 83
summary: This document introduces the Admin API, explaining its functionality for automating organization management, user administration, and billing tasks, while specifying required permissions.
tags:
    - admin-api
    - organization-management
    - user-provisioning
    - access-control
    - billing-management
category: api
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Admin API

The Admin API provides programmatic access to organization management tasks available through the [Admin Panel](https://admin.mistral.ai).

## Use Cases

Automate:
- Organization and Workspace management
- User invitations and role assignments
- Seat provisioning and access control
- Billing and usage queries

## Authentication

Admin API requests require an API key belonging to a user with the **Admin** role in the Organization.

> [!warning]
> Standard API keys with Member or Billing roles don't have access to administrative endpoints.

See the [API reference](https://docs.mistral.ai/api) for endpoint documentation.

#admin-api #organization-management #user-provisioning #access-control
