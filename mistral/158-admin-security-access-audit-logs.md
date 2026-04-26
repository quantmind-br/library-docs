---
title: Audit logs | Mistral Docs
url: https://docs.mistral.ai/admin/security-access/audit-logs
source: sitemap
fetched_at: 2026-04-26T04:00:58.168555848-03:00
rendered_js: false
word_count: 260
summary: This document explains how to access and utilize audit logs to track user activity, security events, and administrative actions within an Enterprise organization.
tags:
    - audit-logs
    - enterprise-security
    - user-activity
    - compliance-monitoring
    - incident-investigation
    - admin-panel
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Audit Logs

Audit logs provide a **chronological record of actions** performed within your Organization across Studio and Le Chat. Available on **Enterprise** plans. Enabled by default for all Workspaces.

Open [Admin Audit Logs](https://admin.mistral.ai/audit-logs) or click **Audit Logs** in the left menu of the [Admin Panel](https://admin.mistral.ai).

## Log Entry Contents

Each log entry includes:

| Field | Description |
|-------|-------------|
| **Timestamp** (`CreatedAt`) | When the event occurred |
| **Actor** | Who performed the action (human user, API key, or system) |
| **Event** | Specific action (e.g., `batch_job.create`, `le_chat.conversation.deleted`) |
| **Target** | Resource affected (e.g., batch job, conversation, API key) |
| **Metadata** | Additional context about the actor, event, and target |

## Logged Activities

- Authentication events (sign-ins, SSO flows)
- API usage and key management (creation, deletion)
- Organization and Workspace changes
- User management actions (invitations, role changes, removals)
- Settings modifications
- Le Chat interactions (conversation creation, deletion)

## Filtering

Use the filter controls above the log table:

1. Filter by **Actor** (human, API key), **Event** type, or **Target** resource.
2. Combine multiple filters to find specific activities.
3. Customize visible columns by clicking **Columns**.

The table updates automatically as you apply filters.

## Use Cases

- **Security monitoring**: detect unauthorized access or unusual activity patterns.
- **Incident investigation**: trace the sequence of actions leading to an issue.
- **Compliance**: maintain records for regulatory requirements.

> [!note]
> Log export isn't currently supported. Audit logs are only available on Enterprise plans.

#audit-logs #enterprise-security #compliance-monitoring #incident-investigation
