---
title: Overview · Cloudflare Email Routing docs
url: https://developers.cloudflare.com/email-routing/index.md
source: llms
fetched_at: 2026-01-24T15:13:38.575838034-03:00
rendered_js: false
word_count: 242
summary: This document introduces Cloudflare Email Routing, a service that allows users to create custom email addresses and route incoming mail to a primary inbox for improved privacy and management.
tags:
    - email-routing
    - cloudflare-workers
    - custom-email
    - privacy
    - dns-setup
    - email-security
category: concept
---

Create custom email addresses for your domain and route incoming emails to your preferred mailbox.

Available on all plans

Cloudflare Email Routing is designed to simplify the way you create and manage email addresses, without needing to keep an eye on additional mailboxes. With Email Routing, you can create any number of custom email addresses to use in situations where you do not want to share your primary email address, such as when you subscribe to a new service or newsletter. Emails are then routed to your preferred email inbox, without you ever having to expose your primary email address.

Email Routing is free and private by design. Cloudflare will not store or access the emails routed to your inbox.

It is available to all Cloudflare customers [using Cloudflare as an authoritative nameserver](https://developers.cloudflare.com/dns/zone-setups/full-setup/).

***

## Features

### Email Workers

Leverage the power of Cloudflare Workers to implement any logic you need to process your emails. Create rules as complex or simple as you need.

[Use Email Workers](https://developers.cloudflare.com/email-routing/email-workers/)

### Custom addresses

With Email Routing you can have many custom email addresses to use for specific situations.

[Use Custom addresses](https://developers.cloudflare.com/email-routing/get-started/enable-email-routing/)

### Analytics

Email Routing includes metrics to help you check on your email traffic history.

[Use Analytics](https://developers.cloudflare.com/email-routing/get-started/email-routing-analytics/)

***

## Related products

**[Email security](https://developers.cloudflare.com/cloudflare-one/email-security/)**

Cloudflare Email security is a cloud based service that stops phishing attacks, the biggest cybersecurity threat, across all traffic vectors - email, web and network.

**[DNS](https://developers.cloudflare.com/dns/)**

Email Routing is available to customers using Cloudflare as an authoritative nameserver.