---
title: Quickstart · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/quickstart/index.md
source: llms
fetched_at: 2026-01-24T15:35:49.735107991-03:00
rendered_js: false
word_count: 289
summary: This document provides a step-by-step guide for setting up Cloudflare RealtimeKit, covering API authentication, application creation, and meeting participant management.
tags:
    - cloudflare-realtimekit
    - api-token
    - meeting-management
    - participant-presets
    - real-time-integration
category: tutorial
---

### Prerequisites

To integrate RealtimeKit in your application, you must have a [Cloudflare account](https://dash.cloudflare.com).

1. Follow the [Create API token guide](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) to create a new token via the [Cloudflare dashboard](https://dash.cloudflare.com/profile/api-tokens).
2. When configuring permissions, ensure that **Realtime** / **Realtime Admin** permissions are selected.
3. Configure any additional [access policies and restrictions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/) as needed for your use case.

*Optional:* Alternatively, [create tokens programmatically via the API](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/). Please ensure your access policy includes the **Realtime** permission.

### Installation

Select a framework based on the platform you are building for.

### Create a RealtimeKit App

You can create an application from the [Cloudflare Dashboard](https://dash.cloudflare.com/?to=/:account/realtime/kit), by clicking on Create App.

*Optional:* You can also use our [API reference](https://developers.cloudflare.com/api/resources/realtime_kit/) for creating an application:

```bash
curl --location 'https://api.cloudflare.com/client/v4/accounts/<account_id>/realtime/kit/apps' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <api_token>' \
--data '{"name": "My First Cloudflare RealtimeKit app"}'
```

> **Note:** We recommend creating different apps for staging and production environments.

### Create a Meeting

Use our [Meetings API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/create/) to create a meeting. We will use the **ID from the response** in subsequent steps.

```bash
curl --location 'https://api.cloudflare.com/client/v4/accounts/<account_id>/realtime/kit/<app_id>/meetings' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <api_token>' \
--data '{"title": "My First Cloudflare RealtimeKit meeting"}'
```

### Add Participants

#### Create a Preset

Presets define what permissions a user should have. Learn more in the Concepts guide. You can create new presets using the [Presets API](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/presets/methods/create/) or via the [RealtimeKit dashboard](https://dash.cloudflare.com/?to=/:account/realtime/kit).

> **Note:** Skip this step if you created the app in the dashboard—default presets are already set up for you.

> **Note:** Presets can be reused across multiple meetings. Define a role (for example, admin or viewer) once and apply it to participants in any number of meetings.

#### Add a Participant

A participant is added to a meeting using the `Meeting ID` created above and selecting a `Preset Name` from the available options.

The response includes an `authToken` which the **Client SDK uses to add this participant to the meeting** room.

```bash
curl --location 'https://api.cloudflare.com/client/v4/accounts/<account_id>/realtime/kit/<app_id>/meetings/<meeting_id>/participants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <api_token>' \
--data '{
  "name": "Mary Sue",
  "preset_name": "<preset_name>",
  "custom_participant_id": "<uuid_of_the_user_in_your_system>"
}'
```

Learn more about adding participants in the [API reference](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/meetings/methods/add_participant/).

### Frontend Integration

You can now add the RealtimeKit Client SDK to your application.