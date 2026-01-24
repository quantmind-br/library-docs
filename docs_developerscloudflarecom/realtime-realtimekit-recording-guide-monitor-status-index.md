---
title: Monitor Recording Status · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/recording-guide/monitor-status/index.md
source: llms
fetched_at: 2026-01-24T15:36:32.541304018-03:00
rendered_js: false
word_count: 265
summary: This document outlines the lifecycle states of a meeting recording and describes how to monitor these transitions using webhooks and REST APIs.
tags:
    - recording-states
    - realtime-kit
    - webhooks
    - api-integration
    - status-tracking
category: reference
---

## Recording states

The recording of a meeting can have the following states:

| Name | Description |
| - | - |
| INVOKED | Our backend servers have received the recording request, and the master is looking for a ready worker to assign the recording job. |
| RECORDING | The meeting is currently being recorded by a worker; note that this will also hold true if the meeting is being live streamed. |
| UPLOADING | The recording has been stopped and the file is being uploaded to the cloud storage. If you have not specified storage details, then the files will be uploaded only to RealtimeKit's server. Any RTMP and livestreaming link will also stop at this stage. |
| UPLOADED | The recording file upload is complete and the status webhook is also triggered. |
| ERRORED | There was an irrecoverable error while recording the meeting and the file will not be available. |

## Fetching the state

There are two ways you can track what state a recording is in or view more details about a recording:

### Using the `recording.statusUpdate` webhook

RealtimeKit sends out a `recording.statusUpdate` webhook each time the recording transitions between states during its lifecycle. Configure webhooks in your RealtimeKit app to receive these notifications.

### By polling HTTP APIs

Alternatively, you can also use the following APIs:

* [List recordings](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_recordings/): This endpoint gets all past and ongoing recordings linked to a meeting.
* [Fetch active recording](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_active_recordings/): This endpoint gets all ongoing recordings of a meeting.
* [Fetch details of a recording](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/recordings/methods/get_one_recording/): This endpoint gets a specific recording using a recording ID.