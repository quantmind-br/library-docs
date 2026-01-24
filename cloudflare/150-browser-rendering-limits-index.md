---
title: Limits · Cloudflare Browser Rendering docs
url: https://developers.cloudflare.com/browser-rendering/limits/index.md
source: llms
fetched_at: 2026-01-24T15:08:35.427567578-03:00
rendered_js: false
word_count: 1286
summary: This document outlines the usage limits, concurrency constraints, and troubleshooting procedures for Cloudflare Workers Browser Rendering across Free and Paid plans.
tags:
    - cloudflare-workers
    - browser-rendering
    - usage-limits
    - concurrency
    - rate-limiting
    - error-handling
category: reference
---

Available on Free and Paid plans

## Workers Free

Users on the [Workers Free plan](https://developers.cloudflare.com/workers/platform/pricing/) are limited to **10 minutes of browser rendering usage per day**.

To increase this limit, go to the **Compute (Workers) > Workers plans** page in the Cloudflare dashboard:

[Go to **Workers plans**](https://dash.cloudflare.com/?to=/:account/workers/plans)

[Learn more about Workers Plans](https://developers.cloudflare.com/workers/platform/pricing).

| Feature | Limit |
| - | - |
| Concurrent browsers per account (Workers Bindings only) | 3 per account |
| New browser instances per minute (Workers Bindings only) | 3 per minute |
| Browser timeout | 60 seconds |
| Total requests per min (REST API only) | 6 per minute [1](#user-content-fn-1) |

Note on browser timeout

By default, a browser will time out if it does not get any [devtools](https://chromedevtools.github.io/devtools-protocol/) command for 60 seconds, freeing one instance. Users can optionally increase this by using the [`keep_alive` option](https://developers.cloudflare.com/browser-rendering/puppeteer/#keep-alive). `browser.close()` releases the browser instance.

## Workers Paid

Higher limit requests

The limits for Browser Rendering will continue to be raised over time. In the meantime, Cloudflare will grant [requests for higher limits](https://forms.gle/CdueDKvb26mTaepa9) on a case-by-case basis if a need for a higher limit can be clearly demonstrated.

| Feature | Limit |
| - | - |
| Concurrent browsers per account (Workers Bindings only) | 30 per account [2](#user-content-fn-2) |
| New browser instances per minute (Workers Bindings only) | 30 per minute [2](#user-content-fn-2) |
| Browser timeout | 60 seconds |
| Total requests per min (REST API only) | 180 per minute [2](#user-content-fn-2)[3](#user-content-fn-3) |

Note on browser timeout

By default, a browser will time out if it does not get any [devtools](https://chromedevtools.github.io/devtools-protocol/) command for 60 seconds, freeing one instance. Users can optionally increase this by using the [`keep_alive` option](https://developers.cloudflare.com/browser-rendering/puppeteer/#keep-alive). `browser.close()` releases the browser instance.

## Note on concurrency

While the limits above define the maximum number of concurrent browser sessions per account, in practice you may not need to hit these limits. Browser sessions close automatically—by default, after 60 seconds of inactivity or upon task completion—so if each session finishes its work before a new request comes in, the effective concurrency is lower. This means that most workflows do not require very high concurrent browser limits.

## Limits FAQ & troubleshooting

To upgrade, go to the **Compute (Workers) > Workers plans** page in the Cloudflare dashboard:

[Go to **Workers plans**](https://dash.cloudflare.com/?to=/:account/workers/plans)

### How can I manage concurrency and session isolation with Browser Rendering?

If you are hitting concurrency [limits](https://developers.cloudflare.com/browser-rendering/limits/#workers-paid), or want to optimize concurrent browser usage with the [Workers Binding method](https://developers.cloudflare.com/browser-rendering/workers-bindings/), here are a few tips:

* Optimize with tabs or shared browsers: Instead of launching a new browser for each task, consider opening multiple tabs or running multiple actions within the same browser instance.
* [Reuse sessions](https://developers.cloudflare.com/browser-rendering/workers-bindings/reuse-sessions/): You can optimize your setup and decrease startup time by reusing sessions instead of launching a new browser every time. If you are concerned about maintaining test isolation (for example, for tests that depend on a clean environment), we recommend using [incognito browser contexts](https://pptr.dev/api/puppeteer.browser.createbrowsercontext), which isolate cookies and cache with other sessions.

If you are still running into concurrency limits you can [request a higher limit](https://forms.gle/CdueDKvb26mTaepa9).

### Can I increase the browser timeout?

By default, a browser instance will time out after 60 seconds of inactivity. If you want to keep the browser open longer, you can use the [`keep_alive` option](https://developers.cloudflare.com/browser-rendering/puppeteer/#keep-alive), which allows you to extend the timeout to up to 10 minutes.

### Is there a maximum session duration?

There is no fixed maximum lifetime for a browser session as long as it remains active. By default, Browser Rendering closes sessions after one minute of inactivity to prevent unintended usage. You can [increase this inactivity timeout](https://developers.cloudflare.com/browser-rendering/puppeteer/#keep-alive) to up to 10 minutes.

If you need sessions to remain open longer, keep them active by sending a command at least once within your configured inactivity window (for example, every 10 minutes). Sessions also close when Browser Rendering rolls out a new release.

### I upgraded from the Workers Free plan, but I'm still hitting the 10-minute per day limit. What should I do?

If you recently upgraded to the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/) but still encounter the 10-minute per day limit, redeploy your Worker to ensure your usage is correctly associated with the new plan.

### Why is my browser usage higher than expected?

If you are hitting the daily limit or seeing higher usage than expected, the most common cause is browser sessions that are not being closed properly. When a browser session is not explicitly closed with `browser.close()`, it remains open and continues to consume browser time until it times out (60 seconds by default, or up to 10 minutes if you use the `keep_alive` option).

To minimize usage:

* Always call `browser.close()` when you are finished with a browser session.
* Wrap your browser code in a `try/finally` block to ensure `browser.close()` is called even if an error occurs.
* Use [`puppeteer.history()`](https://developers.cloudflare.com/browser-rendering/puppeteer/#list-recent-sessions) or [`playwright.history()`](https://developers.cloudflare.com/browser-rendering/playwright/#list-recent-sessions) to review recent sessions and identify any that closed due to `BrowserIdle` instead of `NormalClosure`. Sessions that close due to idle timeout indicate the browser was not closed explicitly.

You can monitor your usage and view session close reasons in the Cloudflare dashboard on the **Browser Rendering** page:

[Go to **Browser Rendering**](https://dash.cloudflare.com/?to=/:account/workers/browser-rendering)

Refer to [Browser close reasons](https://developers.cloudflare.com/browser-rendering/reference/browser-close-reasons/) for more information.

### Error: `429 Too many requests`

When you make too many requests in a short period of time, Browser Rendering will respond with HTTP status code `429 Too many requests`. The response includes a `Retry-After` header, which specifies how many seconds to wait before retrying. You can view your account's rate limits in the [Workers Free](#workers-free) and [Workers Paid](#workers-paid) sections above.

Rate limits are enforced with a fixed per-second fill rate. For example, a limit of 180 requests per minute translates to three requests per second. You cannot send all requests at once; the API expects them to be spread evenly over the minute.

The example below demonstrates how to handle rate limiting gracefully by reading the `Retry-After` value and retrying the request after that delay.

* REST API

  ```js
  const response = await fetch('https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/content', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer <your-token>',
      },
      body: JSON.stringify({ url: 'https://example.com' })
  });


  if (response.status === 429) {
      const retryAfter = response.headers.get('Retry-After');
      console.log(`Rate limited. Waiting ${retryAfter} seconds...`);
      await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));


      // Retry the request
      const retryResponse = await fetch(/* same request as above */);
  }
  ```

* Workers Bindings

  ```js
  import puppeteer from "@cloudflare/puppeteer";


  try {
    const browser = await puppeteer.launch(env.MYBROWSER);


    const page = await browser.newPage();
    await page.goto("https://example.com");
    const content = await page.content();


    await browser.close();
  } catch (error) {
    if (error.status === 429) {
      const retryAfter = error.headers.get("Retry-After");
      console.log(
        `Browser instance limit reached. Waiting ${retryAfter} seconds...`,
      );
      await new Promise((resolve) => setTimeout(resolve, retryAfter * 1000));


      // Retry launching browser
      const browser = await puppeteer.launch(env.MYBROWSER);
    }
  }
  ```

### Error: `429 Browser time limit exceeded for today`

This `Error processing the request: Unable to create new browser: code: 429: message: Browser time limit exceeded for today` error indicates you have hit the daily browser limit on the Workers Free plan. [Workers Free plan accounts are limited](#workers-free) to 10 minutes of browser rendering usage per day. If you exceed that limit, you will receive a `429` error until the next UTC day.

You can [increase your limits](#workers-paid) by upgrading to a Workers Paid plan on the **Workers plans** page of the Cloudflare dashboard:

[Go to **Workers plans**](https://dash.cloudflare.com/?to=/:account/workers/plans)

If you recently upgraded but still encounter the 10-minute per day limit, redeploy your Worker to ensure your usage is correctly associated with the new plan.

## Footnotes

1. Rate limits are enforced with a fixed per-second fill rate. For example, a limit of six requests per minute translates to one request every 10 seconds. This means you cannot send all six requests at once; the API expects them to be spread evenly over the minute. If your account has a custom higher limit, it will also be enforced as a per-second rate. [↩](#user-content-fnref-1)

2. Contact our team to request increases to this limit. [↩](#user-content-fnref-2) [↩2](#user-content-fnref-2-2) [↩3](#user-content-fnref-2-3)

3. Rate limits are enforced with a fixed per-second fill rate. For example, a limit of 180 requests per minute translates to three requests per second. This means you cannot send all 180 requests at once; the API expects them to be spread evenly over the minute. If your account has a custom higher limit, it will also be enforced as a per-second rate. [↩](#user-content-fnref-3)