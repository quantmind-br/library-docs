---
title: Guides Security Compliance Audit Logs
url: https://docs.fireworks.ai/guides/security_compliance/audit_logs
source: sitemap
fetched_at: 2026-04-27T20:18:14.770382051-03:00
rendered_js: false
word_count: 110
summary: This document describes the functionality of audit logs available for Enterprise accounts, explaining that they provide enhanced security visibility, incident investigation capabilities, and compliance reporting by logging all storage operations.
tags:
    - audit-logs
    - enterprise-accounts
    - security-visibility
    - data-access-logging
    - compliance-reporting
    - fireworks-cli
category: guide
optimized: true
optimized_at: 2026-04-27T00:00:00Z
---
Audit logs are available for Enterprise accounts. They enhance security visibility, incident investigation, and compliance reporting by logging all read, write, and delete operations on storage.

## View audit logs

Use the Fireworks CLI to view audit logs, including data access logs:

```bash
firectl ls audit-logs
```

![Audit logs table showing data access activities with columns for timestamp, principal, response code, resource path, and message](https://mintcdn.com/fireworksai/XAK4ji8XrlzPoITj/images/audit-logs-example.png?fit=max&auto=format&n=XAK4ji8XrlzPoITj&q=85&s=b105237a94cf59826404c2dd275297f3)

The audit log table includes:
- **Timestamp**: When the operation occurred
- **Principal**: Account or user who performed the operation
- **Response code**: Outcome of the operation
- **Resource path**: Storage resource accessed
- **Message**: Operation details

> [!tip]
> For other security features, see [[083-guides-security-compliance-data-security|Data Security]].

#audit-logs #security #enterprise-accounts
