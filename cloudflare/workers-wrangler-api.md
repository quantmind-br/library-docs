---
title: API · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/wrangler/api/#unstable_dev
source: llms
fetched_at: 2026-01-24T15:32:13.81435059-03:00
rendered_js: false
word_count: 885
summary: This document explains how to use Wrangler's programmatic Node.js APIs to start development servers, run integration tests, and emulate the Cloudflare Workers platform.
tags:
    - wrangler-api
    - cloudflare-workers
    - integration-testing
    - node-js
    - dev-server
    - platform-emulation
category: api
---

Wrangler offers APIs to programmatically interact with your Cloudflare Workers.

- [`unstable_startWorker`](#unstable_startworker) - Start a server for running integration tests against your Worker.
- [`unstable_dev`](#unstable_dev) - Start a server for running either end-to-end (e2e) or integration tests against your Worker.
- [`getPlatformProxy`](#getplatformproxy) - Get proxies and values for emulating the Cloudflare Workers platform in a Node.js process.

## `unstable_startWorker`

This API exposes the internals of Wrangler's dev server, and allows you to customise how it runs. For example, you could use `unstable_startWorker()` to run integration tests against your Worker. This example uses `node:test`, but should apply to any testing framework:

```

import assert from "node:assert";
import test,{after,before,describe} from "node:test";
import {unstable_startWorker} from "wrangler";
describe("worker",()=>{
letworker;
before(async()=>{
worker=awaitunstable_startWorker({ config:"wrangler.json"});
});
test("hello world",async()=>{
assert.strictEqual(
await (awaitworker.fetch("http://example.com")).text(),
"Hello world",
);
});
after(async()=>{
awaitworker.dispose();
});
});
```

## `unstable_dev`

Start an HTTP server for testing your Worker.

Once called, `unstable_dev` will return a `fetch()` function for invoking your Worker without needing to know the address or port, as well as a `stop()` function to shut down the HTTP server.

By default, `unstable_dev` will perform integration tests against a local server. If you wish to perform an e2e test against a preview Worker, pass `local: false` in the `options` object when calling the `unstable_dev()` function. Note that e2e tests can be significantly slower than integration tests.

### Constructor

```

constworker=awaitunstable_dev(script,options);
```

### Parameters

- `script` string
  
  - A string containing a path to your Worker script, relative to your Worker project's root directory.
- `options` object optional
  
  - Optional options object containing `wrangler dev` configuration settings.
  - Include an `experimental` object inside `options` to access experimental features such as `disableExperimentalWarning`.
    
    - Set `disableExperimentalWarning` to `true` to disable Wrangler's warning about using `unstable_` prefixed APIs.

### Return Type

`unstable_dev()` returns an object containing the following methods:

- `fetch()` `Promise<Response>`
  
  - Send a request to your Worker. Returns a Promise that resolves with a [`Response`](https://developers.cloudflare.com/workers/runtime-apis/response) object.
  - Refer to [`Fetch`](https://developers.cloudflare.com/workers/runtime-apis/fetch/).
- `stop()` `Promise<void>`
  
  - Shuts down the dev server.

### Usage

When initiating each test suite, use a `beforeAll()` function to start `unstable_dev()`. The `beforeAll()` function is used to minimize overhead: starting the dev server takes a few hundred milliseconds, starting and stopping for each individual test adds up quickly, slowing your tests down.

In each test case, call `await worker.fetch()`, and check that the response is what you expect.

To wrap up a test suite, call `await worker.stop()` in an `afterAll` function.

#### Single Worker example

- [JavaScript](#tab-panel-4039)
- [TypeScript](#tab-panel-4040)

```

const{unstable_dev}=require("wrangler");
describe("Worker",()=>{
letworker;
beforeAll(async()=>{
worker=awaitunstable_dev("src/index.js",{
experimental:{ disableExperimentalWarning:true},
});
});
afterAll(async()=>{
awaitworker.stop();
});
it("should return Hello World",async()=>{
constresp=awaitworker.fetch();
consttext=awaitresp.text();
expect(text).toMatchInlineSnapshot(`"Hello World!"`);
});
});
```

#### Multi-Worker example

You can test Workers that call other Workers. In the below example, we refer to the Worker that calls other Workers as the parent Worker, and the Worker being called as a child Worker.

If you shut down the child Worker prematurely, the parent Worker will not know the child Worker exists and your tests will fail.

- [JavaScript](#tab-panel-4041)
- [TypeScript](#tab-panel-4042)

```

import {unstable_dev} from "wrangler";
describe("multi-worker testing",()=>{
letchildWorker;
letparentWorker;
beforeAll(async()=>{
childWorker=awaitunstable_dev("src/child-worker.js",{
config:"src/child-wrangler.toml",
experimental:{ disableExperimentalWarning:true},
});
parentWorker=awaitunstable_dev("src/parent-worker.js",{
config:"src/parent-wrangler.toml",
experimental:{ disableExperimentalWarning:true},
});
});
afterAll(async()=>{
awaitchildWorker.stop();
awaitparentWorker.stop();
});
it("childWorker should return Hello World itself",async()=>{
constresp=awaitchildWorker.fetch();
consttext=awaitresp.text();
expect(text).toMatchInlineSnapshot(`"Hello World!"`);
});
it("parentWorker should return Hello World by invoking the child worker",async()=>{
constresp=awaitparentWorker.fetch();
constparsedResp=awaitresp.text();
expect(parsedResp).toEqual("Parent worker sees: Hello World!");
});
});
```

## `getPlatformProxy`

The `getPlatformProxy` function provides a way to obtain an object containing proxies (to **local** `workerd` bindings) and emulations of Cloudflare Workers specific values, allowing the emulation of such in a Node.js process.

One general use case for getting a platform proxy is for emulating bindings in applications targeting Workers, but running outside the Workers runtime (for example, framework local development servers running in Node.js), or for testing purposes (for example, ensuring code properly interacts with a type of binding).

### Syntax

```

constplatform=awaitgetPlatformProxy(options);
```

### Parameters

- `options` object optional
  
  - Optional options object containing preferences for the bindings:
    
    - `environment` string
      
      The environment to use.
    - `configPath` string
      
      The path to the config file to use.
      
      If no path is specified, the default behavior is to search from the current directory up the filesystem for a [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) to use.
      
      **Note:** this field is optional but if a path is specified it must point to a valid file on the filesystem.
    - `persist` boolean | `{ path: string }`
      
      Indicates if and where to persist the bindings data. If `true` or `undefined`, defaults to the same location used by Wrangler, so data can be shared between it and the caller. If `false`, no data is persisted to or read from the filesystem.
      
      **Note:** If you use `wrangler`'s `--persist-to` option, note that this option adds a subdirectory called `v3` under the hood while `getPlatformProxy`'s `persist` does not. For example, if you run `wrangler dev --persist-to ./my-directory`, to reuse the same location using `getPlatformProxy`, you will have to specify: `persist: { path: "./my-directory/v3" }`.
    - `experimental` `{ remoteBindings: boolean }`
      
      Object used to enable experimental features, no guarantees are made to the stability of this API, use at your own risk.
      
      - `remoteBindings` Enables `getPlatformProxy` to connect to [remote bindings](https://developers.cloudflare.com/workers/development-testing/#remote-bindings).

### Return Type

`getPlatformProxy()` returns a `Promise` resolving to an object containing the following fields.

- `env` `Record<string, unknown>`
  
  - Object containing proxies to bindings that can be used in the same way as production bindings. This matches the shape of the `env` object passed as the second argument to modules-format workers. These proxy to binding implementations run inside `workerd`.
  - TypeScript Tip: `getPlatformProxy<Env>()` is a generic function. You can pass the shape of the bindings record as a type argument to get proper types without `unknown` values.
- `cf` IncomingRequestCfProperties read-only
  
  - Mock of the `Request`'s `cf` property, containing data similar to what you would see in production.
- `ctx` object
  
  - Mock object containing implementations of the [`waitUntil`](https://developers.cloudflare.com/workers/runtime-apis/context/#waituntil) and [`passThroughOnException`](https://developers.cloudflare.com/workers/runtime-apis/context/#passthroughonexception) functions that do nothing.
- `caches` object
  
  - Emulation of the [Workers `caches` runtime API](https://developers.cloudflare.com/workers/runtime-apis/cache/).
  - For the time being, all cache operations do nothing. A more accurate emulation will be made available soon.
- `dispose()` () =&gt; `Promise<void>`
  
  - Terminates the underlying `workerd` process.
  - Call this after the platform proxy is no longer required by the program. If you are running a long running process (such as a dev server) that can indefinitely make use of the proxy, you do not need to call this function.

### Usage

The `getPlatformProxy` function uses bindings found in the [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/). For example, if you have an [environment variable](https://developers.cloudflare.com/workers/configuration/environment-variables/#add-environment-variables-via-wrangler) configuration set up in the Wrangler configuration file:

- [wrangler.jsonc](#tab-panel-4049)
- [wrangler.toml](#tab-panel-4050)

```

{
"$schema":"./node_modules/wrangler/config-schema.json",
"vars":{
"MY_VARIABLE":"test"
}
}
```

You can access the bindings by importing `getPlatformProxy` like this:

```

import {getPlatformProxy} from "wrangler";
const{env}=awaitgetPlatformProxy();
```

To access the value of the `MY_VARIABLE` binding add the following to your code:

```

console.log(`MY_VARIABLE = ${env.MY_VARIABLE}`);
```

This will print the following output: `MY_VARIABLE = test`.

### Supported bindings

All supported bindings found in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) are available to you via `env`.

The bindings supported by `getPlatformProxy` are:

- [Environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/)
- [Service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/)
- [KV namespace bindings](https://developers.cloudflare.com/kv/api/)
- [R2 bucket bindings](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)
- [Queue bindings](https://developers.cloudflare.com/queues/configuration/javascript-apis/)
- [D1 database bindings](https://developers.cloudflare.com/d1/worker-api/)
- [Hyperdrive bindings](https://developers.cloudflare.com/hyperdrive)
- [Workers AI bindings](https://developers.cloudflare.com/workers-ai/get-started/workers-wrangler/#2-connect-your-worker-to-workers-ai)
- [Durable Object bindings](https://developers.cloudflare.com/durable-objects/api/)
  
  - To use a Durable Object binding with `getPlatformProxy`, always specify a [`script_name`](https://developers.cloudflare.com/workers/wrangler/configuration/#durable-objects).
    
    For example, you might have the following binding in a Wrangler configuration file read by `getPlatformProxy`.
    
    - [wrangler.jsonc](#tab-panel-4053)
    - [wrangler.toml](#tab-panel-4054)
    
    ```
    
    {
    "$schema":"./node_modules/wrangler/config-schema.json",
    "durable_objects":{
    "bindings":[
    {
    "name":"MyDurableObject",
    "class_name":"MyDurableObject",
    "script_name":"external-do-worker"
    }
    ]
    }
    }
    ```
    
    You will need to declare your Durable Object `"MyDurableObject"` in another Worker, called `external-do-worker` in this example.
    
    ```
    
    exportclassMyDurableObjectextendsDurableObject{
    // Your DO code goes here
    }
    exportdefault{
    fetch(){
    // Doesn't have to do anything, but a DO cannot be the default export
    returnnewResponse("Hello, world!");
    },
    };
    ```
    
    That Worker also needs a Wrangler configuration file that looks like this:
    
    - [wrangler.jsonc](#tab-panel-4051)
    - [wrangler.toml](#tab-panel-4052)
    
    ```
    
    {
    "name":"external-do-worker",
    "main":"src/index.ts",
    "compatibility_date":"XXXX-XX-XX"
    }
    ```
    
    If you are not using RPC with your Durable Object, you can run a separate Wrangler dev session alongside your framework development server.
    
    Otherwise, you can build your application and run both Workers in the same Wrangler dev session.
    
    If you are using Pages run:
    
    - [npm](#tab-panel-4043)
    - [yarn](#tab-panel-4044)
    - [pnpm](#tab-panel-4045)
    
    ```
    
    npxwranglerpagesdev-cpath/to/pages/wrangler.jsonc-cpath/to/external-do-worker/wrangler.jsonc
    ```
    
    If you are using Workers with Assets run:
    
    - [npm](#tab-panel-4046)
    - [yarn](#tab-panel-4047)
    - [pnpm](#tab-panel-4048)
    
    ```
    
    npxwranglerdev-cpath/to/workers-assets/wrangler.jsonc-cpath/to/external-do-worker/wrangler.jsonc
    ```

## Was this helpful?

- **Resources**
- [API](https://developers.cloudflare.com/api/)
- [New to Cloudflare?](https://developers.cloudflare.com/fundamentals/)
- [Directory](https://developers.cloudflare.com/directory/)
- [Sponsorships](https://developers.cloudflare.com/sponsorships/)
- [Open Source](https://github.com/cloudflare)

<!--THE END-->

- **Support**
- [Help Center](https://support.cloudflare.com/)
- [System Status](https://www.cloudflarestatus.com/)
- [Compliance](https://www.cloudflare.com/trust-hub/compliance-resources/)
- [GDPR](https://www.cloudflare.com/trust-hub/gdpr/)

<!--THE END-->

- **Company**
- [cloudflare.com](https://www.cloudflare.com/)
- [Our team](https://www.cloudflare.com/people/)
- [Careers](https://www.cloudflare.com/careers/)

<!--THE END-->

- **Tools**
- [Cloudflare Radar](https://radar.cloudflare.com/)
- [Speed Test](https://speed.cloudflare.com/)
- [Is BGP Safe Yet?](https://isbgpsafeyet.com/)
- [RPKI Toolkit](https://rpki.cloudflare.com/)
- [Certificate Transparency](https://ct.cloudflare.com/)

<!--THE END-->

- **Community**
- [X](https://x.com/cloudflare)
- [Discord](http://discord.cloudflare.com/)
- [YouTube](https://www.youtube.com/cloudflare)
- [GitHub](https://github.com/cloudflare/cloudflare-docs)