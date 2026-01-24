---
title: End a session · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/core/end-a-session/index.md
source: llms
fetched_at: 2026-01-24T15:36:08.292427504-03:00
rendered_js: false
word_count: 302
summary: This document explains how to end a Cloudflare RealtimeKit session by removing all participants and provides instructions for permanently disabling a meeting via backend APIs.
tags:
    - realtimekit
    - session-management
    - cloudflare-api
    - webhooks
    - meeting-control
category: guide
---

Prerequisites

Ensure your participant's preset has the **Kick Participants** (`kick_participant`) host permission enabled.

To end the current [session](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/#session/) for all participants, remove all participants using `kickAll()`. This stops any ongoing recording for that session and sets the session status to `ENDED`.

Ending a session is different from leaving a meeting. Leaving disconnects only the current participant. The session remains active if other participants are still present.

## Steps

1. Check that the local participant has permission to remove participants.

2. End the session by removing all participants.

3. Listen for the session end event.

You can also end a session from your backend by removing all participants using the [Kick all participants](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/kick_all_participants/) API.

## End a session from your backend

### Remove all participants with the API

Use the [Kick all participants](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/active-session/methods/kick_all_participants/) API method to remove all participants from an active session for a meeting.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

* `Realtime Admin`
* `Realtime`

```bash
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings/$MEETING_ID/active-session/kick-all" \
  --request POST \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN"
```

### Listen for session end events with webhooks

Register a webhook that subscribes to `meeting.ended`. RealtimeKit sends this event when the session ends. You can use it to trigger backend workflows, such as sending a notification, generating a report, or updating session records in your database.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

* `Realtime Admin`
* `Realtime`

```bash
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/webhooks" \
  --request POST \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --json '{
    "name": "Session ended webhook",
    "url": "<YOUR_WEBHOOK_URL>",
    "events": [
        "meeting.ended"
    ]
  }'
```

## Disable a meeting

Ending a session does not disable the meeting. Participants can join the meeting again and start a new session. To prevent participants from joining again and starting a new session, set the meeting status to `INACTIVE` using the [Update a meeting](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/update_meeting_by_id/) API.

Required API token permissions

At least one of the following [token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) is required:

* `Realtime Admin`
* `Realtime`

```bash
curl "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/realtime/kit/$APP_ID/meetings/$MEETING_ID" \
  --request PATCH \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --json '{
    "status": "INACTIVE"
  }'
```

## Next steps

* Review how presets control permissions in [Preset](https://developers.cloudflare.com/realtime/realtimekit/concepts/preset/).
* Review the possible values of the local participant room state in [Local Participant](https://developers.cloudflare.com/realtime/realtimekit/core/local-participant/#state-properties/).