---
title: Overview · Cloudflare Turnstile docs
url: https://developers.cloudflare.com/turnstile/
source: llms
fetched_at: 2026-01-24T15:26:25.237243444-03:00
rendered_js: false
word_count: 279
summary: This document provides an overview of Cloudflare Turnstile, a smart and non-intrusive CAPTCHA alternative that uses browser-based challenges to verify human traffic.
tags:
    - cloudflare-turnstile
    - captcha-alternative
    - bot-protection
    - security-challenges
    - web-accessibility
category: concept
---

Cloudflare's smart CAPTCHA alternative.

Turnstile can be embedded into any website without sending traffic through Cloudflare and works without showing visitors a CAPTCHA.

Cloudflare issues challenges through the [Challenge Platform](https://developers.cloudflare.com/cloudflare-challenges/), which is the same underlying technology powering [Turnstile](https://developers.cloudflare.com/turnstile/).

In contrast to our Challenge page offerings, Turnstile allows you to run challenges anywhere on your site in a less-intrusive way without requiring the use of Cloudflare's CDN.

## How Turnstile works

Turnstile adapts the challenge outcome to the individual visitor or browser. First, we run a series of small non-interactive JavaScript challenges to gather signals about the visitor or browser environment.

These challenges include proof-of-work, proof-of-space, probing for web APIs, and various other challenges for detecting browser-quirks and human behavior. As a result, we can fine-tune the difficulty of the challenge to the specific request and avoid showing a visual or interactive puzzle to a user.

### Widget types

Turnstile [widget types](https://developers.cloudflare.com/turnstile/concepts/widget/) include:

- **Non-interactive**: Visitors never need to interact with the widget.
- **Managed**: Visitors are presented with an interactive checkbox if they are a suspected bot.
- **Invisible**: The widget is completely hidden from the visitor.

* * *

## Accessibility

Turnstile is WCAG 2.1 AA compliant.

* * *

## Features

### Turnstile Analytics

Assess the number of challenges issued, evaluate the [challenge solve rate](https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/), and view the metrics of issued challenges.

### Pre-clearance

Integrate Cloudflare challenges on single-page applications (SPAs) by allowing Turnstile to issue a Pre-Clearance cookie.

* * *

[**Bots**](https://developers.cloudflare.com/bots/)

Cloudflare bot solutions identify and mitigate automated traffic to protect your domain from bad bots.

[**DDoS Protection**](https://developers.cloudflare.com/ddos-protection/)

Detect and mitigate Distributed Denial of Service (DDoS) attacks using Cloudflare's Autonomous Edge.

[**WAF**](https://developers.cloudflare.com/waf/)

Get automatic protection from vulnerabilities and the flexibility to create custom rules.

* * *

## More resources

[Plans](https://developers.cloudflare.com/turnstile/plans/)

Learn more about Turnstile's plan availability.