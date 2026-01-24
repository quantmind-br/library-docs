---
title: Manage gateways · Cloudflare AI Gateway docs
url: https://developers.cloudflare.com/ai-gateway/configuration/manage-gateway/index.md
source: llms
fetched_at: 2026-01-24T14:01:40.57780575-03:00
rendered_js: false
word_count: 221
summary: This document provides instructions for managing AI Gateways through the Cloudflare dashboard and API, covering creation, modification, and deletion processes.
tags:
    - ai-gateway
    - cloudflare
    - gateway-management
    - api-token
    - dashboard-settings
    - resource-management
category: guide
---

You have several different options for managing an AI Gateway.

## Create gateway

* Dashboard

  [Go to **AI Gateway**](https://dash.cloudflare.com/?to=/:account/ai/ai-gateway)

  1. Log into the [Cloudflare dashboard](https://dash.cloudflare.com/) and select your account.
  2. Go to **AI** > **AI Gateway**.
  3. Select **Create Gateway**.
  4. Enter your **Gateway name**. Note: Gateway name has a 64 character limit.
  5. Select **Create**.

* API

  To set up an AI Gateway using the API:

  1. [Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with the following permissions:

     * `AI Gateway - Read`
     * `AI Gateway - Edit`

  2. Get your [Account ID](https://developers.cloudflare.com/fundamentals/account/find-account-and-zone-ids/).

  3. Using that API token and Account ID, send a [`POST` request](https://developers.cloudflare.com/api/resources/ai_gateway/methods/create/) to the Cloudflare API.

## Edit gateway

* Dashboard

  To edit an AI Gateway in the dashboard:

  1. Log into the [Cloudflare dashboard](https://dash.cloudflare.com/) and select your account.
  2. Go to **AI** > **AI Gateway**.
  3. Select your gateway.
  4. Go to **Settings** and update as needed.

* API

  To edit an AI Gateway, send a [`PUT` request](https://developers.cloudflare.com/api/resources/ai_gateway/methods/update/) to the Cloudflare API.

Note

For more details about what settings are available for editing, refer to [Configuration](https://developers.cloudflare.com/ai-gateway/configuration/).

## Delete gateway

Deleting your gateway is permanent and can not be undone.

* Dashboard

  To delete an AI Gateway in the dashboard:

  1. Log into the [Cloudflare dashboard](https://dash.cloudflare.com/) and select your account.
  2. Go to **AI** > **AI Gateway**.
  3. Select your gateway from the list of available options.
  4. Go to **Settings**.
  5. For **Delete Gateway**, select **Delete** (and confirm your deletion).

* API

  To delete an AI Gateway, send a [`DELETE` request](https://developers.cloudflare.com/api/resources/ai_gateway/methods/delete/) to the Cloudflare API.