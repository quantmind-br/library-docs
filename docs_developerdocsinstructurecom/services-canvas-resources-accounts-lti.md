---
title: Accounts (LTI) | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti
source: sitemap
fetched_at: 2026-02-15T09:06:46.32975-03:00
rendered_js: false
word_count: 109
summary: This document provides technical documentation for the Canvas LMS API endpoint used to retrieve account details via the LTI Advantage authorization scheme.
tags:
    - canvas-lms
    - lti-advantage
    - account-api
    - lti-authorization
    - api-endpoint
category: api
---

API for accessing account data using an LTI dev key. Allows a tool to get account information via LTI Advantage authorization scheme, which does not require a user session like normal developer keys do. Requires the account lookup scope on the LTI key.

**An Account object looks like:**

```
{
  // the ID of the Account object
"id": 2,
  // The display name of the account
"name": "Canvas Account",
  // The UUID of the account
"uuid": "WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5",
  // The account's parent ID, or null if this is the root account
"parent_account_id": 1,
  // The ID of the root account, or null if this is the root account
"root_account_id": 1,
  // The state of the account. Can be 'active' or 'deleted'.
"workflow_state": "active"
}
```

[Lti::AccountLookupController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/lti/account_lookup_controller.rb)

`GET /api/lti/accounts/:account_id`

**Scope:** `url:GET|/api/lti/accounts/:account_id`

Retrieve information on an individual account, given by local or global ID.

Returns an [Account](https://developerdocs.instructure.com/services/canvas/resources/accounts_-lti#account) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).