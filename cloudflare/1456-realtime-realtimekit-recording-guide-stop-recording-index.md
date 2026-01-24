---
title: Stop Recording · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/stop-recording/index.md
source: llms
fetched_at: 2026-01-24T15:36:35.124423957-03:00
rendered_js: false
word_count: 157
summary: 'This document outlines the three methods for stopping RealtimeKit recordings: automatic termination due to inactivity or duration limits, and manual termination via the API.'
tags:
    - realtimekit
    - recording-management
    - automatic-stop
    - api-control
    - recording-states
category: guide
---

RealtimeKit recordings can be stopped in any of the following ways:

1. **Automatic Stop (Empty meeting)**: A RealtimeKit recording will automatically stop if the meeting has no participants for a duration of 1 minute or more. This wait time can be customized by contacting RealtimeKit's support team to configure a custom value for your app.
2. **Automatic Stop (maxSeconds elapsed)**: A recording will automatically stop when it reaches the duration specified by the `max_seconds` parameter passed while starting the recording, regardless of whether participants are present in the meeting. If this parameter is not passed, it defaults to 24 hours (86400 seconds).
3. **Using Stop Recording API**: A recording can also be stopped by passing the recording ID and `stop` action to the [Stop Recording API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/).

When a recording is stopped, it transitions to the `UPLOADING` state and then to the `UPLOADED` state after it has been transferred to RealtimeKit's storage and any external storage that has been set up.