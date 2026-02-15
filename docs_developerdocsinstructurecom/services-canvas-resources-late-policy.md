---
title: Late Policy | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/late_policy
source: sitemap
fetched_at: 2026-02-15T09:10:27.544088-03:00
rendered_js: false
word_count: 262
summary: This document details the API endpoints and object structure for managing course late policies, including configurations for missing and late submission deductions.
tags:
    - canvas-lms
    - api-endpoints
    - late-policy
    - grading-rules
    - course-management
    - submission-deductions
category: api
---

Manage a course's late policy.

**A LatePolicy object looks like:**

```
{
  // the unique identifier for the late policy
"id": 123,
  // the unique identifier for the course
"course_id": 123,
  // whether to enable missing submission deductions
"missing_submission_deduction_enabled": true,
  // amount of percentage points to deduct
"missing_submission_deduction": 12.34,
  // whether to enable late submission deductions
"late_submission_deduction_enabled": true,
  // amount of percentage points to deduct per late_submission_interval
"late_submission_deduction": 12.34,
  // time interval for late submission deduction
"late_submission_interval": "hour",
  // whether to enable late submission minimum percent
"late_submission_minimum_percent_enabled": true,
  // the minimum score a submission can receive in percentage points
"late_submission_minimum_percent": 12.34,
  // the time at which this late policy was originally created
"created_at": "2012-07-01T23:59:00-06:00",
  // the time at which this late policy was last modified in any way
"updated_at": "2012-07-01T23:59:00-06:00"
}
```

[LatePolicyController#showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/late_policy_controller.rb)

`GET /api/v1/courses/:id/late_policy`

**Scope:** `url:GET|/api/v1/courses/:id/late_policy`

Returns the late policy for a course.

**Example Response:**

```
{
  "late_policy": LatePolicy
}
```

[LatePolicyController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/late_policy_controller.rb)

`POST /api/v1/courses/:id/late_policy`

**Scope:** `url:POST|/api/v1/courses/:id/late_policy`

Create a late policy. If the course already has a late policy, a bad\_request is returned since there can only be one late policy per course.

**Request Parameters:**

`late_policy[missing_submission_deduction_enabled]`

Whether to enable the missing submission deduction late policy.

`late_policy[missing_submission_deduction]`

How many percentage points to deduct from a missing submission.

`late_policy[late_submission_deduction_enabled]`

Whether to enable the late submission deduction late policy.

`late_policy[late_submission_deduction]`

How many percentage points to deduct per the late submission interval.

`late_policy[late_submission_interval]`

The interval for late policies.

`late_policy[late_submission_minimum_percent_enabled]`

Whether to enable the late submission minimum percent for a late policy.

`late_policy[late_submission_minimum_percent]`

The minimum grade a submissions can have in percentage points.

**Example Response:**

```
{
  "late_policy": LatePolicy
}
```

[LatePolicyController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/late_policy_controller.rb)

`PATCH /api/v1/courses/:id/late_policy`

**Scope:** `url:PATCH|/api/v1/courses/:id/late_policy`

Patch a late policy. No body is returned upon success.

**Request Parameters:**

`late_policy[missing_submission_deduction_enabled]`

Whether to enable the missing submission deduction late policy.

`late_policy[missing_submission_deduction]`

How many percentage points to deduct from a missing submission.

`late_policy[late_submission_deduction_enabled]`

Whether to enable the late submission deduction late policy.

`late_policy[late_submission_deduction]`

How many percentage points to deduct per the late submission interval.

`late_policy[late_submission_interval]`

The interval for late policies.

`late_policy[late_submission_minimum_percent_enabled]`

Whether to enable the late submission minimum percent for a late policy.

`late_policy[late_submission_minimum_percent]`

The minimum grade a submissions can have in percentage points.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).