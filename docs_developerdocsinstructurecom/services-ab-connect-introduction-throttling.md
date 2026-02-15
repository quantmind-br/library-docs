---
title: Call Throttling | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/ab-connect/introduction/throttling
source: sitemap
fetched_at: 2026-02-15T09:04:04.353071-03:00
rendered_js: false
word_count: 296
summary: This document explains the API rate limiting and payload size constraints for AB Connect, describing the token bucket model used to manage call frequency and system performance.
tags:
    - api-throttling
    - rate-limiting
    - token-bucket
    - ab-connect
    - payload-constraints
    - http-429
category: reference
---

As adoption of AB Connect increases, We need to ensure all partners have an optimal integration experience. In order to achieve this goal, API controls limit call frequency and payload sizes. Payload sizes have been constrained with a cap on the `limit` for a page (see [Paging Data](https://developerdocs.instructure.com/services/ab-connect/introduction/paging) for details on payload constraints). The remainder of this section describes call throttling also known as rate limiting.

To ensure one client can not adversely affect another client's system performance rate limiting has been implemented on a per account basis. The rate limiting uses a [token bucket model backed by Amazon's API Gatewayarrow-up-right](https://aws.amazon.com/blogs/aws/new-usage-plans-for-amazon-api-gateway/). In summary, each account has a bucket. The system adds 5 tokens to an account's bucket every second and the bucket can hold up to 25 tokens. Each API call an account makes removes one token from the bucket. If you have not made any calls for a period of time and your bucket is full, you can make a burst of up to 25 calls. However, once your bucket is empty, you'll need to wait before making another call or you'll receive an HTTP 429 response.

Some accounts may have different limits and it is possible that these thresholds change over time, so it is recommended that implementation of a client-side throttling solution that is either self-adjusting or is easy to adjust manually. Depending on the client side architecture and implementation language, there may be client side throttling frameworks available that handle the complexity for your system.

If you have a particular need for a larger bucket size or bucket fill rate, contact [AB Supportenvelope](mailto:absupport@instructure.com?subject=AB%20Connect%20Token%20Bucket) for additional plans.

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).