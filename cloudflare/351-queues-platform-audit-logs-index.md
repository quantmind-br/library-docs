---
title: Audit Logs · Cloudflare Queues docs
url: https://developers.cloudflare.com/queues/platform/audit-logs/index.md
source: llms
fetched_at: 2026-01-24T15:20:26.724336938-03:00
rendered_js: false
word_count: 145
summary: This document explains how Cloudflare audit logs record configuration changes and administrative actions for Queues, including queue lifecycle events and consumer management.
tags:
    - cloudflare-queues
    - audit-logs
    - account-security
    - logging
    - queue-management
    - monitoring
category: reference
---

[Audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/) provide a comprehensive summary of changes made within your Cloudflare account, including those made to Queues. This functionality is always enabled.

## Viewing audit logs

To view audit logs for your Queue in the Cloudflare dashboard, go to the **Audit logs** page.

[Go to **Audit logs**](https://dash.cloudflare.com/?to=/:account/audit-log)

For more information on how to access and use audit logs, refer to [Review audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/).

## Logged operations

The following configuration actions are logged:

| Operation | Description |
| - | - |
| CreateQueue | Creation of a new queue. |
| DeleteQueue | Deletion of an existing queue. |
| UpdateQueue | Updating the configuration of a queue. |
| AttachConsumer | Attaching a consumer, including HTTP pull consumers, to the Queue. |
| RemoveConsumer | Removing a consumer, including HTTP pull consumers, from the Queue. |
| UpdateConsumerSettings | Changing Queues consumer settings. |