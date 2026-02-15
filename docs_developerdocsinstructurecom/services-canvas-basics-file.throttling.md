---
title: Throttling | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/basics/file.throttling
source: sitemap
fetched_at: 2026-02-15T08:58:16.676235-03:00
rendered_js: false
word_count: 315
summary: This document describes the dynamic throttling mechanism used by Canvas LMS to manage API request volume and explains how to interpret rate-limit headers and handle error responses.
tags:
    - rate-limiting
    - api-throttling
    - canvas-lms
    - http-headers
    - error-handling
    - quota-management
category: concept
---

Canvas includes a built in dynamic throttling mechanism to prevent a single user from abusing the system and causing adverse effects for others. It works by having a rate limit, and a cost for every request. Each request subtracts from your quota, and the quota is automatically replenished over time. In the event that your API request is throttled, you will receive a `429 Forbidden (Rate Limit Exceeded)` response. Your application should be prepared for this error, and retry the request at a later time.

To assist applications with planning, every request will return a `X-Request-Cost` header that is a floating point number of the amount that request deducted from your remaining quota. If throttling is applicable to this request, there will also be a `X-Rate-Limit-Remaining` header of your remaining quota.

Since the cost of a request is roughly based on the amount of time it takes to process, and the quota (by default) replenishes at a rate faster than real-time, any API client that makes no more than one simultaneous request is unlikely to be throttled. Parallel requests are subject to an additional pre-flight penalty to prevent a large number of incoming requests being able to bring the system down before their cost is counted against their quota. As soon as each request finishes, the pre-flight penalty is credited back to the quota, and only the actual cost of the request is counted.

For applications that go through the OAuth flow and obtain an access token for each user, each access token has its own quota, and the developer need not be concerned with requests from one user causing another user to be throttled.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 2 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).