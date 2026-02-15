---
title: Grading Periods | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/grading_periods
source: sitemap
fetched_at: 2026-02-15T09:07:49.267019-03:00
rendered_js: false
word_count: 341
summary: This document provides a technical reference for the Canvas LMS Grading Periods API, detailing endpoints for listing, retrieving, updating, and deleting grading period data.
tags:
    - canvas-lms
    - rest-api
    - grading-periods
    - api-reference
    - course-management
    - grading-period-sets
category: api
---

Manage grading periods

**A GradingPeriod object looks like:**

```
{
  // The unique identifier for the grading period.
"id": 1023,
  // The title for the grading period.
"title": "First Block",
  // The start date of the grading period.
"start_date": "2014-01-07T15:04:00Z",
  // The end date of the grading period.
"end_date": "2014-05-07T17:07:00Z",
  // Grades can only be changed before the close date of the grading period.
"close_date": "2014-06-07T17:07:00Z",
  // A weight value that contributes to the overall weight of a grading period set
  // which is used to calculate how much assignments in this period contribute to
  // the total grade
"weight": 33.33,
  // If true, the grading period's close_date has passed.
"is_closed": true
}
```

[GradingPeriodsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_periods_controller.rb)

`GET /api/v1/accounts/:account_id/grading_periods`

**Scope:** `url:GET|/api/v1/accounts/:account_id/grading_periods`

`GET /api/v1/courses/:course_id/grading_periods`

**Scope:** `url:GET|/api/v1/courses/:course_id/grading_periods`

Returns the paginated list of grading periods for the current course.

**Example Response:**

```
{
  "grading_periods": [GradingPeriod]
}
```

[GradingPeriodsController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_periods_controller.rb)

`GET /api/v1/courses/:course_id/grading_periods/:id`

**Scope:** `url:GET|/api/v1/courses/:course_id/grading_periods/:id`

Returns the grading period with the given id

**Example Response:**

```
{
  "grading_periods": [GradingPeriod]
}
```

[GradingPeriodsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_periods_controller.rb)

`PUT /api/v1/courses/:course_id/grading_periods/:id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/grading_periods/:id`

Update an existing grading period.

**Request Parameters:**

`grading_periods[][start_date]`

The date the grading period starts.

`grading_periods[][end_date]`

`grading_periods[][weight]`

A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade

**Example Response:**

```
{
  "grading_periods": [GradingPeriod]
}
```

[GradingPeriodsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_periods_controller.rb)

`DELETE /api/v1/courses/:course_id/grading_periods/:id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/grading_periods/:id`

`DELETE /api/v1/accounts/:account_id/grading_periods/:id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/grading_periods/:id`

**204 No Content** response code is returned if the deletion was successful.

[GradingPeriodsController#batch\_updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_periods_controller.rb)

`PATCH /api/v1/courses/:course_id/grading_periods/batch_update`

**Scope:** `url:PATCH|/api/v1/courses/:course_id/grading_periods/batch_update`

`PATCH /api/v1/grading_period_sets/:set_id/grading_periods/batch_update`

**Scope:** `url:PATCH|/api/v1/grading_period_sets/:set_id/grading_periods/batch_update`

Update multiple grading periods

**Request Parameters:**

The id of the grading period set.

The id of the grading period. If the id parameter does not exist, a new grading period will be created.

The title of the grading period. The title is required for creating a new grading period, but not for updating an existing grading period.

`grading_periods[][start_date]`

The date the grading period starts. The start\_date is required for creating a new grading period, but not for updating an existing grading period.

`grading_periods[][end_date]`

The date the grading period ends. The end\_date is required for creating a new grading period, but not for updating an existing grading period.

`grading_periods[][close_date]`

The date after which grades can no longer be changed for a grading period. The close\_date is required for creating a new grading period, but not for updating an existing grading period.

`grading_periods[][weight]`

A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade

**Example Response:**

```
{
  "grading_periods": [GradingPeriod]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).