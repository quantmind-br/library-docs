---
title: Quickstart guide · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/sfu/get-started/index.md
source: llms
fetched_at: 2026-01-24T15:37:07.093404496-03:00
rendered_js: false
word_count: 75
summary: This document provides instructions on how to create a Cloudflare Realtime App and obtain the necessary credentials for API access.
tags:
    - cloudflare-realtime
    - app-setup
    - authentication
    - api-credentials
category: tutorial
---

Before you get started:

You must first [create a Cloudflare account](https://developers.cloudflare.com/fundamentals/account/create-account/).

## Create your first app

Every Realtime App is a separate environment, so you can make one for development, staging and production versions for your product. Either using [Dashboard](https://dash.cloudflare.com/?to=/:account/realtime/sfu), or the [API](https://developers.cloudflare.com/api/resources/calls/subresources/sfu/methods/create/) create a Realtime App. When you create a Realtime App, you will get:

* App ID
* App Secret

These two combined will allow you to make API Realtime from your backend server to Realtime.