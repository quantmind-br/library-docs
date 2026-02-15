---
title: Grading Period Sets | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/grading_period_sets
source: sitemap
fetched_at: 2026-02-15T09:07:47.958073-03:00
rendered_js: false
word_count: 223
summary: This document provides API documentation for managing grading period sets in Canvas LMS, including instructions for listing, creating, updating, and deleting these objects.
tags:
    - canvas-lms
    - rest-api
    - grading-period-sets
    - account-management
    - grading
category: api
---

Manage grading period sets

**A GradingPeriodSets object looks like:**

```
{
  // The title of the grading period set.
"title": "Hello World",
  // If true, the grading periods in the set are weighted.
"weighted": true,
  // If true, the totals for all grading periods in the set are displayed.
"display_totals_for_all_grading_periods": true
}
```

[GradingPeriodSetsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_period_sets_controller.rb)

`GET /api/v1/accounts/:account_id/grading_period_sets`

**Scope:** `url:GET|/api/v1/accounts/:account_id/grading_period_sets`

Returns the paginated list of grading period sets

**Example Response:**

```
{
  "grading_period_set": [GradingPeriodGroup]
}
```

[GradingPeriodSetsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_period_sets_controller.rb)

`POST /api/v1/accounts/:account_id/grading_period_sets`

**Scope:** `url:POST|/api/v1/accounts/:account_id/grading_period_sets`

Create and return a new grading period set

**Request Parameters:**

A list of associated term ids for the grading period set

`grading_period_set[title]`

The title of the grading period set

`grading_period_set[weighted]`

A boolean to determine whether the grading periods in the set are weighted

`grading_period_set[display_totals_for_all_grading_periods]`

A boolean to determine whether the totals for all grading periods in the set are displayed

**Example Response:**

```
{
  "grading_period_set": [GradingPeriodGroup]
}
```

[GradingPeriodSetsController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_period_sets_controller.rb)

`PATCH /api/v1/accounts/:account_id/grading_period_sets/:id`

**Scope:** `url:PATCH|/api/v1/accounts/:account_id/grading_period_sets/:id`

Update an existing grading period set

**204 No Content** response code is returned if the update was successful.

**Request Parameters:**

A list of associated term ids for the grading period set

`grading_period_set[][title]`

The title of the grading period set

`grading_period_set[][weighted]`

A boolean to determine whether the grading periods in the set are weighted

`grading_period_set[][display_totals_for_all_grading_periods]`

A boolean to determine whether the totals for all grading periods in the set are displayed

[GradingPeriodSetsController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_period_sets_controller.rb)

`DELETE /api/v1/accounts/:account_id/grading_period_sets/:id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/grading_period_sets/:id`

**204 No Content** response code is returned if the deletion was successful.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).