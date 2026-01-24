---
title: Pricing · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/sfu/pricing/index.md
source: llms
fetched_at: 2026-01-24T15:37:12.663921587-03:00
rendered_js: false
word_count: 164
summary: Explains the billing structure and pricing model for Cloudflare Realtime services, covering egress costs, free tier limits, and specific usage rules for SFU and TURN.
tags:
    - cloudflare-realtime
    - billing
    - pricing
    - sfu
    - turn
    - data-egress
category: reference
---

Cloudflare Realtime billing is based on data sent from Cloudflare edge to your application.

Cloudflare Realtime SFU and TURN services cost $0.05 per GB of data egress.

There is a free tier of 1,000 GB before any charges start. This free tier includes usage from both SFU and TURN services, not two independent free tiers. Cloudflare Realtime billing appears as a single line item on your Cloudflare bill, covering both SFU and TURN.

Traffic between Cloudflare Realtime TURN and Cloudflare Realtime SFU or Cloudflare Stream (WHIP/WHEP) does not get double charged, so if you are using both SFU and TURN at the same time, you will get charged for only one.

### TURN

Please see the [TURN FAQ page](https://developers.cloudflare.com/realtime/turn/faq), where there is additional information on specifically which traffic path from RFC8656 is measured and counts towards billing.

### SFU

Only traffic originating from Cloudflare towards clients incurs charges. Traffic pushed to Cloudflare incurs no charge even if there is no client pulling same traffic from Cloudflare.