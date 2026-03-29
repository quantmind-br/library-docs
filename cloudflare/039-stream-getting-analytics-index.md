---
title: Analytics · Cloudflare Stream docs
url: https://developers.cloudflare.com/stream/getting-analytics/index.md
source: llms
fetched_at: 2026-01-24T15:23:24.51001955-03:00
rendered_js: false
word_count: 79
summary: This document outlines the capabilities and access methods for Cloudflare Stream's server-side analytics, including usage tracking via the dashboard and GraphQL API.
tags:
    - cloudflare-stream
    - video-analytics
    - graphql-api
    - server-side-analytics
    - usage-metrics
category: concept
---

Stream provides server-side analytics that can be used to:

* Identify most viewed video content in your app or platform.
* Identify where content is viewed from and when it is viewed.
* Understand which creators on your platform are publishing the most viewed content, and analyze trends.

You can access data on either:

* The Stream **Analytics** page of the Cloudflare dashboard.

  [Go to **Analytics**](https://dash.cloudflare.com/?to=/:account/stream/analytics)

* The [GraphQL Analytics API](https://developers.cloudflare.com/stream/getting-analytics/fetching-bulk-analytics).

Users will need the **Analytics** permission to access analytics via Dash or GraphQL.