---
title: Consistency model · Cloudflare R2 docs
url: https://developers.cloudflare.com/r2/reference/consistency/index.md
source: llms
fetched_at: 2026-01-24T15:21:37.055392065-03:00
rendered_js: false
word_count: 493
summary: This document explains the consistency model for Cloudflare R2, detailing the differences between strong and eventual consistency and how caching affects data visibility.
tags:
    - cloudflare-r2
    - consistency-model
    - strong-consistency
    - object-storage
    - distributed-systems
    - caching
category: reference
---

This page details R2's consistency model, including where R2 is strongly, globally consistent and which operations this applies to.

R2 can be described as "strongly consistent", especially in comparison to other distributed object storage systems. This strong consistency ensures that operations against R2 see the latest (accurate) state: clients should be able to observe the effects of any write, update and/or delete operation immediately, globally.

## Terminology

In the context of R2, *strong* consistency and *eventual* consistency have the following meanings:

* **Strongly consistent** - The effect of an operation will be observed globally, immediately, by all clients. Clients will not observe 'stale' (inconsistent) state.
* **Eventually consistent** - Clients may not see the effect of an operation immediately. The state may take a some time (typically seconds to a minute) to propagate globally.

## Operations and Consistency

Operations against R2 buckets and objects adhere to the following consistency guarantees:

Additional notes:

* In the event two clients are writing (`PUT` or `DELETE`) to the same key, the last writer to complete "wins".
* When performing a multipart upload, read-after-write consistency continues to apply once all parts have been successfully uploaded. In the case the same part is uploaded (in error) from multiple writers, the last write will win.
* Copying an object within the same bucket also follows the same read-after-write consistency that writing a new object would. The "copied" object is immediately readable by all clients once the copy operation completes.
* To delete an R2 bucket, it must be completely empty before deletion is allowed. If you attempt to delete a bucket that still contains objects, you will receive an error such as: `The bucket you tried to delete (X) is not empty (account Y)` or `Bucket X cannot be deleted because it isn’t empty.`"

## Caching

Note

By default, Cloudflare's cache will cache common, cacheable status codes automatically [per our cache documentation](https://developers.cloudflare.com/cache/how-to/configure-cache-status-code/#edge-ttl).

When connecting a [custom domain](https://developers.cloudflare.com/r2/buckets/public-buckets/#custom-domains) to an R2 bucket and enabling caching for objects served from that bucket, the consistency model is necessarily relaxed when accessing content via a domain with caching enabled.

Specifically, you should expect:

* An object you delete from R2, but that is still cached, will still be available. You should [purge the cache](https://developers.cloudflare.com/cache/how-to/purge-cache/) after deleting objects if you need that delete to be reflected.
* By default, Cloudflare’s cache will [cache HTTP 404 (Not Found) responses](https://developers.cloudflare.com/cache/how-to/configure-cache-status-code/#edge-ttl) automatically. If you upload an object to that same path, the cache may continue to return HTTP 404s until the cache TTL (Time to Live) expires and the new object is fetched from R2 or the [cache is purged](https://developers.cloudflare.com/cache/how-to/purge-cache/).
* An object for a given key is overwritten with a new object: the old (previous) object will continue to be served to clients until the cache TTL expires (or the object is evicted) or the cache is purged.

The cache does not affect access via [Worker API bindings](https://developers.cloudflare.com/r2/api/workers/) or the [S3 API](https://developers.cloudflare.com/r2/api/s3/), as these operations are made directly against the bucket and do not transit through the cache.