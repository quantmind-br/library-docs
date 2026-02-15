---
title: Grading Standards | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/grading_standards
source: sitemap
fetched_at: 2026-02-15T09:07:49.477086-03:00
rendered_js: false
word_count: 480
summary: This document defines the data structures and API endpoints for managing grading standards and schemes within a learning management system. It details how to create, list, retrieve, and update grading criteria at both the course and account levels.
tags:
    - api-reference
    - canvas-lms
    - grading-standards
    - grading-schemes
    - rest-api
    - course-administration
category: api
---

**A GradingSchemeEntry object looks like:**

```
{
  // The name for an entry value within a GradingStandard that describes the range
  // of the value
"name": "A",
  // The value for the name of the entry within a GradingStandard. The entry
  // represents the lower bound of the range for the entry. This range includes
  // the value up to the next entry in the GradingStandard, or the maximum value
  // for the scheme if there is no upper bound. The lowest value will have a lower
  // bound range of 0.
"value": 0.9,
  // The value that will be used to compare against a grade. For percentage based
  // grading schemes, this is a number from 0 - 100 representing a percent. For
  // point based grading schemes, this is the lower bound of points to achieve the
  // grade.
"calculated_value": 90
}
```

**A GradingStandard object looks like:**

```
{
  // the title of the grading standard
  "title": "Account Standard",
  // the id of the grading standard
  "id": 1,
  // the context this standard is associated with, either 'Account' or 'Course'
  "context_type": "Account",
  // the id for the context either the Account or Course id
  "context_id": 1,
  // whether this is a points-based standard
  "points_based": false,
  // the factor by which to scale a score. 1 for percentage based schemss and the
  // max value of points for points based schemes. This number cannot be changed
  // for percentage based schemes.
  "scaling_factor": 1.0,
  // A list of GradingSchemeEntry that make up the Grading Standard as an array of
  // values with the scheme name and value
  "grading_scheme": [{"name":"A","value":0.9}, {"name":"B","value":0.8}, {"name":"C","value":0.7}, {"name":"D","value":0.6}]
}
```

[GradingStandardsApiController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_standards_api_controller.rb)

`POST /api/v1/accounts/:account_id/grading_standards`

**Scope:** `url:POST|/api/v1/accounts/:account_id/grading_standards`

`POST /api/v1/courses/:course_id/grading_standards`

**Scope:** `url:POST|/api/v1/courses/:course_id/grading_standards`

Create a new grading standard

**Request Parameters:**

The title for the Grading Standard.

Whether or not a grading scheme is points based. Defaults to false.

The factor by which to scale a percentage into a points based scheme grade. This is the maximum number of points possible in the grading scheme. Defaults to 1. Not required for percentage based grading schemes.

`grading_scheme_entry[][name]`

The name for an entry value within a GradingStandard that describes the range of the value e.g. A-

`grading_scheme_entry[][value]`

The value for the name of the entry within a GradingStandard. The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. e.g. 93

**Example Request:**

```
curl https://<canvas>/api/v1/courses/<course_id>/grading_standards \
  -X POST \
  -H 'Authorization: Bearer <token>' \
  -d 'title=New standard name' \
  -d 'points_based=false' \
  -d 'scaling_factor=1.0' \
  -d 'grading_scheme_entry[][name]=A' \
  -d 'grading_scheme_entry[][value]=94' \
  -d 'grading_scheme_entry[][name]=A-' \
  -d 'grading_scheme_entry[][value]=90' \
  -d 'grading_scheme_entry[][name]=B+' \
  -d 'grading_scheme_entry[][value]=87' \
  -d 'grading_scheme_entry[][name]=B' \
  -d 'grading_scheme_entry[][value]=84' \
  -d 'grading_scheme_entry[][name]=B-' \
  -d 'grading_scheme_entry[][value]=80' \
  -d 'grading_scheme_entry[][name]=C+' \
  -d 'grading_scheme_entry[][value]=77' \
  -d 'grading_scheme_entry[][name]=C' \
  -d 'grading_scheme_entry[][value]=74' \
  -d 'grading_scheme_entry[][name]=C-' \
  -d 'grading_scheme_entry[][value]=70' \
  -d 'grading_scheme_entry[][name]=D+' \
  -d 'grading_scheme_entry[][value]=67' \
  -d 'grading_scheme_entry[][name]=D' \
  -d 'grading_scheme_entry[][value]=64' \
  -d 'grading_scheme_entry[][name]=D-' \
  -d 'grading_scheme_entry[][value]=61' \
  -d 'grading_scheme_entry[][name]=F' \
  -d 'grading_scheme_entry[][value]=0'
```

**Example Response:**

```
{
  "title": "New standard name",
  "id": 1,
  "context_id": 1,
  "context_type": "Course",
  "grading_scheme": [
    {"name": "A", "value": 0.9},
    {"name": "B", "value": 0.8}
  ]
}
```

Returns a [GradingStandard](https://developerdocs.instructure.com/services/canvas/resources/grading_standards#gradingstandard) object.

[GradingStandardsApiController#context\_indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_standards_api_controller.rb)

`GET /api/v1/courses/:course_id/grading_standards`

**Scope:** `url:GET|/api/v1/courses/:course_id/grading_standards`

`GET /api/v1/accounts/:account_id/grading_standards`

**Scope:** `url:GET|/api/v1/accounts/:account_id/grading_standards`

Returns the paginated list of grading standards for the given context that are visible to the user.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/1/grading_standards \
  -H 'Authorization: Bearer <token>'
```

Returns a list of [GradingStandard](https://developerdocs.instructure.com/services/canvas/resources/grading_standards#gradingstandard) objects.

[GradingStandardsApiController#context\_showarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_standards_api_controller.rb)

`GET /api/v1/courses/:course_id/grading_standards/:grading_standard_id`

**Scope:** `url:GET|/api/v1/courses/:course_id/grading_standards/:grading_standard_id`

`GET /api/v1/accounts/:account_id/grading_standards/:grading_standard_id`

**Scope:** `url:GET|/api/v1/accounts/:account_id/grading_standards/:grading_standard_id`

Returns a grading standard for the given context that is visible to the user.

**Example Request:**

```
curl https://<canvas>/api/v1/courses/1/grading_standards/5 \
  -H 'Authorization: Bearer <token>'
```

Returns a [GradingStandard](https://developerdocs.instructure.com/services/canvas/resources/grading_standards#gradingstandard) object.

[GradingStandardsApiController#updatearrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_standards_api_controller.rb)

`PUT /api/v1/courses/:course_id/grading_standards/:grading_standard_id`

**Scope:** `url:PUT|/api/v1/courses/:course_id/grading_standards/:grading_standard_id`

`PUT /api/v1/accounts/:account_id/grading_standards/:grading_standard_id`

**Scope:** `url:PUT|/api/v1/accounts/:account_id/grading_standards/:grading_standard_id`

Updates the grading standard with the given id

If the grading standard has been used for grading, only the title can be updated. The data, points\_based, and scaling\_factor cannot be modified once the grading standard has been used to grade assignments.

**Request Parameters:**

The title for the Grading Standard

Whether or not a grading scheme is points based. Defaults to false.

The factor by which to scale a percentage into a points based scheme grade. This is the maximum number of points possible in the grading scheme. Defaults to 1. Not required for percentage based grading schemes.

`grading_scheme_entry[][name]`

The name for an entry value within a GradingStandard that describes the range of the value e.g. A-

`grading_scheme_entry[][value]`

The value for the name of the entry within a GradingStandard. The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. e.g. 93

**Example Request:**

```
curlhttps://<canvas>/api/v1/courses/1/grading_standards/5\
-XPUT\
-H'Authorization: Bearer <token>'\
-d'title=Updated+Grading+Standard'
-d'points_based=false'\
-d'scaling_factor=1.0'\
-d'grading_scheme_entry[][name]=A'\
-d'grading_scheme_entry[][value]=94'\
-d'grading_scheme_entry[][name]=A-'\
-d'grading_scheme_entry[][value]=90'\
-d'grading_scheme_entry[][name]=B+'\
-d'grading_scheme_entry[][value]=87'\
-d'grading_scheme_entry[][name]=B'\
-d'grading_scheme_entry[][value]=84'\
-d'grading_scheme_entry[][name]=B-'\
-d'grading_scheme_entry[][value]=80'\
-d'grading_scheme_entry[][name]=C+'\
-d'grading_scheme_entry[][value]=77'\
-d'grading_scheme_entry[][name]=C'\
-d'grading_scheme_entry[][value]=74'\
-d'grading_scheme_entry[][name]=C-'\
-d'grading_scheme_entry[][value]=70'\
-d'grading_scheme_entry[][name]=D+'\
-d'grading_scheme_entry[][value]=67'\
-d'grading_scheme_entry[][name]=D'\
-d'grading_scheme_entry[][value]=64'\
-d'grading_scheme_entry[][name]=D-'\
-d'grading_scheme_entry[][value]=61'\
-d'grading_scheme_entry[][name]=F'\
-d'grading_scheme_entry[][value]=0'
```

Returns a [GradingStandard](https://developerdocs.instructure.com/services/canvas/resources/grading_standards#gradingstandard) object.

[GradingStandardsApiController#destroyarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/grading_standards_api_controller.rb)

`DELETE /api/v1/courses/:course_id/grading_standards/:grading_standard_id`

**Scope:** `url:DELETE|/api/v1/courses/:course_id/grading_standards/:grading_standard_id`

`DELETE /api/v1/accounts/:account_id/grading_standards/:grading_standard_id`

**Scope:** `url:DELETE|/api/v1/accounts/:account_id/grading_standards/:grading_standard_id`

Deletes the grading standard with the given id

**Example Request:**

```
curlhttps://<canvas>/api/v1/courses/1/grading_standards/5\
-XDELETE\
-H'Authorization: Bearer <token>'
```

Returns a [GradingStandard](https://developerdocs.instructure.com/services/canvas/resources/grading_standards#gradingstandard) object.

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).