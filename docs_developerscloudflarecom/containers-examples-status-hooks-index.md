---
title: Status Hooks · Cloudflare Containers docs
url: https://developers.cloudflare.com/containers/examples/status-hooks/index.md
source: llms
fetched_at: 2026-01-24T15:11:20.951220027-03:00
rendered_js: false
word_count: 33
summary: This document explains how to implement lifecycle hooks in the Cloudflare Container class to execute custom code during container start, stop, and error events.
tags:
    - cloudflare-containers
    - lifecycle-hooks
    - event-handling
    - error-management
    - worker-development
category: guide
---

When a Container starts, stops, and errors, it can trigger code execution in a Worker that has defined status hooks on the `Container` class. Refer to the [Container package docs](https://github.com/cloudflare/containers/blob/main/README.md#lifecycle-hooks) for more details.

```js
import { Container } from '@cloudflare/containers';


export class MyContainer extends Container {
  defaultPort = 4000;
  sleepAfter = '5m';


  override onStart() {
    console.log('Container successfully started');
  }


  override onStop(stopParams) {
    if (stopParams.exitCode === 0) {
      console.log('Container stopped gracefully');
    } else {
      console.log('Container stopped with exit code:', stopParams.exitCode);
    }


    console.log('Container stop reason:', stopParams.reason);
  }


  override onError(error: string) {
    console.log('Container error:', error);
  }
}
```