---
title: Add a custom domain to a branch · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/how-to/custom-branch-aliases/index.md
source: llms
fetched_at: 2026-01-24T15:18:17.626400591-03:00
rendered_js: false
word_count: 269
summary: This guide explains how to map a custom domain to a specific branch of a Cloudflare Pages project by configuring branch aliases and proxied DNS records.
tags:
    - cloudflare-pages
    - custom-domains
    - branch-aliases
    - dns-configuration
    - deployment
category: guide
---

In this guide, you will learn how to add a custom domain (`staging.example.com`) that will point to a specific branch (`staging`) on your Pages project.

This will allow you to have a custom domain that will always show the latest build for a specific branch on your Pages project.

Note

This setup is only supported when using a proxied Cloudflare DNS record.

If you attempt to follow this guide using an external DNS provider or an unproxied DNS record, your custom alias will be sent to the production branch of your Pages project.

First, make sure that you have a successful deployment on the branch you would like to set up a custom domain for.

Next, add a custom domain under your Pages project for your desired custom domain, for example, `staging.example.com`.

![Follow the instructions below to access the custom domains overview in the Pages dashboard.](https://developers.cloudflare.com/_astro/pages_custom_domain-1.CiOZm32-_1hDrtY.webp)

To do this:

1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

   [Go to **Workers & Pages**](https://dash.cloudflare.com/?to=/:account/workers-and-pages)

2. Select your Pages project.

3. Select **Custom domains** > **Setup a custom domain**.

4. Input the domain you would like to use, such as `staging.example.com`

5. Select **Continue** > **Activate domain**

![After selecting your custom domain, you will be asked to activate it.](https://developers.cloudflare.com/_astro/pages_custom_domain-2.BTtd80-v_Z2tx6JW.webp)

After activating your custom domain, go to [DNS](https://dash.cloudflare.com/?to=/:account/:zone/dns) for the `example.com` zone and find the `CNAME` record with the name `staging` and change the target to include your branch alias.

In this instance, change `your-project.pages.dev` to `staging.your-project.pages.dev`.

![After activating your custom domain, change the CNAME target to include your branch name.](https://developers.cloudflare.com/_astro/pages_custom_domain-3.DhnYG8VS_Z2cp0T8.webp)

Now the `staging` branch of your Pages project will be available on `staging.example.com`.