---
title: Custom limits · Cloudflare for Platforms docs
url: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/configuration/custom-limits/index.md
source: llms
fetched_at: 2026-01-24T15:09:56.973946196-03:00
rendered_js: false
word_count: 59
summary: This document explains how to programmatically set and enforce resource usage limits, specifically CPU time and subrequests, for Workers using dynamic dispatch.
tags:
    - cloudflare-workers
    - dynamic-dispatch
    - resource-management
    - cpu-limits
    - subrequest-limits
category: guide
---

Custom limits allow you to programmatically enforce limits on your customers' Workers' resource usage. You can set limits for the maximum CPU time and number of subrequests per invocation. If a user Worker hits either of these limits, the user Worker will immediately throw an exception.

## Set Custom limits

Custom limits can be set in the dynamic dispatch Worker:

```js
export default {
  async fetch(request, env) {
    try {
      // parse the URL, read the subdomain
      let workerName = new URL(request.url).host.split(".")[0];
      let userWorker = env.dispatcher.get(
        workerName,
        {},
        {
          // set limits
          limits: { cpuMs: 10, subRequests: 5 },
        },
      );
      return await userWorker.fetch(request);
    } catch (e) {
      if (e.message.startsWith("Worker not found")) {
        // we tried to get a worker that doesn't exist in our dispatch namespace
        return new Response("", { status: 404 });
      }
      return new Response(e.message, { status: 500 });
    }
  },
};
```