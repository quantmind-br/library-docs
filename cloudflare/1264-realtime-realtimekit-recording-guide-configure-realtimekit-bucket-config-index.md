---
title: Disable Upload to RealtimeKit Bucket · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/configure-realtimekit-bucket-config/index.md
source: llms
fetched_at: 2026-01-24T15:36:26.457809658-03:00
rendered_js: false
word_count: 134
summary: Explains how to manage recording storage settings in RealtimeKit, specifically how to enable or disable uploads to the default Cloudflare R2 bucket.
tags:
    - realtimekit
    - recording-storage
    - cloudflare-r2
    - storage-configuration
    - api-settings
category: configuration
---

Once the recording is complete, by default, RealtimeKit uploads all recordings to RealtimeKit's Cloudflare R2 bucket. Additionally, a presigned URL is generated with a 7-day expiry. The recording can be accessed using the `downloadUrl` associated with each recording.

However, RealtimeKit provides users with the flexibility to choose whether or not to upload their recordings to RealtimeKit's R2 bucket. If you wish to disable uploads to RealtimeKit's bucket, you can set the `realtimekit_bucket_config` parameter to false in the [Start Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/start_recordings/).

For example:

```json
{
  "realtimekit_bucket_config": {
    "enabled": false
  }
}
```

Note

If you haven't specified an external storage configuration and also disabled uploads to RealtimeKit's bucket, then the recording will not be uploaded to any location. It is considered as an invalid recording.

For more information on how to set your external storage configuration, see [Publish Recorded File to Your Cloud Provider](https://developers.cloudflare.com/realtime/realtimekit/recording-guide/custom-cloud-storage/).