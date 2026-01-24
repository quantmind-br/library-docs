---
title: Workers as your fallback origin · Cloudflare for Platforms docs
url: https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/worker-as-origin/index.md
source: llms
fetched_at: 2026-01-24T15:10:48.292523646-03:00
rendered_js: false
word_count: 315
summary: This document explains how to configure Cloudflare Workers as a fallback origin for SaaS zones and details how custom hostname traffic is routed using specific Worker route patterns.
tags:
    - cloudflare-workers
    - cloudflare-for-saas
    - fallback-origin
    - custom-hostnames
    - routing-rules
    - dns-configuration
category: guide
---

If you are building your application on [Cloudflare Workers](https://developers.cloudflare.com/workers/), you can use a Worker as the origin for your SaaS zone (also known as your fallback origin).

## How custom hostname traffic reaches your Worker

When customers point their domains to your SaaS zone (for example, `mystore.customer.com` CNAMEs to `service.saasprovider.com`), their traffic enters your Cloudflare zone. Any Worker routes configured on your zone will match this incoming traffic.

For example, if you have:

* Your SaaS zone: `saasprovider.com`
* Your fallback origin: `service.saasprovider.com`
* Customer's custom hostname: `mystore.customer.com` (pointed to your zone via CNAME)
* Worker route: `*/*`

When a visitor requests `mystore.customer.com`, Cloudflare routes that request through your zone. The `*/*` route pattern matches all traffic entering your zone, including traffic from custom hostnames like `mystore.customer.com`.

Note

You do not need to add individual Worker routes for each custom hostname. The wildcard route pattern (`*/*`) automatically captures all traffic entering your zone, including traffic from customer vanity domains.

## Set up a Worker as your fallback origin

1. In your SaaS zone, [create and set a fallback origin](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/getting-started/#1-create-fallback-origin). Ensure the fallback origin only has an [originless DNS record](https://developers.cloudflare.com/dns/troubleshooting/faq/#what-ip-should-i-use-for-parked-domain--redirect-only--originless-setup):

   * **Example**: `service.example.com AAAA 100::`

2. In that same zone, navigate to **Workers Routes**.

3. Click **Add route**.

4. Configure a route to send traffic to your Worker. Choose one of the following options based on your needs:

   * **Route all traffic to the Worker** (recommended for most SaaS applications):

     * **Route**: `*/*`
     * **Worker**: Select the Worker used for your SaaS application.

     This pattern routes all traffic entering your zone to the Worker, including requests from custom hostnames (for example, `mystore.customer.com`) and requests to your own subdomains (for example, `app.saasprovider.com`).

   * **Route all but specific routes to worker**:

     * **Route**: `*/*`
     * **Worker**: Select the Worker used for your SaaS application.
     * Add a second route for your zone's own hostnames with **Worker** set to **None** to exclude them.

     For example, if your zone is `saasprovider.com` and you want `api.saasprovider.com` to bypass the Worker, create an additional route `api.saasprovider.com/*` with no Worker assigned. More specific routes take precedence over wildcard routes.

   * **Route only custom hostname traffic to the Worker**:

   * **Route**: `vanity.customer.com`

   * **Worker**: Select the Worker used for your SaaS application.

5. Click **Save**.

***

Zone name restriction

Do not configure a custom hostname which matches the zone name. For example, if your SaaS zone is `example.com`, do not create a custom hostname named `example.com`.

## Related resources

* [Hostname routing](https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/hostname-routing/) - Learn about advanced routing patterns, including dispatch Workers and Orange-to-Orange (O2O) behavior.
* [Workers routes](https://developers.cloudflare.com/workers/configuration/routing/routes/) - Learn more about route pattern matching and validity rules.