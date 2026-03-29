---
title: Websocket to Container · Cloudflare Containers docs
url: https://developers.cloudflare.com/containers/examples/websocket/index.md
source: llms
fetched_at: 2026-01-24T15:11:22.617971934-03:00
rendered_js: false
word_count: 26
summary: Explains how to forward WebSocket requests to a Cloudflare Container using the fetch method and the Container class.
tags:
    - cloudflare-containers
    - websockets
    - fetch-api
    - worker-bindings
category: guide
---

WebSocket requests are automatically forwarded to a container using the default `fetch` method on the `Container` class:

```js
import { Container, getContainer } from "@cloudflare/containers";


export class MyContainer extends Container {
  defaultPort = 8080;
  sleepAfter = "2m";
}


export default {
  async fetch(request, env) {
    // gets default instance and forwards websocket from outside Worker
    return getContainer(env.MY_CONTAINER).fetch(request);
  },
};
```

View a full example in the [Container class repository](https://github.com/cloudflare/containers/tree/main/examples/websocket).