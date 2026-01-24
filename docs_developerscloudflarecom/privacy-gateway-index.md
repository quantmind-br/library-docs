---
title: Overview · Cloudflare Privacy Gateway docs
url: https://developers.cloudflare.com/privacy-gateway/index.md
source: llms
fetched_at: 2026-01-24T15:19:48.141903393-03:00
rendered_js: false
word_count: 174
summary: Cloudflare Privacy Gateway is a managed service that implements the Oblivious HTTP standard to protect client privacy by masking IP addresses from application backends.
tags:
    - privacy-gateway
    - oblivious-http
    - ohttp
    - client-privacy
    - network-security
category: concept
---

Implements the Oblivious HTTP IETF standard to improve client privacy.

Enterprise-only

[Privacy Gateway](https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/) is a managed service deployed on Cloudflare’s global network that implements part of the [Oblivious HTTP (OHTTP) IETF](https://www.ietf.org/archive/id/draft-thomson-http-oblivious-01.html) standard. The goal of Privacy Gateway and Oblivious HTTP is to hide the client's IP address when interacting with an application backend.

OHTTP introduces a trusted third party between client and server, called a relay, whose purpose is to forward encrypted requests and responses between client and server. These messages are encrypted between client and server such that the relay learns nothing of the application data, beyond the length of the encrypted message and the server the client is interacting with.

***

## Availability

Privacy Gateway is currently in closed beta – available to select privacy-oriented companies and partners. If you are interested, [contact us](https://www.cloudflare.com/lp/privacy-edge/).

***

## Features

### Get started

Learn how to set up Privacy Gateway for your application.

[Get started](https://developers.cloudflare.com/privacy-gateway/get-started/)

### Legal

Learn about the different parties and data shared in Privacy Gateway.

[Learn more](https://developers.cloudflare.com/privacy-gateway/reference/legal/)

### Metrics

Learn about how to query Privacy Gateway metrics.

[Learn more](https://developers.cloudflare.com/privacy-gateway/reference/metrics/)