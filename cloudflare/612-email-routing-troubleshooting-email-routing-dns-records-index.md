---
title: Troubleshooting misconfigured DNS records · Cloudflare Email Routing docs
url: https://developers.cloudflare.com/email-routing/troubleshooting/email-routing-dns-records/index.md
source: llms
fetched_at: 2026-01-24T15:13:59.342050704-03:00
rendered_js: false
word_count: 118
summary: Explains how to enable Cloudflare Email Routing via the dashboard, including steps for configuring DNS records and troubleshooting SPF issues.
tags:
    - cloudflare
    - email-routing
    - dns-configuration
    - email-security
    - spf-records
category: guide
---

1. In the Cloudflare dashboard, go to the **Email Routing** page.

   [Go to **Email Routing**](https://dash.cloudflare.com/?to=/:account/:zone/email/routing)

2. Go to **Settings**. Email Routing will show you the status of your DNS records, such as `Missing`.

3. Select **Enable Email Routing**.

4. The next page will show you what kind of action is needed. For example, if you are missing DNS records, select **Add records and enable**.

If there is a problem with your SPF records, refer to [Troubleshooting SPF records](https://developers.cloudflare.com/email-routing/troubleshooting/email-routing-spf-records/).

Note

If you are not using Email Routing but notice an Email Routing DNS record in your zone that you cannot delete, you can use the [Disable Email Routing API call](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/delete/). It will remove any unexpected records, such as DKIM TXT records like `cf2024-1._domainkey.<hostname>`.