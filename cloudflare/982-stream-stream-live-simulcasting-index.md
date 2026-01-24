---
title: Simulcast (restream) videos · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/stream-live/simulcasting/index.md
source: llms
fetched_at: 2026-01-24T15:23:50.737028908-03:00
rendered_js: false
word_count: 315
summary: This document explains how to set up and manage simulcasting for live streams, allowing users to broadcast to multiple third-party platforms simultaneously via API or the Cloudflare dashboard.
tags:
    - simulcasting
    - live-streaming
    - cloudflare-stream
    - rtmp-outputs
    - video-broadcast
    - api-management
category: guide
---

Simulcasting lets you forward your live stream to third-party platforms such as Twitch, YouTube, Facebook, Twitter, and more. You can simulcast to up to 50 concurrent destinations from each live input. To begin simulcasting, select an input and add one or more Outputs.

## Add an Output using the API

Add an Output to start retransmitting live video. You can add or remove Outputs at any time during a broadcast to start and stop retransmitting.

```bash
curl -X POST \
--data '{"url": "rtmp://a.rtmp.youtube.com/live2","streamKey": "<redacted>"}' \
-H "Authorization: Bearer <API_TOKEN>" \
https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/stream/live_inputs/<INPUT_UID>/outputs
```

```json
{
  "result": {
    "uid": "6f8339ed45fe87daa8e7f0fe4e4ef776",
    "url": "rtmp://a.rtmp.youtube.com/live2",
    "streamKey": "<redacted>"
  },
  "success": true,
  "errors": [],
  "messages": []
}
```

## Control when you start and stop simulcasting

You can enable and disable individual live outputs with either:

* The **Live inputs** page of the Cloudflare dashboard.

  [Go to **Live inputs**](https://dash.cloudflare.com/?to=/:account/stream/inputs)

* [The API](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/update/)

This allows you to:

* Start a live stream, but wait to start simulcasting to YouTube and Twitch until right before the content begins.
* Stop simulcasting before the live stream ends, to encourage viewers to transition from a third-party service like YouTube or Twitch to a direct live stream.
* Give your own users manual control over when they go live to specific simulcasting destinations.

When a live output is disabled, video is not simulcast to the live output, even when actively streaming to the corresponding live input.

By default, all live outputs are enabled.

### Enable outputs from the dashboard:

1. In the Cloudflare dashboard, go to the **Live inputs** page.

   [Go to **Live inputs**](https://dash.cloudflare.com/?to=/:account/stream/inputs)

2. Select an input from the list.

3. Under **Outputs** > **Enabled**, set the toggle to enabled or disabled.

## Manage outputs

| Command | Method | Endpoint |
| - | - | - |
| [List outputs](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/list/) | `GET` | `accounts/:account_identifier/stream/live_inputs` |
| [Delete outputs](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/methods/delete/) | `DELETE` | `accounts/:account_identifier/stream/live_inputs/:live_input_identifier` |
| [List All Outputs Associated With A Specified Live Input](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/list/) | `GET` | `/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs` |
| [Delete An Output](https://developers.cloudflare.com/api/resources/stream/subresources/live_inputs/subresources/outputs/methods/delete/) | `DELETE` | `/accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}` |

If the associated live input is already retransmitting to this output when you make the `DELETE` request, that output will be disconnected within 30 seconds.