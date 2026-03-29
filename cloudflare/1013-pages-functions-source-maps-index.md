---
title: Source maps and stack traces · Cloudflare Pages docs
url: https://developers.cloudflare.com/pages/functions/source-maps/index.md
source: llms
fetched_at: 2026-01-24T15:17:26.249991289-03:00
rendered_js: false
word_count: 310
summary: This document explains how to enable and use source maps in Cloudflare Pages to deobfuscate stack traces for easier debugging in production environments.
tags:
    - cloudflare-pages
    - source-maps
    - stack-traces
    - wrangler
    - debugging
    - error-handling
category: guide
---

[Stack traces](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack) help with debugging your code when your application encounters an unhandled exception. Stack traces show you the specific functions that were called, in what order, from which line and file, and with what arguments.

Most JavaScript code is first bundled, often transpiled, and then minified before being deployed to production. This process creates smaller bundles to optimize performance and converts code from TypeScript to Javascript if needed.

Source maps translate compiled and minified code back to the original code that you wrote. Source maps are combined with the stack trace returned by the JavaScript runtime to present you with a stack trace.

Warning

Support for uploading source maps for Pages is available now in open beta. Minimum required Wrangler version: 3.60.0.

## Source Maps

To enable source maps, provide the `--upload-source-maps` flag to [`wrangler pages deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#deploy-1) or add the following to your Pages application's [Wrangler configuration file](https://developers.cloudflare.com/pages/functions/wrangler-configuration/) if you are using the Pages build environment:

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "upload_source_maps": true
  }
  ```

* wrangler.toml

  ```toml
  upload_source_maps = true
  ```

When uploading source maps is enabled, Wrangler will automatically generate and upload source map files when you run [`wrangler pages deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#deploy-1).

## Stack traces

​​ When your application throws an uncaught exception, we fetch the source map and use it to map the stack trace of the exception back to lines of your application’s original source code.

You can then view the stack trace when streaming [real-time logs](https://developers.cloudflare.com/pages/functions/debugging-and-logging/).

Note

The source map is retrieved after your Pages Function invocation completes — it's an asynchronous process that does not impact your applications's CPU utilization or performance. Source maps are not accessible inside the application at runtime, if you `console.log()` the [stack property](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/stack), you will not get a deobfuscated stack trace.

## Limits

| Description | Limit |
| - | - |
| Maximum Source Map Size | 15 MB gzipped |

## Related resources

* [Real-time logs](https://developers.cloudflare.com/pages/functions/debugging-and-logging/) - Learn how to capture Pages logs in real-time.