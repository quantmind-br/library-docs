---
title: Configure MTA-STS · Cloudflare Email Routing docs
url: https://developers.cloudflare.com/email-routing/setup/mta-sts/index.md
source: llms
fetched_at: 2026-01-24T15:13:58.638272932-03:00
rendered_js: false
word_count: 361
summary: This guide provides instructions for enabling MTA Strict Transport Security (MTA-STS) on domains using Cloudflare Email Routing to protect against downgrade and man-in-the-middle attacks. It explains how to configure DNS records and use a Cloudflare Worker to serve the required security policy file via HTTPS.
tags:
    - mta-sts
    - email-routing
    - cloudflare-workers
    - smtp-security
    - dns-configuration
    - email-security
category: tutorial
---

MTA Strict Transport Security ([MTA-STS](https://datatracker.ietf.org/doc/html/rfc8461)) was introduced by email service providers including Microsoft, Google and Yahoo as a solution to protect against downgrade and man-in-the-middle attacks in SMTP sessions, as well as solving the lack of security-first communication standards in email.

Suppose that `example.com` is your domain and uses Email Routing. Here is how you can enable MTA-STS for it.

1. In the Cloudflare dashboard, go to the **Records** page.

   [Go to **Records**](https://dash.cloudflare.com/?to=/:account/:zone/dns/records)

2. Create a new CNAME record with the name `_mta-sts` that points to Cloudflare’s record `_mta-sts.mx.cloudflare.net`. Make sure to disable the proxy mode.

![MTA-STS CNAME record](https://developers.cloudflare.com/_astro/mta-sts-record.DbwO-t_X_Z1UxIwF.webp)

1. Confirm that the record was created:

```sh
dig txt _mta-sts.example.com
```

```sh
_mta-sts.example.com. 300 IN  CNAME _mta-sts.mx.cloudflare.net.
_mta-sts.mx.cloudflare.net. 300 IN  TXT "v=STSv1; id=20230615T153000;"
```

This tells the other end client that is trying to connect to us that we support MTA-STS.

Next you need an HTTPS endpoint at `mta-sts.example.com` to serve your policy file. This file defines the mail servers in the domain that use MTA-STS. The reason why HTTPS is used here instead of DNS is because not everyone uses DNSSEC yet, so we want to avoid another MITM attack vector.

To do this you need to deploy a Worker that allows email clients to pull Cloudflare’s Email Routing policy file using the “well-known” URI convention.

1. Go to your **Account** > **Workers & Pages** and select **Create**. Pick the default "Hello World" option button, and replace the sample worker code with the following:

```js
export default {
  async fetch(request, env, ctx) {
    return await fetch(
      "https://mta-sts.mx.cloudflare.net/.well-known/mta-sts.txt",
    );
  },
};
```

This Worker proxies `https://mta-sts.mx.cloudflare.net/.well-known/mta-sts.txt` to your own domain.

1. After deploying it, go to the Worker configuration, then **Settings** > **Domains & Routes** > **+Add**. Type the subdomain `mta-sts.example.com`.

![MTA-STS Worker Custom Domain](https://developers.cloudflare.com/_astro/mta-sts-domain.UfZmAoBe_Z1Vf75K.webp)

You can then confirm that your policy file is working with the following:

```sh
curl https://mta-sts.example.com/.well-known/mta-sts.txt
```

```sh
version: STSv1
mode: enforce
mx: *.mx.cloudflare.net
max_age: 86400
```

This says that you domain `example.com` enforces MTA-STS. Capable email clients will only deliver email to this domain over a secure connection to the specified MX servers. If no secure connection can be established the email will not be delivered.

Email Routing also supports MTA-STS upstream, which greatly improves security when forwarding your Emails to service providers like Gmail, Microsoft, and others.

While enabling MTA-STS involves a few steps today, we aim to simplify things for you and automatically configure MTA-STS for your domains from the Email Routing dashboard as a future improvement.