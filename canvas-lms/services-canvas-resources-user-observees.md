---
title: User Observees | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/user_observees
source: sitemap
fetched_at: 2026-02-15T09:08:08.514306-03:00
rendered_js: false
word_count: 585
summary: This document defines the API endpoints for managing relationships between observers and observees, including methods for listing, creating, updating, and deleting observation links and generating pairing codes.
tags:
    - canvas-lms
    - api-endpoints
    - user-management
    - observers
    - observees
    - pairing-codes
category: api
---

API for managing linked observers and observees

**A PairingCode object looks like:**

```
// A code used for linking a user to a student to observe them.
{
  // The ID of the user.
"user_id": 2,
  // The actual code to be sent to other APIs
"code": "abc123",
  // When the code expires
"expires_at": "2012-05-30T17:45:25Z",
  // The current status of the code
"workflow_state": "active"
}
```

[UserObserveesController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

`GET /api/v1/users/:user_id/observees`

**Scope:** `url:GET|/api/v1/users/:user_id/observees`

A paginated list of users that the given user is observing. This endpoint returns users linked to the observer at the account level (such that the observer is automatically enrolled in observees’ courses); it doesn’t return one-off observer enrollments from individual courses.

**Note:** all users are allowed to list their own observees. Administrators can list other users’ observees.

The returned observees will include an attribute “observation\_link\_root\_account\_ids”, a list of ids for the root accounts the observer and observee are linked on. The observer will only be able to observe in courses associated with these root accounts.

**Request Parameters:**

- “avatar\_url”: Optionally include avatar\_url.

Allowed values: `avatar_url`

**Example Request:**

```
curl https://<canvas>/api/v1/users/<user_id>/observees \
     -X GET \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

[UserObserveesController#observersarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

`GET /api/v1/users/:user_id/observers`

**Scope:** `url:GET|/api/v1/users/:user_id/observers`

A paginated list of observers linked to a given user.

**Note:** all users are allowed to list their own observers. Administrators can list other users’ observers.

The returned observers will include an attribute “observation\_link\_root\_account\_ids”, a list of ids for the root accounts the observer and observee are linked on. The observer will only be able to observe in courses associated with these root accounts.

**Request Parameters:**

- “avatar\_url”: Optionally include avatar\_url.

Allowed values: `avatar_url`

**Example Request:**

```
curl https://<canvas>/api/v1/users/<user_id>/observers \
     -X GET \
     -H 'Authorization: Bearer <token>'
```

Returns a list of [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) objects.

[UserObserveesController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

`POST /api/v1/users/:user_id/observees`

**Scope:** `url:POST|/api/v1/users/:user_id/observees`

Register the given user to observe another user, given the observee’s credentials.

**Note:** all users are allowed to add their own observees, given the observee’s credentials or access token are provided. Administrators can add observees given credentials, access token or the [observee’s id](https://developerdocs.instructure.com/services/canvas/resources/user_observees#method.user_observees.update).

**Request Parameters:**

The login id for the user to observe. Required if access\_token is omitted.

The password for the user to observe. Required if access\_token is omitted.

The access token for the user to observe. Required if `observee[unique_id]` or `observee[password]` are omitted.

A generated pairing code for the user to observe. Required if the Observer pairing code feature flag is enabled

The ID for the root account to associate with the observation link. Defaults to the current domain account. If ‘all’ is specified, a link will be created for each root account associated to both the observer and observee.

**Example Request:**

```
curl https://<canvas>/api/v1/users/<user_id>/observees \
     -X POST \
     -H 'Authorization: Bearer <token>' \
     -F 'observee[unique_id]=UNIQUE_ID' \
     -F 'observee[password]=PASSWORD'
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[UserObserveesController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

`GET /api/v1/users/:user_id/observees/:observee_id`

**Scope:** `url:GET|/api/v1/users/:user_id/observees/:observee_id`

Gets information about an observed user.

**Note:** all users are allowed to view their own observees.

**Example Request:**

```
curl https://<canvas>/api/v1/users/<user_id>/observees/<observee_id> \
     -X GET \
     -H 'Authorization: Bearer <token>'
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[UserObserveesController#show\_observerarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

`GET /api/v1/users/:user_id/observers/:observer_id`

**Scope:** `url:GET|/api/v1/users/:user_id/observers/:observer_id`

Gets information about an observer.

**Note:** all users are allowed to view their own observers.

**Example Request:**

```
curl https://<canvas>/api/v1/users/<user_id>/observers/<observer_id> \
     -X GET \
     -H 'Authorization: Bearer <token>'
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[UserObserveesController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

`PUT /api/v1/users/:user_id/observees/:observee_id`

**Scope:** `url:PUT|/api/v1/users/:user_id/observees/:observee_id`

Registers a user as being observed by the given user.

**Request Parameters:**

The ID for the root account to associate with the observation link. If not specified, a link will be created for each root account associated to both the observer and observee.

**Example Request:**

```
curl https://<canvas>/api/v1/users/<user_id>/observees/<observee_id> \
     -X PUT \
     -H 'Authorization: Bearer <token>'
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[UserObserveesController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/user_observees_controller.rb)

`DELETE /api/v1/users/:user_id/observees/:observee_id`

**Scope:** `url:DELETE|/api/v1/users/:user_id/observees/:observee_id`

Unregisters a user as being observed by the given user.

**Request Parameters:**

If specified, only removes the link for the given root account

**Example Request:**

```
curlhttps://<canvas>/api/v1/users/<user_id>/observees/<observee_id>\
-XDELETE\
-H'Authorization: Bearer <token>'
```

Returns an [User](https://developerdocs.instructure.com/services/canvas/resources/users#user) object.

[ObserverPairingCodesApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/observer_pairing_codes_api_controller.rb)

`POST /api/v1/users/:user_id/observer_pairing_codes`

**Scope:** `url:POST|/api/v1/users/:user_id/observer_pairing_codes`

If the user is a student, will generate a code to be used with self registration or observees APIs to link another user to this student.

Returns a [PairingCode](https://developerdocs.instructure.com/services/canvas/resources/user_observees#pairingcode) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).