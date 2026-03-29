---
title: API reference · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/functions/api-reference/index.md
source: llms
fetched_at: 2026-01-24T15:17:12.777371531-03:00
rendered_js: false
word_count: 416
summary: This document defines the request handler methods and context object properties available for configuring and developing Cloudflare Pages Functions. It explains how to handle specific HTTP verbs and interact with the execution environment through the EventContext and EnvWithFetch types.
tags:
    - cloudflare-pages
    - pages-functions
    - request-handlers
    - api-reference
    - event-context
    - serverless-functions
category: reference
---

The following methods can be used to configure your Pages Function.

## Methods

### `onRequests`

The `onRequest` method will be called unless a more specific `onRequestVerb` method is exported. For example, if both `onRequest` and `onRequestGet` are exported, only `onRequestGet` will be called for `GET` requests.

* `onRequest(contextEventContext)` Response | Promise\<Response>

  * This function will be invoked on all requests no matter what the request method is, as long as no specific request verb (like one of the methods below) is exported.

* `onRequestGet(contextEventContext)` Response | Promise\<Response>

  * This function will be invoked on all `GET` requests.

* `onRequestPost(contextEventContext)` Response | Promise\<Response>

  * This function will be invoked on all `POST` requests.

* `onRequestPatch(contextEventContext)` Response | Promise\<Response>

  * This function will be invoked on all `PATCH` requests.

* `onRequestPut(contextEventContext)` Response | Promise\<Response>

  * This function will be invoked on all `PUT` requests.

* `onRequestDelete(contextEventContext)` Response | Promise\<Response>

  * This function will be invoked on all `DELETE` requests.

* `onRequestHead(contextEventContext)` Response | Promise\<Response>

  * This function will be invoked on all `HEAD` requests.

* `onRequestOptions(contextEventContext)` Response | Promise\<Response>

  * This function will be invoked on all `OPTIONS` requests.

### `env.ASSETS.fetch()`

The `env.ASSETS.fetch()` function allows you to fetch a static asset from your Pages project.

You can pass a [Request object](https://developers.cloudflare.com/workers/runtime-apis/request/), URL string, or URL object to `env.ASSETS.fetch()` function. The URL must be to the pretty path, not directly to the asset. For example, if you had the path `/users/index.html`, you will request `/users/` instead of `/users/index.html`. This method call will run the header and redirect rules, modifying the response that is returned.

## Types

### `EventContext`

The following are the properties on the `context` object which are passed through on the `onRequest` methods:

* `request` [Request](https://developers.cloudflare.com/workers/runtime-apis/request/)

  This is the incoming [Request](https://developers.cloudflare.com/workers/runtime-apis/request/).

* `functionPath` string

  This is the path of the request.

* `waitUntil(promisePromise<any>)` void

  Refer to [`waitUntil` documentation](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil) for more information.

* `passThroughOnException()` void

  Refer to [`passThroughOnException` documentation](https://developers.cloudflare.com/workers/runtime-apis/context/#passthroughonexception) for more information. Note that this will not work on an [advanced mode project](https://developers.cloudflare.com/pages/functions/advanced-mode/).

* `next(input?Request | string, init?RequestInit)` Promise\<Response>

  Passes the request through to the next Function or to the asset server if no other Function is available.

* `env` [EnvWithFetch](#envwithfetch)

* `params` Params\<P>

  Holds the values from [dynamic routing](https://developers.cloudflare.com/pages/functions/routing/#dynamic-routes).

  In the following example, you have a dynamic path that is `/users/[user].js`. When you visit the site on `/users/nevi` the `params` object would look like:

  ```js
  {
    user: "nevi";
  }
  ```

  This allows you fetch the dynamic value from the path:

  ```js
  export function onRequest(context) {
    return new Response(`Hello ${context.params.user}`);
  }
  ```

  Which would return `"Hello nevi"`.

* `data` Data

### `EnvWithFetch`

Holds the environment variables, secrets, and bindings for a Function. This also holds the `ASSETS` binding which is how you can fallback to the asset-serving behavior.