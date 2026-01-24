---
title: Storage and Broadcast · Cloudflare Realtime docs
url: https://developers.cloudflare.com/realtime/realtimekit/collaborative-stores/index.md
source: llms
fetched_at: 2026-01-24T15:35:58.840166833-03:00
rendered_js: false
word_count: 226
summary: This document outlines the RealtimeKit Stores API, providing instructions on how to create, manage, and subscribe to synchronized key-value data stores within active sessions.
tags:
    - realtimekit
    - stores-api
    - key-value-storage
    - real-time-updates
    - data-synchronization
category: api
---

The RealtimeKit Stores API allows you to create multiple key-value pair realtime stores. Users can subscribe to changes in a store and receive real-time updates. Data is stored until a [session](https://developers.cloudflare.com/realtime/realtimekit/concepts/meeting/#session) is active.

### Create a Store

You can create a realtime store (changes are synced with other users):

| Param | Type | Description | Required |
| - | - | - | - |
| `name` | string | Name of the store | true |

To create a store:

Note

This method must be executed for every user.

### Update a Store

You can add, update or delete entires in a store:

| Param | Type | Description | Required |
| - | - | - | - |
| `key` | string | Unique identifier used to store/update a value in the store | Yes |
| `value` | StoreValue | Value that can be stored agains a key | Yes |

Note

The `set` method overwrites the existing value, while the `update` method updates the existing value.

For example, if the stored value is `['a', 'b']` and you call `update` with `['c']`, the final value will be `['a', 'b', 'c']`.

### Subscribe to a Store

You can attach event listeners on a store's key, which fire when the value changes.

### Fetch Store Data

You can fetch the data stored in the store: