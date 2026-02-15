---
title: Temporary Enrollment Pairings | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings
source: sitemap
fetched_at: 2026-02-15T09:08:11.545107-03:00
rendered_js: false
word_count: 210
summary: Technical documentation for the Canvas LMS Temporary Enrollment Pairings API, detailing the endpoints and object structures required to manage temporary enrollment associations within a root account.
tags:
    - canvas-lms
    - api-documentation
    - enrollment-pairings
    - rest-api
    - account-management
category: api
---

circle-exclamation

**Welcome to Our New API Docs!** This is the new home for all things API (previously at [Canvas LMS REST API Documentationarrow-up-right](https://api.instructure.com)).

## [hashtag](#temporary-enrollment-pairings-api) Temporary Enrollment Pairings API

**A TemporaryEnrollmentPairing object looks like:**

```
// A pairing unique to that enrollment period given to a recipient of that
// temporary enrollment.
{
  // the ID of the temporary enrollment pairing
"id": 1,
  // The current status of the temporary enrollment pairing
"workflow_state": "active"
}
```

### [hashtag](#method.temporary_enrollment_pairings_api.index) [List temporary enrollment pairings](https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings#method.temporary_enrollment_pairings_api.index)

[TemporaryEnrollmentPairingsApiController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

`GET /api/v1/accounts/:account_id/temporary_enrollment_pairings`

**Scope:** `url:GET|/api/v1/accounts/:account_id/temporary_enrollment_pairings`

Returns the list of temporary enrollment pairings for a root account.

Returns a list of [TemporaryEnrollmentPairing](https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings#temporaryenrollmentpairing) objects.

### [hashtag](#method.temporary_enrollment_pairings_api.show) [Get a single temporary enrollment pairing](https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings#method.temporary_enrollment_pairings_api.show)

[TemporaryEnrollmentPairingsApiController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

`GET /api/v1/accounts/:account_id/temporary_enrollment_pairings/:id`

**Scope:** `url:GET|/api/v1/accounts/:account_id/temporary_enrollment_pairings/:id`

Returns the temporary enrollment pairing with the given id.

Returns a [TemporaryEnrollmentPairing](https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings#temporaryenrollmentpairing) object.

### [hashtag](#method.temporary_enrollment_pairings_api.new) [New TemporaryEnrollmentPairing](https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings#method.temporary_enrollment_pairings_api.new)

[TemporaryEnrollmentPairingsApiController#newarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

`GET /api/v1/accounts/:account_id/temporary_enrollment_pairings/new`

**Scope:** `url:GET|/api/v1/accounts/:account_id/temporary_enrollment_pairings/new`

Initialize an unsaved Temporary Enrollment Pairing.

Returns a [TemporaryEnrollmentPairing](https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings#temporaryenrollmentpairing) object.

### [hashtag](#method.temporary_enrollment_pairings_api.create) [Create Temporary Enrollment Pairing](https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings#method.temporary_enrollment_pairings_api.create)

[TemporaryEnrollmentPairingsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

`POST /api/v1/accounts/:account_id/temporary_enrollment_pairings`

**Scope:** `url:POST|/api/v1/accounts/:account_id/temporary_enrollment_pairings`

Create a Temporary Enrollment Pairing.

**Request Parameters:**

Parameter

Type

Description

`workflow_state`

`string`

The workflow state of the temporary enrollment pairing.

`ending_enrollment_state`

`string`

The ending enrollment state to be given to each associated enrollment when the enrollment period has been reached. Defaults to “deleted” if no value is given. Accepted values are “deleted”, “completed”, and “inactive”.

Allowed values: `deleted`, `completed`, `inactive`

Returns a [TemporaryEnrollmentPairing](https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings#temporaryenrollmentpairing) object.

### [hashtag](#method.temporary_enrollment_pairings_api.destroy) [Delete Temporary Enrollment Pairing](https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings#method.temporary_enrollment_pairings_api.destroy)

[TemporaryEnrollmentPairingsApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/temporary_enrollment_pairings_api_controller.rb)

`DELETE /api/v1/accounts/:account_id/temporary_enrollment_pairings/:id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/temporary_enrollment_pairings/:id`

Delete a temporary enrollment pairing

Returns a [TemporaryEnrollmentPairing](https://developerdocs.instructure.com/services/canvas/resources/temporary_enrollment_pairings#temporaryenrollmentpairing) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).