---
title: Product compatibility · Cloudflare Privacy Gateway docs
url: https://developers.cloudflare.com/privacy-gateway/reference/product-compatibility/index.md
source: llms
fetched_at: 2026-01-24T15:19:53.814585135-03:00
rendered_js: false
word_count: 76
summary: This document outlines the compatibility limitations of various Cloudflare products when used alongside Privacy Gateway, explaining why certain features are unsupported due to end-to-end encryption.
tags:
    - privacy-gateway
    - cloudflare-compatibility
    - api-shield
    - caching
    - waf
    - encryption
    - limitations
category: reference
---

When [using Privacy Gateway](https://developers.cloudflare.com/privacy-gateway/get-started/), the majority of Cloudflare products will be compatible with your application.

However, the following products are not compatible:

* [API Shield](https://developers.cloudflare.com/api-shield/): [Schema Validation](https://developers.cloudflare.com/api-shield/security/schema-validation/) and [API discovery](https://developers.cloudflare.com/api-shield/security/api-discovery/) are not possible since Cloudflare cannot see the request URLs.
* [Cache](https://developers.cloudflare.com/cache/): Caching of application content is no longer possible since each between client and gateway is end-to-end encrypted.
* [WAF](https://developers.cloudflare.com/waf/): Rules implemented based on request content are not supported since Cloudflare cannot see the request or response content.