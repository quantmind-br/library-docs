---
title: FAQ
url: https://docs.z.ai/help/faq.md
source: llms
fetched_at: 2026-01-24T11:23:32.276093546-03:00
rendered_js: false
word_count: 252
summary: This document addresses frequently asked questions regarding GLM-4.5, including details on its caching mechanism, billing delays, rate limits, and payment troubleshooting.
tags:
    - faq
    - glm-4-5
    - caching
    - billing
    - rate-limits
    - payment-processing
category: other
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.z.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# FAQ

#### How does cache works in GLM-4.5?

The caching mechanism is currently undergoing open beta testing. Therefore, the underlying logic of the caching mechanism (including but not limited to: how cache hits are triggered, how long cached content is retained, etc.) has not yet been announced. A part of your request content may be cached on our cloud platform, and the storage of cached content is currently completely free. During the request process, if your request triggers a cache hit, the cached content will be calculated at 1/5 of the original price.

#### Why hasn’t my account balance changed after I used the API?

* Please be advised that there is currently a processing delay in our billing system. You do not need to worry too much if you see your account balance kept the same after using api port.
* The billing history reflect daily consumption records, and therefore display the billing status from the previous day (n-1).
* Current day consumption will not be immediately visible in the billing details.

#### How can I check the rate limits?

You can check the rate limits from here: [https://z.ai/manage-apikey/rate-limits](https://z.ai/manage-apikey/rate-limits)

#### How should I recharge?

You can recharge from the billing page: [https://z.ai/manage-apikey/billing](https://z.ai/manage-apikey/billing)

#### Why can't I recharge when using credit card?

When using a credit card to recharge, please ensure that you are not using 3DS verification. 3DS verfication is not supported in our platform at this moment.