---
title: Deploy a static WordPress site
url: https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/index.md
source: llms
fetched_at: 2026-01-24T15:18:18.012687426-03:00
rendered_js: false
word_count: 475
summary: This guide explains how to convert a WordPress site into static files using the Simply Static plugin and deploy them to Cloudflare Pages using the direct upload method.
tags:
    - cloudflare-pages
    - wordpress
    - static-site-generation
    - deployment-guide
    - simply-static
category: tutorial
---

---
title: Deploy a static WordPress site · Cloudflare Pages docs
description: Learn how to deploy a static WordPress site using Cloudflare Pages.
lastUpdated: 2025-10-09T15:47:46.000Z
chatbotDeprioritize: false
tags: WordPress
source_url:
  html: https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/
  md: https://developers.cloudflare.com/pages/how-to/deploy-a-wordpress-site/index.md
---

## Overview

In this guide, you will use a WordPress plugin, [Simply Static](https://wordpress.org/plugins/simply-static/), to convert your existing WordPress site to a static website deployed with Cloudflare Pages.

## Prerequisites

This guide assumes that you are:

* The Administrator account on your WordPress site.
* Able to install WordPress plugins on the site.

## Setup

To start, install the [Simply Static](https://wordpress.org/plugins/simply-static/) plugin to export your WordPress site. In your WordPress dashboard, go to **Plugins** > **Add New**.

Search for `Simply Static` and confirm that the resulting plugin that you will be installing matches the plugin below.

![Simply Static plugin](https://developers.cloudflare.com/_astro/simply-static.B1STKlmC_ZDt3bU.webp)

Select **Install** on the plugin. After it has finished installing, select **Activate**.

### Export your WordPress site

After you have installed the plugin, go to your WordPress dashboard > **Simply Static** > **GENERATE STATIC FILES**.

In the **Activity Log**, find the **ZIP archive created** message and select **Click here to download** to download your ZIP file.

### Deploy your WordPress site with Pages

With your ZIP file downloaded, deploy your site to Pages:

1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

   [Go to **Workers & Pages**](https://dash.cloudflare.com/?to=/:account/workers-and-pages)

2. Select **Create application** > **Pages** > **Use direct upload**.

3. Name your project, then select **Create project**.

4. Drag and drop your ZIP file (or unzipped folder of assets) or select it from your computer.

5. After your files have been uploaded, select **Deploy site**.

Your WordPress site will now be live on Pages.

Every time you make a change to your WordPress site, you will need to download a new ZIP file from the WordPress dashboard and redeploy to Cloudflare Pages. Automatic updates are not available with the free version of Simply Static.

## Limitations

There are some features available in WordPress sites that will not be supported in a static site environment:

* WordPress Forms.
* WordPress Comments.
* Any links to `/wp-admin` or similar internal WordPress routes.

## Conclusion

By following this guide, you have successfully deployed a static version of your WordPress site to Cloudflare Pages.

With a static version of your site being served, you can:

* Move your WordPress site to a custom domain or subdomain. Refer to [Custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/) to learn more.
* Run your WordPress instance locally, or put your WordPress site behind [Cloudflare Access](https://developers.cloudflare.com/pages/configuration/preview-deployments/#customize-preview-deployments-access) to only give access to your contributors. This has a significant effect on the number of attack vectors for your WordPress site and its content.
* Downgrade your WordPress hosting plan to a cheaper plan. Because the memory and bandwidth requirements for your WordPress instance are now smaller, you can often host it on a cheaper plan, or moving to shared hosting.

Connect with the [Cloudflare Developer community on Discord](https://discord.cloudflare.com) to ask questions and discuss the platform with other developers.