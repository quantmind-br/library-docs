---
title: Developer Key Account Bindings | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/developer_key_account_bindings
source: sitemap
fetched_at: 2026-02-15T09:07:21.09579-03:00
rendered_js: false
word_count: 141
summary: This document describes the Developer Key Account Bindings API used to create or update associations between developer keys and specific account contexts within the Canvas LMS.
tags:
    - canvas-lms
    - api-endpoint
    - developer-keys
    - account-bindings
    - workflow-state
category: api
---

## Developer Key Account Bindings API

Developer key account bindings API for binding a developer key to a context and specifying a workflow state for that relationship.

**A DeveloperKeyAccountBinding object looks like:**

```
{
  // The Canvas ID of the binding
"id": 1,
  // The global Canvas ID of the account in the binding
"account_id": 10000000000001,
  // The global Canvas ID of the developer key in the binding
"developer_key_id": 10000000000008,
  // The workflow state of the binding. Will be one of 'on', 'off', or 'allow.'
"workflow_state": on,
  // True if the requested context owns the binding
"account_owns_binding": true
}
```

[DeveloperKeyAccountBindingsController#create\_or\_updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/developer_key_account_bindings_controller.rb)

`POST /api/v1/accounts/:account_id/developer_keys/:developer_key_id/developer_key_account_bindings`

**Scope:** `url:POST|/api/v1/accounts/:account_id/developer_keys/:developer_key_id/developer_key_account_bindings`

Create a new Developer Key Account Binding. The developer key specified in the request URL must be available in the requested account or the requested account’s account chain. If the binding already exists for the specified account/key combination it will be updated.

**Request Parameters:**

The workflow state for the binding. Must be one of “on”, “off”, or “allow”. Defaults to “off”.

Returns a [DeveloperKeyAccountBinding](https://developerdocs.instructure.com/services/canvas/resources/developer_key_account_bindings#developerkeyaccountbinding) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).