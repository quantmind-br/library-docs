---
title: Cache for SaaS · Cloudflare for Platforms docs
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/performance/cache-for-saas/index.md
source: llms
fetched_at: 2026-01-24T15:09:28.998666888-03:00
rendered_js: false
word_count: 96
summary: Explains how Cloudflare improves website performance for SaaS providers by caching static and dynamic content across globally distributed data centers.
tags:
    - cloudflare
    - caching
    - saas
    - latency-reduction
    - content-delivery
category: concept
---

Cloudflare makes customer websites faster by storing a copy of the website’s content on the servers of our globally distributed data centers. Content can be either static or dynamic: static content is “cacheable” or eligible for caching, and dynamic content is “uncacheable” or ineligible for caching. The cached copies of content are stored physically closer to users, optimized to be fast, and do not require recomputing.

As a SaaS provider, enabling caching reduces latency on your custom domains. For more information, refer to [Cache](https://developers.cloudflare.com/cache/). If you would like to enable caching, review [Getting Started with Cache](https://developers.cloudflare.com/cache/get-started/).