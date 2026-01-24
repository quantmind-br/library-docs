---
title: Create multitenancy · Cloudflare AI Search docs
url: https://developers.cloudflare.com/ai-search/how-to/multitenancy/index.md
source: llms
fetched_at: 2026-01-24T14:00:36.706406984-03:00
rendered_js: false
word_count: 274
summary: This document explains how to implement multitenancy in AI Search by organizing content into tenant-specific folders and applying metadata filters to isolate data access.
tags:
    - ai-search
    - multitenancy
    - metadata-filtering
    - data-isolation
    - r2-folders
    - workers-binding
category: guide
---

AI Search supports multitenancy by letting you segment content by tenant, so each user, customer, or workspace can only access their own data. This is typically done by organizing documents into per-tenant folders and applying [metadata filters](https://developers.cloudflare.com/ai-search/configuration/metadata/) at query time.

## 1. Organize Content by Tenant

When uploading files to R2, structure your content by tenant using unique folder paths.

Example folder structure:

When indexing, AI Search will automatically store the folder path as metadata under the `folder` attribute. It is recommended to enforce folder separation during upload or indexing to prevent accidental data access across tenants.

## 2. Search Using Folder Filters

To ensure a tenant only retrieves their own documents, apply a `folder` filter when performing a search.

Example using [Workers Binding](https://developers.cloudflare.com/ai-search/usage/workers-binding/):

```js
const response = await env.AI.autorag("my-autorag").search({
  query: "When did I sign my agreement contract?",
  filters: {
    type: "eq",
    key: "folder",
    value: `customer-a/contracts/`,
  },
});
```

To filter across multiple folders, or to add date-based filtering, you can use a compound filter with an array of [comparison filters](https://developers.cloudflare.com/ai-search/configuration/metadata/#compound-filter).

## Tip: Use "Starts with" filter

While an `eq` filter targets files at the specific folder, you'll often want to retrieve all documents belonging to a tenant regardless if there are files in its subfolders. For example, all files in `customer-a/` with a structure like:

To achieve this [starts with](https://developers.cloudflare.com/ai-search/configuration/metadata/#starts-with-filter-for-folders) behavior, use a compound filter like:

```js
filters: {
    type: "and",
    filters: [
      {
        type: "gt",
        key: "folder",
        value: "customer-a//",
      },
      {
        type: "lte",
        key: "folder",
        value: "customer-a/z",
      },
    ],
  },
```

This filter identifies paths starting with `customer-a/` by using:

* The `and` condition to combine the effects of the `gt` and `lte` conditions.
* The `gt` condition to include paths greater than the `/` ASCII character.
* The `lte` condition to include paths less than and including the lower case `z` ASCII character.

This filter captures both files `profile.md` and `contract-1.pdf`.