---
title: Test Email Routing · Cloudflare Email Routing docs
url: https://developers.cloudflare.com/email-routing/get-started/test-email-routing/index.md
source: llms
fetched_at: 2026-01-24T15:13:53.474632894-03:00
rendered_js: false
word_count: 114
summary: Explains how to verify that Email Routing is configured correctly by sending a test email from an address different from the destination.
tags:
    - cloudflare-email-routing
    - testing
    - email-configuration
    - troubleshooting
category: guide
---

To test that your configuration is working properly, send an email to the custom address [you set up in the dashboard](https://developers.cloudflare.com/email-routing/get-started/enable-email-routing/). You should send your test email from a different address than the one you specified as the destination address.

For example, if you set up `your-name@gmail.com` as the destination address, do not send your test email from that same Gmail account. Send a test email to that destination address from another email account (for example, `your-name@outlook.com`).

The reason for this is that some email providers will discard what they interpret as an incoming duplicate email and will not show it in your inbox, making it seem like Email Routing is not working properly.