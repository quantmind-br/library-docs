---
title: Hostname validation · Cloudflare for Platforms docs
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/index.md
source: llms
fetched_at: 2026-01-24T15:10:19.95361365-03:00
rendered_js: false
word_count: 142
summary: This document explains the requirements and methods for verifying customer ownership of custom hostnames within Cloudflare for SaaS. It outlines the differences between pre-validation and real-time validation to help users minimize downtime or simplify the setup process.
tags:
    - cloudflare-for-saas
    - custom-hostnames
    - hostname-validation
    - dns-verification
    - domain-ownership
category: guide
---

Before Cloudflare can proxy traffic through a custom hostname, we need to verify your customer's ownership of that hostname.

Note

If a custom hostname is already on Cloudflare, using the [pre-validation methods](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/) will not shift the traffic to the SaaS zone. That will only happen once the [DNS target](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#3-have-customer-create-cname-record) of the custom hostnames changes to point to the SaaS zone.

## Options

If minimizing downtime is more important to you, refer to our [pre-validation methods](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/).

If ease of use for your customers is more important, review our [real-time validation methods](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/).

## Limitations

Custom hostnames using another CDN are not compatible with Cloudflare for SaaS. Since Cloudflare must be able to validate your customer's ownership of the hostname you add, if their usage of another CDN obfuscates their DNS records, hostname validation will fail.

## Related resources

* [Pre-validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/pre-validation/)
* [Real-time validation](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/realtime-validation/)
* [Backoff schedule](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/backoff-schedule/)
* [Validation status](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/validation-status/)
* [Error codes](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/domain-support/hostname-validation/error-codes/)