---
title: Audit Logs · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/platform/audit-logs/index.md
source: llms
fetched_at: 2026-01-24T15:21:28.34933586-03:00
rendered_js: false
word_count: 260
summary: This document explains how to use Cloudflare audit logs to track and review configuration changes made to R2 buckets, including bucket creation, deletion, and settings updates.
tags:
    - cloudflare-r2
    - audit-logs
    - bucket-management
    - account-security
    - logging
category: guide
---

[Audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/) provide a comprehensive summary of changes made within your Cloudflare account, including those made to R2 buckets. This functionality is available on all plan types, free of charge, and is always enabled.

## Viewing audit logs

To view audit logs for your R2 buckets, go to the **Audit logs** page.

[Go to **Audit logs**](https://dash.cloudflare.com/?to=/:account/audit-log)

For more information on how to access and use audit logs, refer to [Review audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/).

## Logged operations

The following configuration actions are logged:

| Operation | Description |
| - | - |
| CreateBucket | Creation of a new bucket. |
| DeleteBucket | Deletion of an existing bucket. |
| AddCustomDomain | Addition of a custom domain to a bucket. |
| RemoveCustomDomain | Removal of a custom domain from a bucket. |
| ChangeBucketVisibility | Change to the managed public access (`r2.dev`) settings of a bucket. |
| PutBucketStorageClass | Change to the default storage class of a bucket. |
| PutBucketLifecycleConfiguration | Change to the object lifecycle configuration of a bucket. |
| DeleteBucketLifecycleConfiguration | Deletion of the object lifecycle configuration for a bucket. |
| PutBucketCors | Change to the CORS configuration for a bucket. |
| DeleteBucketCors | Deletion of the CORS configuration for a bucket. |

Note

Logs for data access operations, such as `GetObject` and `PutObject`, are not included in audit logs. To log HTTP requests made to public R2 buckets, use the [HTTP requests](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/http_requests/) Logpush dataset.

## Example log entry

Below is an example of an audit log entry showing the creation of a new bucket:

```json
{
  "action": { "info": "CreateBucket", "result": true, "type": "create" },
  "actor": {
    "email": "<ACTOR_EMAIL>",
    "id": "3f7b730e625b975bc1231234cfbec091",
    "ip": "fe32:43ed:12b5:526::1d2:13",
    "type": "user"
  },
  "id": "5eaeb6be-1234-406a-87ab-1971adc1234c",
  "interface": "API",
  "metadata": { "zone_name": "r2.cloudflarestorage.com" },
  "newValue": "",
  "newValueJson": {},
  "oldValue": "",
  "oldValueJson": {},
  "owner": { "id": "1234d848c0b9e484dfc37ec392b5fa8a" },
  "resource": { "id": "my-bucket", "type": "r2.bucket" },
  "when": "2024-07-15T16:32:52.412Z"
}
```