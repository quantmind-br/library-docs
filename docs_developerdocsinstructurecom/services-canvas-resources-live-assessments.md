---
title: LiveAssessments | Instructure Developer Documentation Portal
url: https://developerdocs.instructure.com/services/canvas/resources/live_assessments
source: sitemap
fetched_at: 2026-02-15T09:05:03.95492-03:00
rendered_js: false
word_count: 149
summary: This document details the API endpoints and data structures for managing live assessments and their results within a course. It explains how to create, retrieve, and link assessment data to specific outcomes and users.
tags:
    - canvas-lms
    - live-assessments
    - assessment-results
    - api-endpoints
    - student-data
    - rest-api
category: api
---

Manage live assessment results

Manage live assessments

**A Result object looks like:**

```
// A pass/fail results for a student
{
  // A unique identifier for this result
"id": "42",
  // Whether the user passed or not
"passed": true,
  // When this result was recorded
"assessed_at": "2014-05-13T00:01:57-06:00",
  // Unique identifiers of objects associated with this result
"links": {"user":"42","assessor":"23","assessment":"5"}
}
```

**A ResultLinks object looks like:**

```
// Unique identifiers of objects associated with a result
{
  // A unique identifier for the user to whom this result applies
"user": "42",
  // A unique identifier for the user who created this result
"assessor": "23",
  // A unique identifier for the assessment that this result is for
"assessment": "5"
}
```

**An Assessment object looks like:**

```
// A simple assessment that collects pass/fail results for a student
{
  // A unique identifier for this live assessment
  "id": "42",
  // A client specified unique identifier for the assessment
  "key": "2014-05-27,outcome_52",
  // A human readable title for the assessment
  "title": "May 27th Reading Assessment"
}
```

[LiveAssessments::ResultsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/live_assessments/results_controller.rb)

`POST /api/v1/courses/:course_id/live_assessments/:assessment_id/results`

**Scope:** `url:POST|/api/v1/courses/:course_id/live_assessments/:assessment_id/results`

Creates live assessment results and adds them to a live assessment

**Example Request:**

```
{
  "results": [{
    "passed": false,
    "assessed_at": "2014-05-26T14:57:23-07:00",
    "links": {
      "user": "15"
    }
  },{
    "passed": true,
    "assessed_at": "2014-05-26T13:05:40-07:00",
    "links": {
      "user": "16"
    }
  }]
}
```

**Example Response:**

[LiveAssessments::ResultsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/live_assessments/results_controller.rb)

`GET /api/v1/courses/:course_id/live_assessments/:assessment_id/results`

**Scope:** `url:GET|/api/v1/courses/:course_id/live_assessments/:assessment_id/results`

Returns a paginated list of live assessment results

**Request Parameters:**

If set, restrict results to those for this user

**Example Response:**

[LiveAssessments::AssessmentsController#createarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/live_assessments/assessments_controller.rb)

`POST /api/v1/courses/:course_id/live_assessments`

**Scope:** `url:POST|/api/v1/courses/:course_id/live_assessments`

Creates or finds an existing live assessment with the given key and aligns it with the linked outcome

**Example Request:**

```
{
  "assessments": [{
    "key": "2014-05-27-Outcome-52",
    "title": "Tuesday's LiveAssessment",
    "links": {
      "outcome": "1"
    }
  }]
}
```

**Example Response:**

```
{
  "links": {
    "assessments.results": "http://example.com/courses/1/live_assessments/5/results"
  },
  "assessments": [Assessment]
}
```

[LiveAssessments::AssessmentsController#indexarrow-up-right](https://github.com/instructure/canvas-lms/blob/master/app/controllers/live_assessments/assessments_controller.rb)

`GET /api/v1/courses/:course_id/live_assessments`

**Scope:** `url:GET|/api/v1/courses/:course_id/live_assessments`

Returns a paginated list of live assessments.

**Example Response:**

```
{
  "links": {
    "assessments.results": "http://example.com/courses/1/live_assessments/{assessments.id}/results"
  },
  "assessments": [Assessment]
}
```

* * *

This documentation is generated directly from the Canvas LMS source code, available [on Githubarrow-up-right](https://github.com/instructure/canvas-lms).

Last updated 5 months ago

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.instructure.com/policies/marketing-privacy).