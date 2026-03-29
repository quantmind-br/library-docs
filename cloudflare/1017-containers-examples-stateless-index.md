---
title: Stateless Instances · Cloudflare Containers docs
url: https://developers.cloudflare.com/containers/examples/stateless/index.md
source: llms
fetched_at: 2026-01-24T15:11:20.786662139-03:00
rendered_js: false
word_count: 75
summary: This document explains how to distribute incoming requests across multiple container instances using the getRandom helper function for basic load balancing.
tags:
    - cloudflare-containers
    - load-balancing
    - request-routing
    - serverless-containers
    - proxying
category: guide
---

To simply proxy requests to one of multiple instances of a container, you can use the `getRandom` function:

```ts
import { Container, getRandom } from "@cloudflare/containers";


const INSTANCE_COUNT = 3;


class Backend extends Container {
  defaultPort = 8080;
  sleepAfter = "2h";
}


export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // note: "getRandom" to be replaced with latency-aware routing in the near future
    const containerInstance = await getRandom(env.BACKEND, INSTANCE_COUNT);
    return containerInstance.fetch(request);
  },
};
```

Note

This example uses the `getRandom` function, which is a temporary helper that will randomly select one of N instances of a Container to route requests to.

In the future, we will provide improved latency-aware load balancing and autoscaling.

This will make scaling stateless instances simple and routing more efficient. See the [autoscaling documentation](https://developers.cloudflare.com/containers/platform-details/scaling-and-routing) for more details.