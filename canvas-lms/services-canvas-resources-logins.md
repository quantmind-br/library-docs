---
title: Logins | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/logins
source: sitemap
fetched_at: 2026-02-15T09:10:21.239223-03:00
rendered_js: false
word_count: 850
summary: This document defines the API endpoints for managing user login credentials, including creating, listing, updating, and deleting logins as well as handling password resets.
tags:
    - canvas-lms-api
    - user-authentication
    - login-management
    - sis-integration
    - account-administration
    - pseudonyms
category: api
---

API for creating and viewing user logins under an account

[PseudonymsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/pseudonyms_controller.rb)

`GET /api/v1/accounts/:account_id/logins`

**Scope:** `url:GET|/api/v1/accounts/:account_id/logins`

`GET /api/v1/users/:user_id/logins`

**Scope:** `url:GET|/api/v1/users/:user_id/logins`

Given a user ID, return a paginated list of that user’s logins for the given account.

**API response field:**

The ID of the login’s account.

The unique, numeric ID for the login.

The login’s unique SIS ID.

The login’s unique integration ID.

The unique ID for the login.

The unique ID of the login’s user.

- authentication\_provider\_id

The ID of the authentication provider that this login is associated with

- authentication\_provider\_type

The type of the authentication provider that this login is associated with

The current status of the login

The declared intention for this user’s role

**Example Response:**

```
[
  {
    "account_id": 1,
    "id" 2,
    "sis_user_id": null,
    "unique_id": "belieber@example.com",
    "user_id": 2,
    "authentication_provider_id": 1,
    "authentication_provider_type": "facebook",
    "workflow_state": "active",
    "declared_user_type": null,
  }
]
```

[PseudonymsController#forgot\_passwordarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/pseudonyms_controller.rb)

`POST /api/v1/users/reset_password`

**Scope:** `url:POST|/api/v1/users/reset_password`

Given a user email, generate a nonce and email it to the user

**API response field:**

The recovery request status

**Example Response:**

[PseudonymsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/pseudonyms_controller.rb)

`POST /api/v1/accounts/:account_id/logins`

**Scope:** `url:POST|/api/v1/accounts/:account_id/logins`

Create a new login for an existing user in the given account.

**Request Parameters:**

The ID of the user to create the login for.

The unique ID for the new login.

The new login’s password.

SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account.

Integration ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account. The Integration ID is a secondary identifier useful for more complex SIS integrations.

`login[authentication_provider_id]`

The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider).

`login[declared_user_type]`

The declared intention of the user type. This can be set, but does not change any Canvas functionality with respect to their access. A user can still be a teacher, admin, student, etc. in any particular context without regard to this setting. This can be used for administrative purposes for integrations to be able to more easily identify why the user was created. Valid values are:

```
* administrative
* observer
* staff
* student
* student_other
* teacher
```

A Canvas User ID to identify a user in a trusted account (alternative to ‘id`,`existing\_sis\_user\_id`, or`existing\_integration\_id\`). This parameter is not available in OSS Canvas.

`user[existing_integration_id]`

An Integration ID to identify a user in a trusted account (alternative to ‘id`,`existing\_user\_id`, or`existing\_sis\_user\_id\`). This parameter is not available in OSS Canvas.

`user[existing_sis_user_id]`

An SIS User ID to identify a user in a trusted account (alternative to ‘id`,`existing\_integration\_id`, or`existing\_user\_id\`). This parameter is not available in OSS Canvas.

The domain of the account to search for the user. This field is required when identifying a user in a trusted account. This parameter is not available in OSS Canvas.

**Example Request:**

```
#create a facebook login for user with ID 123
curl 'https://<canvas>/api/v1/accounts/<account_id>/logins' \
     -F 'user[id]=123' \
     -F 'login[unique_id]=112233445566' \
     -F 'login[authentication_provider_id]=facebook' \
     -H 'Authorization: Bearer <token>'
```

```
#create a login for user in another trusted account:
curl 'https://<canvas>/api/v1/accounts/<account_id>/logins' \
     -F 'user[existing_user_sis_id]=SIS42' \
     -F 'user[trusted_account]=canvas.example.edu' \
     -F 'login[unique_id]=112233445566' \
     -H 'Authorization: Bearer <token>'
```

[PseudonymsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/pseudonyms_controller.rb)

`PUT /api/v1/accounts/:account_id/logins/:id`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/logins/:id`

Update an existing login for a user in the given account.

**Request Parameters:**

The new unique ID for the login.

The new password for the login. Admins can only set a password for another user if the “Password setting by admins” account setting is enabled.

The prior password for the login. Required if the caller is changing their own password.

SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account.

Integration ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account. The Integration ID is a secondary identifier useful for more complex SIS integrations.

`login[authentication_provider_id]`

The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider). To unassociate from a known provider, specify null or an empty string.

Used to suspend or re-activate a login.

Allowed values: `active`, `suspended`

`login[declared_user_type]`

The declared intention of the user type. This can be set, but does not change any Canvas functionality with respect to their access. A user can still be a teacher, admin, student, etc. in any particular context without regard to this setting. This can be used for administrative purposes for integrations to be able to more easily identify why the user was created. Valid values are:

```
* administrative
* observer
* staff
* student
* student_other
* teacher
```

Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness

**Example Request:**

```
curl https://<canvas>/api/v1/accounts/:account_id/logins/:login_id \
  -H "Authorization: Bearer <ACCESS-TOKEN>" \
  -X PUT
```

**Example Response:**

```
{
  "id": 1,
  "user_id": 2,
  "account_id": 3,
  "unique_id": "bieber@example.com",
  "created_at": "2020-01-29T19:33:35Z",
  "sis_user_id": null,
  "integration_id": null,
  "authentication_provider_id": null,
  "workflow_state": "active",
  "declared_user_type": "teacher"
}
```

[PseudonymsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/pseudonyms_controller.rb)

`DELETE /api/v1/users/:user_id/logins/:id`

**Scope:** `url:DELETE|/api/v1/users/:user_id/logins/:id`

Delete an existing login.

**Example Request:**

```
curl https://<canvas>/api/v1/users/:user_id/logins/:login_id \
  -H "Authorization: Bearer <ACCESS-TOKEN>" \
  -X DELETE
```

**Example Response:**

```
{
  "unique_id": "bieber@example.com",
  "sis_user_id": null,
  "account_id": 1,
  "id": 12345,
  "user_id": 2
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).