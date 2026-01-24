---
title: Remove domain from SaaS provider · Cloudflare for Platforms docs
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/remove-domain/index.md
source: llms
fetched_at: 2026-01-24T15:09:48.974993257-03:00
rendered_js: false
word_count: 93
summary: This document explains how Cloudflare users can disconnect their domains from a SaaS provider by removing the associated DNS records. It describes the impact of record deletion on traffic routing and the resulting status of custom hostnames.
tags:
    - cloudflare-dns
    - saas-integration
    - dns-management
    - custom-hostnames
    - domain-routing
category: guide
---

If your SaaS domain is also a [domain using Cloudflare](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/saas-customers/), you can use your Cloudflare DNS to remove your domain from your SaaS provider.

This means that - if you [remove the DNS records](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#delete-dns-records) pointing to your SaaS provider - Cloudflare will stop routing domain traffic through your SaaS provider and the associated custom hostname will enter a **Moved** state.

This also means that you need to keep DNS records pointing to your SaaS provider for as long as you are a customer. Otherwise, you could accidentally remove your domain from their services.