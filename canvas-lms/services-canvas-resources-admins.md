---
title: Admins | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/admins
source: sitemap
fetched_at: 2026-02-15T09:06:59.803335-03:00
rendered_js: false
word_count: 296
summary: This document details the API endpoints for managing account-level administrative roles, including listing, assigning, and removing admin privileges for users within Canvas LMS.
tags:
    - canvas-lms
    - admins-api
    - role-management
    - user-permissions
    - account-administration
    - rest-api
category: api
---

Manage account role assignments

**An Admin object looks like:**

```
{
  // The unique identifier for the account role/user assignment.
"id": 1023,
  // The account role assigned. This can be 'AccountAdmin' or a user-defined role
  // created by the Roles API.
"role": "AccountAdmin",
  // The user the role is assigned to. See the Users API for details.
"user": null,
  // The status of the account role/user assignment.
"workflow_state": "deleted"
}
```

[AdminsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/admins_controller.rb)

`GET /api/v1/accounts/:account_id/admins`

**Scope:** `url:GET|/api/v1/accounts/:account_id/admins`

A paginated list of the admins in the account

**Request Parameters:**

Scope the results to those with user IDs equal to any of the IDs specified here.

The partial name or full ID of the admins to match and return in the results list. Must be at least 2 characters.

When set to true, returns admins who have been deleted

Returns a list of [Admin](https://developerdocs.instructure.com/services/canvas/resources/admins#admin) objects.

[AdminsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/admins_controller.rb)

`POST /api/v1/accounts/:account_id/admins`

**Scope:** `url:POST|/api/v1/accounts/:account_id/admins`

Flag an existing user as an admin within the account.

**Request Parameters:**

The id of the user to promote.

- DEPRECATED
  
  The user’s admin relationship with the account will be

created with the given role. Defaults to ‘AccountAdmin’.

The user’s admin relationship with the account will be created with the given role. Defaults to the built-in role for ‘AccountAdmin’.

Send a notification email to the new admin if true. Default is true.

Returns an [Admin](https://developerdocs.instructure.com/services/canvas/resources/admins#admin) object.

[AdminsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/admins_controller.rb)

`DELETE /api/v1/accounts/:account_id/admins/:user_id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/admins/:user_id`

Remove the rights associated with an account admin role from a user.

**Request Parameters:**

- DEPRECATED
  
  Account role to remove from the user.

The id of the role representing the user’s admin relationship with the account.

Returns an [Admin](https://developerdocs.instructure.com/services/canvas/resources/admins#admin) object.

[AdminsController#self\_rolesarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/admins_controller.rb)

`GET /api/v1/accounts/:account_id/admins/self`

**Scope:** `url:GET|/api/v1/accounts/:account_id/admins/self`

A paginated list of the current user’s roles in the account. The results are the same as those returned by the [List account admins](https://developerdocs.instructure.com/services/canvas/resources/admins#method.admins.index) endpoint with `user_id` set to `self`, except the “Admins - Add / Remove” permission is not required.

Returns a list of [Admin](https://developerdocs.instructure.com/services/canvas/resources/admins#admin) objects.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).