---
title: Get started · Cloudflare Email Routing docs
url: https://developers.cloudflare.com/email-routing/get-started/index.md
source: llms
fetched_at: 2026-01-24T15:13:52.165393895-03:00
rendered_js: false
word_count: 137
summary: This document provides an overview of how to enable and manage Email Routing, including creating custom email rules for forwarding to destination addresses or workers.
tags:
    - email-routing
    - email-forwarding
    - cloudflare-setup
    - email-rules
    - configuration
category: guide
---

To enable Email Routing, start by creating a custom email address linked to a destination address or Email Worker. This forms an **email rule**. You can enable or disable rules from the Cloudflare dashboard. Refer to [Enable Email Routing](https://developers.cloudflare.com/email-routing/get-started/enable-email-routing) for more details.

Custom addresses you create with Email Routing work as forward addresses only. Emails sent to custom addresses are forwarded by Email Routing to your destination inbox. Cloudflare does not process outbound email, and does not have an SMTP server.

The first time you access Email Routing, you will see a wizard guiding you through the process of creating email rules. You can skip the wizard and add rules manually.

If you need to pause Email Routing or offboard to another service, refer to [Disable Email Routing](https://developers.cloudflare.com/email-routing/setup/disable-email-routing/).

* [Enable Email Routing](https://developers.cloudflare.com/email-routing/get-started/enable-email-routing/)
* [Test Email Routing](https://developers.cloudflare.com/email-routing/get-started/test-email-routing/)
* [Analytics](https://developers.cloudflare.com/email-routing/get-started/email-routing-analytics/)
* [Audit logs](https://developers.cloudflare.com/email-routing/get-started/audit-logs/)