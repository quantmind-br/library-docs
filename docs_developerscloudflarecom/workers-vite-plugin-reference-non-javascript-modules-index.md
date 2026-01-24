---
title: Non-JavaScript modules · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/index.md
source: llms
fetched_at: 2026-01-24T15:31:20.014975957-03:00
rendered_js: false
word_count: 94
summary: This document outlines the supported non-script module types in Cloudflare Workers and details how various file extensions are automatically converted into JavaScript types upon import.
tags:
    - cloudflare-workers
    - module-imports
    - webassembly
    - static-assets
    - wasm-loading
    - developer-tools
category: reference
---

In addition to TypeScript and JavaScript, the following module types are automatically configured to be importable in your Worker code.

| Module extension | Imported type |
| - | - |
| `.txt` | `string` |
| `.html` | `string` |
| `.sql` | `string` |
| `.bin` | `ArrayBuffer` |
| `.wasm`, `.wasm?module` | `WebAssembly.Module` |

For example, with the following import, `text` will be a string containing the contents of `example.txt`:

```js
import text from "./example.txt";
```

This is also the basis for importing Wasm, as in the following example:

```ts
import wasm from "./example.wasm";


// Instantiate Wasm modules in the module scope
const instance = await WebAssembly.instantiate(wasm);


export default {
  fetch() {
    const result = instance.exports.exported_func();


    return new Response(result);
  },
};
```

Note

Cloudflare Workers does not support `WebAssembly.instantiateStreaming()`.