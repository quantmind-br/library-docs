---
title: Custom TURN domains · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/turn/custom-domains/index.md
source: llms
fetched_at: 2026-01-24T15:37:19.469756961-03:00
rendered_js: false
word_count: 209
summary: This document explains how to configure custom domains for Cloudflare Realtime TURN via CNAME records and outlines protocol support for UDP and TCP.
tags:
    - cloudflare
    - turn-service
    - custom-domains
    - dns-configuration
    - networking
    - cname-records
category: configuration
---

Cloudflare Realtime TURN service supports using custom domains for UDP, and TCP - but not TLS protocols. Custom domains do not affect any of the performance of Cloudflare Realtime TURN and is set up via a simple CNAME DNS record on your domain.

| Protocol | Custom domains | Primary port | Alternate port |
| - | - | - | - |
| STUN over UDP | ✅ | 3478/udp | 53/udp |
| TURN over UDP | ✅ | 3478/udp | 53 udp |
| TURN over TCP | ✅ | 3478/tcp | 80/tcp |
| TURN over TLS | No | 5349/tcp | 443/tcp |

## Setting up a CNAME record

To use custom domains for TURN, you must create a CNAME DNS record pointing to `turn.cloudflare.com`.

Warning

Do not resolve the address of `turn.cloudflare.com` or `stun.cloudflare.com` or use an IP address as the value you input to your DNS record. Only CNAME records are supported.

Any DNS provider, including Cloudflare DNS can be used to set up a CNAME for custom domains.

Note

If Cloudflare's authoritative DNS service is used, the record must be set to [DNS-only or "grey cloud" mode](https://developers.cloudflare.com/dns/proxy-status/#dns-only-records).\`

There is no additional charge to using a custom hostname with Cloudflare Realtime TURN.