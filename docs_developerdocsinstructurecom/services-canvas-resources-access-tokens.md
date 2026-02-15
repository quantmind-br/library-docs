---
title: Access Tokens | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/access_tokens
source: sitemap
fetched_at: 2026-02-15T09:01:02.096348-03:00
rendered_js: false
word_count: 287
summary: This document provides a reference for the Token object structure and the associated REST API endpoints for managing user access tokens in Canvas LMS.
tags:
    - canvas-lms
    - access-tokens
    - rest-api
    - authentication
    - token-management
    - oauth-tokens
category: api
---

**A Token object looks like:**

```
{
  // The internal database ID of the token.
"id": null,
  // The time the token was created.
"created_at": null,
  // The time the token will permanently expire, or null if it does not
  // permanently expire.
"expires_at": null,
  // The current state of the token. One of 'active', 'pending', 'disabled', or
  // 'deleted'.
"workflow_state": null,
  // Whether the token should be remembered across sessions. Only applicable for
  // OAuth tokens.
"remember_access": null,
  // The scopes associated with the token. If empty, there are no scope
  // limitations.
"scopes": null,
  // If the token was created while masquerading, this is the ID of the real user.
  // Otherwise, null.
"real_user_id": null,
  // The actual access token. Only included when the token is first created.
"token": null,
  // A short, unique string that can be used to look up the token.
"token_hint": null,
  // The ID of the user the token belongs to.
"user_id": null,
  // The purpose of the token.
"purpose": null,
  // If the token was created by an OAuth application, this is the name of that
  // application. Otherwise, null.
"app_name": null,
  // Whether the current user can manually regenerate this token.
"can_manually_regenerate": null
}
```

[TokensController#user\_generated\_tokensarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tokens_controller.rb)

`GET /api/v1/users/:user_id/user_generated_tokens`

**Scope:** `url:GET|/api/v1/users/:user_id/user_generated_tokens`

Returns a list of manually generated access tokens for the specified user. Note that the actual token values are only returned when the token is first created.

**Request Parameters:**

The number of results to return per page. Defaults to 10. Maximum of 100.

Returns a list of [Token](https://developerdocs.instructure.com/services/canvas/resources/access_tokens#token) objects.

[TokensController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tokens_controller.rb)

`GET /api/v1/users/:user_id/tokens/:id`

**Scope:** `url:GET|/api/v1/users/:user_id/tokens/:id`

The ID can be the actual database ID of the token, or the ‘token\_hint’ value.

[TokensController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tokens_controller.rb)

`POST /api/v1/users/:user_id/tokens`

**Scope:** `url:POST|/api/v1/users/:user_id/tokens`

Create a new access token for the specified user. If the user is not the current user, the token will be created as “pending”, and must be activated by the user before it can be used.

**Request Parameters:**

The purpose of the token.

The time at which the token will expire.

The scopes to associate with the token. Ignored if the default developer key does not have the “enable scopes” option enabled. In such cases, the token will inherit the user’s permissions instead.

[TokensController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tokens_controller.rb)

`PUT /api/v1/users/:user_id/tokens/:id`

**Scope:** `url:PUT|/api/v1/users/:user_id/tokens/:id`

Update an existing access token.

The ID can be the actual database ID of the token, or the ‘token\_hint’ value.

Regenerating an expired token requires a new expiration date.

**Request Parameters:**

The purpose of the token.

The time at which the token will expire.

The scopes to associate with the token.

Regenerate the actual token.

[TokensController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/tokens_controller.rb)

`DELETE /api/v1/users/:user_id/tokens/:id`

**Scope:** `url:DELETE|/api/v1/users/:user_id/tokens/:id`

The ID can be the actual database ID of the token, or the ‘token\_hint’ value.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 4 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).