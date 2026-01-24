---
title: Enable Email Workers · Cloudflare Email Routing docs
url: https://developers.cloudflare.com/email-routing/email-workers/enable-email-workers/index.md
source: llms
fetched_at: 2026-01-24T15:13:44.526911093-03:00
rendered_js: false
word_count: 157
summary: This guide provides step-by-step instructions for enabling Cloudflare Email Workers and configuring email routing, including custom address setup and DNS record verification.
tags:
    - cloudflare-workers
    - email-routing
    - email-workers
    - dns-setup
    - serverless
category: tutorial
---

Follow these steps to enable and add your first Email Worker. If you have never used Cloudflare Workers before, Cloudflare will create a subdomain for you, and assign you to the Workers [free pricing plan](https://developers.cloudflare.com/workers/platform/pricing/).

1. In the Cloudflare dashboard, go to the **Email Routing** page.

   [Go to **Email Routing**](https://dash.cloudflare.com/?to=/:account/:zone/email/routing)

2. Select **Get started**.

3. In **Custom address**, enter the custom email address you want to use (for example, `my-new-email`).

4. In **Destination**, choose the email address or Email Worker you want your emails to be forwarded to — for example, `your-name@gmail.com`. You can only choose a destination address you have already verified. To add a new destination address, refer to [Destination addresses](#destination-addresses).

5. Select **Create and continue**.

6. Verify your destination address and select **Continue**.

7. Configure your DNS records and select **Add records and enable**.

You have successfully created your Email Worker. In the Email Worker’s card, select the **route** field to expand it and check the routes associated with the Worker.