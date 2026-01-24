---
title: Enable Web Analytics · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/how-to/web-analytics/index.md
source: llms
fetched_at: 2026-01-24T15:18:25.843212738-03:00
rendered_js: false
word_count: 240
summary: This document provides instructions for enabling, viewing, and troubleshooting Cloudflare Web Analytics on a Cloudflare Pages project to monitor site performance and visitor metrics.
tags:
    - cloudflare-pages
    - web-analytics
    - performance-monitoring
    - site-metrics
    - javascript-snippet
category: guide
---

Cloudflare Web Analytics provides free, privacy-first analytics for your website without changing your DNS or using Cloudflare’s proxy. Cloudflare Web Analytics helps you understand the performance of your web pages as experienced by your site visitors.

All you need to enable Cloudflare Web Analytics is a Cloudflare account and a JavaScript snippet on your page to start getting information on page views and visitors. The JavaScript snippet (also known as a beacon) collects metrics using the Performance API, which is available in all major web browsers.

## Enable on Pages project

Cloudflare Pages offers a one-click setup for Web Analytics:

1. In the Cloudflare dashboard, go to the **Workers & Pages** page.

   [Go to **Workers & Pages**](https://dash.cloudflare.com/?to=/:account/workers-and-pages)

2. Select your Pages project.

3. Go to **Metrics** and select **Enable** under Web Analytics.

Cloudflare will automatically add the JavaScript snippet to your Pages site on the next deployment.

## View metrics

To view the metrics associated with your Pages project:

1. In the Cloudflare dashboard, go to the **Web Analytics** page.

   [Go to **Web analytics**](https://dash.cloudflare.com/?to=/:account/web-analytics)

2. Select the analytics associated with your Pages project.

For more details about how to use Web Analytics, refer to the [Web Analytics documentation](https://developers.cloudflare.com/web-analytics/data-metrics/).

## Troubleshooting

For Cloudflare to automatically add the JavaScript snippet, your pages need to have valid HTML.

For example, Cloudflare would not be able to enable Web Analytics on a page like this:

```html
Hello world.
```

For Web Analytics to correctly insert the JavaScript snippet, you would need valid HTML output, such as:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Title</title>
  </head>
  <body>


    <p>Hello world.</p>


  </body>
</html>
```