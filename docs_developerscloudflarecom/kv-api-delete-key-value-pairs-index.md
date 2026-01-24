---
title: Delete key-value pairs · Cloudflare Workers KV docs
url: https://developers.cloudflare.com/kv/api/delete-key-value-pairs/index.md
source: llms
fetched_at: 2026-01-24T15:16:13.191136198-03:00
rendered_js: false
word_count: 223
summary: This document explains how to delete key-value pairs from Cloudflare Workers KV namespaces using the delete method, command-line tools, or the REST API.
tags:
    - cloudflare-workers
    - kv-namespace
    - data-deletion
    - api-reference
    - serverless-storage
    - bulk-delete
category: reference
---

To delete a key-value pair, call the `delete()` method of the [KV binding](https://developers.cloudflare.com/kv/concepts/kv-bindings/) on any [KV namespace](https://developers.cloudflare.com/kv/concepts/kv-namespaces/) you have bound to your Worker code:

```js
env.NAMESPACE.delete(key);
```

#### Example

An example of deleting a key-value pair from within a Worker:

```js
export default {
  async fetch(request, env, ctx) {
    try {
      await env.NAMESPACE.delete("first-key");


      return new Response("Successful delete", {
        status: 200
      });
    }
    catch (e)
    {
      return new Response(e.message, {status: 500});
    }
  },
};
```

## Reference

The following method is provided to delete from KV:

* [delete()](#delete-method)

### `delete()` method

To delete a key-value pair, call the `delete()` method of the [KV binding](https://developers.cloudflare.com/kv/concepts/kv-bindings/) on any KV namespace you have bound to your Worker code:

```js
env.NAMESPACE.delete(key);
```

#### Parameters

* `key`: `string`
  * The key to associate with the value.

#### Response

* `response`: `Promise<void>`
  * A `Promise` that resolves if the delete is successful.

This method returns a promise that you should `await` on to verify successful deletion. Calling `delete()` on a non-existing key is returned as a successful delete.

Calling the `delete()` method will remove the key and value from your KV namespace. As with any operations, it may take some time for the key to be deleted from various points in the Cloudflare global network.

## Guidance

### Delete data in bulk

Delete more than one key-value pair at a time with Wrangler or [via the REST API](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/keys/methods/bulk_delete/).

The bulk REST API can accept up to 10,000 KV pairs at once. Bulk writes are not supported using the [KV binding](https://developers.cloudflare.com/kv/concepts/kv-bindings/).

## Other methods to access KV

You can also [delete key-value pairs from the command line with Wrangler](https://developers.cloudflare.com/kv/reference/kv-commands/#kv-namespace-delete) or [with the REST API](https://developers.cloudflare.com/api/resources/kv/subresources/namespaces/subresources/values/methods/delete/).