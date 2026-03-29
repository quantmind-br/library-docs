---
title: KV bindings
url: https://developers.cloudflare.com/kv/concepts/kv-bindings/index.md
source: llms
fetched_at: 2026-01-24T15:16:18.672330136-03:00
rendered_js: false
word_count: 359
summary: This document explains how to configure and use KV bindings to facilitate communication between Cloudflare Workers and KV namespaces.
tags:
    - cloudflare-workers
    - kv-bindings
    - wrangler-configuration
    - kv-namespaces
    - serverless-storage
category: concept
---

---
title: KV bindings · Cloudflare Workers KV docs
description: KV bindings allow for communication between a Worker and a KV namespace.
lastUpdated: 2025-09-30T16:36:58.000Z
chatbotDeprioritize: false
tags: Bindings
source_url:
  html: https://developers.cloudflare.com/kv/concepts/kv-bindings/
  md: https://developers.cloudflare.com/kv/concepts/kv-bindings/index.md
---

KV [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) allow for communication between a Worker and a KV namespace.

Configure KV bindings in the [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/).

## Access KV from Workers

A [KV namespace](https://developers.cloudflare.com/kv/concepts/kv-namespaces/) is a key-value database replicated to Cloudflare's global network.

To connect to a KV namespace from within a Worker, you must define a binding that points to the namespace's ID.

The name of your binding does not need to match the KV namespace's name. Instead, the binding should be a valid JavaScript identifier, because the identifier will exist as a global variable within your Worker.

A KV namespace will have a name you choose (for example, `My tasks`), and an assigned ID (for example, `06779da6940b431db6e566b4846d64db`).

To execute your Worker, define the binding.

In the following example, the binding is called `TODO`. In the `kv_namespaces` portion of your Wrangler configuration file, add:

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "name": "worker",
    "kv_namespaces": [
      {
        "binding": "TODO",
        "id": "06779da6940b431db6e566b4846d64db"
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  name = "worker"


  # ...


  kv_namespaces = [
    { binding = "TODO", id = "06779da6940b431db6e566b4846d64db" }
  ]
  ```

With this, the deployed Worker will have a `TODO` field in their environment object (the second parameter of the `fetch()` request handler). Any methods on the `TODO` binding will map to the KV namespace with an ID of `06779da6940b431db6e566b4846d64db` – which you called `My Tasks` earlier.

```js
export default {
  async fetch(request, env, ctx) {
    // Get the value for the "to-do:123" key
    // NOTE: Relies on the `TODO` KV binding that maps to the "My Tasks" namespace.
    let value = await env.TODO.get("to-do:123");


    // Return the value, as is, for the Response
    return new Response(value);
  },
};
```

## Use KV bindings when developing locally

When you use Wrangler to develop locally with the `wrangler dev` command, Wrangler will default to using a local version of KV to avoid interfering with any of your live production data in KV. This means that reading keys that you have not written locally will return `null`.

To have `wrangler dev` connect to your Workers KV namespace running on Cloudflare's global network, set `"remote" : true` in the KV binding configuration. Refer to the [remote bindings documentation](https://developers.cloudflare.com/workers/development-testing/#remote-bindings) for more information.

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "name": "worker",
    "kv_namespaces": [
      {
        "binding": "TODO",
        "id": "06779da6940b431db6e566b4846d64db"
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  name = "worker"


  # ...


  kv_namespaces = [
    { binding = "TODO", id = "06779da6940b431db6e566b4846d64db" }
  ]
  ```

## Access KV from Durable Objects and Workers using ES modules format

[Durable Objects](https://developers.cloudflare.com/durable-objects/) use ES modules format. Instead of a global variable, bindings are available as properties of the `env` parameter [passed to the constructor](https://developers.cloudflare.com/durable-objects/get-started/#2-write-a-durable-object-class).

An example might look like:

```js
import { DurableObject } from "cloudflare:workers";


export class MyDurableObject extends DurableObject {
  constructor(ctx, env) {
    super(ctx, env);
  }


  async fetch(request) {
    const valueFromKV = await this.env.NAMESPACE.get("someKey");
    return new Response(valueFromKV);
  }
}
```